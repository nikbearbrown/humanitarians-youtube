# FACTCHECK — Weekly work video

Source of truth is the **generated report and the source file**, not the PR description.
Where the two could differ, the generated artifact wins.

| # | Claim (beat) | Verdict | Basis |
|---|---|---|---|
| 1 | Actual EBITDA 261,000 → 230,000 → 265,000 (B00, B03, BVDT) | **VERIFIED** | `reports/generated/mycroft-finance-investigator-trend-week35.md`, Historical EBITDA table. |
| 2 | Movements −31,000 (DETERIORATED) and +35,000 (IMPROVED) (B03) | **VERIFIED** | Same table, "Change from prior" and "Movement" columns, copied verbatim. |
| 3 | "Fifteen separate refusal paths" (B00, B04, B06, BVDT) | **VERIFIED BY COUNT** | `inspect.getsource(trend._load_run)` contains exactly 15 `raise TrendError` statements. Scoped in the narration to *the loader*, not the module (which has 30). |
| 4 | B05 tamper-check code, ten lines (B05) | **VERIFIED — verbatim** | Extracted with `inspect.getsource`, dedented only; no lines added, removed or reordered. |
| 5 | "There is no branch that logs a warning and carries on" (B05) | **VERIFIED** | Both failure paths in the shown block `raise`. No warning-and-continue exists in `_load_run`. |
| 6 | Revenue, COGS and opex recur; payroll does not (B07, BVDT) | **VERIFIED** | Category Pattern table: revenue/cogs/opex adverse in 3 periods, `Recurring adverse: YES`; payroll 0 adverse periods, `NO`. |
| 7 | Payroll figures are favourable in all three periods (B07) | **VERIFIED** | +8,000 / +20,000 / +10,000 in the same table. |
| 8 | "49 tests pass" (B09, BVDT) | **VERIFIED** | PR #17 verification section: `python3 -m unittest discover -s tests -v` — 49 passed. Not independently re-run for this video; sourced from the PR's recorded result. |
| 9 | Recipe still `DRAFT`, materiality unapproved, human gate `OPEN` (B09, BVDT) | **VERIFIED** | Report header: materiality `10000.00 (DEMO_UNAPPROVED)`, `Human gate: OPEN`; PR "Human boundary" section. |
| 10 | "It supplies no forecast, no recommendation, no cause" (B08, BVDT) | **VERIFIED** | Report classification `HISTORICAL_COMPARISON_NOT_FORECAST`; "Current Explanation — Owner Required: _Intentionally blank._" |
| 11 | "It re-derives rather than re-reads" (B02) | **ACCURATE** | `_load_run` re-hashes every source file, constructs a fresh `FinanceEngine`, recomputes `ebitda_variance()`, and compares it to the logged observation before the run is admitted. |
| 12 | "A detector that flags everything is worthless" (B07) | **EDITORIAL** | The fellow's framing, stated as reasoning rather than as a finding. The *evidence* for discrimination — payroll returning NO — is the verified part. |

## Corrections applied during authoring

- **Scoped the refusal count.** An early draft said "fifteen refusal paths in the trend
  engine." The module contains 30; 15 are in `_load_run`. Narration now says the loader.
- **Dropped a causal phrasing.** A draft line read "revenue is the problem." Recurrence is
  not causation, and saying so would break the exact boundary the feature enforces. The line
  now says revenue *recurs*.
- **Sourced figures from the generated report rather than the PR summary.** The PR prose and
  the report agree here, but the report is the artifact the code actually produced.
- **Test count attributed, not re-run.** Row 8 records that 49 passing tests comes from the
  PR's recorded verification, not from a run performed for this video.

## Anti-dating audit

No model, vendor, benchmark or price appears. On-screen identifiers are all from the project:
`trend.py`, `_load_run`, `TrendError`, `_sha256`, the four category names, and the period
labels. Dollar figures are synthetic sample data and are labelled as such in B09 and BVDT.

## Verdict

> FACT GATE: CLEARED. Rows 1–7 and 9–11 verified against the generated report or the source
> file; row 8 is attributed to the PR's recorded run; row 12 is labelled editorial.
