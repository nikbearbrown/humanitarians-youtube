# SCRIPT.md — Feedback, Not a Redesign. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-design-critique` (Teardown, walks the Anthropic
`design-critique` Skill — structured design feedback on usability,
hierarchy, and consistency) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a design critique means Claude fixes the mockup itself. It
doesn't — it gives structured feedback on usability, hierarchy, and
consistency. So: how do I get Claude to critique my design mockup?

*(Text typed on screen: "How do I get Claude / to fix my design / mockup?"
— trigger word "fix" corrects to "critique", landing on: "How do I get
Claude to critique my design mockup?" 49 characters across 3 lines, under
the family's established-safe 60-char config, so the same charMs/
mistakeRate/hesitate rates clear the TIMING LAW window with margin to
spare.)*

## Body — anatomy, the pipeline, the limit

**NB01 — A folder, not a program** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
design-critique — a single SKILL.md file, about three kilobytes. It's the
whole instruction set, written in plain language, with no hidden logic
underneath it. Claude reads it, then acts on what it says. The file is
the program.

**NB02 — How it gets picked up and run** (source B02, pipeline; job
description folded in from source B00's own quoted description)
Its job, word for word: get structured design feedback on usability,
hierarchy, and consistency. It triggers when you ask Claude to review a
design, critique a mockup, or say what do you think of this screen — or
when you share a Figma link or screenshot, at any stage from early
exploration to final polish. Once triggered, Claude reads the Steps
section and runs them in order — linear, no branching unless a step says
so.

**NB03 — Feedback, not a redesign** (source B03/BVDT, design tell +
verdict — re-registered Teardown → Plain, judgment stripped, kept as the
one fact a general viewer can act on)
That's feedback, not a redesign. The skill reviews usability, hierarchy,
and consistency, and hands back structured feedback — but it never
touches the mockup itself. Run the same screen through twice, and the
feedback comes back the same both times. But it only checks those three
things — usability, hierarchy, consistency — anything outside that is
outside what it sees.

## Close

**BCRY — carry-out**
design-critique doesn't redesign your mockup — it hands back structured
feedback on usability, hierarchy, and consistency, the same way every
time.

**BHTF — your turn**
Your turn. Paste this into Claude: I want structured feedback on this
design's usability, hierarchy, and consistency — read the
design-critique skill and walk me through what you will do before you do
it. That clause matters: having Claude explain itself first, before it
acts, is how you actually see the instructions it's following, not just
the result.

**BOUT — outro**
Feedback, Not a Redesign. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a scope question — will Claude redesign the mockup, or hand back feedback on it? |
| Wrong guess | B00 (WRITER LAW) | "fix" corrected to "critique" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the single-file folder anatomy, the description's trigger-match role (review a design, critique a mockup, "what do you think of this screen?", or a shared Figma link/screenshot at any stage), and the linear Steps pipeline once triggered |
| Anchor | the design-critique skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill, one running case — a mockup checked against usability, hierarchy, and consistency) — not a planted-and-paid-off separate case, so there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states both what holds (same screen, same feedback, every time) and what doesn't (anything outside usability/hierarchy/consistency is outside what the skill sees); BCRY states the same pair as the closing sentence — matching the source's verdict beat, which paired the identical two facts ("repeatable results" / "only what the file says") |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the design-critique Skill's SKILL.md specifies (the single-file structure,
the job description quoted from the description field, the trigger
phrases — "review this design", "critique this mockup", "what do you
think of this screen?", or a shared Figma link/screenshot at any stage
from exploration to final polish — the linear Steps execution, and the
same-input/same-output/spec-only limit) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each
(NB02 additionally folds in the job-description clause the source only
quoted inline at B00, since B00 is no longer the composer-ask beat that
carried it); B03's Teardown "design tell" framing ("here is the Teardown
moment", "what it gets right / what it bites") and BVDT's verdict artifact
(four bulleted lines restating the skill name, its job description, the
same-input/same-output claim, and the "only what the SKILL.md specifies"
limit) are merged into a single NB03 beat, stripped of judgment language
per the NO JUDGMENT register check, and kept as the one fact a general
audience needs and can act on (repeatable feedback / three-checks-only
limit) — BVDT's separate artifact card is not kept as its own beat, per
CARRY-OUT LAW (the verdict facts belong in the single BCRY sentence, not a
bulleted recap); BHTF kept as the your-turn handoff, with the source's
garbled truncation artifacts (B03's "...trigger with \"review this d." and
BVDT's "...trigger." and BHTF's "...trigger.") rewritten to the actual
job-description phrase the skill's own description uses in full at source
B00 ("get structured design feedback on usability, hierarchy, and
consistency. Trigger with 'review this design', 'critique this mockup',
'what do you think of this screen?', or when sharing a Figma link or
screenshot for feedback at any stage from exploration to final polish"),
since the source text was a template-substitution artifact cut off
mid-sentence at those three beats, not a deliberately authored prompt;
BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03
+ BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
