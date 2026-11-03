"""Exact quantisation noise per bit depth, in float64.

ffmpeg's filter graph is 32-bit float internally (24-bit mantissa), so a 24-bit
round-trip is lossless *to ffmpeg* and reports -inf error. That is a limit of
the tool, not a property of 24-bit audio. numpy in float64 has the headroom to
measure all three depths honestly.

Rounding, mid-tread, no dither. Error is measured against the float64 original.
"""
import numpy as np

SR, DUR, F = 48000, 20.0, 440.0
t = np.arange(int(SR * DUR), dtype=np.float64) / SR
x = 0.5 * np.sin(2 * np.pi * F * t)          # -6 dBFS peak, a healthy level

def db(v):
    return -np.inf if v <= 0 else 20.0 * np.log10(v)

print(f"{'DEPTH':<9}{'NOISE RMS dBFS':>17}{'THEORY':>10}{'DELTA':>8}{'STEP SIZE':>14}")
print("-" * 58)
rows = []
for bits in (8, 16, 24):
    levels = 2 ** bits
    step = 2.0 / levels                       # full scale is -1..+1
    q = np.round(x / step) * step             # quantise
    q = np.clip(q, -1.0, 1.0 - step)
    err = q - x
    rms = db(np.sqrt(np.mean(err ** 2)))
    theory = -(6.02 * bits + 1.76)
    rows.append((bits, rms, step))
    print(f"{str(bits)+'-bit':<9}{rms:>17.2f}{theory:>10.1f}{rms-theory:>+8.1f}{step:>14.3e}")

print()
print(f"signal RMS: {db(np.sqrt(np.mean(x**2))):.2f} dBFS  (peak -6.0 dBFS)")
print()
print("Dynamic range = how far below full scale a sound can sit and still be")
print("louder than the noise the format itself adds:")
for bits, rms, _ in rows:
    print(f"  {bits:>2}-bit : {abs(rms):6.1f} dB")
