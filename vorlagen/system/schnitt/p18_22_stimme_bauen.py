"""Stimm-Fassungen der Reels 18–22 aus Loris' Sammelaufnahme vom 17.10. (aufnahmen/2026-10-17_sprechtexte.mp3, 8:22 min,
mehrere Fassungen je Reel + Anweisungen an Claude). Je Reel werden die besten Sätze aus den Fassungen zu einer Geschichte
zusammengesetzt (SEG = Zeitbereiche in der Originaldatei, Reihenfolge = Reihenfolge im Reel), der Rest fällt weg.
Bilder: die Karten der Fassung ohne Stimme (posts/<ordner>/_karten/), Untertitel wörtlich oben, Hook groß in der Mitte.

    cd vorlagen/system/schnitt && python3 p18_22_stimme_bauen.py [18 19 …]   (ohne KORR: zeigt nur die behaltenen Wörter)
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np, imageio_ffmpeg

hier = Path(__file__).resolve().parent
sys.path.insert(0, str(hier.parent))
from stimme import aufbereiten, lufs
from reels_0810_bauen import zeilen

REPO = hier.parent.parent.parent
QUELLE = REPO / "aufnahmen/2026-10-17_sprechtexte.mp3"
WOERTER = json.loads((REPO / "aufnahmen/2026-10-17_sprechtexte_woerter.json").read_text())
FF = imageio_ffmpeg.get_ffmpeg_exe()
for w in WOERTER:  # Whisper setzt „Ja,“ (Verlustvortrag) auf 168,36 s mit Länge 0 – am Pegel liegt es bei 166,94–167,32 s
    if w[0] == "Ja," and abs(w[1] - 168.36) < 0.01: w[1], w[2] = 166.94, 167.32
UT = {"groesse": 78, "y": 400, "x": 480, "breite": 860}  # Untertitel oben (die Karten liegen bei y 590–1480)
STILL = -34  # dB: darunter Pause


def energie():
    raw = subprocess.run([FF, "-loglevel", "error", "-i", str(QUELLE), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32)
    return np.array([20 * np.log10(np.sqrt((x[i:i + 320] ** 2).mean()) + 1e-9) for i in range(0, len(x) - 320, 320)])


E = energie()
def e(t): return E[min(max(int(t * 50), 0), len(E) - 1)]


def nachschaerfen(w):
    """Whisper hängt Pausen an Wörter – Wortgrenzen auf die tatsächlich gesprochenen Frames ziehen."""
    a, b = w[1], w[2]
    laut = [i / 50 for i in range(int(a * 50), int(b * 50) + 1) if e(i / 50) > STILL]
    if laut: a, b = max(a, laut[0] - 0.03), min(b, laut[-1] + 0.06)
    return [w[0], round(a, 2), round(max(b, a + 0.05), 2)] + w[3:]


def kante(t, richtung):
    """Schnittkante ins leiseste Frame in der Nähe legen (vor dem Satz: davor suchen, nach dem Satz: danach)."""
    fenster = np.arange(t - 0.25, t + 0.06, 0.02) if richtung < 0 else np.arange(t - 0.04, t + 0.3, 0.02)
    return round(float(min(fenster, key=e)), 2)


def zeit_neu(t, behalten, neu):
    """Originalzeit → Zeit im Reel. Die Abschnitte können umgestellt sein (Satz aus einer früheren Fassung) – deshalb das
    Wort, das zeitlich am nächsten an t liegt (Wortende nach t), nicht das erste in Reel-Reihenfolge."""
    kand = [(o[2] - t if o[2] > t else 1e9, n) for o, n in zip(behalten, neu)]
    d, n = min(kand, key=lambda x: x[0])
    return max(n[1] - 0.05, 0) if d < 1e9 else neu[-1][2]


def gross(wort, t, y, farbe="weiss", groesse=150):
    return dict(wort=wort, t=t, y=y, farbe=farbe, groesse=groesse)


REELS = {
    "18": dict(ordner="posts/18_2026-10-19_reel_aufbewahrung", musik="09_runway_lofi_piano.mp3",
               SEG=[(52.12, 55.14), (55.80, 56.70), (58.70, 65.26), (65.66, 68.22), (69.36, 82.64)],
               szenen=[(52.12, "szene_1.png", [gross("10 Jahre?", 52.3, 860, "gelb", 190), gross("Nicht mehr.", 55.8, 1060, "rot", 170)]),
                       (58.70, "szene_2.png", []), (65.66, "szene_3.png", []), (69.36, "szene_4.png", [])],
               KORR=["Du","willst","deine","Belege","wirklich","10","Jahre","aufbewahren?","Das","brauchst","du","nicht","mehr.","Seit","2025","musst","du","Buchungsbelege","nur","noch","8","Jahre","aufbewahren.","Bücher","und","Jahresabschlüsse","bleiben","bei","10","Jahren.","Aber","ein","Problem:","Solange","das","Jahr","steuerlich","noch","offen","ist,","bleibt","der","Beleg","im","Archiv.","Speicher","dir","das,","bevor","du","den","Keller","ausmistest.","Danach","ist","zu","spät."]),
    "19": dict(ordner="posts/19_2026-10-20_reel_verlustvortrag", musik="07_runway_minimal_tech.mp3",
               SEG=[(161.66, 179.38), (179.78, 184.72)],
               szenen=[(161.66, "szene_1.png", [gross("3 Mio. Verlust", 161.7, 800, "weiss", 130), gross("2 Mio. Gewinn", 164.2, 960, "gruen", 130), gross("… trotzdem Steuer?", 165.7, 1130, "gelb", 120)]),
                       (168.36, "szene_2.png", []), (170.34, "szene_3.png", []),
                       (173.66, "szene_4.png", [gross("KSt: 300.000 €", 174.0, 820, "gruen", 140), gross("GewSt: 400.000 €", 177.0, 1010, "gelb", 140),
                                                 gross("Demo-Zahlen", 179.8, 1170, "weiss", 60)])],
               KORR=["3","Mio.","Verlustvortrag,","2","Mio.","Gewinn","und","trotzdem","Steuer?","Ja:","Mindestbesteuerung.","Die","erste","Mio.","voll,","vom","Rest","nur","70","%.","Bleiben","300.000","","steuerpflichtig,","bei","der","Gewerbesteuer","400.000.","","Das","sind","natürlich","nur","Demo-Zahlen,","aber","speichert","ihr","das","ruhig."]),
    "20": dict(ordner="posts/20_2026-10-21_reel_erechnung", musik="11_runway_future_garage.mp3",
               SEG=[(294.66, 313.50), (331.42, 334.10), (335.54, 340.14), (344.88, 348.92)],
               szenen=[(294.66, "szene_1.png", [gross("800.000 €", 294.7, 860, "gelb", 180), gross("Umsatz?", 297.9, 1060, "weiss", 150)]),
                       (305.32, "szene_3.png", []), (335.54, "szene_4.png", [])],
               KORR=["Hast","du","dieses","Jahr","800.000","","Euro","Umsatz?","Dann","mach","dich","bereit","für","die","E-Rechnung,","","denn","du","musst","ab","2027","E-Rechnungen","","ausstellen","im","XML-Format.","","Ab","2028","müssen","das","dann","alle.","Frag","dich","also","selbst:","Kann","euer","Posteingang","lesen?","Wenn","nicht,","schreibt","mir","eine","DM,","dann","richten","wir","das","ein."]),
    "21": dict(ordner="posts/21_2026-10-22_reel_zinsschranke", musik="10_runway_spannung.mp3",
               SEG=[(360.50, 370.58), (371.38, 377.00), (377.96, 382.00), (382.98, 386.88), (387.48, 388.50)],
               szenen=[(360.48, "szene_1.png", [gross("Voll abziehbar?", 360.5, 900, "weiss", 130), gross("Nicht immer.", 362.9, 1080, "rot", 150)]),
                       (364.60, "szene_2.png", []), (371.38, "szene_3.png", []),
                       (377.96, "szene_1.png", [gross("30 %", 379.2, 860, "gelb", 200), gross("3 Mio.", 381.2, 1060, "gruen", 200)]),
                       (382.98, "szene_1.png", [gross("Regel 1", 383.0, 860, "gruen", 190), gross("von 6", 385.2, 1060, "weiss", 150)])],
               KORR=["Zinsen","voll","abziehbar?","Ne,","so","einfach","ist","es","nicht.","Die","Zinsschranke","deckelt","den","Nettozinsaufwand","bei","30","%","vom","steuerlichen","EBITDA.","Aber","unter","3","Millionen","Euro","Nettozinsaufwand","greift","sie","gar","nicht.","Zwei","Zahlen:","30","%,","3","Millionen.","Das","ist","Regel","Nr.","1.","Es","gibt","aber","noch","5","andere.","Speichert ihr","das."]),
    "22": dict(ordner="posts/22_2026-10-18_reel_steuersatz", musik="08_runway_chill_house.mp3",
               SEG=[(439.67, 444.23), (415.93, 422.99), (450.59, 453.19), (454.27, 462.09), (463.05, 466.09), (468.95, 471.87)],
               szenen=[(439.67, "szene_1.png", [gross("30 % an", 439.7, 860, "weiss", 170), gross("12 Stellen?", 440.6, 1060, "gelb", 170)]),
                       (415.93, "szene_2.png", []),
                       (450.59, "szene_4.png", [gross("Zelle für Zelle", 451.9, 880, "weiss", 140), gross("ändern …", 452.8, 1060, "gelb", 140)]),
                       (454.27, "szene_4.png", [gross("Tab 13,", 454.6, 860, "weiss", 150), gross("Zelle 384", 457.1, 1040, "rot", 150)]),
                       (463.05, "szene_1.png", [gross("Bei mir:", 463.0, 860, "weiss", 150), gross("eine Zelle.", 464.7, 1040, "gruen", 160),
                                                 gross("Kommentiere „TOOL“", 468.95, 1260, "gruen", 90)])],
               KORR=["30","%","an","12","Stellen?","Wie","oft","steht","ein","Steuersatz","in","deiner","Excel?","Ab","2028","sinkt","die","Körperschaftsteuer","jedes","Jahr","um","1","Punkt","bis","auf","10 %.","Festwerte","heißt:","Zelle","für","Zelle","ändern.","Und","auf","Tab","13,","in","Zelle","384","vergisst","du","es","zu","ändern.","Bei","mir","ist","es","eine","Zelle.","Kommentiere","mit","„TOOL“","und","ich","schicke","dir","die","Demo."]),
}


def bauen(nr, r):
    seg = [(kante(a, -1), kante(b, +1)) for a, b in r["SEG"]]
    # Wörter je Abschnitt (Reihenfolge des Reels), Original-Zeiten nachgeschärft
    teile = [[nachschaerfen(w) for w in WOERTER if a <= (w[1] + w[2]) / 2 < b] for a, b in seg]
    if not r["KORR"]:
        for (a, b), t in zip(seg, teile): print(f"{a:.2f}-{b:.2f}:", " ".join(w[0] for w in t))
        print(len(sum(teile, [])), "Wörter"); return
    ordner = REPO / r["ordner"]; (ordner / "ton").mkdir(exist_ok=True)
    # Abschnitte einzeln aufbereiten (gleiche Lautheit, harte Kanten) und dann aneinanderhängen
    korr = iter(r["KORR"])
    stuecke, neu_alle, behalten_alle, t0 = [], [], [], 0.0
    for k, ((a, b), worte) in enumerate(zip(seg, teile)):
        raus = [(0.0, a), (b, 10_000.0)]
        text = [next(korr) for _ in worte]
        ziel = ordner / f"ton/stimme_teil{k}.flac"
        neu = aufbereiten(QUELLE, worte, ziel, raus=raus, text=text)
        dauer = float(subprocess.run([FF, "-i", str(ziel)], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[-1])
        neu_alle += [[w, x + t0, y + t0] for w, x, y in neu]; behalten_alle += worte
        stuecke.append(ziel); t0 += dauer + 0.06
    liste = ordner / "ton/teile.txt"
    liste.write_text("".join(f"file '{p.name}'\nfile 'luecke.flac'\n" for p in stuecke))
    subprocess.run([FF, "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.06", str(ordner / "ton/luecke.flac")], check=True)
    stimme = ordner / "ton/stimme.flac"
    subprocess.run([FF, "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(liste), str(stimme)], check=True)
    for p in stuecke + [liste, ordner / "ton/luecke.flac"]: p.unlink()
    for p in ordner.glob("ton/stimme_teil*.json"): p.unlink()
    (ordner / "ton/stimme.json").write_text(json.dumps(neu_alle, ensure_ascii=False))
    ende = neu_alle[-1][2] + 0.5
    ut = zeilen(neu_alle)
    # jede Zeile bleibt stehen, bis die nächste kommt (kurze Lücken nicht leer), nie zwei Zeilen gleichzeitig
    ut = [(z, x, (ut[i + 1][1] if i + 1 < len(ut) and ut[i + 1][1] - y < 0.8 else y + 0.3)) for i, (z, x, y) in enumerate(ut)]
    starts = [zeit_neu(t, behalten_alle, neu_alle) if i else 0 for i, (t, _, _) in enumerate(r["szenen"])]
    szenen = []
    for i, (t, karte, akz) in enumerate(r["szenen"]):
        a = starts[i]; b = starts[i + 1] if i + 1 < len(starts) else ende
        text = [{"wort": z, **UT, "ab": round(max(x - a, 0), 2), "bis": round(min(y, b) - a, 2)} for z, x, y in ut if x < b and y > a]
        for g in akz:
            x = zeit_neu(g["t"], behalten_alle, neu_alle)
            if a <= x < b: text.append({"wort": g["wort"], "farbe": g["farbe"], "groesse": g["groesse"], "y": g["y"], "x": 480, "breite": 880, "ab": round(x - a, 2), "bis": round(b - a, 2)})
        sz = {"karte": f"../../{r['ordner']}/_karten/{karte}", "dauer": round(b - a, 3), "von": [540, 960, 1080], "nach": [540, 960, 1040], "text": text}
        if i == 1: sz["rein"] = "whip"
        szenen.append(sz)
    szenen.append({"karte": f"../../{r['ordner']}/_karten/abspann.png", "dauer": 1.6, "von": [540, 960, 1040], "nach": [540, 960, 1000], "text": []})
    hook = starts[1] if len(starts) > 1 else 2.0
    cfg = {"ausgabe": f"../../{r['ordner']}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen,
           "ton": [{"datei": f"../../{r['ordner']}/ton/stimme.flac", "ab": 0, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.2},
                   {"datei": "../../musik/atmo/uhr_ticken.mp3", "ab": 0, "start": 0, "dauer": hook, "lautstaerke": 0.12, "aus": 0.2},
                   {"datei": f"../../musik/{r['musik']}", "ab": hook - 0.1, "start": 0, "lautstaerke": 0.09, "ein": 0.6}]}
    pfad = hier / f"p{nr}_reel_stimme.json"
    pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
    subprocess.run([sys.executable, str(hier.parent / "montage.py"), str(pfad)], check=True, cwd=hier.parent)
    print(f"✓ {nr}: {ende + 1.6:.1f} s · Mix {lufs(ordner / 'reel.mp4'):.1f} LUFS")


if __name__ == "__main__":
    for nr in (sys.argv[1:] or REELS): bauen(nr, REELS[nr])
