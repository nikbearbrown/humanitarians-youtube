# SCRIPT.md — Follows the File, Not Its Own Reasoning. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-comps-analysis` (Teardown, walks the anatomy of the
Anthropic `comps-analysis` Skill — a `market-researcher` plugin Skill,
financial-services family) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude reasons through a comps analysis, like an analyst
would. It doesn't — it follows a written file, step by step. So: when
Claude runs a comps analysis, does it follow the steps?

*(Text typed on screen: "When Claude runs / a comps analysis, / does it
reason / through the steps?" — trigger word "reason" corrects to "follow",
landing on: "When Claude runs a comps analysis, does it follow the
steps?")*

## Body — anatomy, pipeline, the spec's shape

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
comps-analysis. The SKILL.md file inside it is the full instruction set —
plain language, no hidden logic. Claude reads it, then acts. The file is
the program.

**NB02 — Steps, in order** (source B02, pipeline)
The actual pipeline lives in the file's Steps section. Claude reads each
step and executes it, one at a time, in the order written. Linear — it
doesn't branch unless a step tells it to.

**NB03 — Spec, not suggestion** (source B03 + BVDT, Teardown compressed to
Plain: the "gets it right / where it bites" framing is dropped; the
underlying fact is kept)
That's what makes comps-analysis a specification rather than a suggestion.
Run it on the same input twice and the same steps produce the same output,
both times. But step outside what the file actually says, and there's
nothing written down to fall back on.

## Close

**BCRY — carry-out**
Inside a Skill, Claude follows the written steps — it doesn't reason its
own way through the task. That's why the same input gets the same output
every time, and never more than the file says.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to run a comps analysis on a
public company. Read the comps-analysis skill and walk me through what you
will do before you do it. That last clause matters — asking Claude to
explain first, before it runs, is what actually shows you the steps the
file wrote for it.

**BOUT — outro**
Follows the File, Not Its Own Reasoning. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanism question — does Claude reason through a task like an analyst, or execute a written procedure? |
| Wrong guess | B00 (WRITER LAW) | "reason" corrected to "follow" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the file/folder anatomy (SKILL.md = the program) and the actual execution model (Steps section, read in order, linear, no branching unless told) |
| Anchor | the comps-analysis skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the design guarantees (same input, same output) and what it doesn't cover (outside the file, nothing) in the same beat; BCRY restates both halves as one sentence pair — together they cover what following-the-file buys you and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim describes what the
comps-analysis Skill's own file structure specifies (a folder containing a
SKILL.md instruction set, a Steps section executed in order, and the
consequence that identical input yields identical output because nothing
outside the file is consulted) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "design tell" framing ("what it gets right: repeatable
results. What it bites: anything outside the spec") is compressed into
NB03 as a plain mechanism-and-consequence statement, stripped of the
strengths/gaps verdict framing per the NO JUDGMENT register check; BVDT's
verdict facts (same input → same output every run; limited to what the
file says) are merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as
the your-turn handoff — the source's prompt had an unfilled template slot
("I want to │. Read the comps-analysis skill and walk me through what you
will do before you do it"), which this redo fills with a concrete,
paste-ready task ("I want to run a comps analysis on a public company")
consistent with the source's generic, no-setup-required intent; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

**Source defect, logged and worked around, not silently carried over:** the
source `beat_sheet.json`'s narration for B00, B03, BVDT, and BHTF contains
a literal unfilled template placeholder character (`│`) where a
comps-analysis-specific clause was evidently meant to be substituted by
whatever batch script generated the source and never was (confirmed by:
`PEDAGOGY.md` in the source dir reads only "Batch build — skill teardown
format"; the `source_skill` path in the source sheet's metadata points to
`/Users/bear/Documents/CoWork/.../comps-analysis/SKILL.md`, which does not
exist on this machine, so the specific missing clause cannot be recovered
or verified). Rather than inventing unverifiable comps-analysis-specific
mechanics (e.g. which financial multiples it computes) to fill that gap,
this redo kept every beat's teaching point at the level the source actually
supports without the placeholder — the generic Skill-execution facts
(folder, SKILL.md, Steps section, linear execution, determinism, the
file-bound limit) — and filled BHTF's placeholder with a generic, plausible
task ("run a comps analysis on a public company") rather than a specific
one, since the source never specified which task the missing clause named.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
