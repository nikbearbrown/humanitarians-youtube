# Week 17 — Evidence archival and verification protocol

## Purpose and scope
Preserve the evidence chain established in Week 16 without refitting the causal model. The archive is the existing local report directory, not a new backup service. Verification compares actual file bytes with the existing manifest and checks the recorded audit and regression statuses. It does not establish authenticity against a malicious party able to replace the manifest and all files.

## Evidence inventory
| Artifact | Role | Handling |
|---|---|---|
| Original unified daily-SKU CSV | Source observations | Retain unchanged; restricted access |
| Week 15 quality JSON | Recorded descriptive profile | Retain exact bytes |
| Week 16 audit JSON | Recorded checks and regression result | Verify hash and status |
| Week 16 audit Markdown | Human-readable evidence | Verify hash |
| Week 16 audit HTML | Offline dashboard | Verify hash |
| Week 16 manifest JSON | Expected fingerprints | Retain separately in a trusted location |
| Week 17 archive JSON | Verification record | Retain with manifest fingerprint |

## Verification procedure
1. Identify the exact CSV and Week 15 JSON used in the Week 16 audit; do not substitute a newer export.
2. Verify the Week 16 labels and expected inventory. Compare the manifest input entries against the audit JSON input entries.
3. Compute SHA-256 over each original input and each of the three output files. Compare with the manifest; the manifest does not hash itself.
4. Check that the recorded audit status is `reproduced_descriptive_evidence` and the recorded regression status is `pass`. This does not rerun the tests.
5. Save the Week 17 JSON outside the Week 16 bundle. Record the manifest and audit hashes in the verification record.

## Exception handling
| Condition | Response |
|---|---|
| Missing file | Locate original artifact or document absence; do not fabricate it |
| Changed bytes | Quarantine the altered copy and recover the original from a trusted location |
| Input identity disagreement | Reconcile source names and fingerprints with the original audit |
| Recorded audit not reproduced | Retain the failure and investigate the original audit |
| Malformed JSON | Stop execution; recover a readable original record |

A `requires_review` result is not a reason to delete or regenerate historical evidence. If a new run is needed, retain it separately and record why. A missing or unreadable manifest/audit causes a CLI error rather than a successful verification record.

## Retention and access
Keep source data and generated evidence outside public commits unless approved. Maintain a separate trusted copy of the manifest and document the code revision, environment and data owner where known. Retention duration and access policy require organizational approval; no retention period or storage service is assumed here. Hashes detect byte differences relative to the reference, not truthfulness, source completeness, or causal validity.
