"""The star, the spectrum, the teacher and the student, for Ep. 14.

The student here is the real algorithm. `Cannon` is a data-driven model of
exactly the published form: a quadratic polynomial in the stellar labels
fitted independently at every wavelength pixel, then inverted at test time to
read labels back off a new spectrum. Ness et al. (2015) describe it as making
"no use of stellar models nor any line-list" beyond the reference labels,
which is the whole point of this episode -- everything it knows about physics
arrives through its training labels, and nothing else.

So the chain has four links, and only the first is nature:

    star  ->  spectrum  ->  [a physics model fits it]  ->  LABELS
                                                            |
                                        [a data-driven model fits those]
                                                            |
                                                        predictions

A data-driven model trained on labels is not measuring the star. It is
predicting what the physics model would have said about the star.

Nothing here is a model of any survey. The parameters are illustrative of the
mechanism; only the direction and rough size of the effect are claimed.
"""
import numpy as np

NPIX = 160
LABELS = ("teff", "logg", "feh")

# label ranges, loosely those of a red-giant sample
LO = np.array([4000.0, 1.5, -1.00])
HI = np.array([6500.0, 4.5, 0.40])
SCALE = np.array([1000.0, 1.0, 1.0])     # units the systematic is written in
PIVOT = np.array([5200.0, 2.8, -0.25])


def draw_stars(rng, n):
    """True stellar parameters. These are what nature has; nobody sees them."""
    u = rng.random((n, 3))
    return LO + u * (HI - LO)


# ── nature: the spectrum a star actually produces ───────────────────────────
def _line_bank(rng_seed=1414, n_lines=26):
    """Absorption lines with fixed, arbitrary sensitivities to the labels.

    The sensitivities are drawn once from a fixed seed and then frozen, so
    'nature' is the same function on every run. Lines respond to temperature,
    gravity and metallicity with different strengths and a little curvature,
    which is what makes the inverse problem non-trivial without making it
    degenerate.
    """
    r = np.random.default_rng(rng_seed)
    return dict(
        centre=np.sort(r.uniform(6, NPIX - 6, n_lines)),
        width=r.uniform(1.1, 2.4, n_lines),
        depth=r.uniform(0.08, 0.38, n_lines),
        d_teff=r.normal(0, 0.22, n_lines),
        d_logg=r.normal(0, 0.10, n_lines),
        d_feh=r.uniform(0.10, 0.55, n_lines),      # lines deepen with metals
        curv=r.normal(0, 0.05, n_lines),
    )


BANK = _line_bank()


def spectrum(theta, bank=BANK):
    """Flux for one star, or a stack of stars. Continuum normalised to 1."""
    th = np.atleast_2d(np.asarray(theta, float))
    z = (th - PIVOT) / SCALE                      # scaled labels
    x = np.arange(NPIX)[None, :]
    out = np.ones((th.shape[0], NPIX))
    for j in range(bank["centre"].size):
        s = (1.0
             + bank["d_teff"][j] * z[:, 0]
             + bank["d_logg"][j] * z[:, 1]
             + bank["d_feh"][j] * z[:, 2]
             + bank["curv"][j] * z[:, 0] * z[:, 2])
        s = np.clip(s, 0.0, None)[:, None]
        prof = np.exp(-0.5 * ((x - bank["centre"][j]) / bank["width"][j]) ** 2)
        out -= bank["depth"][j] * s * prof
    return np.clip(out, 0.02, None)


def observe(theta, rng, snr=100.0):
    f = spectrum(theta)
    return f + rng.normal(0.0, 1.0 / snr, f.shape)


# ── the teacher: a physics model that is slightly wrong ─────────────────────
def teacher_labels(theta, rng, bias=0.18, noise=0.03):
    """What the physics pipeline reports for these stars.

    `bias` is a TEMPERATURE-DEPENDENT metallicity error, in dex per 1000 K.
    This is the shape a real missing-opacity or microturbulence error takes:
    not a constant offset you would notice, but a trend across the sample
    that looks like astrophysics.

    Set bias = 0 and the teacher is unbiased, which is the control the
    self-check uses.
    """
    L = np.array(theta, float).copy()
    dteff = (L[:, 0] - PIVOT[0]) / SCALE[0]
    L[:, 2] += bias * dteff
    L[:, 0] += rng.normal(0, 25.0, L.shape[0])
    L[:, 1] += rng.normal(0, 0.04, L.shape[0])
    L[:, 2] += rng.normal(0, noise, L.shape[0])
    return L


def anchor_labels(theta, rng, noise_feh=0.08):
    """A model-independent anchor: fewer stars, noisier, but unbiased.

    This is what asteroseismic gravities and cluster members do for a real
    survey -- they are not derived from the same atmosphere model, so they do
    not carry its systematic. They are also scarcer and individually less
    precise, which is exactly the trade the episode is about.
    """
    L = np.array(theta, float).copy()
    L[:, 0] += rng.normal(0, 45.0, L.shape[0])
    L[:, 1] += rng.normal(0, 0.03, L.shape[0])
    L[:, 2] += rng.normal(0, noise_feh, L.shape[0])
    return L


# ── the student: the real data-driven model ─────────────────────────────────
class Cannon:
    """A quadratic data-driven model of stellar spectra.

    Training: at every pixel, regress flux on a quadratic expansion of the
    labels. Test: hold those per-pixel coefficients fixed and solve for the
    labels that best reproduce a new spectrum.

    It contains no physics. Its only contact with the world is the labels it
    was handed.
    """

    @staticmethod
    def _vec(z):
        z = np.atleast_2d(z)
        cols = [np.ones(z.shape[0]), z[:, 0], z[:, 1], z[:, 2],
                z[:, 0] ** 2, z[:, 0] * z[:, 1], z[:, 0] * z[:, 2],
                z[:, 1] ** 2, z[:, 1] * z[:, 2], z[:, 2] ** 2]
        return np.stack(cols, axis=1)

    def fit(self, labels, flux):
        self.mu = labels.mean(0)
        self.sd = labels.std(0) + 1e-12
        A = self._vec((labels - self.mu) / self.sd)
        # one least-squares solve per pixel, all at once
        self.coef, *_ = np.linalg.lstsq(A, flux, rcond=None)   # (10, NPIX)
        resid = flux - A @ self.coef
        self.scatter = resid.std(0) + 1e-6
        return self

    def _predict_flux(self, z):
        return self._vec(z) @ self.coef

    def predict(self, flux, iters=14, step=0.55):
        """Gauss-Newton on the scaled labels, from the training mean."""
        n = flux.shape[0]
        z = np.zeros((n, 3))
        w = 1.0 / self.scatter
        for _ in range(iters):
            model = self._predict_flux(z)
            r = (flux - model) * w
            # numerical Jacobian: 3 labels, cheap enough
            J = np.empty((n, NPIX, 3))
            for k in range(3):
                dz = np.zeros(3)
                dz[k] = 1e-3
                J[:, :, k] = ((self._predict_flux(z + dz)
                               - self._predict_flux(z - dz)) / 2e-3) * w
            for i in range(n):
                dzi, *_ = np.linalg.lstsq(J[i], r[i], rcond=None)
                z[i] += step * dzi
            z = np.clip(z, -4.0, 4.0)
        return z * self.sd + self.mu
