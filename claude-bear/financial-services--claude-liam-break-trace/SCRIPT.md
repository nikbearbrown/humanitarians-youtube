# SCRIPT.md — Trace It, Don't Fix It. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-break-trace` (Teardown, walks the Anthropic
`break-trace` Claude Code Skill from the `financial-services` book's
`gl-reconciler` plugin) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would fix a break in the books. It doesn't — it
traces one. So: does Claude trace a break back to where the two sides
stopped agreeing?

*(Text typed on screen: "Does Claude / fix a break / in the / books?" —
trigger word "fix" corrects to "trace", landing on: "Does Claude trace a
break in the books?" Rates (42ms/char, 8% hesitateBetween, 4% mistakeRate)
reused directly from the working configuration on the
`claude-plugins-official--claude-liam-agent-development` sibling, which
hit its ≥8s TIMING LAW floor cleanly with a comparably short 4-line text —
avoids re-discovering that sibling's first-attempt overrun.)*

## Body — anatomy, pipeline, what break-trace actually does

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
break-trace. It's just one file, SKILL.md, written in plain language — no
hidden code. Claude reads the file, then acts on what it says. The file is
the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside, the instructions are steps, and Claude runs them in order. First:
read the file. Then: run each step exactly as written. Then: hand back the
result. No branching, unless a step itself tells it to branch.

**NB03 — Trace, Not Fix** (source B03, design tell — re-registered
Teardown → Plain: the source's "gets it right / where it bites" framing is
dropped for a plain statement of the mechanism and its boundary)
This particular skill only runs after another skill has already flagged a
break — a spot where two records that should match, don't. Break-trace's
job is to follow the trail back, on each side, to the original transaction
or posting, and state exactly what's different and why. It doesn't decide
what to do about the difference. It just finds where it started.

## Close

**BCRY — carry-out**
Break-trace finds exactly where two numbers stopped agreeing and says
why — it never decides what happens next.

**BHTF — your turn**
Your turn. Paste this into Claude: I have two numbers that should match,
but they don't. Before you try to fix anything, walk me through exactly
where they first differ and why. That's the same order break-trace
follows — find the cause, say it plainly, and only then talk about a fix.

**BOUT — outro**
Trace It, Don't Fix It. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a fix-or-diagnose question — does Claude resolve the discrepancy, or just explain it? |
| Wrong guess | B00 (WRITER LAW) | "fix" corrected to "trace" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder structure and the linear step pipeline Claude runs it through |
| Anchor | the break-trace skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill positively does (traces to source, states the diff) and what it does not do (decide the fix); BCRY states the same pair as the carry-out — matches the source's verdict beat, which paired the same two facts (repeatable result; limited to the file's scope) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the break-trace Skill's SKILL.md specifies (the one-file folder structure,
the linear step execution, the root-cause-to-source-transaction mechanism,
the dependency on gl-recon's prior classification, and the same-input/
same-output determinism) — not an inference about hidden model internals.
Per simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown design-tell) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right: repeatable results / where it bites:
anything outside the spec" framing is restated in NB03 as a plain
mechanism-and-boundary fact (what the skill traces to, and what it
declines to decide) rather than a strengths/gaps verdict, per the NO
JUDGMENT register check; BVDT's verdict facts (same input → same output
every run; limited to what the file specifies) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, but the
source's prompt text is adapted rather than copied verbatim — the source
asked the viewer to "read the break-trace skill," which requires a plugin
install a general viewer won't have, so this redo substitutes an
equivalent, actually-paste-ready prompt that exercises the same
trace-before-fix habit ("walk me through exactly where they first differ
and why" before "you try to fix anything") without depending on any
specific Skill file; BOUT kept, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
