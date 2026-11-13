"""gen_sched.py -- the experiment, its self-check, and the five plates.

Ep. 17, *scheduling-the-night*.

Run:  python -I assets/gen_sched.py          (~2 min: the ILP dominates)

SIX claims are ASSERTED.  If any fails, NOTHING is written -- a plate that
disagrees with the narration is worse than no plate.

Plates carry IMAGERY ONLY.  No text, no tick labels, no legend: every label
on screen is placed by scenes.py OUTSIDE the plate, because a plate is an
ImageMobject and the layout gate is nearly blind to its interior.
"""
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sched as S  # noqa: E402

OUT = os.path.join(HERE, "plots")

CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)
ACCT = (164, 74, 50)
FAINT = (214, 210, 196)

SEED = 1717
N_SETS = 450
TIME_LIMIT = 120.0          # the ILP does NOT close in this; see FACTCHECK F4
REL_GAP = 1e-3
BONUSES = (0.0, 0.25, 0.5, 1.0, 2.0, 5.0, 20.0)
TOUR_BLOCK = 8              # mid-night, both schedulers well warmed up


# ═════════════════════════════════════════════════════════════════════════════
#  the experiment
# ═════════════════════════════════════════════════════════════════════════════
def run():
    night = S.Night(seed=SEED, n_sets=N_SETS)
    out = {"night": night}
    out["greedy"] = S.run_greedy(night)
    out["bonus"] = [S.run_greedy(night, finish_bonus=b) for b in BONUSES]
    out["planner"] = S.run_planner(night, time_limit=TIME_LIMIT,
                                   rel_gap=REL_GAP)
    out["log10_orderings"] = S.log10_orderings(1000)
    return out


def selfcheck(p):
    """Every number the narration says, re-derived here and asserted.

    The point of asserting rather than printing is that a failure must stop
    the build.  A plate is evidence; evidence that quietly drifts away from
    what the voice-over claims is the one defect no gate downstream can see.
    """
    g, pl = p["greedy"], p["planner"]
    bon = p["bonus"]
    ok = []

    def claim(name, cond, shown):
        ok.append(bool(cond))
        print("  [%s] %-34s %s" % ("ok" if cond else "FAIL", name, shown))

    claim("orderings",
          p["log10_orderings"] > 2500.0,
          "log10(1000!) = %.1f" % p["log10_orderings"])

    claim("greedy strands pairs",
          0.70 < g["completion"] < 0.90,
          "greedy completion = %.3f" % g["completion"])

    claim("planner finishes what it starts",
          pl["completion"] > 0.999,
          "planner completion = %.3f" % pl["completion"])

    claim("throughput is comparable",
          abs(pl["visits_per_hour"] - g["visits_per_hour"])
          / g["visits_per_hour"] < 0.10,
          "greedy %.1f/h vs planner %.1f/h"
          % (g["visits_per_hour"], pl["visits_per_hour"]))

    claim("planner works lower in the sky",
          pl["median_airmass"] < g["median_airmass"],
          "median X: greedy %.3f, planner %.3f"
          % (g["median_airmass"], pl["median_airmass"]))

    # The falsifiability test.  Greedy CAN be paid to finish pairs -- but the
    # payment is throughput, and it buys the gain by starting fewer fields.
    # If this ever came out free, the episode's claim would be wrong.
    top = bon[-1]
    claim("a paid greedy buys completion with throughput",
          top["completion"] > 0.95 and top["started"] < bon[0]["started"]
          and top["visits_per_hour"] < bon[0]["visits_per_hour"],
          "bonus=%g: completion %.3f (started %d->%d, %.1f->%.1f /h)"
          % (BONUSES[-1], top["completion"], bon[0]["started"],
             top["started"], bon[0]["visits_per_hour"],
             top["visits_per_hour"]))

    if not all(ok):
        raise SystemExit("[gen_sched] claims failed -- nothing written.")
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
            self.d.line([x, yy, min(x + 16, r - 4), yy], fill=colour,
                        width=width)
            x += 30

    def curve(self, xs, ys, colour=ACC, width=7):
        pts = [(float(self.X(a)), float(self.Y(b))) for a, b in zip(xs, ys)]
        if len(pts) > 1:
            self.d.line(pts, fill=colour, width=width, joint="curve")

    def dot(self, x, y, colour=INK, r=11):
        px, py = float(self.X(x)), float(self.Y(y))
        self.d.ellipse([px - r, py - r, px + r, py + r], fill=colour)

    def ring(self, x, y, colour=ACCT, r=11, width=5):
        px, py = float(self.X(x)), float(self.Y(y))
        self.d.ellipse([px - r, py - r, px + r, py + r], fill=CREAM,
                       outline=colour, width=width)

    def bar(self, x, y, w, colour, y0=None):
        y0 = self.ylim[0] if y0 is None else y0
        top, base = float(self.Y(y)), float(self.Y(y0))
        self.d.rectangle([float(self.X(x - w)), top,
                          float(self.X(x + w)), base], fill=colour)

    def band(self, y0, y1, colour=FAINT):
        l, _, r, _ = self.bx
        self.d.rectangle([l, float(self.Y(y1)), r, float(self.Y(y0))],
                         fill=colour)


W, H = 1560, 780


def window_plate(p):
    """Altitude against time for a sample of fields, with the 20 deg floor.

    This is the whole constraint in one frame: every field is a hill, each
    hill peaks at a different hour, and the shaded strip is sky the telescope
    may not point into.  Nothing here is a scheduling decision -- it is the
    board the game is played on.
    """
    night = p["night"]
    ax = Axes(W, H, (0.0, S.NIGHT_H), (0.0, 90.0), m=(14, 14, 14, 14))
    ax.band(0.0, S.ALT_MIN_DEG, FAINT)

    ts = np.linspace(0.0, S.NIGHT_H, 160)
    lst = (night.lst0 + 360.0 * ts / 23.9344696) % 360.0
    rng = np.random.default_rng(4)
    pick = rng.choice(night.n, size=34, replace=False)
    for i, j in enumerate(pick):
        alt, _ = S.altaz(np.full_like(lst, night.ra[j]),
                         np.full_like(lst, night.dec[j]), lst)
        vis = alt > -2.0
        if vis.sum() < 4:
            continue
        col = GHOST if i % 3 else SOFT
        ax.curve(ts[vis], np.clip(alt[vis], 0.0, 90.0), colour=col, width=4)

    # Three hot tracks, chosen to PEAK AT DIFFERENT HOURS -- the point of the
    # frame is that the good moment for each field is a different moment.
    peaks = []
    for j in pick:
        alt, _ = S.altaz(np.full_like(lst, night.ra[j]),
                         np.full_like(lst, night.dec[j]), lst)
        if alt.max() > 55.0:
            peaks.append((float(ts[int(np.argmax(alt))]), int(j)))
    peaks.sort()
    hot = [j for _, j in (peaks[:1] + peaks[len(peaks) // 2:
                                            len(peaks) // 2 + 1]
                          + peaks[-1:])] if len(peaks) >= 3 else list(pick[:3])
    for j in hot:
        alt, _ = S.altaz(np.full_like(lst, night.ra[j]),
                         np.full_like(lst, night.dec[j]), lst)
        vis = alt > -2.0
        ax.curve(ts[vis], np.clip(alt[vis], 0.0, 90.0), colour=ACC, width=8)

    ax.hline(S.ALT_MIN_DEG, colour=ACCT, width=5, dash=True)
    return ax.img


def _polar(d, cx, cy, R, alt, az):
    r = R * (90.0 - np.asarray(alt, float)) / 70.0
    a = np.radians(np.asarray(az, float))
    return cx + r * np.sin(a), cy - r * np.cos(a)


def tour_plate(p):
    """One half-hour of sky, twice: what each scheduler's path looks like.

    Left is the greedy rule, which picks the single best next exposure and so
    walks wherever the best exposure happens to be.  Right is the planner's
    block, sequenced as a travelling-salesman tour because once you have
    DECIDED the set, ordering it is a different and much easier problem.
    """
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    R = 320
    t0 = TOUR_BLOCK * S.BLOCK_MIN * 60.0
    t1 = (TOUR_BLOCK + 1) * S.BLOCK_MIN * 60.0

    for side, res in ((0, p["greedy"]), (1, p["planner"])):
        cx = W * (0.26 + 0.48 * side)
        cy = H * 0.5
        for frac, col, wd in ((1.0, GHOST, 4), (70.0 / 70.0, None, 0)):
            if col:
                d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=col,
                          width=wd)
        rr = R * (90.0 - 45.0) / 70.0
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=FAINT,
                  width=3)

        seq = [e for e in res["log"] if t0 <= e["t"] < t1]
        xs, ys = _polar(d, cx, cy, R, [e["alt"] for e in seq],
                        [e["az"] for e in seq])
        pts = list(zip(xs, ys))
        if len(pts) > 1:
            d.line(pts, fill=SOFT if side == 0 else ACC, width=5,
                   joint="curve")
        # Colour says WHICH SCHEDULER, matching every other plate. It must not
        # say "band": each of these blocks happens to be single-band, so a
        # band encoding would read as a scheduler encoding and mislead.
        c = INK if side == 0 else ACCT
        for (x, y) in pts:
            d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=c)
    return img


def completion_plate(p):
    """One square per sequence the scheduler STARTED. Filled = it finished it.

    The bar chart this replaces was unreadable without axis labels, and plates
    here carry no text. This version needs none: a hollow square is a field
    that got one half of its g+r pair and never got the other, which is not
    half a detection -- it is zero, because nothing can be compared against
    nothing. Greedy starts MORE and leaves a scatter of holes; the planner
    starts fewer and leaves none, which is the whole episode in one frame.
    """
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    cols, pitch, r = 20, 30.0, 9.5

    for side, res in ((0, p["greedy"]), (1, p["planner"])):
        done, req = res["done"], p["night"].n_req
        touched = done.sum(axis=1) > 0
        full = (done >= req).all(axis=1)
        flags = [bool(full[i]) for i in range(len(touched)) if touched[i]]
        rows = int(math.ceil(len(flags) / float(cols)))
        x0 = 120.0 + 720.0 * side      # two 600px blocks, gaps 120/120/120
        y0 = (H - rows * pitch) * 0.5
        for i, done_i in enumerate(flags):
            cx = x0 + (i % cols) * pitch
            cy = y0 + (i // cols) * pitch
            box = [cx - r, cy - r, cx + r, cy + r]
            if done_i:
                d.rectangle(box, fill=INK if side == 0 else ACC)
            else:
                d.rectangle(box, fill=CREAM, outline=ACCT, width=4)
    return img


def bonus_plate(p):
    """Can a myopic rule simply be PAID to care about finishing?

    Partly, yes -- and the colour of each marker is the price.  A filled
    marker is a bonus setting that held its exposure rate; a hollow one gave
    rate away.  The curve climbs toward the dashed line, but it goes hollow
    before it gets there, which is the finding.
    """
    bon = p["bonus"]
    base = bon[0]["visits_per_hour"]
    xs = np.arange(len(BONUSES), dtype=float)
    ys = [b["completion"] for b in bon]

    ax = Axes(W, H, (-0.45, len(BONUSES) - 0.55), (0.76, 1.045),
              m=(70, 40, 70, 40))
    ax.hline(p["planner"]["completion"], colour=GHOST, width=4, dash=True)
    ax.curve(xs, ys, colour=ACC, width=8)
    for x, b in zip(xs, bon):
        if b["visits_per_hour"] >= base - 1e-9:
            ax.dot(x, b["completion"], INK, r=14)
        else:
            ax.ring(x, b["completion"], ACCT, r=14, width=6)
    return ax.img


def airmass_plate(p):
    """Where in the sky each scheduler actually spent the night.

    Airmass is not bookkeeping: depth falls and seeing worsens as it rises,
    so a distribution pushed left is a night of deeper images.  The planner's
    advantage here is a SIDE EFFECT -- it was never asked for low airmass, it
    was asked to finish pairs, and finishing pairs means choosing fields that
    will still be high when their second half comes due.
    """
    g = np.array([e["X"] for e in p["greedy"]["log"]])
    pl = np.array([e["X"] for e in p["planner"]["log"]])
    lo, hi = 1.0, 3.0      # alt=20 deg is X~2.9: nothing is clipped
    edges = np.linspace(lo, hi, 33)
    hg, _ = np.histogram(np.clip(g, lo, hi), bins=edges)
    hp, _ = np.histogram(np.clip(pl, lo, hi), bins=edges)
    top = max(hg.max(), hp.max()) * 1.12

    ax = Axes(W, H, (lo, hi), (0.0, top), m=(40, 34, 40, 34))
    ctr = 0.5 * (edges[:-1] + edges[1:])
    wd = (edges[1] - edges[0]) * 0.46
    for c, v in zip(ctr, hg):
        if v:
            ax.bar(c, v, wd, FAINT)

    def step(h, colour, width):
        xs, ys = [], []
        for i, v in enumerate(h):
            xs += [edges[i], edges[i + 1]]
            ys += [float(v), float(v)]
        ax.curve(xs, ys, colour=colour, width=width)

    step(hg, SOFT, 6)
    step(hp, ACC, 8)
    return ax.img


# ═════════════════════════════════════════════════════════════════════════════
def main():
    os.makedirs(OUT, exist_ok=True)
    print("[gen_sched] running the night (n_sets=%d, seed=%d)"
          % (N_SETS, SEED))
    p = run()
    print("[gen_sched] checking claims")
    selfcheck(p)

    plates = {
        "window": window_plate(p),
        "tour": tour_plate(p),
        "completion": completion_plate(p),
        "bonus": bonus_plate(p),
        "airmass": airmass_plate(p),
    }
    for name, im in plates.items():
        path = os.path.join(OUT, name + ".png")
        im.save(path)
        print("  wrote %s  %dx%d" % (path, im.size[0], im.size[1]))


if __name__ == "__main__":
    main()
