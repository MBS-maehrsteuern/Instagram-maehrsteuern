"""Standbilder für die Reels 28 (Zuschläge) und 30 (GWG): dunkler Hintergrund + Karussell-Folie als Karte.
Aufruf (im Ordner vorlagen/system): python3 schnitt/p28_p30_material.py  – danach montage.py mit p28_/p30_-JSON."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

W, H = 1080, 1920
root = Path(__file__).resolve().parents[3]
bib = root / "assets/bibliothek"


def hintergrund():
    """Radialer Verlauf im Serien-Stil (dunkelgrün), ohne App-Screenshot (keine Daten im Bild)."""
    bg = Image.new("RGB", (W, H), (9, 15, 13))
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W * 0.5 - 520, H * 0.42 - 620, W * 0.5 + 520, H * 0.42 + 620), fill=255)
    glow = glow.filter(ImageFilter.GaussianBlur(260))
    farbe = Image.new("RGB", (W, H), (22, 62, 50))
    return Image.composite(farbe, bg, glow)


def ohne_zaehler(f):
    """Karussell-Zähler unten rechts („3/7“) mit der Hintergrundfarbe daneben übermalen – im Reel ohne Sinn (und bei 28 in falscher Reihenfolge)."""
    d = ImageDraw.Draw(f)
    for y in range(1230, 1310):
        d.line((880, y, 1060, y), fill=f.getpixel((870, y)))
    return f


def karte(folie, y=470, skala=0.9, zaehler=True):
    bild = hintergrund()
    f = Image.open(folie).convert("RGB")
    if not zaehler: f = ohne_zaehler(f)
    f = f.resize((round(f.width * skala), round(f.height * skala)), Image.LANCZOS)
    x = (W - f.width) // 2
    schatten = Image.new("L", (W, H), 0)
    ImageDraw.Draw(schatten).rounded_rectangle((x + 6, y + 18, x + f.width + 6, y + f.height + 18), 36, fill=170)
    bild.paste((0, 0, 0), (0, 0), schatten.filter(ImageFilter.GaussianBlur(28)))
    maske = Image.new("L", f.size, 0)
    ImageDraw.Draw(maske).rounded_rectangle((0, 0, f.width - 1, f.height - 1), 32, fill=255)
    bild.paste(f, (x, y), maske)
    rahmen = ImageDraw.Draw(bild)
    rahmen.rounded_rectangle((x, y, x + f.width - 1, y + f.height - 1), 32, outline=(83, 195, 162), width=3)
    return bild


auftraege = {
    root / "posts/28_2026-10-19_reel_zuschlaege/material": {
        "hintergrund.png": None,
        "karte_saeumnis.png": (bib / "karussell/fristen_ao/folie_03.png", False),  # 14.10.: Zähler 3/7 vor 2/7 ausgeblendet
        "karte_verspaetung.png": (bib / "karussell/fristen_ao/folie_02.png", False),
    },
    root / "posts/30_2026-10-21_reel_gwg/material": {
        "hintergrund.png": None,
        "karte_schwellen.png": bib / "karussell/gwg/folie_02.png",
        "karte_einheitlich.png": bib / "karussell/gwg/folie_03.png",
    },
}
for ordner, dateien in auftraege.items():
    ordner.mkdir(parents=True, exist_ok=True)
    for name, quelle in dateien.items():
        if isinstance(quelle, tuple): quelle, zaehler = quelle
        else: zaehler = True
        (hintergrund() if quelle is None else karte(quelle, zaehler=zaehler)).save(ordner / name)
        print("✓", ordner / name)
