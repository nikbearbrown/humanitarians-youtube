"""The simulator, the models and the metric for Ep. 12.

The thing being demonstrated is a property of the EVALUATION, not of the Sun,
so the data generator only has to reproduce the structure that causes the
problem. That structure is:

  1. An active region lives for days and is measured over and over, so one
     region contributes many rows that look almost identical.
  2. Whether a region flares is a property OF THE REGION, not of the row. A
     few complex regions flare repeatedly; most never produce an M-class
     flare at all.

Put those together and a row carries, in effect, the identity of its region.
Split the rows at random and the same region lands on both sides of the
split, so a flexible model can recognise the region rather than learn the
physics -- and the score you report is partly a memory test.

Nothing here is a model of the Sun. The parameters are chosen to be
illustrative of the mechanism; only the direction and rough size of the
effect are claimed, and the reel says so.
"""
import numpy as np

# ── the GOES-like class imbalance ───────────────────────────────────────────
# SWAN-SF reports 60:1 for M- and X-class flares against flare-quiet
# instances (Ahmadzadeh et al. 2021). A base rate near 1/60 is the target.
TARGET_BASE_RATE = 1.0 / 60.0


def make_regions(rng, n_regions=350, d=4, fingerprint=1.0,
                 drift=0.012, noise=0.14, p_flarer=0.07, p_quiet=0.003):
    """Generate active regions, each observed hourly over its lifetime.

    Returns a dict of arrays, all row-aligned:
      X        (n, d)  the measured features of each row
      y        (n,)    1 if an M+ flare follows within 24 h
      region   (n,)    which active region the row came from
      t        (n,)    the hour, globally, so a chronological split is possible

    `fingerprint` is the scale of the per-region constant offset -- the thing
    that makes two rows from one region look alike. Set it to 0 and the
    leakage disappears, which is the control the self-check uses.

    `drift` and `noise` are small ON PURPOSE. A real active region's magnetic
    parameters barely move from one hour to the next, which is precisely why
    its rows are near-duplicates. A first version used drift 0.12 and noise
    0.45; over a 72-hour lifetime the random walk then wandered further than
    the fingerprint itself, rows of one region ended up no more alike than
    rows of different regions, and the leak -- the whole subject of the
    episode -- was simulated away. The nearest-neighbour distance was 0.18
    under every split, which is how that showed up.
    """
    rows_X, rows_y, rows_r, rows_t = [], [], [], []
    # regions appear through the window, so time and region are entangled
    # the way they are in a real catalogue
    starts = np.sort(rng.integers(0, 24 * 300, size=n_regions))
    # A few regions are magnetically complex and flare repeatedly; most never
    # produce an M-class flare. Complexity is PARTLY visible in the features,
    # so there is genuine skill to be had -- but only partly, which is what
    # leaves room for memorising the region to beat it.
    U = rng.normal(0.0, fingerprint, size=(n_regions, d))
    pf = 1.0 / (1.0 + np.exp(-(1.6 * U[:, 0] - 1.9)))
    is_flarer = rng.random(n_regions) < pf
    for i in range(n_regions):
        life = int(rng.integers(24, 96))           # 1 to 4 days, hourly
        u = U[i]                                   # the region's fingerprint
        p = p_flarer if is_flarer[i] else p_quiet
        walk = np.cumsum(rng.normal(0.0, drift, size=(life, d)), axis=0)
        X = u[None, :] + walk + rng.normal(0.0, noise, size=(life, d))
        y = (rng.random(life) < p).astype(int)
        rows_X.append(X)
        rows_y.append(y)
        rows_r.append(np.full(life, i))
        rows_t.append(starts[i] + np.arange(life))
    return dict(X=np.vstack(rows_X), y=np.concatenate(rows_y),
                region=np.concatenate(rows_r), t=np.concatenate(rows_t))


# ── the three ways people split this data ───────────────────────────────────
def split_random(d, rng, frac=0.30):
    """Shuffle the ROWS. This is the one that leaks."""
    n = d["y"].size
    idx = rng.permutation(n)
    k = int(n * frac)
    return idx[k:], idx[:k]


def split_by_region(d, rng, frac=0.30):
    """Assign whole REGIONS to one side or the other."""
    regs = np.unique(d["region"])
    regs = rng.permutation(regs)
    k = int(regs.size * frac)
    test_regs = set(regs[:k].tolist())
    is_test = np.array([r in test_regs for r in d["region"]])
    return np.where(~is_test)[0], np.where(is_test)[0]


def split_chronological(d, rng=None, frac=0.30):
    """Train on the past, test on the future. What deployment actually is."""
    order = np.argsort(d["t"], kind="stable")
    k = int(order.size * (1 - frac))
    return order[:k], order[k:]


# ── two models, deliberately of different capacity ──────────────────────────
class Logistic:
    """Plain logistic regression by gradient descent. LOW capacity: it can
    only draw one hyperplane, so it cannot memorise which region a row is."""

    def __init__(self, iters=400, lr=0.5, l2=1e-3):
        self.iters, self.lr, self.l2 = iters, lr, l2

    def fit(self, X, y):
        self.mu, self.sd = X.mean(0), X.std(0) + 1e-9
        Z = (X - self.mu) / self.sd
        Z = np.hstack([Z, np.ones((Z.shape[0], 1))])
        w = np.zeros(Z.shape[1])
        # class weights, because the positives are ~1 in 60
        pw = np.where(y == 1, (y == 0).sum() / max((y == 1).sum(), 1), 1.0)
        for _ in range(self.iters):
            p = 1.0 / (1.0 + np.exp(-Z @ w))
            g = Z.T @ (pw * (p - y)) / Z.shape[0] + self.l2 * w
            w -= self.lr * g
        self.w = w
        return self

    def score(self, X):
        Z = (X - self.mu) / self.sd
        Z = np.hstack([Z, np.ones((Z.shape[0], 1))])
        return 1.0 / (1.0 + np.exp(-Z @ self.w))


class NearestNeighbour:
    """k-nearest-neighbour. HIGH capacity: it can answer by finding the row
    that looks most like this one -- which, after a random split, is very
    often another hour of the SAME region."""

    def __init__(self, k=25):
        # k has to be big enough to ESTIMATE a region's flare rate rather
        # than echo one neighbour's coin flip. At k=5 this model was simply
        # worse than logistic regression under every split, so its inflation
        # was the inflation of a bad number and proved nothing. At k=25 it is
        # competitive when evaluated honestly, which is the situation the
        # episode is actually about: a flexible model that looks like a
        # breakthrough under a random split and merely matches the baseline
        # under an honest one.
        self.k = k

    def fit(self, X, y):
        self.mu, self.sd = X.mean(0), X.std(0) + 1e-9
        self.Z = (X - self.mu) / self.sd
        self.y = y
        return self

    def _dists(self, X, chunk=2000):
        Q = (X - self.mu) / self.sd
        for i in range(0, Q.shape[0], chunk):
            q = Q[i:i + chunk]
            yield i, ((q[:, None, :] - self.Z[None, :, :]) ** 2).sum(-1)

    def score(self, X):
        out = np.empty(X.shape[0])
        for i, D in self._dists(X):
            nn = np.argpartition(D, self.k, axis=1)[:, :self.k]
            out[i:i + D.shape[0]] = self.y[nn].mean(1)
        return out

    def nn_distance(self, X):
        """Distance to the single closest training row. This is the leak,
        measured directly: after a random split it is near zero, because the
        closest row is the same region an hour earlier."""
        out = np.empty(X.shape[0])
        for i, D in self._dists(X):
            out[i:i + D.shape[0]] = np.sqrt(D.min(1))
        return out


# ── the metric the field actually uses ──────────────────────────────────────
def tss(y, p, thresh):
    """True Skill Statistic = TPR - FPR = sensitivity + specificity - 1.

    Chosen because it is the standard in flare forecasting and, unlike
    accuracy, it is not fooled by the base rate: always predicting "quiet"
    scores 0, not 0.98.
    """
    yh = (p >= thresh).astype(int)
    tp = int(((yh == 1) & (y == 1)).sum())
    fn = int(((yh == 0) & (y == 1)).sum())
    fp = int(((yh == 1) & (y == 0)).sum())
    tn = int(((yh == 0) & (y == 0)).sum())
    tpr = tp / max(tp + fn, 1)
    fpr = fp / max(fp + tn, 1)
    return tpr - fpr


def best_tss(y, p):
    """TSS at the threshold that maximises it -- the usual reported figure."""
    cand = np.unique(np.quantile(p, np.linspace(0.50, 0.9995, 120)))
    return max(tss(y, p, c) for c in cand)
