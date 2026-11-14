"""
Evidence for "Every Group Went The Other Way" — how an aggregate can point the
opposite way to every group inside it.

Two halves, and the distinction matters:

  REAL DATA   the UC Berkeley 1973 graduate admissions table (Bickel, Hammel &
              O'Connell, Science 1975; the same six departments distributed as
              `UCBAdmissions` in R). Published, verifiable, not constructed by
              me. Every figure the reel puts on screen about Berkeley comes
              from here.

  SIMULATION  the part the real table cannot answer: under what conditions is
              a reversal even possible, and how often does one appear by
              chance? Seeded, reproducible, and clearly labelled as synthetic.

    python simpson_evidence.py
"""

import json
import numpy as np

SEED = 20261113
RNG = np.random.default_rng(SEED)

# ---------------------------------------------------------------- real data
# Bickel, Hammel & O'Connell (1975), Table 1 — the six largest departments.
# Counts are applicants and admits, NOT percentages: the percentages below are
# derived here so they cannot drift from the counts.
BERKELEY = {
    #        men: (admitted, applied)   women: (admitted, applied)
    "A": {"m": (512, 825), "w": (89, 108)},
    "B": {"m": (353, 560), "w": (17, 25)},
    "C": {"m": (120, 325), "w": (202, 593)},
    "D": {"m": (138, 417), "w": (131, 375)},
    "E": {"m": (53, 191), "w": (94, 393)},
    "F": {"m": (22, 373), "w": (24, 341)},
}

out = {}
print("=" * 72)
print("REAL DATA — UC Berkeley 1973, six largest departments")
print("Bickel, Hammel & O'Connell, Science 187(4175), 1975")
print("=" * 72)

m_adm = sum(v["m"][0] for v in BERKELEY.values())
m_app = sum(v["m"][1] for v in BERKELEY.values())
w_adm = sum(v["w"][0] for v in BERKELEY.values())
w_app = sum(v["w"][1] for v in BERKELEY.values())

print(f"\nAGGREGATE across the six departments")
print(f"  men   {m_adm:>5} / {m_app:<5} = {m_adm/m_app:6.1%}")
print(f"  women {w_adm:>5} / {w_app:<5} = {w_adm/w_app:6.1%}")
print(f"  gap   {m_adm/m_app - w_adm/w_app:+.1%} in favour of men")

out["aggregate"] = {
    "men_admitted": m_adm, "men_applied": m_app, "men_rate": m_adm / m_app,
    "women_admitted": w_adm, "women_applied": w_app, "women_rate": w_adm / w_app,
    "gap_pp": (m_adm / m_app - w_adm / w_app) * 100,
}

print(f"\nBY DEPARTMENT")
print(f"  {'dept':<6}{'men':>18}{'women':>18}   favours")
rows = []
for d, v in BERKELEY.items():
    mr = v["m"][0] / v["m"][1]
    wr = v["w"][0] / v["w"][1]
    fav = "women" if wr > mr else "men"
    print(f"  {d:<6}{v['m'][0]:>6}/{v['m'][1]:<5}{mr:>6.1%}"
          f"{v['w'][0]:>6}/{v['w'][1]:<5}{wr:>6.1%}   {fav}")
    rows.append({"dept": d, "men_rate": mr, "women_rate": wr,
                 "men_applied": v["m"][1], "women_applied": v["w"][1],
                 "favours": fav})
out["departments"] = rows

fav_w = sum(1 for r in rows if r["favours"] == "women")
print(f"\n  women admitted at a HIGHER rate in {fav_w} of {len(rows)} departments,")
print(f"  yet LOWER overall by {out['aggregate']['gap_pp']:.1f} points.")
out["departments_favouring_women"] = fav_w

# ------------------------------------------------- why: the confounder
# Departments differ enormously in how hard they are to get into, and the two
# groups did not apply to them in the same proportions. That is the whole
# mechanism, and it is measurable rather than asserted.
print(f"\nTHE CONFOUNDER — selectivity, and who applied where")
print(f"  {'dept':<6}{'overall rate':>14}{'% of men':>11}{'% of women':>13}")
share = []
for d, v in BERKELEY.items():
    tot_adm = v["m"][0] + v["w"][0]
    tot_app = v["m"][1] + v["w"][1]
    ms = v["m"][1] / m_app
    ws = v["w"][1] / w_app
    print(f"  {d:<6}{tot_adm/tot_app:>13.1%}{ms:>11.1%}{ws:>13.1%}")
    share.append({"dept": d, "overall_rate": tot_adm / tot_app,
                  "men_share": ms, "women_share": ws})
out["shares"] = share

easy = [s for s in share if s["overall_rate"] >= 0.5]
print(f"\n  The two easiest departments ({', '.join(s['dept'] for s in easy)}) took "
      f"{sum(s['men_share'] for s in easy):.0%} of men's applications")
print(f"  and only {sum(s['women_share'] for s in easy):.0%} of women's.")
out["easy_depts"] = [s["dept"] for s in easy]
out["easy_share_men"] = sum(s["men_share"] for s in easy)
out["easy_share_women"] = sum(s["women_share"] for s in easy)

# --------------------------------------------- direct standardisation
# The counterfactual the aggregate hides: hold the department-specific rates
# fixed and give women the men's application pattern.
expected = sum((v["w"][0] / v["w"][1]) * (v["m"][1] / m_app)
               for v in BERKELEY.values())
print(f"\nSTANDARDISED — women's own department rates, men's application pattern")
print(f"  women, as observed              {w_adm/w_app:6.1%}")
print(f"  women, had they applied as men  {expected:6.1%}")
print(f"  men, as observed                {m_adm/m_app:6.1%}")
print(f"  -> the 14-point deficit becomes a {expected - m_adm/m_app:+.1%} surplus")
out["standardised_women_rate"] = expected
out["standardised_vs_men_pp"] = (expected - m_adm / m_app) * 100

# ------------------------------------------------------------- simulation
print("\n" + "=" * 72)
print("SIMULATION — when is a reversal possible at all?  (synthetic, seeded)")
print("=" * 72)

N_SIM = 20_000


def trial(rng, confound):
    """Two groups, two strata. `confound` sets how unevenly group B is routed
    to the hard stratum. Group B is given a genuinely HIGHER success rate in
    BOTH strata; the question is whether the total can still say otherwise."""
    easy_rate, hard_rate = 0.70, 0.20
    bump = 0.05                       # B really is better, everywhere
    n = 1000
    a_easy = int(n * 0.5)
    b_easy = int(n * (0.5 - confound))
    a_hard, b_hard = n - a_easy, n - b_easy

    a_s = rng.binomial(a_easy, easy_rate) + rng.binomial(a_hard, hard_rate)
    b_s = (rng.binomial(b_easy, easy_rate + bump)
           + rng.binomial(b_hard, hard_rate + bump))

    a_easy_r = easy_rate
    # per-stratum truth is fixed by construction: B is better in both.
    return (b_s / n) < (a_s / n)      # did the TOTAL reverse the truth?


print(f"\n  group B is better in BOTH strata, by 5 points, every time.")
print(f"  {'routing imbalance':>20}{'total says B is worse':>26}")
curve = []
for confound in (0.0, 0.1, 0.2, 0.3, 0.4, 0.45):
    hits = sum(trial(RNG, confound) for _ in range(N_SIM // 10))
    r = hits / (N_SIM // 10)
    curve.append({"imbalance": confound, "reversal_rate": r})
    bar = "#" * int(round(r * 50))
    print(f"  {confound:>19.0%}{r:>25.1%}  {bar}")
out["reversal_curve"] = curve

print("\n  With the groups routed identically, the total can essentially never")
print("  contradict every stratum. The reversal is not a quirk of arithmetic —")
print("  it requires a confounder that is correlated with BOTH the grouping")
print("  and the outcome. No confounder, no paradox.")

with open("simpson_results.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)
print("\nwrote simpson_results.json")
