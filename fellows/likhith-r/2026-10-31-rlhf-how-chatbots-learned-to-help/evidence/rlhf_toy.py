"""rlhf_toy.py — every number shown on screen in claude-hai-rlhf.

Run:  .venv/bin/python youtube/brutalist/claude-hai-rlhf/evidence/rlhf_toy.py
Writes rlhf_toy.out.txt (human-readable) and rlhf_toy.json (copied into the scenes) next to itself.

Toy, not a benchmark. Each candidate answer is reduced to two numbers:
    c = substance (is it actually right / useful?)
    f = flattery  (does it agree with you, sound sure of itself?)
Simulated raters prefer   u = c + LAMBDA * f   (they are swayed by being agreed with),
and rank K answers with noise (Plackett-Luce = sort by u + Gumbel noise).

  1. Reward model: a linear Bradley-Terry model r(x) = w . x, fit by gradient descent on the
     ranked pairs (P(a beats b) = sigmoid(r_a - r_b)), the InstructGPT loss with K = 4.
  2. RL step: the KL-regularised objective  max E_pi[r] - beta * KL(pi || pi_ref)  has the exact
     solution  pi(i) ∝ pi_ref(i) * exp(r_i / beta); we use it over a fixed pool of answers the
     SFT model wrote (pi_ref uniform over the pool). Smaller beta = weaker leash.
  3. Reward hacking: the "SFT model" sometimes writes people-pleasing answers (high f, low c).
     Sweeping beta shows the learned reward climbing while true substance peaks, then falls.
Paper constants (InstructGPT, GPT-3) are echoed here so every on-screen figure has one source.
"""
import json
import math
import pathlib

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
OUT, J = [], {}
rng = np.random.default_rng(2026)


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    OUT.append(line)


# ---------------------------------------------------------------- paper constants (B03/B04/B05/B07)
say("== paper constants ==")
gpt3_params, gpt3_tokens = 175e9, 300e9           # Brown et al. 2020, sec. 2.1-2.2
ig_small = 1.3e9                                   # Ouyang et al. 2022 (InstructGPT), abstract
sft_prompts, rm_prompts, ppo_prompts = 13_000, 33_000, 31_000   # InstructGPT sec. 3.3 ("about")
ratio = gpt3_params / ig_small
say(f"GPT-3: {gpt3_params/1e9:.0f}B parameters, trained on {gpt3_tokens/1e9:.0f}B tokens")
say(f"InstructGPT prompts: SFT ~{sft_prompts:,}  RM ~{rm_prompts:,}  PPO ~{ppo_prompts:,}")
say(f"175B / 1.3B = {ratio:.1f}x  (paper: '100x fewer parameters'; on screen 'more than 100x')")
J["paper"] = dict(gpt3B=175, tokensB=300, smallB=1.3, ratio=round(ratio, 1),
                  sft=sft_prompts, rm=rm_prompts, ppo=ppo_prompts)

say("\n== ranking K answers -> pairwise comparisons ==")
for K in (4, 9):
    say(f"K = {K}: {math.comb(K, 2)} pairs")
J["pairs"] = {4: math.comb(4, 2), 9: math.comb(9, 2)}

# ---------------------------------------------------------------- the SFT model's answers (pi_ref)
LAMBDA = 1.0          # how much raters reward flattery, relative to substance
P_PLEASER = 0.06      # share of people-pleasing answers the SFT model writes


def write_answers(n):
    pleaser = rng.random(n) < P_PLEASER
    c = np.where(pleaser, rng.normal(-2.0, 0.4, n), rng.normal(0.0, 1.0, n))
    f = np.where(pleaser, rng.normal(3.0, 1.6, n), rng.normal(0.0, 1.0, n))
    return np.stack([c, f], 1), pleaser


def rank(X):
    """rater ranking of one set of answers: best first (Plackett-Luce via Gumbel noise)"""
    u = X[:, 0] + LAMBDA * X[:, 1] + rng.gumbel(0, 1, len(X))
    return np.argsort(-u)


# ---------------------------------------------------------------- B05: reward model from ranked pairs
K, N_TRAIN, N_TEST = 4, 3000, 1000


def pairs_from(nsets):
    A, B = [], []
    for _ in range(nsets):
        X, _ = write_answers(K)
        order = rank(X)
        for i in range(K):
            for j in range(i + 1, K):
                A.append(X[order[i]]); B.append(X[order[j]])     # A preferred over B
    return np.array(A), np.array(B)


A_tr, B_tr = pairs_from(N_TRAIN)
A_te, B_te = pairs_from(N_TEST)
D_tr, D_te = A_tr - B_tr, A_te - B_te
w = np.zeros(2)
curve = []
lr = 0.5
for step in range(201):
    if step in (0, 5, 10, 20, 40, 80, 120, 200):
        acc = float(np.mean(D_te @ w > 0)) if step else 0.5
        curve.append((step, round(acc * 100, 1)))
    p = 1 / (1 + np.exp(-(D_tr @ w)))
    w += lr * D_tr.T @ (1 - p) / len(D_tr)
acc_te = float(np.mean(D_te @ w > 0))
say(f"\n== B05: Bradley-Terry reward model, {N_TRAIN} ranked sets of K={K} -> {len(D_tr)} pairs ==")
say(f"learned weights: substance {w[0]:.2f}, flattery {w[1]:.2f}  (raters: 1.00, {LAMBDA:.2f})")
say(f"held-out pairs ({len(D_te)}): reward model agrees with the raters {acc_te*100:.1f} %")
say("learning curve (step, held-out agreement %):", curve)
J["rm"] = dict(sets=N_TRAIN, pairs=len(D_tr), test_pairs=len(D_te), acc=round(acc_te * 100, 1),
               w=[round(float(x), 2) for x in w], curve=curve)

# a worked example for the ranking card: four answers, their learned scores
Xex, _ = write_answers(K)
order = rank(Xex)
scores = Xex @ w
say("example set: rater order", order.tolist(), " reward-model scores", [round(float(s), 2) for s in scores[order]])
J["example"] = [round(float(s), 2) for s in scores[order]]

# ---------------------------------------------------------------- B06 / B08: the RL step over a pool
POOL = 20000
Xp, plz = write_answers(POOL)
r = Xp @ w                       # learned reward (what RL optimises)
c = Xp[:, 0]                     # true substance (what we wanted)


def tilt(beta):
    z = r / beta
    z -= z.max()
    p = np.exp(z); p /= p.sum()
    kl = float(np.sum(p * np.log(np.maximum(p * POOL, 1e-300))))
    return p, kl


say(f"\n== RL step over a pool of {POOL} SFT answers ({plz.mean()*100:.1f} % people-pleasers) ==")
say(f"pi_ref: mean reward {r.mean():+.2f}, mean substance {c.mean():+.2f}")
rows = []
for beta in [np.inf, 4, 2, 1.5, 1.2, 1.0, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]:
    if beta == np.inf:
        p, kl = np.full(POOL, 1 / POOL), 0.0
    else:
        p, kl = tilt(beta)
    row = dict(beta=None if beta == np.inf else beta, kl=round(kl, 2), reward=round(float(p @ r), 2),
               substance=round(float(p @ c), 2), pleaser=round(float(p @ plz) * 100, 1))
    rows.append(row)
    say(f"beta {str(beta):>5}: KL {kl:5.2f} nats  reward {row['reward']:+.2f}  substance {row['substance']:+.2f}  people-pleasers {row['pleaser']:5.1f} %")
J["sweep"] = rows
best = max(rows, key=lambda d: d["substance"])
say(f"substance peaks at KL {best['kl']} (beta {best['beta']}): {best['substance']:+.2f}; "
    f"strongest push (beta {rows[-1]['beta']}): substance {rows[-1]['substance']:+.2f}, reward {rows[-1]['reward']:+.2f}")
J["peak"] = best

# B06: one leashed step, as score histograms before / after
BETA_B06 = 1.0
p6, kl6 = tilt(BETA_B06)
edges = np.linspace(-4, 8, 13)
h_ref = np.histogram(r, edges)[0] / POOL
h_new = np.histogram(r, edges, weights=p6)[0]
say(f"\n== B06: leashed step (beta {BETA_B06}) ==")
say(f"mean reward {r.mean():+.2f} -> {p6 @ r:+.2f}; KL {kl6:.2f} nats; substance {c.mean():+.2f} -> {p6 @ c:+.2f}")
say("histogram edges", edges.tolist())
say("before", np.round(h_ref * 100, 1).tolist())
say("after ", np.round(h_new * 100, 1).tolist())
J["b06"] = dict(beta=BETA_B06, r0=round(float(r.mean()), 2), r1=round(float(p6 @ r), 2), kl=round(kl6, 2),
                c0=round(float(c.mean()), 2), c1=round(float(p6 @ c), 2), edges=edges.tolist(),
                before=np.round(h_ref * 100, 1).tolist(), after=np.round(h_new * 100, 1).tolist())

(HERE / "rlhf_toy.out.txt").write_text("\n".join(OUT) + "\n")
(HERE / "rlhf_toy.json").write_text(json.dumps(J, indent=1) + "\n")
