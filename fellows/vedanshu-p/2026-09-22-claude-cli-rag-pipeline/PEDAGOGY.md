# PEDAGOGY — Watch A Bug Name Its Own Stage. (personal-author cli-explainer)

CLI explainer of *RAG Foundations*, Chapter 7 ("The RAG Pipeline End to End").
Built with the **`cli-explainer`** skill — the build-with-Claude loop.

**Tier note.** `cli-explainer` is ADVANCED tier ("Bear only" in CLAUDE.md).
Invoked by explicit human request. It escalates nothing: the whole build runs on
the free path (Kokoro `am_onyx`, Remotion, local numpy, an already-cached model
checkpoint), spends **$0.00**, calls no paid API and makes no network request.

Personal author channel: persona and sign-off are the book's author, Vedanshu
Daxesh Patel (`@VedanshuDaxeshPatel`). IN-FOR-BEAR LAW does not apply — the
narrator is named as themself in B00 and signs off as themself in B11.
Never publishes.

**Book root.** Built into `D:\ai1-cli-main\youtube\` per CLAUDE.md rule 3.
Folder dated **2026-09-22** per explicit instruction.

**Siblings.** Follows the spine set by the Ch. 3, 5 and 6 CLI reels, and shares
chrome (`EmbedChrome`) and beat clock (`ChunkChrome`) with the Ch. 4
ai-explainer — so Chapters 3–7 cut together as one series. `encoder.py` is
carried over from the Ch. 6 build.

## The ONE idea

> Five stages that each hand on exactly one thing are what let a single wrong
> answer be traced back to a single broken stage.

## Why this chapter suits a CLI video

Chapter 7 is the first chapter whose subject is a *whole system*, and its
central claim is unusually testable: it says the five-stage breakdown is
valuable because "a symptom at the output can usually be traced back to exactly
one stage." That is a hypothesis with an experiment attached — build the
pipeline, break one stage at a time, and check whether the symptoms differ.

So this reel does not explain the pipeline diagram. It runs the experiment the
chapter implies, and reports whether the claim survived.

## Act structure (the mandatory CLI spine)

- **B00 INTRO** — `ClaudeComposerAsk`, ask shown answered (COLD OPEN LAW).
- **B01 PROBLEM** — `RagExecutiveSummary`. One symptom, four suspects: a
  finished pipeline emits a single answer, so every cause looks alike.
  Mandatory beat; no code yet.
- **B02 CLI → B03 CODE → B04 OUTPUT** — cycle 1. Five functions, one return
  value each; B04 rebuilds Fig. 01 carrying the measured artifacts.
- **B05 CLI → B06 CODE → B07 OUTPUT** — the revision (THE REVISION LAW).
  B05 states the falsification condition *before* the result: if any two faults
  share a signature, the pipeline is not a diagnostic map.
- **B08 OUTPUT (second result, same run)** — the four answers in their own
  words. The broken retriever's answer is the reel's sharpest moment.
- **B09 SUMMARY** — the lesson, and the generator caveat.
- **B10 NEXT STEPS** — `ClaudeComposerAsk`, `"Your turn."` (HANDOFF LAW).
- **B11 OUTRO** — `TitleOutroChannel`, exact title restate, signature.

## The finding

| stage broken | right fact? | cited | grounded |
|---|---|---|---|
| none (control) | yes | VA-101#0 | yes |
| retrieve | NO | SL-140#0 | yes |
| augment | yes | none | yes |
| generate | NO | none | NO |

Three faults, three distinct signatures — the chapter's claim holds. Each fault
also has a recognisable *character*:

- **retrieve** — fluent, correctly cited, and about the wrong policy. The answer
  *"Employees receive 10 paid sick days per calendar year"* is a good answer to
  a question nobody asked, and it is the failure mode that survives casual
  review.
- **augment** — right fact, no attribution. The system knows the answer and
  cannot tell you where it came from.
- **generate** — a confident number that appears nowhere in the context.

## Evidence discipline (DOUBLE-CHECK LAW) — full detail in SOURCES.md

| Claim | Basis | Verdict |
|---|---|---|
| The pipeline is ingest → embed → retrieve → augment → generate | Ch. 7, explicitly the book's own device | Framed as such on screen; never attributed to the source paper |
| RAG's core is a retriever plus a generator | Lewis et al. (2020) | Cited in B07 |
| Every stage's output is exactly the next stage's input | Ch. 7 | **Demonstrated** — the trace prints each handoff; five single-return functions |
| A symptom traces back to exactly one stage | Ch. 7 | **Tested** — B07, three distinct signatures |
| Retrieval returns the gold chunk plus plausibly-related ones | Ch. 7 ("perhaps…") | **Did not reproduce** — all three hits came from VA-101 itself. B04 reports what happened |

## Friction protected

- **Kept: the generator caveat, at summary length.** The clean four-row table is
  clean *because* the reader is deterministic. B09 spends a third of its
  narration saying so, because the alternative — letting the result imply it
  generalises to a real LLM — is the most misleading move available to this
  reel. The stand-in is presented as a control with a named limitation, not as
  a convenience.
- **Kept: the falsification condition stated before the result.** B05 says what
  would disprove the claim while the outcome is still unknown to the viewer.
  Stating it afterwards would be narration dressed as method.
- **Kept: the retrieval set that didn't match the chapter.** The chapter guesses
  sick-leave and benefits-overview chunks will come back alongside the right
  one; three VA-101 paragraphs came back instead. Reported, not smoothed over.
- **Kept: the distractor documents.** SL-140 and BO-001 exist so the broken
  retriever returns something *plausible*. Without them the retrieval fault
  would have returned obvious nonsense and demonstrated nothing.
- **Dropped: any accuracy number.** One question, four runs. The reel does not
  extrapolate to a hit rate, because it cannot.
- **Dropped: the augment stage's formatting detail.** Chapter 7 defers labelled
  separators to Chapter 8, and so does this reel — the augment fault here is
  label removal, which is the coarsest possible version, left for Ch. 8 to
  refine.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B00/B01 name the five stages and why separation
  matters before any code)
- WORKED EXAMPLE ✓ (the chapter's own question, executed stage by stage)
- FALSIFIABILITY ✓ (B05 states the disproof condition; B07 reports the measured
  signatures)
- SCAFFOLDED VIEWER TASK ✓ (B10 — log three signals per answer, surface the rows
  where they disagree)
- FOUR BOOKENDS ✓ (intro, problem, summary, handoff + outro)
- NO-SOURCE-NO-VERDICT ✓ (every number is captured stdout; every concept cited)

## VERDICT: PASS

Beat sheet, code, and both captured runs reviewed against the chapter before
audio. Proceeding to Kokoro audio → Remotion render → compile at 4K →
frame-level visual QC.
