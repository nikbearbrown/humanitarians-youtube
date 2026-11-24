"""Why Did the AI Say No? -- executable evidence for Boopesh M.'s explainer on reason codes.

SYNTHETIC APPLICANTS ONLY. 20,000 made-up loan applicants with five plain features:
  income ($k a year), debt-to-income (% of monthly income spent on debt payments),
  missed payments (last 2 years), credit history length (years), credit card utilisation (% of limit).
No protected attributes are generated or used (fairness is out of scope for this film).
A known "true" default-risk rule (with two kinks) produces each applicant's default / no-default label.

Two models predict default risk:
  (1) a logistic "scorecard": its reasons are exact -- weight x (applicant value - average applicant),
  (2) a gradient-boosted tree model (sklearn HistGradientBoostingClassifier): no weights to read, so we
      compute exact Shapley values ourselves (all 2^5 = 32 feature coalitions, 500 background applicants).
Applicant A is a hand-written made-up applicant; both models deny them at the cutoff (an assumption).
We list their top-3 reasons per model, check whether the models agree, and find the smallest single
change (card balance or monthly debt payments) that flips each model's decision.

Run:  python credit_reasons.py > run.log      -> results.json
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")   # deterministic + polite on a shared 4-CPU box

import itertools
import json
import math
import time
from pathlib import Path

import numpy as np
import sklearn
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

SEED = 42
N = 20_000
CUTOFF = 0.30            # deny when predicted default risk >= 30 % (illustrative assumption)
N_BACKGROUND = 500       # comparison applicants for the Shapley values
CARD_LIMIT = 10_000      # Applicant A's total card limit, $ (to turn utilisation into dollars)
HERE = Path(__file__).resolve().parent

FEATS = ["income", "dti", "missed", "history", "util"]
NAMES = {"income": "income", "dti": "debt-to-income", "missed": "missed payments",
         "history": "credit history length", "util": "card utilisation"}
UNITS = {"income": "$k/yr", "dti": "%", "missed": "in 2 yrs", "history": "yrs", "util": "%"}
# plain-language reason text for a reason that pushes toward "deny"
REASON = {"income": "income too low for the loan", "dti": "debt payments too high for income",
          "missed": "recent missed payments", "history": "short credit history",
          "util": "card balances near their limits"}

APPLICANT_A = {"income": 52.0, "dti": 44.0, "missed": 1.0, "history": 4.0, "util": 72.0}


def make_applicants(rng, n):
    income = np.clip(np.exp(rng.normal(math.log(55.0), 0.40, n)), 15, 250)
    dti = np.clip(100 * rng.beta(2.5, 5.0, n), 0, 85)
    missed = np.clip(rng.poisson(0.45, n), 0, 8).astype(float)
    history = np.clip(rng.gamma(2.5, 4.0, n), 0.5, 40)
    util = np.clip(100 * rng.beta(2.0, 3.0, n) + 6 * missed, 0, 100)
    return np.column_stack([income, dti, missed, history, util])


def true_logit(X):
    income, dti, missed, history, util = X.T
    return (-3.0
            - 0.012 * (income - 55)
            + 0.030 * (dti - 33) + 0.090 * np.maximum(dti - 40, 0)     # kink: debt above 40 % bites harder
            + 0.75 * np.minimum(missed, 4)
            - 0.55 * np.log(history / 8)
            + 0.020 * (util - 40) + 0.050 * np.maximum(util - 70, 0))  # kink: cards near the limit


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def shapley_exact(f, x, background):
    """Exact interventional Shapley values of f (log-odds) at x against a background sample.
    v(S) = mean_b f(x on S, b elsewhere); 2^d coalitions, each scored on the whole background."""
    d = len(x)
    v = {}
    for r in range(d + 1):
        for S in itertools.combinations(range(d), r):
            Z = background.copy()
            Z[:, list(S)] = x[list(S)]
            v[S] = float(np.mean(f(Z)))
    phi = np.zeros(d)
    for i in range(d):
        others = [j for j in range(d) if j != i]
        for r in range(d):
            w = math.factorial(r) * math.factorial(d - r - 1) / math.factorial(d)
            for S in itertools.combinations(others, r):
                phi[i] += w * (v[tuple(sorted(S + (i,)))] - v[S])
    return phi, v[()], v[tuple(range(d))], len(v) * len(background)


def top3(contrib):
    order = np.argsort(-contrib)
    return [FEATS[i] for i in order[:3] if contrib[i] > 0]


def flip_search(model_logit, x, feat, lo, hi, step):
    """Smallest move of one feature (toward `lo`) that brings risk below the cutoff."""
    i = FEATS.index(feat)
    for val in np.arange(x[i], lo - 1e-9, -step):
        z = x.copy()
        z[i] = val
        if sigmoid(model_logit(z[None, :]))[0] < CUTOFF:
            return round(float(val), 4)
    return None


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    X = make_applicants(rng, N)
    p_true = sigmoid(true_logit(X))
    y = (rng.random(N) < p_true).astype(int)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=SEED)
    print(f"sklearn {sklearn.__version__}  numpy {np.__version__}  SYNTHETIC applicants {N}  "
          f"default rate {y.mean():.2%}")
    print(f"train {len(ytr)}  test {len(yte)}  cutoff: deny if risk >= {CUTOFF:.0%}")

    mean = Xtr.mean(axis=0)
    sd = Xtr.std(axis=0)

    # (1) logistic scorecard on standardised features (weights reported per raw unit)
    lr = LogisticRegression(max_iter=5000)
    lr.fit((Xtr - mean) / sd, ytr)
    w_std = lr.coef_[0]
    w_raw = w_std / sd
    b0 = float(lr.intercept_[0])        # = log-odds of the average applicant (features at the mean)

    def lr_logit(Z):
        return ((Z - mean) / sd) @ w_std + b0

    # (2) gradient-boosted trees ("black box"), deterministic: no early stopping
    gb = HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, max_leaf_nodes=15,
                                        min_samples_leaf=40, early_stopping=False, random_state=SEED)
    gb.fit(Xtr, ytr)

    def gb_logit(Z):
        return gb.decision_function(Z)

    auc_lr = roc_auc_score(yte, sigmoid(lr_logit(Xte)))
    auc_gb = roc_auc_score(yte, gb.predict_proba(Xte)[:, 1])
    auc_true = roc_auc_score(yte, sigmoid(true_logit(Xte)))
    deny_lr = float(np.mean(sigmoid(lr_logit(Xte)) >= CUTOFF))
    deny_gb = float(np.mean(gb.predict_proba(Xte)[:, 1] >= CUTOFF))
    print(f"test AUC  scorecard {auc_lr:.3f}  boosted {auc_gb:.3f}  (true rule {auc_true:.3f})")
    print(f"test denial rate at cutoff  scorecard {deny_lr:.1%}  boosted {deny_gb:.1%}")
    print("scorecard weights per unit (log-odds):",
          ", ".join(f"{f} {w:+.4f}" for f, w in zip(FEATS, w_raw)))

    xa = np.array([APPLICANT_A[f] for f in FEATS])
    risk_true = float(sigmoid(true_logit(xa[None, :]))[0])
    risk_lr = float(sigmoid(lr_logit(xa[None, :]))[0])
    risk_gb = float(gb.predict_proba(xa[None, :])[0, 1])
    avg_risk_lr = float(sigmoid(b0))
    print(f"\nApplicant A {APPLICANT_A}")
    print(f"risk  true rule {risk_true:.1%}  scorecard {risk_lr:.1%}  boosted {risk_gb:.1%}  "
          f"(cutoff {CUTOFF:.0%})")

    # scorecard reasons: exact, one multiplication per feature
    c_lr = w_raw * (xa - mean)
    assert abs(b0 + c_lr.sum() - lr_logit(xa[None, :])[0]) < 1e-9
    print("\nscorecard contributions = weight x (A - average)   [log-odds; + pushes toward deny]")
    for f, c, m in zip(FEATS, c_lr, mean):
        print(f"  {f:8s} A {APPLICANT_A[f]:6.1f}  avg {m:6.2f}  -> {c:+.3f}")
    print("  top 3:", top3(c_lr))

    # background sample for Shapley (same for both models)
    bidx = np.random.default_rng(SEED + 1).choice(len(Xtr), N_BACKGROUND, replace=False)
    B = Xtr[bidx]
    phi_lr, base_lr, full_lr, runs = shapley_exact(lr_logit, xa, B)
    # sanity: for a linear model, exact Shapley = weight x (A - background mean)
    lin_check = float(np.max(np.abs(phi_lr - w_raw * (xa - B.mean(axis=0)))))
    print(f"\ncheck: scorecard Shapley vs weight x (A - background mean): max diff {lin_check:.2e}")

    phi_gb, base_gb, full_gb, runs = shapley_exact(gb_logit, xa, B)
    add_err = abs(base_gb + phi_gb.sum() - full_gb)
    print(f"boosted Shapley values (exact, {2 ** len(FEATS)} coalitions x {N_BACKGROUND} applicants = "
          f"{runs:,} model runs)   additivity error {add_err:.1e}")
    for f, c in zip(FEATS, phi_gb):
        print(f"  {f:8s} -> {c:+.3f}")
    print("  top 3:", top3(phi_gb))

    t_lr, t_gb = top3(c_lr), top3(phi_gb)
    shared = [f for f in t_lr if f in t_gb]
    same_order = t_lr == t_gb
    print(f"agreement: {len(shared)} of 3 reasons shared; same order: {same_order}")

    # does the black box's answer depend on who we compare against? (approved-only background)
    approved = Xtr[gb.predict_proba(Xtr)[:, 1] < CUTOFF]
    B2 = approved[np.random.default_rng(SEED + 2).choice(len(approved), N_BACKGROUND, replace=False)]
    phi_gb2, _, _, _ = shapley_exact(gb_logit, xa, B2)
    print("boosted Shapley vs APPROVED applicants only:",
          ", ".join(f"{f} {c:+.3f}" for f, c in zip(FEATS, phi_gb2)), " top 3:", top3(phi_gb2))

    # does it depend on the training run? retrain the boosted model on a different random 70 %
    Xtr3, _, ytr3, _ = train_test_split(X, y, test_size=0.3, stratify=y, random_state=SEED + 7)
    gb3 = HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, max_leaf_nodes=15,
                                         min_samples_leaf=40, early_stopping=False, random_state=SEED)
    gb3.fit(Xtr3, ytr3)
    phi_gb3, _, _, _ = shapley_exact(gb3.decision_function, xa, B)
    print("boosted retrained on another 70 % split:",
          ", ".join(f"{f} {c:+.3f}" for f, c in zip(FEATS, phi_gb3)), " top 3:", top3(phi_gb3),
          f" risk {gb3.predict_proba(xa[None, :])[0, 1]:.1%}")

    # what would change the decision? one feature at a time
    cf = {}
    for name, fl in (("scorecard", lr_logit), ("boosted", gb_logit)):
        cf[name] = {"util": flip_search(fl, xa, "util", 0, 100, 0.5),
                    "dti": flip_search(fl, xa, "dti", 0, 85, 0.5)}
    monthly_income = APPLICANT_A["income"] * 1000 / 12

    def util_dollars(u):
        return None if u is None else round((APPLICANT_A["util"] - u) / 100 * CARD_LIMIT)

    def dti_dollars(dv):
        return None if dv is None else round((APPLICANT_A["dti"] - dv) / 100 * monthly_income)

    print(f"\ncounterfactuals (one change at a time; card limit ${CARD_LIMIT:,}, "
          f"monthly income ${monthly_income:,.0f})")
    for name in cf:
        u, dv = cf[name]["util"], cf[name]["dti"]
        print(f"  {name:9s} utilisation {APPLICANT_A['util']:.0f}% -> {u}%  (pay cards down ${util_dollars(u)})"
              f"   |  DTI {APPLICANT_A['dti']:.0f}% -> {dv}%  (cut debt payments ${dti_dollars(dv)}/month)")
    both_util = None if None in (cf["scorecard"]["util"], cf["boosted"]["util"]) else \
        min(cf["scorecard"]["util"], cf["boosted"]["util"])
    if both_util is not None:
        za = xa.copy()
        za[FEATS.index("util")] = both_util
        r_lr2 = float(sigmoid(lr_logit(za[None, :]))[0])
        r_gb2 = float(gb.predict_proba(za[None, :])[0, 1])
        print(f"  both approve at utilisation {both_util}% (pay down ${util_dollars(both_util):,}): "
              f"scorecard {r_lr2:.1%}  boosted {r_gb2:.1%}")
    else:
        r_lr2 = r_gb2 = None

    res = {
        "setup": {"synthetic": True, "seed": SEED, "n_applicants": N, "features": FEATS,
                  "feature_names": NAMES, "units": UNITS, "reason_text": REASON,
                  "default_rate": float(y.mean()), "train": int(len(ytr)), "test": int(len(yte)),
                  "cutoff": CUTOFF, "cutoff_note": "illustrative assumption, not from any lender",
                  "n_background": N_BACKGROUND, "card_limit": CARD_LIMIT,
                  "protected_attributes": "none generated or used",
                  "sklearn_version": sklearn.__version__, "numpy_version": np.__version__,
                  "average_applicant": dict(zip(FEATS, map(float, mean)))},
        "models": {"scorecard": {"type": "LogisticRegression on standardised features",
                                 "weights_per_unit": dict(zip(FEATS, map(float, w_raw))),
                                 "weights_per_sd": dict(zip(FEATS, map(float, w_std))),
                                 "intercept_at_average": b0, "avg_applicant_risk": avg_risk_lr,
                                 "test_auc": float(auc_lr), "test_denial_rate": deny_lr},
                   "boosted": {"type": "HistGradientBoostingClassifier(max_iter=300, lr=0.05, "
                                       "max_leaf_nodes=15, min_samples_leaf=40)",
                               "test_auc": float(auc_gb), "test_denial_rate": deny_gb},
                   "true_rule_test_auc": float(auc_true)},
        "applicant_a": {"values": APPLICANT_A, "risk_true_rule": risk_true,
                        "risk_scorecard": risk_lr, "risk_boosted": risk_gb,
                        "denied_scorecard": risk_lr >= CUTOFF, "denied_boosted": risk_gb >= CUTOFF},
        "reasons": {
            "scorecard": {"contrib": dict(zip(FEATS, map(float, c_lr))), "top3": t_lr,
                          "method": "weight x (A - average applicant), exact, 5 multiplications"},
            "scorecard_shapley_check_max_diff": lin_check,
            "boosted": {"contrib": dict(zip(FEATS, map(float, phi_gb))), "top3": t_gb,
                        "base_logodds": base_gb, "full_logodds": full_gb, "additivity_error": add_err,
                        "model_runs": runs,
                        "method": "exact interventional Shapley, 32 coalitions x 500 background applicants"},
            "boosted_vs_approved_background": {"contrib": dict(zip(FEATS, map(float, phi_gb2))),
                                               "top3": top3(phi_gb2)},
            "boosted_retrained_other_split": {"contrib": dict(zip(FEATS, map(float, phi_gb3))),
                                              "top3": top3(phi_gb3)},
            "agreement": {"shared": shared, "n_shared": len(shared), "same_order": same_order}},
        "counterfactual": {"scorecard": cf["scorecard"], "boosted": cf["boosted"],
                           "util_dollars": {k: util_dollars(cf[k]["util"]) for k in cf},
                           "dti_dollars_per_month": {k: dti_dollars(cf[k]["dti"]) for k in cf},
                           "both_approve_util": both_util,
                           "both_approve_paydown": util_dollars(both_util),
                           "risk_after": {"scorecard": r_lr2, "boosted": r_gb2},
                           "monthly_income": monthly_income},
        "runtime_s": round(time.time() - t0, 2),
    }
    (HERE / "results.json").write_text(json.dumps(res, indent=2) + "\n")
    print(f"\nwrote results.json")


if __name__ == "__main__":
    main()
