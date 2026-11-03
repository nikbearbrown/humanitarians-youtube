# FACTCHECK — Week 22 work-video

Two kinds of claim in this film. **Claims about Capital One** resolve to the case study's
primary sources. **Claims about the build** resolve to a file and line, and were verified by
running the code, not by reading it.

No row is scripted without a row here.

---

## A. Claims about the build — verified by execution

| # | Claim | Verified how | Status |
|---|---|---|---|
| A1 | 7 `CONFIRMED`, 10 `CONSTRUCTED`, 15 `[DEV]` markers across the 8 source files that have content (10 files exist; two are empty `__init__.py`) | counted by script over `src/**/*.py` | ✅ |
| A2 | `ValidationGate` raises `TypeError` at construction when no decision function is supplied — "no default acceptance criteria exist or ever will" | `validation_gate.py:34–40`, executed | ✅ |
| A3 | An unrecognised decision-function return raises `ValueError`; "an unrecognized value is never treated as an implicit approval" | `validation_gate.py:56–61` | ✅ |
| A4 | `max_advance_booking_days` is defined in business rules but deliberately not enforced — "documented limitation, not silently ignored" | `validation_gate.py:81–84` | ✅ |
| A5 | `explain.py` has no halt condition, because "no source discloses this step failing, and inventing one here would add a scenario Capital One never described" | `explain.py:5–8` | ✅ |
| A6 | `schedule_handoff` degrades to a fallback CRM record for an unknown vehicle "rather than inventing a halt condition that isn't sourced" — an inline refusal in the executable path, not a docstring | `schedule_handoff.py:41–46` | ✅ |
| A7 | Intake's vehicle vocabulary is deliberately separate from the CRM's inventory, so the two can disagree | `intake.py:16–20, 25` | ✅ |
| A8 | CRM staleness and conflicts are an explicit scope exclusion tied to the case study's §6.5 | `mock_dealer_crm.py:7–11` | ✅ |
| A9 | The three halt reason codes are a fixed enum locked in review Pass 2/5, chosen "rather than free text, so tests assert against stable values" | `docs/DESIGN_DECISIONS.md` §8 | ✅ |
| A10 | The decision function receives the two check outcomes and never the raw plan — contested in review and resolved deliberately | `docs/DESIGN_DECISIONS.md` §5; `validation_gate.py:42–50` | ✅ |
| A11 | **32 tests across six files, all passing** | run with a stdlib harness (`pytest` is not installed; the env was not modified) | ✅ |

**A11 correction.** The README and the case study both stated **27** tests. The suite
actually contains **32** test functions — 3 + 6 + 6 + 5 + 3 + 9. All pass. The README has
been corrected to 32; the case study is a published deliverable and is left for Tanmay to
decide.

---

## B. Claims about Capital One — primary sources via the case study

| # | Claim (as it would be spoken) | Source | Status |
|---|---|---|---|
| B1 | Capital One's tech blog describes Chat Concierge performing four functions via "multiple logical agents" | Capital One tech blog, Mar. 5 2025 (primary) | ✅ |
| B2 | The blog names the validation step's two checks distinctly: "check for hallucinations or errors" and "simulate the execution of the action plan and determine if the outcome conforms to policies and business rules" | same | ✅ |
| B3 | The blog states the explain step "generate[s] and deliver[s] a natural language detailed explanation of the plan to the customer" | same | ✅ |
| B4 | On rejection the evaluator returns the plan to the planning agent for correction "based on its judgement of where the problem was," iteratively | VentureBeat, Jul. 7 2025, Naphade direct quote (secondary, named-executive) | ✅ |
| B5 | What remains undisclosed is narrower: no source states an iteration cap or what happens if the loop fails to converge | case study §3.2 / §6.4 | ✅ |
| B6 | Milind Naphade is **SVP, Technology (AI Foundations)** — not Chief AI Officer | [Capital One's own page](https://www.capitalone.com/tech/machine-learning/milind-naphade-svp-ai-foundations/), corroborated by VentureBeat | ✅ — **README corrected** |

**B6 correction.** The case study's own closing note flagged this as the one outstanding item
before the entry could be closed. It was still open in the repository README; it has now been
fixed there.

---

## C. Not scripted

| Claim | Why not |
|---|---|
| Either "55%" figure | Both are self-reported and unaudited (case study §6.1, §6.2), and the number-collision angle duplicates Week 21's topic video |
| The four-agent breakdown | A secondary-source specification, not Capital One's own stated architecture (§6.3) |
| The single-dealer 10–15% sales figure | One dealer, testimonial, unaudited (§5.3) |
| Anything about the correction loop being "missing" from the build | The loop is confirmed at Capital One and simply outside this pipeline's scope. Saying it is absent without saying it was never in scope would misrepresent the build |

---

## Open

1. B1–B3 are quoted through the case study's transcription of the Capital One blog. The
   blog is a live primary source; if any of those three sentences is narrated verbatim on
   screen, read the blog directly first.
2. The case study still says 27 tests in three places. Tanmay's call — it is the published
   artifact.
