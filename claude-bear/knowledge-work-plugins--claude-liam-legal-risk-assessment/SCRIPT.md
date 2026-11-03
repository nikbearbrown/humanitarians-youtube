# SCRIPT.md — It Sorts the Risk. It Doesn't Score It. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-legal-risk-assessment` (Teardown, walks the Anthropic
`legal-risk-assessment` Claude Skill from the `knowledge-work-plugins`
book's legal plugin set) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would score a contract's legal risk with a single
verdict. It doesn't — it sorts issues by severity and likelihood, and
flags which need escalation. So: does Claude sort legal risk this way?

*(Text typed on screen: "Does Claude / score my / contract's / legal
risk?" — trigger word "score" corrects to "sort", landing on: "Does Claude
sort my contract's legal risk?" Timing config reused from the
`compliance-check`/`audit-support` siblings' proven working configuration
(42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line text), which
cleared the >=8s TIMING LAW floor cleanly with comparably short text.)*

## Body — anatomy, pipeline, what legal-risk-assessment actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
legal-risk-assessment. It's just one file, SKILL.md, written in plain
language — no hidden logic. Claude reads the file, then acts on what it
says. The file is the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
identify the legal issue. Then: rate it by severity and by how likely it
is to happen. Then: check it against escalation criteria — does this need
senior counsel or outside review. No branching, unless a step itself tells
it to branch.

**NB03 — Sorts and Flags** (source B03, design tell — re-registered
Teardown → Plain: the source's "gets it right: repeatable results / what
it bites: anything outside the spec" framing is dropped for a plain
statement of the mechanism and its boundary)
This particular skill is built for one job: sorting legal issues onto a
severity-by-likelihood grid, then flagging which ones cross into needing
senior counsel or outside legal review. Given a contract or a deal, it
classifies each issue and writes up where it lands. It doesn't score the
matter with a single verdict, and it doesn't replace a lawyer's judgment.
It sorts and flags — the legal call stays with counsel.

## Close

**BCRY — carry-out**
Legal-risk-assessment sorts legal issues by severity and likelihood and
flags which ones need escalation — it never scores the matter with a
single verdict of its own.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a contract clause that worries
me. Before you tell me if it's risky, walk me through how severe it would
be if it went wrong, how likely that is to happen, and whether it's the
kind of thing that needs a lawyer to look at — then leave the final call
to me. That's the same order legal-risk-assessment follows — rate
severity, rate likelihood, flag escalation, and leave the legal judgment
to counsel.

**BOUT — outro**
It Sorts the Risk. It Doesn't Score It. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a score-or-sort question — does Claude render a verdict on the risk, or just sort it and flag what needs a lawyer? |
| Wrong guess | B00 (WRITER LAW) | "score" corrected to "sort" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through (identify the issue, rate severity and likelihood, check escalation criteria) |
| Anchor | the legal-risk-assessment skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (sorts issues onto the severity/likelihood grid, flags escalation) and what it does not do (score the matter with its own verdict, replace a lawyer's judgment); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the legal-risk-assessment Skill's SKILL.md specifies (the one-file
folder structure, the linear step execution, the severity-by-likelihood
classification with escalation criteria, and the same-input/same-output
determinism) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B03's Teardown "gets it right: repeatable results / what it bites:
anything outside the spec" framing is restated in NB03 as a plain
mechanism-and-boundary fact (what the skill sorts and flags, and what it
declines to decide) rather than a strengths/gaps verdict, per the NO
JUDGMENT register check; BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the
source's prompt text is adapted rather than copied verbatim — the source
asked the viewer to "read the legal-risk-assessment skill," which requires
a plugin install a general viewer won't have, so this redo substitutes an
equivalent, actually paste-ready prompt that exercises the same
sort-before-escalate habit ("walk me through... then leave the final call
to me") without depending on any specific Skill file; BOUT kept, re-skinned
to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT
= 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
