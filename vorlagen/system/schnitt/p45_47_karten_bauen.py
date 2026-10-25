"""Reel-Karten für die Reels 45 (vGA) und 47 (Betriebsaufspaltung), Nachtlauf 14.10.
Gleiches Verfahren (Funktion kopiert) wie p24_27_karten_bauen.py (Folien-Inhaltsbereich auf 9:16, Safe-Zone).

    cd vorlagen/system/schnitt && python3 p45_47_karten_bauen.py
Danach:  cd vorlagen/system && python3 montage.py schnitt/p45_reel_vga.json  (bzw. p47_reel_betriebsaufspaltung.json)
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


P45 = REPO / "posts/45_2026-10-31_reel_vga/bausteine"
P47 = REPO / "posts/47_2026-11-01_reel_betriebsaufspaltung/bausteine"

folie_karte("karussell/vga/folie_02.png", ziel=P45 / "karte_was_ist.png")
folie_karte(P45 / "folie_klassiker3.png", ziel=P45 / "karte_klassiker.png")  # 3 statt 5 Punkte (Reel-Regel)

folie_karte("karussell/betriebsaufspaltung/folie_02.png", ziel=P47 / "karte_sachlich.png")
folie_karte("karussell/betriebsaufspaltung/folie_03.png", ziel=P47 / "karte_personell.png")
folie_karte("karussell/betriebsaufspaltung/folie_04.png", ziel=P47 / "karte_folge.png")
