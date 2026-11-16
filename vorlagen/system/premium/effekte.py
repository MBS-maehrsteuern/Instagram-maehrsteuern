"""Kamera-Effekte nach dem Rendern auf die Einzelbilder legen (Gerba-Stil, Loris 16.11.):
    python3 effekte.py <frame-ordner> <effekte.json>
effekte.json: [[start_s, dauer_s, "zoom"|"whipx"|"whipy", staerke], ...]
  zoom  = Crash-Zoom mit radialer Unschärfe (staerke ≈ 0.15–0.35 = Zoom-Spreizung)
  whipx = Reißschwenk waagerecht, whipy = senkrecht (staerke ≈ Pixel Wischweg, z. B. 160)
Stärke läuft als Dreieck: 0 → voll in der Mitte → 0."""
import json, sys
from pathlib import Path
import numpy as np
from PIL import Image

ordner, eff = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text())
FPS, N = 30, 7


def zoom(im, s):
    W, H = im.size; acc = np.zeros((H, W, 3), np.float32)
    for k in range(N):
        f = 1 + s * k / (N - 1); w, h = int(W * f), int(H * f)
        z = im.resize((w, h), Image.BILINEAR).crop(((w - W) // 2, (h - H) // 2, (w - W) // 2 + W, (h - H) // 2 + H))
        acc += np.asarray(z, np.float32)
    return Image.fromarray((acc / N).astype(np.uint8))


def whip(im, px, achse):
    a = np.asarray(im, np.float32); acc = np.zeros_like(a)
    for k in range(N):
        acc += np.roll(a, int(px * (k / (N - 1) - .5)), axis=achse)
    return Image.fromarray((acc / N).astype(np.uint8))


bilder = {}
for start, dauer, art, st in eff:
    for i in range(int(start * FPS), int((start + dauer) * FPS) + 1):
        x = (i / FPS - start) / dauer
        if not 0 <= x <= 1: continue
        bilder.setdefault(i, []).append((art, st * (1 - abs(2 * x - 1))))
for i, liste in sorted(bilder.items()):
    p = ordner / f"f{i:05d}.jpg"
    if not p.exists(): continue
    im = Image.open(p).convert("RGB")
    for art, s in liste:
        if s < .01 * (1 if art == "zoom" else 100): continue
        im = zoom(im, s) if art == "zoom" else whip(im, s, 1 if art == "whipx" else 0)
    im.save(p, quality=92)
print("✓ Effekte auf", len(bilder), "Bilder")
