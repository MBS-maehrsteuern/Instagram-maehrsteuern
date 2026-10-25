"""Reel-Karten für die Reels 57 (§ 8c KStG) und 58 (Vorsteuer), Nachtlauf 14.10.
Gleiches Verfahren (Funktion kopiert) wie p24_27_karten_bauen.py (Folien-Inhaltsbereich auf 9:16, Safe-Zone).

    Vorher:  cd vorlagen/system && node render.mjs jobs/p57_reel_verlust_8c.json  (bausteine/folie_anker.png)
    cd vorlagen/system/schnitt && python3 p57_58_karten_bauen.py
Danach:  cd vorlagen/system && python3 montage.py schnitt/p57_reel_verlust_8c.json  (bzw. p58_reel_vorsteuer.json)

Teaser-Karten für die Storys 57 und 59: Funktion teaser_karte kopiert aus p38_47_teaser_karten_bauen.py (QA KW44).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[3]
B = REPO / "assets/bibliothek"
W, H, BG = 1080, 1920, (11, 17, 14)
SKALA, X, OBEN, UNTEN = 0.88, 40, 360, 1200


def folie_karte(folie, overlays=(), ziel=None, y=600):
    """y = Oberkante des Folienausschnitts; darüber (250 … y) ist Platz für die großen Reel-Texte."""
    im = Image.open(folie if isinstance(folie, Path) else B / folie).convert("RGB").crop((0, OBEN, 1080, UNTEN))
    im = im.resize((round(1080 * SKALA), round((UNTEN - OBEN) * SKALA)), Image.LANCZOS)
    maske = Image.new("L", im.size, 0)  # weiche Kanten, damit kein Rand zur Leinwand sichtbar ist
    ImageDraw.Draw(maske).rectangle((25, 25, im.width - 25, im.height - 25), fill=255)
    maske = maske.filter(ImageFilter.GaussianBlur(12))
    bild = Image.new("RGB", (W, H), BG)
    bild.paste(im, (X, y), maske)
    bild = bild.convert("RGBA")
    for o in overlays:
        bild.alpha_composite(Image.open(o if isinstance(o, Path) else B / o).convert("RGBA"))
    ziel.parent.mkdir(parents=True, exist_ok=True)
    bild.convert("RGB").save(ziel)
    print("✓", ziel.relative_to(REPO))


KW, KH, F = 900, 640, 2          # Kartengröße wie in story.html, doppelt aufgelöst
RAND = 70                        # Mindestabstand Inhalt → Kartenrand (in Kartenpixeln, vor F)


def inhalt_bbox(im):
    """Helle Pixel (Schrift, Pill-Rahmen) – der verwischte Dashboard-Hintergrund bleibt deutlich dunkler."""
    grau = im.convert("L").point(lambda v: 255 if v > 110 else 0)
    return grau.getbbox()


def teaser_karte(titelbild, ziel, unten=None, einfarbig=False):
    """unten: Bild vorher bei dieser Höhe abschneiden (Karussell-Folie: Fußzeile „@maehrsteuern · Wischen →“ weg).
    einfarbig: Hintergrund der Karte einfarbig statt verwischter Kopie (QA KW45: bei 59 schimmerte links ein Doppelbild durch)."""
    im = Image.open(titelbild).convert("RGB")
    if unten:
        im = im.crop((0, 0, im.width, unten))
    x0, y0, x1, y1 = inhalt_bbox(im)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    s = min((KH - 2 * RAND) / (y1 - y0), (KW - 2 * RAND) / (x1 - x0), KW / im.width * 1.0)
    klein = im.resize((round(im.width * s * F), round(im.height * s * F)), Image.LANCZOS)
    # Hintergrund: Titelbild formatfüllend, stark verwischt und abgedunkelt
    hg = im.resize((KW * F, round(im.height * KW * F / im.width)), Image.LANCZOS)
    top = max(0, round(cy * KW * F / im.width - KH * F / 2))
    hg = hg.crop((0, top, KW * F, top + KH * F)).filter(ImageFilter.GaussianBlur(30))
    hg = Image.blend(hg, Image.new("RGB", hg.size, (8, 13, 11)), 0.5)
    if einfarbig:
        hg = Image.new("RGB", hg.size, (11, 18, 16))  # #0b1210
    px, py = round(KW * F / 2 - cx * s * F), round(KH * F / 2 - cy * s * F)
    maske = Image.new("L", klein.size, 0)
    ImageDraw.Draw(maske).rectangle((40, 40, klein.width - 40, klein.height - 40), fill=255)
    hg.paste(klein, (px, py), maske.filter(ImageFilter.GaussianBlur(20)))
    hg.save(ziel)
    print(f"✓ {ziel.relative_to(REPO)}  (Skala {s / (KW / im.width):.0%} der bisherigen Karte)")



P57 = REPO / "posts/57_2026-11-07_reel_verlust_8c/bausteine"
P58 = REPO / "posts/58_2026-11-08_reel_vorsteuer/bausteine"

folie_karte("karussell/par8c/folie_02.png", ziel=P57 / "karte_regel.png")
# QA KW45: Normbox „Sätze 4–8“ statt „4–9“ – Folie aus jobs/p57_reel_verlust_8c.json, Bibliothek par8c unverändert
folie_karte(P57 / "folie_anker.png", ziel=P57 / "karte_anker.png")

folie_karte("karussell/vorsteuer/folie_04.png", ziel=P58 / "karte_rechnung.png")
folie_karte(P58 / "folie_pflicht3.png", ziel=P58 / "karte_pflicht.png")  # 3 statt 5 Punkte (Reel-Regel)

teaser_karte(P57.parent / "titelbild.png", P57 / "teaser_karte.png")
# QA KW45: Fußzeile (y ab ca. 1240) weggeschnitten, Hintergrund einfarbig
teaser_karte(REPO / "posts/59_2026-11-08_pensionen/folie_01.png", REPO / "posts/59_2026-11-08_pensionen/bausteine/teaser_karte.png",
             unten=1220, einfarbig=True)
