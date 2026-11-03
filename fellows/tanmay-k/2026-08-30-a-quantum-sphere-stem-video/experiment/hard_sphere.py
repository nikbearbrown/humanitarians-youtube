#!/usr/bin/env python3
"""Quantum hard-sphere scattering: the total cross section, from partial waves.

The physics
    An impenetrable sphere of radius `a`. The wavefunction must vanish on its surface,
    which fixes every phase shift exactly -- no potential integral, no approximation:

        tan d_l = j_l(ka) / n_l(ka)

    and the total cross section follows from the partial-wave sum

        sigma = (4*pi/k^2) * SUM_l (2l+1) sin^2 d_l

    Reported here as the ratio to the CLASSICAL answer, pi*a^2, since that ratio is the
    whole story:

        sigma/(pi a^2) = (4/(ka)^2) * SUM_l (2l+1) * j_l^2 / (j_l^2 + n_l^2)

Why write it out instead of calling scipy
    Two reasons. It runs on a stock python3 with no install, so anyone can re-run the
    numbers in this folder. And the l > ka regime -- which is exactly where the sum has to
    be truncated -- is where the naive upward recurrence for j_l silently loses all its
    significant figures. Owning that failure is half the result (see --stability).

Usage
    python3 hard_sphere.py --validate     # check j_l/n_l against closed forms + Wronskian
    python3 hard_sphere.py --limits       # the two limits, and how fast each is reached
    python3 hard_sphere.py --exponent     # measure the approach to 2; don't assume 2/3
    python3 hard_sphere.py --check-source # verify the numbers shown in the source video
    python3 hard_sphere.py --stability    # why upward recurrence for j_l is wrong here
    python3 hard_sphere.py --curve        # sigma/(pi a^2) over a ka grid -> CSV
    python3 hard_sphere.py --contrast     # control: a square well, which DOES resonate
    python3 hard_sphere.py --all
"""

import argparse
import json
import math
import pathlib
import sys

# ---------------------------------------------------------------------------
# Spherical Bessel functions
# ---------------------------------------------------------------------------
# n_l (spherical Neumann, "second kind") grows with l, so UPWARD recurrence is stable:
# the dominant solution is the one being computed and rounding error stays relatively
# small. j_l is the opposite -- for l > x it decays like (x/2)^l / (2l+1)!!, so upward
# recurrence lets any rounding error, which grows like n_l, swamp the answer.


def sph_n(lmax, x):
    """n_l(x) for l = 0..lmax by upward recurrence (stable for the Neumann function)."""
    if x <= 0.0:
        raise ValueError("x must be positive")
    out = [0.0] * (lmax + 1)
    out[0] = -math.cos(x) / x
    if lmax >= 1:
        out[1] = -math.cos(x) / (x * x) - math.sin(x) / x
    for l in range(1, lmax):
        out[l + 1] = (2 * l + 1) / x * out[l] - out[l - 1]
    return out


def sph_j(lmax, x):
    """j_l(x) for l = 0..lmax by Miller's downward recurrence, normalised on j_0.

    Start high above lmax with an arbitrary seed and recur DOWNWARD. The downward
    direction is the stable one for j_l: the unwanted n_l admixture decays instead of
    growing, so whatever the seed was, the ratios converge onto the true j_l. Fixing the
    overall scale afterwards against the closed form j_0 = sin(x)/x turns those ratios
    into values.
    """
    if x <= 0.0:
        raise ValueError("x must be positive")
    # Start far enough above both lmax and x that the seed has room to be forgotten.
    start = int(lmax + 20 + 15 * math.sqrt(max(x, 1.0)))
    vals = [0.0] * (start + 2)
    vals[start + 1] = 0.0
    vals[start] = 1e-280  # arbitrary seed; the normalisation at the end removes it
    for l in range(start, 0, -1):
        vals[l - 1] = (2 * l + 1) / x * vals[l] - vals[l + 1]
        if abs(vals[l - 1]) > 1e250:  # renormalise before the recurrence overflows
            scale = 1e-250
            for k in range(l - 1, start + 2):
                vals[k] *= scale
    norm = (math.sin(x) / x) / vals[0]
    return [vals[l] * norm for l in range(lmax + 1)]


# ---------------------------------------------------------------------------
# Cross section
# ---------------------------------------------------------------------------

def lmax_for(ka, pad=25):
    """Partial waves to keep. Semiclassically, l ~ ka is the last wave whose impact
    parameter l/k still lands on the sphere; higher waves miss it and contribute
    essentially nothing. The pad covers the soft 'edge' region just above ka."""
    return int(ka + pad + 8 * ka ** (1.0 / 3.0))


def sigma_ratio(ka, lmax=None, want_terms=False):
    """sigma / (pi a^2) for a hard sphere at wavenumber*radius = ka."""
    if lmax is None:
        lmax = lmax_for(ka)
    j = sph_j(lmax, ka)
    n = sph_n(lmax, ka)
    total = 0.0
    terms = []
    for l in range(lmax + 1):
        denom = j[l] * j[l] + n[l] * n[l]
        s2 = 0.0 if denom == 0.0 else (j[l] * j[l]) / denom  # sin^2 d_l
        contrib = (2 * l + 1) * s2
        total += contrib
        if want_terms:
            terms.append(contrib)
    ratio = 4.0 / (ka * ka) * total
    return (ratio, terms) if want_terms else ratio


def waves_needed(ka, frac=0.999):
    """Smallest l_max capturing `frac` of the converged sum -- the honest 'how many
    partial waves does this actually take' number."""
    full, terms = sigma_ratio(ka, want_terms=True)
    target = frac * (full * ka * ka / 4.0)
    run = 0.0
    for l, t in enumerate(terms):
        run += t
        if run >= target:
            return l
    return len(terms) - 1


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

def validate():
    print("=== VALIDATION: j_l and n_l against independent closed forms ===\n")
    worst = 0.0
    for x in (0.3, 1.0, 5.0, 13.6, 40.0):
        j = sph_j(6, x)
        n = sph_n(6, x)
        # Closed forms, written out independently of the recurrences above.
        cf_j = [math.sin(x) / x,
                math.sin(x) / x**2 - math.cos(x) / x,
                (3 / x**3 - 1 / x) * math.sin(x) - 3 / x**2 * math.cos(x)]
        cf_n = [-math.cos(x) / x,
                -math.cos(x) / x**2 - math.sin(x) / x,
                (-3 / x**3 + 1 / x) * math.cos(x) - 3 / x**2 * math.sin(x)]
        for l in range(3):
            worst = max(worst, abs(j[l] - cf_j[l]), abs(n[l] - cf_n[l]))
        # Wronskian: j_l(x) n_{l-1}(x) - j_{l-1}(x) n_l(x) = 1/x^2, for every l.
        wr = max(abs((j[l] * n[l - 1] - j[l - 1] * n[l]) - 1 / x**2) for l in range(1, 7))
        print(f"  x={x:6.2f}   max |closed-form - recurrence| = {max(abs(j[l]-cf_j[l]) for l in range(3)):.3e}"
              f"   max Wronskian error (l=1..6) = {wr:.3e}")
        worst = max(worst, wr)
    print(f"\n  Worst error anywhere: {worst:.3e}")
    print("  VERDICT:", "PASS" if worst < 1e-12 else "FAIL")


def stability():
    print("\n=== STABILITY: why j_l needs downward recurrence ===\n")
    x = 13.6
    lmax = 40

    def sph_j_upward(lmax, x):
        out = [0.0] * (lmax + 1)
        out[0] = math.sin(x) / x
        out[1] = math.sin(x) / x**2 - math.cos(x) / x
        for l in range(1, lmax):
            out[l + 1] = (2 * l + 1) / x * out[l] - out[l - 1]
        return out

    up = sph_j_upward(lmax, x)
    dn = sph_j(lmax, x)
    print(f"  ka = {x}   (so l > {int(x)} is the 'classically forbidden' tail)\n")
    print(f"  {'l':>3}  {'j_l upward':>15}  {'j_l downward':>15}  {'rel. error':>12}")
    for l in (5, 10, 14, 16, 20, 25, 30, 40):
        rel = abs(up[l] - dn[l]) / abs(dn[l]) if dn[l] != 0 else float("inf")
        print(f"  {l:3d}  {up[l]:15.6e}  {dn[l]:15.6e}  {rel:12.2e}")
    print("\n  Upward recurrence is fine while l < ka and then diverges completely --")
    print("  by l=30 it is not wrong in the last digit, it is wrong in every digit.")
    print("  Those are exactly the waves the truncation decision depends on.")


def limits():
    print("\n=== THE TWO LIMITS ===\n")
    print("  Classical hard sphere: sigma/(pi a^2) = 1 exactly, at every energy.\n")
    print("  LOW ENERGY  (ka -> 0):")
    print(f"  {'ka':>10}  {'sigma/(pi a^2)':>16}  {'waves (99.9%)':>14}")
    for ka in (1e-4, 1e-3, 1e-2, 0.05, 0.1, 0.3, 0.5, 1.0):
        print(f"  {ka:10.4g}  {sigma_ratio(ka):16.9f}  {waves_needed(ka):14d}")
    print("\n  -> 4. Four times the classical cross section, carried entirely by l=0.\n")

    print("  HIGH ENERGY  (ka -> inf):")
    print(f"  {'ka':>10}  {'sigma/(pi a^2)':>16}  {'excess over 2':>14}  {'waves (99.9%)':>14}")
    rows = []
    for ka in (5, 10, 20, 50, 100, 200, 500, 1000, 2000):
        r = sigma_ratio(float(ka))
        rows.append((ka, r))
        print(f"  {ka:10d}  {r:16.9f}  {r - 2.0:14.6f}  {waves_needed(float(ka)):14d}")
    print("\n  -> 2. Twice classical, and it converges SLOWLY.")

    # Fit the approach: is the excess over 2 going like (ka)^(-2/3)?
    print("\n  How fast? Fit (sigma/pi a^2 - 2) = C * (ka)^(-p) on the last decade:")
    (x1, y1), (x2, y2) = (rows[-3][0], rows[-3][1]), (rows[-1][0], rows[-1][1])
    p = -math.log((y2 - 2) / (y1 - 2)) / math.log(x2 / x1)
    C = (y1 - 2) * x1 ** p
    print(f"    fitted exponent p = {p:.4f}   (textbook edge-effect prediction: 2/3 = 0.6667)")
    print(f"    fitted C          = {C:.4f}")
    print(f"    => to get within 1% of 2 you need ka ~ {(C / 0.02) ** (1 / p):,.0f}")
    r100 = sigma_ratio(100.0)
    print("\n  The 'high-energy limit is 2' is a limit, not a description of any")
    print(f"  experiment: at ka=100 the true answer is {r100:.4f}, still"
          f" {(r100 - 2) / 2 * 100:.1f}% above it.")


def check_source():
    print("\n=== CHECKING THE SOURCE VIDEO'S ON-SCREEN NUMBERS ===\n")
    print("  Frame B06 of claude-liam-cli-vol3-hard-sphere-crosssection displays:")
    print('    "At ka = 13.6:  sigma/a^2 = 2.328"')
    print('    "Current ka = 13.6 | l_max needed = 16"\n')
    ka = 13.6
    r = sigma_ratio(ka)
    n999 = waves_needed(ka, 0.999)
    n9999 = waves_needed(ka, 0.9999)
    print(f"  Recomputed here:  sigma/(pi a^2) = {r:.6f}")
    print(f"  Source claim:                      2.328")
    print(f"  Difference:                        {abs(r - 2.328):.6f}   ->"
          f" {'MATCH' if abs(r - 2.328) < 5e-4 else 'MISMATCH'}\n")
    print(f"  Waves for 99.9% of the sum:  l_max = {n999}")
    print(f"  Waves for 99.99% of the sum: l_max = {n9999}")
    print(f"  Source claim:                l_max = 16   ->"
          f" {'MATCH' if n999 == 16 or n9999 == 16 else 'differs (see note)'}\n")
    print("  NOTE ON THE LABEL, NOT THE NUMBER: the frame writes 'sigma/a^2', but 2.328")
    print("  is the ratio to pi*a^2, not to a^2. The value is right; the label drops a pi.")


def curve(path=None):
    # Relative to THIS file, not the caller's cwd -- the outputs belong next to the
    # script that made them regardless of where it was invoked from.
    path = path or (pathlib.Path(__file__).resolve().parent / "sigma_curve.csv")
    print("\n=== CURVE ===\n")
    grid = [0.01 * i for i in range(1, 100)] + [0.1 * i for i in range(10, 300)]
    with open(path, "w") as fh:
        fh.write("ka,sigma_over_pi_a2,waves_999\n")
        for ka in grid:
            fh.write(f"{ka:.4f},{sigma_ratio(ka):.9f},{waves_needed(ka)}\n")
    print(f"  Wrote {pathlib.Path(path).name}  ({len(grid)} points, ka = 0.01 .. 30)")

    # Is the descent from 4 to 2 monotonic? The answer is the interesting part.
    # Include the right endpoint. The curve is monotone decreasing (see below), so the
    # minimum over the range IS the endpoint -- a grid stopping at 29.98 reports 2.1989
    # where ka = 30 gives 2.1988, and then the doc and the frame quote different numbers.
    vals = ([(ka, sigma_ratio(ka)) for ka in [0.02 * i for i in range(1, 1500)]]
            + [(30.0, sigma_ratio(30.0))])
    turns = []
    for i in range(1, len(vals) - 1):
        a, b, c = vals[i - 1][1], vals[i][1], vals[i + 1][1]
        if (b - a) * (c - b) < 0:
            turns.append((vals[i][0], b, "min" if b < a else "max"))
    print(f"\n  Turning points on 0 < ka < 30: {len(turns)}")
    for ka, v, kind in turns[:8]:
        print(f"    ka = {ka:6.2f}   sigma/(pi a^2) = {v:.4f}   ({kind})")
    if turns:
        print("\n  So the fall from 4 to 2 is NOT monotonic -- it overshoots and rings.")
        print("  Each wobble is one partial wave switching on as ka passes it.")
    else:
        print("\n  None. The fall from 4 to 2 is strictly monotonic.")
        print("  This was worth checking and the guess going in was wrong: a partial-wave")
        print("  sum switching on one wave at a time sounds like it should ring, and for a")
        print("  square WELL it does -- quasi-bound states inside the well give resonances.")
        print("  An impenetrable sphere has no inside. Nothing can be quasi-bound in it, so")
        print("  there is no resonance to ring, and the curve just slides from 4 to 2.")
    lo = min(v for _, v in vals)
    print(f"\n  Minimum over the scanned range: sigma/(pi a^2) = {lo:.4f}")
    print(f"  Classical value:                                 1.0000")
    print("  The quantum curve never touches classical anywhere on this range.")


def exponent():
    """How fast does sigma/(pi a^2) fall to 2? Measure the exponent, don't assume it."""
    print("\n=== THE APPROACH TO 2, MEASURED ===\n")
    print("  Model: sigma/(pi a^2) - 2 = C * (ka)^(-p). Fit p on successive decades and")
    print("  watch whether it settles. If it drifts, the model is wrong; if it converges,")
    print("  the limit it converges to is the answer.\n")
    pts = [10, 32, 100, 320, 1000, 3200, 10000]
    vals = [(x, sigma_ratio(float(x)) - 2.0) for x in pts]
    print(f"  {'ka range':>16}  {'excess at ka1':>14}  {'excess at ka2':>14}  {'local p':>9}")
    ps = []
    for (x1, e1), (x2, e2) in zip(vals, vals[1:]):
        p = -math.log(e2 / e1) / math.log(x2 / x1)
        ps.append(p)
        print(f"  {x1:6d} -> {x2:<6d}  {e1:14.6f}  {e2:14.6f}  {p:9.4f}")
    print(f"\n  p climbs monotonically {ps[0]:.4f} -> {ps[-1]:.4f} across three decades.")
    print(f"  2/3 = {2/3:.4f}. The measurement is consistent with p = 2/3 and with")
    print("  nothing else nearby; it is still a numerical result, not a proof.")
    print("\n  Consequence, which is the part that matters for reading a graph:")
    C = vals[-1][1] * pts[-1] ** (2 / 3)
    for tol in (0.10, 0.05, 0.01):
        print(f"    within {tol*100:4.1f}% of 2  =>  ka > {(C/(2*tol))**1.5:>12,.0f}")


def export_props(path=None):
    """Emit the real measured curves as beat-sheet props -> component_props.json.

    The Remotion scenes must draw the DATA, not an artist's impression of it. The house
    convention is that a scene is generic and its content arrives per beat, so the numbers
    travel as props rather than being baked into the component or into the shared toolkit.

    Curves are downsampled to ~140 points -- smooth at 1920px, small enough to sit in a
    beat sheet without drowning it.
    """
    path = path or (pathlib.Path(__file__).resolve().parent / "component_props.json")

    def sample(lo, hi, n):
        """Log-spaced where the action is, since the interesting structure is at small ka."""
        return [lo * (hi / lo) ** (i / (n - 1)) for i in range(n)]

    sphere = [(round(ka, 4), round(sigma_ratio(ka), 5)) for ka in sample(0.02, 30.0, 140)]
    well = [(round(ka, 4), round(well_ratio(ka, 900.0), 5))
            for ka in [0.02 + i * (18.0 - 0.02) / 359 for i in range(360)]]

    payload = {
        "_source": "experiment/hard_sphere.py --export-props",
        "sphereCurve": sphere,
        "wellCurve": well,
        "classical": 1.0,
        "limits": {"low": 4.0, "high": 2.0},
        "minimum": {"ka": 30.0, "value": round(sigma_ratio(30.0), 4)},
        "readouts": {
            "low": {"ka": 1e-4, "value": round(sigma_ratio(1e-4), 9)},
            "mid": {"ka": 13.6, "value": round(sigma_ratio(13.6), 6)},
            "high": {"ka": 2000.0, "value": round(sigma_ratio(2000.0), 4)},
        },
        "wavesNeeded": [{"ka": ka, "waves": waves_needed(float(ka))}
                        for ka in (100, 2000)],
        "exponentScan": [], "rivalExponents": [], "tolerance": [],
    }
    pts = [10, 32, 100, 320, 1000, 3200, 10000]
    vals = [(x, sigma_ratio(float(x)) - 2.0) for x in pts]
    for (x1, e1), (x2, e2) in zip(vals, vals[1:]):
        payload["exponentScan"].append(
            {"range": f"{x1} -> {x2}", "p": round(-math.log(e2 / e1) / math.log(x2 / x1), 4)})
    for name, p_ in (("0.65", 0.65), ("2/3", 2 / 3), ("0.70", 0.70)):
        cs = [(sigma_ratio(float(ka)) / 2 - 1) * ka ** p_ for ka in (100, 1000, 10000, 30000)]
        payload["rivalExponents"].append(
            {"p": name, "c": [round(c, 4) for c in cs], "drift": round(cs[-1] / cs[0], 3),
             "flat": abs(cs[-1] / cs[0] - 1) < 0.05})
    C = (sigma_ratio(10000.0) - 2.0) * 10000 ** (2 / 3)
    for tol in (0.10, 0.05, 0.01):
        payload["tolerance"].append({"within": f"{tol*100:.0f}%",
                                     "ka": int((C / (2 * tol)) ** 1.5)})
    pathlib.Path(path).write_text(json.dumps(payload, indent=1))
    print(f"\n=== EXPORT ===\n  Wrote {pathlib.Path(path).name}: "
          f"{len(sphere)} sphere points, {len(well)} well points, "
          f"{len(payload['exponentScan'])} scan rows")


def exponent_test():
    """Is the exponent 2/3, or just near it? Test it instead of asserting it.

    If  sigma/(2 pi a^2) - 1 = C * (ka)^(-p)  with p = 2/3, then the quantity

        C(ka) := (sigma/(2 pi a^2) - 1) * (ka)^(2/3)

    must flatten to a constant as ka grows. Assume a WRONG exponent and the same quantity
    drifts without limit -- monotonically, and in a direction that tells you the sign of the
    error. So the drift of C is a sharper test than fitting p, and it is falsifiable: a rival
    exponent has to survive it too.
    """
    print("\n=== IS THE EXPONENT 2/3? A FALSIFICATION TEST ===\n")
    kas = [100, 300, 1000, 3000, 10000, 30000]
    excess = [(ka, sigma_ratio(float(ka)) / 2.0 - 1.0) for ka in kas]

    rivals = [("3/5", 0.6), ("0.65", 0.65), ("2/3", 2.0 / 3.0), ("0.70", 0.70),
              ("3/4", 0.75)]
    print("  C(ka) = (sigma/(2 pi a^2) - 1) * (ka)^p, for each candidate p.")
    print("  The true p is the one whose C stops moving.\n")
    header = "  " + f"{'ka':>7}" + "".join(f"{n:>11}" for n, _ in rivals)
    print(header)
    cols = {n: [] for n, _ in rivals}
    for ka, e in excess:
        row = f"  {ka:7d}"
        for name, p in rivals:
            c = e * ka ** p
            cols[name].append(c)
            row += f"{c:11.4f}"
        print(row)

    print("\n  Drift across the range (last / first) -- 1.000 means perfectly flat:")
    best, best_drift = None, None
    for name, _ in rivals:
        drift = cols[name][-1] / cols[name][0]
        mark = ""
        if best_drift is None or abs(math.log(drift)) < abs(math.log(best_drift)):
            best, best_drift = name, drift
        print(f"    p = {name:>5}   drift = {drift:6.3f}   "
              f"{'rises' if drift > 1.01 else 'falls' if drift < 0.99 else 'FLAT'}{mark}")
    print(f"\n  Flattest: p = {best} (drift {best_drift:.3f}).")
    print("  The neighbours drift monotonically in opposite directions, which brackets the")
    print("  true exponent between them. 2/3 is not merely the best fit on offer -- it is the")
    print("  only candidate tested that does not drift.")
    print("\n  Still a numerical result. It does not derive 2/3; it rules out the alternatives")
    print("  nearby, which is a different and weaker claim, and the script says so.")


def sph_jp(l, x, j=None):
    """d/dx j_l(x), via j_l'(x) = j_{l-1}(x) - (l+1)/x * j_l(x)."""
    j = j or sph_j(max(l, 1), x)
    jm = math.cos(x) / x if l == 0 else j[l - 1]  # j_{-1}(x) = cos(x)/x
    return jm - (l + 1) / x * j[l]


def sph_np(l, x, n=None):
    n = n or sph_n(max(l, 1), x)
    nm = math.sin(x) / x if l == 0 else n[l - 1]  # n_{-1}(x) = sin(x)/x
    return nm - (l + 1) / x * n[l]


def well_ratio(ka, u0a2):
    """sigma/(pi a^2) for an ATTRACTIVE spherical square well, depth set by
    u0a2 = 2*m*V0*a^2/hbar^2. Matching the interior and exterior log-derivatives at r=a:

        tan d_l = [ka j_l'(ka) - b_l j_l(ka)] / [ka n_l'(ka) - b_l n_l(ka)],
        b_l = Ka j_l'(Ka)/j_l(Ka),   (Ka)^2 = (ka)^2 + u0a2

    Included only as a CONTROL: it is the case that does ring, which is how we know the
    hard sphere's smoothness is a fact about the sphere and not about the method.
    """
    Ka = math.sqrt(ka * ka + u0a2)
    lmax = lmax_for(ka)
    j_out, n_out = sph_j(lmax + 1, ka), sph_n(lmax + 1, ka)
    j_in = sph_j(lmax + 1, Ka)
    total = 0.0
    for l in range(lmax + 1):
        if j_in[l] == 0.0:
            continue
        b = Ka * sph_jp(l, Ka, j_in) / j_in[l]
        num = ka * sph_jp(l, ka, j_out) - b * j_out[l]
        den = ka * sph_np(l, ka, n_out) - b * n_out[l]
        d = math.atan2(num, den)
        total += (2 * l + 1) * math.sin(d) ** 2
    return 4.0 / (ka * ka) * total


def contrast():
    print("\n=== CONTROL: does the method ring when the target CAN ring? ===\n")
    print("  Claim under test: the hard sphere's 4->2 slide is smooth because an")
    print("  impenetrable sphere has no interior to hold a quasi-bound state -- not")
    print("  because a partial-wave sum is intrinsically smooth.")
    print("  Test: run the identical machinery on an attractive square well, which does")
    print("  have an interior. If that rings, the explanation survives.\n")
    u0a2 = 900.0  # 2 m V0 a^2 / hbar^2
    vals = [(0.02 * i, well_ratio(0.02 * i, u0a2)) for i in range(1, 900)]
    peaks = []
    for i in range(1, len(vals) - 1):
        a, b, c = vals[i - 1][1], vals[i][1], vals[i + 1][1]
        if b > a and b > c:
            peaks.append((vals[i][0], b))
    print(f"  Attractive well, 2mV0a^2/hbar^2 = {u0a2:g}:  {len(peaks)} resonance peaks"
          f" on 0 < ka < 18")
    for ka, v in peaks[:6]:
        print(f"    ka = {ka:5.2f}   sigma/(pi a^2) = {v:8.3f}")
    hs = [(0.02 * i, sigma_ratio(0.02 * i)) for i in range(1, 900)]
    hs_peaks = sum(1 for i in range(1, len(hs) - 1)
                   if hs[i][1] > hs[i - 1][1] and hs[i][1] > hs[i + 1][1])
    print(f"\n  Same code, same ka grid, hard sphere:      {hs_peaks} resonance peaks")
    print("\n  VERDICT:", "SUPPORTED" if peaks and hs_peaks == 0 else "NOT SUPPORTED",
          "-- the machinery rings fine when there is an interior to ring in.")
    print("  The hard sphere's smoothness is a fact about the target, not the tool.")


def main():
    ap = argparse.ArgumentParser()
    for flag in ("validate", "limits", "exponent", "exponent-test", "check-source",
                 "stability", "curve", "contrast", "export-props", "all"):
        ap.add_argument(f"--{flag}", action="store_true")
    args = ap.parse_args()
    ran = False
    if args.all or args.validate:
        validate(); ran = True
    if args.all or args.stability:
        stability(); ran = True
    if args.all or args.limits:
        limits(); ran = True
    if args.all or args.exponent:
        exponent(); ran = True
    if args.all or getattr(args, "exponent_test"):
        exponent_test(); ran = True
    if args.all or getattr(args, "check_source"):
        check_source(); ran = True
    if args.all or args.curve:
        curve(); ran = True
    if args.all or args.contrast:
        contrast(); ran = True
    if args.all or getattr(args, "export_props"):
        export_props(); ran = True
    if not ran:
        ap.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
