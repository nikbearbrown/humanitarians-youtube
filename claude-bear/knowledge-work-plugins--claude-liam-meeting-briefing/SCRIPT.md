# SCRIPT.md — A Written Plan, Not a Guess. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-meeting-briefing` (Teardown, walks the Anthropic
`meeting-briefing` knowledge-work-plugins Skill) — question, facts, and
body argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude improvises a plan when you ask for a meeting
briefing. It doesn't — it follows one, already written. So: does Claude
follow a plan to brief me for a meeting?

*(Text typed on screen: "Does Claude / improvise a plan / to brief me / for
a meeting?" — trigger word "improvise" corrects to "follow," landing on:
"Does Claude follow a plan to brief me for a meeting?" Same slot both ways —
"[improvise/follow] a plan" — so the correction reads as a real second
thought, not a random edit.)*

## Body — anatomy, the pipeline, the consistency-and-limit fact

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is
meeting-briefing — prepare structured briefings for meetings with legal
relevance, and track the resulting action items. The instructions live in
one file, SKILL.md, written in plain language, no hidden logic. Claude
reads it, then acts. The file is the program.

**NB02 — The plan is the Steps section** (source B02, pipeline)
The plan itself lives in a Steps section. Claude reads each step in order
and executes it — prepare the briefing, surface the legal context, hand
back the action items to track. Linear: no branching, no skipping ahead,
unless a step itself says so.

**NB03 — Same steps, same kind of result** (source B03 design tell + BVDT
verdict, re-registered Teardown → Plain, kept as the single most teachable
fact rather than the full "gets it right / where it bites" list)
Because the steps are fixed, the same meeting-briefing request produces the
same kind of briefing every time — same sections, same action-item
tracking, run after run. What it can't do is step outside that file:
anything the SKILL.md doesn't spell out isn't part of the plan.

## Close

**BCRY — carry-out**
A Skill isn't Claude guessing what a good briefing looks like — it's a
written plan Claude follows step by step, and the briefing only ever
covers what that plan spells out.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a meeting coming up on
[your topic]. Before you prepare a briefing, walk me through your plan as
a numbered list of steps — then execute it. That two-part ask is the whole
lesson: a plan you can read before Claude runs it, not an improvisation you
only see after.

**BOUT — outro**
A Written Plan, Not a Guess. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is whether Claude improvises the briefing on the spot, or works from something already written |
| Wrong guess | B00 (WRITER LAW) | "improvise" corrected to "follow" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the SKILL.md file as the instruction set (NB01); the Steps section as the linear plan Claude actually executes (NB02) |
| Anchor | the meeting-briefing skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the consistency the fixed steps buy (same kind of briefing every run) and the limit they impose (nothing outside the file) together; BCRY restates both in one sentence — matching the source's verdict beat, which paired the same two facts ("same output every run" / "know the limit") |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the meeting-briefing Skill's SKILL.md specifies, per the source narration
(a SKILL.md file Claude reads before acting; a Steps section executed in
order; the same input producing the same kind of output; the limit being
only what the file specifies) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's "design tell" (what it gets right / where it bites) and BVDT's
verdict recap are merged into NB03, keeping only the single fact a general
audience needs and can act on — the concrete consistency-and-limit pair —
and dropping Teardown's judgment framing ("gets it right," "where it
bites," "makes Claude execute... reliably") per the NO JUDGMENT register
check; BVDT's facts are then restated once more, compressed to one
sentence, as BCRY's carry-out rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, but
the source's prompt ("Read the meeting-briefing skill and walk me through
what you will do before you do it") assumed the viewer already has that
specific internal Skill file installed, so it is replaced with a
functionally identical but genuinely runnable prompt — ask Claude to state
its plan as numbered steps before executing, on any meeting the viewer
actually has — teaching the same lesson (a plan you can read before Claude
runs it) without depending on a Skill most viewers don't have; BOUT kept,
re-skinned to the Humanitarians AI outro with a new title restating the
carry-out rather than the source's literal "Claude, Meeting Briefing."
title. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
