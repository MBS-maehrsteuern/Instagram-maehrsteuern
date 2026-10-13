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


def folie_karte(folie, ziel, y=600, overlays=()):
    im = Image.open(folie).convert("RGB").crop((0, OBEN, 1080, UNTEN))
    im = im.resize((round(1080 * SKALA), round((UNTEN - OBEN) * SKALA)), Image.LANCZOS)
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
folie_karte(K / "bp_vorbereitung/folie_04.png", P38 / "karte_verfahrensdoku.png", y=640,
            overlays=[(P38 / "leiste_pruefpfad.png", 0.86, (40, 300))])
folie_karte(K / "bp_vorbereitung/folie_03.png", P38 / "karte_datenzugriff.png", y=420,
            overlays=[(P38 / "haken_ueber_pruefpfad.png", 0.84, (40, 1060))])

folie_karte(K / "holding/folie_02.png", P39 / "karte_regel.png")
folie_karte(K / "holding/folie_03.png", P39 / "karte_rechnung.png")

folie_karte(K / "excel_formeln/folie_06.png", P40 / "karte_wennfehler.png")
folie_karte(K / "excel_formeln/folie_02.png", P40 / "karte_xverweis.png")
folie_karte(K / "excel_formeln/folie_05.png", P40 / "karte_namen.png")
