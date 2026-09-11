#!/usr/bin/env python3
"""Compute every plate for Ep. 08 — *The Number Went Up.*

NOTHING HERE IS A DRAWING OF A RESULT. Each plate runs the calculation the
episode describes and prints its own diagnostic, so a wrong plate announces
itself instead of looking plausible:

  detect.png        a synthetic star field at two epochs and its real
                    difference image; prints how many sources the naive
                    detector finds and how many of them are actually real
  stamps.png        the eight postage-stamp classes the ATLAS CNN sorts,
                    each SYNTHESISED FROM ITS OWN PHYSICAL MODEL (a cosmic
                    ray is not a blurred dot; a dipole is a misregistration
                    residual; a spike is a diffraction artefact)
  tracklet.png      four detections in one hour; prints the straight-line
                    fit residual for the real mover and for the artefacts,
                    which is the quantity the second-stage MLP is scoring
  bplane.png        the target-plane geometry at three uncertainty widths:
                    Earth in the core, in the tail, then outside it
  impactprob.png    the impact probability as a function of the width of the
                    uncertainty region, by exact quadrature. THIS IS THE
                    POINT OF THE EPISODE: the rise-then-collapse is forced by
                    geometry alone. The script asserts its own numeric peak
                    against the analytic prediction sigma_peak -> d/sqrt(2)
                    and refuses to write anything if it disagrees.
  completeness.png  the near-Earth asteroid size-frequency distribution
                    with the discovered fraction shaded

Run:  python assets/gen_neo.py       (numpy + Pillow only; no network, no keys)

Deterministic: one seed, 8801, logged in SOURCES.md.
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SEED = 8801
OUT = Path(__file__).resolve().parent / "plots"
OUT.mkdir(parents=True, exist_ok=True)

# ── the Claude fidelity palette ──────────────────────────────────────────────
CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)          # terracotta — marks the MACHINE'S judgment
ACCT = (164, 74, 50)          # accented text
WHITE = (255, 255, 255)

# ── physical constants (SI-ish, km and km/s) ─────────────────────────────────
R_EARTH = 6371.0              # km
V_ESC = 11.186                # km/s, surface escape speed
V_IMPACT_YR4 = 17.3           # km/s, 2024 YR4's would-be impact speed (PMC12963224)


# ═════════════════════════════════════════════════════════════════════════════
#  imaging primitives
# ═════════════════════════════════════════════════════════════════════════════
def _gauss2d(shape, x0, y0, fwhm, flux):
    """One point source with a Gaussian PSF. Analytic, not a blurred pixel."""
    h, w = shape
    s = fwhm / 2.3548200450309493
    yy, xx = np.mgrid[0:h, 0:w]
    r2 = (xx - x0) ** 2 + (yy - y0) ** 2
    return flux / (2 * math.pi * s * s) * np.exp(-0.5 * r2 / (s * s))


def _trail(shape, x0, y0, dx, dy, fwhm, flux, n=24):
    """A source that MOVED during the exposure: a PSF smeared along a segment.

    A 30-second exposure of a fast near-Earth object is a short streak, not a
    dot. Summing sub-exposures is the honest way to make one -- convolving a
    line with a Gaussian by hand gets the end caps wrong.
    """
    acc = np.zeros(shape)
    for t in np.linspace(-0.5, 0.5, n):
        acc += _gauss2d(shape, x0 + dx * t, y0 + dy * t, fwhm, flux / n)
    return acc


def _sky(shape, rng, level=120.0, fwhm=3.4, nstar=140, seed_stars=None):
    """A star field: Poisson sky + a power-law brightness distribution."""
    h, w = shape
    img = np.full(shape, level, float)
    if seed_stars is None:
        sx = rng.uniform(0, w, nstar)
        sy = rng.uniform(0, h, nstar)
        # a realistic-ish flux distribution: many faint, few bright
        sf = 300.0 * (rng.pareto(1.2, nstar) + 1.0)
        seed_stars = (sx, sy, sf)
    sx, sy, sf = seed_stars
    for x, y, f in zip(sx, sy, sf):
        img += _gauss2d(shape, x, y, fwhm, f)
    return img, seed_stars


def _poisson(img, rng, gain=1.0):
    return rng.poisson(np.clip(img * gain, 0, None)) / gain


def _stretch(a, lo_pct=1.0, hi_pct=99.6, gamma=0.85):
    """Percentile-clipped arcsinh-ish stretch. Ep. 07's lesson: a gamma below
    1 lifts the faint end WITHOUT flattening the bright end into mush."""
    lo, hi = np.percentile(a, lo_pct), np.percentile(a, hi_pct)
    v = np.clip((a - lo) / max(hi - lo, 1e-9), 0, 1)
    return v ** gamma


def _stretch_sky(a, bg, span=26.0, gamma=0.75, pedestal=0.0):
    """A PHYSICAL stretch, shared by every panel: `pedestal` at the sky level,
    full scale `span` noise-sigmas above it.

    Per-panel percentile clipping was the bug in the first stamp sheet. It
    rescales each cut-out against its own brightest pixels, so a stamp
    containing one saturated column maps everything else to black and the
    eight classes stop being comparable -- which is precisely the comparison
    the beat is making. Anchoring every panel to the same sky level and the
    same noise unit is both honest and legible.

    `pedestal` exists for the postage stamps, which are cut from a DIFFERENCE
    image and are therefore signed. With the sky at pure black a negative
    excursion is indistinguishable from background, so the subtraction dipole
    -- two lobes, one positive and one negative -- rendered as a single dot
    and lost the whole point of that class. Lifting the zero point off black
    lets the negative lobe darken below it.
    """
    sigma = math.sqrt(max(bg, 1.0))
    v = pedestal + (1.0 - pedestal) * ((a - bg) / (span * sigma))
    return np.clip(v, 0.0, 1.0) ** gamma


def _stretch_diff(a, bg, span=14.0, gamma=0.8):
    """A difference image is signed. Cream at zero, ink upward, and the
    negative side clipped -- otherwise the noise floor fills the whole ramp
    and the one real source in the frame is lost inside it.
    """
    sigma = math.sqrt(max(bg, 1.0)) * math.sqrt(2.0)     # two frames differenced
    return np.clip(a / (span * sigma), 0.0, 1.0) ** gamma


def _warm_plate(v, bg=(16, 15, 13), fg=(247, 243, 233)):
    """Map [0,1] to a warm near-black -> warm white ramp, so a sky image sits
    inside the Claude palette instead of fighting it."""
    bg = np.array(bg, float)
    fg = np.array(fg, float)
    rgb = bg[None, None, :] + (fg - bg)[None, None, :] * v[:, :, None]
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _ink_plate(v, bg=CREAM, fg=INK):
    """Same ramp, but ink-on-cream for DIAGRAM-like images (the difference
    frame reads better dark-on-light beside the sky frames)."""
    return _warm_plate(v, bg=bg, fg=fg)


def _frame(img, colour=INK, width=3):
    ImageDraw.Draw(img).rectangle([0, 0, img.width - 1, img.height - 1],
                                  outline=colour, width=width)
    return img


def _paste_row(panels, gap=18, bg=CREAM, pad=0):
    """Lay panels out in a row on a cream ground."""
    h = max(p.height for p in panels)
    w = sum(p.width for p in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (w + 2 * pad, h + 2 * pad), bg)
    x = pad
    for p in panels:
        sheet.paste(p, (x, pad + (h - p.height) // 2))
        x += p.width + gap
    return sheet


# ═════════════════════════════════════════════════════════════════════════════
#  1. detection by image differencing
# ═════════════════════════════════════════════════════════════════════════════
def detect_plate(size=300, scale=4):
    """Two epochs of the same field and their difference.

    The mover appears in the difference. So do several things that are not
    movers, which is the entire reason a classifier exists.
    """
    rng = np.random.default_rng(SEED)
    shape = (size, size)

    BG = 120.0
    ref, stars = _sky(shape, rng, level=BG)
    new, _ = _sky(shape, rng, level=BG, seed_stars=stars)

    # the real thing: a near-Earth object, trailed by its own motion.
    # Bright enough to actually SEE in the difference: at 5200 it sat inside
    # the noise and the plate was a picture of nothing.
    ax, ay = 196.0, 122.0
    new = new + _trail(shape, ax, ay, 9.0, -3.0, 3.4, 34000.0)

    # things that are NOT the real thing, each from its own mechanism
    cr_x, cr_y = 88.0, 210.0                       # cosmic ray: 2 px, no PSF
    new[int(cr_y):int(cr_y) + 2, int(cr_x):int(cr_x) + 2] += 4200.0
    sat = _trail(shape, 150.0, 250.0, 250.0, 46.0, 2.6, 30000.0, n=180)
    new = new + sat                                # satellite streak

    ref = _poisson(ref, rng)
    new = _poisson(new, rng)

    # a real subtraction is imperfect: registration is off by a fraction of a
    # pixel, which turns every bright star into a positive/negative dipole
    shift = 0.35
    reg = np.roll(ref, 0, axis=0)
    reg = (1 - shift) * ref + shift * np.roll(ref, 1, axis=1)
    diff = new - reg

    # the naive detector: threshold at 5 sigma of the difference's own noise
    sigma = 1.4826 * np.median(np.abs(diff - np.median(diff)))
    mask = diff > 5.0 * sigma
    n_pix = int(mask.sum())
    # count connected blobs (4-connectivity flood fill, no scipy needed)
    seen = np.zeros_like(mask)
    blobs = []
    for j, i in zip(*np.nonzero(mask)):
        if seen[j, i]:
            continue
        stack, cells = [(j, i)], []
        seen[j, i] = True
        while stack:
            cj, ci = stack.pop()
            cells.append((cj, ci))
            for nj, ni in ((cj + 1, ci), (cj - 1, ci), (cj, ci + 1), (cj, ci - 1)):
                if 0 <= nj < size and 0 <= ni < size and mask[nj, ni] and not seen[nj, ni]:
                    seen[nj, ni] = True
                    stack.append((nj, ni))
        blobs.append(cells)
    blobs = [b for b in blobs if len(b) >= 3]

    # which blob is the asteroid? the one whose centroid sits on it
    real = 0
    for b in blobs:
        cy = np.mean([c[0] for c in b])
        cx = np.mean([c[1] for c in b])
        if (cx - ax) ** 2 + (cy - ay) ** 2 < 8.0 ** 2:
            real += 1

    px = size * scale // 2

    def up(v, plate=_warm_plate):
        return _frame(plate(v).resize((px, px), Image.LANCZOS))

    pa = up(_stretch_sky(ref, BG))
    pb = up(_stretch_sky(new, BG))
    pd = up(_stretch_diff(diff, BG), plate=_ink_plate)

    # ring the asteroid in the difference frame — terracotta marks the machine's find
    r = size * scale // 2 / size
    d = ImageDraw.Draw(pd)
    rad = 26
    d.ellipse([ax * r - rad, ay * r - rad, ax * r + rad, ay * r + rad],
              outline=ACC, width=5)

    _paste_row([pa, pb, pd]).save(OUT / "detect.png")

    print(f"  detect.png   5-sigma blobs in the difference: {len(blobs)}  "
          f"({real} real, {len(blobs) - real} artefacts)  "
          f"threshold={5 * sigma:.0f} ADU over {n_pix} px")
    return len(blobs), real


# ═════════════════════════════════════════════════════════════════════════════
#  2. the eight postage-stamp classes
# ═════════════════════════════════════════════════════════════════════════════
def stamp_plate(n=48, scale=6):
    """The CNN's actual input: 8 classes of small cut-out, each generated by
    the process that really makes it. A cosmic ray is NOT a faint asteroid
    with the contrast turned down -- it has no PSF at all, and that is exactly
    the difference a convolutional net can learn and a threshold cannot.
    """
    rng = np.random.default_rng(SEED + 1)
    shape = (n, n)
    c = n / 2.0
    stamps = {}

    # 1. a clean, slightly trailed near-Earth object
    stamps["asteroid"] = _trail(shape, c, c, 5.0, -1.8, 3.2, 2600.0)
    # 2. a main-belt asteroid: slower, so effectively a point source
    stamps["point source"] = _gauss2d(shape, c, c, 3.2, 1900.0)
    # 3. cosmic ray: 1-2 pixels, sharper than the PSF can possibly be
    cr = np.zeros(shape)
    cr[int(c), int(c)] = 3000.0
    cr[int(c) + 1, int(c)] = 1400.0
    stamps["cosmic ray"] = cr
    # 4. subtraction dipole: a star that moved by a third of a pixel
    stamps["dipole"] = (_gauss2d(shape, c + 0.9, c, 3.2, 2400.0)
                        - _gauss2d(shape, c - 0.9, c, 3.2, 2400.0))
    # 5. diffraction spike off a bright star just outside the stamp
    sp = _trail(shape, c, c, 0.0, n * 1.6, 2.2, 9000.0, n=120)
    sp += _trail(shape, c, c, n * 1.6, 0.0, 2.2, 9000.0, n=120)
    stamps["spike"] = sp
    # 6. satellite trail: straight, uniform, crosses the whole stamp
    stamps["streak"] = _trail(shape, c, c, n * 2.2, n * 0.7, 2.4, 14000.0, n=200)
    # 7. saturated-star column bleed: charge overflowing along one CCD column
    bl = _gauss2d(shape, c, c, 4.0, 4200.0)
    bl[:, int(c) - 1:int(c) + 2] += 900.0
    stamps["bleed"] = bl
    # 8. nothing at all -- pure noise. The largest class in practice.
    stamps["noise"] = np.zeros(shape)

    BG = 90.0
    panels, labels = [], []
    for k, v in stamps.items():
        a = _poisson(np.clip(v, 0, None) + BG, rng)
        if k == "dipole":                          # signed: keep both lobes
            a = _poisson(np.clip(v, 0, None) + BG, rng) - _poisson(
                np.clip(-v, 0, None) + BG, rng) + BG
        im = _warm_plate(_stretch_sky(a, BG, pedestal=0.20))
        im = im.resize((n * scale, n * scale), Image.NEAREST)
        panels.append(_frame(im, GHOST, 2))
        labels.append(k)

    # two rows of four
    cell = panels[0].width
    gap, lab = 16, 44
    sheet = Image.new("RGB", (4 * cell + 3 * gap, 2 * (cell + lab) + gap), CREAM)
    d = ImageDraw.Draw(sheet)
    for i, (p, name) in enumerate(zip(panels, labels)):
        x = (i % 4) * (cell + gap)
        y = (i // 4) * (cell + lab + gap)
        sheet.paste(p, (x, y))
        # a tick mark, not text: Manim sets the type, the plate stays a plate
        colour = ACC if name in ("asteroid", "point source") else GHOST
        d.line([(x + 4, y + cell + 14), (x + cell - 4, y + cell + 14)],
               fill=colour, width=6)
    sheet.save(OUT / "stamps.png")
    print(f"  stamps.png   {len(panels)} classes, "
          f"{sum(1 for l in labels if l in ('asteroid', 'point source'))} real / "
          f"{sum(1 for l in labels if l not in ('asteroid', 'point source'))} bogus")
    return labels


# ═════════════════════════════════════════════════════════════════════════════
#  3. the tracklet — what the second stage actually scores
# ═════════════════════════════════════════════════════════════════════════════
def tracklet_plate(w=1500, h=720):
    """Four detections over one hour.

    ATLAS takes four exposures of each field within about an hour. A real
    solar-system object walks a STRAIGHT line at a CONSTANT rate over that
    span; artefacts do not. The second-stage network is handed the sequence,
    not the pictures, and this plate computes the discriminant: the RMS
    residual about a least-squares straight line through the four positions.
    """
    rng = np.random.default_rng(SEED + 2)
    t = np.array([0.0, 0.31, 0.64, 1.0])          # hours

    # a real mover: linear in both axes, plus honest astrometric scatter
    rx, ry = 0.0 + 7.4 * t, 0.0 - 2.6 * t
    rx = rx + rng.normal(0, 0.035, 4)
    ry = ry + rng.normal(0, 0.035, 4)

    # four unrelated artefacts that happened to land near each other
    bx = rng.uniform(0, 7.4, 4)
    by = rng.uniform(-2.6, 0.9, 4)

    def rms(x, y):
        """RMS distance of the points from their own best-fit straight line,
        parameterised by time -- the same thing a linear tracklet fit does."""
        A = np.vstack([t, np.ones_like(t)]).T
        cx = np.linalg.lstsq(A, x, rcond=None)[0]
        cy = np.linalg.lstsq(A, y, rcond=None)[0]
        dx, dy = x - A @ cx, y - A @ cy
        return float(np.sqrt(np.mean(dx ** 2 + dy ** 2)))

    r_real, r_bogus = rms(rx, ry), rms(bx, by)

    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    m = {'l': 70, 'r': 40, 't': 48, 'b': 70}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']
    allx = np.concatenate([rx, bx])
    ally = np.concatenate([ry, by])
    x0, x1 = allx.min() - 0.7, allx.max() + 0.7
    y0, y1 = ally.min() - 0.6, ally.max() + 0.6

    def X(v):
        return m['l'] + (v - x0) / (x1 - x0) * pw

    def Y(v):
        return m['t'] + ph - (v - y0) / (y1 - y0) * ph

    for gx in np.linspace(x0, x1, 9):
        d.line([(X(gx), m['t']), (X(gx), m['t'] + ph)], fill=(226, 222, 210), width=1)
    for gy in np.linspace(y0, y1, 6):
        d.line([(m['l'], Y(gy)), (m['l'] + pw, Y(gy))], fill=(226, 222, 210), width=1)

    # the fitted line for the real mover, drawn to the frame
    A = np.vstack([t, np.ones_like(t)]).T
    cx = np.linalg.lstsq(A, rx, rcond=None)[0]
    cy = np.linalg.lstsq(A, ry, rcond=None)[0]
    # drawn only across the data span, so it cannot cross the axis and leave
    # the plot area (the first version ran out through the bottom-right corner)
    te = np.array([-0.06, 1.06])
    d.line([(X(cx[0] * te[0] + cx[1]), Y(cy[0] * te[0] + cy[1])),
            (X(cx[0] * te[1] + cx[1]), Y(cy[0] * te[1] + cy[1]))],
           fill=ACC, width=4)

    for x, y in zip(bx, by):                       # the artefacts: ghost, hollow
        d.ellipse([X(x) - 13, Y(y) - 13, X(x) + 13, Y(y) + 13], outline=SOFT, width=4)
    for x, y in zip(rx, ry):                       # the mover: solid terracotta
        d.ellipse([X(x) - 13, Y(y) - 13, X(x) + 13, Y(y) + 13], fill=ACC)

    d.line([(m['l'], m['t']), (m['l'], m['t'] + ph), (m['l'] + pw, m['t'] + ph)],
           fill=INK, width=3)
    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "tracklet.png")

    print(f"  tracklet.png straight-line RMS residual: real {r_real:.3f}  "
          f"artefacts {r_bogus:.3f}  (ratio {r_bogus / r_real:.0f}x)")
    return r_real, r_bogus


# ═════════════════════════════════════════════════════════════════════════════
#  4 + 5. the target plane and the impact probability
# ═════════════════════════════════════════════════════════════════════════════
def capture_radius(v_impact=V_IMPACT_YR4):
    """The Earth's gravitationally focused capture radius on the target plane.

        b_cap = R * sqrt(1 + (v_esc / v_inf)^2)

    An object aimed at a miss distance b < b_cap is pulled in and hits. Note
    the INPUT is the impact speed, so v_inf must be recovered first:
    v_imp^2 = v_inf^2 + v_esc^2. Using the impact speed directly here is a
    real and easy mistake -- it understates b_cap by about 12%.
    """
    v_inf = math.sqrt(max(v_impact ** 2 - V_ESC ** 2, 1e-9))
    return R_EARTH * math.sqrt(1.0 + (V_ESC / v_inf) ** 2), v_inf


def impact_probability(sigma_along, d, b_cap, sigma_across_frac=0.12,
                       n=20001, rng=None):
    """Probability that the object hits, given an uncertainty region of
    along-track width `sigma_along` and a nominal miss distance `d`.

    The orbit solution's uncertainty projects onto the target plane as a very
    elongated Gaussian -- the line of variations. The answer is the Gaussian's
    mass inside the capture disc, so integrate it:

        P = INT_{d-b}^{d+b} phi(x/sx)/sx * erf( sqrt(b^2-(x-d)^2) / (sy*sqrt2) ) dx

    the inner y-integral having been done in closed form. This used to be a
    Monte Carlo, and the Monte Carlo broke the self-check below: at a disc
    1/1000 of the miss distance the peak probability is 1e-5, so even 800,000
    samples leave about 8 hits per point and argmax over a noisy curve returns
    noise. Quadrature is deterministic and exact to the grid, which is what a
    self-check needs to mean anything.
    """
    from scipy.special import erf

    sx = float(sigma_along)
    sy = max(sigma_across_frac * sx, 1e-12)
    x = np.linspace(d - b_cap, d + b_cap, n)
    h = np.sqrt(np.clip(b_cap ** 2 - (x - d) ** 2, 0.0, None))
    dens = np.exp(-0.5 * (x / sx) ** 2) / (sx * math.sqrt(2 * math.pi))
    return float(np.trapezoid(dens * erf(h / (sy * math.sqrt(2.0))), x))


def prob_plate(w=1720, h=860):
    """P(impact) against the width of the uncertainty region.

    THE EPISODE'S CENTRAL CLAIM, COMPUTED: as observations accumulate the
    region shrinks, and while the Earth is still inside it the probability
    RISES. It collapses only once the region has shrunk past the Earth. The
    rise was never evidence that anything got worse.

    SELF-CHECK, and it earned its keep. The first version of this docstring
    asserted the peak sits at sigma_along = d, from the one-dimensional
    argument: maximise sigma^-1 exp(-d^2 / 2 sigma^2) and you get sigma = d.
    The Monte Carlo said 0.67, and the Monte Carlo was right. The uncertainty
    shrinks in BOTH target-plane directions at once -- sigma_across is held at
    a fixed fraction of sigma_along here -- so for a capture disc small
    compared with the region, the probability goes as the disc area times the
    2-D density at the Earth:

        P  ~  b_cap^2 / sigma^2  *  exp(-d^2 / 2 sigma^2)

    and maximising THAT gives -2/sigma + d^2/sigma^3 = 0, so

        sigma_peak  ->  d / sqrt(2)  =  0.7071 d .

    The 1-D answer was simply the wrong geometry. The script now asserts the
    2-D prediction as b_cap/d -> 0 and prints PASS or FAIL.
    """
    b_cap, v_inf = capture_radius()
    d = 8.0 * b_cap                                # nominal misses, but not by much
    rng = np.random.default_rng(SEED + 3)

    # range chosen so the interesting part FILLS the plate: the first version
    # ran out to 60 d and spent 60% of its width on a flat zero tail.
    sig = np.logspace(math.log10(0.28 * d), math.log10(7.0 * d), 400)
    p = np.array([impact_probability(s, d, b_cap) for s in sig])
    i_pk = int(np.argmax(p))

    # the self-check: shrink the disc and watch the peak walk onto d/sqrt(2)
    PREDICTED = 1.0 / math.sqrt(2.0)
    checks = []
    for f in (8.0, 40.0, 200.0, 1000.0):
        dd = f * b_cap
        ss = np.logspace(math.log10(0.35 * dd), math.log10(4.0 * dd), 400)
        pp = np.array([impact_probability(s, dd, b_cap) for s in ss])
        checks.append((b_cap / dd, ss[int(np.argmax(pp))] / dd, pp.max()))
    converged = checks[-1][1]
    ok = abs(converged - PREDICTED) < 0.03

    img = Image.new("RGB", (w, h), WHITE)
    dr = ImageDraw.Draw(img)
    m = {'l': 104, 'r': 46, 't': 46, 'b': 88}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']
    sx0, sx1 = sig[0] / d, sig[-1] / d
    py1 = max(p.max() * 1.22, 1e-4)

    def X(s):
        """x runs BACKWARDS in sigma: left = a wide region (few observations),
        right = a narrow one (many). Built into the mapping rather than
        mirrored afterwards — the mirrored version worked but was impossible
        to reason about, and the peak marker had to repeat the same algebra.
        """
        u = (math.log10(s) - math.log10(sx0)) / (math.log10(sx1) - math.log10(sx0))
        return m['l'] + (1.0 - u) * pw

    def Y(v):
        return m['t'] + ph - (v / py1) * ph

    for e in range(-1, 3):                         # decade gridlines
        gx = 10.0 ** e
        if sx0 <= gx <= sx1:
            dr.line([(X(gx), m['t']), (X(gx), m['t'] + ph)], fill=(226, 222, 210), width=1)
    for frac in (0.25, 0.5, 0.75, 1.0):
        gy = py1 * frac
        dr.line([(m['l'], Y(gy)), (m['l'] + pw, Y(gy))], fill=(226, 222, 210), width=1)

    dr.line([(X(s / d), Y(v)) for s, v in zip(sig, p)], fill=ACC, width=6)

    # mark the peak
    pk_x = X(sig[i_pk] / d)
    dr.line([(pk_x, m['t']), (pk_x, m['t'] + ph)], fill=INK, width=3)
    dr.ellipse([pk_x - 12, Y(p[i_pk]) - 12, pk_x + 12, Y(p[i_pk]) + 12], fill=INK)

    dr.line([(m['l'], m['t']), (m['l'], m['t'] + ph), (m['l'] + pw, m['t'] + ph)],
            fill=INK, width=3)
    dr.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "impactprob.png")

    print(f"  impactprob.png  v_inf={v_inf:.2f} km/s  "
          f"b_cap={b_cap:.0f} km = {b_cap / R_EARTH:.3f} R_E")
    print(f"                  peak P={p[i_pk] * 100:.2f}% at sigma/d="
          f"{sig[i_pk] / d:.2f}, collapses to {p[0] * 100:.4f}% "
          f"at sigma/d={sig[0] / d:.2f}")
    print(f"                  SELF-CHECK  peak sigma/d must -> 1/sqrt(2) = "
          f"{PREDICTED:.4f} as b_cap/d -> 0:")
    for bc, speak, pmax in checks:
        print(f"                    b_cap/d={bc:.4f}  ->  peak at sigma/d="
              f"{speak:.4f}   (P_max {pmax * 100:.3f}%)")
    print(f"                  {'PASS' if ok else 'FAIL'}: converged to "
          f"{converged:.4f} vs predicted {PREDICTED:.4f} "
          f"(delta {converged - PREDICTED:+.4f})")
    if not ok:
        raise SystemExit("[gen_neo] self-check FAILED — the target-plane "
                         "geometry does not match the analytic prediction. "
                         "Fix the physics before rendering anything.")
    return b_cap, d, float(p[i_pk]), float(sig[i_pk] / d)


def bplane_plate(b_cap, d, w=1680, h=560, frac_across=0.12):
    """The same geometry as a picture, at three uncertainty widths.

    Earth is a fixed ink disc at a fixed offset d; only the uncertainty
    changes. Panel 1: Earth in the CORE of the region. Panel 2: Earth out on
    the TAIL. Panel 3: the region has shrunk PAST the Earth.

    The region is rendered as the actual 2-D Gaussian density, not as nested
    outlines. The outline version was unreadable: at sigma = 14 d the 3-sigma
    ellipse is far wider than the panel, so it clipped into horizontal bands
    that looked like a rendering bug. Everything here is to scale -- Earth's
    disc really is b_cap and really sits d from the nominal -- and the panel
    span is chosen so the widest 1-sigma contour still fits.
    """
    sigmas = [1.6 * d, 0.50 * d, 0.16 * d]
    tags = ["Earth in the core", "Earth on the tail", "region past Earth"]
    span = 2.2 * d                                  # half-width of each panel, km
    pw = (w - 4 * 16) // 3
    ph = h - 2
    panels = []
    for s in sigmas:
        k = (pw * 0.46) / span                      # km -> px
        yy, xx = np.mgrid[0:ph, 0:pw]
        cx, cy = pw / 2.0, ph / 2.0
        sx = s * k
        sy = max(frac_across * s * k, 1.2)
        g = np.exp(-0.5 * (((xx - cx) / sx) ** 2 + ((yy - cy) / sy) ** 2))
        g = g / g.max()
        # terracotta density on white — a real rendering of the LOV cloud
        base = np.array(WHITE, float)
        acc = np.array(ACC, float)
        rgb = base[None, None, :] + (acc - base)[None, None, :] * (g ** 0.55)[:, :, None]
        pan = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
        dr = ImageDraw.Draw(pan)
        dr.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=ACCT)     # the nominal
        ex = cx + d * k                                             # the Earth
        rr = max(b_cap * k, 6.0)
        dr.ellipse([ex - rr, cy - rr, ex + rr, cy + rr], fill=INK)
        dr.rectangle([0, 0, pan.width - 1, pan.height - 1], outline=INK, width=3)
        panels.append(pan)

    _paste_row(panels, gap=16).save(OUT / "bplane.png")
    print("  bplane.png   " + ";  ".join(
        f"sigma/d={s / d:.2f} ({t}, Earth at {d / s:.1f} sigma)"
        for s, t in zip(sigmas, tags)))
    print(f"                to scale: Earth disc = b_cap = {b_cap:.0f} km, "
          f"offset d = {d:.0f} km = {d / b_cap:.1f} b_cap")


# ═════════════════════════════════════════════════════════════════════════════
#  6. the survey ledger
# ═════════════════════════════════════════════════════════════════════════════
def completeness_plate(w=1420, h=760):
    """How much of the population has been found, by size class.

    Three CATEGORIES, not a continuum — so the axis is categorical and the
    bars sit at fixed positions well inside the frame. The first version put
    them on a log-diameter axis, which pushed the end bars onto the frame
    edges and clipped them, and it computed a power-law curve that it then
    never drew at all.

    Ink = catalogued. Terracotta outline = the part still out there. The
    accented rule is the 90% the survey was told to reach. Fractions are
    published (SOURCES.md), not computed here — this plate is a ledger.
    """
    classes = [("1 km +", 0.90), ("140 m +", 0.40), ("30 m +", 0.05)]
    TARGET = 0.90

    img = Image.new("RGB", (w, h), WHITE)
    dr = ImageDraw.Draw(img)
    m = {'l': 92, 'r': 64, 't': 52, 'b': 84}
    pwid, ph = w - m['l'] - m['r'], h - m['t'] - m['b']

    def Y(v):
        return m['t'] + ph - v * ph

    for frac in (0.25, 0.5, 0.75, 1.0):
        dr.line([(m['l'], Y(frac)), (m['l'] + pwid, Y(frac))],
                fill=(226, 222, 210), width=1)

    # the mandate rule is a REFERENCE, so it goes down first and the bars
    # cover it. Drawn last it landed on top of the kilometre bar's own edge
    # and read as part of that bar.
    dr.line([(m['l'], Y(TARGET)), (m['l'] + pwid, Y(TARGET))], fill=ACCT, width=5)

    slot = pwid / len(classes)
    bw = slot * 0.40
    for i, (_, comp) in enumerate(classes):
        x = m['l'] + slot * (i + 0.5)
        dr.rectangle([x - bw / 2, Y(1.0), x + bw / 2, Y(0.0)], outline=GHOST, width=3)
        if comp < TARGET:          # only an UNMET class carries the terracotta gap
            dr.rectangle([x - bw / 2, Y(1.0), x + bw / 2, Y(comp)], outline=ACC, width=5)
        dr.rectangle([x - bw / 2, Y(comp), x + bw / 2, Y(0.0)], fill=INK)
    dr.line([(m['l'], m['t']), (m['l'], m['t'] + ph), (m['l'] + pwid, m['t'] + ph)],
            fill=INK, width=3)
    dr.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "completeness.png")
    print("  completeness.png  " + ", ".join(f"{n} -> {c:.0%}" for n, c in classes)
          + f";  mandate rule at {TARGET:.0%}")


# ═════════════════════════════════════════════════════════════════════════════
def main():
    print(f"[gen_neo] seed {SEED} -> {OUT}")
    detect_plate()
    stamp_plate()
    tracklet_plate()
    b_cap, d, p_pk, s_pk = prob_plate()
    bplane_plate(b_cap, d)
    completeness_plate()
    print("[gen_neo] done — six plates. If any number above looks wrong, the "
          "plate is wrong; fix the physics, not the picture.")


if __name__ == "__main__":
    main()
