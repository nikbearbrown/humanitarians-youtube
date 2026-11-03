"""
Primary evidence for "You're Only Seeing Half the Curve".

Reproduces double descent with random Fourier features ridgeless regression --
the same model family Belkin, Hsu, Ma & Mandal used in PNAS 2019 (they ran it
on an MNIST subset; this uses a synthetic target so the script needs no data
download and runs in a few seconds).

Setup
-----
  n = 100 training examples, fixed.
  The model is a linear fit on p random Fourier features cos(w_i . x + b_i),
  with w_i drawn once and REUSED as p grows, so the p=200 model literally
  contains the p=100 model's features. Only p changes along the x axis.
  No regularisation: we take the minimum-norm least-squares solution
  (np.linalg.pinv), which is what gradient descent from zero converges to.

What it shows
-------------
  p <  n : the classical regime. Test error falls, then rises -- the U-curve.
  p == n : the interpolation threshold. Exactly enough parameters to hit the
           training data exactly, and the fit is forced. Test error explodes.
  p >  n : the modern regime. Many different parameter settings fit the data
           perfectly; min-norm picks the smallest of them. Test error falls
           again, and goes BELOW the best the classical regime could reach.

Every number spoken or shown in the video comes out of this file.
Run:  python double_descent_evidence.py
"""
import numpy as np

GAMMA, NOISE = 0.3, 0.2          # feature bandwidth; label noise sd
D, N_TRAIN, N_TEST, P_MAX = 8, 100, 8000, 4000
SEEDS = 12
P_GRID = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95,
          100,
          105, 110, 120, 140, 180, 250, 400, 700, 1200, 2000, 4000]


def teacher(X):
    """A fixed smooth function of the inputs. Nothing about it is special."""
    return (np.sin(X[:, 0]) + 0.5 * X[:, 1] ** 2
            - 0.8 * X[:, 2] * X[:, 3] + 0.3 * X[:, 4])


def one_run(seed):
    rng = np.random.default_rng(seed)
    W = rng.normal(0, GAMMA, (P_MAX, D))
    b = rng.uniform(0, 2 * np.pi, P_MAX)

    Xtr = rng.normal(0, 1, (N_TRAIN, D))
    Xte = rng.normal(0, 1, (N_TEST, D))
    mu, sd = teacher(Xtr).mean(), teacher(Xtr).std()
    ytr = (teacher(Xtr) - mu) / sd + rng.normal(0, NOISE, N_TRAIN)
    yte = (teacher(Xte) - mu) / sd

    train, test = {}, {}
    for p in P_GRID:
        f = lambda X: np.sqrt(2.0 / p) * np.cos(X @ W[:p].T + b[:p])
        Ptr, Pte = f(Xtr), f(Xte)
        w = np.linalg.pinv(Ptr, rcond=1e-13) @ ytr     # min-norm least squares
        train[p] = float(np.mean((Ptr @ w - ytr) ** 2))
        test[p] = float(np.mean((Pte @ w - yte) ** 2))
    return train, test


def main():
    runs = [one_run(s) for s in range(SEEDS)]
    med_tr = {p: float(np.median([r[0][p] for r in runs])) for p in P_GRID}
    med_te = {p: float(np.median([r[1][p] for r in runs])) for p in P_GRID}

    print(__doc__.split("Run:")[0].strip())
    print(f"\n{SEEDS} seeds, {N_TRAIN} training examples, median over seeds\n")
    print(f"{'params p':>9} {'p/n':>6} {'train MSE':>11} {'test MSE':>11}   regime")
    for p in P_GRID:
        regime = ("CLASSICAL" if p < N_TRAIN
                  else "<<< INTERPOLATION THRESHOLD" if p == N_TRAIN else "modern")
        print(f"{p:>9} {p/N_TRAIN:>6.2f} {med_tr[p]:>11.5f} {med_te[p]:>11.3f}   {regime}")

    lo_y, lo_p = min((v, k) for k, v in med_te.items() if k < N_TRAIN)
    hi_y, hi_p = min((v, k) for k, v in med_te.items() if k > N_TRAIN)
    peak = med_te[N_TRAIN]

    print("\n--- the three numbers the video uses ---")
    print(f"  best the CLASSICAL rule can reach   p={lo_p:<5} test MSE {lo_y:.2f}")
    print(f"  at the interpolation threshold      p={N_TRAIN:<5} test MSE {peak:.0f}"
          f"   ({peak/lo_y:.0f}x worse)")
    print(f"  deep in the MODERN regime           p={hi_p:<5} test MSE {hi_y:.2f}"
          f"   ({100*(1-hi_y/lo_y):.0f}% better than the classical best)")

    wins = sum(min(v for k, v in r[1].items() if k > N_TRAIN)
               < min(v for k, v in r[1].items() if k < N_TRAIN) for r in runs)
    ratios = [min(v for k, v in r[1].items() if k > N_TRAIN)
              / min(v for k, v in r[1].items() if k < N_TRAIN) for r in runs]
    print(f"\n  the modern regime beats the classical best in {wins}/{SEEDS} seeds")
    print(f"  worst seed still {100*(1-max(ratios)):.0f}% better; median {100*(1-np.median(ratios)):.0f}% better")
    print(f"\n  train MSE at p={N_TRAIN}: {med_tr[N_TRAIN]:.1e}  "
          f"and it stays there for every larger p -- which is why training error "
          f"cannot tell you where you are on this curve.")


if __name__ == "__main__":
    main()
