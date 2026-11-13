# FACTCHECK — Mycroft Phase 6 (9:16)

**Source of truth:** `source/Mycroft_Phase6_Autonomous_Monitoring.ipynb` and its executed output,
saved verbatim as `docs/NOTEBOOK-OUTPUT.txt`. Figure 2 was extracted from the notebook's own
display data.

**Nothing was recomputed.** The notebook was not re-run and `Stock_Prices_Dataset.csv` is not in
this package. Every figure below is quoted from the author's executed run.

## Data

| # | Claim | Value | Status |
|---|---|---|---|
| F1 | Rows | 184,138 | verbatim ✅ |
| F2 | Tickers | 120 | verbatim ✅ |
| F3 | Date range | 2020-01-03 → 2026-02-11 | verbatim ✅ |

## Agent A — robust anomaly

| # | Claim | Source | Status |
|---|---|---|---|
| F4 | Rolling modified z-score, window 60, min_periods 30, scaled by 0.6745 | `rolling_modified_z()` | verbatim ✅ |
| F5 | Built on medians and MAD, not means | same | ✅ |
| F6 | Applied to `return_1d`, `Volume`, `intraday_range` | code | ✅ |
| F7 | `anomaly_severity` = max absolute z of the three | code | ✅ |
| F8 | Flag at ≥ 4.0 | `anomaly_flag` | verbatim ✅ |

## Agents B and C

| # | Claim | Source | Status |
|---|---|---|---|
| F9 | Agent B ranks within `["Date","Industry"]` | `peer_pct_*` | ✅ |
| F10 | Weights 50% (1−return_20d rank) / 25% volatility rank / 25% (1−drawdown rank) | `peer_weakness` | verbatim ✅ |
| F11 | Agent B flag at ≥ .80 | code | verbatim ✅ |
| F12 | Agent C ranks by Date across the whole market | `risk_score` | ✅ |
| F13 | Weights 40% volatility / 35% (1−drawdown) / 25% intraday range | code | verbatim ✅ |
| F14 | Agent C flag at ≥ .80 | code | verbatim ✅ |

## Agent D — thesis deterioration

| # | Claim | Source | Status |
|---|---|---|---|
| F15 | Health = 25% momentum + 20% sector-relative + 20% trend vs SMA-50 + 20% drawdown + 15% low volatility, ×100 | `thesis_health` | verbatim ✅ (sums to 1.00) |
| F16 | Flag when `thesis_change_20d <= -20` | code | verbatim ✅ |

## Agent E — isolation forest

| # | Claim | Source | Status |
|---|---|---|---|
| F17 | `IsolationForest(n_estimators=250, contamination=.03, random_state=42)` inside a `StandardScaler` pipeline | code | verbatim ✅ |
| F18 | **Fit on training dates only**, then scored on all rows | `iso.fit(train[ISO_FEATURES])` after `date_split` | ✅ **no lookahead in the fit** |
| F19 | Eight features | `ISO_FEATURES` list | counted ✅ |
| F20 | "The only machine-learning model here" | A–D are deterministic rules/ranks; E is the only fitted model | ✅ accurate |

## Review priority

| # | Claim | Source | Status |
|---|---|---|---|
| F21 | anomaly ×2 + peer ×1 + risk ×2 + thesis ×2 + multivariate ×2 | `review_priority` | verbatim ✅ |
| F22 | Maximum 9 | 2+1+2+2+2 | arithmetic ✅ |
| F23 | Plain integer weights, no learned model | code | ✅ |
| F24 | `explain_row()` writes the triggering value into each reason | code | verbatim ✅ |

## Monitoring summary — 2026-02-11

| # | Field | Value | Status |
|---|---|---|---|
| F25 | tickers_monitored | 120 | verbatim ✅ |
| F26 | flagged_for_review | 43 | verbatim ✅ |
| F27 | priority_5_plus | 3 | verbatim ✅ |
| F28 | anomaly_flags | 11 | verbatim ✅ |
| F29 | peer_outliers | 3 | verbatim ✅ |
| F30 | high_risk | 15 | verbatim ✅ |
| F31 | thesis_deteriorations | 29 | verbatim ✅ |
| F32 | multivariate_anomalies | 4 | verbatim ✅ |

## Review queue

| # | Claim | Status |
|---|---|---|
| F33 | SPGI priority 8 — robust_anomaly(z=7.5), risk_score=0.92, thesis_change20d=−74.0, isolation_score=0.025 | verbatim ✅ |
| F34 | SCHW 6 · UNH 5 · EMR 4 · GD 4 | verbatim ✅ |
| F35 | `human_decision` and `human_rationale` created as `None` | code + queue output | verbatim ✅ |
| F36 | Event log is JSON, one entry per row with priority > 0, carrying reasons and agent outputs | `events` loop | ✅ |

## The historical diagnostic

| priority | n | large-move rate | on screen |
|---|---|---|---|
| 0 | 122,102 | 0.1776 | **17.8%** ✅ |
| 1 | 1,018 | 0.2151 | — |
| 2 | 46,769 | 0.2268 | — |
| 3 | 2,035 | 0.2029 | dip ✅ named |
| 4 | 8,948 | 0.3438 | **34.4%** ✅ |
| 5 | 1,075 | 0.2679 | dip ✅ named |
| 6 | 1,028 | 0.3940 | **39.4%** ✅ |
| 7 | 228 | 0.2851 | dip ✅ named |
| 8 | 271 | 0.4059 | **40.6%** ✅ |
| 9 | 64 | 0.3281 | n = 64 ✅ named |

| # | Claim | Status |
|---|---|---|
| F37 | Large move = \|5-day forward return\| ≥ 5% | code ✅ |
| F38 | "The trend is real" | 17.8% at 0 rising to ~40% at 6 and 8 ✅ |
| F39 | "But it is noisy, it dips at 3, 5 and 7" | **true of the table** ✅ must stay on screen |
| F40 | "The high scores are rare (n = 64 at priority 9)" | verbatim ✅ |
| F41 | "A historical diagnostic, not a forecast" | the film's own framing; the notebook computes this in-sample over all history ✅ |

**This is the scene that bounds the claim.** The score ranks attention, not outcomes. It is not
evaluated out-of-sample, and the relationship is not monotonic. Never present it as predictive.

## Advisory

| # | Item | Status |
|---|---|---|
| A1 | "Research decision-support only. Agents prioritize evidence and anomalies; the human reviewer makes the final decision." | The notebook writes this string into every queue row; the film shows it in the S01 source line, the S12 strip and the end card ✅ |
| A2 | No profitability, performance or prediction-accuracy claim | audited — none present ✅ |
| A3 | Ticker symbols are public identifiers used as research examples | no personal data in the package ✅ |

## Open items — work in progress, not achievements

| # | Item | Why |
|---|---|---|
| W1 | The priority score is uncalibrated | Weights are hand-set integers, not fitted against outcomes |
| W2 | The diagnostic is in-sample | Computed over the whole history with no train/test separation for the score itself |
| W3 | Non-monotonic response | Dips at 3, 5 and 7 are unexplained; small n at high priorities |
| W4 | Agents A–D are thresholds, not models | Cut-offs (4.0, .80, .80, −20) are chosen, not learned |
| W5 | No scheduled run yet | "Daily monitoring" describes the pass the notebook performs, not a deployed job |

## Gate before publication

| Gate | Status |
|---|---|
| Re-run the notebook and confirm F1–F41 on the publish date | ⏳ |
| Confirm the ticker examples are still appropriate to show | ⏳ |
| Narration read aloud against the animatic | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
