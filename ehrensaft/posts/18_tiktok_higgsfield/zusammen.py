"""Echtes Flaschen-Video (schnitt.py) + transparente Grafik-Ebene (render_overlay.mjs) zusammenlegen.
python3 zusammen.py <footage_frames> <overlay_frames> <ziel_frames>"""
import sys
from pathlib import Path
from PIL import Image
import numpy as np
fo, ov, ziel = map(Path, sys.argv[1:4]); ziel.mkdir(parents=True, exist_ok=True)
fs = sorted(fo.glob("f*.jpg")); os_ = sorted(ov.glob("o*.png"))
# leichter Verlauf oben/unten, damit Schrift und Hinweis auf jedem Hintergrund lesbar bleiben
y = np.linspace(0, 1, 1920)[:, None]
a = np.clip(np.maximum((0.22 - y) / 0.22, (y - 0.70) / 0.30), 0, 1) * 0.22
verlauf = Image.fromarray(np.dstack([np.full((1920, 1080, 3), 13, np.uint8), (np.repeat(a, 1080, 1) * 255).astype(np.uint8)]), "RGBA")
for i, o in enumerate(os_):
    b = Image.open(fs[min(i, len(fs) - 1)]).convert("RGBA")
    b.alpha_composite(verlauf); b.alpha_composite(Image.open(o).convert("RGBA"))
    b.convert("RGB").save(ziel / f"f{i:05d}.jpg", quality=93)
print("✓", len(os_), "Bilder")
