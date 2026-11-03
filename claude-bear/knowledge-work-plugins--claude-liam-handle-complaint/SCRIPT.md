# SCRIPT.md — Draft, Not Send. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-handle-complaint` (Teardown, walks the Anthropic
`handle-complaint` Skill — handles an incoming customer complaint
end-to-end: pulls context, drafts a response, and suggests an operational
fix, with an optional email or ticket ID argument) — question, facts, and
body argument carried over; narration re-registered to Plain (explain,
then stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed handling a complaint means Claude sends the reply itself.
It doesn't — it drafts a response and suggests a fix. So: how do I get
Claude to draft a reply to an angry customer?

*(Text typed on screen: "How do I get Claude / to send a reply / to an
angry customer?" — trigger word "send" corrects to "draft", landing on:
"How do I get Claude to draft a reply to an angry customer?" 57 characters
across 3 lines, comfortably under the family's established-safe 60-char
config, so the same charMs/mistakeRate/hesitate rates clear the TIMING LAW
window with margin to spare.)*

## Body — anatomy, the pipeline, the limit

**NB01 — A folder, not a program** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
handle-complaint — a single SKILL.md file, about two kilobytes. It's the
whole instruction set, written in plain language, with no hidden logic
underneath it. Claude reads it, then acts on what it says. The file is the
program.

**NB02 — How it gets picked up and run** (source B02, pipeline; job-spec
clause folded in from source B00's own quoted description, since B00 is no
longer the beat that carried it)
Its job, word for word: pulls context on the complaint, drafts a response,
and suggests an operational fix — with an optional email or ticket ID as
input. Once triggered, Claude reads the Steps section and runs each one in
order — linear, no branching unless a step says so.

**NB03 — Drafts and suggests, not sends and fixes** (source B03/BVDT,
design tell + verdict — re-registered Teardown → Plain, judgment stripped,
kept as the one fact a general viewer can act on)
Claude's job here is to draft the reply and suggest the fix — not to send
anything or make the fix itself. Run the same complaint through twice, and
you get the same kind of response and the same kind of fix, every time.
But it only covers what the file says — anything the SKILL.md doesn't
spec is outside what this skill does.

## Close

**BCRY — carry-out**
handle-complaint doesn't resolve a complaint — it drafts a response and
suggests a fix, the same way every time; sending the reply and making the
fix are still yours to do.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to handle an incoming customer
complaint — read the handle-complaint skill and walk me through what you
will do before you do it. That clause matters: having Claude explain
itself first, before it acts, is how you actually see the draft and the
fix it's proposing, not just the result.

**BOUT — outro**
Draft, Not Send. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a scope question — will Claude send the reply itself, or hand you a draft and a suggestion? |
| Wrong guess | B00 (WRITER LAW) | "send" corrected to "draft" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the single-file folder anatomy, the job description's own verbs (pulls / drafts / suggests), and the linear Steps pipeline once triggered |
| Anchor | the handle-complaint skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill, and the one running case — an incoming customer complaint) — not a planted-and-paid-off separate case, so there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states both what holds (same complaint, same kind of draft and fix, every time) and what doesn't (anything outside the SKILL.md's spec is outside what it does); BCRY states the same pair as the closing sentence — matching the source's verdict beat, which paired the identical two facts ("Same input, same output, every run" / "only what the file says") |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the handle-complaint Skill's SKILL.md specifies (the single-file structure,
the job description's own verbs — pulls context, drafts a response,
suggests an operational fix, optional email/ticket ID argument — and the
linear Steps execution, same-input/same-output/spec-only limit) — not an
inference about hidden model internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open, quoting the job
description) + B01/B02 (anatomy / pipeline) + B03 (design tell) + BVDT
(verdict) + BHTF (your turn) + BOUT (outro). This redo keeps that same
7-beat shape: B00 replaced 1:1 with BrutalistHesitantWriter (carrying the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01,
B02→NB02 kept as one beat each (NB02 additionally folds in the job-spec
clause the source only quoted inline at B00, since B00 is no longer the
composer-ask beat that carried it); B03's Teardown "design tell" framing
("here is the Teardown moment", "what it gets right / what it bites") and
BVDT's verdict artifact (four bulleted lines restating the skill name, its
job description, the same-input/same-output claim, and the "only what the
file says" limit) are merged into a single NB03 beat, stripped of judgment
language per the NO JUDGMENT register check, and kept as the one fact a
general audience needs and can act on (repeatable draft-and-suggest /
spec-only limit) — BVDT's separate artifact card is not kept as its own
beat, per CARRY-OUT LAW (the verdict facts belong in the single BCRY
sentence, not a bulleted recap); BHTF kept as the your-turn handoff, with
the source's garbled truncation artifact ("I want to handles an incoming
customer complaint end-to-end — pulls context, drafts a resp...") rewritten
to clean grammar ("I want to handle an incoming customer complaint"),
since the source text was a template-substitution artifact cut off
mid-sentence with a grammatical error ("I want to handles"), not a
deliberately authored prompt; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
