# SCRIPT.md — It Drafts the Protocol. It Doesn't Decide the Trial. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-clinical-trial-protocol-skill` (Teardown, walks the
Anthropic `clinical-trial-protocol-skill` Claude Skill from the `healthcare`
book's plugin set) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians
AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would decide how a clinical trial should run. It
doesn't — it drafts the protocol document to a fixed specification. So: does
Claude draft a clinical trial protocol, not decide one?

*(Text typed on screen: "Does Claude / decide a clinical / trial protocol?"
— trigger word "decide" corrects to "draft", landing on: "Does Claude draft
a clinical trial protocol?" Rates reused from the working
`financial-services--claude-liam-kyc-rules` sibling's proven configuration
(42ms/char, 8% hesitateBetween, 4% mistakeRate, short 3-line text), which has
cleared the >=8s TIMING LAW floor cleanly with comparably short text across
several other reels in this series.)*

## Body — anatomy, pipeline, what the skill actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
clinical-trial-protocol-skill. It has five files — SKILL.md holds the
instructions, in plain language, alongside a README, and folders for assets,
references, and scripts. Claude reads the file, then acts on what it says.

**NB02 — Three-step pipeline** (source B02, pipeline — kept as-is; source's
own AUDIT.md flagged no content error here, unlike the note-extract-skill
sibling)
The pipeline runs in three steps: Claude reads SKILL.md to load the
instructions, executes each step from the Steps section in order, then
returns the result. Execution is linear — no branching, unless a step itself
says so.

**NB03 — Drafts to spec, never decides** (source B03, design tell —
re-registered Teardown → Plain: the source's "gets it right: repeatable
results / what it bites: anything outside the spec" framing is dropped for a
plain statement of the mechanism and its boundary; also folds in BVDT's
verdict facts)
This skill's job is generating clinical trial protocols for medical devices
or drugs — for requests like "create a clinical trial protocol" or "help me
design a clinical study." It follows the SKILL.md's instructions exactly, so
the same request produces the same kind of protocol, every run. What it
won't do is anything outside what the file specifies — the trial-design
decisions still belong to a person.

## Close

**BCRY — carry-out**
Clinical-trial-protocol-skill drafts the protocol to a fixed spec — it
doesn't decide how the trial should run; that call still belongs to a
person.

**BHTF — your turn**
Your turn. Paste this into Claude: I want you to draft a document from an
outline I'll give you. Before you write anything, walk me through what
you'll include and what you won't — then flag anything my outline doesn't
cover. That's the same discipline clinical-trial-protocol-skill follows:
work the spec exactly, and say out loud what's outside it.

**BOUT — outro**
It Drafts the Protocol. It Doesn't Decide the Trial. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a decide-or-draft question — is Claude exercising clinical judgment, or only producing a document to spec? |
| Wrong guess | B00 (WRITER LAW) | "decide" corrected to "draft" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the three-step pipeline (read SKILL.md, execute steps, return result) Claude runs it through |
| Anchor | the clinical-trial-protocol-skill skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time, matching the `clinical-note-extract-skill` sibling's disposition |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (drafts a protocol to spec, repeatably) and what it does not do (decide the trial design); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the clinical-trial-protocol-skill Skill specifies (the folder/file
structure, the three-step pipeline, the spec-driven drafting mechanism, and
the same-input/same-output determinism) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 kept as one beat; B02→NB02 kept as
one beat (no content correction needed, per the source's own AUDIT.md — see
QUESTION.md); B03's Teardown framing is restated in NB03 as a plain
mechanism-and-boundary fact rather than a strengths/gaps verdict, per the NO
JUDGMENT register check, and BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) are merged into NB03/BCRY
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW;
BHTF kept as the your-turn handoff, but the source's prompt text is adapted
rather than copied verbatim — the source asked the viewer to "read the
clinical-trial-protocol-skill skill," which requires a plugin install a
general viewer won't have, so this redo substitutes an equivalent,
actually paste-ready prompt that exercises the same spec-discipline on any
document/outline, without depending on any specific Skill file or medical
subject matter; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
