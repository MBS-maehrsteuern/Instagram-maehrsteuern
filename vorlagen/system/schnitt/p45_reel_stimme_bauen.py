"""Reel 45 (Verdeckte Gewinnausschüttung) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Bild = erster gesprochener Satz).
Stimme: posts/45_2026-10-31_reel_vga/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_45.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p45_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/45_2026-10-31_reel_vga"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_45.mp3"]
(REPO / O / "ton").mkdir(exist_ok=True)
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_45.wav", REPO / O / "ton/stimme.wav")
shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")
FIX = {20: 'das', 24: 'Folge,', 32: 'außerbilanziell', 48: 'über Marktwert.', 50: 'beherrschenden', 51: 'Gesellschafter'}
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
      (0.0, H, [g('Darlehen an', 0.0, 820, 'weiss', 130), g('dich selbst =', 0.0, 990, 'gelb', 130), g('Ausschüttung', 0.0, 1200, 'rot', 150)]),
      (4.0, H, [g('0 % Zinsen', 4.02, 860, 'gelb', 170), g('von der eigenen GmbH', 5.08, 1060, 'weiss', 85)]),
      (7.9, H, [g('Folge:', 7.98, 860, 'weiss', 130), g('verdeckte', 8.74, 1030, 'gelb', 140), g('Gewinnausschüttung', 9.12, 1200, 'weiss', 90)]),
      (10.0, 'bausteine/karte_was_ist.png', []),
      (13.2, H, [g('Nur einer der', 13.28, 820, 'weiss', 110), g('Klassiker:', 13.66, 970, 'weiss', 110), g('Gehalt zu hoch', 14.86, 1130, 'gelb', 110), g('Privatnutzung', 16.98, 1270, 'gelb', 110), g('Miete über Marktwert', 19.04, 1410, 'gelb', 85)]),
      (20.1, H, [g('Beherrschender', 20.26, 860, 'weiss', 110), g('Gesellschafter:', 20.76, 1000, 'weiss', 110), g('Vereinbarung vorher', 22.36, 1170, 'gelb', 90)]),
      (24.5, H, [g('Was seht ihr häufiger?', 24.64, 880, 'weiss', 85), g('Darlehen', 25.74, 1050, 'gelb', 170), g('oder Gehalt?', 26.18, 1230, 'weiss', 120)]),
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
pfad = hier / "p45_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 45:", round(ende + 1.8, 1), "s")
