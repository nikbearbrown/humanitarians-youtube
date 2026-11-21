"""craters.py -- the physics and the toy field for Ep. 18, *counting-craters*.

Nothing in here draws. `gen_craters.py` imports this, re-derives every number
the narration says, asserts it, and only then writes the plates.

Two kinds of thing live here and they must never be confused:

  REAL      the Neukum chronology function and everything derived from it.
            These are published constants; the numbers that come out are the
            numbers the episode says out loud.

  TOY       the synthetic crater field and the synthetic analysts. These exist
            so the viewer can SEE "denser = older" and "analysts disagree".
            Their only honest claim is the one the code asserts: the two
            patches differ in crater count by exactly the ratio the REAL
            chronology function gives. Crater SIZES are drawn from a power law
            purely so the patch looks like terrain -- that exponent is a
            drawing choice, not a measurement, and FACTCHECK says so.
"""
import math
import random

# ─────────────────────────────────────────────────────────────────────────────
#  REAL -- the lunar chronology function
#
#  Neukum (1983); restated in Neukum, Ivanov & Hartmann (2001) and in the form
#  below in Neukum et al., LPSC XXXIII (2002), abstract 1263:
#
#      N(1) = 5.44e-14 (exp(6.93 T) - 1) + 8.38e-4 T
#
#  N(1) is the CUMULATIVE number of craters with D > 1 km per km^2 that a
#  surface has accumulated in time T, with T measured in Ga BEFORE PRESENT.
#  The exponential term is the early heavy bombardment; the linear term is the
#  roughly constant rate since. The whole episode lives in the fact that these
#  two terms hand over somewhere around 3.5 Ga.
# ─────────────────────────────────────────────────────────────────────────────
CF_A = 5.44e-14
CF_B = 6.93
CF_C = 8.38e-4

T_MAX = 4.5          # no surface is older than the Moon


def N1(T):
    """Cumulative craters D > 1 km per km^2 accumulated in time T (Ga)."""
    return CF_A * (math.exp(CF_B * T) - 1.0) + CF_C * T


def T_of_N1(N):
    """Invert the chronology function: the age (Ga) that produces density N.

    Bisection, not a solver -- N1 is strictly increasing on [0, T_MAX], so 200
    halvings puts the answer well past any precision the episode quotes.
    """
    if N <= 0.0:
        return 0.0
    lo, hi = 0.0, T_MAX
    if N >= N1(T_MAX):
        return T_MAX
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if N1(mid) < N:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def age_window(T, rel_err):
    """The ages you would report if your crater COUNT were off by +-rel_err.

    This is the episode's central operation. A counting error is an error in
    density; the chronology function turns it into an error in age -- and
    because that function is wildly non-linear, the SAME counting error is
    worth completely different amounts of time depending on where you are.
    """
    n = N1(T)
    return T_of_N1((1.0 - rel_err) * n), T_of_N1((1.0 + rel_err) * n)


def early_share(T_old, T_split):
    """Fraction of a T_old surface's craters that landed before T_split."""
    return 1.0 - N1(T_split) / N1(T_old)


# ─────────────────────────────────────────────────────────────────────────────
#  TOY -- a synthetic patch of ground, so "denser = older" is visible
# ─────────────────────────────────────────────────────────────────────────────
#  Cumulative size-frequency exponent for the drawn craters. A DRAWING CHOICE
#  in the neighbourhood of the small-crater branch of the production function.
#  It sets how many little craters there are per big one -- i.e. what the patch
#  LOOKS like -- and no number the episode speaks depends on it.
SFD_SLOPE = 1.8
D_MIN, D_MAX = 0.016, 0.115      # crater diameter as a fraction of patch width


def _draw_diameter(rng):
    """One crater diameter from a truncated power law (cumulative slope SFD_SLOPE)."""
    u = rng.random()
    a = 1.0 - SFD_SLOPE
    lo, hi = D_MIN ** a, D_MAX ** a
    return (lo + u * (hi - lo)) ** (1.0 / a)


def synth_patch(n, seed, pad=0.0, tries=400):
    """n craters scattered on the unit square, avoiding heavy overlap.

    Rejection sampling, not a physical model: a real surface saturates and
    overprints, and this one simply declines to put two circles on top of each
    other so the viewer can count what they see. Returns [(x, y, d), ...]
    sorted large-first so the big ones draw underneath.
    """
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        for _try in range(tries):
            d = _draw_diameter(rng)
            r = 0.5 * d
            x = rng.uniform(r + pad, 1.0 - r - pad)
            y = rng.uniform(r + pad, 1.0 - r - pad)
            ok = True
            for (ox, oy, od) in out:
                if math.hypot(x - ox, y - oy) < 0.52 * (d + od):
                    ok = False
                    break
            if ok:
                out.append((x, y, d))
                break
    out.sort(key=lambda c: -c[2])
    return out


def patch_counts(T_young, T_old, n_young):
    """Crater counts for the two patches, in the TRUE chronology ratio.

    The young patch gets n_young craters; the old patch gets however many the
    real chronology function says, for the same area. This is the one claim
    the toy field makes, and gen_craters.py asserts it.
    """
    ratio = N1(T_old) / N1(T_young)
    return n_young, int(round(n_young * ratio))


# ─────────────────────────────────────────────────────────────────────────────
#  TOY -- synthetic analysts, so "they disagree" is visible
# ─────────────────────────────────────────────────────────────────────────────
#  Each analyst sees a crater with a probability that FALLS with decreasing
#  size: the big ones are unanimous, the small ones are argued over. That is
#  the shape Robbins et al. (2014) report -- disagreement concentrated at
#  small diameters -- but the plate asserts nothing numerical about it. The
#  +-45% the episode says out loud is CITED from that paper and placed on
#  screen by scenes.py, never read off this simulation.
def analyst_votes(field, n_analysts, seed, d_half=0.038, sharp=5.0):
    """How many of n_analysts marked each crater. Returns [votes, ...].

    d_half is the diameter at which an analyst is 50/50; sharp sets how fast
    the probability swings from "everyone sees it" to "nobody does".
    """
    rng = random.Random(seed)
    votes = []
    for (_x, _y, d) in field:
        p = 1.0 / (1.0 + math.exp(-sharp * (d - d_half) / d_half))
        votes.append(sum(1 for _ in range(n_analysts) if rng.random() < p))
    return votes
