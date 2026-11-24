"""Executable evidence for "Attention, One Head at a Time" (tldr-attention).

Every number shown on screen or spoken in this film comes from this file's output
(demo/RUN-LOG.txt + demo/evidence.json). Pure Python + numpy, seeded, no ML libraries.
Run:  python demo/attention_demo.py

One head of scaled dot-product attention (Vaswani et al. 2017, eq. 1):
    Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V
on a 4-word sentence with toy integer embeddings and toy integer projection matrices.

Sizes, chosen for legibility (marked on screen as simplifications):
    d_model = 4  (each word is a list of four numbers)
    d_k     = 4  (queries and keys have four numbers, so sqrt(d_k) = 2)
    d_v     = 2  (values have two numbers, so every value and output is a point we can draw)
The real paper uses d_model = 512, d_k = d_v = 64, and 8 heads.

The weights are SEEDED TOYS, not a trained model: the pattern of who-attends-to-whom
means nothing linguistically. The machinery is exactly the real one.

SEED choice: seed 290537 was found by a scratch search over seeds 0..299999 of
numpy default_rng for these legibility criteria, which this script re-asserts:
  * every entry of X, W_Q, W_K, W_V is in {-1, 0, 1}; each embedding row has at most one 0
  * every entry of Q, K, V is in [-2, 2]; every scaled score is in [-2.5, 2.5]
  * the four value points are distinct and in convex position (each is a corner)
  * "chase"'s heaviest weight is in [0.40, 0.60], on another word, and its lightest is >= 0.06
  * no row's top two weights are within 0.06 of each other; no weight above 0.75
"""
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parent
SEED = 290537
WORDS = ["cats", "chase", "small", "dogs"]
FOCUS = 1  # "chase"


def softmax_rows(s):
    e = np.exp(s - s.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)


def r(x, nd=4):
    """Round for JSON; -0.0 -> 0.0."""
    a = np.round(np.asarray(x, dtype=float), nd) + 0.0
    return a.tolist()


rng = np.random.default_rng(SEED)
X = rng.integers(-1, 2, (4, 4))      # embeddings, one row per word
W_Q = rng.integers(-1, 2, (4, 4))    # toy stand-ins for learned projections
W_K = rng.integers(-1, 2, (4, 4))
W_V = rng.integers(-1, 2, (4, 2))
D_K = W_Q.shape[1]
SCALE = float(np.sqrt(D_K))          # = 2.0


def head(Xin):
    Q, K, V = Xin @ W_Q, Xin @ W_K, Xin @ W_V
    S = Q @ K.T
    A = softmax_rows(S / SCALE)
    return Q, K, V, S, A, A @ V


Q, K, V, S, A, O = head(X)

# ---- legibility criteria (see docstring) -------------------------------------------
def convex_position(P):
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    pts = sorted(map(tuple, P))
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return len(set(pts)) == 4 and len(lo[:-1] + up[:-1]) == 4


assert set(np.unique(np.concatenate([X.ravel(), W_Q.ravel(), W_K.ravel(), W_V.ravel()]))) <= {-1, 0, 1}
assert ((X == 0).sum(1) <= 1).all()
assert np.abs(Q).max() <= 2 and np.abs(K).max() <= 2 and np.abs(V).max() <= 2
assert np.abs(S / SCALE).max() <= 2.5
assert convex_position(V)
f = A[FOCUS]
assert 0.40 <= f.max() <= 0.60 and f.argmax() != FOCUS and f.min() >= 0.06
srt = np.sort(A, 1)
assert (srt[:, -1] - srt[:, -2] >= 0.06).all() and A.max() <= 0.75
assert np.allclose(A.sum(1), 1.0)
# hand formula check: output row = sum_j a_ij v_j
assert np.allclose(O[FOCUS], sum(A[FOCUS, j] * V[j] for j in range(4)))

ev = {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform(),
      "seed": SEED, "words": WORDS, "focus": WORDS[FOCUS],
      "sizes": {"d_model": 4, "d_k": D_K, "d_v": 2, "sqrt_d_k": SCALE,
                "paper": {"d_model": 512, "d_k": 64, "d_v": 64, "heads": 8}},
      "X": X.tolist(), "W_Q": W_Q.tolist(), "W_K": W_K.tolist(), "W_V": W_V.tolist(),
      "Q": Q.tolist(), "K": K.tolist(), "V": V.tolist(),
      "scores": S.tolist(), "scaled": r(S / SCALE, 2),
      "weights": r(A, 4), "weights2": r(A, 2), "row_sums": r(A.sum(1), 6),
      "outputs": r(O, 4), "outputs2": r(O, 2)}

# ---- the focus row, worked by hand (TANGENT zone 4) --------------------------------
q = Q[FOCUS]
ev["worked"] = {
    "word": WORDS[FOCUS], "query": q.tolist(),
    "dots": [{"key_word": WORDS[j], "key": K[j].tolist(),
              "products": (q * K[j]).tolist(), "score": int(q @ K[j]),
              "scaled": float(q @ K[j] / SCALE)} for j in range(4)],
    "exp": r(np.exp(S[FOCUS] / SCALE), 4),
    "exp_sum": round(float(np.exp(S[FOCUS] / SCALE).sum()), 4),
    "weights": r(A[FOCUS], 4),
    "output": r(O[FOCUS], 4),
    "output_terms": [r(A[FOCUS, j] * V[j], 4) for j in range(4)],
}

# ---- B11 INSTANCE: blends (weighted averages) of value points ------------------------
two = (V[0], V[2])  # cats, small
ev["blend_two"] = {"points": [WORDS[0], WORDS[2]], "a": V[0].tolist(), "b": V[2].tolist(),
                   "sweep": [{"w": w, "point": r(w * two[0] + (1 - w) * two[1], 4)}
                             for w in (0.5, 0.8, 0.2)]}
four_w = [[0.7, 0.1, 0.1, 0.1], [0.1, 0.1, 0.7, 0.1], [0.1, 0.7, 0.1, 0.1]]
ev["blend_four"] = [{"w": w, "point": r(np.array(w) @ V, 4)} for w in four_w]

# ---- B12 INSTANCE: a second row of matches, for contrast ---------------------------
ev["match_small"] = {"query": Q[2].tolist(), "scores": S[2].tolist()}

# ---- B13 NAIVE: equal weights for everyone ------------------------------------------
U = np.full((4, 4), 0.25)
ev["naive_equal"] = {"weights": 0.25, "outputs": r(U @ V, 4), "all_same": bool(np.allclose(U @ V, (U @ V)[0]))}
assert ev["naive_equal"]["all_same"]

# ---- TANGENT zone 5: why divide by sqrt(d_k) ---------------------------------------
A_unscaled = softmax_rows(S.astype(float))
ev["unscaled_focus_row"] = r(A_unscaled[FOCUS], 4)
vr = np.random.default_rng(0)
qs, ks = vr.standard_normal((100_000, 64)), vr.standard_normal((100_000, 64))
dots = (qs * ks).sum(1)
ev["variance_check"] = {"d": 64, "samples": 100_000, "seed": 0,
                        "var_raw": round(float(dots.var()), 2),
                        "var_scaled": round(float((dots / 8).var()), 3)}

# ---- B10 HOOK / B18 PAYOFF: swap "cats" for "kids" ----------------------------------
KIDS = np.array([1, 1, 1, 0])  # hand-picked from {-1,0,1}^4: distinct row, distinct value point
X_k = X.copy(); X_k[0] = KIDS
Qk, Kk, Vk, Sk, Ak, Ok = head(X_k)
assert not any((KIDS == x).all() for x in X)
assert not any((Vk[0] == v).all() for v in V)
ev["swap"] = {"sentence": ["kids", "chase", "small", "dogs"], "kids_embedding": KIDS.tolist(),
              "kids_key": Kk[0].tolist(), "kids_value": Vk[0].tolist(),
              "chase_scores": Sk[FOCUS].tolist(), "chase_weights": r(Ak[FOCUS], 4),
              "chase_weights2": r(Ak[FOCUS], 2),
              "chase_output": r(Ok[FOCUS], 4), "chase_output2": r(Ok[FOCUS], 2),
              "moved_by": round(float(np.linalg.norm(Ok[FOCUS] - O[FOCUS])), 4)}
assert (Qk[FOCUS] == Q[FOCUS]).all(), "chase's own query must not change"

# ---- B19 BOUNDARY: reorder the sentence --------------------------------------------
perm = [3, 1, 2, 0]  # "dogs chase small cats"
Qp, Kp, Vp, Sp, Ap, Op = head(X[perm])
equivariant = bool(np.allclose(Op, O[perm]) and np.allclose(Ap, A[np.ix_(perm, perm)]))
assert equivariant
cats_new = perm.index(0)
ev["shuffle"] = {"sentence": [WORDS[i] for i in perm], "perm": perm,
                 "outputs_permuted_identically": equivariant,
                 "cats_output_before": r(O[0], 4), "cats_output_after": r(Op[cats_new], 4),
                 "max_abs_diff": float(np.abs(Op - O[perm]).max())}


def sinusoid_pe(n, d):
    """Vaswani et al. 2017 §3.5: PE(pos,2i)=sin(pos/10000^(2i/d)), PE(pos,2i+1)=cos(...)."""
    pe = np.zeros((n, d))
    for pos in range(n):
        for i in range(0, d, 2):
            ang = pos / 10000 ** (i / d)
            pe[pos, i], pe[pos, i + 1] = np.sin(ang), np.cos(ang)
    return pe


PE = sinusoid_pe(4, 4)
O_pe = head(X + PE)[5]
Op_pe = head(X[perm] + PE)[5]
ev["with_position"] = {"pe": r(PE, 4),
                       "cats_output_order1": r(O_pe[0], 4),
                       "cats_output_order2": r(Op_pe[cats_new], 4),
                       "cats_moved_by": round(float(np.linalg.norm(O_pe[0] - Op_pe[cats_new])), 4),
                       "max_abs_diff_vs_permuted": round(float(np.abs(Op_pe - O_pe[perm]).max()), 4)}
assert ev["with_position"]["cats_moved_by"] > 0.05

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1), encoding="utf-8")


def fmt_rows(M, nd=None):
    return ["   " + w.ljust(6) + "  ".join((f"{v:6.{nd}f}" if nd is not None else f"{v:3d}") for v in row)
            for w, row in zip(WORDS, M)]


L = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}",
     f"seed {SEED}   sentence: {' '.join(WORDS)}   d_model=4 d_k=4 d_v=2  sqrt(d_k)={SCALE:g}", ""]
for name, M in (("X (embeddings)", X), ("Q = X W_Q", Q), ("K = X W_K", K), ("V = X W_V", V), ("Q K^T (raw scores)", S)):
    L.append(name); L += fmt_rows(M)
L.append("softmax(Q K^T / 2), row by row  (rows = who asks, columns = who answers)")
L += fmt_rows(A, 4)
L.append("outputs = weights @ V"); L += fmt_rows(O, 4)
w = ev["worked"]
L.append("")
L.append(f"worked row: {w['word']}  query {w['query']}")
for d in w["dots"]:
    L.append(f"   . key({d['key_word']}) {d['key']}  products {d['products']}  score {d['score']}  /2 = {d['scaled']}")
L.append(f"   exp: {w['exp']}  sum {w['exp_sum']}  weights {w['weights']}")
L.append(f"   output = {w['output']}")
L.append(f"blend two (cats, small): " + "; ".join(f"w={s['w']} -> {s['point']}" for s in ev['blend_two']['sweep']))
L.append(f"blend four: " + "; ".join(f"{s['w']} -> {s['point']}" for s in ev['blend_four']))
L.append(f"match row for small: query {ev['match_small']['query']} scores {ev['match_small']['scores']}")
L.append(f"naive equal weights: every output = {ev['naive_equal']['outputs'][0]}  (all same: {ev['naive_equal']['all_same']})")
L.append(f"unscaled softmax, chase row: {ev['unscaled_focus_row']}")
vc = ev["variance_check"]
L.append(f"variance check d=64, {vc['samples']} pairs: var(q.k) = {vc['var_raw']}, var(q.k/8) = {vc['var_scaled']}")
sw = ev["swap"]
L.append(f"swap cats->kids: kids key {sw['kids_key']} value {sw['kids_value']}; chase scores {sw['chase_scores']}")
L.append(f"   chase weights {sw['chase_weights']}  output {sw['chase_output']}  moved {sw['moved_by']}")
sh = ev["shuffle"]
L.append(f"shuffle -> {' '.join(sh['sentence'])}: outputs permuted identically = {sh['outputs_permuted_identically']}"
         f"  (max diff {sh['max_abs_diff']})  cats {sh['cats_output_before']} -> {sh['cats_output_after']}")
wp = ev["with_position"]
L.append(f"with sinusoidal positions added: cats {wp['cats_output_order1']} vs {wp['cats_output_order2']}  moved {wp['cats_moved_by']}")
L.append("")
L.append("script sha256 " + hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
L.append("evidence sha256 " + hashlib.sha256((OUT / "evidence.json").read_bytes()).hexdigest())
(OUT / "RUN-LOG.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
