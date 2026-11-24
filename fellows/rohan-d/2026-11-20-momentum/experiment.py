"""Every number the momentum film shows. Loss f(x,y) = 0.5 * (x^2 + 25 y^2), start (4, 1)."""
import numpy as np
H = np.array([1.0, 25.0])
f = lambda p: 0.5 * float(np.sum(H * p * p))
g = lambda p: H * p
START = np.array([4.0, 1.0])
def run(lr, beta, steps=200, tol=0.01):
    p = START.copy(); v = np.zeros(2); path = [p.copy()]
    hit = None
    for t in range(1, steps + 1):
        v = beta * v + g(p)
        p = p - lr * v
        path.append(p.copy())
        if hit is None and f(p) < tol: hit = t
    return path, hit
LR = 0.07
for beta in (0.0, 0.5, 0.8, 0.9, 0.95, 0.99):
    path, hit = run(LR, beta)
    print(f"beta {beta}: steps to loss<0.01 = {hit}")
print("start loss", f(START))
path, hit = run(LR, 0.0)
print("GD first 6 points", [np.round(p, 3).tolist() for p in path[:7]])
print("GD y signs", [round(float(p[1]), 3) for p in path[:8]])
path, hit = run(LR, 0.8)
print("momentum 0.8 first 8", [np.round(p, 3).tolist() for p in path[:9]])
# velocity components after 10 steps for momentum 0.8
p = START.copy(); v = np.zeros(2)
for t in range(10):
    v = 0.8 * v + g(p); p = p - LR * v
print("v after 10:", np.round(v, 3).tolist(), "gradient now", np.round(g(p), 3).tolist())
print("lr 0.08 GD (unstable edge) steps:", run(0.08, 0.0)[1], " lr 0.09:", run(0.09, 0.0, 30)[1])
print("---- extras ----")
path, hit = run(LR, 0.5)
print("momentum 0.5 first 8", [np.round(p, 3).tolist() for p in path[:9]], "hit", hit)
p = START.copy(); v = np.zeros(2); rows = []
for t in range(1, 6):
    gr = g(p); v = 0.5 * v + gr; rows.append((round(float(gr[0]), 2), round(float(v[0]), 2), round(float(gr[1]), 2), round(float(v[1]), 2))); p = p - LR * v
print("beta .5: (gx, vx, gy, vy) steps 1-5:", rows)
for beta in (0.5, 0.9, 0.99):
    pth, hit = run(LR, beta, 200)
    xs = [q[0] for q in pth]
    print(f"beta {beta}: min x {min(xs):.3f} at step {int(np.argmin(xs))}, loss at 200 = {f(pth[-1]):.4f}")
