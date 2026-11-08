"""gen_ao.py -- the experiment, its self-check, and the five plates.

Ep. 16, *predictive-adaptive-optics*.

Run:  python -I assets/gen_ao.py            (~7 min: the telemetry dominates)
      python -I assets/gen_ao.py --cache DIR  reuse/stash modal telemetry

SEVEN claims are ASSERTED.  If any fails, NOTHING is written -- a plate
that disagrees with the narration is worse than no plate.

Plates carry IMAGERY ONLY.  No text, no tick labels, no legend: every
label on screen is placed by scenes.py OUTSIDE the plate, because a plate
is an ImageMobject and the layout gate is nearly blind to it.
"""
import argparse
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ao  # noqa: E402

OUT = os.path.join(HERE, "plots")

CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)
ACCT = (164, 74, 50)
FAINT = (214, 210, 196)

SEED = 1616
TEL_SEED0 = 10             # first atmosphere seed; segments are TEL_SEED0+s
N_SEG = 12                 # independent atmospheres
N_TRAIN, N_VAL = 8, 2      # the rest is test
DELAY = 2                  # ms -- Keck II measured 1.7 ms on its PyWFS
TAPS = 24                  # 24 ms of modal history
NOISE_REAL = 0.05          # rad RMS per mode: the realistic WFS regime
NOISES = (0.0, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20)
TAUS_MS = (1, 2, 3, 4, 6, 8, 12)
DELAYS = (1, 2, 3, 4, 6, 8, 12)

# Keck's published on-sky improvement in total SH-WFS residual
KECK_TOTAL_GAIN = 0.20

LAYERS = {
    "L1": [(1.0, 2, 0)],                                  # 10 m/s
    "L2": [(0.6, 2, 0), (0.4, -4, 0)],                    # 10, 20 the other way
    "L3": [(0.5, 2, 0), (0.3, 4, 0), (0.2, -1, 0)],       # 10, 20, 5 reversed
}


# ═════════════════════════════════════════════════════════════════════════════
#  the experiment
# ═════════════════════════════════════════════════════════════════════════════
def telemetry(cache=None):
    basis, mask = ao.zernike_basis(ao.N_MODES, int(ao.D_TEL / ao.PIX / ao.SUB))
    out = {}
    for name, layers in LAYERS.items():
        path = os.path.join(cache, name + ".npy") if cache else None
        if path and os.path.exists(path):
            segs = np.load(path)
        else:
            segs = np.stack([ao.build_telemetry(TEL_SEED0 + s, layers,
                                                basis, mask)
                             for s in range(N_SEG)])
            if path:
                os.makedirs(cache, exist_ok=True)
                np.save(path, segs)
        out[name] = [segs[i] for i in range(segs.shape[0])]
        print("  telemetry %s: %d x %d frames, %.1f rad^2 in band"
              % (name, segs.shape[0], segs.shape[1],
                 float(segs[0].var(axis=0).sum())))
    return out, basis, mask


def split(segs):
    return (segs[:N_TRAIN], segs[N_TRAIN:N_TRAIN + N_VAL],
            segs[N_TRAIN + N_VAL:])


def run(cache=None):
    p = {}
    print("[gen_ao] the air, the lag, the predictor\n")

    # --- 1. the shift operator is exactly a translation ------------------
    # (NSUB-1)/NSUB of a pixel, then one more 1/NSUB, must equal a whole
    # pixel roll.  The sign of this operator was wrong once and turned the
    # pupil's track into a zigzag; nothing else caught it.
    rng = np.random.default_rng(SEED)
    small = ao.phase_screen(rng, nx=512, ny=256)
    once = ao.subpixel_copies(ao.subpixel_copies(small)[ao.NSUB - 1])[1]
    p["shift_err"] = float(np.abs(once - np.roll(small, -1, axis=1)).max()
                           / small.std())
    print("  translation operator: %d sub-steps == roll(1 px) to %.1e"
          % (ao.NSUB, p["shift_err"]))

    # --- 2. the textbook law, from the spectrum --------------------------
    taus = np.array(TAUS_MS) * 1e-3
    kol = ao.lag_spectral(taus, pupil=False, l0=None)
    p["kol"] = kol
    p["kol_exp"], _ = ao.fit_exponent(taus, kol)
    p["kol_tau0"] = ao.lag_spectral(ao.TAU0, pupil=False, l0=None)
    p["vk"] = ao.lag_spectral(taus, pupil=True, l0=ao.L0)
    p["vk_exp"], _ = ao.fit_exponent(taus, p["vk"])
    print("  full phase, Kolmogorov : exponent %.6f   sigma^2(tau0) %.4f rad^2"
          % (p["kol_exp"], p["kol_tau0"]))
    print("  full phase, vK + pupil : exponent %.4f" % p["vk_exp"])
    print("  tau0 = 0.314 r0/v = %.2f ms ; 6.88 * 0.314^(5/3) = %.4f"
          % (ao.TAU0 * 1e3, 6.88 * 0.314 ** (5.0 / 3.0)))

    # the delay as a DISTANCE
    p["keck_delay"] = 1.7e-3
    p["slide_m"] = ao.WIND * p["keck_delay"]
    p["slide_frac"] = p["slide_m"] / ao.R0_500
    p["keck_s2"] = float(ao.lag_spectral(p["keck_delay"], pupil=False, l0=None))
    print("  at Keck's measured 1.7 ms and %.0f m/s the air slid %.1f cm"
          % (ao.WIND, p["slide_m"] * 100))
    print("     = %.0f%% of r0 ; full-phase sigma^2 = %.4f rad^2 at 500 nm"
          % (p["slide_frac"] * 100, p["keck_s2"]))

    # --- 3. screens agree with the spectral integral ---------------------
    screens, copies = [], []
    for s in range(2):
        scr = ao.phase_screen(np.random.default_rng(SEED + 70 + s))
        screens.append(scr)
        copies.append(ao.subpixel_copies(scr))
    big = [4, 6, 8, 12]           # below 4 ms the 2 cm grid truncates Nyquist
    meas = ao.lag_variance(copies, big)
    pred = ao.lag_spectral(np.array(big) * 1e-3, pupil=True, l0=ao.L0)
    p["screen_ratio"] = float(np.mean(meas / pred))
    print("  screens vs spectral integral (tau >= 4 ms): ratio %.4f"
          % p["screen_ratio"])
    p["sf_r"] = [2, 4, 8, 16, 32, 64]
    p["sf"] = ao.structure_function(screens, p["sf_r"])
    p["var_measured"] = ao.pupil_var_measured(screens)
    del screens, copies

    # --- 4. the correctable band -----------------------------------------
    tel, basis, mask = telemetry(cache)
    tr, va, te = split(tel["L1"])

    band = []
    for d in DELAYS:
        r = ao.eval_predictors(tr, va, te, delay=d, taps=2, noise_rad=0.0,
                               per_mode=False)
        band.append(r["zero"])
    p["band"] = np.array(band)
    p["band_exp"], _ = ao.fit_exponent(DELAYS, band)
    print("\n  correctable band (%d modes): lag error exponent %.3f"
          % (ao.N_MODES, p["band_exp"]))
    print("     full phase is %.3f -- band-limited is SMOOTH, and smooth is"
          % p["vk_exp"])
    print("     what a linear predictor can extrapolate.")

    # How much of the servo-lag error can a deformable mirror even reach?
    # Both sides are von Karman, pupil-averaged, piston-removed, 10 m/s, so
    # this is apples to apples.
    i2 = DELAYS.index(DELAY)
    j2 = TAUS_MS.index(DELAY)
    p["band_at2"] = float(p["band"][i2])
    p["full_at2"] = float(p["vk"][j2])
    p["band_frac"] = p["band_at2"] / p["full_at2"]
    p["var_total"] = ao.pupil_variance()
    p["var_band"] = float(np.mean([s.var(axis=0).sum() for s in tel["L1"]]))
    p["band_var_frac"] = p["var_band"] / p["var_measured"]
    print("  at %d ms: full-phase lag %.4f rad^2, of which only %.4f (%.0f%%)"
          % (DELAY, p["full_at2"], p["band_at2"], p["band_frac"] * 100))
    print("     lies in the %d modes a mirror can shape. The rest is fitting"
          % ao.N_MODES)
    print("     error and no controller, predictive or not, can touch it.")
    print("  [context, NOT claimed on screen] pupil variance %.0f rad^2"
          % p["var_measured"])
    print("     measured vs %.0f from the ideal spectrum, %.0f in band."
          % (p["var_total"], p["var_band"]))
    print("     The in-band SHARE (%.0f%%) swings with realisation because a"
          % (p["band_var_frac"] * 100))
    print("     single screen's lowest modes scatter hard -- too wobbly to")
    print("     put on screen. The 16%% drift share is the stable one: its")
    print("     numerator averages 12 atmospheres and its denominator is an")
    print("     exact integral the screens reproduce to 2%%.")

    # --- 5. taps: how far back is worth looking --------------------------
    p["taps_n"] = (1, 2, 4, 8, 16, 24, 32, 48)
    p["taps_v"] = [ao.eval_predictors(tr, va, te, delay=DELAY, taps=t,
                                      noise_rad=NOISE_REAL,
                                      per_mode=False)["eof"]
                   for t in p["taps_n"]]
    print("  taps sweep at noise %.2f: " % NOISE_REAL
          + " ".join("%d:%.4f" % (t, v) for t, v in zip(p["taps_n"], p["taps_v"])))

    # --- 6. noise is the binding constraint ------------------------------
    p["noise"] = {}
    for name in LAYERS:
        a, b, c = split(tel[name])
        rows = []
        for nz in NOISES:
            r = ao.eval_predictors(a, b, c, delay=DELAY, taps=TAPS,
                                   noise_rad=nz, per_mode=True)
            rows.append(r)
            print("   %s noise %5.3f  zero %.4f  space %.4f (%5.2fx)  "
                  "time %.4f (%5.2fx)  EOF %.4f (%6.2fx)"
                  % (name, nz, r["zero"], r["space"], r["gain_space"],
                     r["time"], r["gain_time"], r["eof"], r["gain_eof"]))
        p["noise"][name] = rows

    p["g_real"] = {k: [r for r, nz in zip(p["noise"][k], NOISES)
                       if nz == NOISE_REAL][0] for k in LAYERS}

    # --- 7. the bridge to the on-sky number ------------------------------
    g = p["g_real"]["L1"]["gain_eof"]
    p["lag_share"] = KECK_TOTAL_GAIN / (1.0 - 1.0 / g)
    g3 = p["g_real"]["L3"]["gain_eof"]
    p["lag_share3"] = KECK_TOTAL_GAIN / (1.0 - 1.0 / g3)
    print("\n  a %.1fx cut in the lag term shows up as Keck's published %.0f%%"
          % (g, KECK_TOTAL_GAIN * 100))
    print("     improvement in TOTAL residual iff lag is %.0f%% of the budget"
          % (p["lag_share"] * 100))
    print("     (%.0f%% for the three-layer gain of %.1fx)"
          % (p["lag_share3"] * 100, g3))
    return p


def selfcheck(p):
    ok = True

    def claim(name, cond, detail):
        nonlocal ok
        print("   %-46s %s   %s" % (name, "ok " if cond else "FAIL", detail))
        ok = ok and bool(cond)

    print("\n[gen_ao] the seven claims")
    claim("translation operator is exact",
          p["shift_err"] < 1e-5, "rel err %.1e" % p["shift_err"])
    claim("Kolmogorov lag exponent is 5/3",
          abs(p["kol_exp"] - 5.0 / 3.0) < 0.005, "%.6f" % p["kol_exp"])
    claim("sigma^2(tau0) = 1 rad^2",
          abs(p["kol_tau0"] - 1.0) < 0.02, "%.4f rad^2" % p["kol_tau0"])
    claim("screens reproduce the spectral integral",
          0.90 < p["screen_ratio"] < 1.10, "ratio %.4f" % p["screen_ratio"])
    claim("in-band lag error goes as tau^2, not tau^(5/3)",
          1.90 < p["band_exp"] < 2.10, "%.3f" % p["band_exp"])
    g1 = p["g_real"]["L1"]["gain_eof"]
    g2 = p["g_real"]["L2"]["gain_eof"]
    g3 = p["g_real"]["L3"]["gain_eof"]
    claim("prediction still wins at realistic noise",
          g1 > 8.0 and g3 > 3.0, "%.2fx (1 layer) %.2fx (3 layers)" % (g1, g3))
    claim("more layers cost the predictor",
          g1 > g2 > g3 * 0.95, "%.2f > %.2f > %.2f" % (g1, g2, g3))
    claim("looking BACK beats looking ACROSS",
          all(p["g_real"][k]["gain_time"] > p["g_real"][k]["gain_space"]
              for k in LAYERS),
          " ".join("%s %.1f/%.1f" % (k, p["g_real"][k]["gain_time"],
                                     p["g_real"][k]["gain_space"])
                   for k in LAYERS))
    if not ok:
        raise SystemExit("[gen_ao] claims failed -- nothing written.")
    print("  -> all hold. writing plates.\n")


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

    def X(self, x):
        l, _, r, _ = self.bx
        a, b = self.xlim
        return l + (r - l) * (np.asarray(x, float) - a) / float(b - a)

    def Y(self, y):
        _, t, _, b = self.bx
        a, c = self.ylim
        return b - (b - t) * (np.asarray(y, float) - a) / float(c - a)

    def hline(self, y, colour=GHOST, width=2, dash=True):
        l, _, r, _ = self.bx
        yy = float(self.Y(y))
        if not dash:
            self.d.line([l + 2, yy, r - 2, yy], fill=colour, width=width)
            return
        x = l + 4
        while x < r - 4:
            self.d.line([x, yy, min(x + 16, r - 4), yy], fill=colour, width=width)
            x += 30

    def vline(self, x, colour=GHOST, width=2, dash=True):
        _, t, _, b = self.bx
        xx = float(self.X(x))
        if not dash:
            self.d.line([xx, t + 2, xx, b - 2], fill=colour, width=width)
            return
        y = t + 4
        while y < b - 4:
            self.d.line([xx, y, xx, min(y + 16, b - 4)], fill=colour, width=width)
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


W, H = 1560, 780


def lawlog_plate(p):
    """
    sigma^2 against delay, log-log.  Two slopes on one frame: the full
    phase at 5/3 (terracotta) and the correctable band at ~2 (ink).  The
    whole episode is the gap between them.
    """
    lx = (math.log10(0.85), math.log10(14.0))
    ly = (-2.3, 0.75)
    ax = Axes(W, H, lx, ly, m=(26, 24, 26, 26))

    ax.vline(math.log10(ao.TAU0 * 1e3), colour=GHOST, width=3)
    ax.hline(0.0, colour=GHOST, width=3)

    # Only TWO curves.  The pure-Kolmogorov line used to be drawn here as
    # well and sat exactly on top of the von Karman one -- visually a
    # shadow, and it left the connector's top end ambiguous.  The textbook
    # verification (exponent 5/3, sigma^2(tau0) = 0.997) is a NUMBER; it
    # does not need its own curve.
    t = np.array(TAUS_MS, float)
    ax.curve(np.log10(t), np.log10(p["vk"]), ACC, 9)
    d = np.array(DELAYS, float)
    ax.curve(np.log10(d), np.log10(p["band"]), INK, 9)

    # THE SUBJECT OF THIS PLATE IS THE VERTICAL GAP, not the slopes.  The
    # first version drew the two curves alone and they read as parallel --
    # true (1.60 vs 1.99 is only a 20 % difference in screen slope) but
    # beside the point.  The connector at the operating delay says what the
    # beat says: most of the servo-lag error is out of the mirror's reach.
    x2 = float(ax.X(math.log10(float(DELAY))))
    yf = float(ax.Y(math.log10(p["full_at2"])))
    yb = float(ax.Y(math.log10(p["band_at2"])))
    ax.d.line([x2, yf, x2, yb], fill=ACCT, width=11)
    for yy in (yf, yb):
        ax.d.line([x2 - 26, yy, x2 + 26, yy], fill=ACCT, width=9)

    return ax.img


def slide_plate(p):
    """
    Why the lag is a DISTANCE.  A real cut through the simulated screen:
    ink is the wavefront NOW, terracotta is the one the mirror is still
    holding -- the same curve, slid by v*tau = 1.7 cm.  Below, r0 and that
    slide as rules from a common left edge, so the ratio is the picture.

    Two earlier versions were wrong.  A full-bleed greyscale patch with
    two boxes on it dropped its scale rules off the bottom edge and was
    the exact mid-grey shape that failed GATE V on Ep. 15's B04.  Adding
    the residual at x10 under the pair then overflowed its band and ran
    through the rules -- and it was a second idea besides.  What is left
    says one thing: the air moved, and here is how far against the scale
    that matters.
    """
    ph, pw = 470, W
    span_m = 0.90                       # metres across the plate (6 r0)
    fine = 0.002                        # 2 mm: fine enough for a 1.7 cm
    nx, ny = 2048, 256                  # slide, coarse enough to read
    rng = np.random.default_rng(SEED + 5)
    scr = ao.phase_screen(rng, nx=nx, ny=ny, pix=fine).astype(np.float64)

    need = int(round(span_m / fine))
    off = int(round(p["slide_m"] / fine))
    x0 = (nx - need - off) // 2
    row = scr[ny // 2]
    now = row[x0 + off:x0 + off + need]
    held = row[x0:x0 + need]                     # the same air, 1.7 cm back
    now, held = now - now.mean(), held - held.mean()

    img = Image.new("RGB", (pw, ph), CREAM)
    d = ImageDraw.Draw(img)
    xs = np.linspace(28, pw - 28, need)

    top, bot = 34, 436
    amp = max(np.abs(now).max(), np.abs(held).max())

    def ymap(v):
        return (top + bot) / 2.0 - (v / amp) * (bot - top) / 2.0 * 0.94

    d.line(list(zip(xs, ymap(held))), fill=ACC, width=9, joint="curve")
    d.line(list(zip(xs, ymap(now))), fill=INK, width=9, joint="curve")
    # The r0 / slide scale rules used to live down here.  They moved OUT to
    # scenes.py as real Manim mobjects: labelling a rule drawn inside the
    # plate would have put text in the plate's interior, which GATE B cannot
    # see at all (it only checks the plate's FRAME).  Drawn in Manim they
    # are fully inspected, and they can be sized per aspect.
    return img


def noise_plate(p):
    """Gain over the zero-order hold against measurement noise, per layer count."""
    # Top of the axis is log10(60), not log10(420): the largest plotted
    # gain is 47x, and an axis sized for a number nobody draws leaves the
    # upper third of the frame empty (FILL-THE-CANVAS).
    # Only ONE layer and THREE are drawn.  Two layers lands within 10 % of
    # three (5.24 vs 4.82) and the curves simply tangle; the full table is
    # in FACTCHECK.md.
    lx = (math.log10(0.004), math.log10(0.26))
    ly = (0.0, math.log10(60.0))
    ax = Axes(W, H, lx, ly, m=(26, 24, 26, 26))
    ax.vline(math.log10(NOISE_REAL), colour=GHOST, width=3)
    ax.hline(0.0, colour=GHOST, width=3)

    nz = np.array([n for n in NOISES if n > 0], float)
    for name, colour, wid in (("L1", ACC, 9), ("L3", INK, 9)):
        g = [r["gain_eof"] for r, n in zip(p["noise"][name], NOISES) if n > 0]
        ax.curve(np.log10(nz), np.log10(g), colour, wid)
        ax.dot(math.log10(NOISE_REAL),
               math.log10(p["g_real"][name]["gain_eof"]), colour, 13)
    return ax.img


def decomp_plate(p):
    """
    Where the gain comes from: looking ACROSS the pupil, looking BACK in
    time, or both.  Two groups (one layer, three layers) of three bars.
    """
    # Log axis whose FLOOR is gain = 1, so every bar is measured from "no
    # improvement" and the axis itself is the baseline.
    #
    # Two earlier attempts were worse.  Log with bars from gain 0 made the
    # space-only bar 5 % of the frame -- the Ep. 14 invisible-mark defect.
    # Linear with a separate rule at 1 was worse still: bars run from 0, so
    # the rule CUT THROUGH them and a 1.2x gain read as mostly below the
    # line, i.e. as worse than doing nothing. On a log floor at 1 the short
    # bars are ~45-60 px tall and say exactly what they mean.
    ax = Axes(W, H, (0.0, 1.0), (0.0, math.log10(13.0)), m=(26, 24, 26, 26))
    groups = (("L1", 0.255), ("L3", 0.745))
    keys = (("gain_space", SOFT), ("gain_time", ACC), ("gain_eof", INK))
    for name, cx in groups:
        for k, (key, colour) in enumerate(keys):
            g = max(float(p["g_real"][name][key]), 1.0)
            ax.bar(cx + (k - 1) * 0.145, math.log10(g), 0.062, colour)
    return ax.img


def budget_plate(p):
    """
    The bridge to the on-sky number.  Total residual improvement against
    the share of the error budget that servo lag owns, for the measured
    in-band gain.  Keck's published 20 % is the horizontal rule.
    """
    # Two STACKED error budgets, before and after prediction.  Terracotta
    # is the servo-lag slice, soft is everything a predictor cannot touch
    # (fitting error, noise, calibration, vibration).  The lag slice very
    # nearly vanishes; the bar barely shortens.  That gap between the two
    # readings IS Keck's "20 % better residuals, comparable Strehl".
    #
    # This replaced a line plot of total-improvement against lag share.
    # That version drew two near-parallel lines through a crosshair -- an
    # arithmetic identity rendered as a graph, teaching nothing the
    # narration did not already say.
    phi = p["lag_share"]
    g = p["g_real"]["L1"]["gain_eof"]
    ax = Axes(W, H, (0.0, 1.0), (0.0, 1.12), m=(26, 24, 26, 26))
    ax.hline(1.0, colour=GHOST, width=3)
    ax.hline(1.0 - KECK_TOTAL_GAIN, colour=GHOST, width=3)

    for cx, lag in ((0.30, phi), (0.70, phi / g)):
        ax.bar(cx, 1.0 - phi, 0.115, SOFT, y0=0.0)
        ax.bar(cx, 1.0 - phi + lag, 0.115, ACC, y0=1.0 - phi)
    return ax.img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=None)
    args = ap.parse_args()

    p = run(args.cache)
    selfcheck(p)
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("lawlog", lawlog_plate), ("slide", slide_plate),
                     ("noise", noise_plate), ("decomp", decomp_plate),
                     ("budget", budget_plate)):
        im = fn(p)
        im.save(os.path.join(OUT, name + ".png"))
        print("  wrote %-8s %s" % (name, im.size))


if __name__ == "__main__":
    main()
