"""Reel-Karten für die Reels 48 (Firmenwagen), 49 (Kleinunternehmer) und 50 (Gebäude-AfA), Nachtlauf 14.10.
Gleiches Verfahren (Funktion kopiert) wie p24_27_karten_bauen.py (Folien-Inhaltsbereich auf 9:16, Safe-Zone).

    cd vorlagen/system/schnitt && python3 p48_50_karten_bauen.py
Vorher:  node render.mjs jobs/p49_reel_kleinunternehmer.json  (Grenz-Folien mit Normbox „§ 19 Abs. 1 UStG“)
Danach:  cd vorlagen/system && python3 montage.py schnitt/p48_reel_firmenwagen.json  (bzw. p49_…, p50_…)
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


P48 = REPO / "posts/48_2026-11-02_reel_firmenwagen/bausteine"
P49 = REPO / "posts/49_2026-11-02_reel_kleinunternehmer/bausteine"
P50 = REPO / "posts/50_2026-11-03_reel_gebaeude_afa/bausteine"

folie_karte("karussell/firmenwagen/folie_05.png", ziel=P48 / "karte_fahrtenbuch.png")
folie_karte("karussell/firmenwagen/folie_02.png", ziel=P48 / "karte_1prozent.png")
folie_karte("karussell/firmenwagen/folie_03.png", ziel=P48 / "karte_arbeitsweg.png")

folie_karte(P49 / "folie_grenze1.png", ziel=P49 / "karte_vorjahr.png")
folie_karte(P49 / "folie_grenze2.png", ziel=P49 / "karte_laufend.png")
folie_karte("karussell/kleinunternehmer/folie_04.png", ziel=P49 / "karte_vorsteuer.png")

folie_karte("karussell/gebaeude_afa/folie_03.png", ziel=P50 / "karte_linear.png")
folie_karte("karussell/gebaeude_afa/folie_04.png", ziel=P50 / "karte_degressiv.png")
folie_karte("karussell/gebaeude_afa/folie_05.png", ziel=P50 / "karte_sonder.png")
