"""Reel 53 (IAB) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Schlussfrage vor Abspann).
Stimme: posts/53_2026-11-04_iab/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_53.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p53_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/53_2026-11-04_iab"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_53.mp3"]
FIX = {31: "200.000", 32: "", 37: "60.000", 38: "", 41: "30.000", 42: "", 66: "rückwirkend"}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
H = "bausteine/hintergrund.png"
SZ = [(0.0, H, [g("Maschine absetzen,", 0.0, 840, "weiss", 120), g("noch vor dem Kauf.", 0.0, 1020, "gelb", 130)]),
      (3.12, "bausteine/karte_50.png", []),
      (8.0, "bausteine/karte_200000.png", []),
      (10.52, H, [g("Maschine: 60.000 €", 10.52, 860, "weiss", 110), g("Abzug: 30.000 €", 12.62, 1040, "gelb", 130)]),
      (15.02, H, [g("Im Kaufjahr:", 15.02, 860, "weiss", 130), g("wieder dazu.", 16.38, 1040, "gelb", 150)]),
      (17.54, "bausteine/haken_frist.png", []),
      (24.22, H, [g("Nutzt ihr", 24.22, 820, "weiss", 140), g("die IAB?", 24.86, 990, "gelb", 170), g("Ja oder nein?", 25.44, 1200, "rot", 140)])]
WHIP = 1
ut = zeilen(woerter)
ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
szenen = []
for i, (a, karte, akz) in enumerate(SZ):
    b = SZ[i + 1][0] if i + 1 < len(SZ) else ende
    text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
    text += [{"wort": k["wort"], "farbe": k["farbe"], "groesse": k["groesse"], "y": k["y"], "x": 480, "breite": 880, "ab": round(k["t"] - a, 2), "bis": round(b - a, 2)} for k in akz]
    sz = {"karte": f"../../{O}/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": ([540, 960, 960] if i == 0 else [540, 960, 1040]), "text": text}
    if i == WHIP: sz["rein"] = "whip"
    szenen.append(sz)
szenen.append({"karte": f"../../{O}/bausteine/abspann_tool.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/06_runway_lofi_ruhig.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p53_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 53:", round(ende + 1.8, 1), "s")
