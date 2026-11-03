# SCRIPT.md — It Tests and Classifies. It Doesn't Decide. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-audit-support` (Teardown, walks the Anthropic
`audit-support` Claude Skill from the `knowledge-work-plugins` book's
finance plugin set) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would decide whether a company passes its SOX 404
audit. It doesn't — it supports the control testing behind that call. So:
does Claude support a company's SOX 404 audit?

*(Text typed on screen: "Does Claude / pass a / company's SOX / 404
audit?" — trigger word "pass" corrects to "support", landing on: "Does
Claude support a company's SOX 404 audit?" Rates reused from the
`financial-services--claude-liam-kyc-rules` sibling's proven working
configuration (42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line
text), which cleared the >=8s TIMING LAW floor cleanly with a comparably
short text.)*

## Body — anatomy, pipeline, what audit-support actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
audit-support. It's just one file, SKILL.md, written in plain language —
no hidden logic. Claude reads the file, then acts on what it says. The
file is the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
select the audit sample. Then: test each item against the control's
stated criteria. Then: classify what it finds and write it up. No
branching, unless a step itself tells it to branch.

**NB03 — Tests and Classifies** (source B03, design tell — re-registered
Teardown → Plain: the source's "gets it right: repeatable results / what
it bites: anything outside the spec" framing is dropped for a plain
statement of the mechanism and its boundary)
This particular skill is built for one job: SOX 404 compliance. Given a
control to test, it picks the sample using the firm's sampling
methodology, tests each item against the control's stated criteria, and
classifies any exception it finds. It doesn't decide whether the
company's controls pass overall. It tests the sample and writes it up —
the audit opinion stays with the auditor.

## Close

**BCRY — carry-out**
Audit-support tests the sample against the firm's own criteria and
classifies what it finds — it never decides whether the company's
controls pass.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a set of criteria and a sample
of items I need to test against them. Before you tell me whether it
passes overall, walk me through each item, whether it meets the criteria,
and what doesn't — then leave the overall call to me. That's the same
order audit-support follows — test the sample against the criteria,
classify what you find, and leave the opinion to a person.

**BOUT — outro**
It Tests and Classifies. It Doesn't Decide. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a pass-or-support question — does Claude decide the company's audit fate, or just support the testing? |
| Wrong guess | B00 (WRITER LAW) | "pass" corrected to "support" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through (select sample, test control, write it up) |
| Anchor | the audit-support skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (picks the sample, tests, classifies) and what it does not do (decide the company's overall pass/fail); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the audit-support Skill's SKILL.md specifies (the one-file folder
structure, the linear step execution, the sample-selection-and-control-
testing mechanism, the classification of exceptions, and the same-input/
same-output determinism) — not an inference about hidden model internals.
Per simple's ONE-FLAG LAW, when the source genuinely supports everything
as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B03's Teardown "gets it right: repeatable results / what it bites:
anything outside the spec" framing is restated in NB03 as a plain
mechanism-and-boundary fact (what the skill tests and classifies, and what
it declines to decide) rather than a strengths/gaps verdict, per the NO
JUDGMENT register check; BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the
source's prompt text is adapted rather than copied verbatim — the source
asked the viewer to "read the audit-support skill," which requires a
plugin install a general viewer won't have, so this redo substitutes an
equivalent, actually paste-ready prompt that exercises the same
test-before-opine habit ("walk me through each item... then leave the
overall call to me") without depending on any specific Skill file; BOUT
kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 +
BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
