# SCRIPT.md — Claude, Daily Briefing. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-daily-briefing` (Teardown, walks the Anthropic
`daily-briefing` sales Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin (OutroSeries + OutroCTA, per this family's current
8-beat convention).

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude already remembered their meetings for a daily
briefing. It doesn't — it reads them fresh, from what you type or connect,
every time. Does Claude read my meetings for a briefing?

*(Text typed on screen: "Does Claude / REMEMBER my meetings / for a
briefing?" — trigger word "REMEMBER" corrects to "read", landing on: "Does
Claude read my meetings for a briefing?")*

## Body — anatomy, pipeline, scope

**B01 — A skill is a folder.** (source B01, anatomy — carried over
near-verbatim; already Plain register, no judgment to strip)
A skill is a folder Claude reads before it works. This one is
daily-briefing. The SKILL.md file holds the full instruction set in plain
language — no hidden logic. Claude reads it, then acts. The file is the
program.

**B02 — How the skill works.** (source B02, pipeline — carried over
near-verbatim)
The pipeline sits in the Steps section. Claude reads each step in order,
then runs it. Linear — no branching unless a step says so.

**B03 — Standalone, or supercharged.** (source B03 "design tell" + BVDT
"verdict" merged and re-registered Teardown → Plain: the source's "Here is
the Teardown moment... what it gets right / what it bites" framing is
stripped to a plain mechanism-and-consequence description)
The scope is specific. daily-briefing works standalone once you tell Claude
your meetings and priorities in chat. Connect your calendar, CRM, and
email, and it's supercharged — reading them directly instead of waiting to
be told. Either way, the same input produces the same briefing every time;
ask for something the file doesn't cover, and the skill has nothing to say
about it.

## Close

**BCRY — carry-out**
Claude doesn't remember your day for a briefing — it reads what you give
it, standalone or connected, and does the same thing with it every time.

**BHTF — your turn**
Your turn. Here's the prompt — read it with me. Read the daily-briefing
skill in this folder. Before you write my briefing, tell me exactly what
you're using — what I told you, versus what you'd need connected — and how
you're ranking it, before you do it.

**BOUT — outro series**
Claude, Daily Briefing.

**BCTA — outro cta**
…Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a memory question — does Claude already know your day, or does it read it fresh? |
| Wrong guess | B00 (WRITER LAW) | "REMEMBER" corrected to "read" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented |
| Mechanism | B01–B02 | the SKILL.md file is what Claude reads (not memory); the Steps section runs linearly, same request in, same kind of output out |
| Anchor | the daily-briefing skill itself, named at B00 and never dropped through B01–B03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into B03 + BCRY | B03 states both modes the design supports (standalone from what you tell it, supercharged once connected) and the one thing it can't do (anything outside the file); BCRY states the mechanism's payoff and its boundary together |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the daily-briefing Skill's SKILL.md specifies (the single-file anatomy, the
linear Steps pipeline, the standalone/supercharged scope, and the
same-input-same-output guarantee) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps B00→B00 (WRITER LAW replacement), B01→B01, B02→B02
(both carried over near-verbatim — the source's own anatomy/pipeline
narration was already Plain-register, no judgment to strip), B03+BVDT
merged into a single B03 (the source's separate "design tell" and
"verdict" beats covered the same standalone/supercharged scope and
same-input-same-output guarantee from two angles; Plain register keeps one
mechanism beat, per CARRY-OUT LAW folding the verdict facts into BCRY
instead of a second recap beat), BHTF kept with the source's own prompt
structure ("read the skill... walk me through what you will do before you
do it") made concretely paste-ready, and BOUT split into BOUT (OutroSeries,
title restate) + BCTA (OutroCTA, "…Liam, in for Bear." + handle) per this
family's current 8-beat close convention (see sibling
`knowledge-work-plugins--claude-liam-crm-cleanup`, built earlier the same
day). Total: B00 + B01 + B02 + B03 + BCRY + BHTF + BOUT + BCTA = 8 beats.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
