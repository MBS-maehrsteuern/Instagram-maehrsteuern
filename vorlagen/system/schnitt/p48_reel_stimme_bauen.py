"""Reel 48 (Firmenwagen Fahrtenbuch) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Bild = erster gesprochener Satz).
Stimme: posts/48_2026-11-02_reel_firmenwagen/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_48.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p48_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/48_2026-11-02_reel_firmenwagen"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_48.mp3"]
(REPO / O / "ton").mkdir(exist_ok=True)
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_48.wav", REPO / O / "ton/stimme.wav")
shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")
FIX = {9: 'verwirft', 16: 'Excel-Liste', 46: '1 %-Regel,', 47: '', 48: '', 56: '50.000', 57: '', 71: '1 %,'}
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
      (0.0, H, [g('Fahrtenbuch', 0.0, 820, 'weiss', 130), g('verworfen', 0.0, 1000, 'rot', 220), g('trotz sauberer Einträge', 0.0, 1250, 'gelb', 80)]),
      (4.1, H, [g('Excel-Liste:', 4.56, 880, 'weiss', 130), g('jederzeit änderbar', 5.8, 1060, 'gelb', 110)]),
      (7.1, 'bausteine/karte_fahrtenbuch.png', []),
      (14.6, H, [g('Sonst gilt', 14.7, 880, 'weiss', 130), g('1 %-Regel', 15.18, 1060, 'gelb', 200)]),
      (18.1, 'bausteine/karte_arbeitsweg.png', []),
      (21.2, H, [g('800 €', 21.34, 900, 'rot', 260), g('im Monat', 22.14, 1130, 'weiss', 130)]),
      (22.7, H, [g('Fahrtenbuch', 22.8, 880, 'gelb', 140), g('oder 1 %?', 23.22, 1050, 'weiss', 140), g('Was nutzt ihr?', 24.38, 1230, 'weiss', 110)]),
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
pfad = hier / "p48_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 48:", round(ende + 1.8, 1), "s")
