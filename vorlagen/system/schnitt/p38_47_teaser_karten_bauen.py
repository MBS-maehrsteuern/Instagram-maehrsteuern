"""Teaser-Karten für die Storys 38, 42, 45, 47 (QA KW44).
Die Teaser-Vorlage (story.html, typ teaser) zeigt das Titelbild als 900×640-Karte mit background-size: cover –
bei langen Titeln wurden Kopfzeile und @maehrsteuern-Pill angeschnitten. Hier wird das Titelbild so weit verkleinert,
dass sein Inhalt (Kopfzeile bis Pill) mit Rand in die Karte passt; die Job-Dateien zeigen auf bausteine/teaser_karte.png.

    cd vorlagen/system/schnitt && python3 p38_47_teaser_karten_bauen.py
Danach:  cd vorlagen/system && node render.mjs jobs/p38_reel_pruefpfad.json  (bzw. p42_…, p45_…, p47_…)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

REPO = Path(__file__).resolve().parents[3]
KW, KH, F = 900, 640, 2          # Kartengröße wie in story.html, doppelt aufgelöst
RAND = 70                        # Mindestabstand Inhalt → Kartenrand (in Kartenpixeln, vor F)


def inhalt_bbox(im):
    """Helle Pixel (Schrift, Pill-Rahmen) – der verwischte Dashboard-Hintergrund bleibt deutlich dunkler."""
    grau = im.convert("L").point(lambda v: 255 if v > 110 else 0)
    return grau.getbbox()


def teaser_karte(titelbild, ziel):
    im = Image.open(titelbild).convert("RGB")
    x0, y0, x1, y1 = inhalt_bbox(im)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    s = min((KH - 2 * RAND) / (y1 - y0), (KW - 2 * RAND) / (x1 - x0), KW / im.width * 1.0)
    klein = im.resize((round(im.width * s * F), round(im.height * s * F)), Image.LANCZOS)
    # Hintergrund: Titelbild formatfüllend, stark verwischt und abgedunkelt
    hg = im.resize((KW * F, round(im.height * KW * F / im.width)), Image.LANCZOS)
    top = max(0, round(cy * KW * F / im.width - KH * F / 2))
    hg = hg.crop((0, top, KW * F, top + KH * F)).filter(ImageFilter.GaussianBlur(30))
    hg = Image.blend(hg, Image.new("RGB", hg.size, (8, 13, 11)), 0.75)
    px, py = round(KW * F / 2 - cx * s * F), round(KH * F / 2 - cy * s * F)
    maske = Image.new("L", klein.size, 0)
    ImageDraw.Draw(maske).rectangle((40, 40, klein.width - 40, klein.height - 40), fill=255)
    hg.paste(klein, (px, py), maske.filter(ImageFilter.GaussianBlur(20)))
    hg.save(ziel)
    print(f"✓ {ziel.relative_to(REPO)}  (Skala {s / (KW / im.width):.0%} der bisherigen Karte)")


for ordner in ["38_2026-10-27_reel_pruefpfad", "42_2026-10-29_reel_afa",
               "45_2026-10-31_reel_vga", "47_2026-11-01_reel_betriebsaufspaltung"]:
    p = REPO / "posts" / ordner
    teaser_karte(p / "titelbild.png", p / "bausteine/teaser_karte.png")
