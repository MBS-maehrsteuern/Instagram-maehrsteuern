"""Reel 54 (Reverse Charge) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Schlussfrage vor Abspann).
Stimme: posts/54_2026-11-05_reel_reverse_charge/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_54.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p54_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/54_2026-11-05_reel_reverse_charge"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_54.mp3"]
FIX = {19: "100.000€", 20: "", 22: "19.000€", 23: "", 40: "19.000€", 41: "", 57: "13b UStG", 58: "", 69: "forderst", 29: "Bauleistung."}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
H = "bausteine/hintergrund.png"
SZ = [(0.0, H, [g("USt bezahlt.", 0.0, 820, "weiss", 150), g("Vorsteuer:", 0.0, 1010, "gelb", 150), g("0 €", 0.0, 1220, "rot", 260)]),
      (3.66, "bausteine/haken_fall.png", []),
      (9.22, H, [g("Du baust selbst.", 9.22, 820, "weiss", 130), g("Du schuldest", 11.02, 1000, "gelb", 140), g("die Steuer.", 11.76, 1150, "gelb", 140)]),
      (12.62, "bausteine/karte_fehler.png", []),
      (19.04, "bausteine/karte_regel.png", []),
      (24.16, H, [g("Zu viel gezahlt:", 24.16, 860, "weiss", 120), g("zurückfordern.", 25.18, 1040, "gelb", 150)]),
      (26.24, H, [g("Schon mal", 26.24, 820, "weiss", 150), g("passiert?", 26.52, 990, "gelb", 170), g("Ja oder nein?", 27.24, 1200, "rot", 140)])]
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
pfad = hier / "p54_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 54:", round(ende + 1.8, 1), "s")
