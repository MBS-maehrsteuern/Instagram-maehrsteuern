"""Virtuelle Kamera über 2 Higgsfield-Shots (Loris 16.11.): Schwenks, Kippen, Upside-down, Drehungen, Zoom-Fahrten – Bild für Bild.
A = Crash-Zoom + Splash (Einschlag 0,95 s), C = Held mit Orbit. Song in TikTok ab 0:44: Drop 3,74 s, Schlag 0,47603 s, CTA 17,545 s.
python3 kamera.py <A.mp4> <C.mp4> <frames_ordner>
Jede Szene: Quelle, Start/Tempo in der Quelle und Kamerakurven von→bis: zoom z, Drehung r (Grad), Schwenk x/y (-1…1), Spiegeln."""
import math, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

B, DROP = 0.47603, 3.74
BEAT = lambda k: DROP + k * B
W, H = 1080, 1920
GRADE = ("colorbalance=rs=.06:gs=.03:bs=-.10:rm=.07:gm=.04:bm=-.10:rh=.06:gh=.05:bh=-.06,"
         "eq=brightness=0.09:contrast=1.06:saturation=1.15:gamma=1.06")
GELB = (240, 226, 150)

ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3                      # schnell rein, weich aus
expo = lambda x: 1 if x >= 1 else 1 - 2 ** (-10 * min(max(x, 0), 1))    # Speed-Ramp
schaukel = lambda x: math.sin(2 * math.pi * x)                          # Pendel


def S(src, start, tempo, dauer, z=(1, 1), r=(0, 0), x=(0, 0), y=(0, 0), fl=False, kurve=ease, rk=None):
    return dict(src=src, start=start, tempo=tempo, dauer=dauer, z=z, r=r, x=x, y=y, fl=fl, kurve=kurve, rk=rk)


SZ = [
    S("C", 0.0, 0.6, DROP - 0.95, z=(2.3, 2.7), r=(-5, 4), y=(-0.5, -0.3)),            # Hook: Makro, langsames Kippen
    S("A", 0.0, 1.0, 0.95, z=(1.0, 1.0)),                                               # Crash-Zoom → Einschlag auf dem Drop
    S("A", 0.95, 0.5, 4 * B, z=(1.0, 1.18), r=(0, -4)),                                 # Drop: Splash, Push-in
    S("A", 1.9, 0.5, 4 * B, z=(1.5, 1.5), r=(360, 0), y=(-0.5, -0.4), kurve=expo),      # Fassrolle (360°-Dreh)
    S("C", 1.0, 1.0, 4 * B, z=(1.3, 1.25), r=(180, 0), kurve=expo),                     # Upside-down → dreht sich auf
    S("A", 2.85, 0.6, 4 * B, z=(1.8, 1.8), r=(8, 8), x=(-0.7, 0.7)),                    # Schwenk über die Früchte
    S("C", 2.0, 1.0, 4 * B, z=(1.6, 1.6), r=(-14, 14), y=(0.4, 0.4), fl=True, rk=schaukel),  # Pendel-Kippen, gespiegelt
    # ein Schnitt pro Schlag – jede Einstellung anders
    S("A", 1.3, 1.0, B, z=(1.9, 1.9), r=(180, 180)),                                    # kopfüber
    S("C", 0.6, 1.0, B, z=(2.0, 2.0), r=(-90, 0), kurve=expo),                          # 90°-Dreh rein
    S("A", 2.3, 1.0, B, z=(1.0, 2.1), y=(0, -0.4), kurve=expo),                         # Zoom-Schuss
    S("C", 3.0, 1.0, B, z=(1.5, 1.5), x=(-1, 1), fl=True),                              # Reißschwenk
    S("A", 3.1, 1.0, B, z=(2.0, 2.0), r=(22, 22)),                                      # extrem schräg
    S("C", 1.6, 1.0, B, z=(2.2, 1.3), r=(0, -10), kurve=expo),                          # Zoom raus + kippen
    S("A", 1.6, 1.0, B, z=(1.7, 1.7), r=(-180, -180), fl=True),                         # kopfüber gespiegelt
    S("C", 2.6, 1.0, B, z=(2.4, 2.4), r=(90, 0), y=(0.35, 0.35), kurve=expo),           # 90°-Dreh aus der anderen Seite
    S("A", 3.3, 0.7, B, z=(1.6, 1.4), r=(-45, 0), kurve=expo),                          # „Du weißt Bescheid“: Dreh rein
    S("C", 0.0, 4.0 / (22.4 - BEAT(29)), 22.4 - BEAT(29), z=(1.08, 1.2), r=(2, 0)),    # CTA: ruhiger Held, Push-in
]


def lade(pfad, ordner):
    ordner.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pfad, "-vf", GRADE, "-q:v", "2", str(ordner / "s%04d.jpg")], check=True)
    return [Image.open(p).convert("RGB") for p in sorted(ordner.glob("s*.jpg"))]


def kamera_bild(bild, z, r, x, y, fl):
    if fl: bild = bild.transpose(Image.FLIP_LEFT_RIGHT)
    sw, sh = bild.size; basis = max(W / sw, H / sh)                  # Quelle füllt das Bild bei z = 1
    th = math.radians(r); c, s = abs(math.cos(th)), abs(math.sin(th))
    z = max(z, c + (H / W) * s, c + (W / H) * s)                     # nie Ränder zeigen: Zoom gleicht die Drehung aus
    k = basis * z
    # Schwenk: wie weit die Mitte wandern darf, ohne den Rand zu erreichen
    mx = max((sw * k - W) / 2, 0) / k; my = max((sh * k - H) / 2, 0) / k
    cx, cy = sw / 2 + x * mx * 0.9, sh / 2 + y * my * 0.9
    co, si = math.cos(th), math.sin(th)
    # Ausgabepixel (u, v) → Quellpixel: um die Bildmitte drehen und skalieren
    a, b_ = co / k, si / k; d, e = -si / k, co / k
    c0 = cx - a * W / 2 - b_ * H / 2; f0 = cy - d * W / 2 - e * H / 2
    return bild.transform((W, H), Image.AFFINE, (a, b_, c0, d, e, f0), Image.BICUBIC, fillcolor=GELB)


quelle = {"A": sys.argv[1], "C": sys.argv[2]}; ziel = Path(sys.argv[3]); ziel.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    clips = {k: lade(v, Path(tmp) / k) for k, v in quelle.items()}
    n, t0 = 0, 0.0
    for sz in SZ:
        ende = round((t0 + sz["dauer"]) * 30)
        while n < ende:
            lt = n / 30 - t0; p = lt / sz["dauer"]
            fr = clips[sz["src"]]; i = min(int((sz["start"] + lt * sz["tempo"]) * 24), len(fr) - 1)
            kv = sz["kurve"](p)
            lerp = lambda ab, q=kv: ab[0] + (ab[1] - ab[0]) * q
            r = sz["r"][0] + (sz["r"][1] - sz["r"][0]) * (0.5 + 0.5 * sz["rk"](p)) if sz["rk"] else lerp(sz["r"])
            kamera_bild(fr[i], lerp(sz["z"]), r, lerp(sz["x"]), lerp(sz["y"]), sz["fl"]).save(ziel / f"f{n:05d}.jpg", quality=93)
            n += 1
        t0 += sz["dauer"]
print(f"✓ {n} Bilder, {t0:.2f} s")
