# FACTCHECK — "Who Approves the Threshold?"

Source of truth is `materiality.py` in `nikbearbrown/mycroft` PR #17 and the shipped CLI run
against the project's real verified pack. Nothing on screen was retyped.

| # | Claim (beat) | Verdict | Basis |
|---|---|---|---|
| 1 | "Every report flagged variances as material using an unapproved threshold" (B00, B02) | **ACCURATE** | `materiality_status: DEMO_UNAPPROVED` is pinned by schema const in `trend-plan.schema.json` and carried in every generated report; "approve or replace the demo materiality" appears as a standing open issue in the bundle. |
| 2 | Four judgements rest on it: revenue, COGS, opex, payroll (B02) | **VERIFIED** | The four categories in `finance.py` `CATEGORIES`, and the four rows of the category bridge in every run log. |
| 3 | B04 code, five lines (B04) | **VERIFIED — verbatim** | `inspect.getsource(materiality.validate_approval)`, the `approved_by` block, dedented only. Line count counted. |
| 4 | The four attempts and their outcomes (B05) | **VERIFIED BY EXECUTION** | Captured from four real `record-materiality` runs against the real pack. Messages copied from stdout. |
| 5 | "Approved at 10000.00 by Dana Whitfield, Controller" (B05) | **REAL OUTPUT of a fixture decision** | The run is real; the approver name is a **test fixture**, not a person who approved anything. No approval record with this name is committed. See corrections. |
| 6 | Hash binding: request records, decision carries, read-back re-hashes (B06, BVDT) | **VERIFIED** | `build_approval_request` hashes all six files; `validate_approval` compares; `approved_threshold` re-hashes on read. |
| 7 | "Change one byte of actuals.csv and the approval stops applying" (B07) | **VERIFIED BY TEST** | `test_threshold_refuses_after_the_data_changes` exercises exactly this and is among the 18 passing cases. |
| 8 | "No approved threshold is shipped" (B09, BVDT) | **VERIFIED** | The repository contains `config/sample-materiality-approval.json` only, whose own `reasoning` field reads "SAMPLE FIXTURE, NOT AN APPROVAL". |
| 9 | The three-question rule (B08, BVDT) | **EDITORIAL** | The fellow's framing, demonstrated rather than asserted: B06 and B07 show the third question enforced in code. |
| 10 | "An agent that approves its own threshold has hidden who decided" (B03) | **EDITORIAL** | A judgement, phrased as one. The mechanism beneath it — the identity refusal — is row 3. |

## Corrections applied during authoring

- **The approver name is labelled as a fixture, not implied to be real.** The CLI output is
  genuine, but "Dana Whitfield, Controller" is a test value. The video never claims a real
  person approved anything, and B09 states on screen that no signature is shipped.
- **"Every framework" phrasing avoided.** No competing tool or framework is named anywhere.
- **No claim that the approved amount is correct.** The verdict's final line states the
  opposite explicitly.

## Anti-dating audit

No model, vendor, benchmark or price appears. On-screen identifiers are `materiality.py`,
`record-materiality`, `AGENT_IDENTITIES`, the six source filenames and the four categories.

## Verdict

> FACT GATE: CLEARED. Rows 3, 4, 6, 7 and 8 verified by execution or source; row 5 discloses
> the fixture; rows 9 and 10 labelled editorial.

## Corrections applied 2026-10-26

- B05's artifact title now reads "four attempts, test fixtures", so the named approver on screen is unambiguously a fixture rather than a person who signed something.
