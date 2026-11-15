# Causal Couture — Week 16 Technical Progress Report (Draft)

**Organization:** Humanitarians.ai  
**Project:** Causal Couture  
**Reporting window:** November 9–15, 2026  
**Phase:** 5 — Causal Intelligence / Analytical Governance  
**Focus:** Reproducibility Auditing, Evidence Integrity, and Regression Verification

## Objective

Extend the Week 15 descriptive data-quality intelligence workflow with a reproducibility audit. The objective is to verify that a saved Week 15 quality report corresponds to the same input CSV, that its reported metrics can be recomputed, and that the existing unit-test suites can be rerun with captured failures. This does **not** estimate or validate a causal effect.

## Implementation prepared

1. **Evidence integrity:** SHA-256 comparison of the CSV against the fingerprint in the saved Week 15 JSON report. Missing and mismatched hashes produce explicit failures.
2. **Profile reproduction:** Recompute the Week 15 quality profile using the installed Week 15 module, then compare the recorded and recomputed data-quality metrics, temporal coverage, attrition, SKU profiles, and findings.
3. **Regression capture:** Optional isolated execution of the Week 12, 14, 15 and 16 `unittest` modules, with captured exit status and a bounded test-output excerpt. Nonzero results or timeouts are recorded as failures.
4. **Governance statuses:** Distinguish `blocked`, `requires_review`, and `reproduced_descriptive_evidence`. The last status only means the requested descriptive reproduction checks passed, not model approval.
5. **Audit outputs:** Generate structured JSON, Markdown, a self-contained HTML dashboard, and a separate SHA-256 manifest of the inputs and three report outputs.
6. **Safety:** Avoid modifying the source CSV or the Week 15 JSON, escape untrusted strings in HTML, and flag optional baseline/Phase 5 evidence inputs as not replayed.

## Deliverables

- `apps/api/causal_audit_integrity.py`
- `apps/api/causal_audit_dashboard.py`
- `apps/api/run_week16_audit.py`
- `apps/api/test_week16_audit.py`
- `docs/WEEK16_INSTALL_AND_RUN.md`
- `docs/WEEK16_TECHNICAL_REPORT.md`
- `examples/SYNTHETIC_week16_daily_sku.csv` (test fixture only)

## Verification status — update after running on your Mac

- Week 16 development tests: **23/23 passed locally**
- Combined Week 12/14/15/16 tests: **62/62 passed locally**
- Real unified CSV path and fingerprint: **CSV: 20260923_221605_unified_daily_sku.csv; SHA-256: d8e0d6c23626e5e738715fe3722fe7beaac8fee1754ff8786f8bef0234d84e2c**
- Saved Week 15 JSON comparison: **See reports/week16/week16_audit.json for the recorded comparison**
- Week 16 audit status: **reproduced_descriptive_evidence**
- Personal repository commit: **[not yet verified]**
- Humanitarians.ai fellows submission: **[not yet verified]**

**Prior discrepancy to investigate:** The submitted Week 15 progress report recorded 38/39 combined tests passing, while its installation guide stated 39/39. The Week 16 workflow is designed to capture a fresh test run rather than assume the discrepancy has been resolved.

## Limitations

A matching hash and reproduced descriptive metrics do not establish source correctness, statistical power, causal identification, production readiness, or business impact. The optional Week 15 baseline and saved Phase 5 evidence inputs require separate replay. Development fixtures must not be presented as observed retail results.

## Next steps

Run the Week 16 suite in the existing project, reproduce Week 15 results using the exact original CSV, investigate any mismatches or failing tests, retain local evidence, then commit verified source files and update this report with actual results before submission.
