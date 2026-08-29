# PEDAGOGY — Watch The Obvious Fix Fail. (cli-explainer, personal author channel)

`cli-explainer` build (per `skills/make/cli-explainer/SKILL.md`) of *RAG
Foundations*, Chapter 2 ("The Problem: Why LLMs Alone Aren't Enough") — the
same source as the sibling ai-explainer reel
`2026-08-18-claude-rag-the-problem`. Where that reel was a vox-style concept
explainer, this one is the **build-with-Claude loop**: show the prompt, show
the ACTUAL code, show the output, then revise. Tool skin: `claude` (default).
Persona/channel: personal author — Kokoro `am_onyx` ("Onyx"), signed
`@VedanshuDaxeshPatel` throughout. IN-FOR-BEAR LAW does not apply.

**Tier note.** `cli-explainer` is listed ADVANCED (Bear-only) in this
toolkit's root `CLAUDE.md`, rule 8. Built on the requester's direct, explicit
instruction: the gate was surfaced, and the requester confirmed proceeding on
the strength of the existing sibling reel (`claude-cli-rag-introduction`,
same book) as precedent that this book's cli-explainer builds are already
covered — not a claim of being Bear.

## Required spine (all mandatory elements present — SKILL.md "not optional")

- **B00 INTRO** — `ClaudeComposerAsk`, cold open, ask shown answered (COLD OPEN LAW).
- **B01 PROBLEM** — stakes/context BEFORE the CLI loop, no prompt yet: a
  fixed-snapshot assistant can only hallucinate or go stale; the "obvious"
  fix (paste everything in) sounds sufficient and isn't.
- **Cycle 1** — B02 CLI (ASK, greeting `"The ask,"`) → B03 CODE (`ClaudeCodeBeat`,
  the REAL `code/naive_assistant.py`) → B04 OUTPUT (`CliRunOutput`, REAL
  captured stdout of `python code/naive_assistant.py`, verdict stamped `bad`).
- **Cycle 2 = THE REQUIRED REVISION** — B05 CLI (CHANGE, greeting `"The
  revision,"`) → B06 CODE (the REAL `code/naive_bigcontext.py`, diff-framed
  against B03) → B07 OUTPUT (REAL captured stdout of
  `python code/naive_bigcontext.py`, verdict stamped `bad` — see Honesty below).
- **B08 SUMMARY** — one beat, the lesson (reuses `RagExecutiveSummary` from
  the sibling reels, props-only — same mechanism, different framing sentence).
- **B09 NEXT STEPS** — `ClaudeComposerAsk`, greeting `"Your turn."`, prompt
  read aloud and discussed (HANDOFF LAW).
- **B10 OUTRO** — `ClaudeTitleOutro`, exact title restate, `@VedanshuDaxeshPatel`
  handle + byline subline (OUTRO LAW).

## Honesty note — both cycles end "bad," on purpose

The Chapter-1 cli-explainer sibling demonstrates retrieval FIXING a stale
answer (that chapter introduces RAG as the resolution). Chapter 2 introduces
no fix — it only names the three failures and argues that a bigger context
window doesn't solve them, then bridges to Chapter 3. Following that
faithfully: B04 (hardcoded dict) fails two ways, and B07 (the "obvious fix"
of pasting the whole manual in) fails a THIRD way (wrong paragraph, buried in
the middle) rather than succeeding. Stamping B07 `good` would overclaim a
resolution the source text doesn't give — a NO-SOURCE-NO-VERDICT violation.
Both stay `bad`, and B08's lesson names what would actually have to change
(deciding WHICH passage matters) without asserting how — that's left for the
book's own Chapter 3.

## THE ACTUAL-CODE LAW — verified, not asserted

`code/naive_assistant.py` and `code/naive_bigcontext.py` in this reel folder
are REAL, runnable, dependency-free Python. Both were executed for real
before authoring the OUTPUT beats; B04/B07's `CliRunOutput.lines` are the
VERBATIM captured stdout, not invented text:

```
$ python code/naive_assistant.py
Q: How many weeks of parental leave do I get?
A: You get 8 weeks of parental leave.

Q: What's the wellness stipend policy?
A: You get 12 wellness days a year, plus a $500 stipend.

$ python code/naive_bigcontext.py
Q: How many weeks of parental leave do I get?
A: Vacation policy: employees accrue 15 vacation days annually. Requests for leave should be submitted two weeks in advance.
```

The `verdict` annotations are editorial stamps rendered as a visually
separate element from the terminal text — never mixed into the real stdout.

The B02/B05 ASK prompts plausibly generate the B03/B06 code shown, and that
code plausibly produces the B04/B07 output shown — one receipt, per house law.

## Evidence discipline (DOUBLE-CHECK LAW)

Same source claims as the sibling ai-explainer reel (see its `SOURCES.md` for
full citations: Ji et al. 2023, Huang et al. 2023, Shuster et al. 2021,
OpenAI 2023, Liu et al. 2024). This build's only new claim — that a naive,
unranked keyword scan over a fully-pasted document returns the first
matching paragraph regardless of relevance — is directly verifiable by
reading `naive_bigcontext.py`'s thirteen lines, and was confirmed by actually
running it (see `SOURCES.md`), not asserted on authority.

## Friction protected

- **Kept**: the full revision cycle (B05–B07) — THE REVISION LAW makes this
  non-optional for a 16:9 cut, and it's also the clearest demonstration of
  the chapter's central claim (a bigger window is necessary for some fixes,
  useless for others).
- **Kept**: both OUTPUT beats stamped `bad` — see Honesty note above.
- **Removed for time**: a third cycle demonstrating hallucination surviving
  even after the big-context fix (asking about a benefit truly absent from
  MANUAL) — the two-failure worked example already carries the lesson;
  belongs to a failure-modes-deep-dive video instead (Chapter 11 territory).

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 states the two-then-three-failure frame before B02–B07)
- WORKED EXAMPLE ✓ (the parental-leave/wellness scenario, run for real, twice)
- FALSIFIABILITY ✓ (B07's run is the counterfactual: what "just paste more
  in" actually does, shown as a real, wrong result — not asserted, run)
- SCAFFOLDED VIEWER TASK ✓ (B09 hands the viewer the same two-failure lens
  to run on their own document)
- FOUR BOOKENDS ✓ (cold open, problem, summary, handoff+outro)
- NO-SOURCE-NO-VERDICT ✓ (every code claim traces to the real, included
  scripts; no fix is claimed that the chapter doesn't give)

## VERDICT: PASS

Approved 2026-08-18 — Vedanshu Daxesh Patel reviewed `beat_sheet.json` and
this document and signed off. Proceeding to Part B (Kokoro audio → render →
compile at 4K → visual QC).