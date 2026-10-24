"""Reel 55 (Thesaurierung) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Schlussfrage vor Abspann).
Stimme: posts/55_2026-11-06_reel_thesaurierung/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_55.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p55_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/55_2026-11-06_reel_thesaurierung"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_55.mp3"]
FIX = {1: "zahlst", 27: "28,25", 28: "", 51: "", 52: "nimmst"}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
H = "bausteine/hintergrund.png"
SZ = [(0.0, H, [g("Gewinn nicht entnommen.", 0.0, 800, "weiss", 100), g("Steuer bis zu", 0.0, 960, "gelb", 130), g("45 %", 0.0, 1180, "rot", 280)]),
      (4.02, H, [g("Muss nicht sein.", 4.02, 900, "weiss", 140)]),
      (5.14, "bausteine/karte_regel.png", []),
      (11.06, H, [g("Ab 2028 sinkt", 11.06, 840, "weiss", 120), g("der Satz.", 12.6, 990, "weiss", 120), g("Ab 2032: 25 %", 14.14, 1170, "gelb", 150)]),
      (16.66, "bausteine/karte_fuer_wen.png", []),
      (19.74, "bausteine/karte_nachversteuerung.png", []),
      (24.96, H, [g("Lohnt sich nur,", 24.96, 840, "weiss", 130), g("wenn das Geld", 26.22, 1010, "gelb", 130), g("lange drin bleibt.", 26.64, 1160, "gelb", 130)]),
      (27.54, H, [g("Gewinn bleibt", 27.54, 840, "weiss", 140), g("drin – oder raus?", 28.86, 1020, "gelb", 120)])]
WHIP = 2
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
pfad = hier / "p55_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 55:", round(ende + 1.8, 1), "s")
