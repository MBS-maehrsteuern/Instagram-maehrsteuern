"""Reel 49 (Kleinunternehmer-Grenze) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Bild = erster gesprochener Satz).
Stimme: posts/49_2026-11-02_reel_kleinunternehmer/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_49.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p49_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/49_2026-11-02_reel_kleinunternehmer"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_49.mp3"]
(REPO / O / "ton").mkdir(exist_ok=True)
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_49.wav", REPO / O / "ton/stimme.wav")
shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")
FIX = {4: 'dich', 19: '25.000', 20: '', 22: 'laufendes', 23: '', 26: '100.000', 27: '', 31: '100.000', 32: '', 67: 'TOOL'}
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
      (0.0, H, [g('Ein Auftrag', 0.0, 820, 'weiss', 130), g('Umsatzsteuer', 0.0, 990, 'gelb', 140), g('ab sofort', 0.0, 1200, 'rot', 220)]),
      (3.4, H, [g('Nicht erst', 3.44, 880, 'weiss', 130), g('ab Januar', 3.88, 1060, 'gelb', 170)]),
      (4.8, H, [g('Seit 2025:', 4.94, 880, 'weiss', 130), g('2 Grenzen', 6.36, 1060, 'gelb', 170)]),
      (7.3, 'bausteine/karte_vorjahr.png', []),
      (9.0, H, [g('Laufendes Jahr:', 9.04, 880, 'weiss', 110), g('100.000 €', 10.0, 1050, 'gelb', 190)]),
      (11.6, H, [g('Über 100.000 €:', 11.86, 880, 'weiss', 120), g('sofort raus', 13.5, 1060, 'rot', 190)]),
      (14.5, 'bausteine/karte_laufend.png', []),
      (17.7, H, [g('Früher: bis Silvester', 17.8, 880, 'weiss', 100), g('heute nicht mehr', 19.66, 1060, 'rot', 120)]),
      (20.6, 'bausteine/karte_vorsteuer.png', []),
      (23.6, H, [g('Kommentiere', 23.7, 880, 'weiss', 130), g('TOOL', 24.2, 1050, 'gelb', 220), g('für den Grenzmonitor', 25.06, 1230, 'weiss', 85)]),
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
pfad = hier / "p49_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 49:", round(ende + 1.8, 1), "s")
