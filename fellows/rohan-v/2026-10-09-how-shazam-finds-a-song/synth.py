"""Deterministic synthetic music for the week-07 evidence programs.

No copyrighted recording is used anywhere: every "song" is generated here from a seed, so
the library, the queries and the listening clips can all be committed and re-run exactly.
A song has a key, sections (verse and chorus, each with its own chords and melody, so the
song does not loop bar for bar), a bass line, a melody, drums for the band styles, and small
human timing and loudness variations.

    render(seed, seconds, sr, style="band", transpose=0, tempo=1.0) -> float32 mono, peak 0.9

`transpose` (semitones) and `tempo` (speed factor) re-perform the same song: the same notes and
rhythm in another key or at another speed, which is what a cover or a live take changes.
style="hum" is the song's melody alone, hummed: a plain tone an octave lower, with the small
pitch and timing wobble a person adds. Two random streams keep this honest: `music` decides
the song (key, tempo, chords, melodies), `perf` decides the performance (drum noise, timing,
loudness), so the hummed or re-keyed version is the same song, not a new one.
"""
import numpy as np

SCALES = {"major": [0, 2, 4, 5, 7, 9, 11], "minor": [0, 2, 3, 5, 7, 8, 10]}
PROGS = [[0, 4, 5, 3], [0, 5, 3, 4], [5, 3, 0, 4], [0, 3, 4, 4], [0, 5, 1, 4], [3, 4, 0, 5]]
STYLES = {
    #            bpm range   drums  piano  pad   lead  bass
    "band":     ((92, 126),  1.0,   0.0,   0.55, 0.6,  0.8),
    "piano":    ((66, 80),   0.0,   1.0,   0.25, 0.0,  0.35),
    "drums":    ((126, 142), 1.35,  0.0,   0.15, 0.25, 0.9),
    "hum":      ((92, 126),  0.0,   0.0,   0.0,  1.0,  0.0),
}
FORM = ["V", "V", "C", "V", "C", "C", "V", "C"]   # 4-bar sections


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def _env(n, sr, a=0.005, d=0.25, s=0.0):
    t = np.arange(n) / sr
    att = np.minimum(1, t / max(a, 1e-4))
    return att * (s + (1 - s) * np.exp(-t / max(d, 1e-4)))


def _tone(f, n, sr, harm, decay_h=1.0):
    t = np.arange(n) / sr
    out = np.zeros(n)
    for k, amp in enumerate(harm, 1):
        if f * k > sr * 0.45:
            break
        out += amp * np.sin(2 * np.pi * f * k * t) * np.exp(-t * decay_h * (k - 1))
    return out


def _phrase(music):
    out, d = [], int(music.integers(0, 5))
    for _ in range(32):                       # 4 bars of eighth notes
        d = int(np.clip(d + music.choice([-2, -1, -1, 0, 1, 1, 2]), -2, 9))
        out.append(None if music.random() < 0.2 else d)
    return out


def render(seed, seconds, sr, style="band", transpose=0.0, tempo=1.0):
    music = np.random.default_rng(seed)
    perf = np.random.default_rng(seed * 7919 + 1)
    hum = style == "hum"
    huma = np.random.default_rng(seed + 424242)        # the hummer's own wobble
    (b0, b1), w_drum, w_piano, w_pad, w_lead, w_bass = STYLES[style]
    bpm = music.uniform(*STYLES["band" if hum else style][0]) * tempo
    beat = 60.0 / bpm
    root = int(music.integers(55, 63))
    scale = SCALES["major" if music.random() < 0.6 else "minor"]
    sections = {"V": (PROGS[int(music.integers(len(PROGS)))], _phrase(music)),
                "C": (PROGS[int(music.integers(len(PROGS)))], _phrase(music))}
    kicks = [[1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0, 0, 1]]
    n = int(seconds * sr)
    out = np.zeros(n + sr * 3)
    deg = lambda d, octv=0: root + transpose + 12 * (octv + d // 7) + scale[d % 7]

    def add(start_s, sig):
        i = int(start_s * sr)
        if i >= n or i < 0:
            return
        j = min(len(out), i + len(sig))
        out[i:j] += sig[: j - i]

    def jit(ms=6):
        return perf.normal(0, ms / 1000)

    t, bar = 0.0, 0
    while t < seconds:
        sec = FORM[(bar // 4) % len(FORM)]
        prog, phrase = sections[sec]
        chord_deg = prog[bar % 4]
        chord = [chord_deg, chord_deg + 2, chord_deg + 4]
        bar_len = 4 * beat
        lift = 12 if sec == "C" else 0
        if w_pad:
            L = int(bar_len * sr)
            for cd in chord:
                add(t, w_pad * 0.16 * _tone(hz(deg(cd) + (lift if cd == chord[0] else 0)), L, sr,
                                           [1, .45, .3, .2, .12], 0.6) * _env(L, sr, 0.05, 9, 0.6))
        if w_piano:
            for k in range(8):
                cd = chord[[0, 1, 2, 1, 0, 2, 1, 2][k]] + (7 if k in (2, 5) else 0)
                L = int(1.6 * sr)
                add(t + k * beat / 2 + jit(), w_piano * perf.uniform(0.22, 0.34)
                    * _tone(hz(deg(cd)), L, sr, [1, .6, .35, .22, .14, .08], 2.2) * _env(L, sr, 0.003, 0.55))
        if w_bass:
            pat = [0, 1, 2, 3] if sec == "V" else [0, 1.5, 2, 3, 3.5]
            for k in pat:
                L = int(beat * 0.8 * sr)
                add(t + k * beat + jit(), w_bass * perf.uniform(0.26, 0.36)
                    * _tone(hz(deg(chord_deg, -2)), L, sr, [1, .5, .2], 0.5) * _env(L, sr, 0.004, 0.32, 0.25))
        if w_lead:
            for k in range(8):
                step = phrase[(bar % 4) * 8 + k]
                if step is None:
                    continue
                L = int(beat / 2 * 0.95 * sr)
                tt = np.arange(L) / sr
                if hum:   # an octave lower, a soft tone, wobbling pitch and timing
                    f = hz(deg(step) + huma.normal(0, 0.3))
                    ph = 2 * np.pi * np.cumsum(f * (1 + 0.006 * np.sin(2 * np.pi * huma.uniform(4, 6) * tt))) / sr
                    sig = (np.sin(ph) + 0.15 * np.sin(2 * ph)) * _env(L, sr, 0.04, 0.5, 0.6)
                    add(t + k * beat / 2 + huma.normal(0, 0.04), 0.35 * sig)
                    continue
                f = hz(deg(step, 1))
                vib = np.sin(2 * np.pi * f * tt + 0.004 * f * np.sin(2 * np.pi * 5.5 * tt) / 5.5)
                sq = vib + 0.33 * np.sin(3 * np.arcsin(np.clip(vib, -1, 1)))
                add(t + k * beat / 2 + jit(), w_lead * perf.uniform(0.16, 0.22) * sq * _env(L, sr, 0.01, 0.4, 0.5))
        if w_drum:
            kick_pat = kicks[(bar // 4 + (1 if sec == "C" else 0)) % len(kicks)]
            fill = bar % 8 == 7
            for k in range(8):
                ts = t + k * beat / 2 + jit(3)
                if kick_pat[k]:
                    L = int(0.35 * sr)
                    tt = np.arange(L) / sr
                    f = 45 + 75 * np.exp(-tt * 28)
                    add(ts, w_drum * perf.uniform(0.45, 0.6) * np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-tt * 9))
                if k in (2, 6) or (fill and k >= 4):
                    L = int(0.2 * sr)
                    nz = np.diff(np.concatenate([[0], perf.standard_normal(L)]))
                    add(ts, w_drum * perf.uniform(0.14, 0.2)
                        * (nz + 0.6 * np.sin(2 * np.pi * 190 * np.arange(L) / sr)) * _env(L, sr, 0.001, 0.06))
                L = int(0.05 * sr)
                hat = np.diff(np.diff(np.concatenate([[0, 0], perf.standard_normal(L)])))
                add(ts, w_drum * perf.uniform(0.025, 0.04) * hat * _env(L, sr, 0.0005, 0.012))
                if style == "drums" and perf.random() < 0.45:
                    add(ts + beat / 4, w_drum * 0.02 * hat * _env(L, sr, 0.0005, 0.01))
        t += bar_len
        bar += 1
    y = out[:n]
    return (0.9 * y / (np.max(np.abs(y)) + 1e-9)).astype(np.float32)
