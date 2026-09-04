# SCRIPT.md — Claude, K12 Lesson Differentiation. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-k12-lesson-differentiation` (Teardown, walks the
Anthropic `k12-lesson-differentiation` Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone wonders if tiering a lesson for three levels means writing it
separately. It doesn't — one lesson, tiered three ways. So: when Claude
tiers a lesson for three levels, does it write one shared version?

*(Text typed on screen: "When Claude tiers / a lesson for three levels, /
does it write separate?" — trigger word "separate" corrects to "one shared
version", landing on: "When Claude tiers a lesson for three levels, does it
write one shared version?" Component note: `triggerWords`/`replacementWords`
must each be a single whitespace token — the component matches against one
split token's punctuation-stripped core, so a multi-word trigger like the
first draft's "three lessons" never matches and the correction silently
never fires. First render caught this at Gate V frame-pull; fixed by making
"separate" — the single last content word before the terminal "?" — the
trigger, confirmed correcting cleanly on the second render.)*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it works. This one is called
k12-lesson-differentiation. Its SKILL.md file holds the full instruction
set, in plain language — no hidden logic. Claude reads it, then acts. The
file is the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and executes it — read the file, execute each step, return the result.
Linear: no branching, unless a step says otherwise.

**NB03 — One source, three tiers** (source B03, design tell — re-registered
Teardown → Plain, and re-derived from the skill's actual purpose text rather
than kept as the source's generic boilerplate; see Beat-count note below)
One design choice matters most: all three tiers, and the teacher's own plan,
render from a single material-source file. The facts get written once.
Change a number in the source and every tier updates together — nothing to
accidentally drift between the below-level version and the above-level
version.

## Close

**BCRY — carry-out**
Claude isn't writing three different lessons — it's tiering one shared
lesson three ways, from a single source file, so the three versions can't
drift apart.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a fifth grade fractions lesson,
and my students read at three different levels. Read the
k12-lesson-differentiation skill, and before you build anything, walk me
through what you'll produce and how the tiers will stay consistent with
each other.

**BOUT — outro**
Claude, K12 Lesson Differentiation. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the standard differentiation assumption — tiering for three levels means writing them separately |
| Wrong guess | B00 (WRITER LAW) | "separate" corrected to "one shared version" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes steps linearly; one specific design fact governs how the three tier documents and the teacher plan all render from one shared source |
| Anchor | the k12-lesson-differentiation Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "tiering one shared lesson, from a single source, so the versions can't drift apart" states both what the mechanism does (produce three consistent tiers) and what it rules out (independent drafts that could diverge), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the Skill's SKILL.md specifies (a folder, one file, a Steps section executed
in order, and the single material-source-JSON design that keeps the three
tier documents from drifting) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02/B03 (anatomy /
pipeline / design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) —
matching the shape of the `claude-for-legal--claude-liam-cease-desist`
sibling exactly (same generic `SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism` / `ClaudeVerdictArtifact`
/ `ClaudeComposerAsk` / `ClaudeTitleOutro` template family). This redo keeps
that same 7-beat shape: B00 replaced 1:1 with BrutalistHesitantWriter
(carrying the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat); B01→NB01, B02→NB02 kept as one beat each, Teardown framing stripped
to a plain mechanism description.

B03→NB03 required one substantive change beyond re-registration: the
source's B03 narration ("Here is the Teardown moment... What it gets right:
repeatable results. What it bites: anything outside the spec.") is generic
template filler shared across the whole `claude-liam-<skill>` batch, not a
skill-specific design fact — re-registering its wording to Plain alone
would have produced a beat that teaches nothing concrete. The source
skill's own purpose text (quoted in full in source B00's narration) does
carry one specific, checkable design fact: the skill "renders [outputs]
from one material-source JSON via bundled scripts (shared content is
written once so tiers cannot drift)". NB03 uses that fact instead — same
beat slot, same "design tell" function in the six-move audit, but drawn
from the skill's actual documented behavior rather than the batch
template's boilerplate verdict language. This is a content substitution
within the locked beat count, not an added beat, and it does not change the
question, the carry-out, or the body's argument shape.

BVDT's two verdict facts (reliable/consistent execution, and the
single-source limit that makes that consistency possible) are merged into
the single BCRY carry-out sentence rather than kept as a separate
artifact-card beat, since Plain register carries one carry-out sentence,
not a bulleted verdict (CARRY-OUT LAW); BHTF kept as the your-turn handoff,
with the source's broken bracket-fill placeholder ("I want to adapts an
existing k-12 lesson (math, ela, science, or social studies) for stude...")
replaced by a concrete, grammatical, paste-ready scenario so the prompt is
actually runnable today; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism` / `ClaudeVerdictArtifact`
/ `ClaudeComposerAsk` / `ClaudeTitleOutro` patterns) with B00 as the
composer-ask cold open (REMOTION, not AI-VIDEO — the source never called a
generation service). NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00's cold open, which this redo replaces per hai-simple's mandate anyway.
The `SkillTeardownAnatomy`/`SkillTeardownPipeline`/`SkillTeardownMechanism`
components are not registered in this toolkit's scene library, so
NB01–NB03 are built fresh as GRAPHIC (Manim) beats on the same generic
"chip row" template used by the `claude-for-legal--claude-liam-cease-desist`
sibling (mechanism, colors, and GATE T exemption notes copied verbatim),
carrying the same teaching point per beat rather than re-slating the
source's unavailable components.
