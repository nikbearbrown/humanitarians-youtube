# SCRIPT.md — It Doesn't Know Your Brand. It Reads It. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-discover-brand` (Teardown, walks the Anthropic
`discover-brand` Skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

**Source-material note:** the source reel's own narration carries several
unfilled `>` placeholders (in B00, B03, BVDT, BHTF) where the specific job
discover-brand does — and the actual prompt a user would run — were never
written in. The source's `metadata.source_skill` path points at a machine
this build has no access to
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-
work-plugins/partner-built/brand-voice/skills/discover-brand/SKILL.md`),
and a workspace-wide search confirmed no copy of that Skill's actual
SKILL.md exists anywhere under `books/` (checked). A sibling reel in the
same batch, `claude-liam-brand-voice-enforcement` (already redone as
`knowledge-work-plugins--claude-liam-brand-voice-enforcement`), hit the
identical gap for its own Skill and is the template this build follows.

Per the redo contract's "facts must be true and current... when in doubt,
describe behavior generically," the confidently-established generic facts
(a skill is a folder with a SKILL.md Claude reads before acting; the Steps
section runs linearly) are kept as stated. For the one fact the source
never spelled out — what discover-brand's "actual job" specifically
produces — this script uses the plugin-family context that IS available
without guessing: `discover-brand` and `brand-voice-enforcement` are
sibling skills in the same `brand-voice` plugin, and the enforcement
skill's own job (confirmed by its already-built reel) is "check a draft
against whatever rules a SKILL.md-adjacent spec lists." The complementary,
name-implied job of *discover*-brand — reading existing material to derive
that spec in the first place — is stated as an explicit, flagged inference
(NB03's "one flag"), never as confirmed fact. No specific brand, word list,
or output format is invented.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude just knows their brand's voice from training. It
doesn't — it reads what you give it first. So: does Claude already know my
brand's voice?

*(Text typed on screen: "Does Claude\nalready know\nmy brand's voice?" —
trigger word "know" corrects to "read", landing on: "Does Claude already
read my brand's voice?" 3 lines, 33 characters — same short-line, moderate-
charMs shape as the brand-voice-enforcement sibling, kept deliberately
inside the >=9s TIMING LAW window rather than discovered by a failed first
render.)*

## Body — anatomy, pipeline, the actual job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
discover-brand. Its SKILL.md file holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — Steps, in order** (source B02, pipeline)
The instructions are laid out in a Steps section. Claude reads each step in
order and runs it — linear, no branching unless a step says otherwise.

**NB03 — Read, don't guess** (source B03, design tell — re-registered
Teardown → Plain, and the source's unfilled `>` placeholder replaced with
an explicitly flagged inference, per the source-material note above)
Here's the actual job, as its name suggests: it reads material you already
have — your site, your docs — and pulls out the patterns: words you favor,
words you avoid, the tone that keeps showing up. Then it writes that down
as a spec. One flag: the source material never spelled out those
specifics, so that's the skill's name talking, not its file.

## Close

**BCRY — carry-out**
discover-brand doesn't already know your brand's voice — it reads what you
give it and writes that down as a spec. Same material in, same spec out,
every time. The limit is exactly what it was given to read.

**BHTF — your turn**
Your turn. Paste this into Claude: Here are three things I've actually
written — an old email, a project note, and something from my own archive.
Read them and tell me three words I use again and again, one word I
clearly avoid, and one sentence that describes my tone — nothing you can't
point to in the text. That's the same discipline the skill runs on: read
what's actually there, then write it down.

**BOUT — outro**
Claude, Discover Brand. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a knowledge question — does Claude already know a brand's voice, the way a person who's absorbed a style guide would? |
| Wrong guess | B00 (WRITER LAW) | "know" corrected to "read" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a skill is a folder with a SKILL.md Claude reads before acting; the Steps section runs linearly; the actual job (flagged) is reading material you supply and writing down the patterns it finds as a spec |
| Anchor | the discover-brand skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — matches the brand-voice-enforcement sibling's shape exactly |
| Both directions | folded into NB03 + BCRY | NB03 states what gets read (whatever material you actually give it); BCRY states the same design's boundary in the other direction (the limit is exactly what it was given to read, nothing more) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

One inference flag, in NB03: "the actual job" — reading material to derive
a brand-voice spec — is inferred from the skill's name and its sibling
skill's confirmed job (checking a draft against a spec), not read off the
actual `discover-brand/SKILL.md`, which this build has no access to. Every
other claim in the reel is a direct, unhedged description already
established by the source's own B01/B02 (a skill is a folder with a
SKILL.md; Claude reads it before acting; the Steps section runs linearly)
or is a restatement of the same flagged inference at BCRY. Per simple's
ONE-FLAG LAW, exactly one flag, at the moment the leap happens.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right / where it bites" framing is compressed into
NB03 as a plain, flagged mechanism description, per the NO JUDGMENT
register check; BVDT's verdict facts are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff — the source's own
prompt was itself an unfilled `>` placeholder ("I want to >. Read the
discover-brand skill..."), so rather than inventing a call to a specific
Anthropic skill a general viewer likely doesn't have installed, this redo
writes a concrete, paste-ready prompt that exercises the identical
mechanism (read real material you supply, extract the patterns, write them
down) with materials any viewer already has — their own writing, not an
invented brand; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
