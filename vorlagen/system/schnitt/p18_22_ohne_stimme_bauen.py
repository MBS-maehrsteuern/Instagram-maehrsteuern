"""Notlösung für die Stimm-Reels 18–22 (Nachtlauf 14.10.): Fassung OHNE Stimme aus Bibliotheks-Material.

    cd vorlagen/system/schnitt && python3 p18_22_ohne_stimme_bauen.py [18 19 …]

Ablauf je Reel:
1. Karten 1080x1920 bauen (posts/<ordner>/_karten/): dunkler Verlauf im Serien-Stil, darauf die Folie bzw. Ampel
   im Bildbereich y ≈ 590–1480 (oben Platz für die Texteinblendungen, unten 420 px und rechts ~120 px frei).
   Der Abspann (TOOL-Aufruf) kommt aus jobs/p18_22_notloesung_abspann.json (node render.mjs …).
2. Montage-Konfiguration schnitt/p<NN>_reel_<thema>_ohne_stimme.json schreiben → montage.py.
3. Lautheit mit ebur128 messen und den Ton auf −18 LUFS ziehen (Video wird nur kopiert).
Texteinblendungen = Sprechtext aus posts/sprechtexte.md (11.10.), Zeile für Zeile; Hook-Text ab 0,3 s.
Die Stimm-Fassung (reel.mp4) bleibt reserviert – hier entsteht reel_ohne_stimme.mp4.
"""
import json, re, shutil, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw

hier = Path(__file__).resolve().parent
SYSTEM = hier.parent
REPO = SYSTEM.parent.parent
BIB = REPO / "assets/bibliothek"
W, H = 1080, 1920
ZIEL_LUFS = -18.0

# Texteinblendungen: Untertitel oben (zwei Zeilen), rechts 120 px frei
def ut(wort, ab, zeile=0, bis=None, farbe="weiss", groesse=94):
    e = {"wort": wort, "ab": ab, "groesse": groesse, "y": [340, 465, 590][zeile], "x": 480, "breite": 860}
    if bis is not None: e["bis"] = bis
    if farbe != "weiss": e["farbe"] = farbe
    return e

def unten(wort, ab, zeile=0, farbe="weiss", groesse=80):  # Untertitel im Abspann: unter der Karte, über y 1500
    e = {"wort": wort, "ab": ab, "groesse": groesse, "y": [1350, 1450][zeile], "x": 480, "breite": 860}
    if farbe != "weiss": e["farbe"] = farbe
    return e

def gross(wort, ab, y, farbe="weiss", groesse=160):  # Hook-Zeilen in der Mitte
    e = {"wort": wort, "ab": ab, "groesse": groesse, "y": y, "x": 480, "breite": 880}
    if farbe != "weiss": e["farbe"] = farbe
    return e

KR = "karussell"
REELS = {
    "18": dict(
        id="p18_reel_aufbewahrung", ordner="posts/18_2026-10-19_reel_aufbewahrung", titel=BIB / "reels/reel_aufbewahrung/titelbild.png",
        musik=("09_runway_lofi_piano.mp3", 0.0), fehlerton=1.3,
        szenen=[
            ("bg", None, 2.6, [ut("Buchungsbelege", 0.3), ut("10 Jahre aufbewahren?", 0.8, 1),
                               gross("10 Jahre?", 0.3, 860, "gelb", 190), gross("Nicht mehr.", 1.3, 1060, "rot", 170)]),
            ("einzel", BIB / "einzelposts/zahl_belege_8.png", 2.9, [ut("Seit 2025", 0.1), ut("nur noch 8.", 0.6, 1, farbe="gruen", groesse=110)]),
            ("folie", BIB / f"{KR}/aufbewahrung/folie_02.png", 3.2, [ut("Bücher und Jahresabschlüsse", 0.1, groesse=76), ut("bleiben bei 10.", 0.9, 1)]),
            ("folie", BIB / f"{KR}/aufbewahrung/folie_04.png", 3.8, [ut("Aber: Solange das Jahr", 0.1, bis=1.9), ut("steuerlich offen ist …", 0.7, 1, bis=1.9),
                                                                      ut("… bleibt der Beleg", 1.9), ut("im Archiv.", 2.4, 1, farbe="gelb", groesse=100)]),
            ("abspann", None, 3.3, [unten("Speicher dir das, bevor du", 0.1, groesse=66), unten("den Keller ausmistest.", 0.6, 1, groesse=66)]),
        ]),
    "19": dict(
        id="p19_reel_verlustvortrag", ordner="posts/19_2026-10-20_reel_verlustvortrag", titel=BIB / "reels/reel_verlust/titelbild.png",
        musik=("07_runway_minimal_tech.mp3", 0.0), fehlerton=1.0,
        szenen=[
            ("bg", None, 2.7, [ut("3 Mio. Verlustvortrag,", 0.3), ut("2 Mio. Gewinn …", 0.8, 1),
                               gross("… trotzdem", 0.3, 860, "weiss", 160), gross("Steuer?", 1.0, 1060, "gelb", 200)]),
            ("folie", BIB / f"{KR}/verlustvortrag/folie_02.png", 2.9, [ut("Ja –", 0.1, farbe="gelb"), ut("Mindestbesteuerung.", 0.5, 1)]),
            ("folie", BIB / f"{KR}/verlustvortrag/folie_03.png", 3.2, [ut("Die erste Million voll,", 0.1), ut("vom Rest nur 70 %.", 0.8, 1, farbe="gruen")]),
            ("bg", None, 3.8, [ut("Bleiben steuerpflichtig:", 0.1),
                               gross("KSt: 300.000 €", 0.4, 820, "gruen", 140), gross("GewSt: 400.000 €", 1.6, 1010, "gelb", 140),
                               gross("Demo-Zahlen · GewSt: 60 % statt 70 %", 1.6, 1170, "weiss", 52)]),
            ("abspann", None, 3.2, [unten("Demo-Zahlen.", 0.1, groesse=66), unten("Speicher dir das.", 0.6, 1, farbe="gruen")]),
        ]),
    "20": dict(
        id="p20_reel_erechnung", ordner="posts/20_2026-10-21_reel_erechnung", titel=BIB / "reels/reel_erechnung/titelbild.png",
        musik=("11_runway_future_garage.mp3", 0.0), fehlerton=1.1,
        szenen=[
            ("bg", None, 2.7, [ut("Eine PDF per Mail …", 0.3), ut("… ist keine E-Rechnung.", 0.8, 1),
                               gross("PDF = E-Rechnung?", 0.3, 860, "weiss", 120), gross("Nein.", 1.1, 1060, "rot", 210)]),
            ("folie", REPO / "posts/10_2026-10-22_e_rechnung/folie_02.png", 2.9, [ut("Empfangen musst du sie", 0.1), ut("schon seit 2025.", 0.7, 1, farbe="gruen")]),
            ("folie", REPO / "posts/10_2026-10-22_e_rechnung/folie_03.png", 4.2, [ut("Ausstellen ab 2027, bei über", 0.1, bis=2.4, groesse=74),
                                                                                   ut("800.000 € Vorjahresumsatz –", 0.7, 1, bis=2.4, groesse=74),
                                                                                   ut("ab 2028:", 2.4), ut("alle.", 2.8, 1, farbe="gruen", groesse=110)]),
            ("folie", REPO / "posts/10_2026-10-22_e_rechnung/folie_04.png", 3.0, [ut("Frag heute nach:", 0.1), ut("Kann euer Posteingang das lesen?", 0.7, 1, farbe="gelb", groesse=72)]),
            ("abspann", None, 3.0, [unten("Speicher dir das.", 0.1, farbe="gruen")]),
        ]),
    "21": dict(
        id="p21_reel_zinsschranke", ordner="posts/21_2026-10-22_reel_zinsschranke", titel=BIB / "reels/reel_zinsschranke/titelbild.png",
        musik=("10_runway_spannung.mp3", 0.0), fehlerton=1.0,
        szenen=[
            ("bg", None, 2.6, [ut("Zinsen voll abziehbar?", 0.3), ut("Nicht immer.", 1.0, 1, farbe="rot"),
                               gross("30 % · 3 Mio.", 0.3, 960, "gruen", 170)]),
            ("ampel", BIB / "bausteine/ampel_zins_rot.png", 3.2, [ut("Nettozinsaufwand: höchstens", 0.1, groesse=72), ut("30 % vom steuerl. EBITDA.", 0.8, 1, farbe="gelb", groesse=80)]),
            ("ampel", BIB / "bausteine/ampel_zins_gruen.png", 3.0, [ut("Unter 3 Mio. € Nettozins", 0.1), ut("greift sie gar nicht.", 0.7, 1, farbe="gruen")]),
            ("folie", BIB / f"{KR}/zinsschranke/folie_04.png", 3.6, [ut("Aber: Der Zinsvortrag geht bei", 0.1, groesse=70),
                                                                      ut("schädlichem Anteilseigner-", 0.7, 1, groesse=70, farbe="rot"),
                                                                      ut("wechsel unter (§ 8c KStG).", 0.7, 2, groesse=70, farbe="rot")]),
            ("abspann", None, 3.2, [unten("2 Zahlen: 30 %, 3 Mio.", 0.1), unten("Speicher dir das.", 0.6, 1, farbe="gruen")]),
        ]),
    "22": dict(
        id="p22_reel_steuersatz", ordner="posts/22_2026-10-18_reel_steuersatz", titel=BIB / "reels/reel_kst2032/titelbild.png",
        musik=("08_runway_chill_house.mp3", 0.0), fehlerton=1.0,
        szenen=[
            ("bg", None, 2.6, [ut("Wie oft steht dein", 0.3), ut("Steuersatz in Excel?", 0.8, 1),
                               gross("30 % an", 0.3, 860, "weiss", 170), gross("12 Stellen?", 1.0, 1060, "gelb", 170)]),
            ("folie", BIB / f"{KR}/kst_staffel/folie_02.png", 3.4, [ut("Ab 2028 sinkt die KSt", 0.1, bis=2.0), ut("jedes Jahr um 1 Punkt –", 0.7, 1, bis=2.0),
                                                                     ut("bis auf 10 %", 2.0, farbe="gruen", groesse=100), ut("ab 2032.", 2.3, 1)]),
            ("folie", BIB / f"{KR}/kst_staffel/folie_03.png", 3.0, [ut("Gesamtsatz 2032: 24,55 %", 0.1, farbe="gruen", groesse=78), ut("bei 400 % Hebesatz.", 0.7, 1)]),
            ("bg", None, 3.4, [ut("Festwerte heißt:", 0.1), ut("Zelle für Zelle ändern –", 0.6, 1),
                               gross("eine vergisst du.", 1.3, 900, "rot", 130), gross("Im Tool: eine Zelle.", 2.2, 1100, "gruen", 110)]),
            ("abspann", None, 3.4, []),  # TOOL steht im Knopf des Abspanns – Zusatztext lag auf der Fußzeile
        ]),
}


def hintergrund():
    """Dunkler Verlauf wie die Bibliotheks-Karten (Mitte ≈ #112C26, Rand ≈ #0B110E)."""
    klein = Image.new("RGB", (W // 4, H // 4))
    px = klein.load()
    for y in range(H // 4):
        for x in range(W // 4):
            d = min((((x * 4 - 540) / 760) ** 2 + ((y * 4 - 900) / 1050) ** 2) ** 0.5, 1)
            k = (1 - d) ** 1.6
            px[x, y] = tuple(round(a + (b - a) * k) for a, b in zip((11, 17, 14), (18, 46, 40)))
    return klein.resize((W, H), Image.BICUBIC)


def karte(art, quelle, bg):
    im = bg.copy()
    if art == "bg":
        return im
    q = Image.open(quelle).convert("RGB")
    if art == "folie":     # Karussell 1080x1350: nur der Inhaltsbereich (ohne leeren Kopf und Fußzeile), größer lesbar
        q = q.crop((0, 150, 1080, 1180)).resize((round(1080 * 0.86), round(1030 * 0.86)), Image.LANCZOS)
    elif art == "einzel":  # Einzelpost 1080x1080
        q = q.resize((880, 880), Image.LANCZOS)
    elif art == "ampel":   # Ampel 1080x1920: Kopf, Ampel, Prüfpunkte und Demo-Hinweis
        q = q.crop((0, 120, 1080, 1640)).resize((round(1080 * 0.58), round(1520 * 0.58)), Image.LANCZOS)
    x = (W - 120 - q.width) // 2 + 20
    y = 590 + (890 - q.height) // 2
    rahmen = Image.new("RGB", (q.width + 4, q.height + 4), (40, 86, 74))
    im.paste(rahmen, (x - 2, y - 2)); im.paste(q, (x, y))
    return im


def lufs(datei):
    r = subprocess.run(["ffmpeg", "-nostats", "-i", str(datei), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1])
    tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])
    return i, tp


def bauen(nr):
    r = REELS[nr]
    ordner = REPO / r["ordner"]
    kdir = ordner / "_karten"; kdir.mkdir(parents=True, exist_ok=True)
    if not (kdir / "abspann.png").exists():
        sys.exit(f"Abspann fehlt: erst  cd vorlagen/system && node render.mjs jobs/p18_22_notloesung_abspann.json")
    bg = hintergrund()
    szenen, t = [], 0.0
    for i, (art, quelle, dauer, texte) in enumerate(r["szenen"]):
        if art == "abspann":
            name = "abspann.png"
        else:
            name = f"szene_{i + 1}.png"
            karte(art, quelle, bg).save(kdir / name)
        sz = {"karte": f"../../{r['ordner']}/_karten/{name}", "dauer": dauer,
              "von": [540, 960, 1080], "nach": [540, 960, 1040], "text": texte}
        if i == 1: sz["rein"] = "whip"  # ein Übergang: Hook → Pointe
        szenen.append(sz)
        t += dauer
    musik, mstart = r["musik"]
    hook = r["szenen"][0][2]
    cfg = {
        "ausgabe": f"../../{r['ordner']}/reel_ohne_stimme.mp4", "fps": 30,
        "ton": [
            {"datei": "../../musik/atmo/uhr_ticken.mp3", "ab": 0, "start": 0, "dauer": hook, "lautstaerke": 0.35, "aus": 0.2},
            {"datei": "../../musik/atmo/fehlerton.mp3", "ab": r["fehlerton"], "start": 0, "dauer": 0.6, "lautstaerke": 0.5, "aus": 0.1},
            {"datei": f"../../musik/{musik}", "ab": hook - 0.15, "start": mstart, "lautstaerke": 0.5, "ein": 0.4},
        ],
        "quellen": {}, "szenen": szenen,
    }
    pfad = hier / f"{r['id']}_ohne_stimme.json"
    pfad.write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
    subprocess.run([sys.executable, str(SYSTEM / "montage.py"), str(pfad)], check=True, cwd=SYSTEM)
    video = ordner / "reel_ohne_stimme.mp4"
    i, tp = lufs(video)
    gain = ZIEL_LUFS - i
    tmp = video.with_suffix(".tmp.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(video), "-c:v", "copy",
                    "-af", f"volume={gain:.2f}dB,alimiter=limit=0.89:level=false", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(tmp)], check=True)
    tmp.replace(video)
    i2, tp2 = lufs(video)
    shutil.copy(r["titel"], ordner / "titelbild.png")
    print(f"✓ {nr}: {t:.1f} s, Ton {i:.1f} → {i2:.1f} LUFS, Peak {tp2:.1f} dBFS")


for nr in (sys.argv[1:] or REELS):
    bauen(nr)
