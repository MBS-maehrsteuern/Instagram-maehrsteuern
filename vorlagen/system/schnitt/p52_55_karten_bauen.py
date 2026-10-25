"""Reel-Karten für die Reels 52 (GoBD), 53 (IAB), 54 (Reverse-Charge) und 55 (§ 34a EStG), Nachtlauf 14.10. (d2) – gleiches Verfahren wie p24_27_karten_bauen.py:
Karussell-Folie (1080×1350) auf 9:16 setzen (nur Inhaltsbereich y 360–1200, 88 %, links 40 px → Safe-Zone frei).

    cd vorlagen/system/schnitt && python3 p52_55_karten_bauen.py
Danach:  cd vorlagen/system && node render.mjs jobs/p53_iab.json  (Story-Teaser 53 mit bausteine/teaser_karte.png)
         cd vorlagen/system && python3 montage.py schnitt/p52_reel_gobd.json  (bzw. p53_reel_iab.json, p54_reel_reverse_charge.json, p55_reel_thesaurierung.json)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[3]
B = REPO / "assets/bibliothek"
W, H, BG = 1080, 1920, (11, 17, 14)
SKALA, X, OBEN, UNTEN = 0.88, 40, 360, 1200


def ohne_nr(im):
    """Grosse gruene Karussell-Nummer (01 … 05, links oben im Inhaltsbereich) mit dem Hintergrund der Zeile uebermalen.
    Kopiert aus p36_40_karten_bauen.py. QA KW45: Im Reel 52 liefen die Nummern 04 → 03 → 05."""
    px = im.load()
    # bis y 700 statt 640: bei gobd/folie_04 und _06 reicht die Nummer bis y 672 (Titel beginnt erst ab y 727)
    gruen = [(x, y) for y in range(360, 700) for x in range(80, 330)
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


def folie_karte(folie, ziel, y=600, oben=OBEN, unten=UNTEN, nr_aus=False):
    im = Image.open(B / folie).convert("RGB")
    if nr_aus:
        im = ohne_nr(im)
    im = im.crop((0, oben, 1080, unten))
    im = im.resize((round(1080 * SKALA), round((unten - oben) * SKALA)), Image.LANCZOS)
    maske = Image.new("L", im.size, 0)
    ImageDraw.Draw(maske).rectangle((25, 25, im.width - 25, im.height - 25), fill=255)
    maske = maske.filter(ImageFilter.GaussianBlur(12))
    bild = Image.new("RGB", (W, H), BG)
    bild.paste(im, (X, y), maske)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    bild.save(ziel)
    print("✓", ziel.relative_to(REPO))


KW, KH, F = 900, 640, 2          # Kartengröße wie in story.html, doppelt aufgelöst
RAND = 70                        # Mindestabstand Inhalt → Kartenrand (in Kartenpixeln, vor F)


def inhalt_bbox(im):
    """Helle Pixel (Schrift, Pill-Rahmen) – der Hintergrund bleibt deutlich dunkler."""
    grau = im.convert("L").point(lambda v: 255 if v > 110 else 0)
    return grau.getbbox()


def teaser_karte(folie, ziel, unten=1220):
    """Teaser-Karte für Story 53 (Karussell): kopiert aus p57_58_karten_bauen.py (unten + einfarbig, QA KW45).
    Folie bei y 1220 abschneiden (Fußzeile „Wischen →“ weg), Inhalt mit Rand in die 900×640-Karte, Hintergrund #0b1210."""
    im = Image.open(folie).convert("RGB").crop((0, 0, 1080, unten))
    x0, y0, x1, y1 = inhalt_bbox(im)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    s = min((KH - 2 * RAND) / (y1 - y0), (KW - 2 * RAND) / (x1 - x0), KW / im.width * 1.0)
    klein = im.resize((round(im.width * s * F), round(im.height * s * F)), Image.LANCZOS)
    hg = Image.new("RGB", (KW * F, KH * F), (11, 18, 16))
    px, py = round(KW * F / 2 - cx * s * F), round(KH * F / 2 - cy * s * F)
    maske = Image.new("L", klein.size, 0)
    ImageDraw.Draw(maske).rectangle((40, 40, klein.width - 40, klein.height - 40), fill=255)
    hg.paste(klein, (px, py), maske.filter(ImageFilter.GaussianBlur(20)))
    hg.save(ziel)
    print(f"✓ {ziel.relative_to(REPO)}  (Skala {s / (KW / im.width):.0%} der bisherigen Karte)")


P52 = REPO / "posts/52_2026-11-04_reel_gobd/bausteine"
P53 = REPO / "posts/53_2026-11-04_iab/bausteine"
P54 = REPO / "posts/54_2026-11-05_reel_reverse_charge/bausteine"
P55 = REPO / "posts/55_2026-11-06_reel_thesaurierung/bausteine"

# QA KW45: Kartennummern ausgeblendet (04 → 03 → 05 wirkte ungeordnet)
folie_karte("karussell/gobd/folie_05.png", P52 / "karte_unveraenderbar.png", nr_aus=True)
folie_karte("karussell/gobd/folie_04.png", P52 / "karte_zeitgerecht.png", nr_aus=True)
folie_karte("karussell/gobd/folie_06.png", P52 / "karte_dokumentiert.png", nr_aus=True)

folie_karte("karussell/iab_2/folie_02.png", P53 / "karte_50.png")
folie_karte("karussell/iab_2/folie_03.png", P53 / "karte_200000.png")
# QA KW45: Story-Teaser Karussell 53 – Unterzeile von Folie 1 war unten angeschnitten
teaser_karte(P53.parent / "folie_01.png", P53 / "teaser_karte.png")

folie_karte("karussell/reverse_charge/folie_02.png", P54 / "karte_regel.png")
folie_karte("karussell/reverse_charge/folie_05.png", P54 / "karte_fehler.png")
folie_karte("karussell/reverse_charge/folie_04.png", P54 / "karte_hinweis.png")

folie_karte("karussell/thesaurierung/folie_02.png", P55 / "karte_regel.png")
folie_karte("karussell/thesaurierung/folie_03.png", P55 / "karte_nachversteuerung.png")
folie_karte("karussell/thesaurierung/folie_04.png", P55 / "karte_fuer_wen.png")
