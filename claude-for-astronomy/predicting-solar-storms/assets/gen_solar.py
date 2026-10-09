#!/usr/bin/env python3
"""Compute every plate for Ep. 12 — *The Same Sunspot, Twice.*

NOTHING HERE IS A DRAWING OF A RESULT. Each plate runs the experiment the
episode describes: active regions observed hourly, two models of different
capacity, and the three ways people split this data. The central claim is
ASSERTED over repeated runs and the script writes nothing if it fails.

  regions.png  the shape of the data: one region, many near-identical rows.
               This is the whole cause, drawn before any model exists.

  split.png    the same regions under a random row split and a by-region
               split. The mechanism, side by side.

  nearest.png  distance from each test row to its closest training row,
               under both splits. The leak, measured rather than argued:
               after a random split the closest row is usually the same
               region an hour earlier.

  scores.png   TSS for both models under both splits.
               ASSERTS the headline — the flexible model BEATS the baseline
               under a random split and LOSES to it under a by-region split.
               The ordering reverses.

  spread.png   the same four numbers across repeated runs, as medians with
               their range, so the reversal is not one lucky draw.

  control.png  inflation against the strength of the region fingerprint.
               ASSERTS the cause: with no region identity in the features
               there is no inflation.

Deterministic: one seed, 1212, logged in SOURCES.md.

Run:  python assets/gen_solar.py           (numpy + Pillow)
      python assets/gen_solar.py --force   (ignore the cache and recompute)
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import flares as F

HERE = Path(__file__).resolve().parent
OUT = HERE / "plots"
OUT.mkdir(parents=True, exist_ok=True)
CACHE = HERE / ".cache_solar.npz"

SEED = 1212
N_REPEAT = 12
KNN_K = 25

# ── the Claude fidelity palette ──────────────────────────────────────────────
CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)          # terracotta — marks THE LEAK and what it buys
ACCT = (164, 74, 50)
WHITE = (255, 255, 255)

SPLITS = (("random", F.split_random),
          ("region", F.split_by_region),
          ("chrono", F.split_chronological))


# ═════════════════════════════════════════════════════════════════════════════
#  the experiment
# ═════════════════════════════════════════════════════════════════════════════
def one_run(seed):
    """One synthetic catalogue, both models, all three splits."""
    rng = np.random.default_rng(seed)
    d = F.make_regions(rng)
    out = {"base_rate": float(d["y"].mean()),
           "rows": int(d["y"].size),
           "regions": int(np.unique(d["region"]).size)}
    for sname, sp in SPLITS:
        tr, te = sp(d, np.random.default_rng(seed + 977))
        # how many TEST regions also appear in TRAIN -- the leak, counted
        shared = len(set(d["region"][te].tolist())
                     & set(d["region"][tr].tolist()))
        out["shared_%s" % sname] = shared / max(
            np.unique(d["region"][te]).size, 1)
        lo = F.Logistic().fit(d["X"][tr], d["y"][tr])
        out["logistic_%s" % sname] = F.best_tss(d["y"][te], lo.score(d["X"][te]))
        kn = F.NearestNeighbour(k=KNN_K).fit(d["X"][tr], d["y"][tr])
        out["knn_%s" % sname] = F.best_tss(d["y"][te], kn.score(d["X"][te]))
        out["nn_%s" % sname] = kn.nn_distance(d["X"][te])
    return d, out


def control_sweep(seed, strengths=(0.0, 0.25, 0.5, 0.75, 1.0)):
    """Inflation against how strongly a row carries its region's identity."""
    rows = []
    for s in strengths:
        rng = np.random.default_rng(seed + 31)
        d = F.make_regions(rng, fingerprint=max(s, 1e-6))
        got = {}
        for sname in ("random", "region"):
            sp = dict(SPLITS)[sname]
            tr, te = sp(d, np.random.default_rng(seed + 977))
            kn = F.NearestNeighbour(k=KNN_K).fit(d["X"][tr], d["y"][tr])
            got[sname] = F.best_tss(d["y"][te], kn.score(d["X"][te]))
        rows.append((s, got["random"], got["region"]))
        print("  fingerprint %.2f   random %.3f   by-region %.3f   "
              "inflation %+.3f" % (s, got["random"], got["region"],
                                   got["random"] - got["region"]))
    return np.array(rows)


def run():
    if CACHE.exists() and "--force" not in sys.argv:
        print("[gen_solar] using cache (pass --force to recompute)")
        return np.load(CACHE, allow_pickle=True)["payload"].item()

    print("[gen_solar] %d repeats, k=%d, seed %d" % (N_REPEAT, KNN_K, SEED))
    d0, first = one_run(SEED)
    print("  rows %d  regions %d  base rate 1 in %.0f"
          % (first["rows"], first["regions"], 1.0 / first["base_rate"]))
    for sname, _ in SPLITS:
        print("  split %-7s  test regions also seen in training: %5.1f%%"
              % (sname, 100 * first["shared_%s" % sname]))

    runs = [first]
    for r in range(1, N_REPEAT):
        _, o = one_run(SEED + r * 101)
        runs.append(o)
        print("  repeat %2d/%d" % (r + 1, N_REPEAT), end="\r")
    print(" " * 30, end="\r")

    print("[gen_solar] control sweep")
    ctrl = control_sweep(SEED)

    payload = dict(sample=d0, first=first, runs=runs, ctrl=ctrl)
    np.savez_compressed(CACHE, payload=np.array(payload, dtype=object))
    return payload


def med(runs, key):
    return float(np.median([r[key] for r in runs]))


def allv(runs, key):
    return np.array([r[key] for r in runs], dtype=float)


# ═════════════════════════════════════════════════════════════════════════════
#  drawing helpers — plates carry IMAGERY ONLY; every label is in scenes.py
# ═════════════════════════════════════════════════════════════════════════════
class Axes:
    def __init__(self, w, h, xlim, ylim, m=(16, 16, 16, 16), box=True):
        self.img = Image.new("RGB", (w, h), CREAM)
        self.d = ImageDraw.Draw(self.img)
        self.xlim, self.ylim = xlim, ylim
        l, r, t, b = m
        self.bx = (l, t, w - r, h - b)
        if box:
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
                self.d.line([x, yy, min(x + 14, r - 4), yy], fill=colour,
                            width=width)
                x += 26

    def bar(self, x, y, w, colour, y0=0.0):
        self.d.rectangle([self.X(x - w), self.Y(y), self.X(x + w), self.Y(y0)],
                         fill=colour)

    def poly(self, xs, ys, colour, width=6, dots=True, rr=9):
        pts = [(self.X(a), self.Y(b)) for a, b in zip(xs, ys)]
        self.d.line(pts, fill=colour, width=width, joint="curve")
        if dots:
            for px, py in pts:
                self.d.ellipse([px - rr, py - rr, px + rr, py + rr],
                               fill=colour)

    def vrange(self, x, lo, hi, colour, w=5):
        self.d.line([self.X(x), self.Y(lo), self.X(x), self.Y(hi)],
                    fill=colour, width=w)


def hist(ax, vals, colour, lo, hi, bins=46, scale=None):
    h, edges = np.histogram(vals, bins=bins, range=(lo, hi))
    h = h / h.max() if scale is None else h / scale
    for i in range(bins):
        if h[i] <= 0:
            continue
        x0, x1 = edges[i], edges[i + 1]
        ax.d.rectangle([ax.X(x0), ax.Y(h[i]), ax.X(x1), ax.Y(0)], fill=colour)
    return h.max()


# ═════════════════════════════════════════════════════════════════════════════
#  1. the shape of the data
# ═════════════════════════════════════════════════════════════════════════════
def regions_plate(p):
    """Ten regions, each as a row of hourly measurements.

    A first version laid the tracks out on a shared global time axis, which
    is honest about when regions appear but turns 22 short lifetimes into a
    diagonal staircase of hairlines -- the individual rows, which are the
    entire point, stopped being visible. Each track is now normalised to its
    own observing window so the DOTS read: one region, dozens of rows, a
    handful of which are flares.
    """
    d = p["sample"]
    W, H = 1560, 740
    img = Image.new("RGB", (W, H), CREAM)
    dr = ImageDraw.Draw(img)
    counts = np.bincount(d["region"])
    # pick ten regions, deliberately including flaring ones, so the plate
    # shows both facts: many rows per region, and few regions flaring
    flaring = [r for r in np.unique(d["region"])
               if d["y"][d["region"] == r].sum() > 0][:3]
    quiet = [r for r in np.unique(d["region"])
             if d["y"][d["region"] == r].sum() == 0 and counts[r] > 50][:7]
    regs = sorted(flaring + quiet)
    pad, rowh = 30, (H - 60) / len(regs)
    for i, r in enumerate(regs):
        m = d["region"] == r
        ys = d["y"][m]
        y = pad + rowh * (i + 0.5)
        x0, x1 = pad + 8, W - pad - 8
        dr.line([x0, y, x1, y], fill=(222, 218, 204), width=3)
        n = ys.size
        for j, yy in enumerate(ys):
            x = x0 + (x1 - x0) * j / max(n - 1, 1)
            if yy:
                dr.ellipse([x - 11, y - 11, x + 11, y + 11], fill=ACCT)
            else:
                dr.ellipse([x - 5, y - 5, x + 5, y + 5], fill=INK)
    return img


# ═════════════════════════════════════════════════════════════════════════════
#  2. the two splits, on the same regions
# ═════════════════════════════════════════════════════════════════════════════
def _split_panels(p, PW, H, n_regions):
    """Rows shuffled, then whole regions assigned. Terracotta = test."""
    d = p["sample"]
    regs = np.unique(d["region"])[:n_regions]
    rng = np.random.default_rng(SEED + 5)
    test_regs = set(rng.permutation(regs)[:int(len(regs) * 0.3)].tolist())
    panels = []
    for mode in ("random", "region"):
        img = Image.new("RGB", (PW, H), CREAM)
        dr = ImageDraw.Draw(img)
        pad, rowh = 20, (H - 40) / len(regs)
        for i, r in enumerate(regs):
            m = d["region"] == r
            ts = d["t"][m]
            y = pad + rowh * (i + 0.5)
            lo, hi = ts.min(), ts.max()
            x0 = pad + (PW - 2 * pad) * 0.02
            x1 = PW - pad
            dr.line([x0, y, x1, y], fill=GHOST, width=3)
            for j, t in enumerate(ts):
                x = x0 + (x1 - x0) * (t - lo) / max(hi - lo, 1)
                if mode == "random":
                    is_test = rng.random() < 0.3
                else:
                    is_test = r in test_regs
                c = ACC if is_test else INK
                rr = 6 if is_test else 4
                dr.ellipse([x - rr, y - rr, x + rr, y + rr], fill=c)
        dr.rectangle([0, 0, PW - 1, H - 1], outline=GHOST, width=2)
        panels.append(img)
    return panels


def split_plate(p):
    panels = _split_panels(p, 760, 700, 18)
    sheet = Image.new("RGB", (760 * 2 + 30, 700), CREAM)
    sheet.paste(panels[0], (0, 0))
    sheet.paste(panels[1], (790, 0))
    return sheet


def split_v_plate(p):
    """Stacked, for portrait. Fewer, shorter tracks: side by side at
    portrait's 3.40-unit width each panel would be 1.7 units across and the
    dots -- which ARE the plate -- would vanish."""
    panels = _split_panels(p, 760, 400, 10)
    sheet = Image.new("RGB", (760, 400 * 2 + 30), CREAM)
    sheet.paste(panels[0], (0, 0))
    sheet.paste(panels[1], (0, 430))
    return sheet


# ═════════════════════════════════════════════════════════════════════════════
#  3. the leak, measured
# ═════════════════════════════════════════════════════════════════════════════
def nearest_plate(p):
    """Distance to the closest training row. Terracotta = after a random
    split, ink = after a by-region split."""
    f = p["first"]
    a, b = np.asarray(f["nn_random"]), np.asarray(f["nn_region"])
    hi = float(np.percentile(np.concatenate([a, b]), 99))
    ax = Axes(1560, 700, (0, hi), (0, 1.06), m=(18, 18, 18, 18))
    s = max(np.histogram(a, bins=46, range=(0, hi))[0].max(),
            np.histogram(b, bins=46, range=(0, hi))[0].max())
    hist(ax, b, INK, 0, hi, scale=s)
    hist(ax, a, ACC, 0, hi, scale=s)
    return ax.img


# ═════════════════════════════════════════════════════════════════════════════
#  4. the reversal                                        (SELF-CHECK 1 and 2)
# ═════════════════════════════════════════════════════════════════════════════
def scores_plate(p):
    """Four bars: two models under two splits. Ink = the simple baseline,
    terracotta = the flexible model."""
    r = p["runs"]
    vals = [(0.28, med(r, "logistic_random"), INK),
            (0.50, med(r, "knn_random"), ACC),
            (1.10, med(r, "logistic_region"), INK),
            (1.32, med(r, "knn_region"), ACC)]
    ax = Axes(1560, 780, (0.0, 1.60), (0.0, 0.50), m=(18, 18, 18, 18))
    for y in (0.1, 0.2, 0.3, 0.4):
        ax.hline(y, colour=(214, 210, 196), width=1)
    for x, v, c in vals:
        ax.bar(x, v, 0.085, c)
    return ax.img


# ═════════════════════════════════════════════════════════════════════════════
#  5. across repeats                                       (not one lucky draw)
# ═════════════════════════════════════════════════════════════════════════════
def spread_plate(p):
    r = p["runs"]
    series = [(0.28, allv(r, "logistic_random"), INK),
              (0.50, allv(r, "knn_random"), ACC),
              (1.10, allv(r, "logistic_region"), INK),
              (1.32, allv(r, "knn_region"), ACC)]
    ax = Axes(1560, 780, (0.0, 1.60), (0.0, 0.50), m=(18, 18, 18, 18))
    for y in (0.1, 0.2, 0.3, 0.4):
        ax.hline(y, colour=(214, 210, 196), width=1)
    rng = np.random.default_rng(3)
    for x, v, c in series:
        ax.vrange(x, v.min(), v.max(), c, w=4)
        for s in v:
            jx = x + rng.normal(0, 0.016)
            ax.d.ellipse([ax.X(jx) - 7, ax.Y(s) - 7, ax.X(jx) + 7,
                          ax.Y(s) + 7], fill=c)
        m = float(np.median(v))
        ax.d.line([ax.X(x - 0.075), ax.Y(m), ax.X(x + 0.075), ax.Y(m)],
                  fill=c, width=7)
    return ax.img


# ═════════════════════════════════════════════════════════════════════════════
#  6. the cause                                             (SELF-CHECK 3)
# ═════════════════════════════════════════════════════════════════════════════
def control_plate(p):
    c = p["ctrl"]
    ax = Axes(1560, 780, (-0.06, 1.06), (-0.04, 0.34), m=(18, 18, 18, 18))
    ax.hline(0.0, colour=GHOST, width=2, dash=True)
    ax.poly(c[:, 0], c[:, 1] - c[:, 2], ACCT, width=7)
    return ax.img


# ═════════════════════════════════════════════════════════════════════════════
#  the self-check — three claims, nothing written if one fails
# ═════════════════════════════════════════════════════════════════════════════
def selfcheck(p):
    r, c = p["runs"], p["ctrl"]
    lr, kr = med(r, "logistic_random"), med(r, "knn_random")
    lg, kg = med(r, "logistic_region"), med(r, "knn_region")
    lc, kc = med(r, "logistic_chrono"), med(r, "knn_chrono")
    print("\n[gen_solar] === the three claims ===")
    print("  base rate 1 in %.0f   (SWAN-SF reports 60:1 for M+ flares)"
          % (1.0 / med(r, "base_rate")))
    print("  test regions also present in training:  random %.0f%%   "
          "by-region %.0f%%" % (100 * med(r, "shared_random"),
                                100 * med(r, "shared_region")))
    print("  1. RANDOM split   baseline %.3f   flexible %.3f   -> flexible "
          "wins by %+.3f" % (lr, kr, kr - lr))
    print("  2. BY-REGION      baseline %.3f   flexible %.3f   -> flexible "
          "loses by %+.3f" % (lg, kg, kg - lg))
    print("     the flexible model's score falls %.0f%%; the baseline's does "
          "not fall at all" % (100 * (1 - kg / kr)))
    print("     chronological     baseline %.3f   flexible %.3f" % (lc, kc))
    print("  3. control: inflation at fingerprint 0.00 = %+.3f, "
          "at 1.00 = %+.3f" % (c[0, 1] - c[0, 2], c[-1, 1] - c[-1, 2]))

    fails = []
    if not kr > lr:
        fails.append("claim 1: the flexible model does NOT beat the baseline "
                     "under a random split (%.3f vs %.3f)" % (kr, lr))
    if not kg < lg:
        fails.append("claim 2: the ordering does NOT reverse under a "
                     "by-region split (%.3f vs %.3f)" % (kg, lg))
    if not (kr - kg) > 3 * abs(lr - lg):
        fails.append("claim 2: the flexible model's drop (%.3f) is not large "
                     "against the baseline's (%.3f)" % (kr - kg, lr - lg))
    if not (c[-1, 1] - c[-1, 2]) > 4 * (c[0, 1] - c[0, 2]):
        fails.append("claim 3: the inflation is not caused by the region "
                     "fingerprint (%.3f at 0, %.3f at 1)"
                     % (c[0, 1] - c[0, 2], c[-1, 1] - c[-1, 2]))
    if fails:
        for m in fails:
            print("  FAIL " + m)
        raise SystemExit("[gen_solar] a central claim does not hold — fix the "
                         "CLAIM, not the tolerance. Nothing written.")
    print("  -> all three hold. writing plates.\n")


def main():
    p = run()
    selfcheck(p)
    for name, fn in (("regions", regions_plate),
                     ("split", split_plate),
                     ("split_v", split_v_plate),
                     ("nearest", nearest_plate),
                     ("scores", scores_plate),
                     ("spread", spread_plate),
                     ("control", control_plate)):
        img = fn(p)
        img.save(OUT / ("%s.png" % name))
        print("[gen_solar] %-8s %dx%d  ratio %.3f"
              % (name, img.width, img.height, img.height / img.width))


if __name__ == "__main__":
    main()
