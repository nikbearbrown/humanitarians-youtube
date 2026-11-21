"""gen_craters.py -- the self-check and the six plates for Ep. 18.

Run:  python -I assets/gen_craters.py        (a few seconds)

NINE claims are ASSERTED. If any one fails, NOTHING is written. A plate that
disagrees with the narration is worse than no plate at all.

Plates carry IMAGERY ONLY. No text, no tick labels, no legend, no axis
numbers: every label on screen is placed by scenes.py OUTSIDE the plate,
because a plate arrives in Manim as an ImageMobject and the layout gate is
nearly blind to its interior.

COLOUR MAP -- fixed across all six plates, never flipped:
    terracotta  THE COUNT  -- the measurement, the thing a detector changes
    ink         THE CLOCK  -- the chronology curve and the dated rocks
    ghost       scaffolding only (frames, axes, the empty gap)
"""
import math
import os
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import craters as C  # noqa: E402

OUT = os.path.join(HERE, "plots")

CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
FAINT = (214, 210, 196)
ACC = (217, 119, 87)

SS = 3                      # supersample, then downsample: smooth circles

# the two surfaces the episode compares
T_YOUNG, T_OLD = 1.0, 3.5
REL_ERR = 0.45              # Robbins et al. (2014): expert-to-expert, up to ~+-45%

# the three populations in pile.png
N_TRAIN = 7048              # Benedix et al. (2020) training set
N_HAND = 384343             # Robbins & Hynek (2012), complete to D >= 1 km
N_SMALL = 3.0e7             # Benedix et al.: 10 m - 1 km on Mars, "tens of millions"

# Chang'e-5
CE5_COUNT_LO, CE5_COUNT_HI = 1.3, 2.7       # Qiao et al. (2021), across chronologies
CE5_ROCK, CE5_ROCK_ERR = 2.030, 0.004       # Li et al. (2021), Pb-Pb

# the calibration anchors. SCHEMATIC IN PLACEMENT -- see FACTCHECK F7. What is
# load-bearing on screen is the shape: a cluster of old anchors, a few young
# ones, and an empty stretch between roughly 1 and 3 Ga.
ANCHORS_OLD = [3.92, 3.85, 3.80, 3.75, 3.41, 3.30, 3.22, 3.15]
ANCHORS_YOUNG = [0.80, 0.109, 0.053, 0.026]
GAP_LO, GAP_HI = 1.0, 3.0


# ═════════════════════════════════════════════════════════════════════════════
#  the self-check -- every number the narration speaks, re-derived
# ═════════════════════════════════════════════════════════════════════════════
def selfcheck():
    """Assert, don't print. A failure must stop the build, not scroll past."""
    rep = []

    # C1 -- the two surfaces, and how much denser the old one is
    ny, no = C.N1(T_YOUNG), C.N1(T_OLD)
    ratio = no / ny
    assert abs(ratio - 5.72) < 0.02, ratio
    rep.append("C1  N(1): %.3e at %.1f Ga, %.3e at %.1f Ga -> old is %.2fx denser"
               % (ny, T_YOUNG, no, T_OLD, ratio))

    # C2 -- +-45% counting error on the YOUNG surface
    lo, hi = C.age_window(T_YOUNG, REL_ERR)
    assert abs(lo - 0.55) < 0.01, lo
    assert abs(hi - 1.45) < 0.01, hi
    span_y = hi - lo
    pct_y = 100.0 * span_y / T_YOUNG
    assert abs(pct_y - 90.0) < 1.0, pct_y
    rep.append("C2  %.1f Ga surface, +-45%% count -> %.2f - %.2f Ga  (%.0f%% of the age)"
               % (T_YOUNG, lo, hi, pct_y))

    # C3 -- the SAME error on the OLD surface
    lo3, hi3 = C.age_window(T_OLD, REL_ERR)
    assert abs(lo3 - 3.05) < 0.01, lo3
    assert abs(hi3 - 3.61) < 0.01, hi3
    span_o = hi3 - lo3
    pct_o = 100.0 * span_o / T_OLD
    assert abs(pct_o - 16.0) < 1.0, pct_o
    rep.append("C3  %.1f Ga surface, the SAME +-45%% -> %.2f - %.2f Ga  (%.0f%% of the age)"
               % (T_OLD, lo3, hi3, pct_o))

    # C4 -- the headline comparison the episode says out loud
    factor = span_y / span_o
    assert 1.5 < factor < 1.7, factor
    assert pct_y / pct_o > 5.0, (pct_y, pct_o)
    rep.append("C4  same error costs %.0f%% of the age at %.1f Ga and %.0f%% at %.1f Ga"
               % (pct_y, T_YOUNG, pct_o, T_OLD))

    # C5 -- why: nearly all of an ancient surface's craters landed early
    share = C.early_share(4.1, T_OLD)
    assert share > 0.95, share
    rep.append("C5  %.0f%% of a 4.1 Ga surface's craters landed before %.1f Ga"
               % (100 * share, T_OLD))

    # C6 -- the toy field carries the REAL ratio
    n_y, n_o = C.patch_counts(T_YOUNG, T_OLD, 14)
    assert n_o == round(14 * ratio) == 80, (n_y, n_o)
    fy = C.synth_patch(n_y, seed=1801)
    fo = C.synth_patch(n_o, seed=1802)
    assert len(fy) == n_y and len(fo) == n_o, (len(fy), len(fo))
    assert abs(len(fo) / len(fy) - ratio) / ratio < 0.02
    rep.append("C6  toy patches: %d vs %d craters = %.2fx, the real chronology ratio"
               % (len(fy), len(fo), len(fo) / len(fy)))

    # C7 -- the rock against the crater count, on the SAME piece of ground
    count_span = (CE5_COUNT_HI - CE5_COUNT_LO) * 1000.0      # Myr
    rock_span = 2.0 * CE5_ROCK_ERR * 1000.0                  # Myr
    tighter = count_span / rock_span
    assert abs(count_span - 1400.0) < 1.0, count_span
    assert abs(rock_span - 8.0) < 0.01, rock_span
    assert abs(tighter - 175.0) < 1.0, tighter
    rep.append("C7  Chang'e-5 unit: counting said a %.0f Myr window, the rock said %.0f Myr"
               " -> %.0fx tighter" % (count_span, rock_span, tighter))

    # C8 -- and the rock's answer sits inside the counted window
    assert CE5_COUNT_LO < CE5_ROCK < CE5_COUNT_HI, CE5_ROCK
    rep.append("C8  %.3f Ga falls inside the %.1f - %.1f Ga counted window: counting was"
               " not WRONG, it was LOOSE" % (CE5_ROCK, CE5_COUNT_LO, CE5_COUNT_HI))

    # C9 -- the anchors really do leave the middle empty
    assert not any(GAP_LO < a < GAP_HI for a in ANCHORS_OLD + ANCHORS_YOUNG)
    assert GAP_LO < CE5_ROCK < GAP_HI
    rep.append("C9  no pre-Chang'e-5 anchor between %.1f and %.1f Ga; the new one lands at %.2f"
               % (GAP_LO, GAP_HI, CE5_ROCK))

    return rep


# ═════════════════════════════════════════════════════════════════════════════
#  drawing helpers
# ═════════════════════════════════════════════════════════════════════════════
def canvas(w, h):
    im = Image.new("RGB", (w * SS, h * SS), CREAM)
    return im, ImageDraw.Draw(im, "RGBA")


def finish(im, name, w, h):
    im = im.resize((w, h), Image.LANCZOS)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    im.save(p)
    return p


def circle(dr, cx, cy, r, outline=None, fill=None, width=2):
    dr.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS],
               outline=outline, fill=fill, width=int(width * SS))


def line(dr, pts, color, width=2):
    dr.line([(x * SS, y * SS) for (x, y) in pts], fill=color, width=int(width * SS),
            joint="curve")


def rect(dr, x0, y0, x1, y1, outline=None, fill=None, width=2):
    dr.rectangle([x0 * SS, y0 * SS, x1 * SS, y1 * SS],
                 outline=outline, fill=fill, width=int(width * SS))


def crater(dr, cx, cy, r, color, filled, width=2.0):
    """One crater. FILL CARRIES MEANING: filled = agreed, open = contested."""
    if filled:
        circle(dr, cx, cy, r, outline=color, fill=color + (46,), width=width)
    else:
        circle(dr, cx, cy, r, outline=color, fill=None, width=width)


# ═════════════════════════════════════════════════════════════════════════════
#  P1  surface.png -- two patches of ground: young / old. Density IS age.
# ═════════════════════════════════════════════════════════════════════════════
def plate_surface():
    W, H = 1880, 940
    im, dr = canvas(W, H)
    side = 760
    top = (H - side) // 2
    for i, (field, x0) in enumerate(((SURF_Y, 140), (SURF_O, W - 140 - side))):
        rect(dr, x0, top, x0 + side, top + side, outline=GHOST, width=2)
        for (fx, fy, d) in field:
            crater(dr, x0 + fx * side, top + fy * side, 0.5 * d * side,
                   ACC, True, width=2.2)
    return finish(im, "surface.png", W, H)


# ═════════════════════════════════════════════════════════════════════════════
#  P2  pile.png -- three populations on a log axis. The scale problem.
# ═════════════════════════════════════════════════════════════════════════════
def plate_pile():
    """THE DECADE RAILS ARE LOAD-BEARING. The axis is log10, and the three
    populations span 3,000 to 30,000,000 -- without visible decades the bars
    read as linear and the viewer concludes the machine's job is ~4x the
    hand job instead of ~78x. The rails are the only thing on this plate
    that says 'each step is another ten times'."""
    W, H = 1880, 620
    im, dr = canvas(W, H)
    x0, x1 = 150, W - 150
    lo, hi = 3.0, 7.8                       # log10 decades spanned
    rows = [N_TRAIN, N_HAND, N_SMALL]
    bh, gap = 112, 70
    top, bot = 70, 70 + 3 * bh + 2 * gap
    for dec in range(4, 8):                 # one rail per power of ten
        x = x0 + (dec - lo) / (hi - lo) * (x1 - x0)
        line(dr, [(x, top - 14), (x, bot + 14)], FAINT, 2)
    y = top
    for n in rows:
        frac = (math.log10(n) - lo) / (hi - lo)
        rect(dr, x0, y, x0 + frac * (x1 - x0), y + bh, fill=ACC + (235,), width=0)
        y += bh + gap
    line(dr, [(x0, top - 14), (x0, bot + 14)], GHOST, 2)     # the zero rail
    return finish(im, "pile.png", W, H)


# ═════════════════════════════════════════════════════════════════════════════
#  P3  spread.png -- one patch, two kinds of crater: unanimous / argued over.
# ═════════════════════════════════════════════════════════════════════════════
def plate_spread():
    W, H = 1000, 1000
    im, dr = canvas(W, H)
    side = 900
    x0, top = (W - side) // 2, (H - side) // 2
    rect(dr, x0, top, x0 + side, top + side, outline=GHOST, width=2)
    for (fx, fy, d), v in zip(SPREAD_F, SPREAD_V):
        crater(dr, x0 + fx * side, top + fy * side, 0.5 * d * side,
               ACC, v == N_ANALYSTS, width=2.4)
    return finish(im, "spread.png", W, H)


# ═════════════════════════════════════════════════════════════════════════════
#  the chronology curve -- shared geometry for P4 and P5
# ═════════════════════════════════════════════════════════════════════════════
CV_W, CV_H = 1760, 1000
CV_L, CV_R, CV_T = 170, CV_W - 120, 90
CV_B = CV_H - 130                   # curve.png: the plot owns the whole canvas
T_LO, T_HI = 0.0, 4.1
L_LO, L_HI = math.log10(6e-5), math.log10(6e-2)


def cx_of(T):
    return CV_L + (T - T_LO) / (T_HI - T_LO) * (CV_R - CV_L)


def cy_of(N, bot=None):
    bot = CV_B if bot is None else bot
    f = (math.log10(max(N, 10 ** L_LO)) - L_LO) / (L_HI - L_LO)
    return bot - f * (bot - CV_T)


def _axes(dr, bot=None):
    bot = CV_B if bot is None else bot
    line(dr, [(CV_L, CV_T - 18), (CV_L, bot)], GHOST, 2)
    line(dr, [(CV_L, bot), (CV_R + 18, bot)], GHOST, 2)
    for dec in range(-4, -1):               # faint decade rails
        y = cy_of(10.0 ** dec, bot)
        if CV_T < y < bot:
            line(dr, [(CV_L, y), (CV_R, y)], FAINT, 1.5)


def _curve(dr, bot=None, width=4.0):
    pts = []
    t = T_LO
    while t <= T_HI + 1e-9:
        pts.append((cx_of(t), cy_of(C.N1(t), bot)))
        t += 0.01
    line(dr, pts, INK, width)


def plate_curve():
    im, dr = canvas(CV_W, CV_H)
    _axes(dr)
    _curve(dr)
    return finish(im, "curve.png", CV_W, CV_H)


# ═════════════════════════════════════════════════════════════════════════════
#  P5  cost.png -- the same +-45% band, run through the curve at 1.0 and 3.5 Ga
#
#  THE SECOND PANEL IS LOAD-BEARING. On an absolute time axis the two age
#  windows come out 0.90 and 0.56 Gyr wide -- only 1.6x apart -- so the top
#  panel alone reads as "about the same" and teaches the OPPOSITE of the beat.
#  The cost is not the width of the window, it is the width of the window
#  AGAINST THE AGE BEING MEASURED. So underneath, each case gets a ghost bar
#  running 0 -> its own age with the terracotta window laid over it: the young
#  bar is swallowed whole, the old one takes a nick at the end.
# ═════════════════════════════════════════════════════════════════════════════
CO_B = 640                          # cost.png: the curve stops here
CO_ROWS = (790, 910)                # ... and the two comparison bars go below


def plate_cost():
    im, dr = canvas(CV_W, CV_H)
    _axes(dr, CO_B)
    for T in (T_YOUNG, T_OLD):
        n = C.N1(T)
        lo, hi = C.age_window(T, REL_ERR)
        yb, yt = cy_of((1 - REL_ERR) * n, CO_B), cy_of((1 + REL_ERR) * n, CO_B)
        xl, xr = cx_of(lo), cx_of(hi)
        # the count error: a horizontal band, from the y-axis out to the curve
        dr.rectangle([CV_L * SS, yt * SS, xr * SS, yb * SS], fill=ACC + (40,))
        # what it becomes in time: the same band dropped onto the age axis
        dr.rectangle([xl * SS, yb * SS, xr * SS, CO_B * SS], fill=ACC + (64,))
        line(dr, [(xl, yb), (xl, CO_B)], ACC, 2.5)
        line(dr, [(xr, yt), (xr, CO_B)], ACC, 2.5)
        circle(dr, cx_of(T), cy_of(n, CO_B), 9, outline=INK, fill=CREAM, width=3.5)
    _curve(dr, CO_B)

    # the panel that stops the plate teaching the opposite of the beat
    for T, yrow in zip((T_YOUNG, T_OLD), CO_ROWS):
        lo, hi = C.age_window(T, REL_ERR)
        h = 34
        rect(dr, cx_of(0.0), yrow - h, cx_of(T), yrow + h,
             fill=FAINT + (150,), width=0)                       # the age itself
        rect(dr, cx_of(lo), yrow - h, cx_of(hi), yrow + h,
             fill=ACC + (150,), width=0)                         # what you can say
        line(dr, [(cx_of(T), yrow - h - 16), (cx_of(T), yrow + h + 16)], INK, 3)
    return finish(im, "cost.png", CV_W, CV_H)


# ═════════════════════════════════════════════════════════════════════════════
#  P6  anchors.png -- what the clock is actually nailed to, and the hole in it
# ═════════════════════════════════════════════════════════════════════════════
def plate_anchors():
    W, H = 1880, 530
    im, dr = canvas(W, H)
    L, R = 160, W - 160
    axis_y = 440

    def ax(T):                              # oldest on the left, today on the right
        return R - (T / 4.2) * (R - L)

    # the empty stretch, drawn as absence: a faint box with nothing in it
    rect(dr, ax(GAP_HI), axis_y - 104, ax(GAP_LO), axis_y, fill=FAINT + (90,), width=0)
    line(dr, [(L, axis_y), (R, axis_y)], GHOST, 2.5)

    # every anchor is a dated ROCK -> ink
    for a in ANCHORS_OLD + ANCHORS_YOUNG:
        x = ax(a)
        line(dr, [(x, axis_y), (x, axis_y - 70)], INK, 3)
        circle(dr, x, axis_y - 70, 11, outline=INK, fill=INK, width=0)

    # the crater COUNT for the Chang'e-5 unit -> terracotta, and wide
    bx0, bx1 = ax(CE5_COUNT_HI), ax(CE5_COUNT_LO)
    rect(dr, bx0, axis_y - 206, bx1, axis_y - 152, fill=ACC + (210,), width=0)

    # the ROCK from that same unit -> ink, and a single point
    xr = ax(CE5_ROCK)
    line(dr, [(xr, axis_y), (xr, axis_y - 152)], INK, 3)
    circle(dr, xr, axis_y - 152, 17, outline=INK, fill=CREAM, width=5)
    return finish(im, "anchors.png", W, H)


# ═════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    for lineout in selfcheck():
        print("  " + lineout)

    N_Y, N_O = C.patch_counts(T_YOUNG, T_OLD, 14)
    SURF_Y = C.synth_patch(N_Y, seed=1801)
    SURF_O = C.synth_patch(N_O, seed=1802)

    N_ANALYSTS = 6
    SPREAD_F = C.synth_patch(46, seed=1803)
    SPREAD_V = C.analyst_votes(SPREAD_F, N_ANALYSTS, seed=1804)

    print()
    for fn in (plate_surface, plate_pile, plate_spread,
               plate_curve, plate_cost, plate_anchors):
        print("  wrote " + os.path.relpath(fn(), HERE))
