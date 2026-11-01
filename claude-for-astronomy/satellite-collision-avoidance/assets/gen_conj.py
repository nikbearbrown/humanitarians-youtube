"""gen_conj.py — the experiment, its self-check, and the six plates.

Ep. 15, *satellite-collision-avoidance*.

Run:  python -I assets/gen_conj.py

FOUR claims are ASSERTED. If any fails, NOTHING is written — a plate that
disagrees with the narration is worse than no plate.

Plates carry IMAGERY ONLY. No text, no tick labels, no legend: every label on
screen is placed by scenes.py OUTSIDE the plate, because a plate is an
ImageMobject and the layout gate is nearly blind to it.
"""
import io
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import conj as C

OUT = os.path.join(HERE, "plots")

CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)
ACCT = (164, 74, 50)
FAINT = (214, 210, 196)

SEED = 1515
N_EVENTS = 120000
N_TRAIN = 80000
D_EX = 300.0          # the worked example's miss distance, metres
SIG_BAD = 5000.0      # a deliberately degraded tracking solution


# ═════════════════════════════════════════════════════════════════════════════
#  the experiment
# ═════════════════════════════════════════════════════════════════════════════
def run():
    s_peak, p_peak = C.peak_sigma(D_EX)
    s_cross = C.sigma_at_threshold(D_EX, thresh=C.P_ACT, branch="upper")
    p_good = float(C.pc(s_peak, D_EX))
    p_bad = float(C.pc(SIG_BAD, D_EX))
    p_max = float(C.pc_max(D_EX)[0])

    print("[gen_conj] worked example: miss distance %.0f m, hard-body %.0f m"
          % (D_EX, C.HBR))
    print("  Pc peaks at sigma %.1f m  (d/sqrt(2) = %.1f)   Pc = %.3e"
          % (s_peak, D_EX / np.sqrt(2), p_peak))
    print("  Pc crosses %.0e at sigma %.1f m on the dilution branch"
          % (C.P_ACT, s_cross))
    print("  well tracked  sigma %7.1f m -> Pc %.3e" % (s_peak, p_good))
    print("  degraded      sigma %7.1f m -> Pc %.3e" % (SIG_BAD, p_bad))
    print("  max-Pc (scale-free)            -> %.3e" % p_max)

    rng = np.random.default_rng(SEED)
    ev = C.make_events(rng, N_EVENTS)
    final = ev["risk"][:, -1]
    i_cut = int(np.where(C.T_GRID == C.T_CUT)[0][0])
    plain, geom, r_last = C.features(ev, i_cut)

    ytr, yte = final[:N_TRAIN], final[N_TRAIN:]
    pers = r_last[N_TRAIN:]
    hi = yte > C.RISK_FLOOR

    w_p = C.ridge_fit(plain[:N_TRAIN], ytr)
    w_g = C.ridge_fit(geom[:N_TRAIN], ytr)
    pred_p = C.ridge_pred(w_p, plain[N_TRAIN:])
    pred_g = C.ridge_pred(w_g, geom[N_TRAIN:])

    elev = r_last[:N_TRAIN] > C.RISK_FLOOR
    ww = np.where(elev, 300.0, 1.0)
    X1 = np.column_stack([geom[:N_TRAIN], np.ones(N_TRAIN)])
    Xw = X1 * ww[:, None]
    w_w = np.linalg.solve(X1.T @ Xw + 1e-3 * np.eye(X1.shape[1]), Xw.T @ ytr)
    pred_w = np.column_stack([geom[N_TRAIN:], np.ones(len(yte))]) @ w_w

    def mse(p, m=None):
        return float(np.mean((p - yte)[m if m is not None else slice(None)] ** 2)
                     ) if m is None else float(np.mean((p[m] - yte[m]) ** 2))

    res = {}
    for nm, p in (("persistence", pers), ("ridge", pred_p),
                  ("ridge_geom", pred_g), ("ridge_weighted", pred_w)):
        res[nm] = (mse(p), mse(p, hi))

    n_hi = {t: int((final >= t).sum()) for t in (-4, -5, -6.0 + 1e-9)}
    print("\n[gen_conj] population: %d events" % N_EVENTS)
    print("  final risk >= 1e-4 : %4d  (%.2f%%)"
          % (n_hi[-4], 100.0 * n_hi[-4] / N_EVENTS))
    print("  ends above the 1e-6 floor (notified): %d of %d test (%.2f%%)"
          % (hi.sum(), len(yte), 100.0 * hi.mean()))
    print("\n  %-18s %10s %14s" % ("", "all MSE", "notified MSE"))
    for nm in ("persistence", "ridge", "ridge_geom", "ridge_weighted"):
        print("  %-18s %10.4f %14.3f" % (nm, res[nm][0], res[nm][1]))

    return dict(s_peak=s_peak, p_peak=p_peak, s_cross=s_cross, p_good=p_good,
                p_bad=p_bad, p_max=p_max, ev=ev, final=final, i_cut=i_cut,
                res=res, hi=hi, yte=yte, n_hi4=n_hi[-4])


# ═════════════════════════════════════════════════════════════════════════════
#  the self-check — four claims
# ═════════════════════════════════════════════════════════════════════════════
def selfcheck(p):
    fails = []
    r = p["res"]

    # 1. Pc is NOT monotonic in sigma: it rises to an interior peak and falls.
    lo = float(C.pc(p["s_peak"] / 20.0, D_EX))
    hi = float(C.pc(p["s_peak"] * 20.0, D_EX))
    ok1 = p["p_peak"] > lo * 10 and p["p_peak"] > hi * 10
    near = abs(p["s_peak"] - D_EX / np.sqrt(2)) / (D_EX / np.sqrt(2)) < 0.05
    if not (ok1 and near):
        fails.append("1: Pc not interior-peaked at d/sqrt(2) "
                     "(peak %.3e vs lo %.3e hi %.3e)" % (p["p_peak"], lo, hi))

    # 2. Degrading tracking walks the decision across the threshold.
    ok2 = p["p_good"] > C.P_ACT > p["p_bad"] and p["p_good"] / p["p_bad"] > 50
    if not ok2:
        fails.append("2: no threshold flip (good %.3e bad %.3e thresh %.0e)"
                     % (p["p_good"], p["p_bad"], C.P_ACT))

    # 3. THE REVERSAL: ridge wins on all events, persistence wins on the
    #    notified ones. This is the claim the first measurement refused --
    #    the original hypothesis was that persistence would win overall --
    #    and it is stated here as what was actually measured.
    ok3 = (r["ridge"][0] < r["persistence"][0] / 2.0
           and r["persistence"][1] < r["ridge"][1] / 2.0)
    if not ok3:
        fails.append("3: no ranking reversal (all %.4f/%.4f notified %.3f/%.3f)"
                     % (r["ridge"][0], r["persistence"][0],
                        r["ridge"][1], r["persistence"][1]))

    # 4. max-Pc gives the OPPOSITE decision to Pc at the degraded covariance.
    ok4 = p["p_max"] > C.P_ACT > p["p_bad"]
    if not ok4:
        fails.append("4: max-Pc does not disagree with Pc at degraded sigma")

    print("\n[gen_conj] === the four claims ===")
    print("  1. Pc peaks at sigma %.1f m and falls on BOTH sides "
          "(%.3e at /20, %.3e at peak, %.3e at x20)"
          % (p["s_peak"], lo, p["p_peak"], hi))
    print("  2. degrade tracking %.1fx -> Pc %.3e -> %.3e, crosses %.0e"
          % (SIG_BAD / p["s_peak"], p["p_good"], p["p_bad"], C.P_ACT))
    print("  3. REVERSAL: ridge %.1fx better on all events, "
          "persistence %.1fx better on the notified ones"
          % (r["persistence"][0] / r["ridge"][0],
             r["ridge"][1] / r["persistence"][1]))
    print("  4. at sigma %.0f m: Pc says no-action (%.3e), "
          "max-Pc says act (%.3e)" % (SIG_BAD, p["p_bad"], p["p_max"]))
    print("     [measured, NOT claimed] sigma/d as a feature moves the "
          "notified error by %.1f%%"
          % (100 * (r["ridge_geom"][1] / r["ridge"][1] - 1)))
    print("     [measured, NOT claimed] reweighting x300 improves notified "
          "%.1fx but costs %.0fx on all events, and STILL loses to "
          "persistence by %.1fx"
          % (r["ridge"][1] / r["ridge_weighted"][1],
             r["ridge_weighted"][0] / r["ridge"][0],
             r["ridge_weighted"][1] / r["persistence"][1]))
    for m in fails:
        print("  FAIL " + m)
    if fails:
        raise SystemExit("[gen_conj] claims failed — nothing written.")
    print("  -> all four hold. writing plates.\n")


# ═════════════════════════════════════════════════════════════════════════════
#  drawing
# ═════════════════════════════════════════════════════════════════════════════
class Axes:
    def __init__(self, w, h, xlim, ylim, m=(18, 18, 18, 18)):
        self.img = Image.new("RGB", (w, h), CREAM)
        self.d = ImageDraw.Draw(self.img)
        self.xlim, self.ylim = xlim, ylim
        l, t, r, b = m[0], m[1], w - m[2], h - m[3]
        self.bx = (l, t, r, b)
        self.d.rectangle(self.bx, outline=GHOST, width=2)

    def X(self, x):
        l, _, r, _ = self.bx
        a, b = self.xlim
        return l + (r - l) * (np.asarray(x) - a) / float(b - a)

    def Y(self, y):
        _, t, _, b = self.bx
        a, c = self.ylim
        return b - (b - t) * (np.asarray(y) - a) / float(c - a)

    def hline(self, y, colour=GHOST, width=2, dash=True):
        l, _, r, _ = self.bx
        yy = float(self.Y(y))
        if not dash:
            self.d.line([l + 2, yy, r - 2, yy], fill=colour, width=width)
            return
        x = l + 4
        while x < r - 4:
            self.d.line([x, yy, min(x + 16, r - 4), yy], fill=colour,
                        width=width)
            x += 30

    def vline(self, x, colour=GHOST, width=2, dash=True):
        _, t, _, b = self.bx
        xx = float(self.X(x))
        if not dash:
            self.d.line([xx, t + 2, xx, b - 2], fill=colour, width=width)
            return
        y = t + 4
        while y < b - 4:
            self.d.line([xx, y, xx, min(y + 16, b - 4)], fill=colour,
                        width=width)
            y += 30

    def curve(self, xs, ys, colour=ACC, width=7):
        self.d.line([(float(self.X(a)), float(self.Y(b)))
                     for a, b in zip(xs, ys)], fill=colour, width=width,
                    joint="curve")

    def dot(self, x, y, colour=INK, r=11):
        px, py = float(self.X(x)), float(self.Y(y))
        self.d.ellipse([px - r, py - r, px + r, py + r], fill=colour)

    def bar(self, x, y, w, colour, y0=None):
        y0 = self.ylim[0] if y0 is None else y0
        top, base = float(self.Y(y)), float(self.Y(y0))
        self.d.rectangle([float(self.X(x - w)), top,
                          float(self.X(x + w)), base], fill=colour)


def geometry_plate(_):
    """Three panels: the same encounter, three qualities of tracking.

    COVARIANCE ELLIPSES, not a density field. The first version shaded the
    Gaussian as a continuous greyscale, and no display mapping of it could
    satisfy both the physics and GATE V's low-contrast check:

      gamma 0.25  honest picture, gate 0.23  (FAIL)
      gamma 0.09  gate 0.34 (pass), but panels two and three rendered almost
                  equally dark -- the picture then read as "more uncertainty,
                  more density", the exact opposite of dilution
      gamma 0.70  gate 0.31 (marginal pass), but panels two and three fell
                  BELOW the gate's ink threshold and vanished

    The density ratio across the panels is 1 : 0.056 : 1e-4. Four orders of
    magnitude cannot be shown as shade without either flattening the ends or
    losing them, so the knob was the wrong lever and the plate was redrawn.

    Rings are how conjunction geometry is actually drawn, they are crisp ink
    rather than soft gradient, and they say the same thing: the 1-sigma
    ellipse grows while the hard-body disk does not. In the third panel the
    1-sigma ellipse is eight times wider than the whole frame, so nothing is
    drawn but the disk -- and that emptiness is the point, not a gap.
    """
    W, H = 1560, 620
    pad, gap = 16, 18
    pw = (W - 2 * pad - 2 * gap) // 3
    ph = H - 2 * pad
    img = Image.new("RGB", (W, H), CREAM)
    half = 620.0                                  # metres shown each way
    sc = pw / (2.0 * half)
    for i, sig in enumerate((50.0, 212.1, SIG_BAD)):
        panel = Image.new("RGB", (pw, ph), CREAM)
        pd = ImageDraw.Draw(panel)
        cx, cy = pw / 2.0, ph / 2.0
        # 1, 2 and 3 sigma. Drawn into the panel's OWN image so anything
        # larger than the panel is clipped rather than bleeding into its
        # neighbour.
        # The hierarchy is carried by STROKE WEIGHT, not by paleness. A
        # ghost-grey outer ring sits just above GATE V's ink threshold and
        # drags the frame's mean ink colour toward the cream: with GHOST the
        # frame scored 0.302 against a 0.30 floor, which is the same
        # one-bad-encode-from-failing margin that cost Ep. 14 its verdict
        # card. Ink and soft at descending widths read the same.
        for k, (colour, wid) in enumerate(((INK, 7), (INK, 4), (SOFT, 3))):
            r = (k + 1) * sig * sc
            if r > (pw + ph):                     # far beyond the frame
                continue
            pd.ellipse([cx - r, cy - r, cx + r, cy + r], outline=colour,
                       width=wid)
        pd.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=INK)   # the mean
        dx = cx + D_EX * sc
        rad = max(C.HBR * sc, 5.0)
        pd.ellipse([dx - rad, cy - rad, dx + rad, cy + rad], fill=ACC)
        img.paste(panel, (pad + i * (pw + gap), pad))
    # NO per-panel border. Three ghost rectangles are three long runs of
    # pixels sitting just above GATE V's ink threshold, and they cost about
    # 0.02 of luminance separation for nothing -- the gaps already separate
    # the panels, and scenes.py frames the plate as a whole.
    return img


def dilution_plate(_):
    """Pc against the covariance scale. The shape IS the episode."""
    sig = np.geomspace(20.0, 2e5, 700)
    y = np.log10(np.maximum(C.pc(sig, D_EX), 1e-12))
    ax = Axes(1560, 780, (np.log10(20.0), np.log10(2e5)), (-12.0, -2.0))
    for yy in (-4, -6, -8, -10):
        ax.hline(yy, colour=FAINT, width=1)
    ax.hline(np.log10(C.P_ACT), colour=INK, width=3, dash=True)
    ax.curve(np.log10(sig), y, ACC, 7)
    k = int(np.argmax(y))
    ax.dot(np.log10(sig[k]), y[k], INK, 13)
    return ax.img


def flip_plate(p):
    """The same conjunction, two tracking solutions, opposite decisions."""
    ax = Axes(1560, 780, (0.0, 2.0), (-7.0, -2.0))
    for yy in (-3, -4, -5, -6):
        ax.hline(yy, colour=FAINT, width=1)
    ax.hline(np.log10(C.P_ACT), colour=INK, width=3, dash=True)
    ax.bar(0.62, np.log10(p["p_good"]), 0.17, INK, y0=-7.0)
    ax.bar(1.38, np.log10(p["p_bad"]), 0.17, ACC, y0=-7.0)
    return ax.img


def shrink_plate(p):
    """Risk against time to closest approach, for a handful of events.

    WHAT THIS PLATE ACTUALLY SHOWS, after measuring instead of assuming.
    The first version was drawn to show alerts BREAKING LATE -- quiet until
    the last message, then jumping. The population contains ZERO such events,
    and that is not an artefact: as the covariance shrinks below the miss
    distance, Pc falls. Better tracking almost always makes an alert DECAY.

    So the true structure is the one drawn here: nearly every conjunction
    fades toward the floor as the solution tightens (ghost), while the few
    that matter climb steadily from the start because their miss distance is
    small enough that the covariance is closing ON it rather than past it
    (terracotta). That is precisely why "assume it stays where it is" is such
    a strong forecast, and why the handful it gets wrong are the only ones
    anybody cares about.
    """
    final, risk = p["final"], p["ev"]["risk"]
    F = C.RISK_FLOOR
    # Climbers must START ON THE FLOOR, or the plate shows events that were
    # always dangerous rather than events that became so. Sorting by final
    # risk picks the most extreme, which are exactly the ones already
    # elevated at the first message; take a spread instead.
    climb = np.where((final > F + 1.5) & (risk[:, 0] <= F + 0.05))[0]
    climb = climb[np.argsort(final[climb])]
    if len(climb) >= 3:
        pick = (np.linspace(0.25, 0.95, 3) * (len(climb) - 1)).astype(int)
        climb = climb[pick]
    decay = np.where((final <= F + 1e-9) & (risk[:, 0] > F + 0.2))[0]

    ax = Axes(1560, 780, (C.T_GRID[0], 0.35), (-6.3, -1.0))
    for yy in (-2, -3, -4, -5, -6):
        ax.hline(yy, colour=FAINT, width=1)
    ax.vline(C.T_CUT, colour=GHOST, width=3)
    ax.hline(np.log10(C.P_ACT), colour=INK, width=3, dash=True)
    rng = np.random.default_rng(7)
    for i in rng.choice(decay, min(12, len(decay)), replace=False):
        ax.curve(C.T_GRID, np.clip(risk[i], -6.3, -1.0), GHOST, 3)
    for i in climb[:3]:
        ax.curve(C.T_GRID, np.clip(risk[i], -6.3, -1.0), ACC, 8)
    return ax.img


def bars_plate(p):
    """The reversal, as two panels that cannot share an axis.

    Left: every event. Right: only the events anybody was ever told about.
    Same two forecasters, opposite winners. The panels are scaled
    independently BECAUSE the two errors differ by two orders of magnitude --
    putting them on one axis would hide the right-hand panel entirely, which
    is the mistake the beat is about.
    """
    r = p["res"]
    W, H = 1560, 780
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    pad, gap = 18, 40
    pw = (W - 2 * pad - gap) // 2
    for panel, (a, b) in enumerate(((r["persistence"][0], r["ridge"][0]),
                                    (r["persistence"][1], r["ridge"][1]))):
        x0 = pad + panel * (pw + gap)
        ph = H - 2 * pad
        d.rectangle([x0, pad, x0 + pw, pad + ph], outline=GHOST, width=2)
        top = max(a, b) * 1.18
        for frac in (0.25, 0.5, 0.75):
            yy = pad + ph * (1 - frac)
            xx = x0 + 4
            while xx < x0 + pw - 4:
                d.line([xx, yy, min(xx + 14, x0 + pw - 4), yy], fill=FAINT,
                       width=1)
                xx += 28
        bw = pw * 0.26
        for j, (v, col) in enumerate(((a, INK), (b, ACC))):
            cx = x0 + pw * (0.3 + 0.4 * j)
            h = ph * (v / top)
            d.rectangle([cx - bw / 2, pad + ph - h, cx + bw / 2, pad + ph],
                        fill=col)
    return img


def maxpc_plate(p):
    """Pc dilutes; the scale-free bound does not."""
    sig = np.geomspace(20.0, 2e5, 700)
    y = np.log10(np.maximum(C.pc(sig, D_EX), 1e-12))
    ax = Axes(1560, 780, (np.log10(20.0), np.log10(2e5)), (-12.0, -2.0))
    for yy in (-4, -6, -8, -10):
        ax.hline(yy, colour=FAINT, width=1)
    ax.hline(np.log10(C.P_ACT), colour=INK, width=3, dash=True)
    ax.curve(np.log10(sig), y, ACC, 7)
    ax.curve([np.log10(20.0), np.log10(2e5)],
             [np.log10(p["p_max"])] * 2, INK, 7)
    ax.dot(np.log10(SIG_BAD), np.log10(p["p_bad"]), ACC, 14)
    ax.dot(np.log10(SIG_BAD), np.log10(p["p_max"]), INK, 14)
    return ax.img


def main():
    p = run()
    selfcheck(p)
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("geometry", geometry_plate), ("dilution", dilution_plate),
                     ("flip", flip_plate), ("shrink", shrink_plate),
                     ("bars", bars_plate), ("maxpc", maxpc_plate)):
        im = fn(p)
        im.save(os.path.join(OUT, name + ".png"))
        print("[gen_conj] %-9s %dx%d  ratio %.3f"
              % (name, im.size[0], im.size[1], im.size[1] / im.size[0]))


if __name__ == "__main__":
    main()
