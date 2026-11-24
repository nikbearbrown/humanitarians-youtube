"""Executable evidence for "Bayes' Theorem: The Positive That's Usually Wrong".

Every number shown on screen in this film comes from this file's output
(demo/RUN-LOG.txt + demo/evidence.json). Pure Python standard library:
exact arithmetic with fractions.Fraction, plus a seeded Monte-Carlo check.
Run:  python demo/bayes_demo.py
"""
import hashlib
import json
import platform
import random
import sys
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).resolve().parent
ev = {"python": sys.version.split()[0], "platform": platform.platform(),
      "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

# ---- 0. The test and the population (exact) ---------------------------------------
N = 10_000
BASE = F(1, 100)          # P(D)       base rate / prior
SENS = F(99, 100)         # P(+ | D)   sensitivity
SPEC = F(95, 100)         # P(- | ~D)  specificity
FPR = 1 - SPEC            # P(+ | ~D)  false-positive rate


def counts(n, base, sens, spec):
    sick = n * base
    healthy = n - sick
    tp, fn = sick * sens, sick * (1 - sens)
    fp, tn = healthy * (1 - spec), healthy * spec
    return {"n": n, "sick": sick, "healthy": healthy, "tp": tp, "fn": fn, "fp": fp, "tn": tn,
            "positives": tp + fp, "negatives": fn + tn}


C = counts(N, BASE, SENS, SPEC)
for k, v in C.items():                      # whole people only — the reason N is 10,000
    assert v.denominator == 1, f"{k} = {v} is not a whole number of people"
C = {k: int(v) for k, v in C.items()}
assert C["tp"] + C["fn"] + C["fp"] + C["tn"] == N

ppv = F(C["tp"], C["positives"])            # P(D | +) from the counts
assert ppv == F(1, 6)

# ---- 1. Bayes' theorem built from the same counts --------------------------------
p_pos = SENS * BASE + FPR * (1 - BASE)      # law of total probability
bayes = SENS * BASE / p_pos
assert p_pos == F(C["positives"], N)        # 594 / 10,000
assert SENS * BASE == F(C["tp"], N)         # 99 / 10,000
assert bayes == ppv, "Bayes' theorem must equal the count fraction"
accuracy = F(C["tp"] + C["tn"], N)

ev["test"] = {"base_rate": str(BASE), "sensitivity": str(SENS), "specificity": str(SPEC),
              "false_positive_rate": str(FPR),
              "base_rate_pct": float(BASE * 100), "sensitivity_pct": float(SENS * 100),
              "specificity_pct": float(SPEC * 100), "fpr_pct": float(FPR * 100)}
ev["counts"] = C
ev["ppv"] = {"fraction": str(ppv), "num": C["tp"], "den": C["positives"],
             "reduced": [ppv.numerator, ppv.denominator], "pct": round(float(ppv) * 100, 2),
             "false_alarm_share": str(1 - ppv)}
ev["bayes"] = {"p_pos": str(p_pos), "p_pos_decimal": float(p_pos),
               "numerator": str(SENS * BASE), "numerator_decimal": float(SENS * BASE),
               "result": str(bayes), "equals_count_fraction": bayes == ppv,
               "worked": "0.99 * 0.01 / 0.0594 = 1/6"}
ev["accuracy"] = {"fraction": str(accuracy), "pct": float(accuracy * 100),
                  "note": "overall share of correct results; '99%' is the sensitivity only"}
ev["likelihood_ratio_pos"] = str(SENS / FPR)                 # 99/5 = 19.8
ev["odds"] = {"prior": "1:99", "after_one_positive": "1:5"}
assert (BASE / (1 - BASE)) * (SENS / FPR) == F(1, 5)

# ---- 2. Base-rate sweep (BOUNDARY) -----------------------------------------------
sweep = []
for b in (F(1, 1000), F(1, 100), F(1, 10), F(1, 2)):
    p = SENS * b / (SENS * b + FPR * (1 - b))
    sweep.append({"base_rate": str(b), "base_rate_pct": float(b * 100),
                  "ppv": str(p), "ppv_pct": round(float(p) * 100, 2)})
ev["base_rate_sweep"] = sweep
# dense curve for the Manim ValueTracker (log-spaced 0.1% .. 50%)
curve = []
for i in range(61):
    b = 0.001 * (500 ** (i / 60))
    p = 0.99 * b / (0.99 * b + 0.05 * (1 - b))
    curve.append([round(b, 6), round(p, 6)])
ev["base_rate_curve"] = curve

# ---- 3. A second positive (BHTF answer key; independence ASSUMED) -----------------
post1 = ppv
post2 = SENS * post1 / (SENS * post1 + FPR * (1 - post1))
M = 1_000_000
two = {"n": M, "sick": int(M * BASE), "sick_pos_twice": int(M * BASE * SENS * SENS),
       "healthy_pos_twice": int(M * (1 - BASE) * FPR * FPR)}
assert F(two["sick_pos_twice"], two["sick_pos_twice"] + two["healthy_pos_twice"]) == post2
ev["second_positive"] = {"assumption": "errors of the two runs independent given disease status",
                         "posterior": str(post2), "pct": round(float(post2) * 100, 2),
                         "counts_per_million": two, "odds_after_two": "99:25"}

# ---- 4. Seeded simulation of 100,000 people --------------------------------------
SEED, NSIM = 20261122, 100_000
rng = random.Random(SEED)
s = {"sick": 0, "tp": 0, "fp": 0}
for _ in range(NSIM):
    sick = rng.random() < 0.01
    pos = rng.random() < (0.99 if sick else 0.05)
    s["sick"] += sick
    s["tp"] += sick and pos
    s["fp"] += (not sick) and pos
sim_ppv = s["tp"] / (s["tp"] + s["fp"])
# binomial-ish standard error of a proportion over the positives
se = (sim_ppv * (1 - sim_ppv) / (s["tp"] + s["fp"])) ** 0.5
ev["simulation"] = {"seed": SEED, "people": NSIM, **s, "positives": s["tp"] + s["fp"],
                    "ppv": round(sim_ppv, 4), "exact": round(float(ppv), 4),
                    "abs_error": round(abs(sim_ppv - float(ppv)), 4), "std_err": round(se, 4),
                    "within_3_se": abs(sim_ppv - float(ppv)) < 3 * se}
assert ev["simulation"]["within_3_se"], "simulation disagrees with the exact answer"

(OUT / "evidence.json").write_text(json.dumps(ev, indent=1), encoding="utf-8")

L = [f"python {ev['python']} on {ev['platform']}",
     f"script sha256 {ev['script_sha256']}", ""]
L.append(f"0) test: base rate {BASE} · sensitivity {SENS} · specificity {SPEC} · population {N:,}")
L.append(f"   sick {C['sick']}: positive {C['tp']}, missed {C['fn']}")
L.append(f"   healthy {C['healthy']}: false positive {C['fp']}, cleared {C['tn']}")
L.append(f"   all positives {C['positives']}")
L.append(f"   P(D|+) = {C['tp']}/{C['positives']} = {ppv} = {float(ppv):.4%}   false alarms {1 - ppv}")
L.append(f"   overall accuracy = {accuracy} = {float(accuracy):.2%}  (99% is sensitivity only)")
L.append(f"1) Bayes: P(+|D)P(D) = {SENS*BASE} ; P(+) = {p_pos} = {float(p_pos)} ; ratio = {bayes}  "
         f"[== count fraction: {bayes == ppv}]")
L.append(f"   likelihood ratio + = {SENS/FPR} ; odds 1:99 -> 1:5")
L.append("2) base-rate sweep:  " + " | ".join(f"{d['base_rate']} -> {d['ppv']} ({d['ppv_pct']}%)" for d in sweep))
L.append(f"3) second positive (independence assumed): {post2} = {float(post2):.2%} ; per million: "
         f"{two['sick_pos_twice']} sick vs {two['healthy_pos_twice']} healthy positive twice")
sm = ev["simulation"]
L.append(f"4) simulation seed {SEED}, {NSIM:,} people: sick {sm['sick']}, tp {sm['tp']}, fp {sm['fp']}, "
         f"P(D|+) = {sm['ppv']} vs exact {sm['exact']} (|err| {sm['abs_error']}, se {sm['std_err']})")
L.append("all assertions passed")
(OUT / "RUN-LOG.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
