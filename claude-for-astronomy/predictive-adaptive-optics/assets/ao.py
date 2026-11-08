"""
ao.py -- the air, the lag, and the predictor.

Ep. 16 `predictive-adaptive-optics`.  Every number the episode puts on
screen is computed here and ASSERTED in gen_ao.py.

----------------------------------------------------------------------
The physics in one paragraph
----------------------------------------------------------------------
An adaptive-optics loop measures the wavefront, computes a correction,
and moves a mirror.  That round trip takes a fixed delay tau.  Under
Taylor frozen-flow the turbulence does not EVOLVE, it TRANSLATES at the
wind speed -- so a delay of tau seconds is exactly a displacement of
v*tau metres, and the residual is the phase structure function evaluated
at that displacement:

    sigma^2_lag(tau) = D_phi(v tau) = 6.88 (v tau / r0)^(5/3)
                     = (tau / tau0)^(5/3),    tau0 = 0.314 r0 / v

because 6.88 * 0.314^(5/3) = 0.9986.  The textbook coherence time is the
structure function in disguise.  The lag is not a clock problem, it is a
GEOMETRY problem -- and prediction works for precisely the reason the
error exists: a sliding pattern has a future you can read off its past.

----------------------------------------------------------------------
How the time series is built (exactly, not approximately)
----------------------------------------------------------------------
A von Karman phase screen is synthesised by FFT on a periodic grid at
PIX = 2 cm.  Wind blows along +x at WIND m/s, so one 1 ms loop frame is
0.5 pixels.  A half-pixel copy of each screen is made by multiplying its
spectrum by a phase ramp -- for a periodic band-limited field that shift
is EXACT, not interpolated (the Nyquist row and column are zeroed first
so the half-shift stays strictly real).  Frame t then reads the screen of
parity t%2 rolled by t//2 whole pixels.  No interpolation error anywhere.
"""

import math

import numpy as np
from scipy.special import j0, j1

# ---------------------------------------------------------------- site
R0_500 = 0.15        # m   Fried parameter at 500 nm  (stated parameter)
L0 = 25.0            # m   von Karman outer scale
WIND = 10.0          # m/s single frozen layer, along +x
D_TEL = 8.0          # m   aperture
LAM0 = 500e-9        # m   wavelength r0 is quoted at
LAM_H = 1.65e-6      # m   H band, where the science camera usually sits

# ------------------------------------------------------------- sampling
PIX = 0.02           # m / pixel
DT = 1.0e-3          # s / loop frame  -> 1 kHz, as Keck II runs its PyWFS
NX = 4096            # 81.92 m along the wind
NY = 2048            # 40.96 m across it
SUB = 4              # pupil subsample for the modal projection (8 cm)
NSUB = 4             # sub-pixel steps of the frozen translation (5 mm)

# ------------------------------------------------------------ the loop
DELAY_FRAMES = 2     # 2 ms; Keck II measured 1.7 ms for its PyWFS
N_MODES = 60         # Zernike Noll 2..61 -- the correctable band
N_TAPS = 12          # how far back the predictor is allowed to look
RIDGE = 1e-3         # regularisation, relative to mean feature power

TAU0 = 0.314 * R0_500 / WIND          # s -- 4.71 ms at these parameters

# how many 1 ms frames one screen yields before it wraps
FRAMES_PER_SCREEN = 2 * NX


# ======================================================================
# Zernike modes, Noll ordering and Noll normalisation
# ======================================================================

def noll_to_nm(j):
    """Noll index j (1-based) -> (n, m).  j=1 is piston."""
    n = 0
    j1 = j - 1
    while j1 > n:
        n += 1
        j1 -= n
    m = (-1) ** j * ((n % 2) + 2 * int((j1 + ((n + 1) % 2)) / 2.0))
    return n, m


def _radial(n, m, rho):
    """Zernike radial polynomial R_n^|m|(rho)."""
    m = abs(m)
    out = np.zeros_like(rho)
    for k in range((n - m) // 2 + 1):
        num = (-1) ** k * math.factorial(n - k)
        den = (math.factorial(k)
               * math.factorial((n + m) // 2 - k)
               * math.factorial((n - m) // 2 - k))
        out += (num / den) * rho ** (n - 2 * k)
    return out


def zernike_basis(n_modes, grid_n):
    """
    (n_modes, npup) basis plus the boolean pupil mask on a grid_n x grid_n
    grid spanning the aperture.  The basis is re-orthonormalised on the
    DISCRETE pupil so that mean(Z_i Z_j) == delta_ij to machine level;
    Noll normalisation is only exact on the continuous disc.
    """
    ax = (np.arange(grid_n) + 0.5) / grid_n * 2.0 - 1.0   # -1 .. +1
    xx, yy = np.meshgrid(ax, ax, indexing="xy")
    rho = np.hypot(xx, yy)
    theta = np.arctan2(yy, xx)
    mask = rho <= 1.0
    r = rho[mask]
    th = theta[mask]

    out = np.zeros((n_modes, r.size), dtype=np.float64)
    for i in range(n_modes):
        j = i + 2                      # skip piston
        n, m = noll_to_nm(j)
        rad = _radial(n, m, r)
        if m == 0:
            z = math.sqrt(n + 1.0) * rad
        elif m > 0:
            z = math.sqrt(2.0 * (n + 1.0)) * rad * np.cos(m * th)
        else:
            z = math.sqrt(2.0 * (n + 1.0)) * rad * np.sin(abs(m) * th)
        out[i] = z

    out -= out.mean(axis=1, keepdims=True)          # drop piston leakage
    gram = (out @ out.T) / r.size
    chol = np.linalg.cholesky(gram)
    out = np.linalg.solve(chol, out)
    return out, mask


# ======================================================================
# von Karman phase screens
# ======================================================================

def phase_screen(rng, nx=NX, ny=NY, pix=PIX, r0=R0_500, l0=L0):
    """
    One periodic von Karman screen in radians of phase at LAM0.

        Phi(f) = 0.0229 r0^(-5/3) (f^2 + 1/L0^2)^(-11/6)     [rad^2 m^2]

    Returns float32 (ny, nx).  The Nyquist row and column are zeroed so a
    later half-pixel Fourier shift stays strictly real.
    """
    fx = np.fft.fftfreq(nx, d=pix)
    fy = np.fft.fftfreq(ny, d=pix)
    fxx, fyy = np.meshgrid(fx, fy, indexing="xy")
    f2 = fxx ** 2 + fyy ** 2

    psd = 0.0229 * r0 ** (-5.0 / 3.0) * (f2 + (1.0 / l0) ** 2) ** (-11.0 / 6.0)
    psd[0, 0] = 0.0                                  # piston is meaningless
    psd[ny // 2, :] = 0.0                            # kill Nyquist row
    psd[:, nx // 2] = 0.0                            # kill Nyquist column

    dfx = 1.0 / (nx * pix)
    dfy = 1.0 / (ny * pix)
    amp = np.sqrt(psd * dfx * dfy)

    z = rng.standard_normal((ny, nx)) + 1j * rng.standard_normal((ny, nx))
    spec = z * amp
    # ifft2 divides by nx*ny; multiply back to get sum_k a_k exp(i 2pi k.r).
    # NO extra sqrt(2) here.  z is a circular complex Gaussian with
    # E|z|^2 = 2, so E|spec_k|^2 = 2 P_k; taking the real part halves that
    # back to P_k and the screen variance is sum_k P_k, as required.  An
    # earlier sqrt(2) made every structure function exactly 2x too big --
    # caught by comparing against the exact discrete PSD, not by eye.
    scr = np.real(np.fft.ifft2(spec)) * (nx * ny)
    return scr.astype(np.float32)


def half_pixel_shift(scr):
    """
    Exact half-pixel LOOK-AHEAD along +x of a periodic band-limited
    screen:  out[c] == scr[c + 0.5].

    The sign is the whole point.  modal_series reads odd frame t from
    this copy at column ix + t//2 and needs that to mean position t/2.
    With the ramp the other way the pupil position sequence came out
    0, -0.5, 1.0, 0.5, 2.0, 1.5 ... -- a zigzag, not a translation, which
    made every ODD delay look worse than its neighbours and the lag error
    non-monotonic in tau.  shift_twice == roll(-1) is asserted in
    gen_ao.py so the sign can never drift again.
    """
    nx = scr.shape[1]
    kx = np.fft.fftfreq(nx)                     # cycles / pixel
    ramp = np.exp(2j * np.pi * kx * 0.5)[None, :]
    out = np.real(np.fft.ifft2(np.fft.fft2(scr.astype(np.float64)) * ramp))
    return out.astype(np.float32)


# ======================================================================
# The lag error, measured on the screen itself (full resolution)
# ======================================================================

def pupil_window(nx=NX, ny=NY, pix=PIX, d=D_TEL):
    """Index arrays for the aperture sitting at the left edge of a screen."""
    npx = int(round(d / pix))                       # 400 px across 8 m
    ax = (np.arange(npx) + 0.5) / npx * 2.0 - 1.0
    xx, yy = np.meshgrid(ax, ax, indexing="xy")
    mask = np.hypot(xx, yy) <= 1.0
    iy, ix = np.nonzero(mask)
    iy = iy + (ny - npx) // 2                       # centre it in y
    return iy.astype(np.int64), ix.astype(np.int64), npx


def lag_variance(copies_list, taus_ms, n_epochs=64, vx_sub=2, rng=None):
    """
    Piston-removed variance of phi(t) - phi(t-tau) over the aperture,
    measured directly on the screens at full 2 cm resolution.  This is the
    INDEPENDENT check on lag_spectral -- a different method, same number.

    `copies_list` is a list of sub-pixel copy sets from subpixel_copies.
    A tau of n ms is n*vx_sub sub-pixel units of displacement.
    Returns rad^2 at LAM0, one entry per tau.
    """
    rng = np.random.default_rng(7) if rng is None else rng
    iy, ix, npx = pupil_window()
    out = np.zeros(len(taus_ms), dtype=np.float64)

    for ti, tau in enumerate(taus_ms):
        off = int(tau) * int(vx_sub)
        whole, frac = off // NSUB, off % NSUB
        acc, cnt = 0.0, 0
        for copies in copies_list:
            starts = rng.integers(0, NX - npx - whole - 2, size=n_epochs)
            for s0 in starts:
                a = copies[0][iy, ix + s0].astype(np.float64)
                b = copies[frac][iy, ix + s0 + whole].astype(np.float64)
                d = b - a
                d -= d.mean()                        # piston is unobservable
                acc += float(np.mean(d * d))
                cnt += 1
        out[ti] = acc / cnt
    return out


def pupil_var_measured(screens, n_epochs=256, rng=None):
    """
    Piston-removed phase variance over the aperture, measured on the same
    screens the modal telemetry comes from.  Comparing the in-band modal
    variance against THIS (rather than against pupil_variance(), which is
    the ideal spectrum) keeps the in-band fraction apples-to-apples: a
    finite screen carries slightly less low-frequency power than the
    continuum von Karman PSD it was drawn from.
    """
    rng = np.random.default_rng(31) if rng is None else rng
    iy, ix, npx = pupil_window()
    acc, cnt = 0.0, 0
    for scr in screens:
        for s0 in rng.integers(0, NX - npx - 2, size=n_epochs):
            a = scr[iy, ix + s0].astype(np.float64)
            a -= a.mean()
            acc += float(np.mean(a * a))
            cnt += 1
    return acc / cnt


def structure_function(screens, rs_pix, n_samp=200000, rng=None):
    """<[phi(r) - phi(r+dr)]^2> along +x, for separations given in pixels."""
    rng = np.random.default_rng(11) if rng is None else rng
    out = np.zeros(len(rs_pix), dtype=np.float64)
    for i, dr in enumerate(rs_pix):
        acc, cnt = 0.0, 0
        for scr in screens:
            yy = rng.integers(0, NY, size=n_samp)
            xx = rng.integers(0, NX - dr - 1, size=n_samp)
            a = scr[yy, xx].astype(np.float64)
            b = scr[yy, xx + dr].astype(np.float64)
            acc += float(np.sum((b - a) ** 2))
            cnt += n_samp
        out[i] = acc / cnt
    return out


# ======================================================================
# The lag error, computed EXACTLY from the spectrum
# ======================================================================
#
# A 1 ms lag at 10 m/s is a 1 cm displacement -- half a pixel on the 2 cm
# screen grid, where Nyquist truncation costs several per cent.  So the
# headline numbers are integrated straight off the PSD instead, and the
# screens are kept as an independent check.
#
#   sigma^2(tau) = int Phi(f) . 4 sin^2(pi f_x v tau) . (1 - |Pi(f)|^2) d2f
#
# |Pi(f)| = 2 J1(pi D f)/(pi D f) is the normalised circular-pupil
# transfer; the (1 - |Pi|^2) factor removes piston, which no wavefront
# sensor can see and no mirror needs to correct.  Dropping that factor
# gives the textbook point-to-point structure function instead.

def pupil_transfer(f, d=D_TEL):
    """|Pi_hat(f)| for a filled circular pupil of diameter d."""
    x = np.pi * d * np.asarray(f, dtype=float)
    out = np.ones_like(x)
    nz = x > 1e-12
    out[nz] = 2.0 * j1(x[nz]) / x[nz]
    return out


def lag_spectral(tau_s, v=WIND, r0=R0_500, l0=L0, pupil=True,
                 nf=60000, fmin=1e-8, fmax=1e5):
    """
    Servo-lag phase variance in rad^2 at LAM0, for a scalar or array of
    delays.

    The angular integral is done ANALYTICALLY.  Only the sin^2 term
    depends on the direction of f, and

        int_0^2pi 4 sin^2(pi f cos(a) v tau) da = 4 pi [1 - J0(2 pi f v tau)]

    which leaves a single well-behaved radial quadrature

        sigma^2 = 4 pi int Phi(f) (1 - |Pi(f)|^2) [1 - J0(2 pi f v tau)] f df

    evaluated on a log-f grid (f df = f^2 dlnf).  Doing the angle on a
    grid instead cost 1-3 %, because sin^2 oscillates hundreds of times
    across the high-f cells.

    fmin matters more than it looks.  For Kolmogorov the low-f tail of
    the structure function falls only as fmin^(1/3), and the truncation
    is tau-dependent, so cutting at 1e-5 bends the recovered exponent to
    1.6637.  At 1e-8 it is 1.666667 exactly and sigma^2(tau0) = 0.997.

    l0=None     -> pure Kolmogorov (the textbook limit).
    pupil=False -> no pupil averaging, no piston removal: the plain
                   point-to-point structure function D_phi(v tau).
    """
    taus = np.atleast_1d(np.asarray(tau_s, dtype=float))

    lnf = np.linspace(math.log(fmin), math.log(fmax), nf)
    f = np.exp(lnf)
    dlnf = lnf[1] - lnf[0]

    if l0 is None:
        psd = 0.0229 * r0 ** (-5.0 / 3.0) * f ** (-11.0 / 3.0)
    else:
        psd = 0.0229 * r0 ** (-5.0 / 3.0) * (f ** 2 + (1.0 / l0) ** 2) ** (-11.0 / 6.0)

    geom = 1.0 - pupil_transfer(f) ** 2 if pupil else np.ones_like(f)
    w = 4.0 * np.pi * psd * geom * f ** 2 * dlnf

    out = np.empty(taus.size, dtype=float)
    for i, tau in enumerate(taus):
        out[i] = float(np.sum(w * (1.0 - j0(2.0 * np.pi * f * v * tau))))
    return out if np.ndim(tau_s) else float(out[0])


def pupil_variance(r0=R0_500, l0=L0, nf=60000, fmin=1e-8, fmax=1e5):
    """
    Total pupil-averaged, piston-removed phase variance in rad^2 at LAM0:

        sigma^2 = 2 pi int Phi(f) (1 - |Pi(f)|^2) f df

    Not lag_spectral at a huge tau -- that is 2*sigma^2 by construction and
    its J0 term oscillates far too fast for any quadrature to resolve.
    """
    lnf = np.linspace(math.log(fmin), math.log(fmax), nf)
    f = np.exp(lnf)
    psd = 0.0229 * r0 ** (-5.0 / 3.0) * (f ** 2 + (1.0 / l0) ** 2) ** (-11.0 / 6.0)
    geom = 1.0 - pupil_transfer(f) ** 2
    return float(np.sum(2.0 * np.pi * psd * geom * f ** 2 * (lnf[1] - lnf[0])))


def fit_exponent(x, y):
    """Least-squares log-log slope, and the prefactor."""
    lx, ly = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    a, b = np.polyfit(lx, ly, 1)
    return float(a), float(np.exp(b))


# ======================================================================
# Modal telemetry -- what the controller actually sees
# ======================================================================

def subpixel_copies(scr, nsub=NSUB):
    """
    nsub copies of scr, the k-th satisfying copy_k[c] == scr[c + k/nsub].
    Exact for a periodic band-limited field (the Nyquist column is zeroed
    at generation so every fractional shift stays strictly real).
    """
    nx = scr.shape[1]
    kx = np.fft.fftfreq(nx)
    spec = np.fft.fft2(scr.astype(np.float64))
    out = [scr]
    for k in range(1, nsub):
        ramp = np.exp(2j * np.pi * kx * (k / nsub))[None, :]
        out.append(np.real(np.fft.ifft2(spec * ramp)).astype(np.float32))
    return out


def modal_series(copies, basis, mask, n_frames=FRAMES_PER_SCREEN,
                 vx_sub=2, vy_px=0, chunk=512):
    """
    (n_frames, n_modes) modal telemetry for ONE frozen layer.

    Frame t sits at x = t*vx_sub/NSUB pixels, y = t*vy_px pixels.  With
    NSUB=4 and PIX=2 cm at a 1 ms frame, vx_sub counts 5 m/s per unit:
    vx_sub=2 is 10 m/s, 4 is 20 m/s, -4 is 20 m/s the other way.

    Layers add linearly in the modal basis, so a multi-layer atmosphere is
    just the sum of these -- which keeps only one layer in memory at a time.
    """
    nsub = len(copies)
    grid_n = mask.shape[0]
    npx = grid_n * SUB
    sy = (NY - npx) // 2

    gy, gx = np.nonzero(mask)
    iy0 = (sy + gy * SUB).astype(np.int64)
    ix0 = (gx * SUB).astype(np.int64)

    out = np.zeros((n_frames, basis.shape[0]), dtype=np.float64)
    t = np.arange(n_frames)
    pos = t * int(vx_sub)                 # position in 1/nsub pixels
    whole = pos // nsub                   # floors toward -inf; frac stays >=0
    frac = pos % nsub
    ypos = t * int(vy_px)

    for p in range(nsub):
        ts = t[frac == p]
        if ts.size == 0:
            continue
        src = copies[p]
        for c0 in range(0, ts.size, chunk):
            sl = ts[c0:c0 + chunk]
            cols = (ix0[None, :] + whole[sl][:, None]) % NX
            rows = (iy0[None, :] + ypos[sl][:, None]) % NY
            vals = src[rows, cols].astype(np.float64)
            vals -= vals.mean(axis=1, keepdims=True)     # piston out
            out[sl] = vals @ basis.T / basis.shape[1]
    return out


def build_telemetry(seed, layers, basis, mask, n_frames=FRAMES_PER_SCREEN,
                    r0=R0_500):
    """
    Modal telemetry for an atmosphere of one or more frozen layers.

    `layers` is a list of (weight, vx_sub, vy_px).  Weights are Cn^2
    fractions summing to 1; a layer carrying fraction w gets its own
    r0_i = r0 * w**(-3/5), which is the standard way turbulence strength
    splits across a profile.
    """
    total = np.zeros((n_frames, basis.shape[0]), dtype=np.float64)
    for i, (w, vx, vy) in enumerate(layers):
        rng = np.random.default_rng(seed * 1000 + i)
        scr = phase_screen(rng, r0=r0 * w ** (-3.0 / 5.0))
        copies = subpixel_copies(scr)
        del scr
        total += modal_series(copies, basis, mask, n_frames, vx, vy)
        del copies
    return total


# ======================================================================
# Predictors
# ======================================================================

def design(segments, delay, taps):
    """
    (X, Y) for the full spatio-temporal (EOF) predictor.  Row t uses
    c[t-delay], c[t-delay-1], ... c[t-delay-taps+1]; the target is c[t].

    `segments` is a LIST of independent telemetry runs.  Rows are built
    strictly inside each one and then concatenated, because a window that
    straddles two unrelated screens is a catastrophic outlier: its error
    is twice the FULL turbulence variance (~310 rad^2) against a typical
    row of ~0.07.  Fourteen such rows in sixteen thousand were enough to
    swamp every number in the first run of this experiment and make the
    fitted predictor look WORSE than no predictor at all.
    """
    if isinstance(segments, np.ndarray):
        segments = [segments]
    m = segments[0].shape[1]
    xs, ys = [], []
    t0 = delay + taps - 1
    for c in segments:
        rows = np.arange(t0, c.shape[0])
        x = np.empty((rows.size, m * taps), dtype=np.float64)
        for k in range(taps):
            x[:, k * m:(k + 1) * m] = c[rows - delay - k]
        xs.append(x)
        ys.append(c[rows])
    return np.vstack(xs), np.vstack(ys)


def ridge_fit(x, y, lam=RIDGE):
    """Ridge solution W with x @ W ~= y.  lam is relative to mean power."""
    p = x.shape[1]
    a = x.T @ x
    scale = np.trace(a) / p
    a[np.diag_indices_from(a)] += lam * scale
    return np.linalg.solve(a, x.T @ y)


LAM_GRID = (1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0)


def _resid(y, x, w):
    """Mean over rows of the summed squared modal error."""
    return float(np.mean(np.sum((y - x @ w) ** 2, axis=1)))


def eval_predictors(c_train, c_val, c_test, delay=DELAY_FRAMES, taps=N_TAPS,
                    noise_rad=0.0, rng=None, lams=LAM_GRID, per_mode=True):
    """
    Residual variances in rad^2 at LAM0, summed over the modal basis --
    the mean-square phase error over the pupil INSIDE the correctable band.

    Four estimators, which between them separate what prediction buys from
    looking BACK in time from what it buys from looking ACROSS the pupil:

      zero   : c_hat(t) = c(t-d).  The textbook servo lag.  No fitting.
      diag   : c_hat(t) = g_i c_i(t-d).  One scalar gain per mode -- the
               best a modal integrator can do with no memory and no
               cross-talk.  THE FAIR BASELINE: it can shrink noise, which
               `zero` cannot, so it is not punished for being handed a
               noisy sample.
      space  : c_hat(t) = W c(t-d).  One frame, all modes.  Pure SPATIAL
               prediction -- the pupil already shows you air that has not
               yet reached the part you care about.
      time   : per-mode, `taps` frames of mode i only.  Pure TEMPORAL.
      eof    : all modes, all taps.  Both.

    Every estimator picks its OWN ridge lambda on `c_val` and is then
    scored once on `c_test`.  Sharing one lambda across estimators made
    the fitted baseline come out WORSE than the unfitted one at high
    noise, which is impossible -- identity is inside its hypothesis class.

    `noise_rad` is white measurement noise (rad RMS per mode) added to the
    INPUTS of train, validation and test alike, as a real wavefront sensor
    would deliver.  The TARGET stays noise-free, so the score is the true
    residual rather than the fit to a noisy label.
    """
    rng = np.random.default_rng(23) if rng is None else rng
    segify = (lambda c: [c] if isinstance(c, np.ndarray) else list(c))
    c_train, c_val, c_test = segify(c_train), segify(c_val), segify(c_test)

    def noisy(segs):
        if noise_rad <= 0:
            return segs
        return [c + rng.normal(0.0, noise_rad, size=c.shape) for c in segs]

    x_tr, y_tr = design(noisy(c_train), delay, taps)
    x_va, _ = design(noisy(c_val), delay, taps)
    x_te, _ = design(noisy(c_test), delay, taps)
    _, y_va = design(c_val, delay, taps)           # targets are clean
    _, y_te = design(c_test, delay, taps)
    m = c_train[0].shape[1]

    def tuned(cols):
        """
        Fit on train, pick lambda on validation, score on test.  The Gram
        matrix is built ONCE and only the diagonal moves with lambda --
        X^T X is n*p^2 and would otherwise dominate the whole run.
        """
        xt, xv, xe = x_tr[:, cols], x_va[:, cols], x_te[:, cols]
        a0 = xt.T @ xt
        b0 = xt.T @ y_tr
        scale = np.trace(a0) / a0.shape[0]
        idx = np.diag_indices_from(a0)
        best = None
        for lam in lams:
            a = a0.copy()
            a[idx] += lam * scale
            w = np.linalg.solve(a, b0)
            v = _resid(y_va, xv, w)
            if best is None or v < best[0]:
                best = (v, lam, w)
        return _resid(y_te, xe, best[2]), best[1]

    first = list(range(m))
    allc = list(range(m * taps))

    v_zero = float(np.mean(np.sum((y_te - x_te[:, :m]) ** 2, axis=1)))

    # diagonal: closed form per mode, g_i = <y_i x_i> / <x_i^2>
    g = ((y_tr * x_tr[:, :m]).sum(0) / (x_tr[:, :m] ** 2).sum(0).clip(1e-30))
    g = np.diag(np.where(np.isfinite(g), g, 0.0))
    v_diag = _resid(y_te, x_te[:, :m], g)

    v_space, lam_space = tuned(first)
    v_eof, lam_eof = tuned(allc)

    out = {"zero": v_zero, "diag": v_diag, "space": v_space, "eof": v_eof,
           "lam_space": lam_space, "lam_eof": lam_eof,
           "gain_eof": v_diag / v_eof, "gain_space": v_diag / v_space,
           "gain_eof_raw": v_zero / v_eof}

    if per_mode:
        # Per-mode Grams are tiny (taps x taps); build them all once.
        grams = []
        for i in range(m):
            cols = [k * m + i for k in range(taps)]
            xt = x_tr[:, cols]
            grams.append((cols, xt.T @ xt, xt.T @ y_tr[:, i:i + 1]))
        best = None
        for lam in lams:
            res_v = np.empty_like(y_va)
            res_e = np.empty_like(y_te)
            for i, (cols, a0, b0) in enumerate(grams):
                a = a0.copy()
                a[np.diag_indices_from(a)] += lam * np.trace(a0) / taps
                wi = np.linalg.solve(a, b0)
                res_v[:, i] = y_va[:, i] - (x_va[:, cols] @ wi)[:, 0]
                res_e[:, i] = y_te[:, i] - (x_te[:, cols] @ wi)[:, 0]
            v = float(np.mean(np.sum(res_v ** 2, axis=1)))
            if best is None or v < best[0]:
                best = (v, lam, float(np.mean(np.sum(res_e ** 2, axis=1))))
        out["time"] = best[2]
        out["lam_time"] = best[1]
        out["gain_time"] = v_diag / best[2]
    return out


# ======================================================================
# Helpers the plates and the scenes both want
# ======================================================================

def tau0_of(v, r0=R0_500):
    return 0.314 * r0 / v


def lag_theory(tau_s, v=WIND, r0=R0_500):
    """sigma^2 = 6.88 (v tau / r0)^(5/3), rad^2 at LAM0."""
    return 6.88 * (v * np.asarray(tau_s, dtype=float) / r0) ** (5.0 / 3.0)


def strehl(sigma2_500, lam=LAM_H):
    """Marechal, with the variance scaled from LAM0 to lam."""
    s2 = np.asarray(sigma2_500, dtype=float) * (LAM0 / lam) ** 2
    return np.exp(-s2)
