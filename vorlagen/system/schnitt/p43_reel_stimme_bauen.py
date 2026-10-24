"""Reel 43 (Paragraf 35) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Bild = erster gesprochener Satz).
Stimme: posts/43_2026-10-30_reel_par35/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_43.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p43_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/43_2026-10-30_reel_par35"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_43.mp3"]
(REPO / O / "ton").mkdir(exist_ok=True)
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_43.wav", REPO / O / "ton/stimme.wav")
shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")
FIX = {3: '10.000', 4: '', 18: '§ 35:', 20: '100.000', 21: '', 24: '24.500', 25: '', 29: '3,5', 30: '', 34: '2.642,50', 35: '', 36: '', 42: 'zahlst', 43: 'du', 44: '', 45: '10.570', 46: '', 60: '10.570', 61: ''}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
H = "bausteine/hintergrund.png"
SZ = [
      (0.0, H, [g('Gewerbesteuer', 0.0, 820, 'weiss', 120), g('10.000 €', 0.0, 1000, 'rot', 230), g('kostet oft fast nichts', 0.0, 1250, 'gelb', 85)]),
      (4.7, H, [g('Der Grund:', 4.9, 900, 'weiss', 130), g('§ 35 EStG', 5.46, 1080, 'gelb', 170)]),
      (6.9, 'bausteine/karte_messzahl.png', []),
      (13.2, H, [g('Messbetrag:', 13.28, 900, 'weiss', 130), g('2.642,50 €', 14.46, 1080, 'gelb', 190)]),
      (17.3, H, [g('Hebesatz 400 %:', 17.56, 860, 'weiss', 120), g('10.570 €', 19.24, 1040, 'gelb', 200), g('Gewerbesteuer', 20.74, 1230, 'weiss', 110)]),
      (22.0, 'bausteine/karte_4fach.png', []),
      (27.3, 'bausteine/karte_400.png', []),
      (32.2, H, [g('Euer Hebesatz:', 32.32, 860, 'weiss', 120), g('unter oder über', 33.66, 1040, 'gelb', 120), g('400 %?', 34.46, 1200, 'rot', 200)]),
]
ut = zeilen(woerter)
ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
szenen = []
for i, (a, karte, akz) in enumerate(SZ):
    b = SZ[i + 1][0] if i + 1 < len(SZ) else ende
    text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
    text += [{"wort": k["wort"], "farbe": k["farbe"], "groesse": k["groesse"], "y": k["y"], "x": 480, "breite": 880, "ab": round(k["t"] - a, 2), "bis": round(b - a, 2)} for k in akz]
    sz = {"karte": f"../../{O}/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": ([540, 960, 960] if i == 0 else [540, 960, 1040]), "text": text}
    if karte != "bausteine/hintergrund.png" and i > 0: sz["rein"] = "whip"
    szenen.append(sz)
szenen.append({"karte": f"../../{O}/bausteine/abspann_tool.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/06_runway_lofi_ruhig.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p43_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 43:", round(ende + 1.8, 1), "s")
