"""Reel 30 (GWG) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag, Hook nach 18_/19_wissen: Ergebnis ab Frame 1).
Stimme: posts/30_2026-10-21_reel_gwg/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_30.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p30_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/30_2026-10-21_reel_gwg"
VIDEO = "reel_gwg.mp4"
# Vorbereitung: alte Fassung sichern, Stimme + Hintergrund in den Post-Ordner
(REPO / O / "ton").mkdir(exist_ok=True); (REPO / O / "bausteine").mkdir(exist_ok=True)
if not (REPO / O / "reel_ohne_stimme.mp4").exists() and (REPO / O / VIDEO).exists(): shutil.copy(REPO / O / VIDEO, REPO / O / "reel_ohne_stimme.mp4")
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_30.wav", REPO / O / "ton/stimme.wav")
if not (REPO / O / "bausteine/hintergrund.png").exists(): shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")
for f, z in (("material/karte_schwellen.png", "bausteine/karte_schwellen.png"), ("material/karte_einheitlich.png", "bausteine/karte_einheitlich.png"), ("../../assets/bibliothek/bausteine/abspann_rechnet.png", "bausteine/abspann_rechnet.png")):
    if not (REPO / O / z).exists(): shutil.copy(REPO / O / f, REPO / O / z)
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_30.mp3"]
FIX = {16: 'netto:', 21: 'Derselbe', 22: '', 27: 'abschreiben:', 28: 'über', 32: 'Sammelposten.', 33: '', 36: 'je', 55: 'bis 1.000', 12: 'Bürostuhl'}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
SZ = [(0.0, "bausteine/hintergrund.png", [g("1 € entscheidet:", 0.0, 820, "weiss", 130), g("sofort oder", 0.0, 1000, "gelb", 150), g("5 Jahre.", 0.0, 1220, "rot", 230)]),
      (3.8, "bausteine/hintergrund.png", [g("Stuhl 799 €:", 3.8, 860, "weiss", 130), g("GWG = sofort", 6.24, 1040, "gruen", 140)]),
      (8.5, "bausteine/hintergrund.png", [g("Stuhl 801 €:", 8.5, 860, "weiss", 130), g("abschreiben", 10.18, 1040, "rot", 140)]),
      (11.44, "bausteine/karte_schwellen.png", []),
      (13.7, "bausteine/hintergrund.png", [g("Pool:", 13.7, 860, "weiss", 130), g("5 Jahre je 20 %", 14.1, 1040, "gelb", 130)]),
      (17.62, "bausteine/karte_einheitlich.png", []),
      (25.24, "bausteine/hintergrund.png", [g("Was nehmt ihr?", 25.24, 860, "weiss", 130), g("GWG oder Pool?", 26.04, 1040, "gelb", 140)])]
ut = zeilen(woerter)
ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
szenen = []
for i, (a, karte, akz) in enumerate(SZ):
    b = SZ[i + 1][0] if i + 1 < len(SZ) else ende
    text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
    text += [{"wort": k["wort"], "farbe": k["farbe"], "groesse": k["groesse"], "y": k["y"], "x": 480, "breite": 880, "ab": round(k["t"] - a, 2), "bis": round(b - a, 2)} for k in akz]
    sz = {"karte": f"../../{O}/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": ([540, 960, 960] if i == 0 else [540, 960, 1040]), "text": text}
    if i == 1: sz["rein"] = "whip"
    szenen.append(sz)
szenen.append({"karte": f"../../{O}/bausteine/abspann_rechnet.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/{VIDEO}", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/06_runway_lofi_ruhig.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p30_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 30:", round(ende + 1.8, 1), "s")
