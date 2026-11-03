# SCRIPT.md — It Updates the Model. Not Itself. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-model-update` (Teardown, walks the Anthropic
`model-update` Claude Skill from the `financial-services` book's
`earnings-reviewer` plugin) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a model update means Claude itself got smarter. It
doesn't — the skill refreshes a financial model with new data. So: does
Claude update a model, not itself, when new numbers come in?

*(Text typed on screen: "Does a model / update mean / Claude just got /
smarter?" — trigger word "smarter" corrects to "new numbers", landing on:
"Does a model update mean Claude just got new numbers?" Rates reused from
the working `financial-services--claude-liam-kyc-rules` sibling's
configuration (42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line
text), which cleared the >=8s TIMING LAW floor cleanly with a comparably
short text.)*

## Body — anatomy, pipeline, what model-update actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
model-update. It's just one file, SKILL.md, written in plain language — no
hidden logic. Claude reads the file, then acts on what it says. The file
is the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
take the new data — earnings, guidance, a revised assumption. Then: adjust
the estimates and recalculate the valuation. Then: flag whatever changed
enough to matter. No branching, unless a step itself tells it to branch.

**NB03 — Updates the model, not Claude** (source B03 + BVDT, design tell
and verdict — re-registered Teardown → Plain: the source's "gets it right:
repeatable results / what it bites: anything outside the spec" framing and
the verdict's "same input, same output / know the limit" facts are dropped
for a plain statement of the mechanism and its boundary)
This particular skill exists so nobody redoes the same update by hand
every time new numbers land. Model-update takes what changed — quarterly
earnings, new guidance, a revised assumption — and works it through: new
estimates, a recalculated valuation, a flag on anything material. None of
that changes Claude. It changes the model, using data Claude is handed for
that one run. The investment call still belongs to a person — the skill
flags what changed, it doesn't decide what to do about it.

## Close

**BCRY — carry-out**
A model update doesn't make Claude smarter — it makes the model current,
and the decision still belongs to a person.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a set of financial estimates,
and new numbers just came in — an earnings print, updated guidance, a
changed assumption. Before you touch anything, walk me through exactly
which estimates you'd adjust, how the valuation changes, and what you'd
flag as material — then wait for me to say go. That's the same order
model-update follows: work out the update, flag what matters, and let a
person greenlight it.

**BOUT — outro**
It Updates the Model. Not Itself. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a version-bump question — did Claude itself get updated, or did a financial model? |
| Wrong guess | B00 (WRITER LAW) | "smarter" corrected to "new numbers" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through |
| Anchor | the model-update skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (adjusts, recalculates, flags) and what it does not do (change Claude, decide the investment call); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the model-update Skill's SKILL.md specifies (the one-file folder structure,
the linear step execution, the earnings/guidance/assumption inputs, the
estimate/valuation/flag outputs, and the same-input/same-output
determinism) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right: repeatable results / what it bites: anything
outside the spec" framing and BVDT's verdict facts ("same input, same
output, every run"; "know the limit: only what the file says") are merged
into a single NB03 mechanism-and-boundary beat rather than kept as two
separate beats (a design-tell beat and a bulleted artifact card), per the
NO JUDGMENT register check and CARRY-OUT LAW (BVDT's residual facts move
into BCRY instead of staying a separate verdict artifact); BHTF kept as
the your-turn handoff, but the source's prompt text is adapted rather than
copied verbatim — the source asked the viewer to "read the model-update
skill," which requires a plugin install a general viewer won't have, so
this redo substitutes an equivalent, actually paste-ready prompt that
exercises the same work-out-then-flag-then-wait habit without depending on
any specific Skill file; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
