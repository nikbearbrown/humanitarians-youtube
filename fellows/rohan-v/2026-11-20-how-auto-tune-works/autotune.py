"""Executable evidence for "How Auto-Tune Works": a small pitch corrector, built from the textbook parts.

1. A synthetic singer (source-filter: a buzzing source shaped by "ah" vowel resonances) sings an original
   seven-note phrase in C major, slightly off-key on purpose: each note detuned, a scoop into each note, vibrato,
   slow drift. Separate random streams: `music` (the tune) and `perf` (the human wobble). We keep the true pitch.
2. Pitch detection: YIN (a normalised autocorrelation-style difference) every 5 ms. Scored against the true pitch.
3. Correction: snap each moment to the nearest note in C major; "retune speed" = how fast the correction follows
   (0 ms = instant, the hard robotic effect; 60 ms = gentle). The correction is applied to the AUDIO with TD-PSOLA
   (cut the wave into one-period grains, re-space them), using only the detected pitch, never the true one.
   The corrected audio is then measured again with the same detector.
4. Shifting without chipmunks: a held note moved up 4 semitones by plain resampling vs by PSOLA; duration and how far the
   vowel's resonances moved (a stretch fit of the cepstral spectral envelope) measured on each; the patent's way
   (resample, then repeat whole cycles to restore the length) is measured too.

    python autotune.py          -> evidence/*.wav, results.json, scene.json, run.log
"""
import json
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.linalg import solve_toeplitz
from scipy.signal import resample_poly, lfilter

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
SR = 44100
HOP = 0.005
KEY = "C major"
SCALE = {0, 2, 4, 5, 7, 9, 11}                     # pitch classes of C major
AH = [(850, 80), (1220, 90), (2810, 120), (3800, 150)]   # "ah" formants (Hz, bandwidth)

music = np.random.default_rng(1120)                # the tune
perf = np.random.default_rng(2026)                 # the singer's wobble

LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


def m2f(m):
    return 440.0 * 2 ** ((np.asarray(m) - 69) / 12)


def f2m(f):
    return 69 + 12 * np.log2(np.asarray(f) / 440.0)


def name(m):
    return ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"][int(round(m)) % 12] + str(int(round(m)) // 12 - 1)


# ---------------------------------------------------------------- 1. the singer
def formant_gain(f):
    g = np.ones_like(f)
    for F, B in AH:
        g *= F * F / np.sqrt((F * F - f * f) ** 2 + (f * B) ** 2)
    return g


def sing(f0, amp):
    """Additive source-filter voice: harmonics of f0(t), tilted like a voice, shaped by fixed vowel formants."""
    n = len(f0)
    phase = 2 * np.pi * np.cumsum(f0) / SR
    out = np.zeros(n)
    kmax = int(0.45 * SR / f0.min())
    for k in range(1, kmax + 1):
        fk = k * f0
        a = formant_gain(fk) / k ** 0.9 * np.clip((0.45 * SR - fk) / 2000, 0, 1)
        if a.max() < 1e-5:
            continue
        out += a * np.sin(k * phase + perf.uniform(0, 2 * np.pi))
    # a little breath: noise through the same vowel, following the loudness
    nz = perf.normal(0, 1, n)
    bf = np.fft.rfftfreq(n, 1 / SR)
    nz = np.fft.irfft(np.fft.rfft(nz) * formant_gain(np.maximum(bf, 1)) / np.maximum(bf / 300, 1) ** 0.5, n)
    out = out / np.abs(out).max() + 0.035 * nz / np.abs(nz).max()
    out *= amp
    return out / np.abs(out).max() * 0.8


TUNE = [64, 67, 69, 67, 64, 62, 60]                  # E4 G4 A4 G4 E4 D4 C4 (an original phrase in C major)
LENS = [0.42, 0.42, 0.62, 0.40, 0.42, 0.44, 0.80]   # seconds; the A and the last C are held


def performance():
    detune = perf.uniform(14, 42, len(TUNE)) * perf.choice([-1, 1], len(TUNE))
    t_starts = np.concatenate([[0.12], 0.12 + np.cumsum(LENS)[:-1]]) + perf.normal(0, 0.012, len(TUNE))
    total = 0.12 + sum(LENS) + 0.25
    n = int(total * SR)
    t = np.arange(n) / SR
    cents = np.zeros(n)
    amp = np.zeros(n)
    for i, (m, L) in enumerate(zip(TUNE, LENS)):
        s = t_starts[i]
        e = t_starts[i + 1] if i + 1 < len(TUNE) else 0.12 + sum(LENS)
        sel = (t >= s) & (t < e)
        tt = t[sel] - s
        scoop = -perf.uniform(60, 110) * np.exp(-tt / perf.uniform(0.035, 0.06))       # slide up into the note
        vib_on = np.clip((tt - 0.16) / 0.15, 0, 1)
        vib = perf.uniform(16, 24) * vib_on * np.sin(2 * np.pi * perf.uniform(5.2, 5.9) * tt + perf.uniform(0, 6))
        drift = perf.uniform(-8, 8) * tt / max(L, 0.3)
        cents[sel] = m * 100 + detune[i] + scoop + vib + drift
        a = np.clip(tt / 0.03, 0, 1) * np.clip((e - s - tt) / 0.05, 0.35, 1)
        amp[sel] = a * (0.85 + 0.15 * np.cos(2 * np.pi * 1.3 * tt))
    # sing from the first note's onset to the end; quiet head and tail
    first, last = t_starts[0], 0.12 + sum(LENS)
    cents[t < first] = cents[(t >= first)][0]
    cents[t >= last] = cents[t < last][-1]
    amp *= np.clip((last + 0.08 - t) / 0.08, 0, 1)
    # smooth the joins (a voice can't jump in zero time)
    k = int(0.012 * SR)
    cents = np.convolve(np.pad(cents, k, mode="edge"), np.ones(k) / k, mode="same")[k:-k]
    amp = np.convolve(np.pad(amp, k, mode="edge"), np.ones(k) / k, mode="same")[k:-k]
    f0 = m2f(cents / 100)
    return t, f0, amp, detune, t_starts, last


# ---------------------------------------------------------------- 2. pitch detection (YIN)
def yin(x, fmin=110, fmax=700, win=0.032, thr=0.12, keep=None):
    W = int(win * SR)
    tmin, tmax = int(SR / fmax), int(SR / fmin)
    hop = int(HOP * SR)
    times, f0s, conf = [], [], []
    for c in range(W // 2 + tmax, len(x) - W // 2 - tmax, hop):
        fr = x[c - W // 2: c - W // 2 + W + tmax + 1]
        if np.sqrt(np.mean(fr[:W] ** 2)) < 0.01:
            times.append(c / SR); f0s.append(np.nan); conf.append(0.0)
            continue
        # difference function d(tau) = sum (x[j] - x[j+tau])^2, by FFT autocorrelation
        a = fr[:W]
        e0 = np.sum(a ** 2)
        cs = np.concatenate([[0], np.cumsum(fr ** 2)])
        et = cs[np.arange(tmax + 1) + W] - cs[np.arange(tmax + 1)]
        n = 1 << int(np.ceil(np.log2(len(fr) + W)))
        r = np.fft.irfft(np.fft.rfft(fr, n) * np.conj(np.fft.rfft(a, n)), n)[:tmax + 1]
        d = e0 + et - 2 * r
        d[0] = 0
        cmnd = d.copy()
        cmnd[1:] = d[1:] * np.arange(1, tmax + 1) / np.maximum(np.cumsum(d[1:]), 1e-12)
        cand = np.where(cmnd[tmin:tmax] < thr)[0]
        if len(cand):
            tau = tmin + cand[0]
            while tau + 1 < tmax and cmnd[tau + 1] < cmnd[tau]:
                tau += 1
        else:
            tau = tmin + int(np.argmin(cmnd[tmin:tmax]))
        if 1 <= tau < tmax:      # parabolic interpolation
            y0, y1, y2 = cmnd[tau - 1], cmnd[tau], cmnd[tau + 1]
            den = y0 - 2 * y1 + y2
            frac = 0.5 * (y0 - y2) / den if abs(den) > 1e-12 else 0
        else:
            frac = 0
        times.append(c / SR); f0s.append(SR / (tau + frac)); conf.append(1 - cmnd[tau])
        if keep is not None and abs(c / SR - keep["at"]) < HOP / 2:
            keep["cmnd"] = cmnd[: int(SR / 150)].tolist()
            keep["wave"] = fr[: int(0.012 * SR)].tolist()
            keep["tau"] = tau + frac
    return np.array(times), np.array(f0s), np.array(conf)


# ---------------------------------------------------------------- 3. correction
def snap_cents(m):
    """Nearest note of the key (in MIDI, for an array of MIDI floats)."""
    base = np.floor(m)
    cands = np.stack([base + d for d in range(-2, 4)])
    ok = np.isin(np.mod(cands, 12).astype(int), list(SCALE))
    dist = np.where(ok, np.abs(cands - m), 99)
    return cands[np.argmin(dist, axis=0), np.arange(len(m))]


def correction(times, det_m, speed_ms):
    """Cents of correction over time; follows (target - detected) with a one-pole lag of `speed_ms`."""
    v = ~np.isnan(det_m)
    m = np.where(v, det_m, np.interp(times, times[v], det_m[v]))
    target = snap_cents(m)
    err = (target - m) * 100
    if speed_ms <= 0:
        return target, err, err
    k = 1 - np.exp(-HOP * 1000 / speed_ms)
    a = np.zeros_like(err)
    acc = err[0]
    for i, e in enumerate(err):
        acc += (e - acc) * k
        a[i] = acc
    return target, err, a


def pitch_marks(x, f0_of_t):
    """One mark per period, snapped to the local peak of a smoothed copy of the wave."""
    lp = lfilter([1 - 0.85], [1, -0.85], x)
    marks = []
    t = 0.13
    end = len(x) / SR - 0.02
    while t < end:
        P = 1 / f0_of_t(t)
        c = int(t * SR)
        w = int(P * SR * 0.3)
        lo, hi = max(c - w, 0), min(c + w, len(x) - 1)
        p = lo + int(np.argmax(lp[lo:hi])) if hi > lo else c
        marks.append(p)
        t = p / SR + P
    return np.array(marks)


def psola(x, marks, f_in, ratio_of_t, tmap=None, n_out=None):
    """TD-PSOLA: two-period Hann grains around each input mark, re-placed at the new period; duration unchanged.
    tmap (output time -> input time) lets the same machinery stretch time instead (whole cycles repeated)."""
    tmap = tmap or (lambda s: s)
    n_out = n_out or len(x)
    out = np.zeros(n_out + SR // 10)
    norm = np.zeros_like(out)
    t = marks[0] / SR
    end = n_out / SR - 0.02
    while t < end and tmap(t) < marks[-1] / SR:
        i = int(np.argmin(np.abs(marks / SR - tmap(t))))
        P_in = 1 / f_in(marks[i] / SR)
        L = int(P_in * SR)
        c = marks[i]
        if c - L < 0 or c + L >= len(x):
            t += P_in
            continue
        win = np.hanning(2 * L + 1)
        g = x[c - L: c + L + 1] * win
        o = int(t * SR)
        out[o - L: o + L + 1] += g
        norm[o - L: o + L + 1] += win
        t += P_in / ratio_of_t(t)
    norm[norm < 0.3] = 1
    y = (out / norm)[: n_out]
    nz = np.nonzero(np.abs(y) > 1e-4)[0]
    f = int(0.01 * SR)
    if len(nz):      # 10 ms fades where the grains start and stop (no edge click)
        y[nz[0]: nz[0] + f] *= np.linspace(0, 1, f)[: len(y[nz[0]: nz[0] + f])]
        y[max(nz[-1] - f, 0): nz[-1]] *= np.linspace(1, 0, len(y[max(nz[-1] - f, 0): nz[-1]]))
    return y


def lpc_formants(seg, sr_to=11025, order=12):
    y = resample_poly(seg, sr_to, SR)
    y = np.append(y[0], y[1:] - 0.94 * y[:-1]) * np.hamming(len(y))
    r = np.correlate(y, y, "full")[len(y) - 1: len(y) + order]
    a = solve_toeplitz(r[:order], -r[1: order + 1])
    roots = np.roots(np.concatenate([[1], a]))
    roots = roots[np.imag(roots) > 0]
    fr = np.angle(roots) * sr_to / (2 * np.pi)
    bw = -np.log(np.abs(roots)) * sr_to / np.pi
    f = sorted(fr[(fr > 250) & (bw < 500)])
    return f[:2]


def envelope(seg, lifter=80):
    """The vowel's spectral envelope (dB): per-frame cepstral smoothing (harmonics removed), averaged."""
    W, hop = 4096, 512
    acc = np.zeros(W // 2 + 1)
    n = 0
    for s0 in range(0, len(seg) - W, hop):
        X = np.abs(np.fft.rfft(seg[s0:s0 + W] * np.hanning(W))) + 1e-9
        c = np.fft.irfft(np.log(X), W)
        c[lifter:W - lifter] = 0
        acc += np.fft.rfft(c, W).real * 20 / np.log(10)
        n += 1
    return np.fft.rfftfreq(W, 1 / SR), acc / n


def envelope_shift(seg, ref):
    """How far the whole envelope moved: the stretch a that best maps ref's envelope onto seg's (400-4000 Hz)."""
    f, e = envelope(seg)
    _, e0 = envelope(ref)
    ff = np.geomspace(400, 4000, 400)
    y = np.interp(ff, f, e)
    best, ba = -2, 1
    for a in np.geomspace(0.7, 1.5, 1601):
        y0 = np.interp(ff / a, f, e0)
        c = np.corrcoef(y, y0)[0, 1]
        if c > best:
            best, ba = c, a
    return float(ba), float(best)


def wav(name_, x):
    wavfile.write(EV / name_, SR, (np.clip(x, -1, 1) * 32767).astype(np.int16))


def main():
    # 1. the take
    t, f0_true, amp, detune, t_starts, t_end = performance()
    x = sing(f0_true, amp)
    wav("take.wav", x)
    log("AUTO-TUNE EVIDENCE (autotune.py): a synthetic singer, a YIN pitch detector, a PSOLA pitch corrector")
    log(f"THE TAKE: {len(TUNE)} notes in {KEY} ({' '.join(name(m) for m in TUNE)}), {len(x) / SR:.2f} s, vowel 'ah'")
    log("  sung off-key on purpose; each note's detune (cents): " + ", ".join(f"{d:+.0f}" for d in detune))
    log(f"  average detune {np.mean(np.abs(detune)):.1f} cents (100 cents = one semitone)")

    results = {}
    # 2. detection, scored against the truth
    keep = {"at": float(t_starts[2] + 0.30)}
    tm, f_det, conf = yin(x, keep=keep)
    voiced = ~np.isnan(f_det) & (tm > t_starts[0] + 0.03) & (tm < t_end - 0.03)
    truth_m = f2m(np.interp(tm, t, f0_true))
    err_c = (f2m(f_det) - truth_m) * 100
    e = np.abs(err_c[voiced])
    log()
    log(f"1. PITCH DETECTION (YIN, 32 ms window, every {HOP * 1000:.0f} ms), {voiced.sum()} sung frames")
    log(f"  error vs the true pitch: median {np.median(e):.2f} cents, 95th percentile {np.percentile(e, 95):.2f} cents, "
        f"worst {e.max():.1f} cents; {np.mean(e < 5) * 100:.1f}% of frames within 5 cents")
    miss = np.where(voiced & (np.abs(err_c) > 50))[0]
    near_on = [float(np.min(np.abs(tm[i] - t_starts))) for i in miss]
    log(f"  misses (over 50 cents): {len(miss)} frames, all within {max(near_on) * 1000 if near_on else 0:.0f} ms of a note's start "
        f"(where the old note fades and the new one begins)")
    results["yin"] = {"misses": len(miss), "miss_max_ms_from_onset": max(near_on) * 1000 if near_on else 0}
    log(f"  example frame at {keep['at']:.2f} s (the A4): best repeat after {keep['tau'] / SR * 1000:.3f} ms -> "
        f"{SR / keep['tau']:.1f} Hz (true {np.interp(keep['at'], t, f0_true):.1f} Hz; A4 = 440 Hz)")

    # 3. correction at two retune speeds, applied to the audio by PSOLA, then measured again
    det_m = f2m(f_det)
    det_m[~voiced] = np.nan
    marks = pitch_marks(x, lambda s: np.interp(s, tm[voiced], f_det[voiced]))
    results.update({"detune_cents": detune.round(1).tolist(), "avg_detune": float(np.mean(np.abs(detune))),
               "yin_score": {"median_cents": float(np.median(e)), "p95_cents": float(np.percentile(e, 95)),
                       "within5": float(np.mean(e < 5)), "frames": int(voiced.sum())}})
    tracks = {}
    note_idx = np.searchsorted(t_starts, tm, side="right") - 1

    def note_offsets(m_track):
        offs, vibs = [], []
        for i, m in enumerate(TUNE):
            s = t_starts[i] + 0.12
            e_ = (t_starts[i + 1] if i + 1 < len(TUNE) else t_end) - 0.04
            sel = (tm > s) & (tm < e_) & ~np.isnan(m_track)
            c = (m_track[sel] - m) * 100
            offs.append(float(np.median(c)))
            vibs.append(float(np.percentile(c, 95) - np.percentile(c, 5)) / 2)
        return np.array(offs), np.array(vibs)

    def on_note(m_track):
        v_ = ~np.isnan(m_track) & voiced
        return float(np.mean(np.abs(m_track[v_] - np.round(m_track[v_])) * 100 < 5))

    o0, v0 = note_offsets(f2m(np.where(voiced, f_det, np.nan)))
    log()
    log(f"2. HOW FAR OFF THE NOTES (measured from the detected pitch, middle of each note)")
    log(f"  as sung: average {np.mean(np.abs(o0)):.1f} cents off; vibrato swing about +/-{np.mean(v0):.0f} cents")
    results["as_sung"] = {"avg_off": float(np.mean(np.abs(o0))), "vib": float(np.mean(v0)), "offsets": o0.round(1).tolist(),
                          "on_note": on_note(np.where(voiced, det_m, np.nan))}
    log(f"  as sung: within 5 cents of a note {results['as_sung']['on_note'] * 100:.1f}% of the sung time")
    tracks["detected"] = det_m
    tracks["truth"] = truth_m
    for label, speed in (("gentle", 60), ("hard", 0)):
        target, err, a = correction(tm, det_m, speed)
        if label == "hard":
            tracks["target"] = target
        corr_c = np.where(voiced, a, 0)
        ratio = lambda s, cc=corr_c: 2 ** (np.interp(s, tm, cc) / 1200)
        y = psola(x, marks, lambda s: np.interp(s, tm[voiced], f_det[voiced]), ratio)
        y = y / np.abs(y).max() * 0.8
        wav(f"{label}.wav", y)
        tm2, f2, _ = yin(y)
        f2i = np.interp(tm, tm2, np.nan_to_num(f2, nan=0.0))
        f2i[(f2i <= 0) | ~voiced] = np.nan
        out_m = f2m(f2i)
        tracks[label] = out_m
        o, v = note_offsets(out_m)
        results[label] = {"retune_ms": speed, "avg_off": float(np.nanmean(np.abs(o))), "vib": float(np.mean(v)),
                          "offsets": np.round(o, 1).tolist(), "on_note": on_note(out_m)}
        log(f"  {label} (retune speed {speed} ms): average {np.mean(np.abs(o)):.1f} cents off; vibrato about +/-{np.mean(v):.0f} cents; "
            f"within 5 cents of a note {on_note(out_m) * 100:.1f}% of the sung time")
    # 4. shifting a held note: resampling vs PSOLA
    hold_t = np.arange(int(1.6 * SR)) / SR
    hf0 = m2f(60 + (18 * np.clip((hold_t - 0.2) / 0.2, 0, 1) * np.sin(2 * np.pi * 5.5 * hold_t)) / 100)
    hamp = np.clip(hold_t / 0.04, 0, 1) * np.clip((1.6 - hold_t) / 0.08, 0, 1)
    h = sing(hf0, hamp)
    wav("held_c4.wav", h)
    up = 4
    r = 2 ** (up / 12)
    chip = resample_poly(h, 100, int(round(100 * r)))          # play it faster: up 4 semitones, shorter
    wav("held_resampled.wav", chip / np.abs(chip).max() * 0.8)
    tmh, fh, _ = yin(h)
    vh = ~np.isnan(fh)
    mk = pitch_marks(h, lambda s: np.interp(s, tmh[vh], fh[vh]))
    ps = psola(h, mk, lambda s: np.interp(s, tmh[vh], fh[vh]), lambda s: r)
    wav("held_psola.wav", ps / np.abs(ps).max() * 0.8)
    # the patent's way: resample (pitch up, shorter), then repeat whole cycles to restore the length
    tmc, fc, _ = yin(chip)
    vc = ~np.isnan(fc)
    mkc = pitch_marks(chip, lambda s: np.interp(s, tmc[vc], fc[vc]))
    cyc = psola(chip, mkc, lambda s: np.interp(s, tmc[vc], fc[vc]), lambda s: 1.0, tmap=lambda s: s / r, n_out=len(h))
    wav("held_cycles.wav", cyc / np.abs(cyc).max() * 0.8)

    def measure(sig):
        tq, fq, _ = yin(sig)
        mid = (tq > 0.25 * len(sig) / SR) & (tq < 0.8 * len(sig) / SR) & ~np.isnan(fq)
        seg = sig[int(0.2 * len(sig)): int(0.85 * len(sig))]
        return {"dur": len(sig) / SR, "f0": float(np.median(fq[mid])), "seg": seg}

    m0, m1, m2, m3 = measure(h), measure(chip), measure(ps), measure(cyc)
    log()
    log(f"3. SHIFTING A HELD NOTE UP {up} SEMITONES (C4 -> E4, x{r:.3f}); the vowel's resonances (its spectral envelope)")
    for lab, m in (("original", m0), ("plain resampling", m1), ("resample + repeat cycles (the patent's way)", m3), ("PSOLA", m2)):
        a_, c_ = envelope_shift(m["seg"], m0["seg"])
        m["env_shift"], m["env_corr"] = a_, c_
        log(f"  {lab:44s}: {m['dur']:.2f} s, pitch {m['f0']:.1f} Hz, resonances moved x{a_:.3f} ({(a_ - 1) * 100:+.1f}%, match r={c_:.3f})")
    for m in (m0, m1, m2, m3):
        m.pop("seg")
    results["shift"] = {"semitones": up, "ratio": r, "orig": m0, "resampled": m1, "psola": m2, "cycles": m3}
    log()
    log("LISTENING: take.wav (as sung), gentle.wav (60 ms), hard.wav (0 ms); held_c4 / held_resampled / held_cycles / held_psola")

    # scene data: decimate to 10 ms for drawing
    sel = np.arange(0, len(tm), 2)
    scene = {"t": tm[sel].round(3).tolist(), "t_starts": t_starts.round(3).tolist(), "t_end": round(float(t_end), 3),
             "tune": TUNE, "names": [name(m) for m in TUNE], "key": KEY,
             "tracks": {k: [None if np.isnan(v) else round(float(v), 3) for v in tracks[k][sel]] for k in tracks},
             "frame": {"at": keep["at"], "wave": np.array(keep["wave"])[::2].round(4).tolist(),
                       "cmnd": np.array(keep["cmnd"])[::2].round(4).tolist(), "step_ms": 2000 / SR,
                       "tau_ms": keep["tau"] / SR * 1000, "hz": SR / keep["tau"]},
             "results": results}
    (EV / "scene.json").write_text(json.dumps(scene), encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
    (EV / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
