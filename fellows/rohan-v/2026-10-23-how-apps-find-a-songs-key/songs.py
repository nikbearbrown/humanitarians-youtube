"""Deterministic synthetic Western songs for the week-09 key evidence.

No recording is used: every song is generated from a seed, so the test set and the listening clip can be
committed and re-run exactly. A song is a chord progression (pad + bass), a melody drawn from the song's
scale, and a light drum-free pulse, in one of five Western styles:

    pop       major, I–V–vi–IV                      (home = the major key)
    minor     natural minor, i–VI–III–VII            (same notes as its relative major)
    harmonic  minor with a major V (raised 7th), i–iv–V–i
    rock      Mixolydian: I–bVII–IV–I (a flat 7th)  (same notes as the major key a fourth up)
    blues     12-bar, dominant sevenths I7–IV7–V7

    render(style, tonic, seed, seconds, sr, modulate_at=None, modulate_by=0) -> float32 mono, peak 0.9

`tonic` is a pitch class 0–11 (0 = C). With `modulate_at`, the song moves up `modulate_by` semitones at that
time (the pop "key change"). Two random streams: `music` decides the song (voicings, melody), `perf` the
performance (timing, loudness).
"""
import numpy as np

MAJOR = [0, 2, 4, 5, 7, 9, 11]
NAT_MINOR = [0, 2, 3, 5, 7, 8, 10]
HARM_MINOR = [0, 2, 3, 5, 7, 8, 11]
MIXO = [0, 2, 4, 5, 7, 9, 10]
BLUES_MEL = [0, 3, 5, 6, 7, 10]

# chord = (root offset from tonic in semitones, chord intervals)
MAJ, MIN, DOM7 = [0, 4, 7], [0, 3, 7], [0, 4, 7, 10]
STYLES = {
    "pop":      dict(mode="major", scale=MAJOR, bpm=(96, 124),
                     prog=[(0, MAJ), (7, MAJ), (9, MIN), (5, MAJ)]),
    "minor":    dict(mode="minor", scale=NAT_MINOR, bpm=(70, 96),
                     prog=[(0, MIN), (8, MAJ), (3, MAJ), (10, MAJ)]),
    "harmonic": dict(mode="minor", scale=HARM_MINOR, bpm=(76, 104),
                     prog=[(0, MIN), (5, MIN), (7, MAJ), (0, MIN)]),
    "rock":     dict(mode="major", scale=MIXO, bpm=(104, 132),
                     prog=[(0, MAJ), (10, MAJ), (5, MAJ), (0, MAJ)]),
    "blues":    dict(mode="major", scale=BLUES_MEL, bpm=(84, 116),
                     prog=[(0, DOM7)] * 4 + [(5, DOM7)] * 2 + [(0, DOM7)] * 2 + [(7, DOM7), (5, DOM7), (0, DOM7), (7, DOM7)]),
}


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def _env(n, sr, a, d, s=0.0):
    t = np.arange(n) / sr
    return np.minimum(1, t / max(a, 1e-4)) * (s + (1 - s) * np.exp(-t / max(d, 1e-4)))


def _tone(f, n, sr, harm):
    t = np.arange(n) / sr
    return sum(a * np.sin(2 * np.pi * f * k * t) for k, a in enumerate(harm, 1) if f * k < sr * 0.45)


def render(style, tonic, seed, seconds=20.0, sr=22050, modulate_at=None, modulate_by=0):
    S = STYLES[style]
    music = np.random.default_rng(seed)
    perf = np.random.default_rng(seed * 7919 + 5)
    bpm = music.uniform(*S["bpm"])
    beat = 60.0 / bpm
    bar = 4 * beat
    base = 48 + tonic                      # tonic near C3–B3
    n = int(seconds * sr)
    out = np.zeros(n + 3 * sr)

    def add(ts, sig, g):
        i = int(round(ts * sr))
        if 0 <= i < n:
            j = min(len(out), i + len(sig)); out[i:j] += g * sig[: j - i]

    # a melody walk over the scale, two notes per beat, phrase repeats every 4 bars with variation
    deg = int(music.integers(0, len(S["scale"])))
    t, b = 0.0, 0
    while t < seconds:
        shift = modulate_by if (modulate_at is not None and t >= modulate_at) else 0
        root_off, chord = S["prog"][b % len(S["prog"])]
        root = base + shift + root_off
        # pad: the chord, sustained over the bar, voiced around middle C
        L = int(bar * sr)
        for iv in chord:
            m = root + iv
            while m < 55:
                m += 12
            while m > 70:
                m -= 12
            add(t, _tone(hz(m), L, sr, [1, .45, .25, .12]) * _env(L, sr, 0.04, 9, 0.7), 0.06)
        # bass: root on beats 1 and 3, fifth on 2 and 4
        for k in range(4):
            m = root - 12 + (7 if k % 2 else 0)
            Lb = int(beat * 0.85 * sr)
            add(t + k * beat + perf.normal(0, 0.004), _tone(hz(m), Lb, sr, [1, .5, .2]) * _env(Lb, sr, 0.005, 0.35, 0.3),
                perf.uniform(0.16, 0.2))
        # melody: eighth notes from the scale, landing on a chord tone at each bar start
        for k in range(8):
            if k == 0:
                ct = (root_off + chord[int(music.integers(0, len(chord)))]) % 12
                deg = min(range(len(S["scale"])), key=lambda d: (S["scale"][d] - ct) % 12)
            else:
                deg = int(np.clip(deg + music.choice([-2, -1, -1, 0, 1, 1, 2]), 0, len(S["scale"]) * 2 - 1))
            if music.random() < 0.18:
                continue
            octv, d = divmod(deg, len(S["scale"]))
            m = base + shift + 12 + 12 * octv + S["scale"][d]
            Lm = int(beat / 2 * 0.9 * sr)
            add(t + k * beat / 2 + perf.normal(0, 0.006), _tone(hz(m), Lm, sr, [1, .35, .2, .1]) * _env(Lm, sr, 0.01, 0.3, 0.4),
                perf.uniform(0.09, 0.12))
        t += bar
        b += 1
    y = out[:n]
    return (0.9 * y / (np.max(np.abs(y)) + 1e-9)).astype(np.float32)
