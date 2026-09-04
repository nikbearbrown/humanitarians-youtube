# SCRIPT.md — Review, Not Repair. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-accessibility-review` (Teardown, walks the Anthropic
`accessibility-review` Skill — a WCAG 2.1 AA accessibility audit for a
design or page) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed accessibility review means Claude fixes the design. It
doesn't — it checks the design against a fixed standard. So: how do I get
Claude to review my design for accessibility?

*(Text typed on screen: "How do I get Claude / to fix my design / for
accessibility?" — trigger word "fix" corrects to "review", landing on:
"How do I get Claude to review my design for accessibility?" 56 characters
across 3 lines, comfortably under the family's established-safe 60-char
config, so the same charMs/mistakeRate/hesitate rates clear the TIMING LAW
window with margin to spare.)*

## Body — anatomy, the pipeline, the limit

**NB01 — A folder, not a program** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
accessibility-review — a single SKILL.md file, about four kilobytes. It's
the whole instruction set, written in plain language, with no hidden logic
underneath it. Claude reads it, then acts on what it says. The file is the
program.

**NB02 — How it gets picked up and run** (source B02, pipeline; trigger
clause folded in from source B00's own quoted description)
Its job, word for word: run a WCAG 2.1 AA accessibility audit on a design
or page. It triggers on requests like auditing accessibility, checking
a11y, or asking if a design is accessible — or before handing off work
that touches color contrast, keyboard navigation, touch target size, or
screen reader behavior. Once triggered, Claude reads the Steps section and
runs them in order — linear, no branching unless a step says so.

**NB03 — An audit, not a repair** (source B03/BVDT, design tell + verdict
— re-registered Teardown → Plain, judgment stripped, kept as the one fact
a general viewer can act on)
That's an audit, not a repair. The skill checks a design against a fixed
standard, WCAG 2.1 AA, and reports exactly where it fails — it doesn't
rewrite the design to fix what it finds. Run the same design through
twice, and the audit comes back the same both times. But it only checks
what that standard covers — anything outside WCAG 2.1 AA is outside what
this skill sees.

## Close

**BCRY — carry-out**
accessibility-review doesn't fix a design — it checks it against WCAG 2.1
AA and reports exactly where it fails, the same way every time.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to audit a design for
accessibility — read the accessibility-review skill and walk me through
what you will do before you do it. That clause matters: having Claude
explain itself first, before it acts, is how you actually see the
instructions it's following, not just the result.

**BOUT — outro**
Review, Not Repair. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a scope question — will Claude fix the design, or check it against a standard? |
| Wrong guess | B00 (WRITER LAW) | "fix" corrected to "review" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the single-file folder anatomy, the description's trigger-match role, and the linear Steps pipeline once triggered |
| Anchor | the accessibility-review skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill, and the one running case — WCAG 2.1 AA against a design or page) — not a planted-and-paid-off separate case, so there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states both what holds (same design, same audit result, every time) and what doesn't (anything outside WCAG 2.1 AA is outside what the skill sees); BCRY states the same pair as the closing sentence — matching the source's verdict beat, which paired the identical two facts ("repeatable results" / "anything outside the spec") |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the accessibility-review Skill's SKILL.md specifies (the single-file
structure, the WCAG 2.1 AA audit job description, the trigger phrases quoted
from the description field, the linear Steps execution, and the
same-input/same-output/standard-only limit) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each
(NB02 additionally folds in the trigger-phrase clause the source only
quoted inline at B00, since B00 is no longer the composer-ask beat that
carried it); B03's Teardown "design tell" framing ("here is the Teardown
moment", "what it gets right / what it bites") and BVDT's verdict artifact
(four bulleted lines restating the skill name, its job description, the
same-input/same-output claim, and the "only what the SKILL.md specifies"
limit) are merged into a single NB03 beat, stripped of judgment language
per the NO JUDGMENT register check, and kept as the one fact a general
audience needs and can act on (repeatable audit / standard-only limit) —
BVDT's separate artifact card is not kept as its own beat, per CARRY-OUT
LAW (the verdict facts belong in the single BCRY sentence, not a bulleted
recap); BHTF kept as the your-turn handoff, with the source's garbled
truncation artifact ("I want to run a wcag 2.1 aa accessibility audit on a
design or page. trigger with \"audit a…") rewritten to the actual trigger
phrase the skill's own description uses ("I want to audit a design for
accessibility"), since the source text was a template-substitution
artifact cut off mid-sentence, not a deliberately authored prompt; BOUT
kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 +
BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
