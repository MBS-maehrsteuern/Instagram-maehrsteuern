"""Stimmen vom 21.10. mit beiden Handy-Mikros neu aufbauen (Loris 26.10.: „perfekt, für alle Reels“).
Die Schnittliste (chunks.json) von damals fehlt. Darum: Jede fertige stimme_NN.wav wird Fenster für Fenster in der
Rohaufnahme wiedergefunden (Kreuzkorrelation) → exakt dieselben Schnitte, aber aus der Frequenzweiche
(rechts bis 7 kHz, links ab 7 kHz, rechts um 5 Samples verzögert) statt aus dem stumpfen Stereo→Mono-Mix.
    cd aufnahmen/2026-10-21 && python3 geschnitten/mikros_neu.py 32 34 …   (Ausgabe: geschnitten/stimme_NN.wav, Original → alt/)"""
import subprocess, sys, shutil
from pathlib import Path
import numpy as np
SR, Q, VERSATZ = 48000, "sprechtexte_fach.mp3", 5
WEICHE = (f"[0:a]channelsplit=channel_layout=stereo[l][r];[r]adelay={VERSATZ}S,lowpass=f=7000,lowpass=f=7000[ru];"
          "[l]highpass=f=7000,highpass=f=7000[lo];[ru][lo]amix=inputs=2:normalize=0[a]")
def lade(args):
    return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", *args, "-ar", str(SR), "-f", "f32le", "-"],
                                        capture_output=True, check=True).stdout, np.float32).copy()
MONO = lade(["-i", Q, "-ac", "1"])                                   # so wurde damals geschnitten
NEU = lade(["-i", Q, "-filter_complex", WEICHE, "-map", "[a]"])
D = 6; m8 = MONO[::D] - MONO[::D].mean()                              # 8 kHz für die Grobsuche
def ncc(x, y): return float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y) + 1e-9))
def suche(w, um=None, weite=60 * SR):                                 # Suche per FFT (erst in der Nähe), dann fein auf 48 kHz
    a = 0 if um is None else max(0, (um - weite) // D); b = len(m8) if um is None else min(len(m8), (um + weite) // D)
    w8 = w[::D]; ref = m8[a:b]; n = len(ref) + len(w8)
    c = np.fft.irfft(np.fft.rfft(ref, n) * np.conj(np.fft.rfft(w8, n)), n)[:len(ref) - len(w8)]
    cs = np.concatenate([[0], np.cumsum(ref.astype(np.float64) ** 2)])
    c = c / np.sqrt((cs[len(w8):] - cs[:-len(w8)])[:len(c)] + 1e-9)   # normiert, sonst gewinnen laute Stellen
    grob = (a + int(np.argmax(c))) * D
    return max(range(grob - 2 * D, grob + 2 * D + 1), key=lambda o: ncc(MONO[o:o + len(w)], w) if 0 <= o <= len(MONO) - len(w) else -1)
FEN, XF = 4800, int(0.025 * SR)                                       # 100-ms-Fenster
(Path("geschnitten/alt")).mkdir(exist_ok=True)
for nr in sys.argv[1:]:
    f = Path(f"geschnitten/stimme_{nr}.wav"); alt = Path(f"geschnitten/alt/stimme_{nr}.wav")
    if not alt.exists(): shutil.copy(f, alt)
    S = lade(["-i", str(alt), "-ac", "1"])
    off = np.full(len(S) // FEN, -1); o = None; ruhig = []
    for k in range(len(off)):
        w = S[k * FEN:(k + 1) * FEN]
        if np.sqrt(np.mean(w ** 2)) < 1e-3: ruhig.append(k); continue  # Stille: Versatz vom Nachbarn
        if o is None or ncc(MONO[o + k * FEN:o + (k + 1) * FEN], w) < 0.8:
            o2 = suche(w, None if o is None else o + k * FEN) - k * FEN
            if ncc(MONO[o2 + k * FEN:o2 + (k + 1) * FEN], w) < 0.8: o2 = suche(w) - k * FEN
            if o is None or ncc(MONO[o2 + k * FEN:o2 + (k + 1) * FEN], w) > ncc(MONO[o + k * FEN:o + (k + 1) * FEN], w): o = o2
        off[k] = o
    for k in range(len(off)):                                          # Lücken (Stille) auffüllen
        if off[k] < 0: off[k] = next((off[j] for j in range(k, len(off)) if off[j] >= 0), off[max(0, k - 1)])
    y = np.zeros(len(S), np.float32); g = np.zeros(len(S), np.float32)
    # stückweise gleicher Versatz → Abschnitte mit 25-ms-Überblendung zusammensetzen
    grenzen = [0] + [k * FEN for k in range(1, len(off)) if off[k] != off[k - 1]] + [len(S)]
    for a, b in zip(grenzen[:-1], grenzen[1:]):
        oo = off[min(a // FEN, len(off) - 1)]; a2, b2 = max(0, a - XF // 2), min(len(S), b + XF // 2)
        seg = NEU[oo + a2:oo + b2].copy(); seg = np.pad(seg, (0, b2 - a2 - len(seg)))
        w = np.ones(b2 - a2, np.float32); r = np.sin(np.linspace(0, np.pi / 2, XF)) ** 2
        if a2 > 0: w[:XF] = r
        if b2 < len(S): w[-XF:] = r[::-1]
        y[a2:b2] += seg * w; g[a2:b2] += w
    y = y / np.maximum(g, 1e-6) * np.minimum(g, 1)
    # Pausen so leise wie im Original: Hüllkurve des alten Stems übernehmen, wo er fast still ist
    y = y / np.max(np.abs(y)) * 0.5
    roh = f"geschnitten/alt/neu_{nr}.f32"; y.tofile(roh)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", roh, "-af",
                    "highpass=f=70,loudnorm=I=-18:TP=-1.5:LRA=9", "-ar", "48000", str(f)], check=True)
    Path(roh).unlink()
    N = lade(["-i", str(f), "-ac", "1"])
    test = [ncc(MONO[off[k] + k * FEN:off[k] + (k + 1) * FEN], S[k * FEN:(k + 1) * FEN]) for k in range(len(off)) if k not in ruhig]
    print(nr, f"{len(S) / SR:.2f}s→{len(N) / SR:.2f}s", "Abschnitte", len(grenzen) - 1, "Treffer≥0.9:", f"{np.mean(np.array(test) > .9):.0%}")
