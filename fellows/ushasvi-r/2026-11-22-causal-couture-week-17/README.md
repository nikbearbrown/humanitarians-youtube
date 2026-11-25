# Causal Couture — Week 17 Technical Progress Report

**Organization:** Humanitarians.ai  
**Reporting window:** November 16–22, 2026  
**Phase:** 5 — Causal Intelligence / Analytical Governance  
**Scope:** Retrospective report; package prepared November 25, 2026.

## Objective
Extend the Week 16 reproducibility workflow with a lightweight evidence inventory and independent byte-integrity verification of the saved audit bundle. Week 16's submitted report recorded 62 passing regression tests and `reproduced_descriptive_evidence`; these are prior reported results, not a new Week 17 test run.

## Implementation
A standard-library Python utility checks the expected three Week 16 output files, the two original inputs, manifest/audit agreement, week labels and recorded audit/regression statuses. It emits a separate JSON verification record with individual check outcomes and the manifest/audit fingerprints. The original evidence is not edited. The accompanying protocol documents evidence retention, exception handling and interpretation boundaries.

## Deliverables
- `apps/api/run_week17_archive.py`
- `apps/api/test_week17_archive.py`
- `docs/WEEK17_EVIDENCE_PROTOCOL.md`
- `docs/WEEK17_TECHNICAL_REPORT.md`

## Verification
Five Week 17 unit tests passed in the package development environment using synthetic fixtures. Local combined regression suite: **72/72 tests passed in 0.224 seconds on November 25, 2026.** All 11 archive integrity checks passed against the existing evidence files. Final archive status: **verified_archive**. No new empirical or causal result is claimed.

## Limitations and next steps
The manifest is not digitally signed; a trusted reference copy is necessary for stronger integrity assurance. Verification does not independently replay Week 16 tests, validate source truth or establish a backup. Run against the original local evidence, retain the verification JSON and investigate discrepancies. Week 18 will use this record for a documented analyst handover.
