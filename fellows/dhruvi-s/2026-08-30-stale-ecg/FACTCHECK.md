# FACTCHECK — stale-ecg

**Status: GATE F — 20 rows checked, 18 PASS, 2 FIXED. Re-verified 2026-08-30
directly against the JSON, not against the write-up.**

Method: every number spoken or shown was re-read from `results/results.json` and
`results/within_patient.json` at check time. `README.md` and `PAPER.md` were
treated as *secondary* — where write-up and data disagreed, the data won and the
disagreement is recorded. Two rows required a fix; both are marked and both were
applied before this file was signed off.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | 144,668 admissions · 52,047 patients · 5,274 deaths | ✓ PASS | `results.json → design` — exact | — |
| 2 | B00 | EHR only AUROC 0.8574; EHR+ECG 0.8595 | ✓ PASS | `overall.EHR.auroc` 0.85744; `overall["EHR+ECG"].auroc` 0.85953 | — |
| 3 | B00/B01 | Added value +0.0021 | ✓ PASS | 0.859534 − 0.857444 = 0.002090 → +0.0021 | — |
| 4 | B01/B04 | ≤1 day: +0.0046 [+0.0028, +0.0061], n=77,973, 3,211 deaths | ✓ PASS | `by_staleness[0]` — exact to 4dp | — |
| 5 | B01/B04 | 1–30 days: +0.0053 [−0.0002, +0.0110], n=17,504, 436 deaths | ✓ PASS | `by_staleness[1]` | — |
| 6 | B01/B04 | 1–12 months: +0.0003 [−0.0042, +0.0045], n=20,363, 535 deaths | ✓ PASS | `by_staleness[2]` (delta 0.000275) | — |
| 7 | B01/B04 | >1 year: −0.0048 [−0.0079, −0.0018], n=28,828, 1,092 deaths | ✓ PASS | `by_staleness[3]` | — |
| 8 | B04 | Middle two bins are **underpowered, not null** | ✓ PASS | `powered_for_fresh_effect: false` on both; MDE 0.0080 and 0.0065 both exceed the fresh effect (0.0046) they would need to detect | Hatched fill + explicit on-screen stamp; narration states it |
| 9 | B04 | Fresh and >1yr intervals both exclude zero | ✓ PASS | [0.0028, 0.0061] and [−0.0079, −0.0018] | — |
| 10 | B03 | Code is `cluster_bootstrap()` from `src/analyze.py`; n = 1000 replicates | ✓ PASS | Verbatim; `N_BOOT = 1000` | 9:16 re-wrapped at existing expression boundaries only — statements byte-identical |
| 11 | B06 | Code is `oof_cross_lag()` from `src/within_patient.py`; lags 0/30/180/365 | ✓ PASS | Verbatim, incl. the author's own inline comment; `STALENESS_LAGS_DAYS = [0, 30, 180, 365]` in `config.py` | — |
| 12 | B07 | 40,764 admissions · 16,157 patients · 1,262 deaths | ✓ PASS | `within_patient.json → design` | — |
| 13 | B07 | Same-day ECG: +0.0056 [+0.0011, +0.0099] | ✓ PASS | `by_ecg_age[0].value_vs_no_ecg` = 0.005553, median age 0.17d | — |
| 14 | B07 | Median ~508 days: −0.0051 [−0.0092, −0.0012], interval excludes zero | ✓ PASS | `by_ecg_age[3]`, median 508.4d | — |
| 15 | B07 | "Crosses into negative territory somewhere around two weeks" | ⚠ **HEDGED — interpolated** | Measured lags are 0 and 30 days (median ages 0.2d and 139d). The crossing is *between* measured points, never observed | Kept with "somewhere around"; chart draws straight segments between measured points, not a fitted curve. **Flagged in `NARRATION-GATE-P.md` for human decision** |
| 16 | B08 | Training distribution = all same-day | ✓ PASS | `design.train_lag: 0` — true by construction | On-screen caption says "train_lag = 0", not a measured distribution |
| 17 | B08 | Deployment mix: 53.9 / 12.1 / 14.1 / 19.9 %; "46% carry an ECG older than a day" | ✓ PASS | Bin n's ÷ 144,668 = 53.9/12.1/14.1/19.9; 100 − 53.9 = 46.1 → "46%" | **FIXED row.** First render drew invented bar shapes with no numeric basis. Replaced with these real proportions |
| 18 | B08 | Falsifier: train on stale ECGs → lands back at EHR-only | ✓ PASS | `reverse_train_on_stale.by_lag` = 0.8534 / 0.8504 / 0.8515 / 0.8517 vs `ehr_only` 0.8518 — straddles it within ±0.0015 | — |
| 19 | B08B | Gap as a feature: +0.0007 [−0.0019, +0.0031] | ✓ PASS | `freshness_aware[3].aware_minus_blind` (lag 365) | **FIXED row.** First draft used bounds inferred from the README's *range of point estimates* (+0.0007 to +0.0013) as if it were a CI. It is not. Replaced with the verbatim bootstrap interval |
| 20 | B08B | Training-mix match: +0.0032 [−0.0018, +0.0078]; both remedies inconclusive | ✓ PASS | `training_mix_remedy[3]`; every interval in both remedy blocks crosses zero at every lag | Panel stamped INCONCLUSIVE — NOT SOLVED |

---

## Description-copy rows (not spoken in the reel)

| # | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| D1 | Decay contrast +0.0092 (95% CI 0.0057–0.0126) | ✓ PASS | `decay_test.contrast_fresh_minus_stale` 0.009246, lo 0.005749, hi 0.012620 | — |
| D2 | Slope −0.0033 AUROC per decade of days | ✓ PASS | `decay_test.slope_per_log10_day` = −0.003278 | — |
| D3 | Bootstrap p < 0.001 | ✓ PASS *(with source caveat)* | `bootstrap_p_no_decay` stores `0.0`. With 1,000 replicates and zero exceedances the reportable value is `p < 0.001` — which is what `README.md` says | Use the README phrasing. **Upstream: the JSON writer should emit `<1/N`, not `0.0`** |
| D4 | "Stable across 5 of 5 fold seeds" | ✗ **FAIL → FIXED** | `seed_summary.n_seeds_positive` = 5 ✓, but per-seed contrasts run +0.0061 to +0.0094 (mean +0.0078) against a +0.0092 headline. The **sign** replicates; the **magnitude** varies by ~1.5× | Rewritten to: *"stays positive in 5 of 5 fold seeds, though its magnitude varies (+0.0061 to +0.0094) — the sign is what replicates, not the size"* |
| D5 | Limitations block (waveform, effect size, single-centre, exclusions 23.5%) | ✓ PASS | `README.md` §Limitations, carried without softening | — |

---

## Claims deliberately NOT made

- **No clinical recommendation.** The reel never says what to do with a patient. It is about model evaluation.
- **No causal claim about outcomes.** Single-centre retrospective; the within-patient design removes case mix, not unmeasured time-varying confounding. The reel says "this is not case mix", never "this causes deaths".
- **No smooth decay across the four bins.** The 1–30 day bin sits nominally *above* the fresh bin (+0.0053 vs +0.0046) on 436 deaths. The chart plots it as-is and the narration does not narrate a monotone decline — consistent with the source's own caution that the decay claim rests on the continuous slope and the within-patient result.
- **No equity claim.** The Medicaid/Private stale-exposure finding is real (`staleness_by_subgroup`) but scoped out of this cut. It is not alluded to.
- **No waveform claim.** Features are report + structured measurements only.

---

## Data-use verification

MIMIC-IV and MIMIC-IV-ECG are credentialed PhysioNet resources under a DUA.
Frame-by-frame check of all 12 beats: every on-screen quantity is a cohort count,
an AUROC, a bootstrap interval, or a percentage of the cohort. **No patient-level
record, waveform, identifier, admission date, or row-level value appears in any
frame or in any narration line.** Consistent with the source repository's own
policy that only aggregate results and figures leave the machine.

---

## Sign-off

```
GATE F — factcheck

Reviewer:  ______________________     Date: __________

[ ] Signed — 18 PASS, 2 FIXED, 1 hedged row (#15) accepted
[ ] Signed with changes (row #15 requires audio regen if reworded)
[ ] Not signed
```

Row #15 is the only line where narration reaches past a measured value. It is
hedged in the script and drawn honestly in the chart, but it is a human call —
see `NARRATION-GATE-P.md` §"Points requiring human judgement".
