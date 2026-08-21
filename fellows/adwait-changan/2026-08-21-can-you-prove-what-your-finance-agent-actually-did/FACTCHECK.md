# Fact-check gate

Status: **CODE-BOUND** — every code excerpt is trimmed verbatim from the real Mycroft files (PR #17);
counts and status strings are read from `bundle.py` / `test_bundle.py`.

| Beat(s) | Claim | Verdict | Evidence |
|---|---|---|---|
| B04 | Before packaging, the bundle re-checks review run_id + source_run_sha256 and scenario baseline/plan hashes; any mismatch raises BundleError. | CONFIRMED | `bundle.py _validate_cross_artifact_contract()` (verbatim). |
| B05 | Seven things validated before packaging: run ID, validation result, review-request hash, evaluation-case hash, scenario-plan hash, raw-data hashes, verified-data hashes. | CONFIRMED | `_validate_cross_artifact_contract()`. |
| B06 | 54 artifacts (raw+verified data, config, schemas, code, tests, logs, reports, recipe, conductor) + manifest.json, manifest.sha256, REVIEW.md. | CONFIRMED | `default_bundle_sources()` (2+6+6+18+10+5+7=54); `build_audit_bundle()` outputs. |
| B08 | verify-bundle recomputes manifest + REVIEW checksums + each artifact's size/SHA-256, rejects extra/missing/altered → `INTEGRITY_MATCHED_HUMAN_REVIEW_OPEN`. | CONFIRMED | `verify_audit_bundle()` (verbatim return status). |
| B09 | Seven tamper cases rejected (altered manifest, modified reviewer view, changed artifact, extra unlisted file, mismatched run hash, unsafe bundle ID, overwrite attempt); 9 bundle tests; 41 total; both CI checks passed. | CONFIRMED (CI fellow-reported) | `tests/test_bundle.py` (9 tests, names in SOURCES.md); suite total 41. CI pass per fellow/PR #17. |
| B10 | SHA-256 proves file integrity, not identity, adequacy, or human approval. | CONFIRMED | `REVIEW.md`: "an integrity checksum, not a signature, human attestation, or release approval." |
| B11 / BVDT | Recipe DRAFT; release BLOCKED_PENDING_HUMAN_REVIEW; five human gates open (materiality, causal explanation, evaluation adequacy, scenario approval, distribution). | CONFIRMED | `bundle.py` open_gates + `release_status` const; schema. |

## Corrections applied
- (none — code, inventory count, and figures verified before render.)
