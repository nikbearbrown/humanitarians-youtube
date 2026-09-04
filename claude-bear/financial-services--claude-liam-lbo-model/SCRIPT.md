# SCRIPT.md — Fills the Template, Doesn't Design the Deal. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-lbo-model` (Teardown, walks the anatomy of the
Anthropic `lbo-model` Skill — a `model-builder` plugin Skill,
financial-services family) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude designs an LBO model from scratch. It doesn't — it
fills in a template's formulas and checks them. So: when Claude runs the
LBO model skill, does it fill the model?

*(Text typed on screen: "When Claude runs / the LBO model skill, / does it
design / the model?" — trigger word "design" corrects to "fill", landing
on: "When Claude runs the LBO model skill, does it fill the model?")*

## Body — anatomy, pipeline, the three concrete actions

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is lbo-model.
The SKILL.md file inside it is the full instruction set — plain
language, no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — Steps, in order** (source B02, pipeline)
The actual pipeline lives in the file's Steps section. Claude reads each
step and executes it, one at a time, in the order written. Linear — it
doesn't branch unless a step tells it to.

**NB03 — Fills, validates, formats** (source B03 + BVDT, Teardown
compressed to Plain: the "gets it right / where it bites" framing is
dropped; the source's own three concrete actions are kept and made the
teaching point)
Concretely, that means three things: it fills in the template's formulas,
it validates the calculations against each other, and it checks the
formatting against a professional standard. And because it reads the
template's own structure first, it can do that on whatever LBO template
you hand it — not just one fixed layout.

## Close

**BCRY — carry-out**
Inside the LBO-model skill, Claude fills in a template's formulas and
validates them — it doesn't design the deal itself. That's why it works
on whatever template you hand it, and never beyond what that template
specifies.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to fill in an LBO model
template for a leveraged buyout deal. Read the lbo-model skill and walk
me through what you will do before you do it. That last clause matters —
asking Claude to explain first, before it runs, is what actually shows
you the steps the file wrote for it.

**BOUT — outro**
Fills the Template, Doesn't Design the Deal. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanism question — does Claude design the deal model itself, or complete a written procedure against an existing template? |
| Wrong guess | B00 (WRITER LAW) | "design" corrected to "fill" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | the file/folder anatomy (SKILL.md = the program), the execution model (Steps section, read in order, linear, no branching unless told), and the three concrete actions the source names (fill formulas, validate calculations, check formatting) plus the template-agnostic reading step that makes those three portable across templates |
| Anchor | the lbo-model skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill does (fills, validates, formats) and the boundary that makes it portable (reads the template's structure first) in the same beat; BCRY restates the core distinction (fills/validates vs. designs) and its consequence (works on any template, bounded by that template) as one sentence pair — matching the source's verdict beat, which paired the same two kinds of fact |
| Carry-out | BCRY | one sentence pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim describes what the
`lbo-model` Skill's own description states directly (a folder containing
a SKILL.md instruction set, a Steps section executed in order, and the
three concrete actions — filling in formulas, validating calculations,
checking formatting — that adapt to any template structure) — not an
inference about hidden model internals or the skill's actual Excel
mechanics beyond what its own description specifies. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "design tell" framing ("What it gets right: repeatable
results. What it bites: anything outside the spec.") is compressed into
NB03 as a plain mechanism statement built from the source's own three
named actions, stripped of the strengths/gaps verdict framing per the NO
JUDGMENT register check; BVDT's verdict facts (same input → same output
every run; limited to what the file says) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff — the
source's prompt had a broken template substitution ("I want to this
skill should be used when completing lbo (leveraged buyout) model
templates. Read the lbo-model skill..."), which this redo fills with a
concrete, paste-ready task ("I want to fill in an LBO model template for
a leveraged buyout deal") consistent with the source's generic,
no-setup-required intent; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching
the source exactly.

**Source defect, logged and worked around, not silently carried over:**
the source `beat_sheet.json`'s narration for BHTF reads "I want to this
skill should be used when completing lbo (leveraged buyout) model
templates. Read the lbo-model skill and walk me through what you will do
before you do it" — a batch template evidently substituted the skill's
own frontmatter description clause directly into the "I want to ___"
slot instead of a task, producing broken grammar. The same batch defect
also truncates the description mid-word in source B03 ("...for privat").
Confirmed against the source dir's `PEDAGOGY.md` (logs only "Batch build
— skill teardown format", no detail) and the source sheet's
`source_skill` path (`/Users/bear/Documents/CoWork/.../lbo-model/SKILL.md`),
which does not exist on this machine, so the skill's full SKILL.md body
cannot be recovered or verified beyond the frontmatter description
already embedded (complete) in the source's own narration. Rather than
inventing unverifiable lbo-model-specific mechanics (which cells it
writes, which template variants it recognizes) to fill the gap, this redo
kept every beat's teaching point at the level the source actually and
completely supports — the folder/SKILL.md/Steps-section mechanism plus
the skill's own three named actions (fills formulas, validates
calculations, checks formatting, adapts to any template structure), which
unlike the comps-analysis sibling's source were NOT truncated or
placeholder-broken — and filled BHTF's broken clause with a generic,
plausible task ("fill in an LBO model template for a leveraged buyout
deal") rather than a specific one, since the source's own broken sentence
never named a real task either.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
