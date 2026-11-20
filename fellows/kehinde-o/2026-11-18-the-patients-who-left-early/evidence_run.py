"""Week 9 evidence run for 'The Patients Who Left Early'.

Uses github.com/Kenny0bi/cancer-survival-prediction's own synthetic cohort
(5,000 patients, seed 42), whose generator knows every patient's TRUE event
time before censoring hides it. A subclass keeps that true time; the run first
proves the subclass reproduces the repo's output exactly, then compares three
ways of handling censored patients against the truth.
"""
import json, os, sys
from pathlib import Path
import numpy as np

REPO = Path(os.environ.get("SURVIVAL_REPO", "cancer-survival-prediction")).expanduser()
sys.path.insert(0, str(REPO)); os.chdir(REPO)
from loguru import logger; logger.remove()
from src.config.settings import settings
from src.data.synthetic_generator import SyntheticCancerDataset

def kaplan_meier(time, event):
    """Product-limit estimate. Censored-at-t are still at risk at t."""
    order = np.lexsort((1 - event, time))          # events before censorings at ties
    t, e = time[order], event[order]
    uniq = np.unique(t[e == 1])
    S, s = [], 1.0
    for u in uniq:
        at_risk = np.sum(t >= u); d = np.sum((t == u) & (e == 1))
        s *= 1.0 - d / at_risk; S.append(s)
    return uniq, np.array(S)

def km_at(uniq, S, x):
    i = np.searchsorted(uniq, x, side="right") - 1
    return 1.0 if i < 0 else float(S[i])

def km_median(uniq, S):
    i = np.argmax(S <= 0.5)
    return float(uniq[i]) if S[i] <= 0.5 else float("nan")

# --- sanity check on a hand-computable example -----------------------------
# times 1,2,3,4,5 with the 2 censored: S(1)=4/5, S(3)=4/5*2/3, S(4)=..*1/2, S(5)=0
u, S = kaplan_meier(np.array([1., 2, 3, 4, 5]), np.array([1, 0, 1, 1, 1]))
hand = [0.8, 0.8 * 2 / 3, 0.8 * 2 / 3 * 0.5, 0.0]
assert np.allclose(S, hand), (S, hand)

# --- the repo's cohort, untouched ------------------------------------------
ref = SyntheticCancerDataset(n_patients=5000, seed=42); ref.generate()
obs_ref = ref.patients_df[["time_months", "event_observed"]].to_numpy()

# --- identical copy of _generate_outcomes that also keeps true_time --------
class WithTruth(SyntheticCancerDataset):
    def _generate_outcomes(self, df, lp, frailty, rng):
        k = settings.weibull_shape
        ref_median = df["cancer_type"].map(settings.reference_median_months).values
        lam = np.log(2.0) / np.power(ref_median, k)
        u = rng.uniform(1e-9, 1.0, len(df))
        true_time = np.power(-np.log(u) / (lam * np.exp(lp + frailty)), 1.0 / k)
        entry = rng.uniform(0, settings.accrual_months, len(df))
        admin_censor = settings.study_months - entry
        dropout = rng.exponential(settings.dropout_scale_months, len(df))
        censor_time = np.minimum(admin_censor, dropout)
        observed = np.minimum(true_time, censor_time)
        event = (true_time <= censor_time).astype(int)
        observed = np.clip(observed, 0.03, None).round(2)
        self.true_time = true_time
        import pandas as pd
        return pd.DataFrame({"time_months": observed, "event_observed": event}, index=df.index), np.log(lam)

wt = WithTruth(n_patients=5000, seed=42); wt.generate()
obs = wt.patients_df[["time_months", "event_observed"]].to_numpy()
assert np.array_equal(obs, obs_ref), "copy is NOT faithful to the repo"
T = wt.true_time; time = obs[:, 0]; event = obs[:, 1].astype(int)

H = 60.0  # five years
uniq, S = kaplan_meier(time, event)
res = {
  "faithful_to_repo": True,
  "n": int(len(T)), "censored": int((event == 0).sum()), "censored_share": round(float((event == 0).mean()), 4),
  "max_followup_months": float(time.max()),
  "truth":  {"median": round(float(np.median(T)), 1), "S60": round(float((T > H).mean()), 4)},
  "drop_censored": {"median": round(float(np.median(time[event == 1])), 1),
                    "S60": round(float((time[event == 1] > H).mean()), 4)},
  "censored_as_death": {"median": round(float(np.median(time)), 1),
                        "S60": round(float((time > H).mean()), 4)},
  "kaplan_meier": {"median": round(km_median(uniq, S), 1), "S60": round(km_at(uniq, S, H), 4)},
  "censored_before_60": int(((event == 0) & (time < H)).sum()),
  "censored_before_60_truly_alive_at_60": int(((event == 0) & (time < H) & (T > H)).sum()),
}
Path(__file__).with_name("evidence.json").write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1))
