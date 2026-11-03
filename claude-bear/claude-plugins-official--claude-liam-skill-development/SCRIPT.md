# SCRIPT.md — The File Is the Program. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-skill-development` (Teardown, walks the Anthropic
`skill-development` Claude Code plugin-dev Skill — the meta-skill for
building Skills) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed building a Skill means writing code Claude runs. It
doesn't — it means writing instructions Claude reads. So: how do I write a
new Skill for Claude?

*(Text typed on screen: "How do I code / a new Skill / for Claude?" —
trigger word "code" corrects to "write", landing on: "How do I write a new
Skill for Claude?" Shorter text (39 chars, 3 lines) than the family's
established-safe agent-development config (60 chars), so the same
charMs/mistakeRate/hesitate rates that cleared that reel's TIMING LAW with
margin to spare clear this one with more margin still.)*

## Body — anatomy, the pipeline, the limit

**NB01 — A folder, not a program** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
skill-development — the skill for building skills. Inside: a SKILL.md file,
about twenty-two kilobytes, and a references folder alongside it. The
SKILL.md is the whole instruction set, written in plain language, with no
hidden logic underneath it. Claude reads the file, then acts on what it
says. The file is the program.

**NB02 — How it gets picked up and run** (source B02, pipeline)
Two things have to happen before any of that runs. First, the SKILL.md
carries a description stating when it applies — for this skill, that's
wanting to create a skill, add one to a plugin, write a new one, improve a
skill's description, organize its content, or get guidance on skill
structure. When a request matches that, Claude reads the file. Then it
executes the Steps section in order, top to bottom — linear, no branching
unless a step says so.

**NB03 — Only what the file says** (source B03/BVDT, design tell +
verdict — re-registered Teardown → Plain, judgment stripped, kept as the
one fact a general viewer can act on)
Because it's plain instructions and not code, skill-development runs the
same way on the same request every time — repeatable, not improvised. But
that reliability has a matching edge: nothing hidden fills in for what the
file doesn't cover. Ask for something the SKILL.md doesn't describe, and
there's no fallback logic underneath it to catch you — the file's words are
the entire boundary of what happens.

## Close

**BCRY — carry-out**
A Skill isn't code Claude runs — it's plain instructions Claude reads and
follows itself. So it only ever does exactly what the words on the page
say, nothing more and nothing hidden.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to create a skill — read the
skill-development skill and walk me through what you will do before you do
it. That clause matters: having Claude explain itself first, before it
acts, is how you actually see the instructions it's following, not just
the result.

**BOUT — outro**
The File Is the Program. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a build question — do you code a Skill, or write one? |
| Wrong guess | B00 (WRITER LAW) | "code" corrected to "write" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the folder/SKILL.md/references anatomy, the description's trigger-match role, and the linear Steps pipeline once triggered |
| Anchor | the skill-development skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill, self-referentially the very skill this pipeline used to build this video) — not a planted-and-paid-off separate case, so there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states both what holds (same request, same result, every time) and what doesn't (nothing hidden covers a request the file doesn't describe); BCRY states the same pair as the closing sentence — matching the source's verdict beat, which paired the identical two facts ("repeatable results" / "anything outside the spec") |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the skill-development Skill's SKILL.md specifies (the SKILL.md + references
folder structure, the plain-language/no-hidden-logic instruction format,
the description's trigger-match role, the linear Steps execution, and the
same-input/same-output/only-what's-written limit) — not an inference about
hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "design tell" framing ("here is the Teardown moment",
"what it gets right / what it bites") and BVDT's verdict artifact (four
bulleted lines restating the skill name, its trigger description, the
same-input/same-output claim, and the "only what the SKILL.md specifies"
limit) are merged into a single NB03 beat, stripped of judgment language
per the NO JUDGMENT register check, and kept as the one fact a general
audience needs and can act on (repeatable results / only what's written) —
BVDT's separate artifact card is not kept as its own beat, per CARRY-OUT
LAW (the verdict facts belong in the single BCRY sentence, not a bulleted
recap); BHTF kept as the your-turn handoff, with the source's already
generic, already-runnable prompt structure ("I want to [do X] — read the
skill-development skill and walk me through what you will do before you do
it") carried over, filled in with the same "create a skill" trigger phrase
the description itself uses rather than the source's garbled inline
clause; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
