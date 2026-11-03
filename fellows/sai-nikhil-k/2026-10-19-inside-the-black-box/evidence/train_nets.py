#!/usr/bin/env python3
"""train_nets.py — do equally good nets agree outside their data? Ten tries, on this Mac.

Wolfram (2023), "Machine Learning, and the Training of Neural Nets": training
makes "different-but-equivalent solutions", and "if we ask, say, for an
'extrapolation' outside the region where we gave training examples, we can get
dramatically different results." This checks that claim on a constructed task.

Task (constructed, shaped like his example): a step function on [-1, 1]
    f(x) = -1 for x < -0.15,  1 for -0.15 <= x < 0.35,  0 for x >= 0.35
400 evenly spaced training points. Ten nets, identical except the random seed
that sets their starting weights: 1 -> 32 -> 32 -> 1, ReLU, mean-squared error,
full-batch Adam (lr 0.01), 4,000 steps. Plain NumPy, written out below.

Reported: each net's error on the training points, and what each predicts at
x = 3, outside the data. Seeds 0-9 are all reported; none were dropped.

Run:  python3 evidence/train_nets.py > evidence/train_nets.out
"""
import datetime
import platform

import numpy as np

SEEDS = range(10)
STEPS, LR, H = 4000, 0.01, 32
X = np.linspace(-1, 1, 400).reshape(-1, 1)
Y = np.where(X < -0.15, -1.0, np.where(X < 0.35, 1.0, 0.0))
PROBE = 3.0


def init(rng):
    def layer(i, o):
        return rng.normal(0, np.sqrt(2 / i), (i, o)), np.zeros(o)
    return [*layer(1, H), *layer(H, H), *layer(H, 1)]


def forward(p, x):
    w1, b1, w2, b2, w3, b3 = p
    z1 = x @ w1 + b1; a1 = np.maximum(0, z1)
    z2 = a1 @ w2 + b2; a2 = np.maximum(0, z2)
    return a2 @ w3 + b3, (x, z1, a1, z2, a2)


def grads(p, x, y):
    w1, b1, w2, b2, w3, b3 = p
    out, (x, z1, a1, z2, a2) = forward(p, x)
    d = 2 * (out - y) / len(x)
    g3 = a2.T @ d; gb3 = d.sum(0)
    d2 = (d @ w3.T) * (z2 > 0)
    g2 = a1.T @ d2; gb2 = d2.sum(0)
    d1 = (d2 @ w2.T) * (z1 > 0)
    g1 = x.T @ d1; gb1 = d1.sum(0)
    return [g1, gb1, g2, gb2, g3, gb3]


def train(seed):
    rng = np.random.default_rng(seed)
    p = init(rng)
    m = [np.zeros_like(a) for a in p]; v = [np.zeros_like(a) for a in p]
    for t in range(1, STEPS + 1):
        for i, g in enumerate(grads(p, X, Y)):
            m[i] = 0.9 * m[i] + 0.1 * g
            v[i] = 0.999 * v[i] + 0.001 * g * g
            p[i] = p[i] - LR * (m[i] / (1 - 0.9 ** t)) / (np.sqrt(v[i] / (1 - 0.999 ** t)) + 1e-8)
    return p


print(f"date      {datetime.datetime.now().isoformat(timespec='seconds')}")
print(f"machine   {platform.machine()} · macOS {platform.mac_ver()[0]} · "
      f"python {platform.python_version()} · numpy {np.__version__}")
print(f"task      step function on [-1, 1], {len(X)} points · net 1-{H}-{H}-1 ReLU · "
      f"Adam lr {LR} · {STEPS} steps")
print()
print(f"{'seed':>4}  {'training MSE':>12}  {'f(x) at x = 3':>14}")
mses, guesses = [], []
for s in SEEDS:
    p = train(s)
    mse = float(np.mean((forward(p, X)[0] - Y) ** 2))
    g = float(forward(p, np.array([[PROBE]]))[0][0, 0])
    mses.append(mse); guesses.append(g)
    print(f"{s:>4}  {mse:12.4f}  {g:14.3f}")
print()
print("SUMMARY")
print(f"  nets trained              {len(mses)}")
print(f"  worst training MSE        {max(mses):.4f}")
print(f"  best training MSE         {min(mses):.4f}")
print(f"  lowest guess at x = 3     {min(guesses):.2f}")
print(f"  highest guess at x = 3    {max(guesses):.2f}")
print(f"  spread at x = 3           {max(guesses) - min(guesses):.2f}")
print(f"  target range on the data  -1 to 1")
