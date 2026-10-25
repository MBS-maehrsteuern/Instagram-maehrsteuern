"""Reel-Karten für die Reels 24, 25, 27 (Nachtlauf 14.10.): Karussell-Folie (1080×1350) auf 9:16 setzen, transparente
Einblendungen (leiste_*, haken_ueber_*) darüberlegen. montage.py liest "karte" als RGB – Transparenz muss vorher verrechnet werden.

    cd vorlagen/system/schnitt && python3 p24_27_karten_bauen.py
Danach je Reel:  cd vorlagen/system && python3 montage.py schnitt/p24_reel_ein_euro.json (bzw. p25_…, p27_…)

Folie: nur der Inhaltsbereich (y 360–1200), auf 88 % verkleinert, links 40 px: Inhalt bleibt in der Safe-Zone (oben 250, unten 420, rechts 120 px frei).
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


P24 = REPO / "posts/24_2026-10-16_reel_ein_euro/bausteine"
P25 = REPO / "posts/25_2026-10-17_reel_plausi/bausteine"
P27 = REPO / "posts/27_2026-10-18_reel_organschaft/bausteine"

folie_karte("karussell/ein_euro/folie_02.png", ziel=P24 / "karte_ebene1.png")
folie_karte("karussell/ein_euro/folie_03.png", ziel=P24 / "karte_ebene2.png")
folie_karte("karussell/ein_euro/folie_04.png", ziel=P24 / "karte_gesamt.png")

# Reel 25: Folien und Einblendungen mit Nummer 1–3 neu gerendert (jobs/p25_reel_plausi.json, Texte aus r5_17/r5_25)
folie_karte(P25 / "folie_check1.png", [P25 / "leiste_check1.png"], P25 / "karte_susa.png")
folie_karte(P25 / "folie_check2.png", [P25 / "leiste_check2.png"], P25 / "karte_vorjahr.png")
folie_karte(P25 / "folie_check3.png", [P25 / "haken_ueber_check3.png"], P25 / "karte_pruefspalte.png", y=800)

folie_karte("karussell/organschaft/folie_04.png", ziel=P27 / "karte_5_jahre.png")
