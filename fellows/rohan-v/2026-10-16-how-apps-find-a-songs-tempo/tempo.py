"""A tempo detector built the classic way, and tested on synthetic Western grooves.

    python tempo.py            # writes evidence/run.log and evidence/results.json

Pipeline (the shape of Ellis 2007 / librosa, written from scratch with numpy):
  1. onset curve  — STFT (centred frames), 40 overlapping mel bands in dB, spectral flux (sum of each band's increase
                    from one frame to the next).
  2. periodicity  — autocorrelation of the onset curve: slide it against itself; a lag where it
                    lines up with itself is a candidate beat period. BPM = 60 / lag. As librosa
                    does it: in 8-second Hann-windowed stretches, averaged.
  3. choosing     — "raw": the strongest lag between 40 and 240 BPM.
                    "prior": the same curve weighted by a bell on log2(BPM), centred at 120 BPM,
                    one octave wide (librosa's default start_bpm=120, std_bpm=1.0).
  4. beats        — dynamic-programming beat tracker (Ellis 2007): each beat lands on a strong
                    onset while keeping the spacing near the chosen period.

Scoring: "right" = within 4% of the true BPM (Accuracy 1, ISMIR 2004 / Gouyon et al. 2006);
"half" / "double" / "third" / "triple" = within 4% of that multiple (the extra cases Accuracy 2
forgives); anything else = "wrong".
"""
import json
from pathlib import Path

import numpy as np

import grooves

try:   # optional cross-check: librosa installed outside the repo (PYTHONPATH), never required
    import librosa as LIBROSA
except ImportError:
    LIBROSA = None

SR, NFFT, HOP = 22050, 2048, 512
FPS = SR / HOP
HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"

# The test set: tempos chosen by me to cover each style's usual feel (not a claim about genres).
SET = {
    "rock":   [100, 112, 120, 132, 144],
    "funk":   [96, 100, 104, 108, 112],
    "house":  [118, 122, 124, 126, 128],
    "hiphop": [80, 85, 88, 92, 96],
    "ballad": [60, 64, 68, 72, 76],
    "dnb":    [160, 165, 170, 174, 178],
    "waltz":  [84, 96, 108, 120, 132],
    "swing":  [110, 130, 150, 170, 190],
}
NAMES = {"rock": "Rock", "funk": "Funk", "house": "House", "hiphop": "Hip hop", "ballad": "Slow ballad",
         "dnb": "Drum and bass", "waltz": "Waltz (3/4)", "swing": "Jazz swing"}


def mel(f):
    return 2595 * np.log10(1 + f / 700)


def bands_db(y):
    """Centred frames (frame i is centred on i*HOP, as librosa's center=True), 40 mel bands."""
    y = np.pad(y, NFFT // 2)
    win = np.hanning(NFFT)
    nfr = 1 + (len(y) - NFFT) // HOP
    fr = np.lib.stride_tricks.as_strided(y, (nfr, NFFT), (y.strides[0] * HOP, y.strides[0])) * win
    P = np.abs(np.fft.rfft(fr, axis=1)) ** 2
    f = np.fft.rfftfreq(NFFT, 1 / SR)
    m = np.linspace(mel(30), mel(SR / 2), 42)
    edges = 700 * (10 ** (m / 2595) - 1)
    B = np.stack([P[:, (f >= lo) & (f < hi)].sum(1) for lo, hi in zip(edges[:-2], edges[2:])], 1)
    D = 10 * np.log10(B + 1e-10)
    return np.maximum(D, D.max() - 80)                      # frames x 40


def onset_curve(y):
    D = bands_db(y)
    flux = np.maximum(0, np.diff(D, axis=0)).mean(1)        # spectral flux, half-wave rectified
    flux = np.concatenate([[0], flux])
    return flux, D                                          # kept positive, as librosa does


WIN_S = 8.0   # librosa's ac_size: autocorrelation in 8-second windows, then averaged


def autocorr(o, win_s=WIN_S, step=4):
    """Average windowed autocorrelation (librosa's tempogram, then its mean over time): each 8-s
    stretch of the onset curve, Hann-windowed, slid against itself; normalised so lag 0 = 1."""
    n = int(round(win_s * FPS))
    w = np.hanning(n)
    acc = np.zeros(n)
    for s in range(0, max(1, len(o) - n + 1), step):
        seg = o[s:s + n] * w
        F = np.fft.rfft(seg, 2 * n)
        a = np.fft.irfft(F * np.conj(F))[:n]
        if a[0] > 0:
            acc += a / a[0]
    return acc / acc[0]


def prior(bpm, centre=120.0, octaves=1.0):
    return np.exp(-0.5 * (np.log2(bpm / centre) / octaves) ** 2)


def estimate(o):
    ac = autocorr(o)
    lags = np.arange(1, len(ac))
    bpm = 60 * FPS / lags
    keep = (bpm >= 40) & (bpm <= 240)
    L, B, A = lags[keep], bpm[keep], ac[1:][keep]
    raw = B[np.argmax(A)]
    pri = B[np.argmax(np.maximum(A, 0) * prior(B))]
    return float(raw), float(pri), (L, B, A)


def refine(o, bpm):
    """Sub-frame period: parabolic peak of the autocorrelation around the chosen lag."""
    ac = autocorr(o)
    lag = 60 * FPS / bpm
    i = int(round(lag))
    if 1 <= i < len(ac) - 1:
        a, b, c = ac[i - 1], ac[i], ac[i + 1]
        d = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) != 0 else 0
        lag = i + float(np.clip(d, -0.5, 0.5))
    return 60 * FPS / lag


def latency():
    """Where the onset curve puts a single click at 1.000 s, minus 1.000 s (the analysis window's
    lead: a centred 2048-sample window starts rising before the click reaches its centre)."""
    y = np.zeros(3 * SR, np.float32); y[SR] = 1.0
    o, _ = onset_curve(y)
    return float(np.argmax(o)) / FPS - 1.0


def track_beats(o, bpm, tightness=100.0):
    """Ellis 2007 dynamic programming: score(t) = onset(t) + best previous score penalised by how far
    the gap is from one period (squared log ratio)."""
    period = 60 * FPS / bpm
    on = o / (o.std() + 1e-9)
    n = len(on)
    score, back = on.copy(), -np.ones(n, int)
    lo, hi = int(round(period / 2)), int(round(period * 2))
    w = np.arange(lo, hi + 1)
    pen = -tightness * np.log(w / period) ** 2
    for t in range(hi, n):
        cand = score[t - w] + pen
        j = int(np.argmax(cand))
        score[t] += cand[j]
        back[t] = t - w[j]
    # end on the best-scoring frame in the last period
    t = int(np.argmax(score[n - hi:])) + n - hi
    beats = []
    while t >= 0:
        beats.append(t)
        t = back[t]
    return np.array(beats[::-1]) / FPS - LATENCY


def classify(est, true):
    for name, m in (("right", 1), ("double", 2), ("half", 0.5), ("triple", 3), ("third", 1 / 3)):
        if abs(est - true * m) <= 0.04 * true * m:
            return name
    return "wrong"


def true_beats(style, bpm, seconds, drift):
    """Beat times as the synth plays them (beats = quarter-note steps), integrating the drift."""
    S = grooves.STYLES[style]
    t, step, out = 0.0, 0, []
    while t < seconds:
        if step % S["spb"] == 0:
            out.append(t)
        t += 60.0 / (bpm * (drift(t) if drift else 1.0)) / S["spb"]
        step += 1
    return np.array(out)


def write_wav(path, y, sr=SR):
    import wave
    pcm = (np.clip(y, -1, 1) * 32767).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())


def example(style="rock", bpm=120, seed=2, show_s=4.0):
    """The worked example the scenes draw: the test set's own rock groove at 120 BPM (seed 2)."""
    y = grooves.render(style, bpm, seed=seed, seconds=30)
    o, D = onset_curve(y)
    raw, pri, _ = estimate(o)
    ac = autocorr(o)
    nf = int(round(show_s * FPS))
    seg = y[: int(show_s * SR)]
    blk = len(seg) // 480
    env = np.abs(seg[: blk * 480]).reshape(480, blk).max(1)
    tb = true_beats(style, bpm, show_s, None)
    lag_max = int(round(2.2 * FPS))
    lags_s = np.arange(lag_max + 1) / FPS
    beat_lag = 60 * FPS / bpm
    pk = lambda m: float(ac[int(round(beat_lag * m))])
    bpm_axis = 60 / np.maximum(lags_s, 1e-9)
    pr = np.where(lags_s > 0, prior(np.maximum(bpm_axis, 1e-3)), 0)
    on = o[:nf] / (o[:nf].max() + 1e-9)
    Dn = (D[:nf] - D[:nf].min()) / (D[:nf].max() - D[:nf].min() + 1e-9)
    write_wav(EV / "groove_rock_120.wav", seg / (np.abs(seg).max() + 1e-9) * 0.9)
    return dict(style=style, bpm=bpm, seed=seed, show_s=show_s, fps=FPS, sr=SR,
                env=[round(float(v), 3) for v in env / env.max()],
                beats=[round(float(b), 4) for b in tb],
                bands=[[round(float(v), 2) for v in row] for row in Dn.T],     # 40 x frames, 0..1
                onset=[round(float(v), 3) for v in on],
                ac_lags_s=[round(float(v), 4) for v in lags_s], ac=[round(float(v), 4) for v in ac[: lag_max + 1]],
                prior=[round(float(v), 4) for v in pr],
                ac_at={"half_beat": round(pk(0.5), 3), "beat": round(pk(1), 3), "two_beats": round(pk(2), 3),
                       "four_beats": round(pk(4), 3)},
                raw=round(refine(o, raw), 1), prior_pick=round(refine(o, pri), 1))


LATENCY = None


def main():
    global LATENCY
    LATENCY = latency()
    EV.mkdir(exist_ok=True)
    log = []
    P = lambda *a: (log.append(" ".join(str(x) for x in a)), print(*a))
    rows = []
    for si, (style, tempos) in enumerate(SET.items()):
        for ti, bpm in enumerate(tempos):
            y = grooves.render(style, bpm, seed=100 * si + ti, seconds=30)
            o, _ = onset_curve(y)
            raw, pri, _ = estimate(o)
            pri = refine(o, pri)
            raw = refine(o, raw)
            row = dict(style=style, bpm=bpm, raw=round(raw, 1), prior=round(pri, 1),
                       raw_class=classify(raw, bpm), prior_class=classify(pri, bpm))
            if LIBROSA:
                env = LIBROSA.onset.onset_strength(y=y, sr=SR)
                lt = float(LIBROSA.feature.tempo(onset_envelope=env, sr=SR)[0])
                row.update(librosa=round(lt, 1), librosa_class=classify(lt, bpm))
            rows.append(row)
    P(f"ONSET LATENCY (click test): the curve peaks {1000 * LATENCY:+.1f} ms from the click; beat times corrected by it")
    P(f"TEST SET: {len(rows)} grooves, 30 s each, 8 Western styles x 5 tempos (synthetic, grooves.py)")
    P("")
    P(f"{'style':14s} {'true':>5s} {'raw':>7s} {'':8s} {'prior':>7s} {'':8s} {'librosa':>7s}")
    for r in rows:
        lib = f"{r['librosa']:7.1f} {r['librosa_class']}" if LIBROSA else "(librosa not installed)"
        P(f"{NAMES[r['style']]:14s} {r['bpm']:5d} {r['raw']:7.1f} {r['raw_class']:8s} {r['prior']:7.1f} "
          f"{r['prior_class']:8s} {lib}")
    P("")
    summary = {}
    for k in ("raw", "prior") + (("librosa",) if LIBROSA else ()):
        c = {}
        for r in rows:
            c[r[k + "_class"]] = c.get(r[k + "_class"], 0) + 1
        acc2 = sum(v for n, v in c.items() if n != "wrong")
        summary[k] = dict(counts=c, acc1=c.get("right", 0), acc2=acc2, n=len(rows))
        P(f"{k:6s}: right {c.get('right', 0)}/{len(rows)}  (Accuracy 1)   right-or-octave {acc2}/{len(rows)}  "
          f"(Accuracy 2)   counts {c}")
    if LIBROSA:
        same = sum(r["prior_class"] == r["librosa_class"] for r in rows)
        close = sum(abs(r["prior"] - r["librosa"]) <= 0.04 * r["librosa"] for r in rows)
        summary["agreement"] = dict(same_class=same, within_4pct=close, n=len(rows), version=LIBROSA.__version__)
        P(f"librosa {LIBROSA.__version__} cross-check: same verdict on {same}/{len(rows)}, "
          f"same tempo within 4% on {close}/{len(rows)}")
    per_style = {s: {k: [r[k + '_class'] for r in rows if r['style'] == s] for k in ('raw', 'prior')} for s in SET}
    P("")
    for s, v in per_style.items():
        P(f"  {NAMES[s]:14s} raw {v['raw']}  prior {v['prior']}")

    # Live-drummer drift: rock at 120, speeding up 4% over 30 s with a slow wobble.
    drift = lambda t: 1.0 + 0.04 * (t / 30.0) + 0.012 * np.sin(2 * np.pi * t / 11.0)
    y = grooves.render("rock", 120, seed=777, seconds=30, drift=drift, loose_ms=8)
    o, _ = onset_curve(y)
    _, pri, _ = estimate(o)
    pri = refine(o, pri)
    tb = true_beats("rock", 120, 30, drift)
    trk = track_beats(o, pri)
    # fixed grid: the single BPM, phase-aligned to the first true beat
    grid = tb[0] + np.arange(len(tb)) * 60.0 / pri
    near = lambda b, ref: np.array([ref[np.argmin(np.abs(ref - x))] - x for x in b])
    grid_err = np.abs(grid - tb)                        # ms the fixed grid is off each true beat
    trk_err = np.abs(near(tb, trk))                     # each true beat vs the nearest tracked beat
    t_off = next((float(tb[i]) for i, e in enumerate(grid_err) if e > 0.05), None)
    drift_res = dict(true_start=120, true_end=round(120 * drift(30.0), 1), est=round(pri, 1),
                     grid_max_ms=round(1000 * grid_err.max(), 0), grid_end_ms=round(1000 * grid_err[-1], 0),
                     grid_off50_at_s=round(t_off, 1) if t_off else None,
                     track_median_ms=round(1000 * np.median(trk_err), 0),
                     track_p95_ms=round(1000 * np.percentile(trk_err, 95), 0),
                     n_beats=len(tb), n_tracked=len(trk))
    P("")
    P(f"DRIFT (rock, starts at 120 BPM, ends at {drift_res['true_end']} BPM, ±1.2% wobble, 8 ms looseness):")
    P(f"  one number: {drift_res['est']} BPM")
    P(f"  fixed grid at that BPM: off by up to {drift_res['grid_max_ms']:.0f} ms, {drift_res['grid_end_ms']:.0f} ms "
      f"at the end; first more than 50 ms off at {drift_res['grid_off50_at_s']} s")
    P(f"  beat tracker: median {drift_res['track_median_ms']:.0f} ms from the true beat, 95% within "
      f"{drift_res['track_p95_ms']:.0f} ms ({drift_res['n_tracked']} beats placed for {drift_res['n_beats']})")
    drift_series = dict(true=[round(float(v), 4) for v in tb], grid=[round(float(v), 4) for v in grid],
                        tracked=[round(float(v), 4) for v in trk],
                        grid_err_ms=[round(float(v) * 1000, 1) for v in grid - tb],
                        track_err_ms=[round(float(v) * 1000, 1) for v in -near(tb, trk)])
    write_wav(EV / "groove_rock_drift.wav", y)

    ex = example()
    P("")
    P(f"EXAMPLE (rock, 120 BPM, seed 2): match at half a beat {ex['ac_at']['half_beat']}, one beat "
      f"{ex['ac_at']['beat']}, two beats {ex['ac_at']['two_beats']}, four beats {ex['ac_at']['four_beats']}; "
      f"strongest repeat -> {ex['raw']} BPM, with the 120 preference -> {ex['prior_pick']} BPM")
    (EV / "scene.json").write_text(json.dumps(dict(example=ex, drift=dict(**drift_res, **drift_series)),
                                              separators=(",", ":")), encoding="utf-8")
    (EV / "run.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(dict(rows=rows, summary=summary, drift=drift_res), indent=1),
                                     encoding="utf-8")


if __name__ == "__main__":
    main()
