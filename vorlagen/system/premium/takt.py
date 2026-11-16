"""Song für den Beat-Schnitt analysieren (Loris 16.11.):  python3 takt.py <song.mp3> [ab_s=0] [laenge_s=90]
Gibt aus: Tempo (BPM), Lage des Schlag-Rasters, starke Akzente, Drop-Kandidaten (Energiesprung) und
Gesangs-Kandidaten (Mitte-Anteil im Stimmband – grob, bitte gegenhören). Alle Zeiten relativ zu ab_s UND absolut im Song."""
import subprocess, sys
import numpy as np

song, ab, laenge = sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 0, float(sys.argv[3]) if len(sys.argv) > 3 else 90
sr = 22050
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ab), "-t", str(laenge), "-i", song, "-ac", "2", "-ar", str(sr), "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.int16).astype(float).reshape(-1, 2) / 32768
mono, seite = x.mean(1), (x[:, 0] - x[:, 1]) / 2


def spek(s, n=1024, hop=256):
    fr = np.lib.stride_tricks.sliding_window_view(s, n)[::hop] * np.hanning(n)
    return np.abs(np.fft.rfft(fr, axis=1))


# Tempo + Raster
hop = 256; fps = sr / hop
M = np.log1p(10 * spek(mono)); flux = np.maximum(np.diff(M, axis=0), 0).sum(1); flux = (flux - flux.mean()) / flux.std()
ac = np.correlate(flux, flux, "full")[len(flux) - 1:]; lag = np.arange(len(ac)) / fps
m = (lag > 60 / 180) & (lag < 60 / 80); T = lag[m][np.argmax(ac[m])]
P = int(round(T * fps)); ph = max(range(P), key=lambda p: flux[p::P].sum()); b0 = ph / fps
print(f"Tempo {60 / T:.1f} BPM · Schlag alle {T:.3f} s · Raster beginnt bei {b0:.2f} s (Song {ab + b0:.2f})")
akz = [k / fps for k in range(1, len(flux) - 1) if flux[k] > 2.5 and flux[k] >= flux[k - 1] and flux[k] >= flux[k + 1]]
print("Starke Akzente:", " ".join(f"{a:.2f}" for a in akz[:80]))

# Drop: größter Sprung der Lautheit (0,12-s-Fenster gegen die 2 s davor)
w = int(.12 * sr); e = np.array([np.sqrt((mono[i:i + w] ** 2).mean()) for i in range(0, len(mono) - w, w)])
sprung = [(i * w / sr, e[i] / (e[max(0, i - 16):i].mean() + 1e-6)) for i in range(16, len(e))]
for t, f in sorted(sprung, key=lambda s: -s[1])[:4]:
    print(f"Drop-Kandidat {t:.2f} s (Song {ab + t:.2f}) · Faktor {f:.1f}")

# Gesang: Anteil der Mitte im Stimmband 300–3000 Hz (Stimme liegt meist mittig)
Mm, Ms = spek(mono, 2048, 1024), spek(seite, 2048, 1024); f = np.fft.rfftfreq(2048, 1 / sr); b = (f > 300) & (f < 3000)
v = (Mm[:, b] ** 2).sum(1) / ((Mm[:, b] ** 2).sum(1) + (Ms[:, b] ** 2).sum(1)); tv = np.arange(len(v)) * 1024 / sr
glatt = np.convolve(v, np.ones(5) / 5, "same"); basis = np.median(glatt)
ein = [tv[i] for i in range(1, len(glatt)) if glatt[i] > basis + .15 and glatt[i - 1] <= basis + .15]
print("Gesangs-Kandidaten (grob):", " ".join(f"{t:.2f}(Song {ab + t:.1f})" for t in ein[:12]))
