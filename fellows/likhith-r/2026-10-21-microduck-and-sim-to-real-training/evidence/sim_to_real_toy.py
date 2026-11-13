"""Toy sim-to-real run for the Microduck reel (B05 and B07 on-screen numbers).

NOT the Microduck stack. A 1-D balance task (an inverted pendulum, the textbook
stand-in for a biped staying upright) is simulated in 4,096 parallel copies with
randomized mass/length and random shoves (domain randomization). A two-gain
linear policy is improved by random search: every generation, each copy tries a
perturbed policy; copies that fall are reset and retried. The toy measures only
the simulation side (falls and their cost); it says nothing about real transfer.

Run:  python3 -I evidence/sim_to_real_toy.py   (numpy only, seeded, ~2 s)
"""
import numpy as np

SEED, N, GENS, STEPS, DT = 7, 4096, 30, 200, 0.01
rng = np.random.default_rng(SEED)


def rollout(k, length, mass, push):
    """Return a per-env fell flag for gains k (N,2)."""
    n = len(length)
    th = rng.normal(0, 0.05, n)
    om = np.zeros(n)
    fell = np.zeros(n, bool)
    for s in range(STEPS):
        u = -(k[:, 0] * th + k[:, 1] * om) / mass
        u_applied = np.clip(u, -12, 12)
        acc = 9.81 / length * np.sin(th) + u_applied + (push if s == 80 else 0)
        om = om + acc * DT
        th = th + om * DT
        fell |= np.abs(th) > 0.6
    return fell


mean, sigma = np.array([2.0, 0.2]), np.array([6.0, 1.0])
total_falls = 0
log = []
for g in range(GENS):
    k = mean + sigma * rng.standard_normal((N, 2))
    length = rng.uniform(0.8, 1.2, N)          # randomized body
    mass = rng.uniform(0.8, 1.2, N)
    push = rng.normal(0, 6.0, N)               # random shove mid-episode
    fell = rollout(k, length, mass, push)
    total_falls += int(fell.sum())
    ok = ~fell
    if ok.any():                               # keep what survived, retry the rest
        mean = 0.5 * mean + 0.5 * k[ok].mean(0)
    sigma = np.maximum(sigma * 0.85, 0.05)
    log.append((g, int(fell.sum())))

# evaluate the final policy in fresh randomized sims
kf = np.tile(mean, (N, 1))
sim_fell = rollout(kf, rng.uniform(0.8, 1.2, N), rng.uniform(0.8, 1.2, N), rng.normal(0, 6.0, N))

print(f"parallel envs: {N}  generations: {GENS}  sim steps: {N * GENS * STEPS:,}")
print(f"falls during training (all reset, hardware cost $0): {total_falls:,}")
print(f"falls per generation: first {log[0][1]:,}  last {log[-1][1]:,}")
print(f"final policy gains: k_angle={mean[0]:.1f} k_rate={mean[1]:.2f}")
print(f"final policy, fresh sims: {100 * (1 - sim_fell.mean()):.1f}% stay up")
print("falls by generation:", " ".join(str(f) for _, f in log))
