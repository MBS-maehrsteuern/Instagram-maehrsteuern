"""Klangabgleich für Loris' Stimme (Loris 26.10.: „hört sich immer noch dumpf an“).
Die Handy-Aufnahmen haben zu viel Bass (200–315 Hz) und ein Loch von 20–30 dB um 1 kHz → dumpf/hohl. Ein fester EQ reicht
nicht: Wir messen das Terzband-Spektrum der lauten Stellen, vergleichen mit einer Zielkurve (Langzeit-Sprachspektrum,
für Social Media etwas heller) und bauen daraus einen firequalizer (Anhebung max. +18 dB, Absenkung max. −10 dB).
    python3 klang.py stimme.wav            → druckt die Kurven
    from klang import filter_fuer          → ffmpeg-Filterkette für reel_bauen.py"""
import subprocess, sys
import numpy as np

TERZ = [100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500]
ZIEL = [-9, -6, -4, -2, -1, 0, 0, -1, -2, -4, -6, -7, -8, -9, -10, -11, -12, -14, -16, -19, -23, -28]
MAX_AUF, MAX_AB = 18, -10


def kurve(datei, af=None):
    roh = subprocess.run(["ffmpeg", "-v", "error", "-i", str(datei), *(["-af", af] if af else []),
                          "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True, check=True).stdout
    a = np.frombuffer(roh, np.float32)
    n = 4800
    stuecke = [a[i:i + n] for i in range(0, len(a) - n, n)]
    rms = np.array([np.sqrt(np.mean(s ** 2)) for s in stuecke])
    laut = [s for s, r in zip(stuecke, rms) if r > np.percentile(rms, 50)]  # nur Sprache, keine Pausen
    P = np.mean([np.abs(np.fft.rfft(s * np.hanning(n), n=48000)) ** 2 for s in laut], 0)
    f = np.arange(len(P))
    b = np.array([P[(f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6))].sum() for c in TERZ])
    d = 10 * np.log10(b / b.max())
    return d - d[TERZ.index(315):TERZ.index(500) + 1].mean()  # auf den Grundton-Bereich bezogen


def gewinne(datei):
    ist = kurve(datei)
    ziel = np.array(ZIEL, float) - np.mean(ZIEL[TERZ.index(315):TERZ.index(500) + 1])
    g = np.clip(ziel - ist, MAX_AB, MAX_AUF)
    g = np.convolve(np.pad(g, 1, mode="edge"), [.25, .5, .25], "valid")  # glätten, keine Zacken
    return g - g.max() if g.max() > 0 else g  # nur absenken → kein Übersteuern, Lautheit macht loudnorm


def filter_fuer(datei):
    g = gewinne(datei)
    eintraege = ";".join(f"entry({f},{x:.1f})" for f, x in zip([20, *TERZ, 20000], [g[0] - 12, *g, g[-1] - 6]))
    return (f"highpass=f=80:p=2,firequalizer=gain_entry='{eintraege}':gain='cubic_interpolate(f)',"
            f"afftdn=nf=-40,aexciter=amount=1:drive=4:freq=8000:ceil=16000,deesser=i=0.4,acompressor=threshold=-20dB:ratio=2:attack=5:release=100:makeup=3,"
            f"alimiter=limit=0.95")


if __name__ == "__main__":
    for d in sys.argv[1:]:
        print(d)
        print(" Hz   ", " ".join(f"{f:>5}" for f in TERZ))
        print(" ist  ", " ".join(f"{x:5.0f}" for x in kurve(d)))
        print(" EQ   ", " ".join(f"{x:5.0f}" for x in gewinne(d)))
        print(" neu  ", " ".join(f"{x:5.0f}" for x in kurve(d, filter_fuer(d))))
