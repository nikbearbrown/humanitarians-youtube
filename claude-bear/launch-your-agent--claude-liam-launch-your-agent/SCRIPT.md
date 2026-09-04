# SCRIPT.md — Claude, Launch Your Agent. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-launch-your-agent` (Teardown, walks the Anthropic
`launch-your-agent` Skill — helps a technical founder build on Claude
Managed Agents) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumes telling Claude to launch your agent means Claude
improvises the whole build. It doesn't — it follows the skill's fixed
steps, in order. So: does launching my agent mean Claude follows fixed
steps, not guesswork?

*(Text typed on screen: "Tell Claude to / launch my agent / and it
improvises, / right?" — trigger word "improvises" corrects to "follows
fixed steps", landing on: "Tell Claude to launch my agent and it follows
fixed steps, right?" Timing, mistake/hesitation rates, and typing speed
(42ms/char, 8% hesitateBetween, 4% mistakeRate, jitter 26, lead_silence_s
1.0) copied from the already-fixed pattern proven on the
claude-plugins-official--claude-liam-agent-development sibling, which hit
this exact TIMING LAW failure mode on its first (longer/faster/noisier)
attempt — reused here to avoid repeating that defect on the first render.)*

## Body — anatomy, the pipeline, the fixed-spec boundary

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
launch-your-agent. The SKILL.md file holds the full instruction set,
written in plain language — no hidden logic, no code Claude has to guess
at. Claude reads the file, then acts on it. The file is the program.

**NB02 — How the skill runs** (source B02, pipeline)
Inside the SKILL.md is a Steps section — the pipeline. Claude reads each
step and executes it, in order. For this skill, the steps are: find out
what the founder wants to build, scope a v0, launch it into their
account, grade the result, and iterate. If it should run on a schedule,
that becomes a scheduled deployment, with anything bigger laid out as v1
and v2. Execution is linear — no branching, unless a step says so.

**NB03 — A fixed spec** (source B03, design tell — re-registered
Teardown → Plain, "gets it right / where it bites" language stripped to a
plain mechanism-and-consequence description)
Because launch-your-agent is written as a fixed specification, not
open-ended judgment, it behaves the same way every time: same input, same
output, every run. That also marks its edge — Claude only does what the
SKILL.md actually specifies. Ask it to do something the steps don't
cover, and that request falls outside the skill entirely.

## Close

**BCRY — carry-out** (merges source BVDT's verdict facts — the fixed
sequence and its limit — into the single sentence that resolves B00's
wrong guess, per CARRY-OUT LAW)
Telling Claude to launch your agent doesn't launch a finished product —
it launches a v0 into your account, then earns anything bigger through
grading and iteration.

**BHTF — your turn** (source's prompt restored from a mid-word
truncation bug — see "Truncation note" below — content unchanged)
Your turn. Paste this into Claude: I want to help a technical founder
build whatever they want on Claude Managed Agents — an internal worker,
a piece of their product, or a customer-facing agent. Read the
launch-your-agent skill and walk me through what you will do before you
do it. That clause matters — asking Claude to explain first surfaces the
fixed steps before it starts running them.

**BOUT — outro**
Claude, Launch Your Agent. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a build question — does telling Claude to launch your agent get you Claude improvising a result, or a fixed process? |
| Wrong guess | B00 (WRITER LAW) | "improvises" corrected to "follows fixed steps" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | the SKILL.md as the program (NB01); the Steps pipeline — find out, scope a v0, launch, grade, iterate, optionally schedule (NB02); the fixed-spec consequence — same input/output, and the outside-the-spec boundary (NB03) |
| Anchor | the launch-your-agent skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the fixed-spec design guarantees (repeatable, same input/output) and what it cannot do (anything outside the SKILL.md's steps); BCRY states the design's payoff and its shape together (you get a v0 now, the bigger version only through iteration) — together they cover what the skill delivers and what it withholds, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the launch-your-agent Skill's SKILL.md specifies (a skill is a
folder read before Claude acts, the Steps pipeline finds out the founder's
goal / scopes a v0 / launches it / grades it / iterates / optionally
schedules it, and the fixed-specification consequence of repeatable
results with a hard boundary at what the file states) — not an inference
about hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02, B03→NB03 kept as one
beat each; BVDT's verdict facts (same input → same output every run,
limited to what the SKILL.md specifies) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

**Truncation note.** The source `beat_sheet.json`'s narration/prop strings
were generated by a batch builder that truncated several fields mid-word
at a fixed character count (e.g. B00's narration ends "...an internal
worker, a piece of their product, a p", BVDT's artifact lines end
"...Claude Managed Agents — an internal w", BHTF's prompt ends "...on
claude managed ag."). This redo restores the full, non-truncated
sentences using the one place the source states the complete fact without
truncation — B00's own `narration_text`, which spells out the skill's
full job ("Help a technical founder build whatever they want on Claude
Managed Agents — an internal worker, a piece of their product, a
customer-facing agent. Find out what they want to build, scope a v0,
launch it in their account, grade it, iterate, and (if it should run on a
clock) put it on a scheduled deployment, with everything bigger laid out
as v1/v2.") — no fact is added or changed, only the mid-word cutoffs are
repaired.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.
