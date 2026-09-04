# SCRIPT.md — Runs the Steps, Not Its Own Reasoning. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-merger-model` (Teardown, walks the anatomy of the
Anthropic `merger-model` Skill — an `investment-banking` plugin Skill,
financial-services family) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumes building a merger model means Claude reasons through the
deal like an M&A analyst would. It doesn't — it follows a written file,
step by step. So: does it follow through the steps?

*(Text typed on screen: "When Claude builds / a merger model, / does it
reason / through the steps?" — trigger word "reason" corrects to "follow",
landing on: "When Claude builds a merger model, does it follow through the
steps?")*

## Body — anatomy, pipeline, what the file actually specifies

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
merger-model. The SKILL.md file inside it is the full instruction set —
plain language, no hidden logic. Claude reads it, then acts. The file is
the program.

**NB02 — Steps, in order** (source B02, pipeline)
The pipeline lives in the file's Steps section. Claude reads each step in
order and executes it. Linear — no branching unless the step says so.

**NB03 — What the file specifies** (source B03, Teardown compressed to
Plain: the "gets it right / what it bites" framing is dropped; the
specific content the source's own B00 narration fully names — but B03's
own copy of it truncates mid-word — is restored from that untruncated
source)
That's what merger-model actually specifies: accretion or dilution
analysis for an M&A deal — pro forma EPS impact, synergy sensitivities,
purchase price allocation. It's a specification, not a suggestion — the
same two companies produce the same walk through those numbers, every
time.

## Close

**BCRY — carry-out**
Inside the merger-model skill, Claude isn't reasoning through the deal —
it's running the written steps. That's why the same two companies produce
the same accretion/dilution result every run, and never more than the
file specifies.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to build an accretion/dilution
analysis for an M&A deal — modeling pro forma EPS impact, synergy
sensitivities, and purchase price allocation. Read the merger-model skill
and walk me through what you will do before you do it. That last clause
matters — asking Claude to explain first, before it runs, is what
actually shows you the steps the file wrote for it.

**BOUT — outro**
Runs the Steps, Not Its Own Reasoning. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanism question — does Claude reason through deal math like an analyst, or execute a written procedure? |
| Wrong guess | B00 (WRITER LAW) | "reason" corrected to "follow" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the file/folder anatomy (SKILL.md = the program) and the execution model (Steps section, read in order, linear, no branching unless told) |
| Anchor | the merger-model skill itself, named at B00 and never dropped through NB01–NB03 (its specific outputs — accretion/dilution, pro forma EPS, synergy sensitivities, purchase price allocation — are the anchor's recurring content, first stated whole in NB03) | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — the concrete deal-math content is what stays on screen through NB03, BCRY, and BHTF |
| Both directions | folded into NB03 + BCRY | NB03 states what the design guarantees (same input, same output) and what it doesn't cover (outside the file, nothing written down); BCRY restates both halves as one sentence pair, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim describes what the
merger-model Skill's own file structure and stated purpose specify (a
folder containing a SKILL.md instruction set; a Steps section executed in
order; the accretion/dilution, pro forma EPS, synergy-sensitivity, and
purchase-price-allocation outputs the skill's own description names; and
the consequent determinism/limit) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "design tell" framing ("Here is the Teardown moment... What
it gets right: repeatable results. What it bites: anything outside the
spec.") is compressed into NB03 as a plain mechanism-and-consequence
statement, stripped of the strengths/gaps verdict framing per the NO
JUDGMENT register check; BVDT's verdict facts (same input → same output
every run; limited to what the file says) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff, its prompt restored
to full grammatical form (see defect note below); BOUT kept, re-skinned to
the Humanitarians AI outro (`OutroSeries`). Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

**Source defect found and worked around, not silently carried over:** the
source `beat_sheet.json`'s narration for B03, BVDT, and BHTF each contain
the merger-model skill description mid-word truncated — "synergy
sensiti." (B03), "pro forma EPS imp." (BVDT), and "models pro forma eps
imp." spliced into an ungrammatical handoff clause ("I want to build
accretion/dilution analysis for m&a transactions. models pro forma eps
imp.") in BHTF — evidently a batch script's fixed-character-budget cut of
the skill's own description string, applied mid-word. Unlike a fully
missing/placeholder value, the complete, untruncated description survives
intact in the source's own **B00** narration ("Build accretion/dilution
analysis for M&A transactions. Models pro forma EPS impact, synergy
sensitivities, and purchase price allocation. Use when evaluating a
potential acquisition, preparing merger consequences analysis for a
pitch, or advising on deal terms."), so this redo recovers the specific,
verifiable facts from that complete copy rather than either propagating
the truncated fragments or inventing unverifiable specifics. NB03 and
BHTF both use the recovered, complete phrasing; the source's
`source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/investment-banking/skills/merger-model/SKILL.md`)
does not resolve on this machine, so nothing beyond what B00 already
states in full was added.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
