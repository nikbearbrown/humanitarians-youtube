"""The search, the interference, and the two tests, for Ep. 13.

The detector here is not a stand-in. `dedoppler` is the actual statistic a
radio technosignature search computes: sum the dynamic spectrum along a
straight track in time-frequency, once per trial drift rate, and keep the
best signal-to-noise. That is what turboSETI and its relatives do.

Using the real algorithm matters, because it puts the episode's subject --
the assumption -- in plain sight as a single number. The search is given a
RANGE of drift rates to try. Anything outside that range is not merely hard
to find; it is not looked for. The range is the hypothesis.

Nothing here is a model of any telescope. The parameters are chosen to be
illustrative of the mechanism; only the direction and rough size of the
effect are claimed, and the reel says so.
"""
import numpy as np

# 32 rows, not 16. De-Doppler only separates a drifting signal from a
# stationary one when the signal moves MANY linewidths across the
# integration. At 16 rows and 0.15-0.60 Hz/s the total drift was 2-10
# channels against a 1-2 channel linewidth, so a zero-drift interference
# line stayed partly coherent at non-zero trial rates and produced just as
# many look-alikes as a real drifting candidate. That is a true statement
# about an under-resolved toy, not about the search. Real surveys integrate
# for minutes and sweep several Hz/s, where drift x time is thousands of
# channels; 32 rows at 0.6-2.0 Hz/s puts this in the same regime.
NT, NF = 32, 512          # time samples, frequency channels
DF = 1.0                  # Hz per channel
DT = 1.0                  # seconds per row


def blank(rng, noise=1.0):
    """An empty dynamic spectrum: time down, frequency across."""
    return rng.normal(0.0, noise, size=(NT, NF))


def add_track(wf, f0, drift, snr, width=1.4, duty=None, rng=None):
    """Put a narrowband signal in, drifting at `drift` Hz/s.

    `duty` None is a continuous carrier; a float in (0,1] makes it pulsed,
    present in that fraction of the time rows. Both are things a transmitter
    can do, and only the first is what searches assume.
    """
    on = np.ones(NT, bool)
    if duty is not None:
        on = rng.random(NT) < duty
    for t in range(NT):
        if not on[t]:
            continue
        fc = f0 + drift * t * DT / DF
        lo, hi = int(fc - 3 * width), int(fc + 3 * width) + 1
        for f in range(max(lo, 0), min(hi, NF)):
            wf[t, f] += snr * np.exp(-0.5 * ((f - fc) / width) ** 2)
    return wf


def add_rfi(wf, rng, n_lines=4, n_blips=10):
    """Terrestrial interference.

    The important property is not that there is a lot of it: it is that it
    sits at ZERO drift. A transmitter bolted to the same rotating planet as
    the telescope has no relative acceleration, so its signal is a straight
    vertical line in the dynamic spectrum. That single fact is what makes
    zero drift uninhabitable for a search, and it is why real pipelines
    exclude it.
    """
    for _ in range(n_lines):
        f0 = rng.uniform(20, NF - 20)
        snr = rng.uniform(2.5, 7.0)
        duty = rng.uniform(0.5, 1.0)
        add_track(wf, f0, 0.0, snr, width=rng.uniform(1.0, 2.2),
                  duty=duty, rng=rng)
    for _ in range(n_blips):
        t = rng.integers(0, NT)
        f0 = int(rng.uniform(10, NF - 10))
        w = int(rng.integers(3, 14))
        wf[t, max(f0 - w, 0):f0 + w] += rng.uniform(2.0, 5.0)
    return wf


# ── the real detection statistic ────────────────────────────────────────────
def dedoppler_map(wf, drift_lo, drift_hi, n_trials=49):
    """Signal-to-noise for every (trial drift rate, frequency) pair.

    For each trial rate the spectrum is summed along the matching straight
    track; a signal drifting at that rate adds coherently and noise does not.
    `drift_lo`..`drift_hi` IS the hypothesis: a signal outside it is not
    searched for.

    A first version took a single maximum over the whole field and asked
    whether it exceeded a threshold. That is not what a search does, and it
    could not work: the interference is brighter than the signal, so the
    maximum was always an interference line and the injected signal never
    moved it. A pipeline returns a HIT LIST, and the question is whether the
    real signal is on it.
    """
    drifts = np.linspace(drift_lo, drift_hi, n_trials)
    sd = _robust_sigma(wf)
    out = np.empty((n_trials, NF))
    for i, d in enumerate(drifts):
        acc = np.zeros(NF)
        for t in range(NT):
            acc += np.roll(wf[t], -int(round(d * t * DT / DF)))
        out[i] = acc / (sd * np.sqrt(NT))
    return drifts, out


def _robust_sigma(wf):
    """Noise scale that the interference cannot inflate.

    Using wf.std() lets a handful of bright interference lines raise the
    denominator and hide everything else. The median absolute deviation
    measures the background instead.
    """
    med = np.median(wf)
    mad = np.median(np.abs(wf - med))
    return float(mad / 0.6745) or 1.0


def detected(wf, f0, drift, drift_lo, drift_hi, thresh, tol_f=3.0,
             tol_d=0.06):
    """Is the injected signal ON the hit list?

    True when some trial track within `tol_d` of the real drift rate and
    `tol_f` channels of the real frequency exceeds `thresh`. If the real
    drift lies outside the searched range this is False by construction --
    which is the point.
    """
    drifts, m = dedoppler_map(wf, drift_lo, drift_hi)
    near = np.abs(drifts - drift) <= tol_d
    if not near.any():
        return False
    lo, hi = int(f0 - tol_f), int(f0 + tol_f) + 1
    return bool(m[near, max(lo, 0):min(hi, NF)].max() > thresh)


def hit_count(wf, drift_lo, drift_hi, thresh, min_sep=8):
    """How many distinct things the search hands a human to look at."""
    _, m = dedoppler_map(wf, drift_lo, drift_hi)
    best = m.max(axis=0)
    hits, last = 0, -10 ** 9
    order = np.argsort(-best)
    taken = []
    for f in order:
        if best[f] <= thresh:
            break
        if all(abs(f - g) >= min_sep for g in taken):
            taken.append(int(f))
            hits += 1
    return hits


def lookalikes(wf, drift, drift_lo, drift_hi, thresh, tol_d=0.06,
               min_sep=8):
    """How many OTHER things in this field share the candidate's drift rate.

    This is the real cost of searching a drift rate, and it is the argument
    that actually killed BLC1: not that the candidate looked wrong, but that
    dozens of interference signals looked the same. At zero drift -- where a
    transmitter that corrects its own Doppler would sit -- every local
    transmitter is a look-alike, because a transmitter on the ground has no
    relative acceleration either.
    """
    drifts, m = dedoppler_map(wf, drift_lo, drift_hi)
    near = np.abs(drifts - drift) <= tol_d
    if not near.any():
        return 0
    best = m[near].max(axis=0)
    taken = []
    for f in np.argsort(-best):
        if best[f] <= thresh:
            break
        if all(abs(f - g) >= min_sep for g in taken):
            taken.append(int(f))
    return len(taken)


def cadence_detected(on_scans, off_scans, f0, drift, drift_lo, drift_hi,
                     margin):
    """The other test: does the signal follow the telescope?

    Observe the target, look away, come back, look away. A source on the sky
    appears when pointed at and vanishes when not. Interference does not care
    where the dish points, so it shows up in both.

    This asks WHERE A SIGNAL COMES FROM, not what it looks like -- which is
    why its answer does not depend on the morphology hypothesis.
    """
    def peak(w):
        drifts, m = dedoppler_map(w, drift_lo, drift_hi)
        near = np.abs(drifts - drift) <= 0.06
        if not near.any():
            return -np.inf
        lo, hi = int(f0 - 3), int(f0 + 3) + 1
        return float(m[near, max(lo, 0):min(hi, NF)].max())

    on = min(peak(w) for w in on_scans)
    off = max(peak(w) for w in off_scans)
    return (on - off) > margin
