# SCRIPT.md — A Checklist, Not an Algorithm. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-competitive-brief` (Teardown, walks the Anthropic
`competitive-brief` marketing Skill: research competitors and generate a
positioning and messaging comparison with content gaps, opportunities, and
threats) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.
Source has no SCRIPT.md; its `beats[*].narration_text` served as the locked
script (same pattern as the `claude-plugins-official--claude-liam-agent-
development` precedent).

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude runs a hidden algorithm to research competitors. It
doesn't — it follows a written checklist. So: does Claude have a special
checklist for competitor research?

*(Text typed on screen: "Does Claude have / a special algorithm / for
competitor / research?" — trigger word "algorithm" corrects to "checklist",
landing on: "Does Claude have a special checklist for competitor research?"
Render params copied from the already-debugged fix on the
`claude-plugins-official--claude-liam-agent-development` sibling —
charMs=42, jitter=26, mistakeRate=4, hesitateWithin=2, hesitateBetween=8 —
because this text is nearly the same length (61 chars vs. that sibling's
fixed 60-char version) as the text that overran its window at the sibling's
slower/higher-hesitation first-attempt settings; using the proven-safe
parameters from the start avoids repeating that failure mode. Verify
media/B00.mp4 ≥ 8s and that "algorithm" visibly corrects to "checklist"
before the clip ends.)*

## Body — anatomy, the pipeline, one job by design

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is just a folder Claude reads before it starts working. This one is
called competitive-brief. Inside is one file — SKILL.md — plain-language
instructions, not a hidden algorithm. Claude reads that file, then acts on
it, step by step. The file is the program.

**NB02 — The pipeline: steps, in order** (source B02, pipeline)
The pipeline lives in the Steps section of that file. Claude reads each
step in order and executes it. It's linear — no branching, unless a step
itself says otherwise.

**NB03 — One job, by design** (source B03, design tell — re-registered
Teardown → Plain, judgment language dropped)
competitive-brief does one job: research the competitors, then generate a
positioning and messaging comparison — content gaps, opportunities, and
threats. Whatever isn't spelled out in those steps, this skill simply
doesn't do. Same input, same steps, every run.

## Close

**BCRY — carry-out**
competitive-brief always runs the same three moves — research, compare,
flag the gaps — in the same order, every time. It only ever does what the
SKILL.md's steps say to do.

**BHTF — your turn**
Your turn. Paste this into Claude: I want to research my competitors and
generate a positioning and messaging comparison with content gaps,
opportunities, and threats. Read the competitive-brief skill and walk me
through what you'll do before you do it. That last part matters — asking
Claude to explain the plan first shows you exactly which steps the file
actually specifies.

**BOUT — outro**
A Checklist, Not an Algorithm. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the question everyone actually has — is there special sauce behind an AI-generated competitor brief? |
| Wrong guess | B00 (WRITER LAW) | "algorithm" corrected to "checklist" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the file is one plain-language document (SKILL.md); execution is linear, one step at a time, from the Steps section |
| Anchor | the competitive-brief skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill's job covers and its hard boundary (nothing outside the written steps) in the same beat; BCRY restates the repeatable-steps payoff and the same boundary together — together they cover what the design does and does not do, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence-pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the competitive-brief Skill's SKILL.md specifies, as carried over from the
source reel's narration (a folder containing one SKILL.md, a Steps section
executed in order, and a stated job of researching competitors and
generating a positioning/messaging comparison with content gaps,
opportunities, and threats) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown "gets it right / where it bites" framing is stripped to a
plain mechanism-and-boundary description for NB03, per the NO JUDGMENT
register check — the underlying fact (repeatable results, nothing outside
the spec) is kept, only the verdict language ("what it gets right," "what
it bites") is removed; BVDT's verdict facts (repeatable steps, the file's
hard boundary) are merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF
kept as the your-turn handoff, with the source's prompt carried over
(research competitors, generate a positioning/messaging comparison, and
ask Claude to explain its plan before acting) — already a concrete,
paste-ready prompt needing no extra setup; BOUT kept, re-skinned to the
Humanitarians AI outro (`OutroSeries`). Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway. NB01–NB03 render as GRAPHIC
(Manim, the generic chip-row template shared with the `claude-plugins-
official` hai-simple siblings) rather than the source's Remotion anatomy
cards, satisfying the same law by a different renderer.
