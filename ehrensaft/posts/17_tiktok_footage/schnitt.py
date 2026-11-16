"""Ehrensaft-TikTok aus echtem Flaschen-Video, auf den Song geschnitten (Loris 16.11.).
Song wird in TikTok gesetzt: „Flower In A Hurricane“ ab 0:44 → Drop bei 3,74 s, Schlag 0,47603 s, CTA (Gesang) bei 17,545 s.
Aufruf: python3 schnitt.py <quelle.mp4> <frames_ordner>   → Einzelbilder f%05d.jpg (30 fps, 1080×1920)
Jede Szene: [quelle_start_s, tempo (0.5 = Zeitlupe), zoom, x_versatz (-1…1), länge in Schlägen, optional y_versatz (-1…1)]"""
import subprocess, sys, json
from pathlib import Path
B, DROP = 0.47603, 3.74
SZENEN = [
  # Hook (leiser Aufbau, 3,74 s): Makro auf den Saft, Zeitlupe
  [19.2, 0.45, 1.2, 0.0, DROP / B],
  # Drop: Held von unten
  [8.45, 0.5, 1.15, 0.0, 4],
  # Drohne von oben auf den Deckel
  [14.95, 0.5, 1.2, 0.0, 4],
  # Flasche kippt / rollt am Boden
  [6.0, 0.5, 1.25, 0.1, 4],
  # Nah von vorn
  [12.0, 0.5, 1.45, 0.0, 4, 1.0],
  # Flasche dreht sich
  [20.4, 0.5, 1.2, 0.0, 4],
  # ein Schnitt pro Schlag
  [22.1, 1, 1.3, 0.0, 1], [24.0, 1, 1.25, 0.0, 1], [17.6, 1, 1.3, 0.0, 1], [20.9, 1, 1.25, 0.0, 1],
  [9.3, 1, 1.25, 0.0, 1], [6.5, 1, 1.3, 0.1, 1], [15.4, 1, 1.25, 0.0, 1], [12.6, 1, 1.5, 0.0, 1],
  # „Du weißt Bescheid“ + CTA bis Ende: Held von vorn, Zeitlupe
  [23.15, 0.5, 1.5, 0.0, 11],
]
quelle, ziel = sys.argv[1], Path(sys.argv[2]); ziel.mkdir(parents=True, exist_ok=True)
t, n = 0.0, 0                                                   # Szene für Szene (spart Speicher)
for s, tempo, z, xv, schlaege, *yv in SZENEN:
    dauer = schlaege * B; bilder = round((t + dauer) * 30) - n
    w, h = int(1080 / z) // 2 * 2, int(1920 / z) // 2 * 2
    x = f"(iw-{w})/2+{xv}*(iw-{w})/2"
    vf = (f"setpts=(PTS-STARTPTS)/{tempo},fps=30,crop={w}:{h}:{x}:(ih-{h})/2+{yv[0] if yv else 0}*(ih-{h})/2,scale=1080:1920:flags=lanczos,"
          f"eq=contrast=1.12:saturation=1.25:gamma=0.95")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-t", f"{dauer * tempo + 0.2:.3f}", "-i", quelle, "-an", "-vf", vf,
                    "-frames:v", str(bilder), "-start_number", str(n), "-q:v", "2", str(ziel / "f%05d.jpg")], check=True)
    n += bilder; t += dauer
print(f"✓ {n} Bilder, Gesamtlänge {t:.2f} s")
