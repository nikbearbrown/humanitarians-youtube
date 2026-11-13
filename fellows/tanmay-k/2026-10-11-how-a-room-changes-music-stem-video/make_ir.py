#!/usr/bin/env python3
"""Makes ir/simulated-cathedral.wav: our own synthetic impulse response (FACTCHECK B5).

A measured cathedral IR was cut on licence grounds (FACTCHECK §C, A23), so the echo is simulated:
a direct-sound spike, a handful of early reflections, then a diffuse tail of exponentially decaying
noise. The tail is split into three bands that decay at different rates, so it darkens as it rings
(high frequencies die first, as they do in stone rooms). Seeded, so the file is reproducible.

Run with the homebrew interpreter that has numpy/scipy:  /opt/homebrew/bin/python3.12 make_ir.py
"""
import json
import wave
from pathlib import Path

import numpy as np
from scipy.signal import butter, sosfilt

HERE = Path(__file__).parent
SR = 24000            # Kokoro's rate (PLAYBOOK §6: match the reel's own parameters)
LENGTH_S = 7.0
RT60 = {"low": 5.5, "mid": 5.0, "high": 2.6}   # seconds to fall 60 dB, per band
EARLY = [(0.019, 0.55), (0.031, 0.42), (0.047, 0.38), (0.063, 0.30), (0.081, 0.26), (0.104, 0.20)]
SEED = 26
# Diffuse-tail level relative to the direct sound (how far the listener sits from the speaker).
# Chosen by measurement, not taste: experiment/demo_grid.py (Whisper word match). At 1.0 nothing
# survives at any pace. Final room: tail 0.25 + early field 1.0 (demo_final.json). Decay RATE unchanged.
TAIL_GAIN = 0.25


def decay(rt, t):
    return 10 ** (-3 * t / rt)          # -60 dB at t = rt


# Early diffuse field: dense reflections in the first 80 ms (walls, floor, nearby columns), at a
# level comparable to the direct sound, as a listener near the speaker hears in a stone room.
# Six sparse taps alone (draft 1) left speech with almost no early energy, which is unrealistic
# and made the room unintelligible at any pace (experiment/demo_grid.json, run 3).
EARLY_FIELD_GAIN = 1.0   # chosen in experiment/demo_final.json (run 5, pre-registered)
EARLY_FIELD_S = (0.005, 0.080)


def build_ir(tail_gain=TAIL_GAIN, early_gain=EARLY_FIELD_GAIN):
    """The impulse response as an array (peak 1.0). experiment/demo_grid.py calls this directly,
    so the grid always measures the same generator the film uses."""
    rng = np.random.default_rng(SEED)
    n = int(SR * LENGTH_S)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    bands = {
        "low": butter(4, 400, "lowpass", fs=SR, output="sos"),
        "mid": butter(4, [400, 3000], "bandpass", fs=SR, output="sos"),
        "high": butter(4, 3000, "highpass", fs=SR, output="sos"),
    }
    tail = sum(sosfilt(sos, noise) * decay(RT60[k], t) for k, sos in bands.items())
    onset = np.clip((t - 0.02) / 0.06, 0, 1)            # diffuse field builds over ~60 ms
    tail *= onset * 0.32 * tail_gain
    ir = tail
    a, b = (int(x * SR) for x in EARLY_FIELD_S)
    ef = rng.standard_normal(b - a) * np.exp(-np.arange(b - a) / (0.03 * SR))
    ir[a:b] += ef * early_gain * 0.25                      # dense early reflections
    ir[0] += 1.0                                          # direct sound
    for delay, gain in EARLY:
        ir[int(delay * SR)] += gain * (1 if rng.random() > 0.5 else -1)
    ir /= np.max(np.abs(ir))
    return ir


def main():
    ir = build_ir()
    t = np.arange(len(ir)) / SR
    out = HERE / "ir" / "simulated-cathedral.wav"
    out.parent.mkdir(exist_ok=True)
    pcm = (ir * 32767 * 0.95).astype("<i2")
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    # measured, not assumed: Schroeder backward integration → T30 extrapolated to 60 dB (ISO 3382 style)
    e = np.cumsum((ir ** 2)[::-1])[::-1]
    edc = 10 * np.log10(e / e[0])
    i5, i35 = np.argmax(edc <= -5), np.argmax(edc <= -35)
    t30 = (t[i35] - t[i5]) * 2
    # tail-only decay (EDC from 0.12 s, after the direct sound and early reflections)
    k = int(0.12 * SR); e2 = np.cumsum((ir[k:] ** 2)[::-1])[::-1]; edc2 = 10 * np.log10(e2 / e2[0])
    j5, j35 = np.argmax(edc2 <= -5), np.argmax(edc2 <= -35)
    t30_tail = (j35 - j5) / SR * 2
    meta = {"file": out.name, "sr": SR, "seconds": LENGTH_S, "seed": SEED, "tail_gain": TAIL_GAIN, "rt60_bands_s": RT60,
            "measured_T30_broadband_s": round(float(t30), 2),
            "measured_T30_tail_s": round(float(t30_tail), 2)}
    (HERE / "ir" / "simulated-cathedral.json").write_text(json.dumps(meta, indent=1))
    print(json.dumps(meta))


if __name__ == "__main__":
    main()
