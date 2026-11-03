# SCRIPT.md — Runs the Steps. Doesn't Write the CIM. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-cim-builder` (Teardown, walks the Anthropic
`cim-builder` skill for sell-side M&A CIM drafting) — question, facts, and
body argument carried over; narration re-registered to Plain (explain,
then stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed cim-builder would write their CIM for them, the way a
person would. It doesn't — it structures one, from a fixed set of steps.
Does cim-builder structure my CIM for me?

*(Text typed on screen: "Does the / cim-builder skill / write my CIM / for
me?" — trigger word "write" corrects to "structure," landing on: "Does the
cim-builder skill structure my CIM for me?")*

## Body — anatomy, the pipeline, the limit

**NB01 — A skill is a folder.** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is cim-builder.
Its SKILL.md holds the full instruction set, in plain language — no hidden
logic. Claude reads the file, then acts on it. The file is the program.

**NB02 — One step at a time.** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and runs it — linear, one after another, unless a step itself says to
branch.

**NB03 — Structure, every time.** (source B03 design tell, re-registered
Teardown → Plain; source BVDT's verdict facts folded into BCRY below)
cim-builder's job is specific: structure and draft a Confidential
Information Memorandum for a sell-side deal — organizing company
information into one investor-ready document, with consistent formatting
and a narrative that holds together, the same way on every run. What isn't
in the SKILL.md's steps isn't part of the job.

## Close

**BCRY — carry-out**
cim-builder doesn't write your CIM — it runs the SKILL.md's fixed steps on
it, the same way every time.

**BHTF — your turn**
Your turn. Here's the prompt — read it with me. Paste this into Claude: "I
want to structure and draft a confidential information memorandum for a
sell-side M&A process. Read the cim-builder skill and walk me through what
you will do before you do it." That last clause matters — asking Claude to
explain first surfaces the actual steps it's about to run.

**BOUT — outro**
Runs the Steps. Doesn't Write the CIM. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an authorship question — does the skill write the CIM's content, or run a spec on what's given? |
| Wrong guess | B00 (WRITER LAW) | "write" corrected to "structure" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder / SKILL.md-as-instruction-set fact, and the linear Steps-section pipeline it executes |
| Anchor | the cim-builder skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the spec covers (structure, formatting, narrative flow, repeatably) and what it doesn't (anything outside the steps); BCRY states the same distinction as the carry-out (runs steps, doesn't write/decide) — together they cover what the skill does and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the cim-builder Skill's SKILL.md specifies, per the source sheet's own
narration (the file-as-instruction-set anatomy, the linear Steps-section
pipeline, the CIM-structuring job description, and the same-input-same-
output/only-what-the-file-says limit) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's design-tell framing ("what it gets right" / "what it bites") is
compressed into NB03 as a plain mechanism-and-scope statement, dropping the
Teardown "gets right/bites" verdict language per the NO JUDGMENT register
check; BVDT's verdict facts (repeatable results, same input → same output,
the file-says-so limit) are merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW;
BHTF kept as the your-turn handoff, with the source's prompt carried over
(lightly de-truncated — the source narration cut the phrase to "sell-side
m&a proc," restored here to "a sell-side M&A process" since it is the same
prompt, not a new one); BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact` / `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's cold open, which this redo replaces
per hai-simple's mandate anyway.
