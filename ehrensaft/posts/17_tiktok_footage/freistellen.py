"""Boden + Schatten wie beim Greenscreen durch cleanes Ehrensaft-Hellgelb ersetzen (Loris 16.11.).
Boden ist beige (Farbton Orange-Gelb, mittlere Sättigung) – Flasche ist dunkelrot/blau/klar und hebt sich ab.
python3 freistellen.py <frames_ein> <frames_aus> [nur_diese_nummern,…]"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

GELB = np.array([255, 243, 176], np.float32)      # helles Zitronengelb (#FFF3B0), Mitte etwas heller
ein, aus = Path(sys.argv[1]), Path(sys.argv[2]); aus.mkdir(parents=True, exist_ok=True)
nur = {int(x) for x in sys.argv[3].split(",")} if len(sys.argv) > 3 else None
y, x = np.mgrid[0:1920, 0:1080].astype(np.float32)
licht = 1 - 0.07 * np.clip(((x - 540) / 900) ** 2 + ((y - 900) / 1300) ** 2, 0, 1)  # leichter Lichtverlauf, sonst flach
grund = (GELB[None, None, :] * licht[..., None]).clip(0, 255)


def huelle(pkt):
    """Konvexe Hülle (Monotone Chain) einer Punktwolke [(x, y), …]."""
    pkt = sorted(set(map(tuple, pkt)))
    if len(pkt) < 3: return pkt
    kreuz = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    unten, oben = [], []
    for q in pkt:
        while len(unten) >= 2 and kreuz(unten[-2], unten[-1], q) <= 0: unten.pop()
        unten.append(q)
    for q in reversed(pkt):
        while len(oben) >= 2 and kreuz(oben[-2], oben[-1], q) <= 0: oben.pop()
        oben.append(q)
    return unten[:-1] + oben[:-1]


def masken(im):
    hsv = np.asarray(im.convert("HSV"), np.float32)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    # Boden/Schatten: Farbton ~15–50° (PIL 0–255 → 8–38), etwas Sättigung, nicht zu dunkel
    boden = (h >= 12) & (h <= 40) & (s >= 25) & (s <= 160) & (v >= 70)   # Saft: v < 50 · Boden/Schatten: v 70–200
    m = Image.fromarray((boden * 255).astype(np.uint8))
    m = m.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(7)).filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.GaussianBlur(2))
    boden = np.asarray(m, np.float32) / 255
    # Flasche: alles außer Boden (+ Deckel/Saft sicher) → konvexe Hülle = Flaschenform (inkl. klarem Plastik dazwischen)
    deckel = (h >= 140) & (h <= 190) & (s >= 70) & (v >= 40)
    saft = ((h >= 200) | (h <= 6)) & (s >= 35) & (v <= 170) & (v >= 12)
    nicht_boden = (boden < 0.5) | deckel | saft      # alles, was kein Boden ist (Sprenkel fliegen unten raus)
    k = Image.fromarray((nicht_boden * 255).astype(np.uint8)).resize((270, 480), Image.BOX)
    k = k.point(lambda p: 255 if p > 140 else 0).filter(ImageFilter.MinFilter(7)).filter(ImageFilter.MaxFilter(7))
    ys, xs = np.nonzero(np.asarray(k))
    if len(xs) > 30:                                  # Ausreißer (Schuhe am Rand) aus der Flaschenform werfen
        d = np.hypot(xs - np.median(xs), ys - np.median(ys)); ok = d <= 2.0 * np.median(d) + 8; xs, ys = xs[ok], ys[ok]
    flasche = Image.new("L", (1080, 1920), 0)
    if len(xs) > 30:
        from PIL import ImageDraw
        ImageDraw.Draw(flasche).polygon([(x * 4 + 2, y * 4 + 2) for x, y in huelle(np.c_[xs, ys])], fill=255)
        flasche = flasche.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(6))
    fl = np.asarray(flasche, np.float32) / 255
    # außen: alles Gelb · innen: durchscheinender Boden wird gelb (klares Plastik vor gelbem Grund)
    return (1 - fl) + fl * boden


for f in sorted(ein.glob("f*.jpg")):
    i = int(f.stem[1:])
    if nur is not None and i not in nur: continue
    im = Image.open(f).convert("RGB"); a = masken(im)[..., None]
    out = np.asarray(im, np.float32) * (1 - a) + grund * a
    Image.fromarray(out.astype(np.uint8)).save(aus / f.name, quality=93)
print("✓ freigestellt")
