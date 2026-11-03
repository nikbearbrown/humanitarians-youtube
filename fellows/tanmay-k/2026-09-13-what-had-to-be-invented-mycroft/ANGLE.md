# Week 22 work-video — angle

**Source material:** `12-capitalone-agentic-ai-auto-finance-CASE-STUDY.md` and
`chat-concierge-pipeline/` — the reference implementation of Capital One's Chat Concierge:
intake → plan → validation gate → explain → schedule handoff. 8 source files with content,
6 test files, 11 logged design decisions.

---

## Correction — my first angle was wrong on the facts

I proposed a film about the validation gate "discarding its diagnosis" and called it a
defect class. **That reading was incorrect, and I should not have written it down before
reading `docs/DESIGN_DECISIONS.md`.**

What the log actually records:

- **Decision 8** — the three reason codes (`unparseable_request`,
  `infeasible_against_business_rules`, `not_validated`) are a **fixed enum, locked in review
  Pass 2 and Pass 5**, chosen deliberately *"rather than free text, so tests assert against
  stable values, not prose that might be reworded later."* It closes an ambiguous-return
  gap that had caused problems in earlier entries. `not_validated` is a contract value, not
  a missing explanation.
- **Decision 5** — the decision function receives the two check outcomes and never the raw
  plan. This was **contested during review and resolved on purpose**, because passing the
  plan would let a decision function weigh plan content over check results. The check
  details are not destroyed; they are routed to the component the design says owns the
  decision.
- The three tests asserting `reason == "not_validated"` are not ratifying a loss. They are
  doing exactly what Decision 8 asks of them.

So there was no defect. I read past `CONSTRUCTED / DELIBERATELY ABSENT` in the gate's own
docstring and past an eleven-item decision log, and asserted more than the source said.

Recording it here because the corrected reading is what the film is actually about.

---

## The angle

**This build refuses to invent, and it marks every place where it refused.**

The organising discipline of the implementation is not a feature of any one module. It is
that the code states, in the file, which parts come from Capital One and which are the
builder's construction — and where the public record stops, the code stops rather than
filling the gap with something plausible.

Counted by script, not by eye: **7 `CONFIRMED`, 10 `CONSTRUCTED` and 15 `[DEV]` markers
across the 8 source files that have content** (10 exist; two are empty `__init__.py`), plus
an 11-entry decision log tying each choice to the review pass that settled it.

Concrete instances:

| Where | What it does |
|---|---|
| `ValidationGate.__init__` | raises if no decision function is supplied — no default acceptance criteria exist "or ever will" |
| `explain.py` | has **no halt condition**, because no source describes this step failing, and "inventing one here would add a scenario Capital One never described" |
| `_check_policy_conformance` | `max_advance_booking_days` is defined but **not enforced** — logged as a documented limitation rather than silently ignored |
| Decision 9 | a gap surfaced only once the code had to run; logged rather than quietly patched |
| Gate naming | `validated` / `not_validated` departs from the series default, grounded in Capital One's own verb "validate that plan" — and the departure is logged |

The material is built from publicly available sources, and the build's response to the
limits of that record is to **name them in place** rather than paper over them. That is the
unusual thing worth a film: most reference implementations invent the missing parts
silently, and a reader six months later cannot tell which parts were real.

---

## Why this is new for the series

| Week | Film | What it was about |
|---|---|---|
| 20 | *Morgan Stanley's AI Drafts One Thing and Files Another* | a source sentence misread while building |
| 21 | *The Stages That Stayed Dark* | tests passing while stages never executed |
| 21 topic | *The Cell Next Door* | the same digits meaning two different quantities |
| 22 topic | *Three Witnesses to Two Per Second* | a qualifier dropped in the retelling |
| **22 work** | **this** | **how a build behaves at the edge of its evidence** |

The four previous films are all about something going wrong. This one is not about an error
at all — it is about a method, shown working, with its costs stated. That is a different
kind of film for the series, not just a different subject.

---

## Ruled out before choosing

**§6.2 — "two 55% figures that share a number, not a meaning."** The case study's most
quotable finding, and disqualified: it is almost exactly Week 21's topic video, where the
same trial reports *38.7 percent* and *38.7 months* a few lines apart. Same shape, eleven
weeks apart.

**§6.3 — the four-agent count is a secondary-source specification.** Too close to this
week's topic video, which is entirely about a claim travelling past what its source said.

**§6.6 — two products sharing a naming family.** Real, but a naming-hygiene note without a
mechanism a viewer can test.

---

## Proposed structure — WHAT WOULD YOU HAVE HAD TO INVENT?

Not a narrative ladder and not a comparison. The film walks the pipeline and asks one
question at each stage: **to ship this, what would a builder have had to make up?** Then it
shows what this build did instead — confirmed it, marked it as constructed, or refused and
said so in the file.

### Verified line by line against the code

Every row below was checked against the file it cites. Counted by script, not by eye:
**7 `CONFIRMED`, 10 `CONSTRUCTED` and 15 `[DEV]` markers across 8 files with content.**

| Stage | What a builder would have had to invent | What this build did | Where |
|---|---|---|---|
| intake | what counts as a complete request | CONSTRUCTED, marked — parsing logic, completeness criteria *and* object shape all named as the repo's own invention, "no source discloses a request schema" | `intake.py:10–14` |
| intake | which vehicles the system recognises | `[DEV]` fabricated vocabulary, deliberately **not** the CRM's inventory, so the two can legitimately disagree | `intake.py:16–20, 25` |
| plan | what makes a slot infeasible | CONSTRUCTED, marked — plan shape and the feasibility check | `plan.py:15–19` |
| validation gate | what counts as good enough to approve | **REFUSED** — "zero built-in acceptance criteria: no confidence threshold, no dollar amount, no approval default of any kind"; raises at construction | `validation_gate.py:5–8, 34–40` |
| validation gate | whether an unrecognised decision means yes | **REFUSED** — raises; "an unrecognized value is never treated as an implicit approval" | `validation_gate.py:56–61` |
| validation gate | enforcing `max_advance_booking_days` | **NOT ENFORCED, AND SAID SO** — "documented limitation, not silently ignored" | `validation_gate.py:81–84` |
| explain | what happens when this step fails | **REFUSED** — no halt condition, because "no source discloses this step failing, and inventing one here would add a scenario Capital One never described" | `explain.py:5–8` |
| schedule handoff | what happens when the vehicle is not in the CRM | **REFUSED INLINE** — degrades gracefully "rather than inventing a halt condition that isn't sourced" | `schedule_handoff.py:41–46` |
| mock CRM | stale or conflicting dealer data | **EXCLUDED ON PURPOSE**, tied to the case study's own §6.5 | `mock_dealer_crm.py:7–11` |

### What the verification changed

Four of my five original rows held. **Row five was wrong** — I had written the schedule-handoff
question as "what does the CRM actually return?", which describes the stub generically and
misses the better thing sitting three lines lower.

The real refusal there is **inline, in the function body, at the exact line where inventing
is most tempting**: a vehicle mention arrives with no matching CRM record, and instead of
adding a halt the code degrades and says in a comment why it will not invent one. Every
other refusal in this build is in a module docstring, where a reader expects hedging. That
one is in the executable path.

It also pairs with row two: intake's vocabulary is deliberately separate from the CRM's
inventory, so a request *can* name a vehicle the CRM does not stock. The build creates that
possibility knowingly and then declines to invent a failure mode for it. Those two rows are
one idea and should probably be one beat.

### The shape

Five stages, one question each, answered by the file. The viewer leaves with a move they can
run on any reference implementation or any vendor system description: for each component,
ask what had to be invented to make it runnable — and check whether the artifact tells you.

The honest cost gets its own beat: a pipeline that refuses to invent hands the caller a halt
they cannot act on without supplying the missing policy themselves. That is a real trade,
stated as a trade.

Checked against every structure used so far: not Week 21's concentric ladder, not this
week's three-witness cross-examination, not Week 20's misread-clause-then-test, not Week
21's move-one-line. A stage-by-stage interrogation of a build's own boundaries has not been
used in this series.

---

## Open before scripting

1. ~~Verify each row of the stage table~~ — **done**, see above. Row five was corrected and
   four new rows were found.
2. Decide whether the honest-cost beat sits in the middle or at the end. At the end it reads
   as a caveat; in the middle it reads as part of the method.
3. The case study's §3.2 correction loop is confirmed but **not implemented** in this
   pipeline. That is a scope boundary, not a gap — confirm how the build documents it before
   the film says anything about it.
