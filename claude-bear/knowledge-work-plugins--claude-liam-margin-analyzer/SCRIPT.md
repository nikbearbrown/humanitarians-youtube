# SCRIPT.md — A Plan, Not a Guess. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-margin-analyzer` (Teardown, walks the `margin-analyzer`
Skill) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## Source-facts note (read before the six-move audit)

The source `beat_sheet.json`'s `source_skill` path
(`.../knowledge-work-plugins/small-business/skills/margin-analyzer/SKILL.md`)
does not exist anywhere in this workspace — it only ever existed on the
machine that ran the original batch build. Worse: the source's OWN
narration and Remotion props never got the skill's specific task
description filled in — five of its seven beats carry a literal, un-substituted
`>` placeholder exactly where that description belongs (B00, B03, BVDT,
BHTF's "I want to >."). Comparing against sibling batch reels (`forecast`,
`crm-cleanup`), which DO have their descriptions filled in, confirms this
is a template-substitution defect specific to this one source, not a
stylistic choice — and the toolkit's own audit (`_audit/audit_results.csv`)
already flags this sheet `no-TYPECHECK;no-FACTCHECK`.

Everything else in the source is generic and fully usable: "a skill is a
folder Claude reads before it works," "the pipeline is in the Steps
section, executed in order," "same input, same output every run," "the
limit is only what the file says" — none of that depends on knowing
margin-analyzer's specific business logic, and all of it is carried over
unchanged below.

The one specific fact the source never supplies — *what margin-analyzer
actually checks* — is not invented. Per hai-simple PHASE 1 ("when in doubt,
describe behavior generically"), NB01 names it as an inference from the
skill's name and its `small-business` category only ("going by its name"),
flagged once (ONE-FLAG LAW) and not asserted as confirmed fact anywhere
else in the reel. BHTF's paste-ready prompt is written to be genuinely
runnable without the (non-public, unavailable) margin-analyzer skill
itself, matching the `claude-tag-plugins--claude-liam-config-guide`
sibling's precedent for a source with admin/skill-specific instructions.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude invents its own plan for checking margins. It
doesn't — it follows a written one, a Skill called margin-analyzer. So:
does Claude invent a plan for this, or follow one?

*(Text typed on screen: "Does Claude / invent a plan / for my margins?" —
trigger word "invent" corrects to "follow", landing on: "Does Claude follow
a plan for my margins?")*

## Body — the file, the steps, what repeatable also limits

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
margin-analyzer — built, going by its name, for a small business checking
its profit margins. The SKILL.md file holds the whole instruction set in
plain language, no hidden code. Claude reads the file, then acts on
exactly what it says.

**NB02 — Steps, in order** (source B02, pipeline)
The instructions live in a Steps section, numbered in order. Claude reads
step one, does it, then moves to step two — straight through, no branching
unless a step says otherwise.

**NB03 — Repeatable, and limited** (source B03 + BVDT, design tell +
verdict — merged, re-registered Teardown → Plain)
Here's the part worth knowing: margin-analyzer is a plan, not a guess.
Every run, Claude checks the numbers the same way, in the same order —
that's what makes the result repeatable. It's also the limit: anything the
plan doesn't cover, the skill doesn't do.

## Close

**BCRY — carry-out**
A Skill is a written plan Claude follows, not a fresh guess it invents
each run — the same steps, every time, and nothing beyond what the plan
says.

**BHTF — your turn**
Your turn. Paste this into Claude: I want a repeatable way to check profit
margins across a list of products, using the cost and price for each one.
Write me a short, numbered set of steps — like a Skill file — that says
exactly what to check, in what order, so running it twice on the same
numbers gives the same answer. Then tell me one thing that plan wouldn't
catch.

**BOUT — outro**
A Plan, Not a Guess. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is: does Claude invent its own plan for a task like this? |
| Wrong guess | B00 (WRITER LAW) | "invent" corrected to "follow" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the folder/SKILL.md structure and the numbered, linear Steps section |
| Anchor | the margin-analyzer Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 | states what running the plan guarantees (repeatable, same steps every time) AND what it never does (anything outside the plan) in the same beat — matching the source's B03+BVDT pairing of the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

Exactly one inference flag, at **NB01**: "built, going by its name, for a
small business checking its profit margins." Margin-analyzer's specific
task is inferred from its name and its `small-business` skills category —
the source `SKILL.md` that would confirm it is unavailable to this build
(see "Source-facts note" above). Everywhere else, the reel describes only
the generic Skill mechanism (folder, SKILL.md, ordered steps, repeatable
output, scoped limit), which the source states directly and which this
redo does not need to infer.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02
(anatomy/pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B03's design-tell beat and BVDT's verdict beat — both built around
the same missing task-specific placeholder in the source — are merged into
the single NB03 (repeatable / also the limit), re-registered Teardown →
Plain (the source's "gets it right" / "what it bites" framing is stripped
to a plain mechanism-and-consequence description, per the NO JUDGMENT
register check); BHTF kept as the your-turn handoff, with the source's
skill-specific instruction ("Read the margin-analyzer skill and walk me
through...", which requires a non-public internal skill the viewer cannot
actually run) replaced by a concrete, paste-ready prompt that needs no
special access, so it's actually runnable by any viewer today; BOUT kept,
re-skinned to the Humanitarians AI outro (`OutroSeries`). Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
