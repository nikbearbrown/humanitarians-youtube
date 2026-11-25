"""Every number the overfitting film shows (numpy only for polyfit; seed 3)."""
import numpy as np
rng = np.random.default_rng(3)
N = 8
x = np.linspace(0, 1, N)
truth = lambda t: 2 * t
y = truth(x) + rng.normal(0, 0.25, N)
xt = np.linspace(0, 1, 200)
yt_rng = np.random.default_rng(99)
yt = truth(xt) + yt_rng.normal(0, 0.25, 200)
print("train x", np.round(x, 3).tolist())
print("train y", np.round(y, 3).tolist())
def mse(a, b): return float(np.mean((a - b) ** 2))
rows = {}
for d in range(1, 8):
    c = np.polyfit(x, y, d)
    tr = mse(np.polyval(c, x), y)
    te = mse(np.polyval(c, xt), yt)
    rows[d] = (tr, te)
    print(f"degree {d}: train {tr:.4f}  test {te:.4f}")
print("noise floor (var of noise) =", 0.25 ** 2)
# more data
rng2 = np.random.default_rng(5)
x40 = np.linspace(0, 1, 40); y40 = truth(x40) + rng2.normal(0, 0.25, 40)
c = np.polyfit(x40, y40, 7)
print("degree 7 with 40 points: train", round(mse(np.polyval(c, x40), y40), 4), "test", round(mse(np.polyval(c, xt), yt), 4))
