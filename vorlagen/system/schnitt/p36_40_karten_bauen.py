"""Reel-Karten für die Reels 36, 38, 39, 40 (Nachtlauf 14.10.) – gleiches Verfahren wie p24_27_karten_bauen.py:
Karussell-Folie (1080×1350) auf 9:16 setzen, transparente Einblendungen (leiste_*, haken_ueber_*) verkleinert in die Safe-Zone legen.

    cd vorlagen/system/schnitt && python3 p36_40_karten_bauen.py
Danach je Reel:  cd vorlagen/system && python3 montage.py schnitt/p36_reel_bewirtung.json (bzw. p38_…, p39_…, p40_…)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[3]
B = REPO / "assets/bibliothek"
W, H, BG = 1080, 1920, (11, 17, 14)
SKALA, X, OBEN, UNTEN = 0.88, 40, 360, 1200


def overlay(bild, datei, skala, xy):
    """Transparente Einblendung auf ihren Inhalt zuschneiden, verkleinern und an xy setzen (Safe-Zone: rechts 120 px frei)."""
    o = Image.open(datei).convert("RGBA")
    o = o.crop(o.getchannel("A").getbbox())
    o = o.resize((round(o.width * skala), round(o.height * skala)), Image.LANCZOS)
    bild.alpha_composite(o, xy)


def ohne_nr(im):
    """Grosse gruene Karussell-Nummer (01 … 05, links oben im Inhaltsbereich) mit dem Hintergrund der Zeile uebermalen.
    QA KW44: Im Reel wirkten die Nummern wie eine falsche Reihenfolge (38: 03 vor 02, 40: 05 → 01 → 04)."""
    px = im.load()
    gruen = [(x, y) for y in range(360, 640) for x in range(80, 330)
             if px[x, y][1] > 120 and px[x, y][1] > px[x, y][0] + 40]
    if not gruen:
        return im
    zeilen = sorted({p[1] for p in gruen})  # nur der erste zusammenhängende Zeilenblock = Nummer (darunter folgt der grüne Titel)
    ende = zeilen[0]
    for z in zeilen[1:]:
        if z - ende > 6:
            break
        ende = z
    gruen = [p for p in gruen if p[1] <= ende]
    x0, x1 = min(p[0] for p in gruen) - 10, max(p[0] for p in gruen) + 10
    y0, y1 = min(p[1] for p in gruen) - 10, max(p[1] for p in gruen) + 10
    for y in range(y0, y1 + 1):
        ref = [px[x, y] for x in range(20, 70)]
        farbe = tuple(sum(c[i] for c in ref) // len(ref) for i in range(3))
        for x in range(x0, x1 + 1):
            px[x, y] = farbe
    return im


def folie_karte(folie, ziel, y=600, overlays=(), oben=OBEN, unten=UNTEN, nr_aus=False):
    im = Image.open(folie).convert("RGB")
    if nr_aus:
        im = ohne_nr(im)
    im = im.crop((0, oben, 1080, unten))
    im = im.resize((round(1080 * SKALA), round((unten - oben) * SKALA)), Image.LANCZOS)
    maske = Image.new("L", im.size, 0)
    ImageDraw.Draw(maske).rectangle((25, 25, im.width - 25, im.height - 25), fill=255)
    maske = maske.filter(ImageFilter.GaussianBlur(12))
    bild = Image.new("RGB", (W, H), BG)
    bild.paste(im, (X, y), maske)
    bild = bild.convert("RGBA")
    for datei, skala, xy in overlays:
        overlay(bild, datei, skala, xy)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    bild.convert("RGB").save(ziel)
    print("✓", ziel.relative_to(REPO))


P36 = REPO / "posts/36_2026-10-26_reel_bewirtung/bausteine"
P38 = REPO / "posts/38_2026-10-27_reel_pruefpfad/bausteine"
P39 = REPO / "posts/39_2026-10-28_reel_holding/bausteine"
P40 = REPO / "posts/40_2026-10-28_reel_formeln/bausteine"
K = B / "karussell"

folie_karte(K / "bewirtung/folie_02.png", P36 / "karte_70.png")

# Reel 38: Folien des Begleit-Karussells 37 (bp_vorbereitung) + Prüfpfad-Einblendungen aus der Bibliothek (R1/R2)
# QA KW44: Kartennummern ausgeblendet (03 lief vor 02); Folie 3 aus Post 37 (neu gerendert, § 147 Abs. 6 AO aktuelle Fassung);
# Box „Ein Klick. Eine Quelle.“ höher, damit der Rahmen auch nach dem Zoom über y 1500 endet.
folie_karte(K / "bp_vorbereitung/folie_04.png", P38 / "karte_verfahrensdoku.png", y=640, nr_aus=True,
            overlays=[(P38 / "leiste_pruefpfad.png", 0.86, (40, 300))])
folie_karte(REPO / "posts/37_2026-10-27_bp_vorbereitung/folie_03.png", P38 / "karte_datenzugriff.png", y=420, oben=540, nr_aus=True,
            overlays=[(P38 / "haken_ueber_pruefpfad.png", 0.84, (40, 990))])

folie_karte(K / "holding/folie_02.png", P39 / "karte_regel.png")
folie_karte(K / "holding/folie_03.png", P39 / "karte_rechnung.png")

# QA KW44: Kartennummern ausgeblendet (05 → 01 → 04 wirkte ungeordnet)
folie_karte(K / "excel_formeln/folie_06.png", P40 / "karte_wennfehler.png", nr_aus=True)
folie_karte(K / "excel_formeln/folie_02.png", P40 / "karte_xverweis.png", nr_aus=True)
folie_karte(K / "excel_formeln/folie_05.png", P40 / "karte_namen.png", nr_aus=True)
