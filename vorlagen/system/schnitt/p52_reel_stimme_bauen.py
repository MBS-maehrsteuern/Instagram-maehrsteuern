"""Reel 52 (GoBD) mit Loris' Stimme aus der Aufnahme 21.10. (Hook nach 18_/19_wissen: Ergebnis ab Frame 1, Schlussfrage vor Abspann).
Stimme: posts/52_2026-11-04_reel_gobd/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_52.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p52_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/52_2026-11-04_reel_gobd"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_52.mp3"]
FIX = {21: "GoBD-Wörter.", 22: "", 1: "Steuer-Excel", 36: "kassentäglich,", 41: "GoBD", 42: "nennt"}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
H = "bausteine/hintergrund.png"
SZ = [(0.0, H, [g("Excel stimmt –", 0.0, 820, "weiss", 130), g("trotzdem", 0.0, 990, "gelb", 140), g("durchgefallen.", 0.0, 1170, "rot", 135)]),
      (3.4, H, [g("Der Prüfer schaut", 3.4, 860, "weiss", 120), g("auf 3 Wörter.", 5.46, 1060, "gelb", 170)]),
      (7.48, "bausteine/karte_unveraenderbar.png", []),
      (13.06, "bausteine/karte_zeitgerecht.png", []),
      (19.04, "bausteine/karte_dokumentiert.png", []),
      (23.2, H, [g("Habt ihr eine", 23.2, 800, "weiss", 110), g("Verfahrens-", 23.7, 960, "gelb", 130), g("dokumentation?", 24.3, 1100, "gelb", 130), g("Ja oder nein?", 25.18, 1320, "rot", 140)])]
WHIP = 3
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
pfad = hier / "p52_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 52:", round(ende + 1.8, 1), "s")
