"""Reel 42 (degressive AfA) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag ~30 s, Hook nach 18_wissen).
Stimme: posts/42_…/ton/stimme.wav (geschnitten nur in echten Pausen, −18 LUFS), Wortzeiten aus aufnahmen/2026-10-21/geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p42_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/42_2026-10-29_reel_afa"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_42.mp3"]
FIX = {8: "30 %", 9: "", 10: "AfA", 14: "2.500", 15: "", 18: "degressive", 19: "AfA", 27: "linearen,", 28: "",
       42: "100.000", 43: "", 51: "30.000", 52: "", 56: "ersten", 57: "Jahr", 62: "Zwölftel.", 67: "linear", 68: "wechseln.", 70: "ihr"}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
# schlichter Hintergrund in Markenfarben für Hook und Frage
bg = REPO / O / "bausteine/hintergrund.png"
im = Image.new("RGB", (1080, 1920), (11, 15, 14)); d = ImageDraw.Draw(im)
for r in range(900, 0, -6): d.ellipse([540 - r, 700 - r, 540 + r, 700 + r], fill=(int(11 + 12 * (1 - r / 900)), int(15 + 26 * (1 - r / 900)), int(14 + 20 * (1 - r / 900))))
im.save(bg)
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
SZ = [(0.0, "bausteine/hintergrund.png", [g("Kauf im Dezember.", 0.1, 820, "weiss", 120), g("30 % AfA?", 1.7, 1000, "gelb", 190), g("Nur 2.500 €.", 3.3, 1200, "rot", 150)]),
      (5.3, "bausteine/karte_regeln.png", []),
      (16.3, "bausteine/karte_beispiel.png", []),
      (21.3, "bausteine/haken_dezember.png", []),
      (27.4, "bausteine/hintergrund.png", [g("Dezember", 27.5, 860, "gelb", 170), g("oder Januar?", 28.4, 1060, "weiss", 150)])]
ut = zeilen(woerter)
ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
szenen = []
for i, (a, karte, akz) in enumerate(SZ):
    b = SZ[i + 1][0] if i + 1 < len(SZ) else ende
    text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
    text += [{"wort": k["wort"], "farbe": k["farbe"], "groesse": k["groesse"], "y": k["y"], "x": 480, "breite": 880, "ab": round(k["t"] - a, 2), "bis": round(b - a, 2)} for k in akz]
    sz = {"karte": f"../../{O}/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": [540, 960, 1040], "text": text}
    if i == 1: sz["rein"] = "whip"
    szenen.append(sz)
szenen.append({"karte": f"../../{O}/bausteine/abspann_tool.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/07_runway_minimal_tech.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p42_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 42:", round(ende + 1.8, 1), "s")
