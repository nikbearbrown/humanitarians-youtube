# PEDAGOGY — Watch Retrieval Fix A Stale Answer. (cli-explainer, personal author channel)

`cli-explainer` build (per `skills/make/cli-explainer/SKILL.md`) of the same
source as `claude-liam-rag-introduction`: *RAG Foundations*, Chapter 1
("Introduction: What RAG Is and Why It Exists"). Where that reel was a
vox-style concept explainer (ai-explainer), this one is the **build-with-Claude
loop**: show the prompt, show the ACTUAL code, show the output, then revise.
Tool skin: `claude` (default). Persona/channel: personal author — Kokoro
`am_onyx` ("Onyx"), signed `@VedanshuDaxeshPatel` throughout, same as the
prior reel. IN-FOR-BEAR LAW does not apply (not `claude-liam`/`@NikBearBrown`).

**Tier note.** `cli-explainer` is listed ADVANCED (Bear-only) in this
toolkit's root `CLAUDE.md`, rule 8. Built on the requester's direct,
explicit instruction after that gate was surfaced and acknowledged.

## Required spine (all mandatory elements present — SKILL.md "not optional")

- **B00 INTRO** — `ClaudeComposerAsk`, cold open, ask shown answered (COLD OPEN LAW).
- **B01 PROBLEM** — stakes/context BEFORE the CLI loop, no prompt yet: frozen
  training data vs. a policy that changed after the cutoff.
- **Cycle 1** — B02 CLI (ASK, greeting `"The ask,"`) → B03 CODE (`ClaudeCodeBeat`,
  the REAL `code/naive_answer.py`) → B04 OUTPUT (`CliRunOutput`, REAL captured
  stdout of `python code/naive_answer.py`, verdict stamped `bad`/plain-ink).
- **Cycle 2 = THE REQUIRED REVISION** — B05 CLI (CHANGE, greeting `"The
  revision,"`) → B06 CODE (the REAL `code/rag_answer.py`, diff-framed against
  B03) → B07 OUTPUT (REAL captured stdout of `python code/rag_answer.py`,
  verdict stamped `good`/terracotta).
- **B08 SUMMARY** — one beat, the lesson (reuses `RagExecutiveSummary` from
  the sibling reel, props-only — same mechanism, different framing sentence).
- **B09 NEXT STEPS** — `ClaudeComposerAsk`, greeting `"Your turn."`, prompt
  read aloud and discussed (HANDOFF LAW).
- **B10 OUTRO** — `ClaudeTitleOutro`, exact title restate, `@VedanshuDaxeshPatel`
  handle + byline subline (OUTRO LAW).

## THE ACTUAL-CODE LAW — verified, not asserted

`code/naive_answer.py` and `code/rag_answer.py` in this reel folder are REAL,
runnable, dependency-free Python. Both were executed for real before
authoring the OUTPUT beats; B04/B07's `CliRunOutput.lines` are the VERBATIM
captured stdout, not invented text:

```
$ python code/naive_answer.py
Q: How many sick days do I get this year?
A: You get 10 sick days this year.

$ python code/rag_answer.py
Q: How many sick days do I get this year?
Retrieved: Effective this year, employees receive 15 sick days annually (updated 8 months ago, replacing the previous 10-day allowance).
A: Based on the current policy: Effective this year, employees receive 15 sick days annually (updated 8 months ago, replacing the previous 10-day allowance).
```

The `verdict` annotations (`stale — no source, no way to tell` / `grounded,
current, cited`) are editorial stamps rendered as a visually separate element
from the terminal text — never mixed into the real stdout, so a viewer can't
mistake the script's own output for a judgment it didn't make.

The B02/B05 ASK prompts plausibly generate the B03/B06 code shown, and that
code plausibly produces the B04/B07 output shown — one receipt, per house law.

## Evidence discipline (DOUBLE-CHECK LAW)

Same source claims as the sibling reel (see its SOURCES.md for full
citations: Lewis et al., 2020; Ovadia et al., 2024; Soudani et al., 2024).
This build additionally makes one NEW claim not in the chapter text — that a
model's "reasoning" is unchanged between the two runs and only its input
changed — which is directly verifiable from the two scripts themselves
(same `answer()` shape, only `retrieve()` differs) rather than asserted on
authority.

## Friction protected

- **Kept**: the full revision cycle (B05–B07) — THE REVISION LAW makes this
  non-optional for a 16:9 cut, and it's also the clearest possible
  demonstration of the chapter's central claim (same model, different input).
- **Kept**: verbatim code in both CODE beats, even though `rag_answer.py`
  duplicates the `DOCUMENT_STORE` dict definition — trimming it would break
  THE ACTUAL-CODE LAW's "real source, not paraphrased" requirement.
- **Removed for time**: a third cycle showing what happens with an
  irrelevant question (retrieval returning nothing) — out of scope for this
  chapter's specific worked example; belongs to a failure-modes video instead
  (Chapter 11 territory).

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 states the frozen-vs-current frame before B02–B07)
- WORKED EXAMPLE ✓ (the sick-leave scenario, run for real, twice)
- FALSIFIABILITY ✓ (B04's run is the counterfactual: what the model does
  WITHOUT retrieval, shown as a real, wrong result)
- SCAFFOLDED VIEWER TASK ✓ (B09 hands the viewer the same broken→fixed
  pattern to run on their own document)
- FOUR BOOKENDS ✓ (cold open, problem, summary, handoff+outro)
- NO-SOURCE-NO-VERDICT ✓ (every code claim traces to the real, included scripts)

## VERDICT: PASS

Human requested this build directly, after the ADVANCED-tier gate was
surfaced and explicitly acknowledged. Proceeding to audio (Kokoro, free) and
render.
