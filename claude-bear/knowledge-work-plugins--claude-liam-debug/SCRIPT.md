# SCRIPT.md — Reproduce First, Fix Last. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-debug` (Teardown, walks the Anthropic `debug` engineering
Skill — a structured debugging session) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed "fix my code" and "debug it" meant the same thing to Claude.
They don't — debug runs a structured session first. So: can I just ask
Claude to debug this broken code right now?

*(Text typed on screen: "Can I just ask / Claude to fix / this broken code /
right now?" — trigger word "fix" corrects to "debug", landing on: "Can I
just ask Claude to debug this broken code right now?" Params reused from the
`claude-plugins-official--claude-liam-agent-development` sibling, already
proven to clear the TIMING LAW floor: charMs 42, mistakeRate 4%,
hesitateWithin 2%, hesitateBetween 8%, lead_silence_s 1.0.)*

## Body — anatomy, the four-step order, the limit

**NB01 — One file, one job** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is debug. Its
SKILL.md spells out one job: run a structured debugging session —
reproduce, isolate, diagnose, then fix. Four steps, always in that order.

**NB02 — What starts the session** (source B02, pipeline — re-scoped to the
debug-specific trigger conditions rather than the generic read/execute/return
pipeline, since the trigger list is the concrete, skill-specific fact a
general viewer can actually use)
Claude runs this session when it recognizes one of a few situations: an
error message or a stack trace, "this works in staging but not in
production," "something broke after the deploy," or behavior that diverges
from what's expected and the cause isn't obvious. Any one of those starts
it. Nothing else does.

**NB03 — Repeatable, not universal** (source B03 design tell + BVDT verdict,
Teardown stripped of judgment and merged — both-directions law)
Run it twice on the same problem and you get the same four steps in the
same order — reproduce, isolate, diagnose, fix — never skipped, never
reordered. That's the guarantee. But the guarantee only starts once your
problem matches one of those triggers. Describe something outside that
list, and the skill has nothing to say about it.

## Close

**BCRY — carry-out**
Debug never jumps straight to a fix. It runs reproduce, isolate, diagnose,
then fix — the same order every time, but only for the kinds of breakage
it's built to recognize.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a feature that works in staging
but breaks in production, and I don't know why. Read the debug skill and
walk me through what you will do — in order — before you start. Watch
whether it reproduces the problem first, or jumps straight to guessing a fix.

**BOUT — outro**
Reproduce First, Fix Last. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a one-shot-fix assumption — does asking Claude to "debug" just mean asking it to "fix"? |
| Wrong guess | B00 (WRITER LAW) | "fix" corrected to "debug" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the four-step order (reproduce, isolate, diagnose, fix) and the concrete trigger conditions that start a session |
| Anchor | the debug skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 + BCRY | NB03 states the guarantee (same order, every run) and the limit (nothing outside the trigger list) together; BCRY restates both in one carry-out sentence — matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `debug` Skill's SKILL.md specifies (the four-step order, the trigger
conditions, same-input/same-output repeatability, and the scope limit) — not
an inference about hidden model internals. Per simple's ONE-FLAG LAW, when
the source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 kept as anatomy; B02→NB02 re-scoped
from the generic "read → execute → return" pipeline description to the
debug-specific trigger conditions the source's own B00/BHTF narration
already named (error/stack trace, staging-vs-prod, post-deploy break,
unexplained divergence) — a more concrete, skill-specific fact than
restating the generic pipeline every skill-teardown episode in this family
already covers; B03's "gets it right / where it bites" Teardown framing and
BVDT's verdict facts (same input → same output every run; limit: only what
the file specifies) are merged into NB03, stripped of Teardown judgment
language per the NO JUDGMENT register check, and stated as a plain
mechanism-and-limit description; BHTF kept as the your-turn handoff, built
from the source's own generic template ("I want to [use case]. Read the
debug skill and walk me through what you will do before you do it.") filled
with one of the source's own listed triggers ("works in staging but not
prod") so the prompt is concrete and paste-ready rather than a fill-in-the-
blank; BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
