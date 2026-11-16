"""Ehrensaft-TikTok aus 2 Higgsfield-Shots, auf den Song geschnitten (Song in TikTok ab 0:44).
A = Crash-Zoom + Splash (Einschlag bei 0,95 s), C = Held mit Orbit. Hintergrund wird auf helles Zitronengelb gegradet.
python3 schnitt.py <A.mp4> <C.mp4> <frames_ordner>
Szene: [quelle, start_s, tempo, zoom, x(-1..1), y(-1..1), drehung_grad, spiegeln, dauer_s]"""
import math, subprocess, sys
from pathlib import Path
B, DROP = 0.47603, 3.74
BEAT = lambda k: DROP + k * B
q = {"A": sys.argv[1], "C": sys.argv[2]}; ziel = Path(sys.argv[3]); ziel.mkdir(parents=True, exist_ok=True)
S = [["C", 0.0, 0.62, 2.0, 0, -0.45, -4, 0, DROP - 0.95],   # Hook: Makro auf Hals + Himbeere, Zeitlupe
     ["A", 0.0, 1.0, 1.0, 0, 0, 0, 0, 0.95],                # Crash-Zoom, Einschlag genau auf dem Drop
     ["A", 0.95, 0.5, 1.0, 0, 0, 0, 0, 4 * B],              # Drop: Splash in Zeitlupe
     ["A", 1.9, 0.5, 1.45, 0, -0.55, 8, 0, 4 * B],          # Früchte fliegen, schräg
     ["C", 1.0, 1.0, 1.25, 0, 0, -6, 0, 4 * B],             # Orbit
     ["A", 2.85, 0.6, 1.7, 0, 0.05, 0, 0, 4 * B],           # Makro Früchte im Saft
     ["C", 2.0, 1.0, 1.7, 0.2, 0.45, 5, 1, 4 * B]]          # Himbeeren am Boden, gespiegelt
for s, z, rot, fl, y in [("A", 1.3, 0, 0, 0), ("C", 1.8, -10, 0, -0.3), ("A", 1.6, 0, 0, -0.4), ("C", 1.3, 0, 1, 0),
                         ("A", 2.0, 0, 0, 0.1), ("C", 1.5, 12, 0, 0), ("A", 1.2, 0, 1, 0), ("C", 2.2, 0, 0, 0.35)]:
    S.append([s, {"A": 1.2, "C": 0.5}[s] + 0.3 * len(S) % 2.2, 1.0, z, 0, y, rot, fl, B])   # ein Schnitt pro Schlag
S.append(["A", 3.3, 0.7, 1.4, 0, -0.1, 0, 0, B])                                             # „Du weißt Bescheid“
S.append(["C", 0.0, 4.0 / (22.4 - BEAT(29)), 1.08, 0, 0.05, 0, 0, 22.4 - BEAT(29)])            # CTA: Held, ruhig
GRADE = ("colorbalance=rs=.06:gs=.03:bs=-.10:rm=.07:gm=.04:bm=-.10:rh=.06:gh=.05:bh=-.06,"
         "eq=brightness=0.09:contrast=1.06:saturation=1.15:gamma=1.06")
t, n = 0.0, 0
for src, st, tempo, z, xv, yv, rot, fl, dauer in S:
    th = math.radians(abs(rot)); z = max(z, math.cos(th) + 1920 / 1080 * math.sin(th) + 0.02)
    W, H = int(1080 * z) // 2 * 2, int(1920 * z) // 2 * 2
    bilder = round((t + dauer) * 30) - n
    vf = (f"setpts=(PTS-STARTPTS)/{tempo},fps=30,scale={W}:{H}:flags=lanczos," + ("hflip," if fl else "")
          + (f"rotate={math.radians(rot):.4f}:ow=iw:oh=ih," if rot else "")
          + f"crop=1080:1920:(iw-1080)/2+{xv}*(iw-1080)/2:(ih-1920)/2+{yv}*(ih-1920)/2," + GRADE)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{st:.3f}", "-i", q[src], "-an", "-vf", vf + ",tpad=stop_mode=clone:stop_duration=3",
                    "-frames:v", str(bilder), "-start_number", str(n), "-q:v", "2", str(ziel / "f%05d.jpg")], check=True)
    n += bilder; t += dauer
print(f"✓ {n} Bilder, {t:.2f} s")
