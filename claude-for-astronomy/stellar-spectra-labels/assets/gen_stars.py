#!/usr/bin/env python3
"""Compute every plate for Ep. 14 — *What The Model Would Say.*

NOTHING HERE IS A DRAWING OF A RESULT. Every plate runs the real chain:
synthetic stars, the spectra they produce, a physics pipeline that is
slightly wrong, and a genuine data-driven model (a quadratic polynomial in
the labels fitted per pixel and inverted at test time) trained on that
pipeline's output. The central claims are ASSERTED and the script writes
nothing if any fails.

  spectra.png   what the data is: three stars, three spectra, the lines
                deepening with metallicity.

  agree.png     the student against its TEACHER'S labels. Tight, 1:1, and
                this is the plot a paper shows.

  truth.png     the same stars against the TRUTH, which nobody normally has.
                The same model, four times worse, and sheared rather than
                scattered.

  bars.png      three numbers side by side: repeat-measurement precision,
                agreement with the labels, and error against truth.
                ASSERTS claim 1 — the precision understates the true error
                by more than a factor of ten.

  structure.png the error against temperature. A line, not a cloud.
                ASSERTS claim 2 — the error is structured, which is what
                makes it survive every check that compares averages.

  anchor.png    error against truth for three training sets: 500 precise
                biased labels, 120 noisy independent ones, and an unbiased
                teacher as the control.
                ASSERTS claim 3 — the systematic is the cause, and fewer
                noisier independent labels beat more precise biased ones.

Deterministic: one seed, 1414, logged in SOURCES.md.

Run:  python assets/gen_stars.py
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spectra as S

HERE = Path(__file__).resolve().parent
OUT = HERE / "plots"
OUT.mkdir(parents=True, exist_ok=True)

SEED = 1414
N_TRAIN, N_TEST = 500, 400
N_ANCHOR = 120
SNR = 100.0
BIAS = 0.18
FEH = 2                      # the label this episode is about

CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)
ACCT = (164, 74, 50)
WHITE = (255, 255, 255)


# ═════════════════════════════════════════════════════════════════════════════
#  the experiment
# ═════════════════════════════════════════════════════════════════════════════
def one(bias=BIAS, n_train=N_TRAIN, anchor=False, seed=SEED):
    rng = np.random.default_rng(seed)
    th_tr = S.draw_stars(rng, n_train)
    f_tr = S.observe(th_tr, rng, SNR)
    L_tr = (S.anchor_labels(th_tr, rng) if anchor
            else S.teacher_labels(th_tr, rng, bias=bias))
    cannon = S.Cannon().fit(L_tr, f_tr)

    th_te = S.draw_stars(rng, N_TEST)
    f_te = S.observe(th_te, rng, SNR)
    L_te = (S.anchor_labels(th_te, rng) if anchor
            else S.teacher_labels(th_te, rng, bias=bias))
    pred = cannon.predict(f_te)
    return dict(th=th_te, L=L_te, pred=pred, cannon=cannon)


def run():
    print("[gen_stars] main run: %d training stars, teacher bias %.2f dex/kK"
          % (N_TRAIN, BIAS))
    main = one()
    th, L, pred = main["th"], main["L"], main["pred"]

    # precision: the same stars, measured again with fresh noise
    rng = np.random.default_rng(SEED + 500)
    reps = np.array([main["cannon"].predict(S.observe(th[:150], rng, SNR))[:, FEH]
                     for _ in range(3)])
    precision = float(reps.std(axis=0).mean())

    e_label = pred[:, FEH] - L[:, FEH]
    e_truth = pred[:, FEH] - th[:, FEH]
    e_teach = L[:, FEH] - th[:, FEH]

    print("  precision (repeat measurement) %.4f dex" % precision)
    print("  vs teacher labels  rms %.4f" % np.std(e_label))
    print("  vs truth           rms %.4f  bias %+.4f" % (np.std(e_truth),
                                                         np.mean(e_truth)))
    print("  teacher vs truth   rms %.4f" % np.std(e_teach))
    cc = float(np.corrcoef(th[:, 0], e_truth)[0, 1])
    slope = float(np.polyfit((th[:, 0] - S.PIVOT[0]) / 1000.0, e_truth, 1)[0])
    print("  error vs Teff: correlation %.3f  slope %+.3f dex/kK" % (cc, slope))

    print("[gen_stars] control: an unbiased teacher")
    ctrl = one(bias=0.0)
    e_ctrl = ctrl["pred"][:, FEH] - ctrl["th"][:, FEH]
    print("  vs truth rms %.4f  corr %.3f"
          % (np.std(e_ctrl), np.corrcoef(ctrl["th"][:, 0], e_ctrl)[0, 1]))

    print("[gen_stars] fix: %d model-independent anchor stars" % N_ANCHOR)
    anch = one(n_train=N_ANCHOR, anchor=True)
    e_anch = anch["pred"][:, FEH] - anch["th"][:, FEH]
    print("  vs truth rms %.4f  corr %.3f"
          % (np.std(e_anch), np.corrcoef(anch["th"][:, 0], e_anch)[0, 1]))

    return dict(th=th, L=L, pred=pred, precision=precision,
                e_label=e_label, e_truth=e_truth, e_teach=e_teach,
                cc=cc, slope=slope, e_ctrl=e_ctrl, e_anch=e_anch)


# ═════════════════════════════════════════════════════════════════════════════
#  drawing — plates carry IMAGERY ONLY; every label lives in scenes.py
# ═════════════════════════════════════════════════════════════════════════════
class Axes:
    def __init__(self, w, h, xlim, ylim, m=(18, 18, 18, 18)):
        self.img = Image.new("RGB", (w, h), CREAM)
        self.d = ImageDraw.Draw(self.img)
        self.xlim, self.ylim = xlim, ylim
        l, r, t, b = m
        self.bx = (l, t, w - r, h - b)
        self.d.rectangle(self.bx, outline=GHOST, width=2)

    def X(self, x):
        l, _, r, _ = self.bx
        a, b = self.xlim
        return l + (r - l) * (x - a) / float(b - a)

    def Y(self, y):
        _, t, _, b = self.bx
        a, c = self.ylim
        return b - (b - t) * (y - a) / float(c - a)

    def hline(self, y, colour=GHOST, width=2, dash=False):
        l, _, r, _ = self.bx
        yy = self.Y(y)
        if not dash:
            self.d.line([l + 2, yy, r - 2, yy], fill=colour, width=width)
        else:
            x = l + 4
            while x < r - 4:
                self.d.line([x, yy, min(x + 16, r - 4), yy], fill=colour,
                            width=width)
                x += 30

    def diag(self, colour=GHOST, width=3):
        a = max(self.xlim[0], self.ylim[0])
        b = min(self.xlim[1], self.ylim[1])
        self.d.line([self.X(a), self.Y(a), self.X(b), self.Y(b)],
                    fill=colour, width=width)

    def points(self, xs, ys, colour=INK, r=5):
        for x, y in zip(xs, ys):
            px, py = self.X(x), self.Y(y)
            self.d.ellipse([px - r, py - r, px + r, py + r], fill=colour)

    def line(self, xs, ys, colour=ACCT, width=7):
        self.d.line([(self.X(a), self.Y(b)) for a, b in zip(xs, ys)],
                    fill=colour, width=width, joint="curve")

    def bar(self, x, y, w, colour, y0=0.0):
        top, base = self.Y(y), self.Y(y0)
        if abs(top - base) < 5:
            self.d.rectangle([self.X(x - w), base - 5, self.X(x + w), base],
                             fill=colour)
        else:
            self.d.rectangle([self.X(x - w), top, self.X(x + w), base],
                             fill=colour)


def spectra_plate(_):
    """Three stars at the same temperature and gravity, different metals."""
    W, H = 1560, 700
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    rng = np.random.default_rng(SEED + 3)
    rows = [(-0.90, SOFT), (-0.25, INK), (0.35, ACCT)]
    pad = 22
    rh = (H - 2 * pad) / 3.0
    # Normalise to the ACTUAL flux range across all three stars. A fixed
    # 0.3-1.0 window clipped the metal-rich spectrum, whose deepest lines go
    # below 0.3 -- and that spectrum having the deepest lines is the entire
    # point of the plate.
    spec = [S.observe(np.array([[5200.0, 2.8, feh]]), rng, SNR)[0]
            for feh, _ in rows]
    lo = min(f.min() for f in spec) - 0.02
    hi = max(f.max() for f in spec) + 0.02
    for i, ((feh, colour), f) in enumerate(zip(rows, spec)):
        y0 = pad + rh * i
        base = y0 + rh * 0.90
        amp = rh * 0.78
        pts = [(pad + (W - 2 * pad) * k / (S.NPIX - 1.0),
                base - amp * (f[k] - lo) / (hi - lo)) for k in range(S.NPIX)]
        d.line(pts, fill=colour, width=3, joint="curve")
    d.rectangle([0, 0, W - 1, H - 1], outline=GHOST, width=2)
    return img


def _scatter(xs, ys, lim, colour, diag=True):
    ax = Axes(1560, 780, lim, lim)
    if diag:
        ax.diag()
    ax.points(xs, ys, colour=colour, r=5)
    return ax.img


def agree_plate(p):
    lim = (-1.35, 0.75)
    return _scatter(p["L"][:, FEH], p["pred"][:, FEH], lim, INK)


def truth_plate(p):
    lim = (-1.35, 0.75)
    return _scatter(p["th"][:, FEH], p["pred"][:, FEH], lim, ACC)


def bars_plate(p):
    vals = [(0.55, p["precision"], INK),
            (1.50, float(np.std(p["e_label"])), INK),
            (2.45, float(np.std(p["e_truth"])), ACC)]
    ax = Axes(1560, 780, (0.0, 3.0), (0.0, 0.155))
    for y in (0.04, 0.08, 0.12):
        ax.hline(y, colour=(214, 210, 196), width=1)
    for x, v, c in vals:
        ax.bar(x, v, 0.26, c)
    return ax.img


def structure_plate(p):
    th, e = p["th"], p["e_truth"]
    ax = Axes(1560, 780, (3900, 6600), (-0.34, 0.34))
    ax.hline(0.0, colour=GHOST, width=2, dash=True)
    ax.points(th[:, 0], e, colour=INK, r=5)
    xs = np.array([3950.0, 6550.0])
    ax.line(xs, p["slope"] * (xs - S.PIVOT[0]) / 1000.0 + float(np.mean(e))
            - p["slope"] * (np.mean(th[:, 0]) - S.PIVOT[0]) / 1000.0, ACCT)
    return ax.img


def anchor_plate(p):
    vals = [(0.55, float(np.std(p["e_truth"])), ACC),
            (1.50, float(np.std(p["e_anch"])), INK),
            (2.45, float(np.std(p["e_ctrl"])), SOFT)]
    ax = Axes(1560, 780, (0.0, 3.0), (0.0, 0.155))
    for y in (0.04, 0.08, 0.12):
        ax.hline(y, colour=(214, 210, 196), width=1)
    for x, v, c in vals:
        ax.bar(x, v, 0.26, c)
    return ax.img


# ═════════════════════════════════════════════════════════════════════════════
#  the self-check
# ═════════════════════════════════════════════════════════════════════════════
def selfcheck(p):
    prec = p["precision"]
    s_lab = float(np.std(p["e_label"]))
    s_tru = float(np.std(p["e_truth"]))
    s_ctl = float(np.std(p["e_ctrl"]))
    s_anc = float(np.std(p["e_anch"]))
    print("\n[gen_stars] === the three claims ===")
    print("  1. precision %.4f   vs truth %.4f   -> understated %.1fx"
          % (prec, s_tru, s_tru / prec))
    print("     agreement with its own labels %.4f (%.1fx tighter than truth)"
          % (s_lab, s_tru / s_lab))
    print("  2. the error is a TREND: correlation %.3f, slope %+.3f dex/kK"
          % (p["cc"], p["slope"]))
    print("  3. control (unbiased teacher) %.4f   anchored (%d stars) %.4f"
          % (s_ctl, N_ANCHOR, s_anc))

    fails = []
    if not s_tru / prec > 10.0:
        fails.append("claim 1: the quoted precision does not badly understate "
                     "the true error (%.4f vs %.4f, %.1fx)"
                     % (prec, s_tru, s_tru / prec))
    if not s_tru / s_lab > 3.0:
        fails.append("claim 1: the model does not reproduce its labels much "
                     "more tightly than the truth (%.4f vs %.4f)"
                     % (s_lab, s_tru))
    if not abs(p["cc"]) > 0.90:
        fails.append("claim 2: the error is not a trend in temperature "
                     "(correlation %.3f)" % p["cc"])
    if not (s_ctl < 0.03 and s_tru / s_ctl > 4.0):
        fails.append("claim 3: removing the teacher's bias does not remove "
                     "the error (%.4f against %.4f)" % (s_ctl, s_tru))
    if not s_anc < 0.5 * s_tru:
        fails.append("claim 3: a small model-independent anchor does not beat "
                     "a large biased training set (%.4f against %.4f)"
                     % (s_anc, s_tru))
    if fails:
        for m in fails:
            print("  FAIL " + m)
        raise SystemExit("[gen_stars] a central claim does not hold — fix the "
                         "CLAIM, not the tolerance. Nothing written.")
    print("  -> all three hold. writing plates.\n")


def main():
    p = run()
    selfcheck(p)
    for name, fn in (("spectra", spectra_plate),
                     ("agree", agree_plate),
                     ("truth", truth_plate),
                     ("bars", bars_plate),
                     ("structure", structure_plate),
                     ("anchor", anchor_plate)):
        img = fn(p)
        img.save(OUT / ("%s.png" % name))
        print("[gen_stars] %-10s %dx%d  ratio %.3f"
              % (name, img.width, img.height, img.height / img.width))


if __name__ == "__main__":
    main()
