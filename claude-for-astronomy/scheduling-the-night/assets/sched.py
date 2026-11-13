"""sched.py — a night of telescope scheduling, built from scratch.

Ep. 17 · `scheduling-the-night`. Everything here is computed locally with
numpy + scipy (HiGHS). No Gurobi, no paid solver, no API.

WHAT THIS IS AND IS NOT
-----------------------
This is a STATED-PARAMETER TOY of a wide-field survey telescope at a southern
site. It is not a model of Rubin, and not a model of ZTF. The published
numbers from those two facilities live in SOURCES.md and are labelled
PUBLISHED wherever they appear; everything this file produces is labelled
COMPUTED. The two are never blended in one sentence.

What the toy is FOR is the structural question, which is instrument
independent: a night is a sequence of a few hundred to a few thousand
pointings, the number of orderings is astronomically large, and there are
exactly two ways anyone actually copes --

  GREEDY   shrink the decision to "what is best RIGHT NOW", and re-decide
           every exposure. No lookahead. (Rubin's Feature Based Scheduler.)
  BLOCKS   shrink the decision to "which half-hour bucket", solve the whole
           night exactly, then order within each bucket. (ZTF's ILP.)

Neither one searches the orderings. Both win by changing what a move IS.

THE GEOMETRY OF THE CLAIM
-------------------------
The decisive measurement is NOT exposures per hour -- the two schedulers are
near-identical on throughput, which is exactly why throughput is the wrong
metric. It is the SEQUENCE COMPLETION FRACTION: the fraction of fields for
which the scheduler got ALL of the visits it set out to get. A lone image of
a field measures nothing; a transient survey needs the pair. Half a pair is
not half a detection, it is zero detections.

And the mechanism behind the gap is not that the planner "tries harder".
It is that in the ILP, completion is a CONSTRAINT, not a reward: a request
set is scheduled with exactly its requested number of visits, or it is not
scheduled at all (Bellm et al. 2019, Eq. 4). The planner REFUSES TO START a
sequence it cannot finish. Greedy has no such concept -- it starts
everything that looks good now, and finishes whatever it happens to get back
to before the field sets.

UNITS. Angles in degrees at the interface, radians internally. Times in
seconds unless a name ends in `_min` or `_h`.
"""
import math

import numpy as np

# ── Site and night ───────────────────────────────────────────────────────────
LAT_DEG = -30.0          # a southern site; STATED, not a specific observatory
NIGHT_H = 8.0            # dark time between twilights
ALT_MIN_DEG = 20.0       # horizon cut: below this the airmass is punishing

# ── Camera and mount (STATED PARAMETERS for an 8 m-class survey telescope) ──
T_EXP = 30.0             # one visit, seconds on sky
T_READ = 2.0             # readout, overlapped where possible but charged here
T_SETTLE = 1.0           # post-slew settle
T_FILTER = 120.0         # band change -- the expensive move
V_ALT, A_ALT = 3.5, 3.5  # deg/s, deg/s^2
V_AZ, A_AZ = 7.0, 7.0    # the azimuth axis is the fast one

# ── Bands. Two is enough to make filter changes cost something ───────────────
BANDS = ("g", "r")
# m5 scaling constants, STATED. The functional form is the standard survey
# depth relation (Ivezic et al. 2019); these coefficients are plausible values
# for a generic 8 m survey telescope and are NEVER quoted on screen -- only
# the scheduling results computed from them are.
CM = {"g": 24.42, "r": 24.44}
KM = {"g": 0.21, "r": 0.10}
MSKY_DARK = {"g": 22.26, "r": 21.20}
SEEING_ZENITH = 0.70     # arcsec, at zenith, in the fiducial band

# ── The night's decision grid ────────────────────────────────────────────────
BLOCK_MIN = 30.0         # ZTF's choice: the MINIMUM DESIRED SEPARATION between
                         # two visits of one field. The block length and the
                         # cadence requirement are the same number on purpose.
N_BLOCK = int(round(NIGHT_H * 60.0 / BLOCK_MIN))   # 16

VISITS_PER_SET = 2       # a "pair": two visits of one field, same band,
                         # in two DIFFERENT blocks -> >= 30 min apart


# ═════════════════════════════════════════════════════════════════════════════
#  Sky geometry
# ═════════════════════════════════════════════════════════════════════════════
def fibonacci_sphere(n):
    """n roughly-uniform points on the sphere -> (ra_deg, dec_deg).

    A tessellation, not a random draw: survey telescopes observe a FIXED grid
    of fields, and which fields exist is not something the scheduler chooses.
    """
    i = np.arange(n, dtype=float) + 0.5
    phi = np.arccos(1.0 - 2.0 * i / n)              # polar angle, 0..pi
    golden = math.pi * (1.0 + 5.0 ** 0.5)
    theta = golden * i
    dec = 90.0 - np.degrees(phi)
    ra = np.degrees(theta) % 360.0
    return ra, dec


def altaz(ra_deg, dec_deg, lst_deg, lat_deg=LAT_DEG):
    """Altitude and azimuth, in degrees, for a local sidereal time."""
    ha = np.radians((lst_deg - ra_deg + 180.0) % 360.0 - 180.0)
    dec = np.radians(dec_deg)
    lat = math.radians(lat_deg)
    sin_alt = np.sin(lat) * np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(ha)
    sin_alt = np.clip(sin_alt, -1.0, 1.0)
    alt = np.arcsin(sin_alt)
    cos_az = (np.sin(dec) - np.sin(alt) * np.sin(lat)) / (
        np.cos(alt) * np.cos(lat) + 1e-12)
    az = np.arccos(np.clip(cos_az, -1.0, 1.0))
    az = np.where(np.sin(ha) > 0, 2.0 * np.pi - az, az)
    return np.degrees(alt), np.degrees(az)


def airmass(alt_deg):
    """Kasten & Young (1989). Diverges gracefully near the horizon.

    The plain secant blows up below ~15 deg; this form is the standard fix and
    matters here because the horizon cut is at 20 deg.
    """
    alt = np.asarray(alt_deg, dtype=float)
    z = 90.0 - alt
    denom = np.cos(np.radians(z)) + 0.50572 * np.power(
        np.maximum(96.07995 - z, 1e-6), -1.6364)
    return np.where(alt > 0, 1.0 / np.maximum(denom, 1e-6), np.inf)


# ═════════════════════════════════════════════════════════════════════════════
#  Depth, and the survey-speed metric
# ═════════════════════════════════════════════════════════════════════════════
def m5_depth(band, X, msky=None, t_vis=T_EXP):
    """5-sigma point-source limiting magnitude.

    m5 = Cm + 0.50 (msky - 21) + 2.5 log10(0.7 / seeing_eff)
         + 1.25 log10(t / 30) - km (X - 1)

    Seeing degrades with airmass as X^0.6, so airmass is charged TWICE: once
    through extinction (the km term) and once through the seeing disc. That
    double charge is why every scheduler on earth wants to observe near zenith,
    and it is why `SlewBasisFunction` alone would not be enough.
    """
    X = np.asarray(X, dtype=float)
    if msky is None:
        msky = MSKY_DARK[band]
    seeing_eff = SEEING_ZENITH * np.power(X, 0.6)
    return (CM[band]
            + 0.50 * (np.asarray(msky, dtype=float) - 21.0)
            + 2.5 * np.log10(SEEING_ZENITH / seeing_eff)
            + 1.25 * np.log10(t_vis / 30.0)
            - KM[band] * (X - 1.0))


def survey_speed(m5, t_total):
    """Volumetric survey speed, V ~ 10^(0.6 m5) / (t_exp + t_OH).

    The form is Bellm et al. (2019) Eq. 2: the volume a single exposure probes,
    normalised by the time it costs. 0.6 = 3/5, because a 1 mag gain in depth
    buys 10^(3/5) in volume -- distance goes as 10^(m/5), volume as the cube.

    This is the honest objective for a TRANSIENT survey. A survey that cares
    about coadded depth instead wants a different exponent, and the episode
    says so: the metric is a choice, not a law.
    """
    return np.power(10.0, 0.6 * np.asarray(m5, dtype=float)) / np.maximum(
        t_total, 1e-6)


# ═════════════════════════════════════════════════════════════════════════════
#  The mount: what it costs to look somewhere else
# ═════════════════════════════════════════════════════════════════════════════
def _axis_time(theta_deg, vmax, amax):
    """Time to move one axis through theta with trapezoidal kinematics.

    Short moves never reach vmax (pure accelerate-decelerate, t = 2 sqrt(th/a));
    long ones cruise. The crossover is at theta = vmax^2 / amax. Getting this
    boundary right matters: a survey's slews are mostly SHORT, which is the
    regime where t grows as sqrt(theta), not linearly -- so the penalty for a
    slightly worse neighbour is much milder than intuition suggests.
    """
    th = np.abs(np.asarray(theta_deg, dtype=float))
    th_crit = vmax * vmax / amax
    short = 2.0 * np.sqrt(np.maximum(th, 0.0) / amax)
    long_ = vmax / amax + th / vmax
    return np.where(th <= th_crit, short, long_)


def slew_time(alt0, az0, alt1, az1):
    """Alt-az slew: the two axes move together, so the cost is the SLOWER one."""
    d_alt = np.abs(np.asarray(alt1, dtype=float) - alt0)
    d_az = np.abs(np.asarray(az1, dtype=float) - az0)
    d_az = np.minimum(d_az, 360.0 - d_az)          # wrap the short way
    t = np.maximum(_axis_time(d_alt, V_ALT, A_ALT),
                   _axis_time(d_az, V_AZ, A_AZ))
    return t + T_SETTLE


def visit_cost(slew_s, band_change):
    """Wall-clock charged to one visit."""
    return T_EXP + T_READ + slew_s + (T_FILTER if band_change else 0.0)


# ═════════════════════════════════════════════════════════════════════════════
#  Sky brightness through the night (twilight + moon, coarse but honest)
# ═════════════════════════════════════════════════════════════════════════════
def sky_brightness(band, t_h, alt_deg, moon_ra=None, moon_dec=None,
                   lst_deg=None, moon_illum=0.25):
    """Darkest in the middle of the night, brighter near a bright moon.

    Deliberately coarse. It exists so that the VALUE of a pointing varies
    through the night in a way a scheduler has to trade against slew time --
    which is the whole point of combining them in one scalar. It is not a sky
    model and nothing on screen is derived from its absolute values.
    """
    msky = np.full(np.shape(alt_deg), float(MSKY_DARK[band]))
    # twilight: the first and last 30 min of the window are measurably brighter
    edge = min(t_h, NIGHT_H - t_h)
    if edge < 0.5:
        msky = msky - 1.2 * (0.5 - edge) / 0.5
    if moon_ra is not None:
        m_alt, _ = altaz(moon_ra, moon_dec, lst_deg)
        if m_alt > 0:
            sep = _ang_sep(moon_ra, moon_dec, _RA_CACHE, _DEC_CACHE) \
                if _RA_CACHE is not None else None
            if sep is not None:
                glare = 2.2 * moon_illum * np.exp(-sep / 35.0) \
                    * min(1.0, m_alt / 30.0)
                msky = msky - glare
    return msky


_RA_CACHE = None
_DEC_CACHE = None


def _ang_sep(ra1, dec1, ra2, dec2):
    """Great-circle separation in degrees."""
    r1, d1 = math.radians(ra1), math.radians(dec1)
    r2, d2 = np.radians(ra2), np.radians(dec2)
    cos_s = (math.sin(d1) * np.sin(d2)
             + math.cos(d1) * np.cos(d2) * np.cos(r2 - r1))
    return np.degrees(np.arccos(np.clip(cos_s, -1.0, 1.0)))


# ═════════════════════════════════════════════════════════════════════════════
#  The night: fields, request sets, weather
# ═════════════════════════════════════════════════════════════════════════════
class Night:
    """One night's geometry, precomputed on the block grid.

    Everything both schedulers need is evaluated ONCE here, so that the only
    difference between them is the decision rule -- not the physics, not the
    weather, not the field list. A comparison where the two sides see different
    skies measures the sky, not the scheduler.
    """

    def __init__(self, seed=1717, n_sky=1800, n_sets=170, moon_illum=0.25,
                 lst0_deg=0.0):
        global _RA_CACHE, _DEC_CACHE
        rng = np.random.default_rng(seed)
        ra, dec = fibonacci_sphere(n_sky)
        self.lst0 = lst0_deg
        self.block_h = BLOCK_MIN / 60.0
        self.t_block_h = (np.arange(N_BLOCK) + 0.5) * self.block_h
        self.lst_block = (lst0_deg + 360.0 * self.t_block_h / 23.9344696) % 360.0

        # keep only fields that clear the horizon cut at some point tonight
        alt_all = np.stack([altaz(ra, dec, L)[0] for L in self.lst_block])
        visible_any = (alt_all > ALT_MIN_DEG).any(axis=0)
        idx = np.flatnonzero(visible_any)
        if len(idx) > n_sets:
            idx = rng.choice(idx, size=n_sets, replace=False)
        idx = np.sort(idx)

        self.ra = ra[idx]
        self.dec = dec[idx]
        self.n = len(idx)
        _RA_CACHE, _DEC_CACHE = self.ra, self.dec

        # moon: a fixed position for the night
        self.moon_ra = float(rng.uniform(0, 360))
        self.moon_dec = float(rng.uniform(-40, 20))
        self.moon_illum = moon_illum

        # per (block, field): alt, az, airmass; per (block, field, band): m5, V
        self.alt = np.zeros((N_BLOCK, self.n))
        self.az = np.zeros((N_BLOCK, self.n))
        self.X = np.zeros((N_BLOCK, self.n))
        self.m5 = {b: np.zeros((N_BLOCK, self.n)) for b in BANDS}
        self.V = {b: np.zeros((N_BLOCK, self.n)) for b in BANDS}
        for t in range(N_BLOCK):
            a, z = altaz(self.ra, self.dec, self.lst_block[t])
            self.alt[t], self.az[t] = a, z
            self.X[t] = airmass(a)
            for b in BANDS:
                msky = sky_brightness(b, self.t_block_h[t], a, self.moon_ra,
                                      self.moon_dec, self.lst_block[t],
                                      moon_illum)
                m5 = m5_depth(b, np.where(a > ALT_MIN_DEG, self.X[t], 50.0),
                              msky)
                self.m5[b][t] = np.where(a > ALT_MIN_DEG, m5, -np.inf)
                # the nominal per-visit cost used for WEIGHTING only; the real
                # cost depends on the slew actually taken
                self.V[b][t] = np.where(
                    a > ALT_MIN_DEG,
                    survey_speed(self.m5[b][t], T_EXP + T_READ + 8.0), 0.0)

        self.feasible = self.alt > ALT_MIN_DEG
        # A REQUEST SET IS A PAIR: one g visit AND one r visit of one field,
        # which is Bellm et al.'s own worked example ("two nightly visits, one
        # in g-band and one in r-band"). Two bands is not decoration -- it is
        # what makes completion COST something, because a block carries only
        # one band, so finishing any field forces a band change somewhere.
        self.n_req = np.ones((self.n, len(BANDS)), dtype=int)
        self.weather_ok = np.ones(N_BLOCK, dtype=bool)

    # ── weather ──────────────────────────────────────────────────────────────
    def apply_weather(self, lost_fraction, seed=0):
        """Knock out whole blocks. Both schedulers get the SAME realisation.

        Losses are contiguous runs, not independent coin flips per block:
        clouds arrive and stay, and a scheduler that can re-plan benefits very
        differently from a run of six bad blocks than from six scattered ones.
        """
        rng = np.random.default_rng(seed)
        self.weather_ok = np.ones(N_BLOCK, dtype=bool)
        n_lost = int(round(lost_fraction * N_BLOCK))
        if n_lost <= 0:
            return self.weather_ok
        start = int(rng.integers(0, max(1, N_BLOCK - n_lost + 1)))
        self.weather_ok[start:start + n_lost] = False
        return self.weather_ok


# ═════════════════════════════════════════════════════════════════════════════
#  Combinatorics: why nobody searches the orderings
# ═════════════════════════════════════════════════════════════════════════════
def log10_orderings(n):
    """log10(n!) -- the size of the sequencing problem."""
    return math.lgamma(n + 1) / math.log(10.0)


def log10_block_assignments(n, n_block):
    """log10(n_block^n) -- the size of the ASSIGNMENT problem.

    Assigning n exposures to n_block buckets is n_block^n. This is still
    exponential, and that is the honest statement: blocking does not make the
    problem small, it makes it a problem a branch-and-bound solver can prune.
    The ratio to n! is the number the episode shows, and it is enormous.
    """
    return n * math.log10(n_block)


# ═════════════════════════════════════════════════════════════════════════════
#  SCHEDULER 1 — GREEDY.  "What is best right now?"  Re-decided every exposure.
# ═════════════════════════════════════════════════════════════════════════════
def run_greedy(night, weather=None, pair_gap_s=None, finish_bonus=0.0):
    """Online, myopic, no lookahead. Rubin's Feature Based Scheduler in spirit.

    At every step it scores every feasible (field, band) by the INSTANTANEOUS
    volumetric survey speed -- Bellm et al. (2019) Eq. 2 -- which already
    divides the volume probed by the time the visit costs, slew and band change
    included. So this greedy is not a straw man: it is explicitly trading depth
    against slew, and it is maximising the same quantity the planner maximises.

    What it cannot do is notice that taking this exposure now will strand a
    half-finished pair later. It has no model of "later".

    `finish_bonus` MULTIPLIES the score of any field already holding one half
    of its pair, so 1.0 doubles the appeal of finishing one. It exists to
    answer the obvious objection to this whole comparison -- maybe greedy
    strands pairs only because nobody TOLD it to care about finishing them.
    Turn the knob and find out whether completion is something a myopic rule
    can be PAID to want, or something it structurally cannot deliver.
    """
    if weather is None:
        weather = night.weather_ok
    if pair_gap_s is None:
        pair_gap_s = BLOCK_MIN * 60.0

    n, nb = night.n, len(BANDS)
    done = np.zeros((n, nb), dtype=int)       # visits taken, per set per band
    last_t = np.full(n, -1e9)                 # last visit of this FIELD

    t = 0.0
    t_end = NIGHT_H * 3600.0
    cur_alt, cur_az = 90.0, 0.0               # parked at zenith
    cur_band = 0
    log = []

    while t < t_end:
        blk = min(int(t // (BLOCK_MIN * 60.0)), N_BLOCK - 1)
        if not weather[blk]:
            nxt = blk + 1
            while nxt < N_BLOCK and not weather[nxt]:
                nxt += 1
            if nxt >= N_BLOCK:
                break
            t = nxt * BLOCK_MIN * 60.0
            continue

        lst = (night.lst0 + 360.0 * (t / 3600.0) / 23.9344696) % 360.0
        alt, az = altaz(night.ra, night.dec, lst)
        X = airmass(alt)
        sl = slew_time(cur_alt, cur_az, alt, az)

        up = (alt > ALT_MIN_DEG) & ((t - last_t) >= pair_gap_s)
        best_v, best_j, best_k, best_m5 = -np.inf, -1, -1, np.nan
        for k, b in enumerate(BANDS):
            sel = up & (done[:, k] < night.n_req[:, k])
            if not sel.any():
                continue
            msky = sky_brightness(b, t / 3600.0, alt, night.moon_ra,
                                  night.moon_dec, lst, night.moon_illum)
            m5 = m5_depth(b, np.where(sel, X, 50.0), msky)
            cost = visit_cost(sl, k != cur_band)
            v = np.where(sel, survey_speed(m5, cost), -np.inf)
            if finish_bonus:
                # already holds the OTHER half of its pair -> finishing it
                # completes a sequence
                half = (done.sum(axis=1) > 0) & (done[:, k] < night.n_req[:, k])
                v = np.where(sel & half, v * (1.0 + finish_bonus), v)
            j = int(np.argmax(v))
            if v[j] > best_v:
                best_v, best_j, best_k, best_m5 = float(v[j]), j, k, float(m5[j])

        if best_j < 0 or not np.isfinite(best_v):
            t += 60.0                          # nothing legal; wait a minute
            continue

        cost = float(visit_cost(sl[best_j], best_k != cur_band))
        if t + cost > t_end:
            break
        t += cost
        cur_alt, cur_az = float(alt[best_j]), float(az[best_j])
        cur_band = best_k
        done[best_j, best_k] += 1
        last_t[best_j] = t
        log.append({"t": t, "set": best_j, "band": BANDS[best_k],
                    "alt": float(alt[best_j]), "az": float(az[best_j]),
                    "X": float(X[best_j]),
                    "slew": float(sl[best_j]), "m5": best_m5})

    return _summarise("greedy", night, done, log)


# ═════════════════════════════════════════════════════════════════════════════
#  SCHEDULER 2 — BLOCK PLANNER.  "Which bucket?"  Solved once, exactly.
# ═════════════════════════════════════════════════════════════════════════════
def plan_blocks(night, weather=None, verbose=False, time_limit=120.0,
                rel_gap=1e-3):
    """Integer linear program over (request set x block x band), via HiGHS.

    The real thing, not an analogy: binary decision variables, a linear
    objective, linear constraints, branch and bound. The formulation follows
    Bellm et al. (2019) section 4:

      Y[r,t,f] = 1 if set r takes its band-f visit in block t
      Yt[t,f]  = 1 if block t is observed in band f
      Z[r]     = 1 if set r is scheduled AT ALL
      S[t]     = 1 if the band changes between block t and t+1

      max  sum V[r,t,f] Y[r,t,f]  -  w (t_filt / (t_exp + t_OH)) sum S[t]

      s.t. sum_t Y[r,t,f] = n_req[r,f] * Z[r]     (Eq. 4: ALL OR NOTHING)
           sum_f Yt[t,f] = 1                       (Eq. 5: one band a block)
           sum_r Y[r,t,f] <= cap * Yt[t,f]         (link, aggregated)
           sum_{r,f} Y[r,t,f] c_exp <= T_block      (Eq. 6: it must FIT)
           S[t] >= |Yt[t,f] - Yt[t+1,f]|            (count the changes)
           Y[r,t,f] = 0 below the horizon cut or in a clouded block

    THE LOAD-BEARING LINE IS THE FIRST CONSTRAINT. `= n_req[r,f] * Z[r]` makes
    completion a CONSTRAINT rather than a hope: the solver may decline a field
    entirely, but it may not take one half of a pair. That single equals sign
    is the whole difference measured later.

    TWO CONSEQUENCES WORTH SEEING. Because a pair is one g visit AND one r
    visit, and because a block carries only one band, completing ANY field
    forces the night to change band at least once -- so the planner has to BUY
    band changes to buy completion. And because the two visits land in
    different blocks, the >= 30 min pair separation is enforced by the block
    grid itself, for free. That is Bellm et al.'s own stated reason for
    blocking: it is where the cadence constraint lives.

    Eq. 6 is an INEQUALITY for a reason the paper states outright: strict
    equality over-constrains the model and it becomes infeasible. The price is
    slack -- blocks that do not quite fill.

    The link is AGGREGATED (one row per block-band, with cap as the big-M)
    rather than written per request set. It is exactly equivalent here, because
    the capacity row already bounds the same sum, and it turns ~10^4 rows into
    ~30.
    """
    from scipy.optimize import milp, LinearConstraint, Bounds
    from scipy import sparse

    if weather is None:
        weather = night.weather_ok
    n, T, nb = night.n, N_BLOCK, len(BANDS)

    nY, nYt, nZ, nS = n * T * nb, T * nb, n, T - 1
    oY, oYt, oZ, oS = 0, nY, nY + nYt, nY + nYt + nZ
    N = nY + nYt + nZ + nS

    def iY(r, t, f):
        return oY + (r * T + t) * nb + f

    c_exp = T_EXP + T_READ + 8.0                   # fiducial overhead, as ZTF
    cap_n = int(BLOCK_MIN * 60.0 // c_exp)         # visits that fit in a block

    c = np.zeros(N)
    Vmax = 0.0
    for f, b in enumerate(BANDS):
        Vb = night.V[b]
        for r in range(n):
            for t in range(T):
                v = float(Vb[t, r])
                c[iY(r, t, f)] = -v                # milp minimises
                if v > Vmax:
                    Vmax = v
    c[oS:oS + nS] = +Vmax * (T_FILTER / (T_EXP + T_READ))

    ub = np.ones(N)
    for r in range(n):
        for t in range(T):
            dead = (not night.feasible[t, r]) or (not weather[t])
            for f in range(nb):
                if dead or night.n_req[r, f] == 0:
                    ub[iY(r, t, f)] = 0.0
    bounds = Bounds(lb=np.zeros(N), ub=ub)

    rows, cols, vals, lb_c, ub_c = [], [], [], [], []
    row = 0

    def add(entries, lo, hi):
        nonlocal row
        for cc, vv in entries:
            rows.append(row); cols.append(cc); vals.append(vv)
        lb_c.append(lo); ub_c.append(hi); row += 1

    for t in range(T):                              # one band per block
        add([(oYt + t * nb + f, 1.0) for f in range(nb)], 1.0, 1.0)
    for r in range(n):                              # all-or-nothing completion
        for f in range(nb):
            e = [(iY(r, t, f), 1.0) for t in range(T) if ub[iY(r, t, f)] > 0]
            e.append((oZ + r, -float(night.n_req[r, f])))
            add(e, 0.0, 0.0)
    for t in range(T):                              # aggregated band link
        for f in range(nb):
            e = [(iY(r, t, f), 1.0) for r in range(n) if ub[iY(r, t, f)] > 0]
            if e:
                e.append((oYt + t * nb + f, -float(cap_n)))
                add(e, -np.inf, 0.0)
    for t in range(T):                              # block capacity
        e = [(iY(r, t, f), c_exp) for r in range(n) for f in range(nb)
             if ub[iY(r, t, f)] > 0]
        if e:
            add(e, -np.inf, BLOCK_MIN * 60.0)
    for t in range(T - 1):                          # band changes, both ways
        for f in range(nb):
            add([(oS + t, 1.0), (oYt + t * nb + f, -1.0),
                 (oYt + (t + 1) * nb + f, 1.0)], 0.0, np.inf)
            add([(oS + t, 1.0), (oYt + t * nb + f, 1.0),
                 (oYt + (t + 1) * nb + f, -1.0)], 0.0, np.inf)

    A = sparse.csc_matrix((vals, (rows, cols)), shape=(row, N))
    res = milp(c=c, constraints=LinearConstraint(A, lb_c, ub_c),
               integrality=np.ones(N), bounds=bounds,
               options={"time_limit": time_limit, "presolve": True,
                        "mip_rel_gap": rel_gap})
    if res.x is None:
        raise RuntimeError("ILP failed: %s" % res.message)
    x = np.round(res.x).astype(int)
    plan = {t: [] for t in range(T)}
    for r in range(n):
        for t in range(T):
            for f in range(nb):
                if ub[iY(r, t, f)] > 0 and x[iY(r, t, f)] == 1:
                    plan[t].append((r, f))
    if verbose:
        print("    [ilp] vars=%d rows=%d cap/block=%d  %s"
              % (N, row, cap_n, res.message))
    return plan, x, res


def _tsp_order(night, members, t_blk, alt0, az0):
    """Order one block's visits to minimise slew: nearest neighbour + 2-opt.

    ZTF solves this exactly, as a TSP in Gurobi with cutting planes. HiGHS has
    no TSP, and an exact formulation across sixteen blocks a night is not what
    this episode is about -- so this is a HEURISTIC stand-in and is reported as
    one. 2-opt on a metric instance is typically within a few percent of
    optimal, and no claim in the episode depends on the gap.
    """
    if not members:
        return [], 0.0
    idx = [m_[0] for m_ in members]
    lst = night.lst_block[t_blk]
    alt, az = altaz(night.ra[idx], night.dec[idx], lst)
    m = len(members)

    # One matrix, computed once. Index m is the telescope's CURRENT pointing,
    # so D[m, j] is the cost of opening the block on field j. The slew model is
    # symmetric, which is what makes the delta trick below exact rather than an
    # approximation.
    a_all = np.concatenate([alt, [alt0]])
    z_all = np.concatenate([az, [az0]])
    D = np.asarray(slew_time(a_all[:, None], z_all[:, None],
                             a_all[None, :], z_all[None, :]), dtype=float)
    np.fill_diagonal(D, np.inf)

    # Nearest neighbour from the current pointing: a decent tour to improve on.
    order, unused, cur = [], list(range(m)), m
    while unused:
        k = int(np.argmin(D[cur, unused]))
        cur = unused.pop(k)
        order.append(cur)

    def tour_cost(o):
        if len(o) == 0:
            return 0.0
        p = np.concatenate([[m], np.asarray(o, dtype=int)])
        return float(D[p[:-1], p[1:]].sum())

    # 2-opt. Reversing order[i:k+1] breaks exactly two edges -- the one into
    # position i and the one out of position k -- so each candidate costs two
    # lookups instead of a full re-walk of the tour.
    best = tour_cost(order)
    o = np.asarray(order, dtype=int)
    guard = 0
    while m > 3 and guard < 60:
        guard += 1
        gain = 0.0
        for i in range(m - 1):
            A = m if i == 0 else int(o[i - 1])
            B = int(o[i])
            ks = np.arange(i + 1, m)
            C = o[ks]
            cut_old = D[A, B]
            delta = D[A, C] - cut_old
            tail = ks[:-1]                      # every k except the last
            if tail.size:
                Nx = o[tail + 1]
                delta[:-1] += D[B, Nx] - D[o[tail], Nx]
            j = int(np.argmin(delta))
            if delta[j] < -1e-9:
                k = int(ks[j])
                o[i:k + 1] = o[i:k + 1][::-1]
                gain += float(delta[j])
        if gain > -1e-9:
            break
    best = tour_cost(o)
    return [members[j] for j in o], best


def run_planner(night, weather=None, verbose=False, time_limit=120.0,
                rel_gap=1e-3):
    """Solve the ILP, sequence each block with the TSP, then EXECUTE it.

    Execution is where a plan meets the night. The plan was made against a
    fiducial overhead; the real slews are whatever the tour costs, so a block
    can run over and drop its tail. That loss is real and is reported.
    """
    if weather is None:
        weather = night.weather_ok
    plan, _, res = plan_blocks(night, weather, verbose, time_limit, rel_gap)

    done = np.zeros((night.n, len(BANDS)), dtype=int)
    log = []
    cur_alt, cur_az = 90.0, 0.0
    cur_band = None
    dropped = 0
    for t in range(N_BLOCK):
        if not weather[t] or not plan[t]:
            continue
        order, _ = _tsp_order(night, plan[t], t, cur_alt, cur_az)
        t_now = t * BLOCK_MIN * 60.0
        t_stop = (t + 1) * BLOCK_MIN * 60.0
        lst = night.lst_block[t]
        for ii, (r, f) in enumerate(order):
            b = BANDS[f]
            alt, az = altaz(night.ra[r], night.dec[r], lst)
            sl = float(slew_time(cur_alt, cur_az, alt, az))
            cost = float(visit_cost(sl, f != cur_band))
            if t_now + cost > t_stop:
                dropped += len(order) - ii
                break                         # the block ran out; tail lost
            t_now += cost
            cur_alt, cur_az, cur_band = float(alt), float(az), f
            done[r, f] += 1
            X = float(airmass(alt))
            log.append({"t": t_now, "set": r, "band": b, "alt": float(alt),
                        "az": float(az),
                        "X": X, "slew": sl, "m5": float(m5_depth(b, X))})
    out = _summarise("planner", night, done, log)
    out["ilp_objective"] = float(-res.fun) if res.fun is not None else None
    out["planned_visits"] = int(sum(len(v) for v in plan.values()))
    out["dropped_at_block_end"] = dropped
    out["ilp_status"] = str(res.message)
    return out


# ═════════════════════════════════════════════════════════════════════════════
#  Scoring
# ═════════════════════════════════════════════════════════════════════════════
def _summarise(name, night, done, log):
    """The metrics, including the one that decides the episode.

    `completion` is the SEQUENCE COMPLETION FRACTION over the sets the
    scheduler actually TOUCHED: of the fields it started, how many did it
    finish? That denominator is the fair one -- a scheduler is not penalised
    for leaving an untouched field alone, only for stranding one it began.

    A pair is one g visit AND one r visit of the same field. One of the two is
    not half a detection. It is zero detections, because nothing can be
    compared against nothing.
    """
    req = night.n_req
    started = int((done.sum(axis=1) > 0).sum())
    full = (done >= req).all(axis=1)
    complete = int(full.sum())
    stranded = int(((done.sum(axis=1) > 0) & (~full)).sum())
    visits = int(done.sum())
    Xs = np.array([e["X"] for e in log]) if log else np.array([np.nan])
    sl = np.array([e["slew"] for e in log]) if log else np.array([np.nan])
    m5s = np.array([e["m5"] for e in log]) if log else np.array([np.nan])
    bands = [e["band"] for e in log]
    changes = sum(1 for i in range(1, len(bands)) if bands[i] != bands[i - 1])
    return {
        "name": name,
        "visits": visits,
        "visits_per_hour": visits / NIGHT_H,
        "started": started,
        "complete": complete,
        "stranded": stranded,
        "completion": (complete / started) if started else 0.0,
        "median_airmass": float(np.median(Xs)),
        "median_slew": float(np.median(sl)),
        "median_m5": float(np.median(m5s)),
        "band_changes": changes,
        "metric_sum": float(np.sum(survey_speed(m5s, T_EXP + T_READ + 8.0)))
        if log else 0.0,
        "done": done,
        "log": log,
    }
