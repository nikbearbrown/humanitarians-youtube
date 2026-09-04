# SCRIPT.md — Claude Doesn't Write One Email. It Designs the Sequence. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-email-sequence` (Teardown, walks the Anthropic
`email-sequence` Skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

**Source-material note:** unlike some sibling redos in this batch, the
source reel's own narration carries the FULL skill description, unbroken,
in its B00 beat: "Design and draft multi-email sequences with full copy,
timing, branching logic, exit conditions, and performance benchmarks. Use
when building onboarding, lead nurture, re-engagement, win-back, or product
launch flows, when you need a complete drip campaign with A/B test
suggestions, or when mapping a sequence end-to-end with a flow diagram."
Later source beats (B03, BVDT, BHTF) quote that same description but got
truncated mid-list by whatever produced them ("...exit conditions, and.");
this redo uses B00's complete, untruncated version as the source of record
everywhere the description is needed, so no fact here is inferred or
guessed — every claim in this script is directly readable in the source
sheet. Per ONE-FLAG LAW: no flag is used in this reel, because the source
genuinely supports everything stated.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed the skill just writes one email. It doesn't — it designs
the whole sequence: timing between sends, branching logic, exit
conditions. So: does Claude write one email?

*(Text typed on screen: "Does Claude\nwrite one\nemail?" — trigger word
"email" corrects to "sequence", landing on: "Does Claude write one
sequence?" 3 lines, 24 characters — short-line, moderate-charMs shape
matching the `knowledge-work-plugins--claude-liam-discover-brand` sibling,
kept deliberately inside the >=9s TIMING LAW window rather than discovered
by a failed first render.)*

## Body — anatomy, pipeline, the actual job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
email-sequence. Its SKILL.md file holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — Steps, in order** (source B02, pipeline)
The instructions are laid out in a Steps section. Claude reads each step in
order and runs it — linear, no branching unless a step says otherwise.

**NB03 — Design the whole sequence** (source B03, design tell —
re-registered Teardown → Plain; no inference, no flag — the full
description is read directly from the source's own B00)
Here's the actual job: design and draft the full multi-email sequence —
the copy for every message, the timing between sends, branching logic for
opens and clicks, exit conditions, and benchmarks to judge it by. Built for
onboarding, lead nurture, win-back, re-engagement, and launch flows.

## Close

**BCRY — carry-out**
Ask it for an email, and email-sequence hands back the whole sequence —
copy, timing, branches, exit conditions — built the same way every time.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm launching a two-week free trial for
my product. Design a five-email onboarding sequence — send timing for
each, one branch for someone who never opens the first email, and an exit
condition once they upgrade. Walk me through the sequence before you write
the copy. That clause matters — explaining first surfaces the real
constraint logic.

**BOUT — outro**
Claude, Email Sequence. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a single-email question — will Claude write me one good email, the way a person answering a request for "an email" would? |
| Wrong guess | B00 (WRITER LAW) | "email" corrected to "sequence" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a skill is a folder with a SKILL.md Claude reads before acting; the Steps section runs linearly; the actual job is designing a full sequence — copy, timing, branching, exit conditions, benchmarks — not one message |
| Anchor | the email-sequence skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — matches the discover-brand sibling's shape exactly |
| Both directions | folded into NB03 + BCRY | NB03 states what gets built (the full sequence, every listed piece); BCRY states the same design's boundary in the other direction (one ask in, the whole flow out, built the same way every time — never more or less than what was asked) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

Zero flags. Per simple's ONE-FLAG LAW: "if the source genuinely supports
everything, there is no flag." Every claim in this script — the skill's
job (full copy, timing, branching logic, exit conditions, performance
benchmarks), its use cases (onboarding, lead nurture, re-engagement,
win-back, product launch flows, drip campaigns with A/B test suggestions),
the anatomy (a skill is a folder with a SKILL.md Claude reads before
acting), the pipeline (Steps run linearly), and the verdict (same input,
same output, every run; the limit is only what the file says) — is read
directly off the source `beat_sheet.json`'s own `narration_text` fields,
principally B00's complete, untruncated skill description. Nothing here is
inferred from a name, a sibling skill, or an inaccessible file.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right / where it bites" framing is compressed into
NB03 as a plain mechanism description, per the NO JUDGMENT register check;
BVDT's verdict facts (same input, same output, every run; the limit is
only what the file says) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff — the source's own
prompt asks Claude to "read the email-sequence skill," which assumes an
Anthropic Skill file a general viewer is unlikely to have installed, so
this redo writes a concrete, paste-ready prompt that exercises the
identical mechanism (one goal in, a designed multi-email sequence with
timing, a branch, and an exit condition out) without requiring any
specific Skill install; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
