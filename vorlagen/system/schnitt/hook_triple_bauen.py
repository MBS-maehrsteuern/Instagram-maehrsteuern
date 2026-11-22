"""Dreifach-Hook („Triple Hook“) bauen: Kinetic-Typografie-Opener, Wort für Wort zu Loris' Stimme.
    python3 vorlagen/system/schnitt/hook_triple_bauen.py --stimme post/ton/stimme.wav --hook hook.json --reel post/reel.mp4 --ziel out.mp4
    (--nur-hook statt --reel: nur der Hook-Clip, Ton = Stimme der ersten Sekunden)
hook.json OHNE Zeiten: {"zeilen":[{"woerter":["Ein","einziger",{"w":"Auftrag","gross":true}],"icon":"dokument"}, …]}
  Wort = "Text" oder {"w":"Text","akzent":"gruen"|"rot"|"serif","gross":true}; Icons: haken auge fragezeichen blitz euro warnung kalender haus auto dokument.
Ablauf: Stimme → 16 kHz mono (ffmpeg, wave) → faster-whisper (small, int8, de, Wortzeiten) → unscharfer Abgleich mit dem Hook-Text →
        Konfiguration mit Zeiten → premium/hook_triple.html über premium/rendern_alpha.mjs → Overlay auf die ersten Sekunden des Reels (Original-Ton bleibt)."""
import argparse, difflib, json, re, shutil, subprocess, tempfile, wave
from pathlib import Path
import numpy as np
hier = Path(__file__).resolve().parent
PREMIUM = hier.parent / "premium"

def sh(*a, **k):
    subprocess.run([str(x) for x in a], check=True, **k)

def norm(s):
    return re.sub(r"[^a-zäöüß0-9]", "", s.lower())

def erkennen(stimme, tmp, sek):
    """Wortzeiten der ersten `sek` Sekunden (wave → float32 16 kHz mono; av.open mit Dateipfad ist hier kaputt)."""
    w16 = tmp / "stimme16.wav"
    sh("ffmpeg", "-y", "-v", "error", "-i", stimme, "-t", sek, "-ac", 1, "-ar", 16000, "-c:a", "pcm_s16le", w16)
    with wave.open(str(w16)) as f:
        audio = np.frombuffer(f.readframes(f.getnframes()), np.int16).astype(np.float32) / 32768
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(audio, language="de", word_timestamps=True, beam_size=5)
    return [(x.word.strip(), x.start, x.end) for sg in segs for x in sg.words]

def abgleichen(woerter, erkannt):
    """Jedes Hook-Wort der Reihe nach dem ähnlichsten noch nicht belegten Whisper-Wort zuordnen (Fenster 4 Wörter, Abstand wird bestraft); Lücken interpolieren."""
    zeiten, pos = [], 0
    for w in woerter:
        best, bi = 0.0, None
        for i in range(pos, min(pos + 4, len(erkannt))):
            r = difflib.SequenceMatcher(None, norm(w), norm(erkannt[i][0])).ratio() - 0.12 * (i - pos)  # nähere Wörter bevorzugen
            if r > best: best, bi = r, i
        if bi is not None and best >= 0.45:
            zeiten.append([erkannt[bi][1], erkannt[bi][2]]); pos = bi + 1
        else:
            zeiten.append(None)
    # Lücken: gleichmäßig zwischen bekannten Nachbarn verteilen
    n = len(zeiten)
    for i in range(n):
        if zeiten[i] is None:
            a = max((j for j in range(i) if zeiten[j]), default=None)
            b = min((j for j in range(i + 1, n) if zeiten[j]), default=None)
            lo = zeiten[a][1] if a is not None else 0.0
            hi = zeiten[b][0] if b is not None else lo + 0.4 * (n - i)
            ka, kb = (a if a is not None else -1), (b if b is not None else n)
            schritt = (hi - lo) / (kb - ka)
            zeiten[i] = [lo + schritt * (i - ka - 1) , lo + schritt * (i - ka)]
    return zeiten

def hook_bauen(cfg, erkannt, vorlauf):
    flach = [(zi, w) for zi, z in enumerate(cfg["zeilen"]) for w in z["woerter"]]
    texte = [(w if isinstance(w, str) else w["w"]) for _, w in flach]
    zt = abgleichen(texte, erkannt)
    zeilen = [{"words": [], **({"icon": z["icon"]} if z.get("icon") else {})} for z in cfg["zeilen"]]
    for (zi, w), t, (s, e) in zip(flach, texte, zt):
        o = {"w": t, "s": round(max(0, s - vorlauf), 3), "e": round(e, 3)}
        if not isinstance(w, str):
            for k in ("akzent", "gross"):
                if w.get(k): o[k] = w[k]
        zeilen[zi]["words"].append(o)
    letzte = max(o["e"] for z in zeilen for o in z["words"])
    ab = round(cfg.get("ausblenden_ab", letzte + 0.6), 3)
    return {"lines": zeilen, "ausblenden_ab": ab, "dauer": round(cfg.get("dauer", ab + 0.25 + 0.04), 3)}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stimme", required=True, help="Stimmen-WAV, Zeit 0 = Reel-Anfang")
    ap.add_argument("--hook", required=True, help="Hook-JSON ohne Zeiten")
    ap.add_argument("--reel", help="vorhandenes reel.mp4 (1080x1920, 30 fps); der Hook ersetzt dessen erste Sekunden im Bild")
    ap.add_argument("--ziel", required=True)
    ap.add_argument("--nur-hook", action="store_true", help="nur den Hook-Clip ausgeben (dunkler Hintergrund, Stimme)")
    ap.add_argument("--vorlauf", type=float, default=0.05, help="Wort erscheint so viele Sekunden vor dem gesprochenen Beginn")
    ap.add_argument("--behalte", help="Ordner, in den Zeit-Konfiguration (hook_zeiten.json) und Frames kopiert werden")
    a = ap.parse_args()
    if not a.nur_hook and not a.reel: ap.error("--reel oder --nur-hook nötig")
    cfg = json.loads(Path(a.hook).read_text(encoding="utf-8"))
    ziel = Path(a.ziel).resolve(); ziel.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        erkannt = erkennen(Path(a.stimme).resolve(), tmp, cfg.get("suchfenster", 12))
        print("erkannt:", " ".join(f"{w}@{s:.2f}" for w, s, _ in erkannt))
        H = hook_bauen(cfg, erkannt, a.vorlauf)
        print("Hook:", " | ".join(" ".join(f"{o['w']}@{o['s']}" for o in z["words"]) for z in H["lines"]), f"→ {H['dauer']} s")
        # Vorlage mit eingesetzter Konfiguration neben der Vorlage ablegen (relative Schrift-Pfade), danach wieder löschen
        seite = PREMIUM / f"_hook_tmp_{Path(td).name}.html"
        try:
            html = (PREMIUM / "hook_triple.html").read_text(encoding="utf-8")
            seite.write_text(html.replace("<!--HOOK-->", f"<script>window.HOOK={json.dumps(H, ensure_ascii=False)}</script>"), encoding="utf-8")
            fr = tmp / "frames"
            sh("node", PREMIUM / "rendern_alpha.mjs", seite, H["dauer"], fr)
        finally:
            seite.unlink(missing_ok=True)
        if a.behalte:
            k = Path(a.behalte); k.mkdir(parents=True, exist_ok=True)
            (k / "hook_zeiten.json").write_text(json.dumps(H, ensure_ascii=False, indent=1), encoding="utf-8")
            shutil.copytree(fr, k / "frames", dirs_exist_ok=True)
        enc = ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
        if a.nur_hook:
            sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=0x070C0A:s=1080x1920:r=30", "-framerate", 30, "-i", fr / "f%05d.png",
               "-i", a.stimme, "-filter_complex", "[0:v][1:v]overlay=shortest=1[v]", "-map", "[v]", "-map", "2:a", "-t", H["dauer"], *enc, "-c:a", "aac", "-b:a", "192k", ziel)
        else:
            sh("ffmpeg", "-y", "-v", "error", "-i", a.reel, "-framerate", 30, "-i", fr / "f%05d.png",
               "-filter_complex", "[0:v][1:v]overlay=eof_action=pass[v]", "-map", "[v]", "-map", "0:a", *enc, "-c:a", "copy", ziel)
    print("✓", ziel)

if __name__ == "__main__":
    main()
