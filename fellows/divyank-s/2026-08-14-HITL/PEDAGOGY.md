# PEDAGOGY — Claude, Reviewed. (deep-explainer, claude-liam)

No book chapter — a general research-centric comparison/explainer on LLM
evaluation through human-in-the-loop review, built per the human's
explicit request. Thesis: a model should never grade its own output; the
grading ladder runs from cheap programmatic checks to human spot-checks;
humans sit at two real, specific gates (the input set, the grading
method) rather than reviewing every case forever; and an automated
grader only earns the right to run unsupervised through calibration
against human judgment, rechecked as conditions shift.

## Spine check

- B00 cold open, signed for Divyank from the start ✓
- 4 acts × (1 `FluencySegmentCard` + 6 content beats) = 28 body beats:
  I why a model can't fully grade itself (the grading ladder, judge
  gaming, never self-grade), II where humans sit in the loop (the two
  sign-off gates, RLHF, disagreement as data), III where human attention
  actually gets spent (triage sampling, not blanket review), IV
  calibration as the real deliverable (earning the right to run alone,
  the two honest failure modes, recalibration) ✓
- VERDICT → HANDOFF ("Your turn.") → title-restate OUTRO ✓

## Research discipline (no book chapter to anchor this one)

Because the task names Claude/Anthropic and is explicitly LLM-judge-
shaped, the `claude-api` skill's trigger condition fired and the skill
was loaded before any content was written. Its `shared/evals/build-eval.md`
guide — read directly this session — grounds every Claude-specific/
current claim: the four-rung grading ladder, the explicit rule against
using the model under test as its own judge, and the two mandatory
sign-off gates (input set, grading method). General human-in-the-loop
industry concepts beyond that guide's scope (RLHF, inter-annotator
disagreement, triage sampling) are stated at the level of stable,
well-documented mechanism — no specific paper's numbers, no benchmark
percentages. See `FACTCHECK.md`.

## Beat-mix contract

28 body beats — VOX 4/28 = **14.3%** (slightly under the usual 15–30%
band — see `SOURCES.md` for why a weak fifth image wasn't forced in),
REMOTION 20/28 = 71.4% (absorbing the MANIM share, no Manim on this
machine), CARD 4/28.

## Portrait (9:16 Short) plan, decided up front

`BinaryBranch`/`DivergentFates` assigned to A1-5, A2-4, A3-4, A4-4 — one
hero beat per act. Expect `shorts.py`'s auto cap-check to need a manual
`--drop` override, the auto-rewritten `BOUT` outro to need a hand
rewrite, and `--handle @DivyankSingh` to be passed explicitly when
deriving the Short.

## Honesty discipline

Every claim about current Claude-API-ecosystem practice (the grading
ladder, the self-grading rule, the sign-off gates) is tied directly to
the `build-eval.md` guide read this session, not recalled from training
data. General industry concepts (RLHF, annotator disagreement, triage
sampling) are kept qualitative and unattributed to any specific paper or
company. See `FACTCHECK.md`.

## Time-limit expectation

Estimate: 501s (8.35 min) — inside the 5–10 min band with margin.

## Status

**VERDICT: PASS** — signed off by the human (Divyank Singh,
singh.divya@northeastern.edu) in chat, 2026-10-17, on review of this
PEDAGOGY.md, FACTCHECK.md, and the beat sheet's narration.
