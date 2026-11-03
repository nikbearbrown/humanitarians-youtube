# SCRIPT.md — It Reads Like Empathy. It's a Spec. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-draft-response` (Teardown, walks the Anthropic
`draft-response` Skill — draft a professional customer-facing response
tailored to the situation and relationship) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude's own empathy writes a good customer reply. It
doesn't — a written file does. So: does Claude use its SKILL.md to draft a
good customer reply?

*(Text typed on screen: "Does Claude use / empathy / to draft a good /
customer reply?" — trigger word "empathy" corrects to "its SKILL.md",
landing on: "Does Claude use its SKILL.md to draft a good customer
reply?")*

## Body — anatomy, the pipeline, the one job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
draft-response. Its SKILL.md holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts on it. The file is
the program.

**NB02 — Read then execute** (source B02, pipeline)
The pipeline lives in the Steps section. Claude reads each step in order,
then executes it — linear, no branching, unless a step says otherwise.

**NB03 — One file, one job** (source B03, design tell — re-registered
Teardown → Plain, kept as the mechanism-and-scope fact rather than the
"gets it right / where it bites" framing)
This skill has exactly one job: draft a professional customer-facing
response, tailored to the situation and the relationship — a product
question, an escalation or outage, bad news like a delay or a won't-fix, a
declined feature request, or a billing issue. All of it lives inside that
one file's script. Nothing outside it is covered.

## Close

**BCRY — carry-out**
It reads like empathy — really it's a spec, and it runs the same way every
time you call it.

**BHTF — your turn**
Your turn. Paste this into Claude: Draft a reply to an escalation for my
team. Walk me through your plan before you act. That last clause matters —
explaining the plan first surfaces the real constraint logic, not just a
draft.

*(On-screen command shortened from the first draft — "Draft a
customer-facing response to an escalation for my team. Walk me through your
plan before you act." (104 chars) — to fit `ClaudeComposerAsk`'s input area,
which is hard-capped at `maxHeight: CMD * 1.45 * 3` with `overflow: hidden`.
Caught by a frame pull mid-BHTF: the visible card read "Draft a
customer-facing response to an escalation for my team. Walk m" with the
rest silently clipped off-frame — the long compound word
"customer-facing" plus "escalation" forced an early wrap past the 3-line
cap even though the raw character count was close to a sibling reel's
working command. Fixed by shortening to "Draft a reply to an escalation for
my team. Walk me through your plan before you act." (85 chars, 2-line fit)
and updating BHTF's narration to match; re-generated BHTF's audio only
(12.48s) and re-rendered BHTF only (media/B00, NB01-03, BCRY, BOUT
untouched). Reverified by frame pull: the full sentence is visible on 2
lines with no clipping.)*

**BOUT — outro**
It Reads Like Empathy. It's a Spec. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a source-of-authority question — does Claude's own empathy write the customer reply? |
| Wrong guess | B00 (WRITER LAW) | "empathy" corrected to "its SKILL.md" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | a skill is a folder with a SKILL.md instruction set Claude reads before acting; the pipeline reads and executes the Steps section in linear order |
| Anchor | the draft-response skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the one job covers (five named situations) and states plainly that anything outside it isn't covered; BCRY states the design's payoff and its limit together (it reads as empathy, but it is a spec that runs the same way every time) — together they cover what the skill delivers and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the draft-response Skill's SKILL.md specifies (the folder/file structure,
the Steps-section pipeline, the linear execute-in-order behavior, and the
exact scope of the one task — drafting a reply across five named
situations) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown framing ("Here is the Teardown moment... What it gets right:
repeatable results. What it bites: anything outside the spec.") is
compressed into NB03, keeping the same underlying fact — the skill's task
is exactly one job (drafting a customer reply across the five named
situations: a product question, an escalation or outage, a delay or
won't-fix, a declined feature request, a billing issue) and nothing beyond
that — stripped of "gets it right / where it bites" verdict language per
the NO JUDGMENT register check; BVDT's verdict facts (repeatable execution,
and the limit that only the file's spec is covered) are merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff — the
source's prompt text was garbled by truncation ("I want to draft a
professional customer-facing response tailored to the situation and rela.")
and is rebuilt here as a concrete, paste-ready, ungarbled prompt carrying
the same request (draft a customer-facing response, this time anchored to
a concrete escalation scenario) plus the source's own flagged clause ("walk
me through what you will do before you do it"); BOUT kept, re-skinned to
the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
