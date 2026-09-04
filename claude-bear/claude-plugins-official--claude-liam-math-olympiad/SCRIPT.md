# SCRIPT.md — The Verifier Never Sees Your Thinking. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-math-olympiad` (Teardown, walks the Anthropic
math-olympiad Claude Code Skill) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed showing the checker everything would help it decide. It's
the opposite — the checker only ever sees the finished proof. So: if you
show it just the proof, does that work?

*(Text typed on screen: "If I show the checker / everything, / does that
/ work?" — trigger word "everything" corrects to "just the proof",
landing on: "If I show the checker just the proof, does that work?")*

## Body — how the proof gets made, then checked blind

**NB01 — Read twice, then solve many ways** (source B01, anatomy —
interpretation check + parallel solving half)
Before solving anything, Claude checks how the problem could be read —
competition problems often bury an easy reading next to the hard one, and
in past runs most errors came from solving the wrong reading entirely.
Once the intended reading is settled, eight to twelve solvers tackle it in
parallel. Each one iterates on its own — solve, self-check, revise — up to
five rounds, with no calculator and no code, reasoning only.

**NB02 — Hide the reasoning, then attack the proof** (source B01, anatomy —
verification half; source B02, asymmetric vote detail)
Before any proof reaches a verifier, everything except the finished
argument is deleted — every false start, every scratch note. A verifier
that saw the reasoning tends to agree with it, right or wrong; a verifier
that sees only the clean proof has nothing to agree with except the logic
itself. Fresh verifiers then attack the proof against a checklist of known
mistakes, and the vote is asymmetric: four clean checks confirm it, but
just two flagged holes are enough to send it back.

**NB03 — Why hiding it matters** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's why that matters. A verifier that reads a full page of confident
reasoning starts nodding along before it reaches the last line — that's
what happens when the reasoning stays visible. Show it only the bare proof
instead, and it has to find the gap on its own, which is exactly when the
pattern checklist catches something a nodding-along verifier would have
waved through.

## Close

**BCRY — carry-out**
Claude checks a competition proof only after hiding the reasoning that
built it — from a verifier that can't agree with logic it's never seen,
and would rather say no confident solution than guess.

**BHTF — your turn**
Your turn. Paste this into Claude: Give me a tricky proof for a claim of
your choosing, but write it in two passes. First, work out the reasoning
however you like. Then hand me only the finished proof, with none of that
reasoning attached, and check it fresh, as if you'd never seen how it was
built. Tell me if the two passes agree.

**BOUT — outro**
The Verifier Never Sees Your Thinking. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a verification question — does showing the checker everything help it decide? |
| Wrong guess | B00 (WRITER LAW) | "everything" corrected to "just the proof" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | interpretation check before solving, eight-to-twelve parallel solvers with internal self-check/revise, no computation; then the thinking trace is stripped before any verifier sees the proof, pattern-armed adversarial attack, asymmetric vote |
| Anchor | the math-olympiad skill's proof-then-verify pipeline itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete failure the trace-stripping rule prevents (a verifier nodding along with visible reasoning); BCRY states the rule's scope (a proof gets in only after the reasoning is hidden, and a verifier would rather abstain than guess) — together they cover what the rule catches and what it refuses to do, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the math-olympiad Skill's SKILL.md specifies (the interpretation
check, the parallel solvers with internal refinement, the no-computation
constraint, stripping the thinking trace before verification, the
pattern-armed adversarial checklist, the asymmetric vote thresholds, and
calibrated abstention) — not an inference about hidden model internals.
Per simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (WRITER LAW requires the trigger word be a
single token the typed text actually contains verbatim — "everything"
corrected to "just the proof" — carrying the wrong-guess pedagogy instead
of a dedicated beat); B01's two halves (interpretation check +
parallel solving; context isolation + adversarial verify + asymmetric
vote) are kept as one beat each, NB01 and NB02, with B02's asymmetric-vote
detail folded into NB02 rather than opening a fourth body beat; B02's
remaining "four patterns" content (label every agent in batch mode, deep
mode before abstention as its own step, the presentation pass) and B05's
long "gets it right / where it bites" list (dual context isolation, the
grounded 50/63 interpretation-error figure, the VERBATIM solver-prompt
fragility, the missing cost guidance, the missing label-recovery path) are
compressed into NB03, keeping only the single fact a general audience
needs and can act on — that a verifier reading visible reasoning tends to
agree with it, which is the concrete reason the trace gets stripped in the
first place — and dropping the batch-labeling, cost, and prompt-wording
gaps that assume a technical audience running the skill directly, which
simple/hai-simple doesn't target; Teardown framing ("gets it right,"
"where it bites") is stripped to a plain mechanism-and-consequence
description, per the NO JUDGMENT register check; BVDT's verdict facts
(the asymmetric vote numbers, calibrated abstention) are merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's olympiad-specific instructions (solve an IMO/Putnam-style
inequality) replaced by a concrete, paste-ready prompt that needs no
competition-math background, so it's actually runnable by any viewer
today; BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`MathOlympiadAnatomy` / `MathOlympiadDesign` / `MathOlympiadTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
