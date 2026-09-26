#!/usr/bin/env python3
"""A toy diffusion model, trained from scratch in plain numpy — the executable
evidence for "How AI Image Generators Turn Noise Into a Picture".

It is small on purpose: 16x16 greyscale pictures of two "prompts" (a heart and
a music note), an MLP denoiser, no GPU, no downloads, no pretrained weights.
The ALGORITHM is the real one — the DDPM forward process, noise schedule and
epsilon-prediction loss of Ho, Jain & Abbeel (2020, arXiv:2006.11239), and
classifier-free guidance from Ho & Salimans (2022, arXiv:2207.12598). The
SCALE is not: Midjourney's models are vastly bigger and their design is not
published. Nothing here claims to be Midjourney.

    python train_toy_diffusion.py            # train + sample + write evidence

Writes (next to this file):
    evidence/toy_diffusion.json   every number the video shows
    evidence/run.log              stdout of this run
    evidence/weights.npz          the trained (EMA) weights
Every random draw is seeded; rerunning reproduces the same numbers.
"""
import hashlib, json, math, os, platform, sys, time

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "evidence")
os.makedirs(OUT, exist_ok=True)
LOG = open(os.path.join(OUT, "run.log"), "w", encoding="utf-8")


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


# ── the pictures ─────────────────────────────────────────────────────────────
S = 16                 # picture side, pixels
D = S * S              # one picture = 256 numbers
PROMPTS = ["heart", "music note"]
NULL = len(PROMPTS)    # the "no prompt" slot classifier-free guidance needs
SS = 8                 # supersampling for antialiased edges


def _heart(d, cx, cy, r):
    pts = []
    for k in range(120):
        a = 2 * math.pi * k / 120
        x = 16 * math.sin(a) ** 3
        y = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
        pts.append((cx + x * r / 17, cy - y * r / 17))
    d.polygon(pts, fill=255)


def _note(d, cx, cy, r):
    # an eighth note: tilted oval head, a stem, a flag
    hx, hy = cx - r * 0.30, cy + r * 0.55
    head = []
    for k in range(60):
        a = 2 * math.pi * k / 60
        x, y = 0.42 * r * math.cos(a), 0.29 * r * math.sin(a)
        c, s = math.cos(-0.45), math.sin(-0.45)
        head.append((hx + x * c - y * s, hy + x * s + y * c))
    d.polygon(head, fill=255)
    sx = hx + 0.36 * r
    w = 0.13 * r
    d.rectangle([sx - w, cy - 0.95 * r, sx + w * 0.2, hy - 0.05 * r], fill=255)
    flag = [(sx, cy - 0.95 * r), (sx + 0.55 * r, cy - 0.45 * r),
            (sx + 0.42 * r, cy - 0.05 * r), (sx + 0.30 * r, cy - 0.35 * r),
            (sx, cy - 0.55 * r)]
    d.polygon(flag, fill=255)


def draw(prompt, rng):
    """One training picture: the prompt's shape at a random place, size, tilt."""
    big = S * SS
    im = Image.new("L", (big, big), 0)
    d = ImageDraw.Draw(im)
    r = big * rng.uniform(0.30, 0.40)
    cx = big / 2 + rng.uniform(-0.12, 0.12) * big
    cy = big / 2 + rng.uniform(-0.12, 0.12) * big
    (_heart if prompt == 0 else _note)(d, cx, cy, r)
    im = im.rotate(rng.uniform(-25, 25), resample=Image.BICUBIC, center=(cx, cy))
    im = im.resize((S, S), Image.LANCZOS)
    return np.asarray(im, np.float32).reshape(-1) / 127.5 - 1.0   # [-1, 1]


# ── the noise schedule (DDPM, Ho et al. 2020, section 4) ─────────────────────
T = 1000
BETA = np.linspace(1e-4, 0.02, T, dtype=np.float64)      # beta_1 .. beta_T
ALPHA = 1.0 - BETA
ABAR = np.cumprod(ALPHA)                                  # alpha-bar_t


def time_embed(t):
    """Sinusoidal embedding of the step number, t in 1..T."""
    half = 32
    f = np.exp(-math.log(1000.0) * np.arange(half) / half)
    a = (t[:, None] / T) * 1000.0 * f[None, :]
    return np.concatenate([np.sin(a), np.cos(a)], 1).astype(np.float32)


# ── the denoiser: an MLP that guesses the noise ──────────────────────────────
H = 768
IN = D + 64 + NULL + 1


def init(rng):
    def lin(i, o, scale=1.0):
        return (rng.standard_normal((i, o)) * math.sqrt(2.0 / i) * scale).astype(np.float32), \
               np.zeros(o, np.float32)
    P = {}
    P["W1"], P["b1"] = lin(IN, H)
    P["W2"], P["b2"] = lin(H, H)
    P["W3"], P["b3"] = lin(H, H)
    P["W4"], P["b4"] = lin(H, D, 0.1)
    return P


def silu(x):
    return x / (1.0 + np.exp(-x))


def dsilu(x):
    s = 1.0 / (1.0 + np.exp(-x))
    return s * (1 + x * (1 - s))


def forward(P, x, t, c):
    onehot = np.zeros((len(c), NULL + 1), np.float32)
    onehot[np.arange(len(c)), c] = 1.0
    h0 = np.concatenate([x, time_embed(t), onehot], 1)
    z1 = h0 @ P["W1"] + P["b1"]; a1 = silu(z1)
    z2 = a1 @ P["W2"] + P["b2"]; a2 = silu(z2) + a1          # residual
    z3 = a2 @ P["W3"] + P["b3"]; a3 = silu(z3) + a2          # residual
    out = a3 @ P["W4"] + P["b4"]
    return out, (h0, z1, a1, z2, a2, z3, a3)


def backward(P, cache, g):
    h0, z1, a1, z2, a2, z3, a3 = cache
    G = {}
    G["W4"] = a3.T @ g; G["b4"] = g.sum(0)
    ga3 = g @ P["W4"].T
    gz3 = ga3 * dsilu(z3)
    G["W3"] = a2.T @ gz3; G["b3"] = gz3.sum(0)
    ga2 = gz3 @ P["W3"].T + ga3
    gz2 = ga2 * dsilu(z2)
    G["W2"] = a1.T @ gz2; G["b2"] = gz2.sum(0)
    ga1 = gz2 @ P["W2"].T + ga2
    gz1 = ga1 * dsilu(z1)
    G["W1"] = h0.T @ gz1; G["b1"] = gz1.sum(0)
    return G


# ── training ─────────────────────────────────────────────────────────────────
def train(steps=24000, batch=256, lr=6e-4, seed=0):
    rng = np.random.default_rng(seed)
    log(f"building training set: 2 prompts x 6000 pictures, {S}x{S}")
    X = np.stack([draw(p, rng) for p in (0, 1) for _ in range(6000)])
    Y = np.repeat([0, 1], 6000)
    P = init(rng)
    E = {k: v.copy() for k, v in P.items()}                 # EMA copy
    m = {k: np.zeros_like(v) for k, v in P.items()}
    v = {k: np.zeros_like(v) for k, v in P.items()}
    b1, b2, eps_ = 0.9, 0.999, 1e-8
    t0 = time.time()
    curve = []
    run = 0.0
    for step in range(1, steps + 1):
        idx = rng.integers(0, len(X), batch)
        x0, c = X[idx], Y[idx].copy()
        c[rng.random(batch) < 0.15] = NULL                  # prompt dropout (CFG)
        t = rng.integers(1, T + 1, batch)
        e = rng.standard_normal((batch, D)).astype(np.float32)
        ab = ABAR[t - 1][:, None].astype(np.float32)
        xt = np.sqrt(ab) * x0 + np.sqrt(1 - ab) * e          # the forward process
        pred, cache = forward(P, xt, t, c)
        diff = pred - e
        loss = float((diff ** 2).mean())
        G = backward(P, cache, 2.0 * diff / diff.size)
        gn = math.sqrt(sum(float((g ** 2).sum()) for g in G.values()))
        clip = min(1.0, 1.0 / (gn + 1e-12))
        a = lr * 0.5 * (1 + math.cos(math.pi * step / steps))
        for k in P:
            g = G[k] * clip
            m[k] = b1 * m[k] + (1 - b1) * g
            v[k] = b2 * v[k] + (1 - b2) * g * g
            P[k] -= a * (m[k] / (1 - b1 ** step)) / (np.sqrt(v[k] / (1 - b2 ** step)) + eps_)
            E[k] = 0.999 * E[k] + 0.001 * P[k]
        run = loss if step == 1 else 0.99 * run + 0.01 * loss
        if step % 500 == 0 or step == 1:
            curve.append([step, round(run, 5)])
            log(f"  step {step:6d}  loss {run:.4f}  {time.time() - t0:6.0f}s")
    return E, curve, time.time() - t0, X, Y


# ── sampling: start from static, remove a little noise 1000 times ────────────
def sample(P, prompt, seed, w=3.0, keep=(1000, 900, 750, 600, 450, 300, 200, 120, 60, 20, 0)):
    rng = np.random.default_rng(seed)
    x = rng.standard_normal((1, D)).astype(np.float32)     # the seed's static
    start = x.copy()
    frames, guesses = {}, {}
    frames[T] = x[0].copy()
    for t in range(T, 0, -1):
        tt = np.array([t])
        ec, _ = forward(P, x, tt, np.array([prompt]))
        eu, _ = forward(P, x, tt, np.array([NULL]))
        e = eu + w * (ec - eu)                             # classifier-free guidance
        ab = ABAR[t - 1]
        x0_hat = np.clip((x - math.sqrt(1 - ab) * e) / math.sqrt(ab), -1, 1)
        mean = (x - BETA[t - 1] / math.sqrt(1 - ab) * e) / math.sqrt(ALPHA[t - 1])
        if t > 1:
            var = BETA[t - 1] * (1 - ABAR[t - 2]) / (1 - ab)
            x = mean + math.sqrt(var) * rng.standard_normal((1, D)).astype(np.float32)
        else:
            x = mean
        if (t - 1) in keep:
            frames[t - 1] = np.clip(x[0], -1, 1).copy()
            guesses[t - 1] = x0_hat[0].copy()
    return start[0], frames, guesses


def to_u8(a):
    return [int(v) for v in np.clip((np.asarray(a) + 1) * 127.5, 0, 255).round()]


def iou(img, ref):
    return float(((img > 0) & (ref > 0)).sum() / max(1, ((img > 0) | (ref > 0)).sum()))


def main():
    log("toy diffusion — numpy", np.__version__, "| python", platform.python_version(),
        "|", platform.platform())
    P, curve, secs, X, Y = train()
    log(f"trained in {secs:.0f} s on CPU")
    np.savez(os.path.join(OUT, "weights.npz"), **P)

    # 1. the forward process on one real training picture (no model involved)
    x0 = X[3]
    rng = np.random.default_rng(11)
    e = rng.standard_normal(D).astype(np.float32)
    forward_steps = [0, 50, 150, 300, 500, 1000]
    fwd = []
    for t in forward_steps:
        ab = 1.0 if t == 0 else ABAR[t - 1]
        xt = math.sqrt(ab) * x0 + math.sqrt(1 - ab) * e
        fwd.append({"t": t, "signal": round(math.sqrt(ab), 4),
                    "noise": round(math.sqrt(1 - ab), 4), "px": to_u8(np.clip(xt, -1, 1))})
        log(f"  forward t={t:4d}  picture weight {math.sqrt(ab):.4f}  noise weight {math.sqrt(1-ab):.4f}")

    # 2. one seed, one prompt: the full reverse trajectory
    runs = []
    def run(prompt, seed):
        start, frames, guesses = sample(P, prompt, seed)
        final = frames[0]
        runs.append({"prompt": PROMPTS[prompt], "seed": seed, "start": to_u8(np.clip(start, -1, 1)),
                     "frames": {str(k): to_u8(v) for k, v in sorted(frames.items(), reverse=True)},
                     "guesses": {str(k): to_u8(v) for k, v in sorted(guesses.items(), reverse=True)},
                     "final": to_u8(final)})
        return final
    run(0, 7)                                   # heart, seed 7
    run(1, 7)                                   # same static, the other prompt
    for s in (101, 202, 303, 404):              # one prompt, four seeds = a grid
        run(0, s)
    again = sample(P, 0, 7)[1][0]               # same seed + prompt, run again
    same = bool(np.array_equal(np.array(to_u8(again)), np.array(runs[0]["final"])))
    log(f"  seed 7 heart, re-run identical: {same}")

    # how different are the four grid pictures from each other, really?
    grid = [np.array(r["final"]) for r in runs[2:6]]
    diffs = [float(np.abs(grid[i] - grid[j]).mean()) for i in range(4) for j in range(i + 1, 4)]
    log(f"  four seeds: mean pixel difference between pictures {np.mean(diffs):.1f}/255")
    # does the training data contain the output? nearest training picture
    fin = (np.array(runs[0]["final"]) / 127.5 - 1)
    near = float(np.min(np.abs(X - fin[None]).mean(1)) * 127.5)
    log(f"  seed-7 heart vs its closest training picture: mean diff {near:.1f}/255")

    params = int(sum(v.size for v in P.values()))
    out = {
        "algorithm": "DDPM (Ho, Jain & Abbeel 2020) + classifier-free guidance (Ho & Salimans 2022)",
        "side": S, "T": T, "beta": [1e-4, 0.02], "guidance": 3.0,
        "params": params, "train_pictures": int(len(X)), "train_steps": 24000,
        "train_seconds": round(secs), "loss_curve": curve,
        "forward": fwd, "runs": runs, "rerun_identical": same,
        "grid_mean_pixel_diff": round(float(np.mean(diffs)), 1),
        "nearest_training_diff": round(near, 1),
        "env": {"numpy": np.__version__, "python": platform.python_version(),
                "platform": platform.platform()},
        "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
    }
    p = os.path.join(OUT, "toy_diffusion.json")
    json.dump(out, open(p, "w", encoding="utf-8"), indent=1)
    log(f"params {params:,} | wrote {p}")
    log("sha256 toy_diffusion.json", hashlib.sha256(open(p, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
