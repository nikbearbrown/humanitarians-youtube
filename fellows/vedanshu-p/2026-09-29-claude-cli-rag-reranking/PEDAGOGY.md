# PEDAGOGY — Reorder Is Not Retrieve. (personal-author cli-explainer)

CLI explainer of *RAG Foundations*, Chapter 9 ("Re-ranking and Query Rewriting").
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
Folder dated **2026-09-29** per explicit instruction.

**Siblings.** Follows the spine set by the Ch. 3, 5, 6 and 7 CLI reels, and
shares chrome (`EmbedChrome`) and beat clock (`ChunkChrome`) with the Ch. 4 and
Ch. 8 ai-explainers — so Chapters 3–9 cut together as one series. `encoder.py`
is carried from the Ch. 7 build and extended.

## The ONE idea

> A re-ranker reorders the shortlist it was handed. It cannot retrieve. Whatever
> the first pass missed, the second pass never sees — which is why the other
> refinement in this chapter is not an alternative to it but a fix for a
> different failure.

## Why this chapter suits a CLI video

Chapter 9 makes two claims that are cheap to assert and awkward to check: that
re-ranking promotes genuinely better candidates, and that a rewritten query
retrieves better than a literal one. Both are measurable in an afternoon against
a real index — and measuring them turns out to be more interesting than
repeating them, because on this corpus only one of them did anything.

The chapter itself is careful to frame both as refinements *inside* the retrieve
stage rather than new stages (Gao et al.'s pre-retrieval / post-retrieval split).
That framing is what makes the finding land: the two techniques attack different
failures, and knowing which failure you have is the whole decision.

## Act structure (the mandatory CLI spine)

- **B00 INTRO** — `ClaudeComposerAsk`, ask shown answered (COLD OPEN LAW).
- **B01 PROBLEM** — `RagExecutiveSummary`. A bi-encoder computes a document's
  score before the question exists. The speed and the blind spot are one
  decision. Mandatory beat; no code yet.
- **B02 CLI → B03 CODE → B04 OUTPUT → B05 OUTPUT** — cycle 1. The two-stage
  cascade, its measured cost, and then the result, which is a null.
- **B06 CLI → B07 CODE → B08 OUTPUT** — the revision (THE REVISION LAW),
  motivated by B05's measured null rather than by a scripted turn.
- **B09 SUMMARY** — the lesson, and three declared limits.
- **B10 NEXT STEPS** — `ClaudeComposerAsk`, `"Your turn."` (HANDOFF LAW).
- **B11 OUTRO** — `TitleOutroChannel`, exact title restate, signature.

## The finding

| | rescued | promoted | demoted |
|---|---|---|---|
| re-ranking (top-5, 6 questions) | 0 | **0** | **0** |
| query rewriting (same 6) | **1** | 0 | 0 |

Answers present in the top-5: 5/6 → 6/6 after rewriting.

The re-ranker was not idle — on the question shown in B05 it visibly reordered
the shortlist. It reordered five documents, none of which answer the question,
because the one that does was never retrieved. That is the ceiling: **stage 2
only ever sees what stage 1 sent.**

## Friction protected

- **Kept: the null result, as the finding.** Re-ranking moved nothing here. The
  reel reports that rather than hunting for a corpus where it would shine. The
  temptation to engineer one was real and is named in SOURCES.md.
- **Kept: the stand-in declaration, at summary length.** Stage 2 is late
  interaction, not a cross-encoder — the mechanism the chapter is actually
  about. B04's caption says so and B09 spends a clause on it, because letting a
  null result imply "cross-encoders don't help" would be the most misleading
  thing this reel could do.
- **Kept: the rewrites are mine, not a model's.** Both of the chapter's named
  methods need an LLM this machine does not have. The caveat lives in the source
  file shown in B07, so the viewer reads it rather than only hearing it.
- **Kept: the chunking artifact.** The first splitter made document titles their
  own chunks and a heading outranked a policy. Found, fixed, and logged, because
  it changed the numbers.
- **Kept: six questions is small.** B09 says so out loud.
- **Dropped: the 27% figure.** Nogueira & Cho measured a BERT cross-encoder on
  MS MARCO. This reel ran neither that model nor that benchmark, so the number
  appears nowhere on screen. Borrowing it would have been the easiest way to
  make the beat feel authoritative and the fastest way to mislead.
- **Dropped: HyDE as a demo.** Named in narration, not run — it needs a
  generative model. Claiming otherwise would be fabrication.

## Evidence discipline (DOUBLE-CHECK LAW) — full detail in SOURCES.md

| Claim | Basis | Verdict |
|---|---|---|
| A bi-encoder's document vector does not depend on the query | Ch. 9; Reimers & Gurevych, 2019 | **Proven** — `prove_query_independence` returns 0.00e+00 |
| Re-ranking is too expensive to run over a whole corpus | Ch. 9 | **Measured** — 86 ms/pair; 23.8 h per query over 1M chunks (arithmetic on the measured time, labelled as such) |
| A cross-encoder promotes genuinely better candidates | Nogueira & Cho, 2019 | **Not tested** — no cross-encoder available; stand-in declared |
| A rewritten query retrieves better | Ch. 9; Ma et al., 2023 | **Tested** — 1 rescue, 0 losses, on hand-written rewrites |
| Both refinements sit inside the retrieve stage | Gao et al., 2023/2024 | Framed as the survey's categorisation, cited on screen |

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 establishes the query-independent score
  before any code)
- WORKED EXAMPLE ✓ (one shortlist walked end to end in B05)
- FALSIFIABILITY ✓ (twice — a check that could have failed, and a reported null)
- SCAFFOLDED VIEWER TASK ✓ (B10 — split your own failures into "ranked low" vs
  "missing entirely", the diagnostic that decides whether re-ranking helps you)
- FOUR BOOKENDS ✓
- NO-SOURCE-NO-VERDICT ✓ (every number is captured stdout; every concept cited)

## VERDICT: PASS

Beat sheet, code and all three captured runs reviewed against the chapter before
audio. Proceeding to Kokoro audio → Remotion render → compile at 4K →
frame-level visual QC.
