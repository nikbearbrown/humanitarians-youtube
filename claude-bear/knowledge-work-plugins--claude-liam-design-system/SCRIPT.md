# SCRIPT.md — Matched, Not Invented. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-design-system` (Teardown, walks the Anthropic
`design-system` Skill — audit, document, or extend your design system) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude keeps a design system consistent using taste. It
doesn't — a written file does. So: does Claude use its SKILL.md to keep a
design system consistent?

*(Text typed on screen: "Does Claude use / taste / to keep a design /
system consistent?" — trigger word "taste" corrects to "its SKILL.md",
landing on: "Does Claude use its SKILL.md to keep a design system
consistent?" NOTE: the `BrutalistHesitantWriter` component matches
`triggerWords` against single whitespace-separated tokens only — see
`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` line 130 — so a
multi-word trigger like "good taste" silently never fires. A first draft
used "good taste" as the trigger; caught by a frame pull through the full
B00 clip showing the naive text still uncorrected at the final frame, fixed
by narrowing the trigger to the single word "taste" and dropping "good"
from the on-screen text and narration.)*

## Body — anatomy, the pipeline, the one job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
design-system. Its SKILL.md holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts on it. The file is
the program.

**NB02 — Read then execute** (source B02, pipeline)
The pipeline lives in the Steps section. Claude reads each step in order,
then executes it — linear, no branching, unless a step says otherwise.

**NB03 — One file, one job** (source B03, design tell — re-registered
Teardown → Plain, kept as the mechanism-and-scope fact rather than the
"gets it right / what it bites" framing)
This skill has exactly one job: audit, document, or extend a design
system — checking for naming inconsistencies or hardcoded values across
components, writing documentation for a component's variants, states, and
accessibility notes, or designing a new pattern that fits the system
already there. All of it lives inside that one file's script. Nothing
outside it is invented from scratch.

## Close

**BCRY — carry-out**
design-system doesn't invent a new look — it checks your components
against the patterns already in your codebase, and matches or extends what
is already there.

**BHTF — your turn**
Your turn. Paste this into Claude: Audit my design system for naming
inconsistencies and hardcoded values. Walk me through your plan before you
act. That last clause matters — explaining the plan first surfaces the
real constraint logic, not just a recommendation.

**BOUT — outro**
Matched, Not Invented. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a source-of-authority question — does Claude's own good taste keep a design system consistent? |
| Wrong guess | B00 (WRITER LAW) | "good taste" corrected to "its SKILL.md" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | a skill is a folder with a SKILL.md instruction set Claude reads before acting; the pipeline reads and executes the Steps section in linear order |
| Anchor | the design-system skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the one job covers (audit, document, or extend against the existing system) and states plainly that nothing outside it is invented from scratch; BCRY states the design's payoff and its limit together (it checks against what's already there, and never invents a fresh look) — together they cover what the skill delivers and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the design-system Skill's SKILL.md specifies (the folder/file structure,
the Steps-section pipeline, the linear execute-in-order behavior, and the
exact scope of the one task — auditing, documenting, or extending a design
system against naming, hardcoded values, variants, states, and
accessibility notes) — not an inference about hidden model internals. Per
simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown framing ("Here is the Teardown moment... What it gets
right: repeatable results. What it bites: anything outside the spec.") is
compressed into NB03, keeping the same underlying fact — the skill's task
is exactly one job (audit, document, or extend, across the named
scenarios: naming inconsistencies, hardcoded values, component
documentation, new-pattern fit) and nothing beyond that — stripped of
"gets it right / where it bites" verdict language per the NO JUDGMENT
register check; BVDT's verdict facts (repeatable execution, and the limit
that only the file's spec is covered) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff — the source's prompt
text was garbled by truncation ("I want to audit, document, or extend your
design system. use when checking for naming inco.") and is rebuilt here as
a concrete, paste-ready, ungarbled prompt carrying the same request (audit
a design system for naming inconsistencies and hardcoded values) plus the
source's own flagged clause ("walk me through what you will do before you
do it"); BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
