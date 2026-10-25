"""Dezentes Sounddesign für Premium-Reels (kein Zirkus): Aufprall zum Hook, Ticks, Ding, Whoosh.
    python3 sfx.py <ausgabe.wav> <dauer_s> "impact@0" "tick@3.88" "ding@4.42" "whoosh@24.5" …"""
import sys, wave
import numpy as np
SR = 48000
aus, dauer, *marken = sys.argv[1:]
spur = np.zeros(int(float(dauer) * SR))
def t(n): return np.arange(int(n * SR)) / SR
def impact():  # tiefer, weicher Schlag + kurzer Luftstoß
    x = t(0.9); s = np.sin(2 * np.pi * (70 - 25 * x) * x) * np.exp(-x * 5.5) * 0.9
    s[:2400] += np.random.default_rng(1).normal(0, 1, 2400) * np.exp(-t(0.05) * 60) * 0.25; return s
def tick():  # trockener Kalender-Klick
    x = t(0.035); return np.sin(2 * np.pi * 2100 * x) * np.exp(-x * 140) * 0.45
def ding():  # helles, kurzes „richtig“
    x = t(1.2); return (np.sin(2 * np.pi * 1318 * x) + 0.5 * np.sin(2 * np.pi * 1976 * x)) * np.exp(-x * 4) * 0.32
def whoosh():  # weicher Luftzug vor dem CTA
    x = t(0.7); n = np.random.default_rng(2).normal(0, 1, len(x))
    n = np.convolve(n, np.ones(24) / 24, mode="same"); return n * np.sin(np.pi * x / 0.7) ** 2 * 0.5
ARTEN = {"impact": impact, "tick": tick, "ding": ding, "whoosh": whoosh}
for m in marken:
    art, ab = m.split("@"); s = ARTEN[art](); i = int(float(ab) * SR)
    spur[i:i + len(s)] += s[:len(spur) - i]
spur = np.clip(spur, -1, 1)
with wave.open(aus, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((spur * 32767).astype("<i2").tobytes())
print("✓", aus)
