"""EXECUTABLE EVIDENCE for "How Spatial Audio Works."

A textbook head, not Apple's code: a rigid sphere 8.75 cm in radius (the classic model), with
  * timing: the extra path around the head to the far ear (Woodworth's formula), applied as a fractional delay;
  * level: the head's shadow, a one-pole/one-zero filter per ear that dims the far ear's highs (Brown & Duda 1998);
  * an outer-ear option: a gentle high-frequency cut for sounds from behind (a simple stand-in for pinna shadow).
Test sound: a short Western melody of plucked-string notes (Karplus-Strong), made here.

Measured:
  1. ITD: the measured left/right delay vs direction (cross-correlation of the rendered ears), and its maximum;
  2. ILD: level difference between the ears at 90 degrees, in a low band (around 500 Hz) and a high band (around 4 kHz);
  3. front/back: a source 30 degrees right-front and its mirror 30 degrees right-behind (150): with the head alone the
     two ears receive the same thing; with the outer-ear filter they differ;
  4. head tracking: you turn your head 40 degrees; without tracking the sound turns with you, with it the sound stays put.
Listening clips (headphones): the melody circling the head once; a sound placed front vs behind with and without the
outer-ear filter.

    python spatial.py     # writes evidence/run.log, results.json, scene.json, the WAVs
"""
import json
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import lfilter, bilinear

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
LOG, SCENE = [], {}
SR, A, C = 48000, 0.0875, 343.0           # sample rate, head radius (m), speed of sound (m/s)


def P(s=""):
    print(s, flush=True)
    LOG.append(s)


# ---------------------------------------------------------------- the test sound: a plucked melody
def pluck(freq, dur, rng):
    n = int(SR * dur)
    period = int(SR / freq)
    buf = rng.uniform(-1, 1, period)
    out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % period]
        buf[i % period] = 0.996 * 0.5 * (buf[i % period] + buf[(i + 1) % period])
    return out * np.exp(-np.arange(n) / (SR * 0.9))


def melody(rng, bars=2):
    notes = [220.0, 261.63, 293.66, 329.63, 392.0, 329.63, 293.66, 261.63] * bars     # A minor pentatonic-ish line
    return np.concatenate([pluck(f, 0.5, rng) for f in notes])


# ---------------------------------------------------------------- the head
def itd_woodworth(theta):
    """Interaural time difference (s) for azimuth theta (rad, 0 = front, +right), Woodworth's spherical-head formula."""
    th = np.abs(np.arcsin(np.sin(theta)))            # lateral angle: front and back mirror each other
    return A / C * (th + np.sin(th))


def shadow(x, angle_to_ear):
    """Brown & Duda head-shadow filter for one ear; angle_to_ear = angle between the source and that ear's axis."""
    w0 = C / A
    a_min, th_min = 0.1, np.radians(150)
    alpha = (1 + a_min / 2) + (1 - a_min / 2) * np.cos(angle_to_ear / th_min * np.pi)
    b, a = bilinear([alpha / (2 * w0), 1], [1 / (2 * w0), 1], SR)       # H(s) = (1 + alpha s/2w0) / (1 + s/2w0)
    return lfilter(b, a, x)


def frac_delay(x, d):
    """Delay by d samples (fractional) with a windowed-sinc filter."""
    n = np.arange(-32, 33)
    h = np.sinc(n - (d - int(d))) * np.hamming(len(n))
    y = np.convolve(x, h / h.sum(), mode="same")
    return np.concatenate([np.zeros(int(d)), y])[: len(x)]


def pinna(x, behind):
    """Outer-ear stand-in: sounds from behind lose some highs (one-pole low-pass blend)."""
    if not behind:
        return x
    b, a = bilinear([1], [1 / (2 * np.pi * 3500), 1], SR)
    return 0.45 * x + 0.55 * lfilter(b, a, x)


def render(x, theta, use_pinna=False):
    """Mono x placed at azimuth theta; returns (left, right)."""
    itd = itd_woodworth(theta)
    left_axis, right_axis = -np.pi / 2, np.pi / 2
    ang = lambda ear: np.abs(np.angle(np.exp(1j * (theta - ear))))
    L, R = shadow(x, ang(left_axis)), shadow(x, ang(right_axis))
    if np.sin(theta) > 0:            # source on the right: the left ear hears it later
        L = frac_delay(L, itd * SR)
    else:
        R = frac_delay(R, itd * SR)
    behind = np.cos(theta) < 0
    return pinna(L, use_pinna and behind), pinna(R, use_pinna and behind)


def measured_itd(L, R):
    """Delay of L relative to R in ms, from the cross-correlation peak (upsampled 8x)."""
    up = 8
    l = np.interp(np.arange(0, len(L), 1 / up), np.arange(len(L)), L)
    r = np.interp(np.arange(0, len(R), 1 / up), np.arange(len(R)), R)
    lag = 60 * up
    cc = [np.dot(l[lag:-lag], np.roll(r, k)[lag:-lag]) for k in range(-lag, lag + 1)]
    return (np.argmax(cc) - lag) / (SR * up) * 1000


def band_db(x, lo, hi):
    X = np.abs(np.fft.rfft(x)) ** 2
    f = np.fft.rfftfreq(len(x), 1 / SR)
    return 10 * np.log10(X[(f >= lo) & (f < hi)].sum() + 1e-20)


rng = np.random.default_rng(1113)
noise = rng.normal(0, 0.3, SR)                       # broadband test burst for the measurements
mel = melody(rng)

# 1. ITD vs direction
P("1. TIMING (ITD): left/right delay measured from the rendered ears, a broadband burst")
itd_rows = []
for deg in (0, 15, 30, 45, 60, 75, 90):
    L, R = render(noise, np.radians(deg))
    m = measured_itd(L, R)
    w = itd_woodworth(np.radians(deg)) * 1000
    itd_rows.append(dict(deg=deg, measured_ms=round(float(m), 3), formula_ms=round(float(w), 3)))
    P(f"  {deg:3d} deg: measured {m:.3f} ms (formula {w:.3f} ms)")
P(f"  maximum (90 deg, straight to one side): {itd_rows[-1]['measured_ms']:.3f} ms")

# 2. ILD by frequency at 90 degrees
L, R = render(noise, np.radians(90))
ild_low = band_db(R, 350, 700) - band_db(L, 350, 700)
ild_high = band_db(R, 3000, 6000) - band_db(L, 3000, 6000)
P("")
P(f"2. LEVEL (ILD) at 90 deg: low band (350-700 Hz) {ild_low:.1f} dB, high band (3-6 kHz) {ild_high:.1f} dB")

# 3. front / back
def ear_diff(a, b):
    """Spectral difference (dB, mean over 1-12 kHz bands) between two renders of the same ear."""
    edges = np.geomspace(1000, 12000, 13)
    return float(np.mean([abs(band_db(a, lo, hi) - band_db(b, lo, hi)) for lo, hi in zip(edges, edges[1:])]))


Lf, Rf = render(noise, np.radians(30))
Lb, Rb = render(noise, np.radians(150))
d_head = max(ear_diff(Lf, Lb), ear_diff(Rf, Rb))
itd_f, itd_b = measured_itd(Lf, Rf), measured_itd(Lb, Rb)
Lf2, Rf2 = render(noise, np.radians(30), True)
Lb2, Rb2 = render(noise, np.radians(150), True)
d_pinna = max(ear_diff(Lf2, Lb2), ear_diff(Rf2, Rb2))
P("")
P(f"3. FRONT/BACK (30 deg front-right vs 150 deg back-right)")
P(f"  head only: ITD {itd_f:.3f} vs {itd_b:.3f} ms; spectra differ by {d_head:.2f} dB on average: the ears can't tell them apart")
P(f"  with the outer-ear filter: spectra differ by {d_pinna:.1f} dB")

# 4. head tracking
P("")
P("4. HEAD TRACKING (a voice straight ahead; you turn your head 40 deg to the right)")
P("  without tracking: rendered at 0 deg from your nose, so it turns with you: it ends up 40 deg right of where it was")
P("  with tracking: rendered at -40 deg from your nose, so it stays where it was in the room")

# ---------------------------------------------------------------- listening clips
def norm(st):
    return (st / np.max(np.abs(st)) * 0.9 * 32767).astype(np.int16)


# circling: 8 seconds, one turn, rendered in short overlapping blocks, WITH the outer-ear filter (without it the
# back half of the turn gives the ears exactly the cues of the front half: B03's point)
blk, hop = 4096, 2048
dur = len(mel)
out = np.zeros((dur + blk, 2))
win = np.hanning(blk)
for s in range(0, dur - blk, hop):
    theta = 2 * np.pi * (s / dur)
    seg = mel[s:s + blk] * win
    L, R = render(np.concatenate([seg, np.zeros(256)]), theta, use_pinna=True)   # outer ear on: behind sounds different from in front
    out[s:s + blk, 0] += L[:blk]
    out[s:s + blk, 1] += R[:blk]
wavfile.write(EV / "circle.wav", SR, norm(out[:dur]))
one = melody(np.random.default_rng(7), bars=1)[: SR * 2]
for name, th, pin in (("front_head", 30, False), ("back_head", 150, False), ("front_pinna", 30, True), ("back_pinna", 150, True)):
    L, R = render(one, np.radians(th), pin)
    wavfile.write(EV / f"{name}.wav", SR, norm(np.stack([L, R], 1)))
P("")
P(f"LISTENING: circle.wav ({dur / SR:.1f} s, one turn around the head, outer-ear filter on); front/back pairs with and without the outer-ear filter")

res = dict(radius_m=A, itd=itd_rows, itd_max_ms=itd_rows[-1]["measured_ms"], ild_low_db=round(float(ild_low), 1),
           ild_high_db=round(float(ild_high), 1), frontback_head_db=round(d_head, 2), frontback_pinna_db=round(d_pinna, 1),
           itd_front_ms=round(float(itd_f), 3), itd_back_ms=round(float(itd_b), 3), turn_deg=40)
SCENE.update(res)
(EV / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
(EV / "scene.json").write_text(json.dumps(SCENE), encoding="utf-8")
(EV / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")
P("wrote evidence/run.log, results.json, scene.json, circle.wav, front/back WAVs")
