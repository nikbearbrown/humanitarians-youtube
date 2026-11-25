# Week 18 — Analytical governance and analyst handover

## Purpose
Translate the verified evidence inventory into a conservative review workflow. The handover utility reruns Week 17 verification, compares the fresh result with the saved record and records whether the evidence package is ready for analyst review. No new model is fitted.

## Status policy
| Status | Meaning | Permitted next step |
|---|---|---|
| ready_for_analyst_review | Saved Week 17 record matches fresh verification and all checks pass | Human review of evidence and assumptions |
| hold_for_review | Record differs or integrity/status checks fail | Investigate and resolve before handover |

Neither status authorizes a causal claim or business action. Both authorization flags are always false. A CLI input error also prevents a successful handover.

## Review checklist
- [ ] Confirm data owner, collection period, SKU identity and engagement-rate definition.
- [ ] Confirm original source fingerprint and independently retained manifest.
- [ ] Inspect Week 15 missingness, duplicates, invalid measurements and temporal attrition.
- [ ] Distinguish prior-observation lags from strict consecutive-day windows.
- [ ] Assess sample sufficiency and within-SKU engagement variation.
- [ ] Review overlap, stockout, placebo, robustness and confounding-sensitivity diagnostics if available.
- [ ] Replay optional baseline and Phase 5 inputs separately if relied upon.
- [ ] Record reviewer, code revision, unresolved issues and decision rationale.
- [ ] Obtain appropriate human approval before operational use or external claims.

## Roles (proposed, not assigned)
The data custodian confirms source lineage and access. The analyst verifies descriptive evidence and documents diagnostic limitations. The project reviewer checks the interpretation and determines whether further analysis is warranted. Operational stakeholders decide whether a separately validated result may inform a business action. No actual sign-off is asserted by this package.

## Escalation and change control
If the source changes, create a new versioned evidence run rather than editing the original record. If verification fails, retain the mismatch, investigate and rerun only after documenting the resolution. If diagnostics are missing or inconclusive, retain the exploratory interpretation boundary. Record any exception and the reviewer responsible for resolving it.

## Handover record fields
Evidence run identifier; source and manifest fingerprints; Week 17 verification record hash; review status; code revision; reviewer name/date; unresolved issues; next action. The utility populates only machine-verifiable fields and open review items. Human approval remains external to the utility.

## Limitations
Matching bytes do not prove that the original measurements are correct. The utility checks a local evidence chain, not a signed attestation or external backup. It does not independently rerun the Week 16 regression suite or estimate an effect. It does not assess statistical power, identification assumptions, production readiness or financial impact.
