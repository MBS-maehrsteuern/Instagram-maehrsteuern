"""Content-Offensive-Reel bauen (07.11.2026): Spec (JSON) + Stimme + Wortzeiten (+ Lip-Sync-Gesicht) → reel.mp4.
    python3 vorlagen/system/premium/offensive_bauen.py <reel_ordner> [--probe 0.1,2,8]
<reel_ordner> enthält: spec.json, ton/stimme.wav, ton/woerter.json, optional gesicht/g0001.jpg … (Lip-Sync-Frames, 30 fps).
Zeiten in der Spec sind Wörter/Phrasen aus der Aufnahme ("at": "Hausmeister") → werden hier auf Sekunden aufgelöst,
damit jede Einblendung exakt auf Loris' Wort kommt. Schreibt reel.mp4 (−18 LUFS), titelbild.png, zeiten.json."""
import json, re, subprocess, sys, tempfile
from pathlib import Path
hier = Path(__file__).resolve().parent
REPO = hier.parent.parent.parent
ordner = Path(sys.argv[1]).resolve()
probe = sys.argv[sys.argv.index("--probe") + 1] if "--probe" in sys.argv else None
nur_ton = "--nur-ton" in sys.argv   # Bild aus vorhandenem reel.mp4 behalten, nur Ton (Musik/SFX) neu mischen
spec = json.loads((ordner / "spec.json").read_text())
wo = json.loads((ordner / "ton/woerter.json").read_text())
W = wo["words"]; dauer = wo["dauer"]
norm = lambda s: re.sub(r"[^\wäöüß]", "", s.lower())
# Transkriptions-Korrekturen für die Untertitel: [["Das Satz","Der Satz"], …] – gleiche Wortzahl ersetzt Wort für Wort
for alt, neu in spec.get("korrektur", []):
    a, n = alt.split(), neu.split()
    for i in range(len(W) - len(a) + 1):
        if [norm(W[i + k]["w"]) for k in range(len(a))] == [norm(x) for x in a]:
            satz = re.findall(r"[.,:?!]*$", W[i + len(a) - 1]["w"])[0]
            if len(a) == len(n):
                for k in range(len(a)): W[i + k]["w"] = n[k] + (satz if k == len(a) - 1 else "")
            else:
                W[i]["w"] = neu + satz
                for k in range(1, len(a)): W[i + k]["w"] = ""
def zeit(at, ab=0.0, ende=False):
    """Phrase → Startzeit (oder Endzeit) des ersten Treffers ab Sekunde `ab`; Zahl bleibt Zahl."""
    if isinstance(at, (int, float)): return float(at)
    p = [norm(x) for x in at.split()]
    for i in range(len(W) - len(p) + 1):
        if W[i]["s"] < ab - 0.01 or not W[i]["w"]: continue
        if all(norm(W[i + k]["w"]).startswith(p[k]) if k == len(p) - 1 else norm(W[i + k]["w"]) == p[k] for k in range(len(p))):
            return W[i + len(p) - 1]["e"] if ende else W[i]["s"]
    raise SystemExit(f"✗ Wort nicht gefunden: {at!r} ab {ab:.2f}s ({ordner.name})")
ge = zeit(spec.get("gesicht_bis", 2.0), 0, ende=True)
spec["gesicht_bis"] = ge
cur = ge
sz = spec["szenen"]
for s in sz:
    if s is sz[0]:   # erste Szene: frühestens dort, wo der Hook-Satz endet (Gesicht kann kürzer sein, Hook-Text bleibt bis dahin stehen)
        s["von"] = max(ge, zeit(spec["szene1_ab"], 0, ende=True)) if spec.get("szene1_ab") else ge
    else:
        s["von"] = max(ge, zeit(s.get("at", cur), cur))
    cur = s["von"]
    for p in s.get("punkte", []) + s.get("optionen", []) + s.get("zeilen", []):
        p["_t"] = zeit(p["at"], cur) if "at" in p else cur
    if s["typ"] == "vs": s["_t2"] = zeit(s.get("at2", cur), cur)
    if s["typ"] == "mythos":
        s["_ts"] = zeit(s.get("stempel_at", cur), cur); s["_tw"] = zeit(s.get("wahr_at", s["_ts"]), s["_ts"])
    if s["typ"] == "cta": s["_ti"] = zeit(s.get("icon_at", cur), cur)
for a, b in zip(sz, sz[1:]): a["bis"] = b["von"]
# CTA braucht Zeit für seine Animation: Video nach dem letzten Wort mit Stille verlängern (mind. 2 s ab CTA-Start)
if sz[-1]["typ"] == "cta": dauer = round(max(dauer, sz[-1]["_ti"] + 2.0, sz[-1]["von"] + 2.0), 2)
sz[-1]["bis"] = dauer + 5
spec["_boeen"] = [0.03, ge] + [s["von"] for s in sz]
spec["_hook_bis"] = sz[0]["von"]
g = ordner / "gesicht"
if g.exists() and any(g.glob("g*.jpg")):
    spec["gesicht"] = {"ordner": str(g), "n": len(list(g.glob("g*.jpg"))), "fps": 30, "versatz": spec.get("gesicht_versatz", 0)}
else:
    # kein Lip-Sync-Clip: Porträt-Modus mit stimmgesteuertem Ring (Lautstärke-Hüllkurve, 30 fps, 0…1)
    import numpy as np, wave
    w = wave.open(str(ordner / "ton/stimme.wav")); a = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(float) / 32768
    n = w.getframerate() // 30; r = np.sqrt((a[: len(a) // n * n].reshape(-1, n) ** 2).mean(1)); r = np.convolve(r, np.ones(3) / 3, "same")
    spec["_amp"] = [round(float(x), 3) for x in np.clip(r / (np.percentile(r, 95) or 1), 0, 1)]
    spec["avatar"] = str(REPO / "assets/marke/loris_headshot_1.jpg")
html = (hier / "offensive.html").read_text().replace("/*SPEC*/", "const SPEC=" + json.dumps(spec, ensure_ascii=False) + ";\nconst WOERTER=" + json.dumps(wo, ensure_ascii=False) + ";")
tmp_html = hier / f"_tmp_{ordner.name}.html"
tmp_html.write_text(html)
(ordner / "zeiten.json").write_text(json.dumps({"gesicht_bis": ge, "szenen": [[s["typ"], round(s["von"], 2)] for s in sz]}, ensure_ascii=False))
try:
    if probe:
        subprocess.run(["node", "rendern.mjs", tmp_html.name, "1", str(ordner / "probe"), probe], check=True, cwd=hier)
        print("✓ Probe", ordner / "probe"); sys.exit(0)
    with tempfile.TemporaryDirectory() as tmp:
        if nur_ton:
            (ordner / "reel.mp4").rename(f"{tmp}/bild.mp4"); bild = ["-i", f"{tmp}/bild.mp4"]; vcodec = ["-c:v", "copy"]
        else:
            subprocess.run(["node", "rendern.mjs", tmp_html.name, str(dauer), tmp], check=True, cwd=hier, stdout=subprocess.DEVNULL)
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f"{tmp}/f00000.jpg", str(ordner / "titelbild.png")], check=True)
            bild = ["-framerate", "30", "-i", f"{tmp}/f%05d.jpg"]; vcodec = ["-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-crf", "20"]
        # Sounddesign: Luftzug bei jeder Böe, Stempel beim Mythos, Pop/Haken beim CTA – leise, nie lauter als die Stimme
        A = "musik/atmo/runway/"
        marken = [f"{A}109_swish_luft.mp3@{max(0, b - 0.12):.2f}@-22" for b in spec["_boeen"][1:]] + [f"{A}110_swoosh_edel.mp3@0.02@-24"]
        for s in sz:
            if s["typ"] == "mythos": marken.append(f"{A}132_stempel.mp3@{s['_ts']:.2f}@-18")
            if s["typ"] == "cta": marken.append(f"{A}{'160_haken_bestaetigt' if s['icon'] in ('save','follow') else '119_pop_subtil'}.mp3@{s['_ti'] + 0.8:.2f}@-20")
            for p in s.get("punkte", []) + s.get("optionen", []): marken.append(f"{A}119_pop_subtil.mp3@{p['_t']:.2f}@-28")
        subprocess.run(["python3", str(hier / "sfx.py"), f"{tmp}/sfx.wav", str(dauer), *marken], check=True, stdout=subprocess.DEVNULL)
        musik = REPO / spec.get("musik", "musik/06_runway_lofi_ruhig.mp3")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *bild, "-i", str(ordner / "ton/stimme.wav"),
                        "-stream_loop", "-1", "-i", str(musik), "-i", f"{tmp}/sfx.wav", "-filter_complex",
                        f"[1:a]apad[v0];[2:a]volume=0.07,afade=t=in:d=0.8,afade=t=out:st={dauer - 1.5}:d=1.5[m];[3:a]volume=0.5[s];"
                        f"[v0][m][s]amix=inputs=3:duration=first:normalize=0,atrim=0:{dauer},asetpts=N/SR/TB,loudnorm=I=-18:TP=-1.5:LRA=11[a]",
                        "-map", "0:v", "-map", "[a]", *vcodec,
                        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", str(dauer), "-movflags", "+faststart", str(ordner / "reel.mp4")], check=True)
    print("✓", ordner / "reel.mp4", f"{dauer:.1f}s")
finally:
    tmp_html.unlink(missing_ok=True)
