"""Reel-Karten für die Reels 42 (degressive AfA) und 43 (§ 35 EStG), Nachtlauf 14.10. – gleiches Verfahren wie p24_27_karten_bauen.py:
Karussell-Folie (1080×1350) auf 9:16 setzen (nur Inhaltsbereich y 360–1200, 88 %, links 40 px → Safe-Zone frei).

    cd vorlagen/system/schnitt && python3 p41_44_karten_bauen.py
Danach:  cd vorlagen/system && python3 montage.py schnitt/p42_reel_afa.json  (bzw. p43_reel_par35.json)
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


P42 = REPO / "posts/42_2026-10-29_reel_afa/bausteine"
P43 = REPO / "posts/43_2026-10-30_reel_par35/bausteine"

folie_karte("karussell/afa_degressiv/folie_02.png", P42 / "karte_regeln.png")
folie_karte("karussell/afa_degressiv/folie_03.png", P42 / "karte_beispiel.png")

folie_karte("karussell/par35/folie_03.png", P43 / "karte_messzahl.png")
folie_karte(P43 / "folie_schritt3.png", P43 / "karte_4fach.png")  # QA KW44: eigene Folie „Die ESt sinkt um das 4,0-Fache.“ statt „zurück“ (Job p43_reel_par35.json)
folie_karte("karussell/par35/folie_05.png", P43 / "karte_400.png")
