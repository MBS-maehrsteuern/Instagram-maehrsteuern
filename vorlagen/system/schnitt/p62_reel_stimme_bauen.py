"""Reel 62 (Gläsern) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag ~30 s, Hook nach 18_wissen).
Stimme: posts/42_…/ton/stimme.wav (geschnitten nur in echten Pausen, −18 LUFS), Wortzeiten aus aufnahmen/2026-10-22/geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p62_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/62_2026-10-22_reel_glaesern"
W = json.loads((REPO / "aufnahmen/2026-10-22/geschnitten_woerter.json").read_text())["stimme_62.mp3"]
FIX = {2: "das", 22: "Erstens:", 24: "Kranken- und Pflegeversicherung.", 27: "meldet", 31: "Zweitens:", 46: "Und drittens – das Wichtigste:", 63: "Schick"}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
SZ = [(0.0, "bausteine/hintergrund.png", [g("Das Finanzamt", 0.0, 820, "weiss", 120), g("weiß es", 0.0, 980, "gelb", 160), g("schon.", 0.0, 1160, "rot", 190)]),
      (6.84, "bausteine/karte_1.png", []),
      (11.66, "bausteine/karte_2.png", []),
      (18.32, "bausteine/karte_3.png", []),
      (24.98, "bausteine/hintergrund.png", [g("Gläsern", 25.0, 860, "weiss", 170), g("bist du längst.", 25.8, 1050, "gelb", 130)])]
ut = zeilen(woerter)
ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
szenen = []
for i, (a, karte, akz) in enumerate(SZ):
    b = SZ[i + 1][0] if i + 1 < len(SZ) else ende
    text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
    text += [{"wort": k["wort"], "farbe": k["farbe"], "groesse": k["groesse"], "y": k["y"], "x": 480, "breite": 880, "ab": round(k["t"] - a, 2), "bis": round(b - a, 2)} for k in akz]
    sz = {"karte": f"../../{O}/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": ([540, 960, 960] if i == 0 else [540, 960, 1040]), "text": text}
    if i == 1: sz["rein"] = "whip"
    szenen.append(sz)
szenen.append({"karte": f"../../{O}/bausteine/abspann.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/10_runway_spannung.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p62_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 62:", round(ende + 1.8, 1), "s")
