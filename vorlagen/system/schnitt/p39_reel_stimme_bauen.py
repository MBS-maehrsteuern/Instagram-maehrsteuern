"""Reel 39 (Holding) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag, Hook nach 18_/19_wissen: Ergebnis ab Frame 1).
Stimme: posts/39_2026-10-28_reel_holding/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_39.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p39_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/39_2026-10-28_reel_holding"
VIDEO = "reel.mp4"
# Vorbereitung: alte Fassung sichern, Stimme + Hintergrund in den Post-Ordner
(REPO / O / "ton").mkdir(exist_ok=True); (REPO / O / "bausteine").mkdir(exist_ok=True)
if not (REPO / O / "reel_ohne_stimme.mp4").exists() and (REPO / O / VIDEO).exists(): shutil.copy(REPO / O / VIDEO, REPO / O / "reel_ohne_stimme.mp4")
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_39.wav", REPO / O / "ton/stimme.wav")
if not (REPO / O / "bausteine/hintergrund.png").exists(): shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")

W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_39.mp3"]
FIX = {7: 'zahlt', 10: '15.000', 11: '', 19: 'Anteile', 37: '50.000', 38: '', 48: '15.000', 49: '', 52: '1,5', 53: '%.'}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
SZ = [(0.0, "bausteine/hintergrund.png", [g("1 Mio. € Gewinn:", 0.0, 840, "weiss", 130), g("unter 15.000 €", 0.0, 1010, "gelb", 140), g("Steuer.", 0.0, 1190, "rot", 200)]),
      (4.26, "bausteine/hintergrund.png", [g("Völlig legal.", 4.26, 960, "gelb", 190)]),
      (5.36, "bausteine/karte_regel.png", []),
      (10.58, "bausteine/karte_rechnung.png", []),
      (18.16, "bausteine/hintergrund.png", [g("Knapp 15.000 €", 18.16, 860, "weiss", 130), g("= rund 1,5 %", 19.5, 1040, "gelb", 170)]),
      (20.84, "bausteine/hintergrund.png", [g("Aber: Verluste", 20.84, 860, "weiss", 130), g("nicht abziehbar", 22.12, 1040, "rot", 130)]),
      (24.96, "bausteine/hintergrund.png", [g("Holding", 24.96, 860, "weiss", 130), g("schon im Einsatz?", 25.26, 1040, "gelb", 120), g("Ja oder nein?", 26.26, 1220, "gelb", 150)])]
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
szenen.append({"karte": f"../../{O}/bausteine/abspann_tool.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/{VIDEO}", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/06_runway_lofi_ruhig.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p39_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 39:", round(ende + 1.8, 1), "s")
