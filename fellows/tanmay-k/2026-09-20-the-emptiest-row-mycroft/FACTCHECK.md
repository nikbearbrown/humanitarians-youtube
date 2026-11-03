# FACTCHECK — Week 23 work-video

Two kinds of claim in this film. **Claims about Lloyds** resolve to the case study's own
cited primary sources. **Claims about the build** resolve to a file and line in
`lloyds_financial_assistant_pipeline.zip`, and were verified by running the code, not by
reading it or trusting the case study's prose about it.

No row is scripted without a row here. Consistent with `[[real-defects-are-evidence-of-rigor]]`:
every row about the found-and-fixed defect states what happened plainly, and the framing
column at the bottom of this file records how each is meant to land — credit to the
process, not a takedown of the build.

---

## A. Claims about the build — verified by execution

| # | Claim | Verified how | Status |
|---|---|---|---|
| A1 | Architecture is a single, linear pipeline — Intake → Retrieval → Authorization Gate — run fail-fast by one orchestrator, not a multi-agent system | `orchestrator.py:1–18`, read directly | ✅ |
| A2 | The Gate is constructed *before* any query is processed, so a pipeline built without a valid decision function fails once, immediately, rather than partway through a real query | `orchestrator.py:35–39` | ✅ |
| A3 | `AuthorizationGate.__init__` raises `TypeError` if no callable decision function is supplied — zero default authorization criteria exist in the file, under any label | `gate.py:38–45`, executed directly (`AuthorizationGate(None)` raises) | ✅ |
| A4 | `AuthorizationGate.evaluate` raises `ValueError` if the supplied decision function returns anything other than a plain bool | `gate.py:56–63`, executed directly | ✅ |
| A5 | Gate terminal states are named `answered_directly` / `escalated_to_human`, matching Lloyds' own "refer to expert human support" phrasing rather than a generic `not_authorized` | `gate.py:48–64` | ✅ |
| A6 | Retrieval keeps three outcomes distinct — no record that day (`no_matching_record`), a record that day but the amount disagrees (`record_mismatch`), a match (`matched`) — rather than one "not found" bucket | `retrieval.py:19–45` | ✅ |
| A7 | Coaching queries are correctly classified and reported (`recognized_not_modeled` / `coaching_out_of_scope`) but deliberately not carried through Retrieval or the Gate — a stated scope decision, not an omission | `orchestrator.py:11–18, 79–87` | ✅ |
| A8 | **Original build: 29 tests, 29 passing on first complete run**, and this was recorded plainly as a clean pass | README.md, case study §4b/§6.2 — historical claim, not independently re-executed (the pre-adversarial-pass code no longer exists as a separate state in the delivered repo) | ✅ (as a historical/narrative claim, sourced to the repo's own account) |
| A9 | Adversarial pass, deliberately attacking with malformed input rather than clean fixtures, found three real defects: (1) a wrong-typed amount (`"42.50"` string vs. float) crashed Retrieval with `TypeError`; (2) a non-string/`None` query crashed Intake with `AttributeError` on `.lower()`; (3) a non-zero-padded date (`"2026-6-15"`) silently returned `no_matching_record` for a transaction that existed under `"2026-06-15"` | `intake.py:11–30` (docstring naming all three), cross-checked against `tests/test_adversarial_edge_cases.py` | ✅ |
| A10 | The fix adds a strict `YYYY-MM-DD` shape check and a finite/non-bool/non-NaN amount check at Intake, ahead of classification, lookup, or arithmetic; the date failure is named `malformed_date` / `unparseable_date_format`, kept **distinct** from `no_matching_record` — "the date could not be read" and "we checked and nothing happened" are different claims | `intake.py:97–118`; `orchestrator.py:56–69` | ✅ |
| A11 | Negative amounts and infinite amounts are real, finite-or-not-NaN numbers and safely fall through to `record_mismatch` rather than being flagged — confirmed correct behavior, not assumed | `tests/test_adversarial_edge_cases.py::test_negative_amount_is_a_valid_number_and_safely_mismatches`, `::test_infinite_amount_is_a_valid_float_and_safely_mismatches`, executed | ✅ |
| A12 | The floating-point boundary exactly at the matching tolerance (0.01) is checked directly in both directions and confirmed correct | `tests/test_adversarial_edge_cases.py::test_floating_point_boundary_exactly_at_tolerance_still_matches`, `::test_amount_just_outside_tolerance_correctly_mismatches`, executed | ✅ |
| A13 | Eight terminal outcomes exist, each independently reachable: `malformed_query_input`, `unparseable_date_format`, `unclassified_query`, `coaching_out_of_scope`, `incomplete_claim_details`, `no_matching_record`, `record_mismatch`, `answered_directly`/`gate_declined` | `orchestrator.py:42–138`, cross-checked against `tests/test_escalation_reasons.py` (8 test methods, one per outcome) | ✅ |
| A14 | **49 tests, 49 passing, 0 failing, across 7 test files** | independently re-run for this film via `python3 -m unittest discover -s tests -v` — **49 ran, all OK** | ✅ — matches the repo's own README and the case study exactly; not taken on trust |
| A15 | The full suite was re-verified in a clean, empty virtual environment (confirmed via `pip list` to contain nothing but `pip`), separately from the working-directory run | case study §4b, "Sandboxed verification" — historical claim about the original build session, not re-run for this film (this film's own A14 re-run served the same independent-verification purpose against the delivered code) | ✅ |

**Framing note for A8–A10, per `[[real-defects-are-evidence-of-rigor]]`:** these rows
describe a real defect that existed and was fixed — nothing here is softened or hidden.
But the beat these rows feed is about what a deliberate adversarial-testing pass is *for*
and proof that it worked, not a takedown of the original build. A8's "clean first pass" is
scripted as a true, limited claim (evidence about the tests run, not about correctness in
general) — exactly how the case study itself frames its own correction — not as an
embarrassing initial failure.

---

## B. Claims about Lloyds — primary sources via the case study

| # | Claim (as it would be spoken) | Source | Status |
|---|---|---|---|
| B1 | Athena is Lloyds' colleague-facing knowledge assistant, using Retrieval-Augmented Generation grounded to source articles; a human colleague reviews every output before a customer hears it | Lloyds Banking Group, "Group accelerates digital transformation with AI-powered Athena," 15 July 2025; Lloyds Banking Group Engineering, Medium, 24 June 2026 (primary) | ✅ |
| B2 | Athena's search-time figure: average colleague search time fell from 59 seconds to c.20 seconds, a 66% reduction | Lloyds, 15 July 2025 (primary) | ✅ |
| B3 | Athena's usage figures across three dated disclosures: 21,000 colleagues / 2.1 million searches (15 July 2025); 20,000 colleagues, point-in-time (29 January 2026); daily usage exceeds 35,000 colleagues, 66% reaffirmed (24 June 2026) | Lloyds, three dated releases as cited above (primary) | ✅ |
| B4 | The AI HR Assistant discloses one figure — approximately 90% of HR queries resolved correctly on first contact — with no query volume, time period, trend, or methodology | Lloyds Banking Group "2025 Results" news release, 29 January 2026 (primary) | ✅ |
| B5 | The complaints-handling tool performs classification, summarisation, and routing, with **no quantified metric disclosed anywhere in the record** the case study reviewed | Lloyds promotional description; Computing "Ctrl Alt Lead" podcast, 2026 (secondary, functional corroboration only) | ✅ |
| B6 | The customer-facing financial assistant is live to over 500,000 Bank of Scotland customers as of 22 June 2026, and can "refer to expert human support when needed" — with no confidence score, topic restriction, or transaction-value threshold disclosed anywhere that defines "needed" | Lloyds Banking Group, 6 November 2025 launch release; 22 June 2026 update (primary) | ✅ |
| B7 | Unlike Athena, no human reviews the financial assistant's output before the customer hears it — it answers the customer directly, live | case study §3.2, direct contrast with §3.1's Athena description | ✅ |
| B8 | The financial assistant's confirmed results consist entirely of reach (500,000+ customers, 7,000-employee/12,000-trial internal beta), with **zero** disclosed resolution rate, escalation rate, or accuracy metric of any kind | Lloyds, 22 June 2026; Retail Banker International reporting on the 6 November 2025 announcement (primary + secondary) | ✅ |
| B9 | The case study's own stated reason for building its reference implementation around the financial assistant rather than Athena: Athena's human-reviewed design means the undisclosed-mechanism risk "doesn't bite the same way there" | case study §4b, "Why the financial assistant, and not Athena" | ✅ — this is the case study's own reasoning, correctly attributed as such, not this film's independent claim |
| B10 | Four named systems, four different disclosure depths, is the case study's own framing choice — it explicitly declines to merge them into one "Lloyds' AI results" figure | case study §5.8 | ✅ |

---

## C. Not scripted

| Claim | Why not |
|---|---|
| "The Authorization Gate ships with zero default criteria" as the film's central point | Real and confirmed (A3 above) but ruled out as the *thesis* per `work-video/ANGLE.md` — this exact finding is already the stated central claim at Lemonade, Zurich (Week 21), and Capital One (Week 22). It still appears as one stop inside the pipeline half of the film, sourced honestly, not presented as new. |
| Prosper / Merlin / Penny nickname mismatch (case study §6.4) | Real, but a naming-hygiene note, not a mechanism a viewer can test — ruled out in `ANGLE.md` |
| Dr Rohit Dhawan's dual role as Lloyds AI lead and HM Treasury AI Champion (case study §7) | Real and striking, but has no connection to the reference implementation; every work video in this series ties its lesson to a build. At most one closing-note sentence, not a beat. |
| The £50m/£100m+ Group-level GenAI value figures, or the cost-savings/headcount figures | Case study §5.4–5.5 explicitly states these are attributed to "digital and AI initiatives" collectively, not to any single named system — not attributable to the two systems this film is actually about |
| The Evident AI Index ranking (#15, independently corroborated) | A real, independently-verified figure (case study §5.6) but about Lloyds' overall AI programme, not about either system this film's matrix or pipeline covers |
| Any claim that the original 29-test build was "wrong" or "sloppy" | It passed every test it had. The finding is that a clean run only proves what was tested — framed per `[[real-defects-are-evidence-of-rigor]]`, not as a defect in the original work |

---

## Open

1. A8 and A15 are historical claims about an earlier state of the build (before the
   adversarial-pass fixes landed) that no longer exists as a separately runnable version in
   the delivered repository — sourced to the repo's own README and the case study's own
   account, not independently re-executed by this film's own testing. If the film narrates
   the pre-fix behavior on screen (see ANGLE.md's "still to decide" #2), it should be
   framed as reported history, not re-demonstrated as if freshly discovered.
2. B9 is the case study's own editorial reasoning, not an independent finding of this
   film — script it as "the case study explains its own choice as..." rather than as this
   film's own deduction, since it is quoting the source's stated rationale.
