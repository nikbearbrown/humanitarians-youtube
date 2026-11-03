# Week 23 work-video — angle

**Source material:** `13-lloyds-banking-group-agentic-ai-retail-banking-CASE-STUDY.md` and
`lloyds_financial_assistant_pipeline.zip` — the reference implementation of Lloyds'
customer-facing financial assistant: Intake → Retrieval → Authorization Gate, run
fail-fast by a single orchestrator. 7 source files with content, 7 test files, 49 tests.
Independently re-run before writing anything below: **49 passed, 0 failed.**

---

## Survey — every prior work-video angle and structure, so nothing here repeats one

| Week | Company | Film | Teachable claim | Structure |
|---|---|---|---|---|
| 18 | HSBC | *Their Numbers, My Arrows* | one figure carries two different meanings depending on which document cites it | ledger, two columns |
| 19 | DBS | *Where the Record Stops* | label every element CONFIRMED / CONSTRUCTED / BLANK; the rubric is "can this run without a human answering?" | three-category label, recited |
| 20 | Morgan Stanley | *...Drafts One Thing and Files Another* | a source sentence was misread while building, producing a real code error | A/A′ — one card, run twice |
| 21 | Zurich | *The Stages That Stayed Dark* | a test that only checks output can pass while the system did the wrong thing to get there — assert on what a pipeline never reached | five-stage pipeline diagram, lamps light as stages execute, the dark ones carry the lesson |
| 22 | Capital One | *What Had to Be Invented* | for each pipeline stage, ask what a builder would have had to invent, then check whether the artifact confirms it, marks it constructed, or refuses and says so | five-stage interrogation, one question per stage, answered by the file |

Two structural notes those five films establish as already-used territory:
1. **The "gate with zero default criteria" finding itself** is not fresh — it is the
   confirmed mechanism at Lemonade, Zurich (W21), Capital One (W22), and now Lloyds.
   Lloyds' own case study says as much directly (§6.6). A fourth film built around "the
   gate refuses to invent a threshold" would be the least original angle available here,
   not the most defensible one — even though it is the case study's own stated central
   finding.
2. **A single-pipeline, stage-by-stage walk is the default shape of this series.** Three
   of five prior films (19, 21, 22) are built that way. Lloyds' case study offers
   something none of the five source case studies before it did: **four named AI systems
   inside one company, disclosed to four different depths, sitting in the same document.**
   That is a shape this series has not used.

---

## Ruled out

**"The gate has no default criteria" (§6.6, the case study's own headline finding).**
Confirmed real, confirmed present in the code (`gate.py` raises at construction with no
decision function supplied, exactly like Zurich's and Capital One's gates) — and ruled
out for that exact reason. This is W21 and W22's thesis a third time, just at a different
bank.

**"Prosper / Merlin / Penny are not real product names" (§6.4).** A genuine finding —
three of four systems have informal video nicknames that appear nowhere in a press
release — but it is a naming-hygiene note, structurally close to W18's "one figure, two
meanings," just applied to names instead of numbers. No mechanism a viewer can test.

**Dhawan's dual role as Lloyds AI lead and government AI Champion (§7).** The most
narratively striking fact in the case study, and left out anyway: it has no connection to
the reference implementation at all, and every work video in this series so far pairs its
teachable claim to a build a viewer can run. Forcing this into a "work video" would mean
either padding in an unrelated code segment or breaking the series' own format. Worth one
line in the film, not the spine of it.

---

## The angle — ONE COMPANY, FOUR SYSTEMS, FOUR DIFFERENT ANSWERS TO THE SAME QUESTION

Every prior work video studies **one pipeline**. This case study is the first in the
fellow's own run of these to hand over **four named systems from a single company** —
Athena, the AI HR Assistant, the complaints tool, and the customer-facing financial
assistant — each disclosed to a different depth, on two independent axes: **is the
mechanism disclosed**, and **is a human between the output and the customer**. Lay the
four out side by side and a pattern falls out that no single-pipeline film could show:
the system with the *least* disclosed mechanism is also the system with the *least*
disclosed outcome, and it is the one system of the four where a human is not
already reviewing the answer before the customer hears it.

| System | Mechanism disclosed? | Outcome disclosed? | Human reviews before customer hears it? |
|---|---|---|---|
| Athena (colleague-facing) | Yes — named RAG architecture | Yes — three dated figures across 11 months (59s→20s search time, 21k→35k+ users) | Yes, always |
| AI HR Assistant | No | One figure, no elaboration (~90% first-contact) | N/A — internal tool |
| Complaints tool | No | None | N/A — internal tool |
| Financial assistant | No | **None — reach only, zero performance metric** | **No — answers the customer directly, live** |

That table is the film's spine, not a side note. It reframes the question this series
usually asks ("what did this one system's builder have to invent?") into a new one this
case study is uniquely positioned to raise: **why does risk concentrate on exactly the
row with the least paperwork?** — and it's the same company disclosing all four, so nothing
about differing disclosure norms across companies can explain the gap.

### The turn into the build

The reference implementation is built around the financial assistant — the bottom row —
and the case study says why in its own words (§4b): Athena wasn't chosen "for exactly
that reason" a human already reviews it, so the undisclosed-mechanism risk doesn't bite
the same way there. The film follows that same reasoning live: the matrix identifies the
one row where an undisclosed boundary is actually dangerous, and the build targets it.

### What testing for real is supposed to catch — and did

This is where the film earns its ending rather than just describing the matrix, and the
framing here matters: this beat is about what a deliberate adversarial-testing pass is
*for*, not a gotcha about the build. A clean first run (29/29 passing) is evidence about
the tests that were run, not proof of correctness in general — the case study says so
itself. So the pipeline was attacked on purpose, with malformed input rather than clean
fixtures, precisely because the matrix had just flagged this as the one system where
nobody but a test is positioned to catch a wrong answer before a customer hears one.

The attack found what it was built to find. Two inputs crashed outright — loud failures,
caught immediately. One did not crash:

```
claimed date "2026-6-15" (not zero-padded) against a real transaction
stored under "2026-06-15" -> returned no_matching_record
-- a confident answer that nothing happened, when something did.
```

That third case is the one worth a beat, and it's a demonstration of the discipline
working exactly as intended: an unreadable date is not the same claim as a genuine empty
record, so the fix gives it its own name (`malformed_date`, kept apart from
`no_matching_record`) rather than folding a "we don't know" into a "we checked and it's
not there." Regression-tested afterward — independently re-run for this film, 49/49
passing, in a clean sandbox. The finding is what happens when you go looking for the
exact failure mode the matrix predicted would matter, and then fix it before it ships —
that's the process working, not a flaw slipping through.

### Teachable claim

> When one company discloses several AI systems at once, don't average them into one
> verdict. Lay them out on the same two axes — mechanism disclosed, human in the loop —
> and check whether risk concentrates where paperwork is thinnest. It does not have to;
> here, it does.

### Reusable rubric

> For a company with more than one disclosed AI system: build a two-axis table (mechanism
> disclosed / outcome disclosed, human-reviewed / customer-facing) before writing about
> any single one of them. The interesting finding is usually not inside one system's row —
> it's in which row is empty.

Checked against the table at the top of this document: none of the five prior work videos
compares more than one pipeline. This is the first.

---

## Structure — THE MATRIX, FILLING IN LIVE

Four systems named up front. The matrix builds one row at a time, left to right —
mechanism, then outcome, then human-in-loop — instead of being revealed all at once.
Athena's row fills in fast and completely (three dated disclosures give it plenty to
show). Each subsequent row fills in thinner than the last. The financial assistant's row
is the last to fill, and it fills in mostly with the same visual mark repeated: undisclosed,
undisclosed, no.

That's the hinge: the emptiest row is also the one the second half of the film builds a
tested pipeline around, and deliberately attacks with malformed input rather than trusting
a clean first pass. The matrix predicts where to look; the adversarial pass confirms the
prediction was worth making — and shows the fix, not just the finding.

**Arc:** four systems, one company → the matrix, filling in row by row → the pattern (risk
concentrates where the row is emptiest) → why the build targets that row specifically →
the pipeline, and why a clean first run isn't the same as a correct one → the adversarial
pass, attacking on purpose → what the fix actually separates (unreadable date vs.
genuinely nothing) → the rubric, restated as a question a viewer can run on any company
disclosing more than one AI system at once.

Checked against every structure used so far: not W18's two-column ledger, not W19's
recited three-category label, not W20's run-twice A/A′, not W21's single pipeline with
dark lamps, not W22's single pipeline with a question at each stage. A cross-system
matrix that narrows to one pipeline has not been used in this series.

---

## What this leaves out, on purpose

- **The gate's empty-criteria design** still appears — it has to, it's how the Authorization
  Gate is actually built — but as one stop inside the pipeline half of the film, not the
  thesis. One line, sourced to the same case study language already used three times, not
  presented as a fresh discovery.
- **Dhawan's dual role** gets, at most, one sentence near the end as a forward-looking
  note (the case study's own §7 treats it as open, not resolved) — not developed, per the
  ruled-out reasoning above.
- **The naming divergence (Prosper/Merlin/Penny)** is left for `FACTCHECK.md` as a sourcing
  note, not a beat.

## Still to decide

1. Whether Athena's row gets real screen time (its three-disclosure history is the richest
   material in the case study) or is compressed to establish the axis quickly before
   moving to the thinner rows. Current instinct: compress — the film is about the shape of
   the whole matrix, not a fifth retelling of Athena's own good numbers.
2. Whether the malformed-date finding is shown as a live before/after (the pre-fix
   behavior, then the fix) the way W21 showed a live broken pipeline, or narrated once and
   shown only in its corrected, regression-tested state. Precedent exists at W21 for
   showing a before/after on screen; if used here, both sides get equal weight so the beat
   reads as "testing caught this and fixed it," not as dwelling on the before.

Nothing scripted. `FACTCHECK.md` and `BEATS-DRAFT.md` wait on approval or redirection.
