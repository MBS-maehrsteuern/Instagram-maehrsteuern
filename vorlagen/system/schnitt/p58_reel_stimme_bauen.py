"""Reel 58 (Vorsteuer) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag ~30 s, Hook nach 18_wissen).
Stimme: posts/42_…/ton/stimme.wav (geschnitten nur in echten Pausen, −18 LUFS), Wortzeiten aus aufnahmen/2026-10-21/geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p58_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/58_2026-11-08_reel_vorsteuer"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_58.mp3"]
FIX = {0: "Rechnung", 2: "Leistung", 3: "erhalten", 32: "eine,", 45: "Kleinbetragsrechnung", 46: "", 59: "zurückwirken."}
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
SZ = [(0.0, "bausteine/hintergrund.png", [g("Rechnung bezahlt.", 0.1, 820, "weiss", 120), g("Vorsteuer:", 2.3, 1000, "gelb", 170), g("0 €.", 3.0, 1190, "rot", 200)]),
      (3.8, "bausteine/karte_rechnung.png", []),
      (8.3, "bausteine/karte_pflicht.png", []),
      (16.06, "bausteine/karte_rechnung.png", []),
      (20.34, "bausteine/hintergrund.png", [g("Berichtigung", 21.6, 860, "gruen", 150), g("wirkt zurück.", 23.2, 1040, "weiss", 140)]),
      (24.42, "bausteine/hintergrund.png", [g("Beim Eingang", 25.2, 860, "weiss", 150), g("prüfen.", 25.9, 1040, "gelb", 170)]),
      (26.9, "bausteine/hintergrund.png", [g("Buchhaltung", 28.0, 860, "weiss", 150), g("oder keiner?", 28.8, 1040, "gelb", 150)])]
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
               {"datei": "../../musik/08_runway_chill_house.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p58_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 58:", round(ende + 1.8, 1), "s")
