# SCRIPT.md — Claude, Demand Draft. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-demand-draft` (Teardown, walks the Anthropic
`demand-draft` legal Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude just writes a demand letter from the facts. It
doesn't just write — it checks first. So: when Claude drafts one, does it
check first?

*(Text typed on screen: "When Claude drafts / a demand letter, / does it
just write?" — trigger word "write" (a single token; the component
matches per-token, not phrase-wise) corrects to "check first", landing on:
"When Claude drafts a demand letter, does it just check first?")*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is called
demand-draft. Its one file, SKILL.md, holds the whole instruction set,
written in plain language — no hidden logic. Claude reads it, then acts.
The file is the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and executes it — read the file, execute each step, return the result.
Linear: no branching, unless a step says otherwise.

**NB03 — The four-part gate** (source B03, design tell — re-registered
Teardown → Plain)
One instruction inside it is specific: before any letter gets drafted, four
checks have to clear — privilege, Rule 408, waiver, and admission. Only
after that does Claude produce the draft, as a docx file, with a post-send
checklist and an offer to open a matter.

## Close

**BCRY — carry-out**
Claude isn't deciding when a demand letter is ready to send — the checklist
is: privilege, Rule 408, waiver, and admission all have to clear first.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a completed intake for a demand
letter. Read the demand-draft skill, and before you draft anything, walk me
through the checklist you'll run first — privilege, Rule 408, waiver,
admission — and what you still need from me.

**BOUT — outro**
Claude, Demand Draft. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a legal question — does Claude just write? |
| Wrong guess | B00 (WRITER LAW) | "just write" corrected to "check first" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes steps linearly; one specific four-part gate governs when a draft may be produced |
| Anchor | the demand-draft Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "the checklist decides, not Claude's judgment" states both what the mechanism does (execute reliably against the gate) and its limit (only what clears the gate goes out), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the Skill's SKILL.md specifies (a folder, one file, a Steps section executed
in order, the privilege/408/waiver/admission gate) — not an inference about
hidden model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (puppet-style cold open) + B01/B02/B03 (anatomy /
pipeline / design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) —
the shortest of the `claude-liam-*` Teardown family, a single-example skill
walkthrough with no wrong-guess, anchor, or both-directions beats of its own
to redistribute. This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02, B03→NB03 kept as one
beat each, Teardown framing ("the design tell," "what it gets right / what
it bites") stripped to a plain mechanism description; BVDT's two verdict
facts (reliable execution, and the checklist-only limit) merged into the
single BCRY carry-out sentence rather than kept as a separate artifact-card
beat, since Plain register carries one carry-out sentence, not a bulleted
verdict (CARRY-OUT LAW); BHTF kept as the your-turn handoff, with the
source's bracketed placeholder replaced by a concrete, paste-ready scenario
so the prompt is actually runnable today; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism` / `ClaudeVerdictArtifact` /
`ClaudeComposerAsk` / `ClaudeTitleOutro` patterns) with B00 as a Composer-UI
cold open (REMOTION `ClaudeComposerAsk`, not AI-VIDEO — the source never
called a generation service). NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's cold open, which this redo replaces per
hai-simple's mandate anyway.
