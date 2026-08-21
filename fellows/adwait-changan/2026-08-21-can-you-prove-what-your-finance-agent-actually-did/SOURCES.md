# Sources

## Primary source — Adwait Changan, Mycroft Finance Investigator (this week · PR #17)

Project root: `/Users/adwaitchangan/Study/Latest Mycroft/mycroft/projects/Mycroft-Finance-Investigator`

On-screen code and artifacts are trimmed verbatim from:
- `mycroft_finance_investigator/bundle.py` — `_validate_cross_artifact_contract()` (B04),
  `default_bundle_sources()` inventory (B06), `verify_audit_bundle()` (B08)
- `mycroft_finance_investigator/cli.py` — the `bundle` and `verify-bundle` subcommands
- `schemas/audit-bundle.schema.json` — manifest contract (release_status const `BLOCKED_PENDING_HUMAN_REVIEW`, integrity `SHA-256`)
- `tests/test_bundle.py` — the 9 bundle tests

## Before packaging, bundle.py hash-validates (B05)
Investigation run ID · validation result (`CONFORMANT_SAMPLE`, equals run-log validation) ·
review-request `run_id` + `source_run_sha256` (+ gate OPEN, undecided) · evaluation `source_cases_sha256`
(+ PASS, matched==case_count, adequacy PENDING_HUMAN_REVIEW) · scenario `source_plan_sha256` +
`baseline_run_sha256` (+ classification SIMULATION_NOT_FORECAST, recommendation None, decision HUMAN_REQUIRED) ·
raw-data hashes · verified-data hashes · recipe `status: DRAFT`.

## The bundle (B06) — 54 artifacts + 3 integrity files
`default_bundle_sources()` inventory (counted): 2 raw meta + 6 raw CSV + 6 verified CSV + 18 (verified
meta/validation, investigation/evaluation/scenario config·log·report, recipe, conductor, project docs,
pyproject) + 10 implementation modules + 5 schemas + 7 tests = **54**. Outputs: `manifest.json`,
`manifest.sha256`, `REVIEW.md`. Manifest `release_status: BLOCKED_PENDING_HUMAN_REVIEW`.

## verify-bundle (B08) → `INTEGRITY_MATCHED_HUMAN_REVIEW_OPEN`
Recomputes manifest + REVIEW.md checksums and every artifact's size + SHA-256; path-escape guard;
rejects extra/missing/altered files.

## The 9 bundle tests (test_bundle.py)
`test_builds_and_verifies_reviewer_handoff`, `test_bundle_is_immutable_by_default`,
`test_bundle_identifier_is_path_safe`, `test_verifier_detects_changed_packaged_artifact`,
`test_verifier_detects_changed_manifest`, `test_verifier_detects_changed_human_review_view`,
`test_verifier_detects_an_unlisted_artifact`, `test_cross_artifact_hash_mismatch_stops_packaging`,
`test_human_boundary_is_visible_in_review`.

## Reported figures (this week)
54 packaged artifacts · verify status `INTEGRITY_MATCHED_HUMAN_REVIEW_OPEN` · 7 tamper cases rejected ·
9 bundle tests · **41 passing tests** total · both GitHub CI checks passed (fellow-reported).

## Provenance rule
SHA-256 proves **file integrity, not identity, adequacy, or human approval** (REVIEW.md states this
verbatim). Recipe DRAFT; release `BLOCKED_PENDING_HUMAN_REVIEW`; five human gates open: materiality
approval, causal explanation, evaluation adequacy, scenario approval, distribution authorization.

## Credits
Fellow/builder/narrator-of-record: **Adwait Changan** · Voice: Kokoro `am_onyx` ("Onyx, in for
Humanitarians AI") · Channel: **@HumanitariansAI**
