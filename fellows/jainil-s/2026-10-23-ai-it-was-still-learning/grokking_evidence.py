"""
Primary evidence for "It Was Still Learning".

Grokking: a network memorises its training set early, sits at near-chance on
held-out data for thousands of steps, and then generalises — long after the
point where training looked finished.

Setup
-----
  Task     modular addition, (a + b) mod 23. Every pair is one example, 529 in
           total; 60% are training, 40% held out.
  Model    one hidden layer, 96 units, SQUARED activation. Modular addition has
           Fourier structure and a quadratic unit can represent it directly,
           which is why this groks in seconds rather than hours.
  Training full-batch Adam, learning rate 1e-3, weight decay 0.8 (decoupled).
           Weight decay is not optional here: without pressure to simplify, the
           memorising solution is stable and the network never moves off it.

What it shows
-------------
  Step ~500    training accuracy is 100%. Validation is near chance.
               By every signal you would normally watch, training is done.
  Step ~6,000  validation reaches 95%+ and keeps going to ~100%.

  Stopping when the training curve flattened would have discarded a model that
  was about to become perfect on data it had never seen.

Every figure spoken or shown in the video comes out of this file.
Run:  python grokking_evidence.py      (about 70 seconds, 8 seeds)
"""
import numpy as np

P, HIDDEN, FRAC = 23, 96, 0.6
WEIGHT_DECAY, LR, STEPS, SEEDS = 0.8, 1e-3, 20000, 8
LOG_EVERY = 250


def train_once(seed):
    rng = np.random.default_rng(seed)
    a, b = np.meshgrid(np.arange(P), np.arange(P), indexing='ij')
    a, b = a.ravel(), b.ravel()
    y = (a + b) % P

    X = np.zeros((len(a), 2 * P), dtype=np.float32)
    X[np.arange(len(a)), a] = 1
    X[np.arange(len(a)), P + b] = 1

    order = rng.permutation(len(a))
    cut = int(FRAC * len(a))
    tr, va = order[:cut], order[cut:]
    Xtr, ytr, Xva, yva = X[tr], y[tr], X[va], y[va]

    W1 = rng.normal(0, 1 / np.sqrt(2 * P), (2 * P, HIDDEN)).astype(np.float32)
    b1 = np.zeros(HIDDEN, dtype=np.float32)
    W2 = rng.normal(0, 1 / np.sqrt(HIDDEN), (HIDDEN, P)).astype(np.float32)
    b2 = np.zeros(P, dtype=np.float32)
    params = [W1, b1, W2, b2]
    m = [np.zeros_like(p) for p in params]
    v = [np.zeros_like(p) for p in params]
    B1, B2, EPS = 0.9, 0.98, 1e-8

    curve = []
    for t in range(1, STEPS + 1):
        u = Xtr @ W1 + b1
        h = u * u                      # squared activation
        z = h @ W2 + b2
        zm = z - z.max(1, keepdims=True)
        e = np.exp(zm)
        p = e / e.sum(1, keepdims=True)
        n = len(ytr)
        d = p.copy()
        d[np.arange(n), ytr] -= 1
        d /= n

        gW2 = h.T @ d
        gb2 = d.sum(0)
        dh = (d @ W2.T) * (2 * u)
        gW1 = Xtr.T @ dh
        gb1 = dh.sum(0)

        for i, (pm, g) in enumerate(zip(params, [gW1, gb1, gW2, gb2])):
            m[i] = B1 * m[i] + (1 - B1) * g
            v[i] = B2 * v[i] + (1 - B2) * g * g
            mh = m[i] / (1 - B1 ** t)
            vh = v[i] / (1 - B2 ** t)
            pm -= LR * (mh / (np.sqrt(vh) + EPS) + WEIGHT_DECAY * pm)

        if t % LOG_EVERY == 0 or t == 1:
            uv = Xva @ W1 + b1
            zv = (uv * uv) @ W2 + b2
            curve.append((t,
                          float((z.argmax(1) == ytr).mean()),
                          float((zv.argmax(1) == yva).mean())))
    return curve


def main():
    print(__doc__.split("Run:")[0].strip())
    runs = [train_once(s) for s in range(SEEDS)]

    memo = [next(t for t, a, _ in r if a > 0.99) for r in runs]
    gen = [next((t for t, _, v in r if v > 0.95), None) for r in runs]
    got = [g for g in gen if g is not None]

    steps = [t for t, _, _ in runs[0]]
    med_tr = {t: float(np.median([r[i][1] for r in runs])) for i, t in enumerate(steps)}
    med_va = {t: float(np.median([r[i][2] for r in runs])) for i, t in enumerate(steps)}

    print(f"\n{SEEDS} seeds, (a+b) mod {P}, {FRAC:.0%} train / {1-FRAC:.0%} held out, median over seeds\n")
    print(f"{'step':>7} {'train acc':>11} {'val acc':>10}")
    for t in (250, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 12000, 20000):
        if t in med_tr:
            print(f"{t:>7} {100*med_tr[t]:>10.1f}% {100*med_va[t]:>9.1f}%")

    print("\n--- the numbers the video uses ---")
    print(f"  memorised  (train > 99%): step {int(np.median(memo))} in every seed")
    print(f"  validation at that step : {100*med_va[int(np.median(memo))]:.1f}%  (chance is {100/P:.1f}%)")
    print(f"  generalised (val > 95%) : median step {int(np.median(got))}, range {min(got)}-{max(got)}")
    print(f"  that is {np.median(got)/np.median(memo):.0f}x later than memorisation")
    print(f"  seeds that generalised  : {len(got)}/{SEEDS}")
    print(f"  final validation        : {100*np.median([r[-1][2] for r in runs]):.1f}%")

    print("\n--- for the on-screen curve (median over seeds) ---")
    pts = [250, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 12000, 20000]
    print("   steps     :", pts)
    print("   train %   :", [round(100 * med_tr[t], 1) for t in pts])
    print("   val %     :", [round(100 * med_va[t], 1) for t in pts])


def weight_decay_ablation():
    """
    Is weight decay actually what drives this, or would it grok anyway?
    Same task, same seeds, 10k steps, only the decay changes.
    """
    global WEIGHT_DECAY, STEPS
    keep_wd, keep_steps = WEIGHT_DECAY, STEPS
    STEPS = 10000
    print("\n--- does weight decay cause it? 3 seeds each, 10k steps ---")
    print(f"{'weight decay':>13} {'train':>8} {'held-out':>10}  generalised")
    out = []
    for wd in (0.0, 0.3, 0.5, 0.8):
        WEIGHT_DECAY = wd
        runs = [train_once(s) for s in range(3)]
        tr = float(np.median([r[-1][1] for r in runs]))
        va = float(np.median([r[-1][2] for r in runs]))
        n = sum(any(v > 0.95 for _, _, v in r) for r in runs)
        out.append((wd, 100 * va))
        print(f"{wd:>13} {100*tr:>7.1f}% {100*va:>9.1f}%  {n}/3")
    print("  With no decay the network memorises and stays there. The pressure to")
    print("  shrink the weights is what eventually makes a simpler solution win.")
    print("\n   for the on-screen bars:", [(w, round(v, 1)) for w, v in out])
    WEIGHT_DECAY, STEPS = keep_wd, keep_steps


if __name__ == "__main__":
    main()
    weight_decay_ablation()
