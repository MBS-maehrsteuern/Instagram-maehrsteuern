"""Schritt-Reel bauen („In X Schritten“): animierte Bilder zu Loris' Stimme, Zeiten aus der Sprache.
    python3 vorlagen/system/schnitt/schritt_reel_bauen.py --stimme post/ton/stimme.wav --skript vorlagen/system/schnitt/schritt_reel_A_einspruch.json --ziel out.mp4
    Stummer Test (nur zum Ansehen, NICHT zum Veröffentlichen): --stumm statt --stimme → erfundene Wortzeiten aus dem Feld "sprechtext" des Skripts.
    Nur Einzelbilder prüfen: --probe 1,6,12 (PNG) oder --kontakt bogen.png (8 Bilder, je 540 px breit; Zeiten mit --probe wählbar).

Skript-JSON OHNE Zeiten. Szenen wie in premium/schritt_reel.html (hook, schrittleiste, untertitel, zaehler, tippen, sprechblase, quelle, liste, cta).
  Zeitangaben je Szene:  ab_s | ab_anker (+ ab_versatz)   und   bis_s | bis_anker (+ bis_versatz) | "bis":"ende"
  Anker = gesprochene Wörter, z. B. {"ab_anker":"Schritt zwei"} → Beginn des ersten dieser Wörter in der Stimme (unscharf, Groß/Klein egal).
  untertitel: "text":"Leg den *Bescheid* daneben" – die Wörter zwischen *…* werden grün; ab/bis ergeben sich aus den gesprochenen Wörtern, wenn nicht angegeben.
  tippen/liste: je Zeile "anker" (sonst gestaffelt). Oberste Felder: "schritte":[{"anker","titel"}], "sprechtext" (nur --stumm), "ende_nach" (Sekunden nach dem letzten Wort).
Ablauf: Stimme → 16 kHz mono (ffmpeg, wave) → faster-whisper (small, int8, de, Wortzeiten) → Anker auflösen → premium/schritt_reel.html (Playwright, premium/rendern.mjs) → mp4 mit Stimme."""
import argparse, difflib, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier))
from hook_triple_bauen import erkennen, abgleichen, norm, sh   # Erkennung und unscharfer Abgleich wiederverwenden
PREMIUM = hier.parent / "premium"

def tok(text):
    """Text → Wörter ohne Sternchen-Markierung: [(wort, markiert)]"""
    out = []
    for teil in re.split(r"(\*[^*]+\*)", text):
        if not teil: continue
        mark = teil.startswith("*")
        out += [(w, mark) for w in teil.strip("*").split()]
    return out

def erfundene_zeiten(sprechtext):
    """Nur für den stummen Test: Wortzeiten schätzen (0,08 s + 0,035 s je Buchstabe, Pausen nach Satzzeichen)."""
    t, out = 0.4, []
    for w in sprechtext.split():
        if re.fullmatch(r"\[[\d.]+\]", w): t += float(w.strip("[]")); continue   # [2.2] = Pause in Sekunden
        d = 0.08 + 0.035 * len(w)
        out.append((w.strip(), t, t + d)); t += d + 0.03
        if w.endswith((".", "?", "!")): t += 0.3
        elif w.endswith((":", ",")): t += 0.12
    return out

class Zeiten:
    def __init__(self, erkannt): self.w = erkannt
    def finde(self, phrase, ab=0):
        """Index des ersten Wortes der Phrase: erster Treffer mit Ähnlichkeit ≥ 0,9, sonst ≥ 0,75, sonst bester ≥ 0,55."""
        ts = [norm(x) for x in phrase.split() if norm(x)]
        sc = []
        for i in range(ab, len(self.w) - len(ts) + 1):
            sc.append((sum(difflib.SequenceMatcher(None, ts[j], norm(self.w[i + j][0])).ratio() for j in range(len(ts))) / len(ts), i))
        for grenze in (0.9, 0.75):      # erst fast exakte, dann unscharfe Treffer (sonst passt „drei“ zu „eins“)
            for w, i in sc:
                if w >= grenze: return i
        best, bi = max(sc, default=(0.0, None))
        if bi is None or best < 0.55: raise SystemExit(f"Anker nicht in der Stimme gefunden: „{phrase}“ (bester Wert {best:.2f})")
        return bi
    def zeit(self, phrase): return self.w[self.finde(phrase)][1]

def aufloesen(skript, erkannt, vorlauf=0.05):
    Z = Zeiten(erkannt)
    ende = round(erkannt[-1][2] + skript.get("ende_nach", 1.0), 2)
    szenen = []
    for s in skript["szenen"]:
        typ = s["typ"]; ab = bis = None
        o = {k: v for k, v in s.items() if k not in ("ab_s", "ab_anker", "ab_versatz", "bis_s", "bis_anker", "bis_versatz", "bis", "zeilen", "anker", "titel_anker")
             and not (k == "text" and typ == "untertitel")}
        if "ab_s" in s: ab = s["ab_s"]
        elif "ab_anker" in s: ab = Z.zeit(s["ab_anker"]) + s.get("ab_versatz", 0) - vorlauf
        if typ == "untertitel":
            wt = tok(s["text"]); i0 = Z.finde(s.get("ab_anker") or " ".join(w for w, _ in wt[:3]))
            zt = abgleichen([w for w, _ in wt], erkannt[i0:i0 + len(wt) + 4])
            o["woerter"] = [{"w": w, "s": round(max(0, a - vorlauf), 3), "e": round(e, 3), **({"akzent": "gruen"} if m else {})} for (w, m), (a, e) in zip(wt, zt)]
            if ab is None: ab = o["woerter"][0]["s"] - 0.1
            if "bis_anker" not in s and "bis_s" not in s and "bis" not in s: bis = o["woerter"][-1]["e"] + 0.5 + s.get("bis_versatz", 0)
        elif typ == "hook":
            flach = [(zi, w) for zi, z in enumerate(s["zeilen"]) for w in z["woerter"]]
            texte = [w if isinstance(w, str) else w["w"] for _, w in flach]
            zt = abgleichen(texte, erkannt)
            zl = [{"words": [], **({"icon": z["icon"]} if z.get("icon") else {})} for z in s["zeilen"]]
            for (zi, w), t, (a, e) in zip(flach, texte, zt):
                d = {"w": t, "s": round(max(0, a - vorlauf), 3), "e": round(e, 3)}
                if not isinstance(w, str): d.update({k: w[k] for k in ("akzent", "gross") if w.get(k)})
                zl[zi]["words"].append(d)
            o["zeilen"] = zl
            if ab is None: ab = 0.0
        elif typ in ("tippen", "liste"):
            zl = []
            for n, z in enumerate(s["zeilen"]):
                d = {k: v for k, v in z.items() if k != "anker"}
                d["s"] = round((Z.zeit(z["anker"]) - vorlauf) if "anker" in z else (ab or 0) + 0.25 + 0.5 * n, 3)
                zl.append(d)
            o["zeilen"] = zl
            if ab is not None: ab = min(ab, min(z["s"] for z in zl) - 0.1) if typ == "tippen" else ab
        elif typ == "schrittleiste":
            st = [{"ab": round(Z.zeit(x["anker"]) - 0.2, 3), "titel": x["titel"]} for x in skript["schritte"]]
            o["schritte"] = st; o["n"] = len(st)
            if ab is None: ab = st[0]["ab"] - 0.1
        if bis is None:
            if s.get("bis") == "ende": bis = ende
            elif "bis_s" in s: bis = s["bis_s"]
            elif "bis_anker" in s: bis = Z.zeit(s["bis_anker"]) + s.get("bis_versatz", 0)
            else: raise SystemExit(f"Szene {typ}: kein Ende (bis_s/bis_anker/bis) angegeben")
        if ab is None: raise SystemExit(f"Szene {typ}: kein Anfang (ab_s/ab_anker) angegeben")
        if typ in ("liste", "tippen"):
            for z in o["zeilen"]: z["s"] = max(z["s"], ab + 0.05)
        o["ab"], o["bis"] = round(max(0, ab), 3), round(min(bis, ende), 3)
        szenen.append(o)
    # Zeitliche Reihenfolge für Fehlersuche; die Vorlage braucht sie nicht
    return {"dauer": ende, "szenen": szenen}

def kontaktbogen(bilder, ziel, breite=540):
    from PIL import Image
    ims = [Image.open(b).convert("RGB") for b in bilder]; h = int(breite * 1920 / 1080)
    ims = [i.resize((breite, h), Image.LANCZOS) for i in ims]; sp = min(4, len(ims)); ze = (len(ims) + sp - 1) // sp
    bogen = Image.new("RGB", (sp * breite + (sp + 1) * 8, ze * h + (ze + 1) * 8), (40, 40, 40))
    for n, im in enumerate(ims): bogen.paste(im, (8 + (n % sp) * (breite + 8), 8 + (n // sp) * (h + 8)))
    bogen.save(ziel)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stimme", help="Stimmen-WAV, Zeit 0 = Reel-Anfang"); ap.add_argument("--stumm", action="store_true", help="Test ohne Stimme (erfundene Zeiten, kein Ton) – nicht veröffentlichen")
    ap.add_argument("--skript", required=True); ap.add_argument("--ziel", help="Ausgabe-mp4")
    ap.add_argument("--probe", help="Zeiten in Sekunden, z. B. 1,6,12: nur diese Einzelbilder (PNG) in --behalte bzw. neben --ziel")
    ap.add_argument("--kontakt", help="Kontaktbogen-PNG (8 Bilder zu den --probe-Zeiten, sonst gleichmäßig verteilt)")
    ap.add_argument("--behalte", help="Ordner für Zeitkonfiguration (reel_zeiten.json) und Probebilder")
    ap.add_argument("--vorlauf", type=float, default=0.05)
    a = ap.parse_args()
    if bool(a.stimme) == a.stumm: ap.error("entweder --stimme oder --stumm")
    if not (a.ziel or a.probe or a.kontakt): ap.error("--ziel, --probe oder --kontakt nötig")
    skript = json.loads(Path(a.skript).read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        erkannt = erfundene_zeiten(skript["sprechtext"]) if a.stumm else erkennen(Path(a.stimme).resolve(), tmp, 600)
        print("Wörter:", len(erkannt), f"· Länge {erkannt[-1][2]:.1f} s")
        R = aufloesen(skript, erkannt, a.vorlauf)
        keep = Path(a.behalte) if a.behalte else (Path(a.ziel).resolve().parent if a.ziel else (Path(a.kontakt).resolve().parent))
        keep.mkdir(parents=True, exist_ok=True)
        (keep / "reel_zeiten.json").write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
        seite = PREMIUM / f"_schritt_tmp_{tmp.name}.html"
        try:
            html = (PREMIUM / "schritt_reel.html").read_text(encoding="utf-8")
            seite.write_text(html.replace("<!--REEL-->", f"<script>window.REEL={json.dumps(R, ensure_ascii=False)}</script>"), encoding="utf-8")
            if a.probe or a.kontakt:
                if a.probe: zeiten = [float(x) for x in a.probe.split(",")]
                else: zeiten = [round(1 + i * (R["dauer"] - 2) / 7, 2) for i in range(8)]
                sh("node", PREMIUM / "rendern.mjs", seite, R["dauer"], keep / "probe", ",".join(str(z) for z in zeiten))
                if a.kontakt: kontaktbogen([keep / "probe" / f"probe_{z}.png" for z in zeiten], a.kontakt); print("✓ Kontaktbogen", a.kontakt)
            if a.ziel:
                fr = tmp / "frames"
                sh("node", PREMIUM / "rendern.mjs", seite, R["dauer"], fr)
                ziel = Path(a.ziel).resolve(); ziel.parent.mkdir(parents=True, exist_ok=True)
                enc = ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
                if a.stumm:
                    sh("ffmpeg", "-y", "-v", "error", "-framerate", 30, "-i", fr / "f%05d.jpg", *enc, ziel)
                else:   # Stimme darunter; Bildlänge = Stimme + Ausklang
                    sh("ffmpeg", "-y", "-v", "error", "-framerate", 30, "-i", fr / "f%05d.jpg", "-i", Path(a.stimme).resolve(), *enc,
                       "-c:a", "aac", "-b:a", "192k", "-map", "0:v", "-map", "1:a", "-shortest", ziel)
                print("✓", ziel)
        finally:
            seite.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
