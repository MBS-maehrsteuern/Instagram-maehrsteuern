"""Reel-Karten für die Reels 52 (GoBD), 53 (IAB), 54 (Reverse-Charge) und 55 (§ 34a EStG), Nachtlauf 14.10. (d2) – gleiches Verfahren wie p24_27_karten_bauen.py:
Karussell-Folie (1080×1350) auf 9:16 setzen (nur Inhaltsbereich y 360–1200, 88 %, links 40 px → Safe-Zone frei).

    cd vorlagen/system/schnitt && python3 p52_55_karten_bauen.py
Danach:  cd vorlagen/system && python3 montage.py schnitt/p52_reel_gobd.json  (bzw. p53_reel_iab.json, p54_reel_reverse_charge.json, p55_reel_thesaurierung.json)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[3]
B = REPO / "assets/bibliothek"
W, H, BG = 1080, 1920, (11, 17, 14)
SKALA, X, OBEN, UNTEN = 0.88, 40, 360, 1200


def folie_karte(folie, ziel, y=600, oben=OBEN, unten=UNTEN):
    im = Image.open(B / folie).convert("RGB").crop((0, oben, 1080, unten))
    im = im.resize((round(1080 * SKALA), round((unten - oben) * SKALA)), Image.LANCZOS)
    maske = Image.new("L", im.size, 0)
    ImageDraw.Draw(maske).rectangle((25, 25, im.width - 25, im.height - 25), fill=255)
    maske = maske.filter(ImageFilter.GaussianBlur(12))
    bild = Image.new("RGB", (W, H), BG)
    bild.paste(im, (X, y), maske)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    bild.save(ziel)
    print("✓", ziel.relative_to(REPO))


P52 = REPO / "posts/52_2026-11-04_reel_gobd/bausteine"
P53 = REPO / "posts/53_2026-11-04_iab/bausteine"
P54 = REPO / "posts/54_2026-11-05_reel_reverse_charge/bausteine"
P55 = REPO / "posts/55_2026-11-06_reel_thesaurierung/bausteine"

folie_karte("karussell/gobd/folie_05.png", P52 / "karte_unveraenderbar.png")
folie_karte("karussell/gobd/folie_04.png", P52 / "karte_zeitgerecht.png")
folie_karte("karussell/gobd/folie_06.png", P52 / "karte_dokumentiert.png")

folie_karte("karussell/iab_2/folie_02.png", P53 / "karte_50.png")
folie_karte("karussell/iab_2/folie_03.png", P53 / "karte_200000.png")

folie_karte("karussell/reverse_charge/folie_02.png", P54 / "karte_regel.png")
folie_karte("karussell/reverse_charge/folie_05.png", P54 / "karte_fehler.png")
folie_karte("karussell/reverse_charge/folie_04.png", P54 / "karte_hinweis.png")

folie_karte("karussell/thesaurierung/folie_02.png", P55 / "karte_regel.png")
folie_karte("karussell/thesaurierung/folie_03.png", P55 / "karte_nachversteuerung.png")
folie_karte("karussell/thesaurierung/folie_04.png", P55 / "karte_fuer_wen.png")
