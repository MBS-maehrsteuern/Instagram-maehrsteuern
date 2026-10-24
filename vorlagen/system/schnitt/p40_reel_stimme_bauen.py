"""Reel 40 (Excel-Formeln) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Bild = erster gesprochener Satz).
Stimme: posts/40_2026-10-28_reel_formeln/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_40.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p40_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/40_2026-10-28_reel_formeln"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_40.mp3"]
(REPO / O / "ton").mkdir(exist_ok=True)
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_40.wav", REPO / O / "ton/stimme.wav")
shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")
FIX = {3: 'deine', 9: 'deine', 12: 'WENNFEHLER', 13: '', 14: 'mit', 55: 'XVERWEIS', 56: '', 76: 'ihr', 24: 'sieht', 26: 'aus,', 27: 'die', 32: 'und', 61: 'Namen', 65: '$C$12.', 66: '', 67: '', 68: '', 73: 'euch', 77: 'WENNFEHLER?', 78: ''}
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
      (0.0, H, [g('Formel macht', 0.0, 820, 'weiss', 130), g('Rückstellung', 0.0, 990, 'gelb', 140), g('falsch', 0.0, 1200, 'rot', 250)]),
      (4.3, 'bausteine/karte_wennfehler.png', []),
      (7.6, H, [g('Tabelle: sauber', 7.82, 860, 'weiss', 110), g('Rückstellung:', 9.54, 1030, 'weiss', 110), g('zu niedrig', 10.2, 1200, 'rot', 190)]),
      (12.0, H, [g('Besser:', 12.04, 860, 'weiss', 130), g('Fehler sichtbar', 12.38, 1040, 'gelb', 130), g('lassen', 13.58, 1200, 'gelb', 130)]),
      (17.2, 'bausteine/karte_xverweis.png', []),
      (20.5, 'bausteine/karte_namen.png', []),
      (24.2, H, [g('Habt ihr', 25.4, 860, 'weiss', 130), g('WENNFEHLER?', 25.82, 1060, 'gelb', 130)]),
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
pfad = hier / "p40_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 40:", round(ende + 1.8, 1), "s")
