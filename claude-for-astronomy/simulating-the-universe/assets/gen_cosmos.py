#!/usr/bin/env python3
"""gen_cosmos.py — every plate used by the simulating-the-universe reel.

Nothing here is downloaded or lifted from a published figure. This generator
**actually runs the two calculations the episode is about**, in 2D:

  1. a Gaussian random field with a CDM-like power spectrum  -> initial conditions
  2. the ZEL'DOVICH APPROXIMATION: move every particle once, in a straight line,
     along the initial displacement field. This is the cheap linear guess the
     real emulator starts from.
  3. a particle-mesh N-BODY solve: deposit mass on a grid, solve Poisson with an
     FFT, kick and drift, repeat. This is the expensive thing the emulator is
     replacing.

So the "cheap guess vs the real thing" comparison on screen is a measured
result, not an illustration. The residual plate is literally where the
Zel'dovich approximation is wrong, and the power-spectrum plate is the measured
P(k) of both fields.

    python assets/gen_cosmos.py

Deterministic: same seed in, byte-identical PNGs out. Seed is logged in
SOURCES.md.

WHY THESE ARE DARK PLATES
  Eps. 04 and 06 shipped dark photographic plates and never had trouble with
  GATE V's contrast check; Ep. 05 lost two passes to near-white plot noise being
  counted as ink. The cosmic web is naturally bright-on-dark, which is both the
  honest rendering and the safe one. The one line plot is deliberately drawn with
  few, dark strokes for the same reason.

CAVEAT STATED ON SCREEN
  This is a 2D toy at 512^2. It is the right *shape* of both calculations and
  the wrong *scale* — a production run is 3D with trillions of particles. Every
  beat that shows a plate says so.
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent / "plots"
OUT.mkdir(parents=True, exist_ok=True)

N = 512          # grid cells per side
NP = 768         # particles per side — MORE than cells on purpose:
                 # one-per-cell leaves the initial lattice visible as
                 # moire in the voids, where particles barely move.
BOX = 1.0        # box side, code units
SEED = 7717

TERRA = (217, 119, 87)
TERRA_D = (164, 74, 50)
INK = (61, 57, 41)
GHOST = (185, 180, 160)


# ── the initial field ────────────────────────────────────────────────────────

def _kgrid(n, box=BOX):
    """Wavenumber grids for an n x n real FFT layout."""
    kx = np.fft.fftfreq(n, d=box / n) * 2 * np.pi
    ky = np.fft.fftfreq(n, d=box / n) * 2 * np.pi
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    K2 = KX ** 2 + KY ** 2
    return KX, KY, K2


def _power(k, ns=0.96, keq=42.0):
    """A CDM-like shape: P ~ k^ns on large scales, turning over and falling as
    ~k^(ns-4) on small ones. Not a fit to any survey — the point is that the
    field has a turnover, so structure has a preferred scale and the web looks
    like a web rather than like noise."""
    with np.errstate(divide='ignore', invalid='ignore'):
        p = k ** ns / (1.0 + (k / keq) ** 2) ** 2
    return np.nan_to_num(p)


def initial_field(seed=SEED, n=N):
    """A Gaussian random field, unit variance, with the power spectrum above."""
    rng = np.random.default_rng(seed)
    white = rng.normal(0, 1, (n, n))
    KX, KY, K2 = _kgrid(n)
    K = np.sqrt(K2)
    amp = np.sqrt(_power(K))
    amp[0, 0] = 0.0                              # no mean mode
    fk = np.fft.fft2(white) * amp
    d = np.real(np.fft.ifft2(fk))
    d /= d.std()
    return d, (KX, KY, K2)


def displacement(delta, kg):
    """Zel'dovich displacement: psi = -i k / k^2 * delta_k. This is the whole
    linear theory of structure formation in one line — every particle gets one
    velocity, and it never changes."""
    KX, KY, K2 = kg
    dk = np.fft.fft2(delta)
    inv = np.zeros_like(K2)
    nz = K2 > 0
    inv[nz] = 1.0 / K2[nz]
    px = np.real(np.fft.ifft2(1j * KX * inv * dk))
    py = np.real(np.fft.ifft2(1j * KY * inv * dk))
    return px, py


# ── mass assignment ──────────────────────────────────────────────────────────

def cic(x, y, n=N, box=BOX):
    """Cloud-in-cell deposit of particles onto an n x n grid, periodic."""
    gx = (x % box) / box * n
    gy = (y % box) / box * n
    i0 = np.floor(gx).astype(np.int64)
    j0 = np.floor(gy).astype(np.int64)
    fx = gx - i0
    fy = gy - j0
    i0 %= n
    j0 %= n
    i1 = (i0 + 1) % n
    j1 = (j0 + 1) % n
    flat = np.zeros(n * n)
    for ii, jj, wgt in ((i0, j0, (1 - fx) * (1 - fy)), (i1, j0, fx * (1 - fy)),
                        (i0, j1, (1 - fx) * fy), (i1, j1, fx * fy)):
        flat += np.bincount(ii * n + jj, weights=wgt, minlength=n * n)
    return flat.reshape(n, n)


def grid_sample(field, x, y, n=N, box=BOX):
    """Bilinear read-back of a grid field at particle positions (periodic)."""
    gx = (x % box) / box * n
    gy = (y % box) / box * n
    i0 = np.floor(gx).astype(np.int64)
    j0 = np.floor(gy).astype(np.int64)
    fx = gx - i0
    fy = gy - j0
    i0 %= n
    j0 %= n
    i1 = (i0 + 1) % n
    j1 = (j0 + 1) % n
    return (field[i0, j0] * (1 - fx) * (1 - fy) + field[i1, j0] * fx * (1 - fy)
            + field[i0, j1] * (1 - fx) * fy + field[i1, j1] * fx * fy)


# ── the two calculations ─────────────────────────────────────────────────────

def lagrangian_grid(npart=NP, box=BOX):
    q = (np.arange(npart) + 0.5) / npart * box
    QX, QY = np.meshgrid(q, q, indexing='ij')
    return QX.ravel(), QY.ravel()


def zeldovich(delta, kg, D=1.0, npart=NP):
    """THE CHEAP GUESS. One straight-line move per particle: x = q + D * psi(q).
    Exact while displacements are small, and progressively wrong once particles
    start to cross — which is exactly when structure forms."""
    px, py = displacement(delta, kg)
    qx, qy = lagrangian_grid(npart)
    sx = grid_sample(px, qx, qy)
    sy = grid_sample(py, qx, qy)
    return qx + D * sx, qy + D * sy, (px, py)


def pm_nbody(delta, kg, D=1.0, steps=200, npart=NP, n=N, box=BOX, a0=0.10):
    """THE EXPENSIVE THING. A particle-mesh gravity solve: deposit mass, solve
    Poisson with an FFT, kick velocities by the force, drift positions, repeat.

    Time variable is the linear growth factor D (equivalently `a` in
    Einstein-de Sitter). With Poisson written as lap(phi) = delta and g = -grad(phi),
    the comoving equation of motion is

        dv/dD = -(3 / 2D) v  +  (3 / 2D^2) g

    Both terms matter. The first is the Hubble drag; the second is gravity. The
    normalisation is fixed by requiring that the ZEL'DOVICH solution x = q + D*psi
    (so v = psi, dv/dD = 0) is an exact solution in the linear regime, where
    g = D*psi. Drop the drag term and the two calculations disagree by a factor
    of twenty on the largest scales — which is how the first version of this
    file was caught.

    Because the Zel'dovich growing mode is an exact solution of this system in
    the linear regime, the two plates START identical by construction. The
    difference between them at D=1 is therefore the genuinely non-linear part,
    not an artefact of mismatched initial conditions.
    """
    KX, KY, K2 = kg
    inv = np.zeros_like(K2)
    nz = K2 > 0
    inv[nz] = 1.0 / K2[nz]

    px, py = displacement(delta, kg)
    qx, qy = lagrangian_grid(npart)
    sx = grid_sample(px, qx, qy)
    sy = grid_sample(py, qx, qy)

    x, y = qx + a0 * sx, qy + a0 * sy     # Zel'dovich positions at a0
    vx, vy = sx.copy(), sy.copy()         # and its growing-mode velocity, dx/dD = psi

    da = (D - a0) / steps
    a = a0

    def accel(x, y):
        rho = cic(x, y, n, box) * float(n * n) / float(npart * npart)
        dk = np.fft.fft2(rho - 1.0)
        phik = -dk * inv                  # lap(phi) = delta
        gx = np.real(np.fft.ifft2(-1j * KX * phik))
        gy = np.real(np.fft.ifft2(-1j * KY * phik))
        return grid_sample(gx, x, y, n, box), grid_sample(gy, x, y, n, box)

    for _ in range(steps):
        ah = a + 0.5 * da
        ax, ay = accel(x, y)              # kick (half)
        vx += (-1.5 / a * vx + 1.5 / a ** 2 * ax) * 0.5 * da
        vy += (-1.5 / a * vy + 1.5 / a ** 2 * ay) * 0.5 * da
        x += vx * da                      # drift (full)
        y += vy * da
        ax, ay = accel(x, y)              # kick (half)
        vx += (-1.5 / ah * vx + 1.5 / ah ** 2 * ax) * 0.5 * da
        vy += (-1.5 / ah * vy + 1.5 / ah ** 2 * ay) * 0.5 * da
        a += da
    return x, y


# ── rendering ────────────────────────────────────────────────────────────────

def _web_plate(rho, gamma=1.15, lo=0.015, hi=1.0, warm=True, soft=0.9):
    """Bright web on near-black, arcsinh-stretched.

    `gamma` is deliberately ABOVE 1. The first version used 0.38, which lifted
    the voids to a flat mid-tone and threw away the whole dynamic range of the
    picture — the web is mostly empty, and the emptiness has to read as empty.
    `soft` is a sub-cell smoothing that removes the residual particle lattice.
    """
    r = _smooth(rho, soft) if soft else rho
    v = np.arcsinh(np.clip(r, 0, None) * 6.0)
    v = v / (np.percentile(v, 99.8) + 1e-9)
    v = np.clip(v, 0, 1) ** gamma
    a = np.clip(lo + (hi - lo) * v, 0, 1)
    if warm:
        rr = (np.clip(a * 1.02, 0, 1) * 255).astype(np.uint8)
        gg = (a ** 1.07 * 247).astype(np.uint8)
        bb = (a ** 1.24 * 231).astype(np.uint8)
    else:
        rr = gg = bb = (a * 255).astype(np.uint8)
    return Image.fromarray(np.dstack([rr, gg, bb]).transpose(1, 0, 2), "RGB")


def _frame(img, colour=(28, 26, 24), width=3):
    ImageDraw.Draw(img).rectangle([0, 0, img.width - 1, img.height - 1],
                                  outline=colour, width=width)
    return img


def _smooth(f, sigma_cells):
    """Gaussian smooth on the grid, via FFT."""
    n = f.shape[0]
    KX, KY, K2 = _kgrid(n)
    fk = np.fft.fft2(f) * np.exp(-0.5 * K2 * (sigma_cells * BOX / n) ** 2)
    return np.real(np.fft.ifft2(fk))


def measured_power(rho, nbins=28):
    """The measured P(k) of a density field — a real measurement off the plate,
    which is what makes the comparison plate honest."""
    n = rho.shape[0]
    d = rho / rho.mean() - 1.0
    dk = np.fft.fft2(d) / (n * n)
    p2 = np.abs(dk) ** 2
    _, _, K2 = _kgrid(n)
    K = np.sqrt(K2).ravel()
    P = p2.ravel()
    kmin = 2 * np.pi / BOX
    kmax = np.pi * n / BOX
    edges = np.geomspace(kmin, kmax * 0.7, nbins + 1)
    idx = np.digitize(K, edges) - 1
    ks, ps = [], []
    for b in range(nbins):
        m = idx == b
        if m.sum() > 4:
            ks.append(K[m].mean())
            ps.append(P[m].mean())
    return np.array(ks), np.array(ps)


def power_plate(name, curves, w=1180, h=760):
    """A clean ink-on-white log-log P(k) plot. Few strokes, all dark — the
    contrast lesson from Ep. 05."""
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    m = {'l': 96, 'r': 34, 't': 34, 'b': 74}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']
    allk = np.concatenate([c[0] for c in curves])
    allp = np.concatenate([c[1] for c in curves])
    kx0, kx1 = allk.min(), allk.max()
    py0, py1 = allp[allp > 0].min(), allp.max()

    def X(k):
        return m['l'] + (math.log10(k) - math.log10(kx0)) / (math.log10(kx1) - math.log10(kx0)) * pw

    def Y(p):
        p = max(p, py0)
        return m['t'] + ph - (math.log10(p) - math.log10(py0)) / (math.log10(py1) - math.log10(py0)) * ph

    # decade gridlines only — no minor clutter
    dk0, dk1 = math.floor(math.log10(kx0)), math.ceil(math.log10(kx1))
    for e in range(int(dk0), int(dk1) + 1):
        k = 10.0 ** e
        if kx0 <= k <= kx1:
            d.line([(X(k), m['t']), (X(k), m['t'] + ph)], fill=(222, 218, 205), width=1)
    dp0, dp1 = math.floor(math.log10(py0)), math.ceil(math.log10(py1))
    for e in range(int(dp0), int(dp1) + 1):
        p = 10.0 ** e
        if py0 <= p <= py1:
            d.line([(m['l'], Y(p)), (m['l'] + pw, Y(p))], fill=(222, 218, 205), width=1)

    for (ks, ps, colour, width) in curves:
        pts = [(X(k), Y(p)) for k, p in zip(ks, ps) if p > 0]
        d.line(pts, fill=colour, width=width)

    d.line([(m['l'], m['t']), (m['l'], m['t'] + ph), (m['l'] + pw, m['t'] + ph)],
           fill=INK, width=3)
    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / name)


def zoom_pair(name, rho_a, rho_b, cx, cy, half=30, w=1180, h=600):
    """A side-by-side zoom on the same region in both calculations.

    The window WRAPS: the box is periodic, so clamping at the edge (which the
    first version did) both distorts the physics and hands `_web_plate` a
    non-square array. `np.take(..., mode='wrap')` is the correct extraction.
    """
    def cut(r):
        n = r.shape[0]
        ii = np.arange(cx - half, cx + half)
        jj = np.arange(cy - half, cy + half)
        sub = np.take(np.take(r, ii, axis=0, mode='wrap'), jj, axis=1, mode='wrap')
        im = _web_plate(sub, gamma=1.05, soft=0.6)
        return im.resize((h - 20, h - 20), Image.LANCZOS)

    a, b = cut(rho_a), cut(rho_b)
    img = Image.new("RGB", (w, h), (255, 255, 255))
    side = h - 20
    gap = (w - 2 * side) // 3
    img.paste(a, (gap, 10))
    img.paste(b, (gap * 2 + side, 10))
    d = ImageDraw.Draw(img)
    d.rectangle([gap, 10, gap + side - 1, h - 11], outline=(28, 26, 24), width=3)
    d.rectangle([gap * 2 + side, 10, gap * 2 + 2 * side - 1, h - 11],
                outline=TERRA, width=5)
    img.save(OUT / name)


def main():
    print(f"[gen_cosmos] grid {N}^2, {NP*NP:,} particles, seed {SEED}")
    delta, kg = initial_field()

    # 1. initial conditions: the field before anything has moved.
    #    Rendered with the SAME polarity as every other plate — overdense
    #    bright, underdense dark — but at low amplitude, because the early
    #    universe really is almost smooth. The first version ran this through
    #    the density stretch, which inverted it (dark lumps on a light page)
    #    and would have read as a reversal halfway through the episode.
    ic = _smooth(delta, 1.4)
    u = np.clip(0.5 + ic / (4.5 * ic.std()), 0, 1)
    a = 0.20 + 0.52 * u
    rr = (np.clip(a * 1.02, 0, 1) * 255).astype(np.uint8)
    gg = (a ** 1.07 * 247).astype(np.uint8)
    bb = (a ** 1.24 * 231).astype(np.uint8)
    icimg = Image.fromarray(np.dstack([rr, gg, bb]).transpose(1, 0, 2), "RGB")
    _frame(icimg).save(OUT / "ic.png")

    # 2. the cheap guess
    zx, zy, _ = zeldovich(delta, kg, D=1.0)
    rho_z = cic(zx, zy)
    _frame(_web_plate(rho_z)).save(OUT / "zeldovich.png")

    # 3. the expensive thing
    nx, ny = pm_nbody(delta, kg, D=1.0, steps=48)
    rho_n = cic(nx, ny)
    _frame(_web_plate(rho_n)).save(OUT / "nbody.png")

    # 4. where the cheap guess is wrong.
    #    Diverging map kept INSIDE the Claude palette: terracotta where the
    #    N-body has piled up more mass than Zel'dovich (the collapsed cores and
    #    filaments it fails to build), ink where it has less (the voids it
    #    over-empties). The first version used red/blue, which is not in the
    #    palette and read as somebody else's figure.
    da = _smooth(rho_n, 1.5) - _smooth(rho_z, 1.5)
    sc = np.percentile(np.abs(da), 99.0) + 1e-9
    t = np.clip(da / sc, -1, 1)
    pos, neg = np.clip(t, 0, 1) ** 0.7, np.clip(-t, 0, 1) ** 0.7
    base = np.array([242.0, 240.0, 233.0])          # cream
    ter = np.array([217.0, 119.0, 87.0])            # terracotta
    ink = np.array([61.0, 57.0, 41.0])              # ink
    chan = []
    for c in range(3):
        v = base[c] + pos * (ter[c] - base[c]) + neg * (ink[c] - base[c])
        chan.append(np.clip(v, 0, 255).astype(np.uint8))
    res = Image.fromarray(np.dstack(chan).transpose(1, 0, 2), "RGB")
    _frame(res, colour=INK).save(OUT / "residual.png")

    # 5. the measured power spectra
    kz, pz = measured_power(rho_z)
    kn, pn = measured_power(rho_n)
    # the first two bins hold a handful of modes each and are pure noise
    power_plate("power.png", [(kn[2:], pn[2:], INK, 5), (kz[2:], pz[2:], TERRA, 5)])

    # 6. a zoom on the biggest DISAGREEMENT, in both.
    #    Centring on the densest structure showed two panels that looked the
    #    same, which defeats the beat: what has to be visible is that the cheap
    #    answer fails to build the core.
    diff = _smooth(np.abs(da), 4.0)
    cx, cy = np.unravel_index(np.argmax(diff), diff.shape)
    zoom_pair("halo_zoom.png", rho_n, rho_z, int(cx), int(cy), half=30)

    # how wrong is the cheap guess, in one number the beat can quote?
    lo = kz < 60
    frac = np.median(np.abs(pz[lo] - pn[lo]) / pn[lo])
    hi = kz > 200
    frach = np.median(np.abs(pz[hi] - pn[hi]) / pn[hi])
    print(f"[gen_cosmos] Zel'dovich vs PM N-body, median |dP/P|:")
    print(f"               large scales (k<60):  {frac*100:5.1f}%")
    print(f"               small scales (k>200): {frach*100:5.1f}%")
    print(f"[gen_cosmos] densest structure at cell ({cx}, {cy})")
    for p in sorted(OUT.glob("*.png")):
        im = Image.open(p)
        print(f"  {p.name:18s} {im.size[0]}x{im.size[1]}")


if __name__ == "__main__":
    main()
