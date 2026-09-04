# SCRIPT.md — It Surfaces the Risk. It Doesn't Approve. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-compliance-check` (Teardown, walks the Anthropic
`compliance-check` Claude Skill from the `knowledge-work-plugins` book's
legal plugin set) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would clear a product feature as compliant. It
doesn't — it flags which regulations, approvals, and risks apply. So: does
Claude flag compliance issues on a proposed feature?

*(Text typed on screen: "Does Claude / clear my / feature for / launch?" —
trigger word "clear" corrects to "flag", landing on: "Does Claude flag my
feature for launch?" Rates reused from the
`knowledge-work-plugins--claude-liam-audit-support` sibling's proven working
configuration (42ms/char, 8% hesitateBetween, 4% mistakeRate, short 4-line
text), which cleared the >=8s TIMING LAW floor cleanly with a comparably
short text.)*

## Body — anatomy, pipeline, what compliance-check actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
compliance-check. It's just one file, SKILL.md, written in plain language —
no hidden logic. Claude reads the file, then acts on what it says. The file
is the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
identify the action and where it touches regulated ground. Then: surface
the applicable regulations and required approvals. Then: flag the risk
areas and write it up. No branching, unless a step itself tells it to
branch.

**NB03 — Surfaces and Flags** (source B03, design tell — re-registered
Teardown → Plain: the source's "gets it right: repeatable results / what
it bites: anything outside the spec" framing is dropped for a plain
statement of the mechanism and its boundary)
This particular skill is built for one job: checking a proposed action
against a compliance framework. Given a feature or initiative, it surfaces
which regulations touch it, which approvals are typically required, and
where the risk areas sit. It doesn't decide whether the feature is approved
to ship. It surfaces what applies and writes it up — the approval call
stays with legal and the people who own it.

## Close

**BCRY — carry-out**
Compliance-check surfaces the regulations, approvals, and risks that apply
to a proposed action — it never decides whether the action gets approved.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a product feature I'm about to
ship. Before you tell me whether it's fine to launch, walk me through which
regulations or policies might touch it, what approvals it would typically
need, and where the risk areas are — then leave the go or no-go call to me.
That's the same order compliance-check follows — surface what applies, flag
the risk areas, and leave the approval to a person.

**BOUT — outro**
It Surfaces the Risk. It Doesn't Approve. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a clear-or-flag question — does Claude sign off on the feature, or just flag what applies to it? |
| Wrong guess | B00 (WRITER LAW) | "clear" corrected to "flag" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through (identify the action, surface regulations and approvals, flag risk, write it up) |
| Anchor | the compliance-check skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (surfaces regulations, approvals, risk areas) and what it does not do (decide whether the feature is approved); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the compliance-check Skill's SKILL.md specifies (the one-file folder
structure, the linear step execution, the regulation/approval/risk
surfacing mechanism, and the same-input/same-output determinism) — not an
inference about hidden model internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right: repeatable results / what it bites: anything
outside the spec" framing is restated in NB03 as a plain mechanism-and-
boundary fact (what the skill surfaces and flags, and what it declines to
decide) rather than a strengths/gaps verdict, per the NO JUDGMENT register
check; BVDT's verdict facts (same input → same output every run; limited
to what the file specifies) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the source's prompt
text is adapted rather than copied verbatim — the source asked the viewer
to "read the compliance-check skill," which requires a plugin install a
general viewer won't have, so this redo substitutes an equivalent, actually
paste-ready prompt that exercises the same surface-before-approve habit
("walk me through... then leave the go or no-go call to me") without
depending on any specific Skill file; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
