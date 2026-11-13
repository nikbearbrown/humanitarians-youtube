"""Deterministic synthetic Western drum grooves for the week-08 tempo evidence.

No recording is used anywhere: every groove is generated from a seed, so the test set and the
listening clips can be committed and re-run exactly. Each groove is a drum kit (kick, snare or
clap, closed and open hats, ride) plus a simple bass line and a chord pad, so the detector hears
pitched sound as well as drums.

    render(style, bpm, seed, seconds, sr, drift=None) -> float32 mono, peak 0.9

`bpm` is the ground truth: the tempo a drummer would count, in quarter notes (for the waltz, in
its three beats per bar). `drift` makes a live drummer: a function of time (s) -> tempo factor,
plus small random timing; with drift=None the groove sits on a perfect grid (a drum machine) apart
from a few milliseconds of human looseness.

Two random streams keep this honest: `kit` decides the sounds and the pattern variations, `perf`
decides the performance (timing, loudness), so the same groove can be re-performed.
"""
import numpy as np

# Each style: beats per bar, steps per beat, and per-step patterns over one bar.
# Patterns are strings, one char per step: x = hit, o = soft hit (ghost / open), . = rest.
STYLES = {
    # 4/4, 16th-note grid (4 steps per beat)
    "rock":    dict(bpb=4, spb=4, swing=0.0,
                    kick="x.......x.x.....", snare="....x.......x...",
                    hat="x.x.x.x.x.x.x.x.", ohat="................", ride="", bass="x.......x.x....."),
    "funk":    dict(bpb=4, spb=4, swing=0.0,
                    kick="x..x..x...x..x..", snare="....x..o.o..x..o",
                    hat="xxxxxxxxxxxxxxxx", ohat="..............o.", ride="", bass="x..x..x...x.x..."),
    "house":   dict(bpb=4, spb=4, swing=0.0,
                    kick="x...x...x...x...", snare="....x.......x...",
                    hat="x.x.x.x.x.x.x.x.", ohat="..o...o...o...o.", ride="", bass="..x...x...x...x."),
    "hiphop":  dict(bpb=4, spb=4, swing=0.12,
                    kick="x......x.xx.....", snare="....x.......x...",
                    hat="x.x.x.x.x.x.x.x.", ohat="................", ride="", bass="x......x.x......"),
    "ballad":  dict(bpb=4, spb=4, swing=0.0,
                    kick="x.......x.......", snare="....x.......x...",
                    hat="x.x.x.x.x.x.x.x.", ohat="................", ride="", bass="x.......x......."),
    "dnb":     dict(bpb=4, spb=4, swing=0.0,
                    kick="x.........x.....", snare="....x.......x...",
                    hat="x.x.x.x.x.x.x.x.", ohat="................", ride="", bass="x.........x....."),
    # 3/4, eighth-note grid (2 steps per beat)
    "waltz":   dict(bpb=3, spb=2, swing=0.0,
                    kick="x.....", snare="..o.o.", hat="x.x.x.", ohat="......", ride="", bass="x....."),
    # 4/4 swing: ride "spang-a-lang", hi-hat foot on 2 and 4, eighth-note grid swung 2:1
    "swing":   dict(bpb=4, spb=2, swing=0.33,
                    kick="x.......", snare="......o.", hat="..x...x.", ohat="........",
                    ride="x.xxx.xx", bass="x.x.x.x."),
}
# Bass walks root-fifth-octave; pad holds the bar's chord.
PROG = [0, 5, 3, 4]  # scale-degree roots per bar, major scale
SCALE = [0, 2, 4, 5, 7, 9, 11]


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def _env(n, sr, a, d, s=0.0):
    t = np.arange(n) / sr
    return np.minimum(1, t / max(a, 1e-4)) * (s + (1 - s) * np.exp(-t / max(d, 1e-4)))


def _kick(perf, sr):
    L = int(0.32 * sr); t = np.arange(L) / sr
    f = 48 + 90 * np.exp(-t * 30)
    body = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t * 10)
    # the beater's click: a real kick has a short broadband attack on top of the low thump
    click = np.diff(np.concatenate([[0], perf.standard_normal(L)])) * np.exp(-t * 900)
    return body + 0.45 * click


def _snare(perf, sr):
    L = int(0.2 * sr); t = np.arange(L) / sr
    nz = np.diff(np.concatenate([[0], perf.standard_normal(L)]))
    return (0.8 * nz + 0.5 * np.sin(2 * np.pi * 185 * t)) * _env(L, sr, 0.001, 0.07)


def _hat(perf, sr, open_=False):
    L = int((0.22 if open_ else 0.05) * sr)
    h = np.diff(np.diff(np.concatenate([[0, 0], perf.standard_normal(L)])))
    return h * _env(L, sr, 0.0005, 0.09 if open_ else 0.014)


def _ride(perf, sr):
    L = int(0.5 * sr); t = np.arange(L) / sr
    h = np.diff(np.concatenate([[0], perf.standard_normal(L)]))
    bell = sum(np.sin(2 * np.pi * f * t) for f in (3150, 4470, 5220)) / 3
    return (0.5 * h + 0.5 * bell) * _env(L, sr, 0.001, 0.18)


def _tone(f, L, sr, harm):
    t = np.arange(L) / sr
    return sum(a * np.sin(2 * np.pi * f * k * t) for k, a in enumerate(harm, 1) if f * k < sr * 0.45)


def render(style, bpm, seed, seconds=30.0, sr=22050, drift=None, loose_ms=4.0):
    S = STYLES[style]
    kit = np.random.default_rng(seed)
    perf = np.random.default_rng(seed * 7919 + 3)
    root = int(kit.integers(40, 47))
    n = int(seconds * sr)
    out = np.zeros(n + 2 * sr)

    def add(ts, sig, g):
        i = int(round(ts * sr))
        if 0 <= i < n:
            j = min(len(out), i + len(sig)); out[i:j] += g * sig[: j - i]

    steps = S["bpb"] * S["spb"]
    # Walk musical time in steps; convert to seconds by integrating the (possibly drifting) tempo.
    t, step = 0.0, 0
    while t < seconds:
        bar, k = divmod(step, steps)
        beat_len = 60.0 / (bpm * (drift(t) if drift else 1.0))
        step_len = beat_len / S["spb"]
        # swing: delay every off-step of each pair by `swing` of a step
        sw = S["swing"] * step_len if (S["swing"] and k % 2 == 1) else 0.0
        ts = t + sw + perf.normal(0, loose_ms / 1000)
        fill = bar % 8 == 7 and k >= steps // 2
        if S["kick"][k] == "x":
            add(ts, _kick(perf, sr), perf.uniform(0.55, 0.7))
        sn = S["snare"][k]
        if sn != "." or (fill and k % 2 == 0):
            add(ts, _snare(perf, sr), perf.uniform(0.32, 0.42) if sn == "x" or fill else perf.uniform(0.06, 0.1))
        if S["hat"][k] == "x":
            add(ts, _hat(perf, sr), perf.uniform(0.05, 0.08) * (1.25 if k % S["spb"] == 0 else 0.8))
        if S["ohat"][k] == "o":
            add(ts, _hat(perf, sr, True), perf.uniform(0.05, 0.07))
        if S["ride"] and S["ride"][k] == "x":
            add(ts, _ride(perf, sr), perf.uniform(0.08, 0.11) * (1.2 if k % 2 == 0 else 0.75))
        deg = PROG[bar % 4]
        if S["bass"][k] == "x":
            m = root + SCALE[deg % 7] + (7 if (k // S["spb"]) % 2 else 0)
            L = int(beat_len * 0.8 * sr)
            add(ts, _tone(hz(m), L, sr, [1, .45, .2]) * _env(L, sr, 0.004, 0.3, 0.3), perf.uniform(0.22, 0.28))
        if k == 0:
            L = int(beat_len * S["bpb"] * sr)
            for d in (0, 2, 4):
                m = root + 24 + SCALE[(deg + d) % 7] + 12 * ((deg + d) // 7)
                add(ts, _tone(hz(m), L, sr, [1, .4, .25, .1]) * _env(L, sr, 0.08, 9, 0.6), 0.035)
        t += step_len
        step += 1
    y = out[:n]
    return (0.9 * y / (np.max(np.abs(y)) + 1e-9)).astype(np.float32)
