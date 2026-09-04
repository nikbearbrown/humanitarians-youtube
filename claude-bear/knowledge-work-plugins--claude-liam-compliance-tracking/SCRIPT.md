# SCRIPT.md — It Tracks. It Doesn't Certify. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-compliance-tracking` (Teardown, walks the Anthropic
`compliance-tracking` Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude would certify whether a company is SOC 2 compliant.
It doesn't — it tracks the requirements and prepares the audit trail. So:
does Claude track a company's SOC 2 compliance?

*(Text typed on screen: "Does Claude / certify a / company's SOC 2 /
compliance?" — trigger word "certify" corrects to "track", landing on:
"Does Claude track a company's SOC 2 compliance?" Params reused verbatim
from the `audit-support` sibling's already-proven-safe values (42ms/char,
4% mistakeRate, 8% hesitateBetween) — text is a similar 4-line length, no
overrun expected.)*

## Body — anatomy, pipeline, this skill's job + boundary

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
compliance-tracking. It's just one file, SKILL.md, written in plain
language — no hidden logic. Claude reads the file, then acts on what it
says. The file is the whole program.

**NB02 — Linear pipeline** (source B02, pipeline)
Inside SKILL.md is a Steps section, and Claude works through it top to
bottom: read the file, execute each step in order, return the result. No
branching, unless a step itself says so.

**NB03 — Tracks and prepares** (source B03 design-tell + BVDT verdict,
re-registered Teardown → Plain: the "gets it right / where it bites"
framing is dropped, kept as a plain mechanism-and-boundary statement)
This particular skill is built for one job: track compliance requirements
and prepare for audit readiness. It responds to trigger phrases like
"compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", or "regulatory
requirement". Run it twice on the same request and the steps come out the
same both times. But it doesn't reach past that page — anything the file
doesn't cover isn't part of the job.

## Close

**BCRY — carry-out**
A compliance skill doesn't certify anything — it tracks the requirements
and preps the audit trail from a written file, the same way every single
time.

**BHTF — your turn**
Your turn. Paste this into Claude: I need to track our compliance
requirements for SOC 2 and prep for an upcoming audit. Before telling me
whether we're compliant, walk me through each requirement, whether we
currently meet it, and what evidence is missing — then leave the overall
compliance call to me. That's the same order compliance-tracking follows:
track the requirements, flag the gaps, and leave the determination to a
person.

**BOUT — outro**
It Tracks. It Doesn't Certify. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an audience question — does Claude judge compliance, or just track it? |
| Wrong guess | B00 (WRITER LAW) | "certify" corrected to "track" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill-as-folder anatomy (one file, plain language); the linear read-execute-return pipeline |
| Anchor | the compliance-tracking skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one skill, one job), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the skill does (tracks requirements, same steps every run) and what it doesn't (reach past the page); BCRY states the same pairing as the one sentence that survives repetition — together they cover the design's payoff (repeatability) and its limit (only what's written), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `compliance-tracking` Skill's own narration specifies (the folder/
SKILL.md anatomy, the linear step pipeline, the job description "track
compliance requirements and audit readiness," the six trigger phrases, and
the same-input-same-output/only-what's-written verdict facts) — not an
inference about hidden model internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each,
narration close to source (both were already generic "skill = folder" /
"linear pipeline" statements, common to the whole `claude-liam-*` Skill
family — no compliance-tracking-specific pipeline detail exists in the
source to specialize further, unlike siblings whose sources named specific
sub-steps); B03's Teardown framing ("gets it right" / "where it bites") and
BVDT's verdict facts are merged into NB03 (a plain mechanism-and-boundary
statement: tracks requirements + prepares audit readiness + six trigger
phrases + same-input-same-output + only-what's-written) plus BCRY (the
single carry-out sentence), per CARRY-OUT LAW; BHTF kept as the your-turn
handoff — the source's actual prompt text was truncated mid-sentence in the
locked sheet's JSON ("trigger with \"compliance\", \"a."), so the full,
untruncated trigger list from the source's own B00 narration was used to
complete it faithfully rather than inventing new content, and the "walk me
through what you will do before you do it" clause — the source's genuine
insight — was kept, reworded as a concrete, paste-ready prompt a viewer can
run today (asking Claude to enumerate per-requirement findings before
rendering an overall compliance call, mirroring the `audit-support` sibling's
equivalent substitution); BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
