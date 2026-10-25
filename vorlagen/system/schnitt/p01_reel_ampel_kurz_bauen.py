"""Ampel-Reel Kurzfassung (12.10., „go kürzen“ von Loris in Issue #7): 26 s → ca. 15 s.
Ohne „Also, wer kennt's nicht?“, „einfach“, „Deswegen“, „und musst eine riesige Excel-Tabelle abstimmen“ und „und ich zeige dir die Demo“.
Kanten am Pegel gemessen (Pausen 1,44–2,16 s · 2,48–2,64 s · 5,24–8,58 s · 19,55–20,30 s · „schreibt“ ab 20,72 s · Tool-Ende 22,20 s).

    cd vorlagen/system/schnitt && python3 p01_reel_ampel_kurz_bauen.py
"""
import json, subprocess, sys
from pathlib import Path

hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent))
from stimme import aufbereiten, lufs
from reels_0810_bauen import zeilen, neue_zeit, UT

REPO = hier.parent.parent.parent
P = "posts/01_2026-10-04_reel_ampel"
QUELLE = REPO / P / "ton/sprachnachricht_2.m4a"
ROH = json.loads((REPO / P / "ton/woerter_small.json").read_text())
# Whisper hängt Pausen an Wörter – Grenzen am Pegel korrigiert (silencedetect −38 dB), damit die Pausen gekürzt werden
for w in ROH:
    if w[0] == "und" and w[1] == 5.04: w[2] = 5.24  # „Fristende und“ bleibt im Ton
    if w[0] == "irgendwelche": w[2] = 9.92
    if w[0] == "Bezugsfehler": w[1] = 10.40
    if w[0] == "schreibt": w[1] = 20.72
    if w[0] == "Formelfähler": w[2] = 14.18
    if w[0] == "und" and w[1] == 14.10: w[1] = 14.85
RAUS = [(0.0, 1.90), (2.50, 2.97), (5.30, 8.40), (19.55, 20.70), (22.20, 30.0)]
KORR = ["Du", "bist", "zwei", "Tage", "vor", "Fristende", "und", "hast", "dann", "irgendwelche", "Bezugsfehler",
        "oder", "Namensfehler", "oder", "Formelfehler", "und", "suchst", "dich", "dumm", "und", "dämlich.", "Aber", "dafür", "gibt",
        "es", "jetzt", "endlich", "eine", "Lösung", "und", "das", "ist", "Code.", "Schreib", "mir", "eine", "DM", "mit", "„TOOL“."]
# (Startzeit Original, Quelle, Extra) – Video-Parameter aus p01_reel_ampel_stimme.json übernommen
SZENEN = [(0, "buero", {"ab": 0.2, "tempo": 0.9, "von": [540, 960, 1080], "nach": [540, 900, 900]}),
          (8.62, "tabelle", {"ab": 1.25}),
          (11.14, "schulter", {"ab": 1.8, "von": [540, 800, 1000], "nach": [560, 760, 820]}),
          (14.85, "tabelle", {"ab": 7.0}),
          (16.86, "ampel", {"ab": 8.0, "rein": "whip", "von": [540, 960, 1080], "nach": [540, 1000, 1000]}),
          (20.72, "ampel", {"ab": 13.8, "von": [540, 960, 1080], "nach": [410, 900, 820]})]
AKZENTE = [(2.06, "2 Tage vor Frist", "rot", 520, 150), (9.76, "#BEZUG!", "rot", 520, 230), (11.52, "#NAME?", "rot", 520, 230),
           (13.26, "#WERT!", "rot", 520, 230), (14.96, "Quelle nicht gefunden.", "rot", 470, 95), (19.12, "Code.", "gruen", 380, 200),
           (21.64, "„TOOL“ per DM", "gruen", 380, 160)]

behalten = [w for w in ROH if not any(a <= (w[1] + w[2]) / 2 < b for a, b in RAUS)]
assert len(behalten) == len(KORR), [w[0] for w in behalten]
neu = aufbereiten(QUELLE, ROH, REPO / P / "ton/stimme_kurz.flac", raus=RAUS, text=KORR)
ende = round(neu[-1][2] + 0.9, 2)  # „TOOL“ etwas stehen lassen
ut = zeilen(neu)
for i, (z, a, b) in enumerate(ut):
    ut[i] = (z, a, ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - b < 0.8 else b + 0.35)
starts = [neue_zeit(t, behalten, neu) if t else 0 for t, _, _ in SZENEN]
szenen = []
for i, (t0, q, ex) in enumerate(SZENEN):
    a = starts[i]; b = starts[i + 1] if i + 1 < len(starts) else ende
    t = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(y - a, 2)} for z, x, y in ut if x < b and y > a]
    for z, x, y in ut:
        if x < a < y: t[[e["wort"] for e in t].index(z)].pop("ab", None)
    for tz, w, f, yy, g in AKZENTE:
        x = neue_zeit(tz, behalten, neu)
        if a <= x < b: t.append({"wort": w, "farbe": f, "groesse": g, "y": yy, "x": 470, "breite": 820, "ab": round(x - a, 2), "bis": round(b - a, 2),
                                 **({"kasten": True} if tz == 21.64 else {})})  # CTA liegt über der Dashboard-Überschrift → dunkler Kasten
    szenen.append({"quelle": q, "dauer": round(b - a, 3), "text": t, **ex})
nz = lambda t: round(neue_zeit(t, behalten, neu), 2)
ton = [{"datei": f"../../{P}/ton/stimme_kurz.flac", "ab": 0, "lautstaerke": 1.0, "ein": 0.02, "aus": 0.3},
       {"datei": "../../musik/atmo/uhr_ticken.mp3", "ab": 0.3, "start": 0.3, "dauer": round(nz(16.86) - 0.3, 2), "lautstaerke": 0.18, "ein": 0.05, "aus": 0.3},
       {"datei": "../../musik/atmo/fehlerton.mp3", "ab": nz(9.76), "dauer": 0.6, "lautstaerke": 0.3},
       {"datei": "../../musik/atmo/fehlerton.mp3", "ab": nz(11.52), "dauer": 0.6, "lautstaerke": 0.22},
       {"datei": "../../musik/atmo/fehlerton.mp3", "ab": nz(13.26), "dauer": 0.6, "lautstaerke": 0.22},
       {"datei": "../../musik/07_runway_minimal_tech.mp3", "ab": nz(16.86), "start": 0.4, "lautstaerke": 0.11, "ein": 0.8}]
quellen = json.loads((hier / "p01_reel_ampel_stimme.json").read_text())["quellen"]
# 14.10.: Ortsangabe im Hebesatz-Hinweis der Aufnahme überdeckt (keine Ortsbezüge), Stammdaten-Seite (ab ~13,6 s) nicht zeigen
quellen["ampel"] = {"video": f"../../{P}/bausteine/aufnahme_gelb_gruen_neutral.mp4"}
cfg = {"ausgabe": f"../../{P}/reel_kurz.mp4", "fps": 30,
       "quellen": quellen, "szenen": szenen, "ton": ton}
(hier / "p01_reel_ampel_kurz.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(hier / "p01_reel_ampel_kurz.json")], check=True, cwd=hier.parent)
print(f"✓ Ampel kurz: {ende:.1f} s · Mix {lufs(REPO / P / 'reel_kurz.mp4'):.1f} LUFS")
