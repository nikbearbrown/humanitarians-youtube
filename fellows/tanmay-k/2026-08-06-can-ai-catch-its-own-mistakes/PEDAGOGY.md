# PEDAGOGY — Can AI Catch Its Own Mistakes? I Ran the Experiment

Film 4. **Repo-topic lane** — rebuilt from
`claude-for-artificial-intelligence/nbb-cli-agent-self-verification-failure`
in the `humanitarians-youtube` repo, the same lane that produced the Klarna
"AI Crossroads" reel. Deliberately *not* the work-derived lane (CommBank,
Lemonade); the two are not mixed.

Built to `../../PROOF.md` and `../../PLAYBOOK.md`.

**Status: PHASE 1 — PREMISE. GATE P not signed. Not yet scripted.**

---

## The source draft, and what's wrong with it

The draft's central claim, verbatim from its own `beat_sheet.json` (B01):

> "This is not hallucination — it is a structural failure of self-reference. **A
> system cannot reliably audit its own output** when the output and the audit
> share the same underlying mechanism."

Four defects, all verifiable in the file:

| # | Defect | Evidence |
|---|---|---|
| 1 | States a **structural impossibility** as established fact | B01, quoted above |
| 2 | Contains **no measured number anywhere** — asserts the model "frequently" confirms wrong answers, with no tally | zero rate/percentage strings across all narration |
| 3 | The experiment **cannot run**: it calls `claude-3-5-haiku-20241022`, **retired 19 Feb 2026** | `beat_sheet.json` |
| 4 | Its design **cannot support its conclusion** — two arms (self-verify vs Python evaluator) that both change everything at once | B02–B06 |

Its `PEDAGOGY.md` is four lines: *"NBB wrapper reuses locked body pedagogy.
VERDICT: PASS."* No evidence discipline, no sourcing, signed off anyway.

**This film does not mock the draft.** Defect 4 is a subtle and extremely common
design mistake, and naming it is the teach. Defects 1–3 are the reason a
rebuild is warranted rather than a patch.

## Thesis

The draft asserts that a system cannot reliably audit its own output. **We built
the control it was missing, ran it on current models, and measured nothing.**
Zero misses out of 33 wrong expressions.

But the finding is not "self-verification works." The finding is the **method
that let us know**, and that method is what a viewer walks away able to apply.

**Critically: the draft's advice survives even though its reason does not.**
"Don't let the model be judge and defendant" is sound engineering. "A system
*cannot* reliably audit its own output" is a claim about mechanism, and that is
the part our data contradicts. The film separates them explicitly (B10) — see
*What survives from the draft* below. Landing on "self-checking is fine" would
be a worse outcome than the draft's overclaim: the draft errs toward caution,
that misreading errs toward none.

## The framework — four questions, shown as a structure before any example

Any claim of the form *"the system fails **because** of X"* has to survive four
questions. This is the reusable instrument.

| # | Question | Fails when |
|---|---|---|
| **1** | **What is the claimed cause?** | The claim names a mechanism ("self-reference") rather than describing an observation |
| **2** | **What rival explanation produces the same observation?** | Only one story is on the table |
| **3** | **Is there an arm where *only* the claimed cause varies?** | Every arm changes several things at once |
| **4** | **Will that arm actually collect data?** | A control that never fires is not a control |

Questions 1–2 are cheap and catch most bad claims. **Question 3 is the one
people skip.** Question 4 is the one *we* skipped — see below.

## Why this is a real framework, not a retrofit

PROOF's reverse-engineering tell is categories mapping one-per-example. These
don't: it is **one instrument applied to three different artifacts**, each
failing at a different question, and one of the three is our own work.

| Artifact | Q1 | Q2 | Q3 | Q4 | Verdict |
|---|:--:|:--:|:--:|:--:|---|
| The source draft | ✅ names self-reference | ❌ never names "the task is hard" | ❌ both arms change everything | — | no finding possible |
| **Our revision 1** | ✅ | ✅ | ✅ added the provenance arm | ❌ **n=0 on the key config** | question left unanswered |
| Our revision 2 | ✅ | ✅ | ✅ | ✅ injection guarantees a denominator | measurable |

**Revision 1 is ours and it failed.** We added the control the draft was
missing — and then the models solved the puzzle so reliably that the
`sonnet5-think` arm produced **zero** wrong answers and therefore no data at
all. The arm existed and never fired. That is question 4, discovered the
expensive way, on our own experiment, and it is why the framework has four
questions instead of three.

## The falsifiability case — it fired

**The framework predicted we would measure a blind spot. We measured zero.**

Published work reports a 64.5% average blind-spot rate across 14 open
non-reasoning models (Tsui 2025). We built the clean control and found **no
effect at all** — self-verification caught wrong answers at exactly the same
rate as external presentation. Gap = 0.0 in every configuration.

This is what makes the instrument real rather than decorative: **it is a method
for finding out, not a device for confirming.** A framework that could only ever
return "you need another arm" would be unfalsifiable. What makes this one
falsifiable is that running the arm can kill the hypothesis — and here it did.

## Worked example — the measurement

Task: make 24 from four numbers, each used exactly once. Ground truth is
decidable, so the model's opinion about correctness is never needed.

Each trial produces one wrong expression — either the model's own mistake, or
its correct answer with **one operator corrupted** — and that same expression is
then verified under three framings:

- **A** presented in the assistant turn, as the model's own
- **B** identical expression, fresh conversation, as a third party's submission
- **C** condition A with `"Wait."` prepended (Tsui's one-token remedy)
- **D** exact rational arithmetic in Python — ground truth

**A vs B is the whole experiment.** It is the arm the draft did not have.

| Configuration | n | self | external | wait | **gap** |
|---|---:|---:|---:|---:|---:|
| `haiku-nothink` (thinking off) | 11 | 0% | 0% | 0% | **0.0** |
| `sonnet5-nothink` (thinking explicitly disabled) | 10 | 0% | 0% | 0% | **0.0** |
| `sonnet5-think` (adaptive thinking) | 12 | 0% | 0% | 0% | **0.0** |

**33 wrong expressions. 99 verdicts. Zero misses. Zero unparseable.**

## What the null licenses — and what it does not

This is the beat where the film could most easily overclaim, so the bound is
stated on screen, not buried.

- **Rejects 64.5% overwhelmingly**: P(observing 0/33 if the true rate were
  64.5%) = **1.4 × 10⁻¹⁵**.
- **Does NOT establish zero.** Exact binomial 95% upper bound on the true rate
  is **8.7%** pooled (**11.7%** on the injected-only subset). The film says
  "below about nine percent," never "zero."
- **Does NOT refute Tsui.** That paper measured 14 *open, non-reasoning* models;
  these are frontier Claude models. "Did not reproduce here" is not "the finding
  was wrong." The honest reading is that the effect is **model-dependent**.
- **One task only.** Arithmetic with decidable ground truth is the easiest
  possible case for verification. This says nothing about code review, factual
  claims, or judgment calls — and the film says so.

## What survives from the draft — the B10 beat

The single most important beat in the film, and the reason it is safe to publish
a null at all.

The draft makes two claims that are easy to hear as one:

| The draft's… | Status | Why |
|---|---|---|
| **Practice** — "audit any loop where LLM output verifies LLM output; add a deterministic check, a lookup, or a human at those steps" | **Survives intact** | Nothing we measured argues against it |
| **Mechanism** — "a system *cannot* reliably audit its own output; it is a structural failure of self-reference" | **Contradicted** | 0 misses / 33; provenance made no difference at all |

Three reasons the practice survives our own null, all of them our own numbers:

1. **The ceiling is 8.7%, not zero.** Roughly one in twelve is a bad rate for
   anything consequential.
2. **This was the easiest possible case** — arithmetic, four numbers, decidable
   ground truth. Nothing here transfers to code review, factual claims, or
   judgment.
3. **The external verifier is what made the measurement possible.** We only know
   the rate is low *because* a deterministic Python evaluator sat outside the
   model and graded every answer. Remove it and there is no finding — there is
   just a model saying it checked.

So the correction is not "drop the external check." It is: **keep it, and change
why you keep it.** Not because the model structurally cannot audit itself — it
demonstrably did, 33 times out of 33 — but because *you don't know the rate for
your task until you measure it, and measuring requires the check anyway.*

That reframing is the film's most useful sentence, and it ties the ending back
to the framework: the external verifier is not merely a safety net, it is the
**instrument**.

## Friction — the viewer has to resolve this

We built a careful experiment to measure a published effect and **found
nothing**. Is that a failed experiment or a result?

The viewer is handed that tension before it is resolved. It matters because the
instinctive answer — "the experiment failed, don't publish it" — is exactly the
reflex that leaves unsupported claims like the draft's in circulation
unchallenged.

## Viewer task — a scaffold, not "ask Claude"

Take a causal claim from your own work or reading — *"it fails because X."*
Then:

1. Write the claimed cause in one sentence.
2. Write **one rival explanation** that would produce the identical observation.
3. Describe the arm where **only** the claimed cause differs. If you cannot
   describe it, you do not have a finding — you have an observation.
4. Ask whether that arm would actually collect data. If the failure it needs
   almost never happens, you need to **induce** it, not wait for it.

**Good result:** you find a claim you believed that has no arm behind it.
**Bad result:** every claim passes on first reading — you graded generously.

## Evidence discipline

| Claim | Source | Calibration |
|---|---|---|
| Draft asserts structural impossibility | `nbb-cli-agent-self-verification-failure/beat_sheet.json` B01 | Verbatim quote from the file |
| Draft contains no measured number | Same file, all narration fields | Verified programmatically |
| Draft calls a retired model | Same file: `claude-3-5-haiku-20241022` | Retired **19 Feb 2026** |
| 64.5% blind-spot rate, 14 open non-reasoning models; "Wait" removes 89.3% | Tsui, *Self-Correction Bench*, arXiv:2507.02778 (Jul 2025) | **PREPRINT — not peer-reviewed.** Labelled as such on screen. |
| Intrinsic self-correction fails on reasoning; can degrade accuracy | Huang et al., ICLR 2024, arXiv:2310.01798 | **Peer-reviewed** |
| 0 misses / 33 wrong expressions; gap 0.0 all configs | `../self-verification-experiment/results-20260812T014950Z.json` | **Our own measurement.** Full transcripts in the JSON. |
| 95% upper bound 8.7% pooled | Exact binomial on n=33, 0 events | Computed, reproducible |

**Not claimed anywhere:** that self-verification is reliable in general; that
Tsui is wrong; that this generalizes beyond arithmetic. The film states each
limit out loud.

## Act structure — original to this film

Shares no shape with the previous three: no ASK→RESULT cold open (CommBank), no
J-curve essay spine (Klarna), no scaffold/production interleave (Lemonade). The
shape here is **one instrument applied three times, with a reversal**.

- **B1** Hook — the draft's claim on screen, verbatim, beside the fact that its
  narration contains no number at all
- **B2** Who I am; what I set out to do (reproduce it) — and the map
- **B3** **THE FOUR QUESTIONS** — framework as structure, before any example
- **B4** Application 1: the draft — fails Q2 and Q3
- **B5** Building the missing arm — same expression, different provenance
- **B6** Application 2: **our own revision 1** — passes Q3, fails Q4
- **B7** Application 3: revision 2 — injection guarantees a denominator
- **B8** The result: **zero out of thirty-three**
- **B9** What that licenses — the 8.7% ceiling, stated plainly
- **B10** **The advice was right for the wrong reason** — mechanism contradicted,
  practice intact; the external check is the instrument, not just the safety net
- **B11** Why a null is a result, not a failure
- **B12** Your turn — the four questions as a card
- **B13** Close

Framework lands at B3, ahead of every application. PROOF's constraint —
framework before examples — is met in full.

## Production gate — the legibility contract

Binary; can veto publish regardless of teaching score.

| Beat | Claim | On-screen artifact | Requirement |
|---|---|---|---|
| B1 | The draft asserts impossibility | The verbatim B01 sentence + its file path | Quote and source legible together |
| B1 | It never measures | The narration field with no number in it | Shown, not just asserted |
| B4 | Retired model | `claude-3-5-haiku-20241022` + retirement date | Both in frame |
| B5 | Only provenance varies | Arm A and arm B prompts **side by side**, identical expression highlighted | **Held ≥2s** — this is the beat the film turns on |
| B6 | Our own rev 1 failed | Rev-1 summary showing `n=0` on `sonnet5-think` | Our own defect, on screen |
| B8 | 0 / 33 | The results table from the real JSON | Readable at render size |
| B8 | The model actually reasoned | A verbatim reply computing `8/3 = 2.666…` | Real transcript, not paraphrase |
| B9 | The ceiling | `95% upper bound = 8.7%` | On screen with the 0/33, never separated |
| B10 | Practice survives, mechanism doesn't | The draft's CTA sentence (kept) **beside** its mechanism sentence (struck) | **Both in frame together, held ≥2s** — the split is the beat |
| B10 | The evaluator made the finding possible | Arm D in the pipeline diagram, highlighted | Shown as the instrument, not a footnote |

## Self-scored against the PROOF rubric (pre-build projection)

| Criterion | Score | Basis |
|---|---|---|
| Explicit framework | 2 | Four questions as a structure at B3, before any application |
| Reusable rubric | 2 | Applied on screen to three artifacts (B4, B6, B7) before being handed over at B12 |
| Worked example | 2 | The make-24 measurement traced through all four arms with real values |
| Falsifiability / edge case | 2 | The framework predicted an effect and found none; Q4 was discovered by our own failure |
| Active task | 2 | Four-step scaffold with explicit pass/fail |
| Friction | 2 | "We measured nothing — is that a failure or a result?" posed before resolution |

**Projected 12/12.** A projection, not a grade — re-scored honestly against the
finished cut, and the production gate is separate.

## Persona / register

Repo-topic lane, inherited from the draft: `topic: COMPUTATIONAL SKEPTICISM`,
**Pragmatist** register, `hai` audience. The draft specifies voice `af_kore`,
which **is not installed in this toolkit** — the only Kokoro voices available
are `am_onyx` and `af_bella`. Using **`am_onyx`** ("Onyx"): this film is a
first-person investigation with a reversal rather than a lesson, and wants a
narrator. Note this departs from the lane's Bella precedent, and that the warm
first-person register is kept rather than switching to Teardown — both
deliberate, both recorded in `SCRIPT.md`.

Narration written conversational from the first draft — warm, reacting, human.
Not clipped. The reversal at B8 should land as genuine surprise, because it was.

## Components — PLAYBOOK §2 check pending

No components built yet. **No pattern name goes into `beat_sheet.json` until it
is registered in `Root.tsx`** — an unregistered name is a hard crash that can
leave a stuck lock hanging the next unrelated render.

Likely reusable as-is: `ClaudeComposerAsk`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`. New generic, props-driven components anticipated: a
four-question board, a side-by-side prompt comparator (B5), and a results table.

---

## GATE P

**VERDICT: PASS** — premise reviewed and signed off by the author (2026-08-12).
The teach confirmed at the gate: *name the claimed cause, name the rival, build
the arm where only the cause varies, and check that the arm will actually fire.*
Cleared to script.

**Phase 1 gate question:** the method a viewer walks away able to apply is —
*name the claimed cause, name the rival explanation, build the arm where only
the cause varies, and check that the arm will actually fire.* Is that the
actual teach, or just the topic?
