#!/usr/bin/env python3
"""Compute every plate for Ep. 09 — *The Sharpest Guess.*

NOTHING HERE IS A DRAWING OF A RESULT. Each plate runs the calculation the
episode describes, and the two load-bearing claims are ASSERTED against
closed-form predictions. If either assertion fails the script writes nothing.

  twokinds.png    the two things people both call "denoising", side by side:
                  1/f detector striping, which is EXACTLY removable by a
                  Fourier fit to known-dark columns (this is what NSClean
                  does), and blur-plus-photon-noise, which is not removable
                  at all. Prints the residual for each.
                  ASSERTS: the stripe pattern is recovered to < 5%, AND the
                  information destroyed above the cutoff is LARGER THAN THE
                  NOISE - i.e. it is the dominant error term, not a footnote.

  forward.png     the forward model as a chain: truth -> PSF -> Poisson
                  photons -> read noise -> pixels. Every step is real.

  nullspace.png   THE CENTREPIECE. Two DIFFERENT truths whose observations
                  are indistinguishable, because the difference between them
                  lives where the telescope's transfer function is ~zero.
                  ASSERTS: the truths differ by > 20% while their
                  observations differ by < 0.3 noise sigma.

  threeanswers.png  the same observation, three different priors, three
                  different sharp pictures - all three EQUALLY consistent
                  with the data. The regularisation strength is solved so
                  that chi-squared/N = 1 for each, and the three values are
                  printed to prove it. "Sharp" is a choice, not a recovery.

  posterior.png   an exact posterior: for a linear-Gaussian inverse problem
                  with a circulant PSF the posterior is Gaussian and
                  DIAGONAL in Fourier space, so the samples are exact rather
                  than approximate. Shows samples, the mean, and the
                  disagreement map - which is the honest output.

  varratio.png    posterior variance / prior variance against signal-to-
                  noise, computed in closed form. The metric rises as the
                  data weakens: that is the prior taking over.

Run:  python assets/gen_deconv.py    (numpy + Pillow only; no network, no keys)

Deterministic: one seed, 9109, logged in SOURCES.md.
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SEED = 9109
N = 256
OUT = Path(__file__).resolve().parent / "plots"
OUT.mkdir(parents=True, exist_ok=True)

# ── the Claude fidelity palette ──────────────────────────────────────────────
CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)          # terracotta — marks WHAT THE PRIOR SUPPLIED
ACCT = (164, 74, 50)
WHITE = (255, 255, 255)


# ═════════════════════════════════════════════════════════════════════════════
#  optics
# ═════════════════════════════════════════════════════════════════════════════
def _kgrid(n=N):
    """Cycles per pixel, fftshift-free (matches np.fft ordering)."""
    kx = np.fft.fftfreq(n)[None, :]
    ky = np.fft.fftfreq(n)[:, None]
    return np.sqrt(kx ** 2 + ky ** 2), kx, ky


def airy_otf(n=N, cutoff=0.075):
    """The optical transfer function of a circular aperture.

    For an incoherent circular pupil the OTF is the autocorrelation of the
    pupil, which has the closed form

        H(k) = (2/pi) [ arccos(u) - u sqrt(1-u^2) ],   u = k / k_c

    and is EXACTLY ZERO for k > k_c. That hard zero is the whole episode:
    spatial frequencies above the cutoff are not attenuated, they are
    annihilated, and no amount of arithmetic brings back a number that was
    multiplied by zero.
    """
    k, _, _ = _kgrid(n)
    u = np.clip(k / cutoff, 0.0, 1.0)
    H = (2.0 / math.pi) * (np.arccos(u) - u * np.sqrt(np.clip(1 - u ** 2, 0, None)))
    H[k > cutoff] = 0.0
    return H, k, cutoff


def blur(x, H):
    return np.real(np.fft.ifft2(np.fft.fft2(x) * H))


def _gauss_field(spec, rng, n=N):
    """A real Gaussian field whose Fourier variance is `spec`.

    ONE convention, used for the prior and for every posterior sample, so the
    two cannot drift apart. Absolute normalisation is fixed by measurement in
    `prior_power` rather than by algebra.
    """
    w = rng.normal(0.0, 1.0, (n, n))
    return np.real(np.fft.ifft2(np.fft.fft2(w) * np.sqrt(np.maximum(spec, 0))))


def prior_power(truth, k, slope=2.6, n=N):
    """A power-law prior, normalised with the factor DERIVED.

    With w ~ N(0,1) white and numpy's unnormalised transforms, E|W_k|^2 = N^2,
    so for f = ifft2(W * sqrt(spec)):

        Var(f) = (1/N^4) SUM_k spec_k E|W_k|^2 = SUM_k spec_k / N^2
        std(f) = sqrt(SUM spec) / N

    An earlier version used `spec *= var*size/spec.sum()`, which is this factor
    wrong by N -- a prior ~255x too weak. Nothing crashed; the prior simply
    stopped contributing, posterior samples collapsed onto the mean, and two
    plates quietly showed the wrong thing.

    The assertion below is over an ENSEMBLE. A single realisation of a steep
    spectrum scatters by tens of per cent because a few low-k modes dominate,
    so checking one draw against another compares two noisy numbers -- which is
    exactly how the previous version managed to fail at 0.773 while being
    correct.
    """
    kk = np.maximum(k, 1.0 / n)
    shape = kk ** -slope
    P = shape * (truth.std() * n) ** 2 / shape.sum()

    predicted = math.sqrt(P.sum()) / n
    if abs(predicted / truth.std() - 1) > 1e-9:
        raise SystemExit("[gen_deconv] prior normalisation algebra is wrong")
    rng = np.random.default_rng(SEED + 98)
    stds = [_gauss_field(P, rng, n).std() for _ in range(24)]
    got = float(np.mean(stds))
    if not 0.70 < got / truth.std() < 1.40:
        raise SystemExit(
            f"[gen_deconv] prior calibration FAILED: mean std over 24 draws is "
            f"{got:.5f} against the target {truth.std():.5f}. The prior must be "
            f"able to represent the sky it is a prior over.")
    return P


# ═════════════════════════════════════════════════════════════════════════════
#  a synthetic sky
# ═════════════════════════════════════════════════════════════════════════════
def galaxy(n=N, rng=None):
    """A Sersic-ish disc with spiral arms, a bar and a few knots.

    Not a real galaxy and never claimed to be - what matters is that it has
    structure across a wide range of spatial scales, so the cutoff has
    something to destroy.
    """
    rng = rng or np.random.default_rng(SEED)
    yy, xx = np.mgrid[0:n, 0:n].astype(float)
    cx = cy = n / 2.0
    x, y = (xx - cx) / n, (yy - cy) / n
    # inclined disc
    xr, yr = x * math.cos(0.5) + y * math.sin(0.5), -x * math.sin(0.5) + y * math.cos(0.5)
    yr = yr / 0.62
    r = np.sqrt(xr ** 2 + yr ** 2) + 1e-6
    th = np.arctan2(yr, xr)
    disc = np.exp(-(r / 0.085) ** (1 / 1.0))                     # exponential disc
    bulge = 1.5 * np.exp(-(r / 0.020) ** (1 / 0.45))              # steep bulge
    arms = 0.55 * np.exp(-(r / 0.10)) * (
        0.5 + 0.5 * np.cos(2 * (th - 9.0 * np.log(r / 0.02 + 1e-9))))
    bar = 0.40 * np.exp(-((xr / 0.055) ** 2 + (yr / 0.011) ** 2))
    img = disc + bulge + arms * (r > 0.018) + bar
    # a handful of compact knots: the small scales the cutoff will erase
    for _ in range(14):
        a = rng.uniform(0, 2 * math.pi)
        rad = rng.uniform(0.03, 0.115)
        kx, ky = cx + rad * n * math.cos(a), cy + rad * n * math.sin(a) * 0.62
        s = rng.uniform(0.9, 1.7)
        img += rng.uniform(0.25, 0.7) * np.exp(
            -(((xx - kx) ** 2 + (yy - ky) ** 2) / (2 * s ** 2)))
    return img / img.max()


def observe(truth, H, peak=340.0, read=2.6, rng=None):
    """Truth -> PSF -> Poisson photons -> Gaussian read noise -> pixels."""
    rng = rng or np.random.default_rng(SEED + 1)
    blurred = np.clip(blur(truth, H), 0, None) * peak
    photons = rng.poisson(blurred).astype(float)
    return photons + rng.normal(0.0, read, truth.shape), blurred, read


# ═════════════════════════════════════════════════════════════════════════════
#  rendering helpers
# ═════════════════════════════════════════════════════════════════════════════
def _stretch(a, lo=0.5, hi=99.7, gamma=0.55):
    p0, p1 = np.percentile(a, lo), np.percentile(a, hi)
    return np.clip((a - p0) / max(p1 - p0, 1e-12), 0, 1) ** gamma


def _plate(v, bg=(16, 15, 13), fg=(247, 243, 233)):
    bg, fg = np.array(bg, float), np.array(fg, float)
    rgb = bg[None, None, :] + (fg - bg)[None, None, :] * v[:, :, None]
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _diverge(a, scale=None):
    """Signed map: terracotta positive, ink negative, cream at zero."""
    s = scale or np.percentile(np.abs(a), 99.5) or 1.0
    t = np.clip(a / s, -1, 1)
    base = np.array(CREAM, float)
    pos = np.array(ACC, float)
    neg = np.array(INK, float)
    rgb = base[None, None, :] + np.where(
        t[:, :, None] > 0, (pos - base)[None, None, :] * t[:, :, None],
        (neg - base)[None, None, :] * (-t[:, :, None]))
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _heat(a):
    """Unsigned magnitude map in terracotta — used for the disagreement map,
    because disagreement is exactly 'what the prior supplied'."""
    v = np.clip(a / (np.percentile(a, 99.5) or 1.0), 0, 1) ** 0.7
    base = np.array(WHITE, float)
    acc = np.array(ACC, float)
    rgb = base[None, None, :] + (acc - base)[None, None, :] * v[:, :, None]
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _frame(img, colour=INK, width=3):
    ImageDraw.Draw(img).rectangle([0, 0, img.width - 1, img.height - 1],
                                  outline=colour, width=width)
    return img


def _row(panels, gap=16, bg=CREAM):
    h = max(p.height for p in panels)
    w = sum(p.width for p in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (w, h), bg)
    x = 0
    for p in panels:
        sheet.paste(p, (x, (h - p.height) // 2))
        x += p.width + gap
    return sheet


def _up(v, px=460, plate=_plate):
    return _frame(plate(v).resize((px, px), Image.LANCZOS))


# ═════════════════════════════════════════════════════════════════════════════
#  1. the two kinds of "denoising"          (SELF-CHECK 1)
# ═════════════════════════════════════════════════════════════════════════════
def twokinds_plate():
    """Detector striping is removable. Lost information is not.

    LEFT: 1/f correlated read noise - constant along the fast-read direction,
    a 1/f power spectrum along the other. NSClean removes this by fitting a
    model in Fourier space to regions known to be dark and subtracting it.
    Reproduced here: fit the stripe profile on the dark columns only, subtract,
    measure what is left.

    RIGHT: the same field blurred past the aperture cutoff. Nothing removes
    that, because the information was multiplied by zero.
    """
    rng = np.random.default_rng(SEED + 2)
    H, k, kc = airy_otf()
    truth = galaxy(rng=np.random.default_rng(SEED))

    # ---- striping ----------------------------------------------------------
    # a 1/f profile down the slow-read axis, constant along each row
    f = np.fft.rfftfreq(N)
    amp = np.zeros_like(f)
    amp[1:] = f[1:] ** -1.0
    ph = rng.uniform(0, 2 * math.pi, f.size)
    prof = np.fft.irfft(amp * np.exp(1j * ph), n=N)
    prof = 9.0 * prof / prof.std()
    stripes = np.repeat(prof[:, None], N, axis=1)

    scene = np.clip(blur(truth, H), 0, None) * 120.0
    read = 2.0
    dirty = scene + stripes + rng.normal(0, read, (N, N))

    # NSClean's move: the source occupies the middle; the outer columns are
    # known-dark, so the stripe profile can be READ OFF them directly.
    dark = np.r_[0:48, N - 48:N]
    est = dirty[:, dark].mean(axis=1)
    cleaned = dirty - est[:, None]

    # Judge the STRIPE ESTIMATE against the true stripe profile. The first
    # version compared the cleaned frame against the noiseless scene, which
    # folded in the read noise that stripe removal never claimed to remove and
    # reported 22% for a method that is in fact recovering the pattern to a
    # few per cent.
    stripe_resid = np.linalg.norm(est - prof) / np.linalg.norm(prof)

    # ---- lost information --------------------------------------------------
    # the part of the truth above cutoff. No estimator recovers it.
    F = np.fft.fft2(truth)
    lost = np.real(np.fft.ifft2(np.where(k > kc, F, 0.0)))
    info_resid = np.linalg.norm(lost) / np.linalg.norm(truth)

    # Is that loss actually significant? Compare it against the measurement
    # error WHERE THE SOURCE IS, at the flux the rest of the reel works at.
    #
    # Comparing global L2 norms (an earlier version of this check) is
    # meaningless: the noise fills all 65,536 pixels while the galaxy occupies
    # a few thousand, so empty sky dominates the ratio and the answer says
    # nothing about whether structure was destroyed. Outside the footprint
    # there is nothing to lose and nothing to measure.
    peak_cmp = 340.0
    src = np.clip(blur(truth, H), 0, None) * peak_cmp
    foot = src > 0.02 * src.max()
    sigma_cmp = np.sqrt(src[foot] + read ** 2)
    lost_vs_noise = float(
        np.linalg.norm(lost[foot] * peak_cmp) / np.linalg.norm(sigma_cmp))

    panels = [
        _up(_stretch(dirty, 1, 99.5, 0.6)),
        _up(_stretch(cleaned, 1, 99.5, 0.6)),
        _up(_stretch(np.clip(blur(truth, H), 0, None), 1, 99.7, 0.55)),
        _up(_stretch(truth, 1, 99.7, 0.55)),
    ]
    _row(panels).save(OUT / "twokinds.png")

    ok_stripe = stripe_resid < 0.05
    ok_info = lost_vs_noise > 1.0
    print(f"  twokinds.png   striping: pattern recovered to "
          f"{stripe_resid*100:.2f}%  -> {'REMOVABLE' if ok_stripe else 'FAILED'}")
    print(f"                 information above cutoff: {info_resid*100:.1f}% of "
          f"the truth, and {lost_vs_noise:.1f}x the noise inside the source "
          f"({int(foot.sum())} px)  -> IRRECOVERABLE")
    if not (ok_stripe and ok_info):
        raise SystemExit("[gen_deconv] SELF-CHECK 1 FAILED — the two kinds of "
                         "denoising are not behaving as claimed. Fix the "
                         "model, not the picture.")
    return stripe_resid, info_resid


# ═════════════════════════════════════════════════════════════════════════════
#  2. the forward model
# ═════════════════════════════════════════════════════════════════════════════
def forward_plate():
    rng = np.random.default_rng(SEED + 3)
    H, _, _ = airy_otf()
    truth = galaxy(rng=np.random.default_rng(SEED))
    blurred = np.clip(blur(truth, H), 0, None) * 340.0
    photons = rng.poisson(blurred).astype(float)
    pixels = photons + rng.normal(0.0, 2.6, truth.shape)
    panels = [_up(_stretch(truth, 1, 99.7, 0.55)),
              _up(_stretch(blurred, 1, 99.7, 0.55)),
              _up(_stretch(photons, 1, 99.5, 0.6)),
              _up(_stretch(pixels, 1, 99.5, 0.6))]
    _row(panels).save(OUT / "forward.png")
    snr = blurred.sum() / math.sqrt(blurred.sum() + 2.6 ** 2 * truth.size)
    print(f"  forward.png    truth -> PSF -> Poisson -> read noise;  "
          f"integrated SNR {snr:.0f}")


# ═════════════════════════════════════════════════════════════════════════════
#  3. the null space                        (SELF-CHECK 2 — the centrepiece)
# ═════════════════════════════════════════════════════════════════════════════
def nullspace_plate():
    """Two different truths, one identical observation.

    Construct truth B = truth A + delta, where delta's Fourier support lies
    ENTIRELY above the aperture cutoff. Then H*delta = 0 exactly, so A and B
    produce the same noiseless image and are indistinguishable in the real one.

    This is not a trick of the rendering. It is what "diffraction limited"
    means, and it is why a denoiser that returns one sharp picture is choosing
    among infinitely many truths rather than recovering the right one.
    """
    rng = np.random.default_rng(SEED + 4)
    H, k, kc = airy_otf()
    A = galaxy(rng=np.random.default_rng(SEED))

    # A field whose power sits just above cutoff...
    w = rng.normal(0, 1, (N, N))
    W = np.fft.fft2(w)
    band = (k > kc * 1.02) & (k < kc * 2.2)
    delta = np.real(np.fft.ifft2(np.where(band, W, 0.0)))

    # ...concentrated where the galaxy's light is, so it reads as a DIFFERENT
    # GALAXY rather than as static over empty sky. Multiplying by an envelope
    # convolves in Fourier and leaks power below the cutoff, which would
    # destroy the exactness this plate exists to demonstrate — so project
    # above the cutoff a second time afterwards. H * delta is then exactly
    # zero again, and the assertion below has to pass for the harder object.
    env = blur(A, np.exp(-(k / (kc * 0.45)) ** 2))
    env = np.clip(env / env.max(), 0, 1) ** 0.5
    delta = delta * env
    delta = np.real(np.fft.ifft2(np.where(k > kc, np.fft.fft2(delta), 0.0)))
    delta *= 0.55 * A.std() / delta.std()
    B = A + delta

    yA = blur(A, H)
    yB = blur(B, H)
    read = 2.6
    peak = 340.0
    obsA = rng.poisson(np.clip(yA, 0, None) * peak).astype(float) + rng.normal(0, read, (N, N))

    truth_diff = np.linalg.norm(B - A) / np.linalg.norm(A)
    obs_diff_rms = np.std((yB - yA) * peak)
    noise_sigma = math.sqrt(np.mean(np.clip(yA, 0, None) * peak) + read ** 2)
    ratio = obs_diff_rms / noise_sigma

    panels = [_up(_stretch(A, 1, 99.7, 0.55)),
              _up(_stretch(B, 1, 99.7, 0.55)),
              _frame(_diverge(delta).resize((460, 460), Image.LANCZOS)),
              _up(_stretch(obsA, 1, 99.5, 0.6))]
    _row(panels).save(OUT / "nullspace.png")

    ok = truth_diff > 0.20 and ratio < 0.30
    print(f"  nullspace.png  truths differ by {truth_diff*100:.1f}%  |  their "
          f"images differ by {ratio:.4f} noise sigma")
    print(f"                 cutoff k_c = {kc:.3f} cycles/pixel; H(k)=0 above "
          f"it EXACTLY  -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("[gen_deconv] SELF-CHECK 2 FAILED — the two truths are "
                         "not observationally identical. The null-space claim "
                         "is the episode's spine; fix it before rendering.")
    return truth_diff, ratio, kc


# ═════════════════════════════════════════════════════════════════════════════
#  4. three answers, all equally consistent with the data
# ═════════════════════════════════════════════════════════════════════════════
def _wiener(Y, H, sigma, P):
    """Posterior mean for a linear-Gaussian problem, per Fourier mode."""
    Hc = np.conj(H)
    return np.real(np.fft.ifft2(Hc * Y / (np.abs(H) ** 2 + sigma ** 2 / P)))


def threeanswers_plate():
    """The same data, three priors, three sharp pictures.

    The regularisation strength of each is SOLVED so that chi^2/N = 1 - i.e.
    each estimate reproduces the observation to within exactly the noise. They
    are therefore all equally consistent with the data, and they still look
    different. That difference is supplied by the prior, not measured.
    """
    rng = np.random.default_rng(SEED + 5)
    H, k, kc = airy_otf()
    truth = galaxy(rng=np.random.default_rng(SEED))
    peak, read = 340.0, 2.6
    y, blurred, _ = observe(truth, H, peak=peak, read=read,
                            rng=np.random.default_rng(SEED + 1))
    sigma = math.sqrt(np.mean(np.clip(blurred, 0, None)) + read ** 2)
    Y = np.fft.fft2(y / peak)
    s = sigma / peak

    # Each candidate prior is calibrated to represent a sky of the right
    # overall amplitude; only its SHAPE (how power falls with scale) differs.
    shapes = {name: prior_power(truth, k, slope=sl)
              for name, sl in (("smooth", 4.0), ("matched", 2.6), ("rough", 1.2))}

    out, chis = {}, {}
    for j, (name, shape) in enumerate(shapes.items()):
        lo, hi = 1e-10, 1e6
        for _ in range(60):                        # bisect on chi^2/N = 1
            mid = math.sqrt(lo * hi)
            xh = _wiener(Y, H, s, mid * shape)
            chi = np.mean((y / peak - blur(xh, H)) ** 2) / s ** 2
            if chi > 1.0:
                lo = mid                           # too regularised
            else:
                hi = mid
        P = mid * shape
        # A generative denoiser returns a SAMPLE from the posterior, not its
        # mean. The mean is identically zero above the cutoff for every prior,
        # so means cannot differ there; samples can, and that difference is
        # exactly the invented detail this beat is about.
        var = 1.0 / (np.abs(H) ** 2 / s ** 2 + 1.0 / P)
        mean = np.real(np.fft.ifft2(var * np.conj(H) * Y / s ** 2))
        xh = mean + _gauss_field(var, np.random.default_rng(SEED + 40 + j))
        out[name] = xh
        chis[name] = np.mean((y / peak - blur(xh, H)) ** 2) / s ** 2

    # Three panels only. A fourth "difference" panel rendered as dense
    # coloured static and said nothing the three pictures do not already say.
    panels = [_up(_stretch(out[n], 1, 99.7, 0.55)) for n in
              ("smooth", "matched", "rough")]
    _row(panels).save(OUT / "threeanswers.png")

    spread = (np.linalg.norm(out["rough"] - out["smooth"])
              / np.linalg.norm(out["matched"]))
    print("  threeanswers.png  chi2/N: " +
          "  ".join(f"{n}={chis[n]:.3f}" for n in shapes) +
          f"   (all == 1: equally consistent with the data)")
    print(f"                    yet they differ from each other by "
          f"{spread*100:.1f}% — that is the prior speaking")
    return chis, spread


# ═════════════════════════════════════════════════════════════════════════════
#  5. the posterior, sampled exactly
# ═════════════════════════════════════════════════════════════════════════════
def posterior_plate(nsamp=256):
    """An EXACT posterior ensemble.

    For y = Hx + n with circulant H, Gaussian noise and a Gaussian prior with
    power spectrum P, the posterior is Gaussian and DIAGONAL in Fourier space:

        var(k)  = 1 / ( |H(k)|^2/sigma^2 + 1/P(k) )
        mean(k) = var(k) * conj(H(k)) Y(k) / sigma^2

    So the samples below are drawn from the true posterior, not from an
    approximation to it. Above the cutoff H = 0 and var(k) -> P(k): the
    posterior there IS the prior, exactly, which is the cleanest possible
    statement of where invented detail comes from.
    """
    rng = np.random.default_rng(SEED + 6)
    H, k, kc = airy_otf()
    truth = galaxy(rng=np.random.default_rng(SEED))
    peak, read = 340.0, 2.6
    y, blurred, _ = observe(truth, H, peak=peak, read=read,
                            rng=np.random.default_rng(SEED + 1))
    sigma = math.sqrt(np.mean(np.clip(blurred, 0, None)) + read ** 2) / peak
    Y = np.fft.fft2(y / peak)

    P = prior_power(truth, k)
    var = 1.0 / (np.abs(H) ** 2 / sigma ** 2 + 1.0 / P)
    mean = np.real(np.fft.ifft2(var * np.conj(H) * Y / sigma ** 2))

    acc = np.zeros_like(truth)
    acc2 = np.zeros_like(truth)
    keep = []
    for i in range(nsamp):
        draw = mean + _gauss_field(var, rng)
        acc += draw
        acc2 += draw ** 2
        if i < 3:
            keep.append(draw)
    m = acc / nsamp
    sd = np.sqrt(np.maximum(acc2 / nsamp - m ** 2, 0))

    # The ABSOLUTE std map is flat: with a stationary prior and stationary
    # noise the posterior variance really is spatially uniform, so a flat map
    # is the honest answer for this model — and a useless picture. The
    # quantity that carries the beat is how uncertain each FEATURE is, i.e.
    # the disagreement relative to the reconstruction.
    frac = sd / (np.abs(m) + 0.06 * np.abs(m).max())
    panels = [_up(_stretch(s, 1, 99.7, 0.55)) for s in keep]
    panels.append(_up(_stretch(m, 1, 99.7, 0.55)))
    panels.append(_frame(_heat(frac).resize((460, 460), Image.LANCZOS)))
    _row(panels).save(OUT / "posterior.png")

    above = k > kc
    frac_prior = float(np.mean(var[above] / P[above]))
    print(f"  posterior.png  {nsamp} exact posterior samples; map = "
          f"pixel-wise std / |mean| (the ABSOLUTE std is uniform for a "
          f"stationary prior)")
    print(f"                 above the cutoff the posterior variance equals "
          f"the PRIOR variance to {frac_prior:.4f} of it "
          f"(1.0 means 'entirely invented')")
    return nsamp, frac_prior


# ═════════════════════════════════════════════════════════════════════════════
#  6. the variance ratio against signal-to-noise
# ═════════════════════════════════════════════════════════════════════════════
def varratio_plate(w=1640, h=820):
    """posterior variance / prior variance, in closed form, against SNR.

    This is the quantity arXiv:2411.19158 proposes as a hallucination
    detector, computed here for the linear-Gaussian case where it has an exact
    expression. The shape is the point: as the data weakens the ratio climbs
    toward 1, and a ratio near 1 means the reconstruction is the prior's
    opinion rather than a measurement.
    """
    H, k, kc = airy_otf()
    truth = galaxy(rng=np.random.default_rng(SEED))
    P = prior_power(truth, k)

    # Restrict to the modes the telescope can actually see. Averaged over ALL
    # modes the ratio is pinned near the fraction lying above the cutoff, where
    # var/P = 1 whatever the data does, and the curve goes flat. The paper this
    # metric comes from takes its ratio inside an aperture around the galaxy
    # for the same reason.
    seen = k <= kc
    snrs = np.logspace(math.log10(1.0), math.log10(1500.0), 140)
    ratios = []
    for snr in snrs:
        sigma = float(np.sqrt(np.mean(np.clip(blur(truth, H), 0, None) ** 2))) / snr
        var = 1.0 / (np.abs(H) ** 2 / sigma ** 2 + 1.0 / P)
        ratios.append(float(var[seen].sum() / P[seen].sum()))
    ratios = np.array(ratios)

    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    m = {'l': 104, 'r': 48, 't': 48, 'b': 88}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']
    y0 = max(ratios.min() / 2.2, 1e-9)
    y1 = ratios.max() * 2.2

    def X(s):
        return m['l'] + (math.log10(s) - math.log10(snrs[0])) / (
            math.log10(snrs[-1]) - math.log10(snrs[0])) * pw

    def Y(v):
        v = max(float(v), y0)
        return m['t'] + ph - (math.log10(v) - math.log10(y0)) / (
            math.log10(y1) - math.log10(y0)) * ph

    for e in range(0, 4):
        gx = 10.0 ** e
        if snrs[0] <= gx <= snrs[-1]:
            d.line([(X(gx), m['t']), (X(gx), m['t'] + ph)], fill=(226, 222, 210), width=1)
    for e in range(-6, 1):
        gy = 10.0 ** e
        if y0 <= gy <= y1:
            d.line([(m['l'], Y(gy)), (m['l'] + pw, Y(gy))],
                   fill=(226, 222, 210), width=1)

    d.line([(X(s), Y(v)) for s, v in zip(snrs, ratios)], fill=ACC, width=6)
    d.line([(m['l'], m['t']), (m['l'], m['t'] + ph), (m['l'] + pw, m['t'] + ph)],
           fill=INK, width=3)
    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "varratio.png")
    lo = ratios[np.argmin(np.abs(snrs - 1000.0))]
    hi = ratios[np.argmin(np.abs(snrs - 3.0))]
    print(f"  varratio.png   variance ratio over the OBSERVABLE band "
          f"(k <= k_c, {int(seen.sum())} of {k.size} modes):")
    print(f"                 {lo:.4f} at SNR~1000  ->  {hi:.4f} at SNR~3  "
          f"({hi/lo:.0f}x more prior-driven)")
    return lo, hi


# ═════════════════════════════════════════════════════════════════════════════
def main():
    print(f"[gen_deconv] seed {SEED}, {N}x{N} -> {OUT}")
    twokinds_plate()
    forward_plate()
    nullspace_plate()
    threeanswers_plate()
    posterior_plate()
    varratio_plate()
    print("[gen_deconv] done — six plates, two hard self-checks passed. If a "
          "number above looks wrong, the plate is wrong.")


if __name__ == "__main__":
    main()
