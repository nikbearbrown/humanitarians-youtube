# Sources

## Primary source — Adwait Changan, Mycroft Finance Investigator (this week)

Project root: `/Users/adwaitchangan/Study/Latest Mycroft/mycroft/projects/Mycroft-Finance-Investigator`

On-screen code and artifacts are trimmed verbatim from:
- `mycroft_finance_investigator/review.py` — `build_review_request()` (B05); `AGENT_IDENTITIES`
  + reviewer/agent rejection + APPROVE requirements + append-only `open("x")` (B07)
- `mycroft_finance_investigator/cli.py` — `review-request` and `record-review` subcommands (B10)
- `schemas/review-decision.schema.json` — required fields + enums (B08)
- `tests/test_review.py` — the 7 review-control tests (B11)

## The 7 new review-control tests (verbatim names)
1. `test_review_request_is_open_and_bound_to_source_hash`
2. `test_agent_cannot_clear_human_gate`
3. `test_approval_requires_causal_explanation`
4. `test_unknown_evidence_is_rejected`
5. `test_request_changes_keeps_gate_closed_without_causal_claim`
6. `test_record_is_append_only`
7. `test_decision_must_match_run`

## Reported figures (this week)
- Recap run: 43 data rows across six synthetic datasets; Budget EBITDA $350,000; Actual
  $230,000; Variance −$120,000; 7 tool steps; 41 evidence references.
- Tests: 7 new review-control tests; **19 passing this week** (12 finance + 7 review).

## Provenance rule
Local deterministic workflow — no external LLM in the runtime. The committed sample review
request remains **OPEN**; no human approval or causal explanation was fabricated. Narration
is limited to what the code and artifacts actually do.

## Credits
Fellow/builder/narrator-of-record: **Adwait Changan** · Voice: Kokoro `am_onyx` ("Onyx, in
for Humanitarians AI") · Channel: **@HumanitariansAI**
