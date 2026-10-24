"""Reel 38 (Prüfpfad) mit Loris' Stimme aus der Aufnahme 21.10. (Fachbeitrag, Hook nach 18_/19_wissen: Ergebnis ab Frame 1).
Stimme: posts/38_2026-10-27_reel_pruefpfad/ton/stimme.wav (= aufnahmen/2026-10-21/geschnitten/stimme_38.wav), Wortzeiten aus geschnitten_woerter.json.
    cd vorlagen/system/schnitt && python3 p38_reel_stimme_bauen.py"""
import json, shutil, subprocess, sys
from pathlib import Path
hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent)); sys.path.insert(0, str(hier))
from reels_0810_bauen import zeilen
REPO = hier.parent.parent.parent
O = "posts/38_2026-10-27_reel_pruefpfad"
VIDEO = "reel.mp4"
# Vorbereitung: alte Fassung sichern, Stimme + Hintergrund in den Post-Ordner
(REPO / O / "ton").mkdir(exist_ok=True); (REPO / O / "bausteine").mkdir(exist_ok=True)
if not (REPO / O / "reel_ohne_stimme.mp4").exists() and (REPO / O / VIDEO).exists(): shutil.copy(REPO / O / VIDEO, REPO / O / "reel_ohne_stimme.mp4")
shutil.copy(REPO / "aufnahmen/2026-10-21/geschnitten/stimme_38.wav", REPO / O / "ton/stimme.wav")
if not (REPO / O / "bausteine/hintergrund.png").exists(): shutil.copy(REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine/hintergrund.png", REPO / O / "bausteine/hintergrund.png")

W = json.loads((REPO / "aufnahmen/2026-10-21/geschnitten_woerter.json").read_text())["stimme_38.mp3"]
FIX = {7: 'Excel', 24: 'GoBD', 27: 'sachverständiger', 28: 'Dritter', 47: 'verknüpften', 53: 'Prüfpfad:', 56: 'Zahl klicken,', 58: 'sehen.', 67: 'Excel', 69: 'Prüfpfad'}
woerter = []
for i, (w, a, b, p) in enumerate(W):
    t = FIX.get(i, w)
    ende = min(W[i + 1][1], a + 0.9) if i + 1 < len(W) else b
    woerter.append([t, a, max(ende, a + 0.08)])
ende = woerter[-1][2] + 0.6
UT = {"groesse": 78, "y": 1560, "x": 480, "breite": 860}
def g(wort, t, y, farbe="weiss", groesse=150): return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)
SZ = [(0.0, "bausteine/hintergrund.png", [g("Betriebsprüfung:", 0.0, 840, "weiss", 120), g("Excel hat", 0.0, 1010, "gelb", 150), g("keine Antwort.", 0.0, 1190, "rot", 130)]),
      (3.28, "bausteine/haken_pruefpfad.png", []),
      (7.5, "bausteine/karte_verfahrensdoku.png", []),
      (13.36, "bausteine/hintergrund.png", [g("Vom Beleg", 13.36, 840, "weiss", 140), g("zur Erklärung", 14.16, 1010, "weiss", 140), g("und zurück", 14.68, 1180, "gelb", 140)]),
      (15.44, "bausteine/hintergrund.png", [g("12 Tabellenblätter:", 15.54, 860, "weiss", 120), g("= Suchen", 17.02, 1050, "rot", 200)]),
      (18.52, "titelbild.png", []),
      (21.36, "bausteine/hintergrund.png", [g("Und heute?", 21.36, 860, "weiss", 130), g("Spur in Excel", 23.1, 1040, "gelb", 130), g("oder Prüfpfad?", 24.02, 1210, "gelb", 130)])]
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
szenen.append({"karte": f"../../{O}/bausteine/abspann_tool.png", "dauer": 1.8, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
cfg = {"ausgabe": f"../../{O}/{VIDEO}", "fps": 30, "quellen": {}, "szenen": szenen,
       "ton": [{"datei": f"../../{O}/ton/stimme.wav", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
               {"datei": "../../musik/06_runway_lofi_ruhig.mp3", "ab": 0.0, "start": 0, "lautstaerke": 0.08, "ein": 0.8}]}
pfad = hier / "p38_reel_stimme.json"; pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
print("✓ 38:", round(ende + 1.8, 1), "s")
