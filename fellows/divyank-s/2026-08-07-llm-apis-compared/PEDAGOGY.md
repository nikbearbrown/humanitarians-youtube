# PEDAGOGY — Claude, Compared. (deep-explainer, claude-liam)

No book chapter — a research-centric comparison of the four major LLM
APIs (OpenAI, Anthropic, Meta, Google), built per the human's explicit
request: compare cost, context window, use case, and open-source vs.
proprietary, plus additional axes volunteered from research (deployment
model, and the 2026 open/closed licensing shift).

## Spine check

- B00 cold open, signed for Divyank from the start ✓
- 4 acts × (1 `FluencySegmentCard` + 6 content beats) = 28 body beats:
  I cost (official per-token pricing, all four), II context window (the
  ~1M-token convergence + what still varies), III use case (each
  company's real specialization), IV open vs. proprietary (the old
  clean split vs. the messier 2026 reality) ✓
- VERDICT → HANDOFF ("Your turn.") → title-restate OUTRO ✓

## Research discipline (no book chapter to anchor this one)

Every pricing/spec number was researched live this session, never
recalled from training data — this is the explicit trigger case for
loading the `claude-api` skill before writing anything about Anthropic's
own API, which this build did first. For OpenAI, Google, and Meta, an
initial WebSearch pass returned third-party pricing aggregators with
**mutually conflicting numbers for the same models** — those were
explicitly rejected as sources, and every number actually used was
re-verified directly against each vendor's own official pricing/docs
page via WebFetch. See `FACTCHECK.md` for the full per-claim sourcing
and the rejected sources.

## Beat-mix contract

28 body beats — VOX 5/28 = **17.9%** (inside 15–30%), REMOTION 19/28 =
67.9% (absorbing the MANIM share, no Manim on this machine), CARD 4/28.

## Portrait (9:16 Short) plan, decided up front

`BinaryBranch`/`DivergentFates` assigned to A1-5, A2-4, A3-5, A4-4 — one
hero beat per act. Expect `shorts.py`'s auto cap-check to still require
a manual `--drop` override, the auto-rewritten `BOUT` outro to need a
hand rewrite, and `--handle @DivyankSingh` to be passed explicitly when
deriving the Short.

## Honesty discipline

Every pricing claim is explicitly tagged **current as of October 2026**
in `FACTCHECK.md` — pricing is this session's most perishable claim
category, more so than any chapter-sourced build this session, since
there is no stable published-book text anchoring it. OpenAI's specific
current model names are used only in on-screen chip labels, not spoken
in narration, since this session verified the pricing/context figures
directly but could not independently confirm naming stability beyond
the one page fetched. No rumored/unconfirmed model (e.g. speculative
next-gen releases debated across conflicting sources) is asserted as
fact. See `FACTCHECK.md`.

## Time-limit expectation

Estimate: 513s (8.55 min) — inside the 5–10 min band with margin.

## Status

**VERDICT: PASS** — signed off by the human (Divyank Singh,
singh.divya@northeastern.edu) in chat, 2026-10-13, on review of this
PEDAGOGY.md, FACTCHECK.md, and the beat sheet's narration.
