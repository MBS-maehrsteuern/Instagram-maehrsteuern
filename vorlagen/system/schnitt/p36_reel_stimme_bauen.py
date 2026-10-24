"""Reel 36 (Bewirtung) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag ~27 s, Hook nach 18_/19_wissen: „0 %“ ab Frame 1).
Stimme: posts/36_…/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_36.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p36_reel_stimme_bauen.py"""
import json, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/36_2026-10-26_reel_bewirtung"
W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_36.mp3"]
FIX = {12: "alles.", 16: "fehlt:", 20: "Bewirtungen", 41: "Nachweis", 43: "erbracht:", 44: "0", 46: "70 %.", 50: "Fehler:", 51: "Bewirtungen", 65: "Anlass –", 66: "auf"}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
SZ = [(0.0, "bausteine/hintergrund.png", [g("Bewirtung", 0.0, 820, "weiss", 130), g("ohne Anlass:", 0.0, 990, "gelb", 140), g("0 %", 0.0, 1220, "rot", 260)]),
      (4.3, "bausteine/hintergrund.png", [g("Ein Wort fehlt:", 4.3, 860, "weiss", 130), g("Anlass.", 5.5, 1060, "gelb", 190)]),
      (6.42, "bausteine/karte_70.png", []),
      (9.36, "bausteine/karte_angaben.png", []),
      (13.18, "bausteine/hintergrund.png", [g("„Arbeitsgespräch“", 13.74, 860, "weiss", 120), g("= 0 %", 16.32, 1060, "rot", 220)]),
      (17.66, "bausteine/karte_konto.png", []),
      (21.78, "bausteine/hintergrund.png", [g("Anlass: Beleg", 22.66, 860, "weiss", 130), g("oder digital?", 24.14, 1040, "gelb", 150)])]
ut = zeilen(woerter)
ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
szenen = []
for i, (a, karte, akz) in enumerate(SZ):
    b = SZ[i + 1][0] if i + 1 < len(SZ) else ende
    text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
    text += [{"wort": k["wort"], "farbe": k["farbe"], "groesse": k["groesse"], "y": k["y"], "x": 480, "breite": 880, "ab": round(k["t"] - a, 2), "bis": round(b - a, 2)} for k in akz]
    sz = {"karte": f"../../{O}/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": ([540, 960, 960] if i == 0 else [540, 960, 1040]), "text": text}
    if i == 2: sz["rein"] = "whip"
    szenen.append(sz)
szenen.append({"karte": f"../../{O}/bausteine/abspann_tool.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/06_runway_lofi_ruhig.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p36_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 36:", round(ende + 1.8, 1), "s")
