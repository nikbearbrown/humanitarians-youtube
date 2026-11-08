# Causal Couture — Week 15 Technical Progress Report

**Organization:** Humanitarians.ai  
**Project:** Causal Couture  
**Reporting window:** November 2–8, 2026  
**Phase:** 5 — Causal Intelligence / Analytical Governance  
**Prepared:** November 8, 2026

## Objective

Extend the existing Week 12 evidence-review and Week 14 data-preflight workflows with a more comprehensive, reproducible **data-quality intelligence** layer. The focus is analytical reliability, input integrity, temporal structure, traceability, and transparent analyst review — not estimating a new causal effect.

## Implementation prepared November 8

1. **Dataset integrity and quality gate:** Implemented required-column checks; missing/invalid date, SKU, sales, and engagement handling; negative sales and out-of-range rate flags; duplicate SKU/date detection and conflicting-measurement identification. Duplicate keys are excluded from temporal counts rather than silently resolved.
2. **Temporal coverage and sample attrition:** Added an auditable stage-by-stage data attrition summary, next-calendar-day pairs, previous-observation/next-day candidate counts aligned to the existing Phase 5 builder, strict three-day windows, and multi-day observation gaps.
3. **SKU-level quality profiles:** Added per-SKU observation counts, time coverage, candidate rows, engagement variation, and descriptive sales/engagement metrics. The SKU breakdown is exportable to CSV.
4. **Optional dataset comparison:** Implemented baseline/current descriptive comparison of quality metrics, SKU overlap, coverage, and changes in average/median sales and engagement. Differences are not interpreted as statistically significant drift.
5. **Evidence-review compatibility:** Added an optional input for a previously saved Phase 5 JSON response, reusing the existing Week 12 evidence-review function without rerunning model estimation.
6. **Reproducibility and presentation:** Implemented SHA-256 source-file fingerprints, structured JSON, Markdown, a standalone HTML dashboard, and SKU CSV exports. HTML source values are escaped; the dashboard is self-contained and does not transmit data.
7. **Automated tests:** Added 20 tests for temporal logic, data quality, duplicate conflict handling, optional comparison, output generation, saved evidence review, safe HTML rendering, and input errors.

## Validation evidence

In an isolated development environment on November 8, **20/20 new Week 15 unit tests passed**. A combined regression run with the earlier Week 12 and Week 14 test modules passed **38/39 tests**. Sample output files were generated using synthetic test data.

These are **development-environment checks**, not proof of successful local installation, actual retail-dataset validation, or deployment. The real unified dataset still needs to be profiled on the contributor's Mac, and the results reviewed. No empirical business impact, causal significance, production adoption, or GitHub push is claimed in this draft.

## New source files

- `apps/api/causal_quality_gate.py`
- `apps/api/causal_quality_comparison.py`
- `apps/api/causal_quality_dashboard.py`
- `apps/api/run_week15_quality.py`
- `apps/api/test_week15_quality.py`
- `docs/WEEK15_INSTALL_AND_RUN.md`
- `docs/WEEK15_TECHNICAL_REPORT.md`

## Outstanding work

- Execute the Week 15 test suite in the local project environment and retain terminal output.
- Run the CLI against an actual unified daily-SKU CSV; inspect any `blocked` or `requires_review` findings and review sample sufficiency.
- Capture a screenshot of the local HTML dashboard if useful for fellowship documentation.
- Commit the seven new files, push to GitHub, and record the verified commit hash.
- If sufficient real data are available, independently assess the existing Phase 5 estimates and diagnostics; data quality alone cannot establish causal identification.

## Summary

Week 15 adds a substantive quality-governance layer to Causal Couture: structured data integrity checks, temporal coverage and attrition accounting, per-SKU diagnostics, descriptive dataset comparison, reproducible source fingerprints, offline visual reporting, and a 20-test unit suite. It strengthens analytical traceability and makes limitations more visible to reviewers while preserving the existing Phase 5 modeling implementation.

**Recordkeeping:** The work in this package was prepared on November 8, 2026, the final day of the Week 15 reporting window. Update this report with the actual local test results and GitHub commit after they occur; do not backdate unperformed work.
