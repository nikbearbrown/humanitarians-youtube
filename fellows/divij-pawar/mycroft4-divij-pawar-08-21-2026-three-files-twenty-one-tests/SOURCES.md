# SOURCES.md — three-files-twenty-one-tests (Video 2 of 2)

**DOUBLE-CHECK LAW.** Every factual claim spoken in this reel traces to the
source script, and through it to the code and logs it describes. This reel makes
claims about a real codebase, so **every number here is re-verifiable against the
repository** — if a figure cannot be reproduced, cut the claim rather than
hedging it.

**Primary source:**
`D:/Code/mycroft/verification-layer/divij/video-script-cross-agent-validation-20min.md`
(PART TWO — chapters 7–13 + close).

**Upstream sources the script itself cites:**

| Ref | Document |
|---|---|
| S1 | `verification-layer/divij/audit.md` — architecture audit, orphan counters, node-layer fingerprinting |
| S2 | `verification-layer/divij/sdd.md` — the design document |
| S3 | `verification-layer/logs/RUN_LOG.md` (2026-08-21) — the known-gaps list, logged the day it was built |
| S4 | `verification-layer/cross_validation.py` — the orchestration + comparison |
| S5 | `verification-layer/adapters/fixture_adapter.py` |
| S6 | `verification-layer/tests/test_cross_validation.py` |
| S7 | `verification-layer/consistency.py` — scoring weights, thresholds, module docstring |
| S8 | `verification-layer/web/db.py` — runs table, append-only triggers |
| S9 | `verification-layer/schemas.py`, `middleware.py`, `parser.py` — ReasoningObject, validation loop |
| S10 | `verification-layer/divij/cross-agent-validation-proposal.md` |

---

## Numeric claims spoken aloud

| Beat | Spoken as | Value | Source |
|---|---|---|---|
| B00 | "three files, twenty-one tests" | 3 / 21 | Script ch.10, ch.12 → S4, S5, S6 |
| B02 | "sixty percent number overlap, forty percent word overlap" | 0.6 / 0.4 | Script ch.7 → S7 |
| B02 | "three thresholds" | 0.70 / 0.40 / below | Script ch.7 → S7 |
| B03 | "twenty-one thousand, eight hundred and twenty-four bytes of specification" | 21,824 | Script ch.8 → S1 |
| B03 | "sixteen scaffolded scripts" | 16 | Script ch.8 → S1 |
| B03 | "zero shared logic connecting them" | 0 | Script ch.8 → S1 |
| B03 | "thirty thousand, four hundred and ninety-seven lines" | 30,497 | Script ch.8 → S1 (node layer, 460 scripts) |
| B03 | "one thousand two hundred and seventy-six … real logic" | 1,276 | Script ch.8 → S1 (8 modules) |
| B03 | "Tests: zero" | 0 | Script ch.8 → S1 |
| B04 | "four open critical security findings" | 4 | Script ch.9 → S1 |
| B06 | "twenty-one new, all passing" | 21 | Script ch.12 → S6 |
| B06 | "seven tests fail" (symmetric_difference → intersection) | 7 | Script ch.12 → S3, mutation run |
| B06 | "three more" (`None` → `False` on halt) | 3 | Script ch.12 → S3, mutation run |

### Figures shown on screen but not spoken

| Beat | On-screen | Value | Source |
|---|---|---|---|
| B02 | HIGH 0.70 / MEDIUM 0.40 / LOW below 0.40 | — | Script ch.7 → S7 |
| B03 | "conductor documents: 1" | 1 | Script ch.8 → S1 |
| B03 | Bar chart 30,497 vs 1,276 | — | Script ch.8 → S1 |
| B06 | "129 / 129" | 129 | Script ch.12 — 21 new + 108 pre-existing → S6 |
| B06 | "file restored byte-identical, suite reconfirmed" | — | Script ch.12 → S3 |
| B06 | `run_id: 7f3a…` | illustrative | Script ch.11 — a redacted example ID, not a real run |

**Not spoken, deliberately:** the file line counts (331 / 81 / 375). B05 says
"the test file is the biggest of them" instead. If you want the exact numbers
back, they are in script ch.10 → S4, S5, S6 and are safe to state.

## Non-numeric factual claims

| Beat | Claim | Source |
|---|---|---|
| B01 | An accountability layer already existed whose job was to put reasoning permanently on the record | Script ch.7 → S9 |
| B01 | It could enforce the record but not verify its truth | Script ch.7, "a perfect filing cabinet for claims of unknown accuracy" |
| B01 | Cross-agent validation was already named on the published architecture diagram, with no implementation | Script ch.8 → S1 |
| B02 | `ReasoningObject` is frozen/immutable after write; holds conclusion, steps, confidence, sources | Script ch.7 → S9 |
| B02 | The validation loop retries exactly once, then halts; both attempts are recorded regardless | Script ch.7 → S9 |
| B02 | The store is SQLite with database-level triggers raising ABORT on update or delete | Script ch.7 → S8 |
| B02 | The consistency probe's scoring already existed and was pointed at one agent vs. a repeat of itself | Script ch.7 → S7 |
| B03 | The orchestration layer declared three mechanisms, all with zero implementation | Script ch.8 → S1 |
| B03 | No one had built it because the project had ~no agents emitting comparable conclusions | Script ch.8 |
| B04 | Producer A is a real agent wired to live SEC EDGAR endpoints (standard library HTTP, no new dependency) | Script ch.9 |
| B04 | Producer B is a hand-written fixture returning a pre-chosen conclusion | Script ch.9 → S5 |
| B04 | With two real producers, "agents disagree" and "comparator broken" are inseparable hypotheses | Script ch.9 |
| B04 | Contradiction is defined as numeric divergence only — no entailment model, no LLM judge | Script ch.9 → S4 |
| B04 | v1 writes a record and stops: no escalation, no alert, no resolution | Script ch.9 → S4 |
| B04 | No new HTTP route was added, so no existing security finding is newly reachable | Script ch.9 → S1 |
| B05 | Each agent receives its own context, by function signature | Script ch.10 → S4 |
| B05 | On `HaltError`, the exception's reasoning objects are carried forward rather than dropped | Script ch.10 → S4 — **VERBATIM: the code comment reads "The halt is the evidence"** |
| B05 | The comparison is `set(a_numbers).symmetric_difference(set(b_numbers))` | Script ch.10 → S4 |
| B05 | `_compute_score` and `_classify` are imported unmodified from the consistency module | Script ch.10 → S4, S7 |
| B05 | The symmetric difference catches both a differing value and a missing value, with no special case | Script ch.10 → S4 |
| B06 | Both agents share one run ID; both records are persisted | Script ch.11 → S4 |
| B06 | The runs table stores a free-form JSON payload, so no migration/table/column was needed | Script ch.11 → S8 |
| B06 | The append-only triggers apply to the new record; a written flag cannot be updated or deleted | Script ch.11 → S8 |
| B06 | A passing suite proves tests agree with code, not that they'd catch a wrong implementation | Script ch.12 |
| B06 | `false` claims a check ran and was clean; `null` says the check could not run | Script ch.12 → S4, S6 |
| B07 | Comparison is numeric only; prose disagreement citing the same figures passes | Script ch.13 item 2 → S3 |
| B07 | Producer B is still a fixture; no genuine cross-agent disagreement has been observed on live data | Script ch.13 item 3 → S3 |
| B07 | The record is retrievable by run ID but not SQL-queryable | Script ch.11, ch.13 item 4 → S8 |
| B07 | A flagged contradiction triggers nothing — no alert, no escalation, no named human | Script ch.13 item 6 → S3 |
| B09 | "The judgment stays with the human" | Script close → project constitution ("AI executes, humans decide") |

## Verbatim quote law

Two strings must appear on screen **exactly as they are in the source** — do not
reword, reflow, or "improve" them:

1. **B05's halt comment:** `# The halt is the evidence — carry its records forward rather than dropping them.` (S4)
2. **B06's payload key:** `cross_agent_comparison` (S4) — the highlighted key in the payload dict.

The `run_id: 7f3a…` shown in B06 is a redacted illustrative ID, not a real run.
Label it as such if the frame allows, or leave it truncated.

## Simplifications, declared

1. **B05 says "the test file is the biggest of them"** rather than quoting
   331 / 81 / 375 lines. Same claim, fewer numbers to verify on screen.
2. **B02 compresses four components into one diagram.** No claim is made about
   any component's internals beyond what's listed above.
3. **B03's "That's the pattern everywhere"** refers to the node-layer
   fingerprinting result in S1 (352 of 460 scripts are freestanding 74-line
   templates). The fingerprinting method is not explained in the reel; only its
   headline result is used.
4. **Video 1's research context is not restated.** This reel assumes Video 1
   or accepts that a viewer arrives without it — nothing in the argument depends
   on the research half. (Video 1 itself refers to that research generically,
   never naming a specific outside system — see its `SOURCES.md`.)

## Claims deliberately NOT made

- That the system has caught a real contradiction. It has not (B07 says so).
- That numeric divergence is a good proxy for disagreement in general. B07 says
  the opposite.
- That the accountability layer is secure. Four critical findings remain open
  (B04); the reel claims only that no new route was added.
- Any claim about `pattern recognition` or `dynamic task allocation` beyond
  "zero implementation."

## Known gap NOT stated in this reel

Script ch.13 item 1 — **only `HaltError` is caught per agent; any other exception
(rate limit, failed EDGAR fetch) propagates and aborts the whole comparison,
discarding the other agent's already-collected records.** This is a real,
logged gap (S3) and it is **absent from every beat of this sheet.** See
`PEDAGOGY.md` for the reasoning and the two places it could be restored. Flagged
here so the omission is on the record rather than accidental.
