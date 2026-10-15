"""Reel 60 „Geld verschenkt“: Stimme aus 3 Takes zusammenschneiden (Schnittkanten an Stille, Pegel angleichen, −16 LUFS).

    python3 p60_stimme_bauen.py   -> posts/60_…/ton/stimme_schnitt.wav (+ stimme_schnitt_woerter.json nach Transkription)
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
REPO = Path(__file__).resolve().parents[3]
TON = REPO / "posts/60_2026-10-15_reel_geld_verschenkt/ton"
SR = 44100
LUECKE = 0.13          # Stille zwischen Sätzen (zusätzlich zum Rest an den Schnittkanten)
FADE = 0.015
SEGMENTE = [(74.24, 76.94), (41.00, 43.26), (80.14, 83.30), (84.20, 85.12), (85.58, 90.58), (91.28, 93.22), (25.84, 28.08)]
WOERTER = json.loads((TON / "woerter.json").read_text())["aufnahme_roh.mp3"]


def lade():
    r = subprocess.run([FF, "-loglevel", "error", "-i", str(TON / "aufnahme_roh.mp3"), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def leiseste(x, lo, hi, wunsch=None):
    """Mitte des leisesten 20-ms-Fensters in [lo, hi] (Sekunden)."""
    n = int(0.02 * SR); c = []
    for s in np.arange(int(lo * SR), int(hi * SR), int(0.002 * SR)):
        c.append((float(np.sqrt(np.mean(x[s:s + n] ** 2)) + 1e-9), (s + n / 2) / SR))
    m = min(e for e, _ in c)
    ok = [t for e, t in c if e <= m * 2.0]  # fast so leise wie das Minimum
    return ok[0] if wunsch is None else min(ok, key=lambda t: abs(t - wunsch))


# Handkorrektur: Take 2 hat vor „Heißt“ ein kurzes „Das“ (85,56–85,63 s) – Schnitt in die Senke davor/danach
START_FIX = {85.58: 0.0}


def kanten(x, a, b):
    ws = [w for w in WOERTER if a - 0.3 < w[1] < b + 0.3]
    erst = min((w for w in ws if w[2] > a + 0.02), key=lambda w: w[1])   # erstes Wort im Bereich
    letzt = max((w for w in ws if w[1] < b - 0.02), key=lambda w: w[2])  # letztes Wort
    a2 = leiseste(x, a - 0.25, min(a + 0.25, erst[1] + 0.01), a)   # Start nie hinter den Wortanfang
    b2 = leiseste(x, max(b - 0.25, letzt[2] - 0.01), b + 0.25, b)  # Ende nie vor das Wortende
    if a in START_FIX: a2 = 85.52   # „Das“ ganz drinlassen (Loris sagt „Das heißt“), Untertitel entsprechend
    return a2, b2, erst[0], letzt[0]


def rms_sprache(y):
    f = 1024; r = np.array([np.sqrt(np.mean(y[i:i + f] ** 2)) for i in range(0, len(y) - f, f)])
    r = r[r > r.max() * 0.1]
    return float(np.sqrt(np.mean(r ** 2))) if len(r) else 1e-6


def lufs(datei):
    out = subprocess.run([FF, "-hide_banner", "-nostats", "-i", str(datei), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", out)[-1])


def bauen():
    x = lade(); teile = []
    for a, b in SEGMENTE:
        a2, b2, w1, w2 = kanten(x, a, b)
        y = x[int(a2 * SR):int(b2 * SR)].copy()
        print(f"{a}-{b} -> {a2:.3f}-{b2:.3f} ({w1} … {w2})")
        f = int(FADE * SR); y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
        teile.append(y)
    ziel = np.mean([rms_sprache(t) for t in teile])
    teile = [t * (ziel / rms_sprache(t)) for t in teile]  # Takes angleichen
    luft = np.zeros(int(LUECKE * SR), dtype=np.float32)
    out = np.concatenate([np.concatenate([t, luft]) for t in teile[:-1]] + [teile[-1]])
    roh = TON / "_roh.wav"; ziel_wav = TON / "stimme_schnitt.wav"
    raw = out.astype("<f4").tobytes()
    subprocess.run([FF, "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                    "-af", "highpass=f=80,acompressor=threshold=-22dB:ratio=2.5:attack=8:release=120:makeup=1", str(roh)], input=raw, check=True)
    l, _ = lufs(roh); gain = -16.0 - l
    subprocess.run([FF, "-loglevel", "error", "-y", "-i", str(roh), "-af", f"volume={gain:.2f}dB,alimiter=limit=0.82:level=false:attack=3:release=40", "-ar", str(SR), str(ziel_wav)], check=True)
    roh.unlink()
    print("Dauer %.2f s, LUFS/Peak:" % (len(out) / SR), lufs(ziel_wav))


def lade_wav():
    r = subprocess.run([FF, "-loglevel", "error", "-i", str(TON / "stimme_schnitt.wav"), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def transkribieren():
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(lade_wav(), language="de", word_timestamps=True, vad_filter=False)
    w = [[x.word.strip(), round(x.start, 3), round(x.end, 3), round(x.probability, 2)] for s in segs for x in s.words]
    (TON / "stimme_schnitt_woerter.json").write_text(json.dumps(w, ensure_ascii=False))
    print(" ".join(f"{a}[{b}-{c}]" for a, b, c, _ in w))


if __name__ == "__main__":
    if "nur_text" not in sys.argv: bauen()
    transkribieren()
