# SCRIPT.md — It Cites the Evidence. It Never Guesses. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-clinical-note-extract-skill` (Teardown, walks the
Anthropic `clinical-note-extract-skill` Claude Skill from the `healthcare`
book's plugin set) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would guess a value missing from a clinical note. It
doesn't — it only cites what's actually written, span by span. So: does
Claude cite a note's values, not guess them?

*(Text typed on screen: "Does Claude / guess a value / from a clinical /
note?" — trigger word "guess" corrects to "cite", landing on: "Does Claude
cite a value from a clinical note?" Rates reused from the working
`financial-services--claude-liam-kyc-rules` sibling's configuration
(42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line text), which
cleared the >=8s TIMING LAW floor cleanly with a comparably short text.)*

## Body — anatomy, pipeline, what the skill actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
clinical-note-extract-skill. It has six files — SKILL.md holds the
instructions, in plain language, and four folders hold assets, references,
scripts, and workflows. Claude reads the file, then acts on what it says.

**NB02 — Four-step pipeline** (source B02, pipeline — corrected, see note
below)
Inside, the instructions run as four steps, in order: define a schema for
what to pull, extract candidate values, validate each one — checking that
its span actually appears in the note, then dispatching further checks by
field type — and report the result. No branching, unless a step itself
says so.

**NB03 — Cites or nulls, never guesses** (source B03, design tell —
re-registered Teardown → Plain: the source's "gets it right: repeatable
results / what it bites: anything outside the spec" framing is dropped for
a plain statement of the mechanism and its boundary; also folds in BVDT's
verdict facts)
This skill pulls values from a clinical note against a schema you define.
For every field it finds, it cites the exact span of text that supports
it. For every field it can't find, it returns an explicit null — never a
guess. Same note, same schema, same output, every run. What it won't do is
infer past what's on the page.

## Close

**BCRY — carry-out**
Clinical-note-extract-skill only writes down what the note actually says,
citing the exact text — and marks everything else null instead of
guessing.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a block of text with several
facts I need pulled into fields. For each field, don't guess — show me the
literal text you're using as evidence, and if you can't find it, tell me
it's null instead of inferring. That's the same discipline
clinical-note-extract-skill follows — cite the evidence, or say it's
missing.

**BOUT — outro**
It Cites the Evidence. It Never Guesses. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a guess-or-cite question — does Claude infer a plausible value, or only report what it can point to? |
| Wrong guess | B00 (WRITER LAW) | "guess" corrected to "cite" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the four-step pipeline (schema, extract, validate, report) Claude runs it through |
| Anchor | the clinical-note-extract-skill skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (cites a span when it finds one) and what it does not do (guess or infer past the page); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the clinical-note-extract-skill Skill specifies (the folder/file
structure, the four-step pipeline, the span-citation and null-safety
mechanism, and the same-input/same-output determinism) — not an inference
about hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Content correction (redo-specific, not an invented fact)

The source's B02 narration claimed "the pipeline has 2 steps" and named
only the two sub-checks inside validation (span check, then per-field-type
check). The source's own `AUDIT.md` ("Content accuracy note (narration
LOCKED — not fixable)") documents this as a scripting error: the actual
`SKILL.md` defines four steps — Define schema, Extract, Validate, Report —
and the locked narration only ever described the two sub-steps of step 3.
Because this redo writes fresh Plain narration from the same underlying
facts rather than reusing the source's locked sentences verbatim, NB02
states the real four-step pipeline and folds the two validation sub-steps
in as part of step 3, matching what AUDIT.md itself documents as correct.
This is a correction sourced from the project's own audit of the real
SKILL.md, not a new invented fact — see QUESTION.md.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01 kept as one beat; B02→NB02 kept
as one beat (content corrected per the note above); B03's Teardown framing
is restated in NB03 as a plain mechanism-and-boundary fact rather than a
strengths/gaps verdict, per the NO JUDGMENT register check, and BVDT's
verdict facts (same input → same output every run; limited to what the
file specifies) are merged into NB03/BCRY rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn
handoff, but the source's prompt text is adapted rather than copied
verbatim — the source asked the viewer to "read the
clinical-note-extract-skill skill," which requires a plugin install a
general viewer won't have, so this redo substitutes an equivalent,
actually paste-ready prompt that exercises the same cite-or-null discipline
on any block of text, without depending on any specific Skill file; BOUT
kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 +
BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
