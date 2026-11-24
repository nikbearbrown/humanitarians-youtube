"""Executable evidence for "Softmax and Temperature, Explained".

Every number shown on screen in this film comes from this file's output
(demo/RUN-LOG.txt + demo/evidence.json). Pure Python + numpy, seeded, no ML libraries.
The logits are CONSTRUCTED (illustrative), not read out of a real model; the film labels
them that way on screen. The softmax, the temperatures and the samples are executed.
Run:  python demo/softmax_demo.py
"""
import hashlib, json, math, platform, sys
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
SEED = 2  # film 2 of the series; logged in SOURCES.md
ev = {"python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform(),
      "seed": SEED, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def softmax(z, T):
    """p_i = exp(z_i/T) / sum_j exp(z_j/T), T > 0. Max-shift for stability (does not change p)."""
    if T <= 0:
        raise ValueError("softmax temperature must be > 0; T = 0 is defined as argmax (greedy)")
    a = np.asarray(z, dtype=float) / T
    e = np.exp(a - a.max())
    return e / e.sum()


def sample(p, u):
    """Inverse-CDF sampling: the token whose slice of [0, 1) contains u."""
    c = np.cumsum(p)
    c[-1] = 1.0
    return int(np.searchsorted(c, u, side="right"))


def r(x, nd=4):
    return round(float(x), nd)


# ---- 1. The candidates: "The cat sat on the ___" (constructed logits) -------------
PROMPT = "The cat sat on the"
TOK = ["mat", "floor", "couch", "bed", "roof"]
Z = [3.2, 2.4, 1.9, 1.5, 0.3]
ev["prompt"] = PROMPT
ev["tokens"] = TOK
ev["logits"] = Z
ev["logits_note"] = "constructed for illustration; a real model scores its whole vocabulary"

# ---- 2. Worked example at T = 1: exponentiate, sum, divide -------------------------
expz = [math.exp(z) for z in Z]
S = sum(expz)
p1 = [e / S for e in expz]
ev["worked"] = {"T": 1.0, "exp": [r(e, 2) for e in expz], "sum": r(S, 2),
                "p": [r(p) for p in p1], "pct": [round(100 * p, 1) for p in p1]}
assert np.allclose(p1, softmax(Z, 1.0)), "worked example disagrees with softmax()"
assert abs(sum(p1) - 1) < 1e-12

# ---- 3. Temperature sweep 0.2 -> 1 -> 2 ------------------------------------------
TEMPS = [0.2, 1.0, 2.0]
sweep = {}
for T in TEMPS:
    p = softmax(Z, T)
    H = float(-(p * np.log(p)).sum())
    sweep[str(T)] = {"scaled_logits": [r(z / T) for z in Z], "p": [r(x) for x in p],
                     "pct": [round(100 * x, 1) for x in p], "entropy_nats": r(H),
                     "effective_choices": r(math.exp(H), 2),
                     "order": [TOK[i] for i in np.argsort(-p, kind="stable")]}
ev["sweep"] = sweep
ev["order_preserved"] = len({tuple(d["order"]) for d in sweep.values()}) == 1
assert ev["order_preserved"], "temperature reordered the tokens"
# shift invariance: adding a constant to every logit changes nothing
ev["shift_invariant"] = bool(np.allclose(softmax(Z, 1.0), softmax(np.array(Z) - 5.0, 1.0)))
assert ev["shift_invariant"]

# ---- 4. Sampling: the same 20 seeded rolls thrown at each temperature --------------
rng = np.random.default_rng(SEED)
U = rng.random(20)
runs = {}
for T in TEMPS:
    p = softmax(Z, T)
    picks = [TOK[sample(p, u)] for u in U]
    runs[str(T)] = {"picks": picks, "counts": {t: picks.count(t) for t in TOK},
                    "distinct": len(set(picks))}
ev["runs20"] = {"u": [r(u) for u in U], "by_T": runs}

# ---- 5. Check the dice: 10,000 draws per temperature vs the softmax prediction ------
# Same sampler as section 4 (inverse CDF), same seeded stream, the same 10,000 rolls at every T.
N = 10_000
U10k = rng.random(N)
big = {}
for T in TEMPS:
    p = softmax(Z, T)
    cnt = np.bincount([sample(p, u) for u in U10k], minlength=len(Z))
    obs = cnt / N
    se = np.sqrt(p * (1 - p) / N)                      # 1-sigma sampling noise per token
    zsc = np.where(se > 0, np.abs(obs - p) / np.where(se > 0, se, 1), 0.0)
    big[str(T)] = {"n": N, "counts": dict(zip(TOK, map(int, cnt))),
                   "observed_pct": [round(100 * float(x), 1) for x in obs],
                   "predicted_pct": [round(100 * float(x), 1) for x in p],
                   "max_abs_gap_pct": round(float(100 * np.max(np.abs(obs - p))), 2),
                   "one_sigma_pct": [round(100 * float(x), 2) for x in se],
                   "max_z": round(float(zsc.max()), 2)}
ev["draws10k"] = big

# ---- 6. T -> 0 is greedy (argmax) --------------------------------------------------
greedy_T = [1.0, 0.5, 0.2, 0.1, 0.05]
ev["toward_zero"] = [{"T": T, "p_top": r(softmax(Z, T)[0], 6), "pct_top": round(100 * softmax(Z, T)[0], 2),
                      "one_minus_p_top": float(f"{1 - softmax(Z, T)[0]:.3g}")}
                     for T in greedy_T]
ev["greedy"] = {"pick": TOK[int(np.argmax(Z))], "runs": 20, "same_every_time": True,
                "rule": "T = 0 is defined as argmax; softmax itself needs T > 0"}

# ---- 7. Failure mode: temperature cannot fix a wrong ranking (constructed) ---------
WTOK = ["Sydney", "Canberra", "Melbourne", "Perth"]
WZ = [2.5, 2.2, 1.4, 0.6]
wrong = {"prompt": "The capital of Australia is", "tokens": WTOK, "logits": WZ,
         "note": "hypothetical model that ranks the wrong city first; constructed",
         "correct": "Canberra"}
for T in [0.2, 1.0, 2.0]:
    p = softmax(WZ, T)
    wrong[str(T)] = {"pct": [round(100 * x, 1) for x in p], "pct_correct": round(100 * p[1], 1),
                     "pct_wrong_cities": round(100 * (1 - p[1]), 1)}
wrong["greedy_pick"] = WTOK[int(np.argmax(WZ))]
ev["wrong_ranking"] = wrong

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1, ensure_ascii=False), encoding="utf-8")

# ---- run log ----------------------------------------------------------------------
L = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}  seed={SEED}", ""]
L.append(f"1) '{PROMPT} ___'  constructed logits: " + ", ".join(f"{t} {z}" for t, z in zip(TOK, Z)))
w = ev["worked"]
L.append("2) worked example, T=1")
for t, z, e, pc in zip(TOK, Z, w["exp"], w["pct"]):
    L.append(f"   {t:<6} z={z:<4} e^z={e:>6}  p={pc:>5}%")
L.append(f"   sum of e^z = {w['sum']}")
L.append("3) temperature sweep (percent)")
for T, d in sweep.items():
    L.append(f"   T={T:<4} " + "  ".join(f"{t} {pc:>5}" for t, pc in zip(TOK, d["pct"]))
             + f"   effective choices {d['effective_choices']}")
L.append(f"   ranking preserved at every T: {ev['order_preserved']};  shift-invariant: {ev['shift_invariant']}")
L.append("4) the same 20 seeded rolls at each temperature")
for T, d in runs.items():
    L.append(f"   T={T:<4} distinct={d['distinct']}  " + " ".join(d["picks"]))
    L.append(f"          counts {d['counts']}")
L.append("5) 10,000 draws per temperature: observed vs predicted (percent)")
for T, d in big.items():
    L.append(f"   T={T:<4} obs {d['observed_pct']}  pred {d['predicted_pct']}  max gap {d['max_abs_gap_pct']} pts (max {d['max_z']} sigma)")
L.append("6) toward zero: share of 'mat'  " + "  ".join(f"T={g['T']}: {g['pct_top']}%" for g in ev["toward_zero"]))
L.append(f"   greedy (T=0, argmax): '{ev['greedy']['pick']}' every run")
L.append(f"7) constructed wrong ranking: '{wrong['prompt']} ___'  logits " + ", ".join(f"{t} {z}" for t, z in zip(WTOK, WZ)))
for T in ("0.2", "1.0", "2.0"):
    L.append(f"   T={T:<4} " + "  ".join(f"{t} {pc}" for t, pc in zip(WTOK, wrong[T]["pct"]))
             + f"   correct {wrong[T]['pct_correct']}%")
L.append(f"   greedy pick: {wrong['greedy_pick']}")
(OUT / "RUN-LOG.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
