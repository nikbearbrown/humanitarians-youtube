# SCRIPT.md — Claude, Irac Practice. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-irac-practice` (Teardown, walks the Anthropic
`irac-practice` legal Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked if practicing IRAC with Claude means Claude hands you the
finished answer. It doesn't — it walks you through the steps. So: does
practicing IRAC with Claude give you the steps?

*(Text typed on screen: "When I practice IRAC / with Claude, / does it
give me / the answer?" — trigger word "answer" corrects to "steps",
landing on: "When I practice IRAC with Claude, does it give me the
steps?")*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is called
irac-practice. Its one file, SKILL.md, holds the whole instruction set for
drilling IRAC — written in plain language, no hidden logic. Claude reads
it, then acts. The file is the program.

**NB02 — Pose, wait, check** (source B02, pipeline)
The drill lives in a Steps section. Claude reads each step in order: pose
the hypo, then wait for your Issue, your Rule, your Application, in that
order. Linear — no skipping ahead, unless a step says otherwise.

**NB03 — Conclusion, or Application** (source B03/BVDT, design tell /
verdict fact — re-registered Teardown → Plain)
One check inside it is specific: stating the right Conclusion without
showing the Application earns nothing — the Application is where the Rule
actually meets the facts, one fact at a time. A Conclusion that skips it is
a guess wearing the right answer.

## Close

**BCRY — carry-out**
Claude isn't grading your Conclusion — it's checking whether you showed
the Application, one fact at a time, on the way to it.

**BHTF — your turn**
Your turn. Paste this into Claude: give me a short fact pattern, one
paragraph. Read the irac-practice skill, and don't give me the answer —
ask me for my Issue first, then my Rule, then my Application, and only
check my Conclusion after I've given all three.

**BOUT — outro**
Claude, Irac Practice. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the practice question — does Claude just give you the answer? |
| Wrong guess | B00 (WRITER LAW) | "answer" corrected to "steps" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes a pose/wait/check pipeline linearly; one specific check governs Conclusion vs. Application |
| Anchor | the irac-practice Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "checking, not grading — Application, not Conclusion" states both what the mechanism does (a specific check applied) and its limit (only that check, not a verdict on whether the whole answer is correct), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: NB01–NB02 are direct descriptions of how any
Skill runs (a folder, one file, steps executed in order) — the same
mechanism already established, unchanged, across the `claude-liam-*` family.
NB03's Conclusion-vs-Application distinction is stated as a fact about IRAC
legal-writing method itself (a well-established convention, not a claim
about Claude's hidden internals), and needs no flag. Per simple's ONE-FLAG
LAW, when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (puppet cold open) + B01/B02/B03 (anatomy / pipeline
/ design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) — the
shortest shape in the `claude-liam-*` Teardown family, a single-example
skill walkthrough with no wrong-guess, anchor, or both-directions beats of
its own to redistribute. This redo keeps that same 7-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02
kept as one beat each; B03 and BVDT (design tell and verdict) are merged
into the single NB03 mechanism beat plus the BCRY carry-out sentence,
because the source's actual content behind those two beats never got past
an unfilled placeholder (literal `>` marks in `narration_text` — see
QUESTION.md) — there is no locked specific fact to preserve there beyond
"the SKILL.md defines a specific check," so this redo supplies the one
concrete, generically-true check that any IRAC-practice task is actually
for: distinguishing a Conclusion that skipped the Application from one that
earned it. BHTF kept as the your-turn handoff, with the source's bracketed
placeholder ("I want to >") replaced by a concrete, paste-ready scenario so
the prompt is actually runnable today; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (SkillTeardownAnatomy /
SkillTeardownPipeline / SkillTeardownMechanism / ClaudeVerdictArtifact /
ClaudeComposerAsk / ClaudeTitleOutro patterns) with B00 as a typed-UI cold
open (REMOTION `ClaudeComposerAsk`, not AI-VIDEO — the source never called a
generation service). NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00's cold open, which this redo replaces per hai-simple's mandate anyway.
