#!/usr/bin/env python3
"""Two original tunes for the film, synthesized from scratch (no samples, no third-party music).

  tune_quick_major.wav   : C major, 156 bpm, bright plucks, upbeat bass; 16 s
  tune_slow_minor.wav    : A minor, 54 bpm, low soft pad + sparse low melody; 16 s

Illustration, not data: they exist so the viewer can hear 'quick and bright' against 'slow and low'.
Run: /opt/homebrew/bin/python3.12 make_tunes.py   -> tunes/*.wav (48 kHz mono, peak -3 dBFS)
"""
import wave
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
OUT = HERE / "tunes"
OUT.mkdir(exist_ok=True)
SR = 48000


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def pluck(freq, dur, bright=1.0, sr=SR):
    t = np.arange(int(dur * sr)) / sr
    env = np.exp(-t * (7.0 / max(dur, 0.2)) * 2.2) * np.minimum(1, t / 0.004)
    x = np.zeros_like(t)
    for k, amp in enumerate([1.0, 0.55, 0.38, 0.22, 0.14, 0.09], start=1):
        x += amp * (bright ** (k - 1)) * np.sin(2 * np.pi * freq * k * t)
    return x * env


def pad(freq, dur, sr=SR):
    t = np.arange(int(dur * sr)) / sr
    att = np.minimum(1, t / 0.9) * np.minimum(1, (dur - t) / 1.1)
    x = np.zeros_like(t)
    for det in (-0.004, 0.0, 0.004):
        x += np.sin(2 * np.pi * freq * (1 + det) * t) + 0.35 * np.sin(2 * np.pi * freq * 2 * (1 + det) * t)
    return x * att / 3


def place(buf, x, start, sr=SR):
    i = int(start * sr)
    j = min(len(buf), i + len(x))
    if i < len(buf):
        buf[i:j] += x[: j - i]


def write(path, x):
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.707
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())


def quick_major(dur=16.0):
    bpm = 156
    beat = 60 / bpm
    buf = np.zeros(int(dur * SR))
    # melody in C major, eighth notes: a rising, bouncing figure (original)
    mel = [72, 76, 79, 76, 74, 77, 81, 77, 76, 79, 83, 79, 77, 74, 72, 67,
           72, 76, 79, 84, 83, 79, 76, 79, 77, 74, 71, 74, 72, 76, 79, 72]
    chords = [(48, 55, 64), (53, 60, 69), (55, 62, 71), (48, 55, 64)]
    t = 0.0
    k = 0
    while t < dur - 0.3:
        place(buf, pluck(midi(mel[k % len(mel)]), beat * 0.6, 1.0) * 0.55, t)
        if k % 2 == 0:
            ch = chords[(k // 8) % 4]
            place(buf, pluck(midi(ch[0] - 12), beat * 0.9, 0.5) * 0.7, t)      # bass on the beat
            for n in ch[1:]:
                place(buf, pluck(midi(n), beat * 0.45, 0.8) * 0.22, t + beat * 0.5)   # offbeat chord stabs
        t += beat / 2
        k += 1
    return buf


def slow_minor(dur=16.0):
    bpm = 54
    beat = 60 / bpm
    buf = np.zeros(int(dur * SR))
    chords = [(45, 52, 57), (41, 48, 53), (43, 50, 55), (40, 47, 52)]   # Am, F, G, Em-ish, low
    for bar in range(int(dur / (beat * 4)) + 1):
        ch = chords[bar % 4]
        for n in ch:
            place(buf, pad(midi(n), beat * 4.2) * 0.5, bar * beat * 4)
    mel = [57, None, 60, None, 59, None, 55, None, 57, None, 53, None, 52, None, 55, None]
    for i, n in enumerate(mel):
        if n is not None and i * beat * 2 < dur - 1:
            place(buf, pluck(midi(n - 12), beat * 3.5, 0.15) * 0.8, i * beat * 2)
    return buf


if __name__ == "__main__":
    write(OUT / "tune_quick_major.wav", quick_major())
    write(OUT / "tune_slow_minor.wav", slow_minor())
    for p in sorted(OUT.glob("*.wav")):
        print(p.name, round(p.stat().st_size / 1e3), "kB")
