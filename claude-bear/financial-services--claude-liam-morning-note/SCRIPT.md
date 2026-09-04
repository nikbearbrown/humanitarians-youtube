# SCRIPT.md — A File, Not a Mode. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-morning-note` (Teardown, walks the Anthropic
`morning-note` Skill — drafts concise 7am morning-meeting notes from
overnight developments, trade ideas, and key events for coverage stocks) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed morning notes came from a special trading mode built into
Claude. They don't — they come from a file it reads. So: is there a special
file for morning notes in Claude?

*(Text typed on screen: "Is there a / special mode / for morning notes / in
Claude?" — trigger word "mode" corrects to "file", landing on: "Is there a
special file for morning notes in Claude?" Params mirror the established
fixed-pattern values from the `claude-plugins-official--claude-liam-agent-
development` sibling (42ms/char, 4% mistakeRate, 8% hesitateBetween, 26%
jitter) on an even shorter text (52 forward chars across 4 lines + the
"mode"->"file" swap), so the typing performance has comfortable margin
inside the narration's ~9-10s window; verified by ffprobe + frame pull
after render per TIMING LAW.)*

## Body — anatomy, pipeline, the design tell

**NB01 — SKILL.md is the program** (source B01, anatomy)
A skill is one file Claude reads before it works. This one is morning-note —
draft concise notes on overnight developments, trade ideas, and key events,
timed for the 7am morning meeting: tight, opinionated, actionable. It wakes
up on plain phrases — 'morning note,' 'what happened overnight,' 'trade
idea' — say one of those, and Claude reads the file before it drafts
anything. The file is the program.

**NB02 — Read, then execute in order** (source B02, pipeline)
Once triggered, Claude reads that file top to bottom and executes each step
in order — no branching, unless a step itself says to branch. Read the
overnight news, name the trade ideas, note the key events for the coverage
list, then return one tight note, ready for the 7am meeting. Same steps,
same order, every single time.

**NB03 — Repeatable, but bounded** (source B03, design tell — re-registered
Teardown → Plain: kept as a plain mechanism-and-consequence description,
stripped of "gets it right / where it bites" framing)
That's the design tell: morning-note is a specification written as
instructions, not a model improvising around the news. Same input, same
output, every run — which is exactly what a trading desk needs at 7am. But
it only covers what the file actually says. Ask for something outside that
scope, and the skill doesn't stretch to reach it.

## Close

**BCRY — carry-out**
A skill is a file Claude reads, not a mode it switches into — so it drafts
the same note, the same way, every single morning. The best skill file in
the world still only covers what it actually spells out.

**BHTF — your turn**
Your turn. Paste this into Claude: Write me a SKILL.md that turns overnight
headlines, my watchlist, and yesterday's closing prices into one tight
morning note — then walk me through what you'll do, step by step, before
you draft anything. Watch whether what it describes reads like a fixed set
of steps, or like it's freelancing past what you actually asked for. That's
the real test of whether a skill file is doing its job.

**BOUT — outro**
A File, Not a Mode. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a "does Claude have a special mode" question — is a morning trading note produced by some built-in market sense, or by following a file? |
| Wrong guess | B00 (WRITER LAW) | "mode" corrected to "file" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | what SKILL.md contains and what wakes it up (NB01); how Claude reads and executes it, linearly, step by step (NB02) |
| Anchor | the morning-note skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete boundary the spec-as-instructions design creates (same input, same output, but only within what the file says); BCRY states the design's payoff and its failure mode together (a well-written skill repeats reliably, but the best skill file in the world still can't reach past what it spells out) — together they cover what the file guarantees and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the morning-note Skill's SKILL.md specifies (drafting concise notes from
overnight developments, trade ideas, and key events; the 7am-meeting format;
the trigger phrases; the linear read-then-execute pipeline; the
same-input/same-output repeatability; the file's scope as its only
boundary) — not an inference about hidden model internals or trading
judgment. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design-tell teardown moment) + BVDT (verdict) + BHTF
(your turn) + BOUT (outro). This redo keeps that same 7-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02
kept as one beat each, with the source's trigger-phrase list (originally
stated only inside source B00's own narration, which this redo replaces
entirely) folded into NB01 so that fact isn't lost; B03's teardown framing
("what it gets right" / "what it bites") is compressed into NB03, stripped
to a plain mechanism-and-consequence description per the NO JUDGMENT
register check, keeping the same two facts (repeatable results; bounded to
the spec) without the Teardown verdict language; BVDT's verdict facts (same
input → same output every run; the limit is only what the file specifies)
are merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff — the source's own prompt text was garbled by truncation
("Draft concise morning meeting notes summarizing overnight developments,
trade id...") and assumed access to a proprietary financial-services plugin
skill no general viewer has, so it was rewritten as an equivalent,
independently runnable prompt: asking Claude to draft its own morning-note
SKILL.md from three inputs any viewer can supply themselves (headlines,
watchlist, yesterday's closes) and narrate its plan before acting — same
teaching point (a skill's reliability comes from being a legible, checkable
file, not a black box), actually paste-ready today; BOUT kept, re-skinned
to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT =
7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
