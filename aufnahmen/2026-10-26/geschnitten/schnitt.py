"""Schnitt Aufnahme 26.10. (Finanzamt-Insider I1–I12): nur vollständige Anläufe, Atmer/Pausen gedämpft und gekürzt,
weiche Übergänge, Stimme gefiltert + leicht komprimiert + auf −16 LUFS. Chunks: chunks.json (Energie-Erkennung).
    cd aufnahmen/2026-10-26 && python3 geschnitten/schnitt.py"""
import json, subprocess
import numpy as np
SR = 48000
C = json.load(open("chunks.json"))
X = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", "insider_roh.mp3", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True).stdout, np.float32).copy()
rg = lambda a, b: list(range(a, b + 1))
# Auswahl je Reel (Chunk-Nummern), Anläufe/Nummern/Versprecher entfernt – Begründung in README.md
R = {"I1": rg(21, 31), "I2": rg(36, 38) + rg(43, 51), "I3": rg(62, 74), "I4": rg(76, 86), "I5": rg(87, 99),
     "I6": rg(103, 111), "I7": rg(113, 122), "I8": rg(124, 130), "I9": rg(132, 137) + rg(143, 144),
     "I10": rg(146, 155), "I11": rg(164, 170), "I12": rg(173, 179)}
PRE, POST, KURZ, PAUSE, DAEMPF, XF = 0.12, 0.14, 0.22, 0.30, 10 ** (-28 / 20), 0.012
def s(a, b): return X[max(0, int(a * SR)):int(b * SR)].copy()
def fade(y):
    n = int(XF * SR); w = np.sin(np.linspace(0, np.pi / 2, n)) ** 2
    y[:n] *= w; y[-n:] *= w[::-1]; return y
for nr, sel in R.items():
    teile = []
    for k, i in enumerate(sel):
        a, b = C[i]
        vor = C[i - 1][1] if i > 0 else 0
        nach = C[i + 1][0] if i + 1 < len(C) else b + 1
        start = a - min(PRE, (a - vor) / 2) if not (k and sel[k - 1] == i - 1) else a
        ende = b + min(POST, (nach - b) / 2)
        teile.append(fade(s(start, ende)))
        if k + 1 < len(sel):
            naechster = sel[k + 1]
            luecke = C[naechster][0] - b if naechster == i + 1 else 1.0
            if naechster == i + 1 and luecke <= KURZ:      # Atemzug-freie Mikropause: natürlich lassen
                teile[-1] = fade(s(start, C[naechster][0] - min(PRE, luecke / 2)))
                ziel = 0
            else:
                ziel = PAUSE if luecke > 0.45 else max(0.12, luecke - PRE - POST)
            if ziel:
                ton = s(b + POST, b + POST + ziel) if naechster == i + 1 else np.zeros(int(ziel * SR), np.float32)
                if len(ton) < int(ziel * SR): ton = np.pad(ton, (0, int(ziel * SR) - len(ton)))
                teile.append(fade(ton * DAEMPF))
    y = np.concatenate(teile)
    roh = f"geschnitten/{nr}_roh.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", roh], input=y.tobytes(), check=True)
    # Stimme veredeln: Rumpeln weg, leichte Entrauschung, sanfte Kompression, De-Esser, Lautheit −16 LUFS / −1,5 dBTP
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", roh, "-af",
                    "highpass=f=80,afftdn=nf=-30,acompressor=threshold=-22dB:ratio=2.5:attack=8:release=120:makeup=2,"
                    "deesser=i=0.35,loudnorm=I=-16:TP=-1.5:LRA=7", "-ar", "48000", f"geschnitten/stimme_{nr}.wav"], check=True)
    print(nr, round(len(y) / SR, 1), "s")
