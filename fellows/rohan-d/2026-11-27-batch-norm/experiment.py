"""Every number the batch-normalization film shows (numpy; seed 4)."""
import numpy as np
# --- the worked batch: one feature, four examples
A = np.array([2.0, 4.0, 6.0, 8.0]); B = np.array([200.0, 400.0, 600.0, 800.0])
def bn(x): return (x - x.mean()) / np.sqrt(x.var() + 0.0)
for name, x in (("A", A), ("B", B)):
    print(name, "mean", x.mean(), "var", x.var(), "std", round(float(x.std()), 4), "-> normalized", np.round(bn(x), 4).tolist())
xh = bn(A)
print("gamma 2, beta 1:", np.round(2 * xh + 1, 4).tolist())
# --- a tiny regression where raw feature scales differ by 100x
rng = np.random.default_rng(4)
n = 40
x1 = rng.normal(5, 2, n); x2 = rng.normal(500, 200, n)
y = 1.5 * (x1 - 5) / 2 - 2.0 * (x2 - 500) / 200 + rng.normal(0, 0.1, n)
def hessian(X): return X.T @ X / len(X)
def steps_to_tol(X, y, lr, tol=0.001, max_steps=100000):
    w = np.zeros(X.shape[1]); best = None
    Xc = X
    wopt = np.linalg.lstsq(Xc, y, rcond=None)[0]
    lopt = float(np.mean((Xc @ wopt - y) ** 2) / 2)
    for t in range(1, max_steps + 1):
        g = Xc.T @ (Xc @ w - y) / len(Xc)
        w = w - lr * g
        if float(np.mean((Xc @ w - y) ** 2) / 2) - lopt < tol * 1.0:
            return t, lopt
    return None, lopt
Xraw = np.column_stack([x1, x2, np.ones(n)])
Xn = np.column_stack([(x1 - x1.mean()) / x1.std(), (x2 - x2.mean()) / x2.std(), np.ones(n)])
for name, X in (("raw", Xraw), ("normalized", Xn)):
    ev = np.linalg.eigvalsh(hessian(X))
    lr = 1.0 / ev.max()
    steps, lopt = steps_to_tol(X, y, lr)
    print(f"{name}: eigenvalues {np.round(ev, 4).tolist()} condition {ev.max()/ev.min():.1f}  lr {lr:.6f}  steps to within 0.001 of optimum: {steps}")
# --- small batches
print("--- batch size and the batch mean")
pop = rng.normal(0, 1, 100000)
for bs in (1, 2, 8, 32):
    means = pop[: (len(pop) // bs) * bs].reshape(-1, bs).mean(axis=1)
    print(f"batch size {bs}: std of the batch mean = {means.std():.3f}")
x = np.array([3.0]); eps = 1e-5
print("batch of one: (x - mean) / sqrt(var + eps) =", float(((x - x.mean()) / np.sqrt(x.var() + eps))[0]))
