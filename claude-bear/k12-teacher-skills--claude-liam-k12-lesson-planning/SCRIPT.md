# SCRIPT.md — Claude, K12 Lesson Planning. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-k12-lesson-planning` (Teardown, walks the Anthropic
`k12-lesson-planning` Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone wonders if Claude plans a lesson by improvising in the moment. It
doesn't — it follows a written set of steps. So: when Claude plans a lesson
for your class, does it follow written steps?

*(Text typed on screen: "When Claude plans / a lesson for my class, / does
it improvise?" — trigger word "improvise" corrects to "follow written
steps", landing on: "When Claude plans a lesson for my class, does it
follow written steps?" Component note: `triggerWords`/`replacementWords`
must each be a single whitespace token — the component matches against one
split token's punctuation-stripped core, so a multi-word trigger never
matches and the correction silently never fires. This exact defect was
caught and fixed on the `k12-lesson-differentiation` sibling built earlier
in this batch; "improvise" here is chosen as a single token immediately
before the terminal "?", so this reel does not repeat it.)*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it works. This one is called
k12-lesson-planning. Its SKILL.md file holds the full instruction set, in
plain language — no hidden logic. Claude reads it, then acts. The file is
the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and executes it — read the file, execute each step, return the result.
Linear: no branching, unless a step says otherwise.

**NB03 — Not only prose** (source B03, design tell — re-registered
Teardown → Plain, and re-derived from the skill's actual file manifest
rather than kept as the source's generic boilerplate; see Beat-count note
below)
One thing is worth knowing about this particular skill: it isn't only
prose. Alongside SKILL.md, the folder ships a references folder and a
scripts folder — supporting material and runnable code the skill uses
directly. Where a step can run as code, it does, so the same step produces
the same result, not a freshly-reasoned answer typed out each time.

## Close

**BCRY — carry-out**
Claude isn't improvising the lesson plan — it's following the
k12-lesson-planning skill's written steps, the same way every time. Ask for
something those steps don't cover, and you get Claude's own judgment, not
the skill's playbook.

**BHTF — your turn**
Your turn. Paste this into Claude: I teach a seventh grade science class and
need a full lesson plan on the water cycle. Read the k12-lesson-planning
skill, and before you build anything, walk me through the steps you'll
follow and what you'll hand back.

**BOUT — outro**
Claude, K12 Lesson Planning. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the standard assumption about any AI writing task — that Claude improvises a lesson plan fresh, the way a person free-associates |
| Wrong guess | B00 (WRITER LAW) | "improvise" corrected to "follow written steps" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes steps linearly; one specific design fact — the folder ships reference material and scripts alongside the prose, so some steps run as code rather than being reasoned out fresh |
| Anchor | the k12-lesson-planning Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "the same way every time... ask for something those steps don't cover, and you get Claude's own judgment" states both what the mechanism does (repeatable execution inside the spec) and what it does not do (cover requests outside the spec), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the Skill's own folder structure specifies (a folder, one instruction file,
a Steps section executed in order, and a references/scripts split alongside
the prose) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02/B03 (anatomy /
pipeline / design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) —
the same generic `SkillTeardownAnatomy` / `SkillTeardownPipeline` /
`SkillTeardownMechanism` / `ClaudeVerdictArtifact` / `ClaudeComposerAsk` /
`ClaudeTitleOutro` template family used across the whole `claude-liam-<skill>`
batch (confirmed identical in shape to the `k12-lesson-differentiation` and
`claude-for-legal--claude-liam-cease-desist` siblings). This redo keeps that
same 7-beat shape: B00 replaced 1:1 with BrutalistHesitantWriter (carrying
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat);
B01→NB01, B02→NB02 kept as one beat each, Teardown framing stripped to a
plain mechanism description.

B03→NB03 and BVDT required a content substitution beyond re-registration.
Unlike the `k12-lesson-differentiation` sibling — where the source's own
B00 narration happened to quote the skill's real purpose text ("renders
[outputs] from one material-source JSON...") that could be re-derived into
a specific design fact — this source's B00/B03/BVDT/BHTF narration carries
literal, unfilled `>` placeholder tokens where a per-skill fact should have
been substituted (a broken batch-build artifact, not a stylistic choice):
e.g. B03 reads "Claude's job: >. What it gets right: repeatable results.
What it bites: anything outside the spec." with the `>` never filled, and
BVDT reads "The SKILL.md is the spec — >." the same way. The actual
`k12-lesson-planning/SKILL.md` this batch was built from
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/...`) does
not exist on this machine, so its specific pedagogical content cannot be
read or verified — inventing lesson-planning-specific claims to fill the
gap would violate the no-fabrication rule.

NB03 instead uses the one fact about this skill that IS real, specific, and
already present (not a placeholder) in the locked source script's own B01
file listing: the folder contains not just `SKILL.md` (29k) but also a
`references/` folder and a `scripts/` folder (4 files total). This is a
generically-true, checkable mechanism claim about how Claude Skills work
(instructions plus runnable code and reference material, not prose alone)
rather than an invented specific about lesson-planning pedagogy — same beat
slot, same "design tell" function in the six-move audit, drawn from the
source's own verified file manifest.

BVDT's two non-broken verdict facts (repeatable execution: "same input, same
output, every run"; and the spec limit: "only what the file says") ARE real
and generic-true, so they carry forward into the single BCRY carry-out
sentence rather than being kept as a separate artifact-card beat, since
Plain register carries one carry-out sentence, not a bulleted verdict
(CARRY-OUT LAW). BHTF kept as the your-turn handoff, with the source's
broken bracket-fill placeholder ("I want to >. Read the k12-lesson-planning
skill and walk me through what you will do before you do it.") replaced by
a concrete, grammatical, paste-ready scenario so the prompt is actually
runnable today. BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro` patterns), never a generation
call. NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's cold
open, which this redo replaces per hai-simple's mandate anyway. The
`SkillTeardownAnatomy`/`SkillTeardownPipeline`/`SkillTeardownMechanism`
components are not registered in this toolkit's scene library, so
NB01–NB03 are built fresh as GRAPHIC (Manim) beats on the same generic
"chip row" template used by the `k12-lesson-differentiation` sibling
(mechanism, colors, and GATE T exemption notes copied verbatim), carrying
the same teaching point per beat rather than re-slating the source's
unavailable components.
