"""Schnitt Aufnahme 27.10. (überarbeitete Sprechtexte). Beide Handy-Mikros per Frequenzweiche (wie 26.10.), Abschnitte nach
Wortzeiten (woerter.json, Whisper medium), Pausen auf max. 0,35 s gekürzt und gedämpft, 12-ms-Blenden, −16 LUFS.
    cd aufnahmen/2026-10-27 && python3 geschnitten/schnitt.py"""
import subprocess, numpy as np
SR = 48000
Q = "alle_reels_roh.mp3"
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", Q, "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout, np.float32).reshape(-1, 2)
L, R = x[:, 0], x[:, 1]; m = slice(SR * 30, SR * 60)
LAG = max(range(-30, 31), key=lambda k: float(np.dot(L[m.start + k:m.stop + k], R[m])))
WEICHE = (f"[0:a]channelsplit=channel_layout=stereo[l][r];[r]adelay={max(LAG,0)}S,lowpass=f=7000,lowpass=f=7000[ru];"
          "[l]highpass=f=7000,highpass=f=7000[lo];[ru][lo]amix=inputs=2:normalize=0[a]")
X = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", Q, "-filter_complex", WEICHE, "-map", "[a]", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32).copy()
# Abschnitte (Sekunden in der Rohaufnahme) – Satzgrenzen aus woerter.json, Versprecher/Anläufe ausgelassen
T = {
 "I13": [(66.5, 77.25), (79.45, 89.7), (90.4, 107.0)],          # „meistens zwei bis vier Wochen“ raus (nicht belegt)
 "I14": [(114.6, 154.2)],
 "M1":  [(160.7, 184.0), (189.15, 200.2)],                       # Wiederholung 184,3–189,2 raus
 "M2":  [(209.8, 237.0)],
 "S1":  [(241.9, 277.1)],
 "S2":  [(283.1, 318.1)],
 "S3":  [(322.3, 351.0)],
 "S4":  [(356.4, 393.0), (395.9, 398.9)],
 "S5":  [(404.2, 437.0)],
}
PAUSE, DAEMPF, XF = 0.35, 10 ** (-28 / 20), int(0.012 * SR)
def fade(y):
    w = np.sin(np.linspace(0, np.pi / 2, XF)) ** 2; y[:XF] *= w; y[-XF:] *= w[::-1]; return y
def stille(y, a):
    """lange Pausen innerhalb eines Abschnitts kürzen (Energie < Rauschen + 12 dB länger als PAUSE)"""
    W = 480; e = np.array([np.sqrt(np.mean(y[i:i + W] ** 2)) + 1e-9 for i in range(0, len(y) - W, W)])
    db = 20 * np.log10(e); laut = db > np.percentile(db, 10) + 12
    teile, i = [], 0
    while i < len(laut):
        j = i
        while j < len(laut) and laut[j] == laut[i]: j += 1
        s = y[i * W:j * W].copy()
        if not laut[i] and (j - i) * W > PAUSE * SR and i > 0 and j < len(laut):
            s = np.concatenate([s[:int(PAUSE / 2 * SR)], s[-int(PAUSE / 2 * SR):]]) * DAEMPF
            s = fade(s)
        teile.append(s); i = j
    return np.concatenate(teile)
for nr, abschnitte in T.items():
    teile = []
    for k, (a, b) in enumerate(abschnitte):
        teile.append(fade(stille(X[int(a * SR):int(b * SR)].copy(), a)))
        if k + 1 < len(abschnitte): teile.append(np.zeros(int(0.3 * SR), np.float32))
    y = np.concatenate(teile)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af",
                    "highpass=f=70,acompressor=threshold=-20dB:ratio=2:attack=10:release=150:makeup=1.5,loudnorm=I=-16:TP=-1.5:LRA=9",
                    "-ar", str(SR), f"geschnitten/stimme_{nr}.wav"], input=y.tobytes(), check=True)
    print(nr, round(len(y) / SR, 1), "s")
print("Versatz", LAG)
