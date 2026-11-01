"""conj.py — conjunction assessment: the probability, and what it is a probability OF.

Ep. 15, *satellite-collision-avoidance*. Nothing here is a model of any real
catalogue or any real operator's process. It is the STANDARD short-encounter
collision-probability calculation, run honestly, so that one property of it
can be measured: it is not monotonic in your own uncertainty.

────────────────────────────────────────────────────────────────────────────
THE CALCULATION

For a short encounter the two objects' relative motion is projected into the
plane perpendicular to the relative velocity (the "encounter plane"). In that
plane the combined position error is Gaussian, and the collision probability
is the Gaussian mass lying inside a disk of radius R (the combined hard-body
radius) centred on the predicted miss distance d:

    Pc = ∫∫_{|x - d| < R}  N(0, σ²I) dx

With a circular covariance this reduces to a one-dimensional integral,

    Pc = ∫₀^R (r/σ²) exp(-(r² + d²)/(2σ²)) I₀(r d / σ²) dr

which is evaluated here in its numerically stable form. Writing I₀(x) =
i₀ₑ(x)·e^{|x|} and folding the exponentials together gives

    Pc = ∫₀^R (r/σ²) exp(-(r - d)²/(2σ²)) · i₀ₑ(r d / σ²) dr

so nothing is ever exponentiated to a large positive argument. The naive form
overflows for d/σ ≳ 30, which is precisely the well-tracked regime the
episode cares about.

────────────────────────────────────────────────────────────────────────────
THE PROPERTY

Pc → 0 in BOTH limits:

  σ → 0   you know exactly where both objects are, and (if d > R) they miss.
  σ → ∞   the probability mass is spread over an enormous area, so almost
          none of it lands inside a disk a few tens of metres across.

So Pc has an interior maximum. The consequence is the one the conjunction
literature calls PROBABILITY DILUTION: past the peak, **degrading your own
tracking lowers the computed collision probability**. A threshold decision
taken on Pc can therefore be switched off by knowing less.

This is not a bug in the integral — the integral is correct. It is a property
of what Pc actually is: not the probability that two objects will collide,
but the probability that they collide GIVEN a particular uncertainty model.

────────────────────────────────────────────────────────────────────────────
WHAT IS SIMULATED, AND WHAT IS NOT

`make_events` builds a population of conjunctions whose covariance shrinks as
the time of closest approach approaches, which is what really happens as more
tracking data arrives. The miss distance is also re-estimated each time.

The numbers that come out are ILLUSTRATIVE. The orbital dynamics are not
modelled at all — there is no propagator here, and no real catalogue. What is
real is the Pc integral and the shape of its dependence on σ, and those are
the only things the reel claims.
"""
import numpy as np
from scipy.special import i0e

# Combined hard-body radius, metres. Two spacecraft of a few metres each plus
# margin; operators typically use 5-50 m. The episode's effect does not depend
# on this value, only on the ratio R/d.
HBR = 20.0

# The operational notification threshold the reel draws. 1e-4 is the value
# most often quoted for "consider a manoeuvre"; ESA's own challenge used 1e-6
# to collect more high-risk events. Both appear in the plates.
P_ACT = 1e-4

# The screening box, metres. Conjunctions are only assessed at all if the
# predicted miss distance falls inside it; see make_events for why the miss
# distance is drawn uniform in area rather than uniform in distance.
D_BOX = 8000.0

# Risks are reported, and scored, on a FLOOR. ESA's own challenge used a
# notification threshold of 1e-6 and its naive baseline predicts "the latest
# risk, or -6.001 if that is below -6" -- i.e. everything quieter than 1e-6 is
# one undifferentiated 'no risk' class. Without a floor the comparison is
# meaningless: a conjunction at 1e-25 and one at 1e-12 are both 'will not
# happen', but their log difference is 13, and squared error would be driven
# entirely by that irrelevant gap.
RISK_FLOOR = -6.0

_GL_N = 2048          # nodes for the radial quadrature


def pc(sigma, d, R=HBR, n=_GL_N):
    """Collision probability for a circular encounter-plane covariance.

    sigma, d may be arrays; they broadcast against each other.
    """
    sigma = np.asarray(sigma, dtype=float)
    d = np.asarray(d, dtype=float)
    sh = np.broadcast(sigma, d).shape
    sigma = np.broadcast_to(sigma, sh)
    d = np.broadcast_to(d, sh)

    # midpoint rule on r in [0, R]; the integrand is smooth and bounded
    r = (np.arange(n) + 0.5) * (R / n)
    r = r.reshape((n,) + (1,) * len(sh))
    s = sigma[None, ...]
    dd = d[None, ...]

    x = r * dd / s ** 2
    integrand = (r / s ** 2) * np.exp(-((r - dd) ** 2) / (2 * s ** 2)) * i0e(x)
    out = integrand.sum(axis=0) * (R / n)
    return np.clip(out, 0.0, 1.0)


def pc_max(d, R=HBR):
    """The LARGEST Pc attainable at this geometry over all covariance scales.

    This is the 'maximum probability' construction: rather than trusting the
    covariance you happen to have, ask how bad the encounter could look under
    the worst-case scale. It depends only on d and R, so — unlike Pc — it
    CANNOT be lowered by tracking the object less well. That is the whole
    point of it, not an incidental property.
    """
    d = np.atleast_1d(np.asarray(d, dtype=float))
    out = np.empty_like(d)
    for i, dv in enumerate(d):
        # the peak sits near d/sqrt(2) for R << d; bracket generously
        grid = np.geomspace(max(dv, R) * 1e-3, max(dv, R) * 1e2, 600)
        out[i] = pc(grid, dv, R).max()
    return out


def peak_sigma(d, R=HBR, lo=1e-3, hi=1e2, n=4000):
    """The covariance scale at which Pc is largest, by direct search."""
    grid = np.geomspace(max(d, R) * lo, max(d, R) * hi, n)
    v = pc(grid, d, R)
    return float(grid[int(np.argmax(v))]), float(v.max())


def sigma_at_threshold(d, R=HBR, thresh=P_ACT, branch="upper"):
    """The sigma at which Pc crosses `thresh`.

    'upper' is the dilution side — the branch on which MORE uncertainty means
    LESS computed risk, and therefore the branch a decision can be walked
    across by degrading tracking.
    """
    s_peak, p_peak = peak_sigma(d, R)
    if p_peak < thresh:
        return None
    if branch == "upper":
        grid = np.geomspace(s_peak, s_peak * 1e4, 20000)
    else:
        grid = np.geomspace(s_peak * 1e-4, s_peak, 20000)
    v = pc(grid, d, R)
    cross = np.where(np.diff(np.sign(v - thresh)))[0]
    if not len(cross):
        return None
    return float(grid[cross[0]])


# ═════════════════════════════════════════════════════════════════════════════
#  A population of conjunctions, each observed repeatedly before TCA
# ═════════════════════════════════════════════════════════════════════════════
# Times to closest approach at which a conjunction data message is issued.
# Real screening produces roughly a dozen per event over the last week; this
# uses seven, which is enough to carry a trend without pretending to realism.
T_GRID = np.array([-7.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0])

# The CUTOFF: the reel's forecasting task is "from everything known at -2
# days, predict the risk at closest approach".
T_CUT = -2.0


def make_events(rng, n=6000):
    """Build conjunctions whose covariance shrinks as TCA approaches.

    Returns dict of arrays shaped (n, len(T_GRID)):
      sig   the encounter-plane covariance scale at each CDM, metres
      dist  the miss distance as currently estimated, metres
      risk  log10 Pc at each CDM

    The population is deliberately dominated by comfortable misses, with a
    thin tail of close ones — which is what makes the high-risk class rare,
    exactly as it is in the real screening problem.
    """
    # True miss distance. NOT log-uniform: conjunctions are screened inside a
    # box, and for encounters arriving from random directions the number with
    # miss distance below d grows like d^2 -- the area of the disk. So d is
    # drawn uniform in AREA, d = D_BOX * sqrt(U). That is what makes a close
    # approach genuinely rare rather than rare by fiat, and it is why the
    # high-risk class here comes out at a fraction of a percent, the order
    # ESA's own challenge reports (30 events above 1e-4 out of 15,321).
    d_true = D_BOX * np.sqrt(rng.uniform(0.0, 1.0, n))

    # The covariance the solution converges to by closest approach, and how
    # much it shrank to get there. More tracking passes -> tighter solution;
    # the spread in how much it tightens is what makes the final risk hard to
    # call early.
    sig_final = np.exp(rng.uniform(np.log(25.0), np.log(200.0), n))
    total_shrink = np.exp(rng.uniform(np.log(20.0), np.log(300.0), n))
    sig0 = sig_final * total_shrink

    frac = (T_GRID - T_GRID[0]) / (T_GRID[-1] - T_GRID[0])      # 0 -> 1
    sig = sig0[:, None] * total_shrink[:, None] ** (-frac[None, :])

    # The estimated miss distance wanders toward the truth as sigma shrinks:
    # early estimates are off by a fraction of the current covariance.
    wobble = rng.normal(0.0, 1.0, (n, len(T_GRID)))
    dist = np.abs(d_true[:, None] + 0.20 * sig * wobble)
    dist = np.maximum(dist, 1.0)

    # Chunked: the quadrature is (nodes x events x messages) and a population
    # large enough to carry a high-risk tail will not fit in one array.
    risk = np.empty_like(sig)
    step = 4000
    for a in range(0, n, step):
        b = min(a + step, n)
        risk[a:b] = np.log10(np.maximum(pc(sig[a:b], dist[a:b], n=256), 1e-300))
    risk = np.maximum(risk, RISK_FLOOR)
    return dict(sig=sig, dist=dist, risk=risk, d_true=d_true)


def features(ev, t_index):
    """Features available at the cutoff CDM, for forecasting the final risk.

    `plain` is what a persistence-style model can see: the latest risk and its
    recent trend. `geom` adds ONE thing — where this conjunction currently
    sits on the dilution curve, log10(sigma/d). That ratio is what decides
    whether the risk is about to climb as the covariance keeps shrinking.
    """
    i = t_index
    r_last = ev["risk"][:, i]
    r_prev = ev["risk"][:, i - 1]
    s = ev["sig"][:, i]
    d = ev["dist"][:, i]
    plain = np.column_stack([r_last, r_last - r_prev, np.log10(s)])
    geom = np.column_stack([plain, np.log10(s / d), np.log10(d)])
    return plain, geom, r_last


def ridge_fit(X, y, lam=1e-3):
    X1 = np.column_stack([X, np.ones(len(X))])
    A = X1.T @ X1 + lam * np.eye(X1.shape[1])
    return np.linalg.solve(A, X1.T @ y)


def ridge_pred(w, X):
    return np.column_stack([X, np.ones(len(X))]) @ w
