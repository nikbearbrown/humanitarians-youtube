"""Week 10 evidence run for 'Every Look Was Right'.

A/A experiments (no true difference) run through github.com/Kenny0bi/
product-analytics-engine's OWN ABTestAnalyzer.frequentist_test and
SequentialTester.compute_sprt, on an in-memory DuckDB with the repo's schema.
Each experiment is checked at 10 looks as data arrives. Any significant result
is a false positive by construction.
"""
import json, math, os, sys
from pathlib import Path
import numpy as np, pandas as pd, duckdb

REPO = Path(os.environ.get("ANALYTICS_REPO", "product-analytics-engine")).expanduser()
sys.path.insert(0, str(REPO))
from loguru import logger; logger.remove()
from src.statistics.ab_testing import ABTestAnalyzer
from src.statistics.sequential import SequentialTester

K, LOOKS, PER_LOOK, P = 1000, 10, 200, 0.10       # 1,000 experiments, 2,000 users per arm
ALPHA, BETA, DELTA = 0.05, 0.20, 0.02            # the repo's SPRT defaults
rng = np.random.default_rng(7)

con = duckdb.connect()
con.execute("create table experiments (experiment_id varchar, control_variant varchar, treatment_variant varchar)")
con.execute("""create table experiment_assignments (experiment_id varchar, variant varchar,
               converted boolean, conversion_value double, assigned_at timestamp)""")
ab, sq = ABTestAnalyzer(con), SequentialTester(con)

# textbook Wald SPRT: theta_0 fixed in advance at the true rate, not re-estimated
UB, LB = math.log((1 - BETA) / ALPHA), math.log(BETA / (1 - ALPHA))
r1, r0 = math.log((P + DELTA) / P), math.log((1 - P - DELTA) / (1 - P))

fixed = peek = sprt_repo = sprt_fixed = 0
first_peek_look = []
t0 = pd.Timestamp("2026-01-01")
for k in range(K):
    eid = f"aa_{k}"
    con.execute("insert into experiments values (?, 'control', 'treatment')", [eid])
    peek_hit = repo_hit = fixed_hit = repo_stopped = False
    llr = 0.0
    for look in range(LOOKS):
        n = 2 * PER_LOOK
        variant = np.repeat(["control", "treatment"], PER_LOOK)
        conv = rng.random(n) < P
        df = pd.DataFrame({"experiment_id": eid, "variant": variant, "converted": conv,
                           "conversion_value": conv.astype(float),
                           "assigned_at": t0 + pd.to_timedelta(np.arange(n) + look * n, unit="s")})
        con.register("batch", df); con.execute("insert into experiment_assignments select * from batch"); con.unregister("batch")

        p = ab.frequentist_test(eid, metric_type="binary").p_value
        if not peek_hit and p < ALPHA:
            peek_hit = True; first_peek_look.append(look + 1)
        if look == LOOKS - 1 and p < ALPHA:
            fixed_hit = True
        if not repo_stopped:                      # a sequential test STOPS at its first boundary, either side
            dec = sq.compute_sprt(eid, alpha=ALPHA, beta=BETA, delta=DELTA).decision
            if dec != "continue":
                repo_stopped = True; repo_hit = (dec == "reject_null")
        x = conv[PER_LOOK:]                       # this look's treatment outcomes
        for xi in x:
            if not np.isfinite(llr): break
            llr += xi * r1 + (1 - xi) * r0
            if llr >= UB: llr = np.inf
            elif llr <= LB: llr = -np.inf
    fixed += int(fixed_hit); peek += int(peek_hit); sprt_repo += int(repo_hit); sprt_fixed += int(bool(llr == np.inf))

res = {"experiments": K, "looks": LOOKS, "users_per_arm": LOOKS * PER_LOOK, "true_rate_both_arms": P,
       "alpha": ALPHA, "beta": BETA, "delta": DELTA,
       "false_positive_rate": {
         "fixed_horizon_final_look_only": round(fixed / K, 4),
         "peek_every_look_stop_at_first_p_below_0_05": round(peek / K, 4),
         "repo_sprt_theta0_reestimated_each_look": round(sprt_repo / K, 4),
         "textbook_sprt_theta0_fixed_in_advance": round(sprt_fixed / K, 4)},
       "false_positive_counts": {"fixed": fixed, "peek": peek, "repo_sprt": sprt_repo, "textbook_sprt": sprt_fixed},
       "peeking_hits_by_look": {str(i): first_peek_look.count(i) for i in range(1, LOOKS + 1)}}
Path(__file__).with_name("evidence.json").write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1))
