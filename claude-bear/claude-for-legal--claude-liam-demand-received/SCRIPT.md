# SCRIPT.md — Claude, Demand Received. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-demand-received` (Teardown, walks the Anthropic
`demand-received` legal Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude just replies when a demand letter comes in. It
doesn't just reply — it triages first. So: when a demand letter arrives,
does Claude triage it?

*(Text typed on screen: "A demand letter arrives. / Does Claude just /
reply?" — trigger word "reply" (a single token; the component matches
per-token, not phrase-wise) corrects to "triage it", landing on: "A demand
letter arrives. Does Claude just triage it?")*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is called
demand-received. Its one file, SKILL.md, holds the whole instruction set,
written in plain language — no hidden logic. Claude reads it, then acts.
The file is the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and executes it — read the file, execute each step, return the result.
Linear: no branching, unless a step says otherwise.

**NB03 — The triage pipeline** (source B03, design tell — re-registered
Teardown → Plain)
One instruction inside it is specific: the skill extracts the letter's key
fields, cross-checks them against the portfolio, and assesses merit — then
it presents response options with a recommendation. If escalation is
warranted, it hands off to matter-intake or demand-intake instead of
resolving it alone.

## Close

**BCRY — carry-out**
Claude isn't deciding whether to escalate on its own — when the assessment
says escalate, it hands off to matter-intake or demand-intake instead of
handling it itself.

**BHTF — your turn**
Your turn. Paste this into Claude: I have an inbound demand letter. Read the
demand-received skill, and before you triage it, walk me through what you
will do — the fields you'll extract, the portfolio cross-check, and the
conditions under which you'd escalate instead of recommending a response
yourself.

**BOUT — outro**
Claude, Demand Received. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a legal question — does Claude just reply? |
| Wrong guess | B00 (WRITER LAW) | "reply" corrected to "triage it" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes steps linearly; the specific triage sequence (extract, cross-check, assess, recommend) ends in an escalation hand-off, not a self-resolved answer |
| Anchor | the demand-received Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "escalation is a hand-off decision, not Claude's own call" states both what the mechanism does (triage reliably: extract, cross-check, assess, recommend) and its limit (only hands off when warranted — it doesn't also decide the escalation itself beyond that flag), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the Skill's SKILL.md specifies (a folder, one file, a Steps section executed
in order, the extract/cross-check/assess/recommend/escalate sequence) — not
an inference about hidden model internals. Per simple's ONE-FLAG LAW, when
the source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-UI cold open) + B01/B02/B03 (anatomy /
pipeline / design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) —
the shortest of the `claude-liam-*` Teardown family, a single-example skill
walkthrough with no wrong-guess, anchor, or both-directions beats of its own
to redistribute. This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02, B03→NB03 kept as one
beat each, Teardown framing ("the design tell," "what it gets right / what
it bites") stripped to a plain mechanism description; BVDT's two verdict
facts (reliable triage execution, and the escalation-hand-off limit) merged
into the single BCRY carry-out sentence rather than kept as a separate
artifact-card beat, since Plain register carries one carry-out sentence, not
a bulleted verdict (CARRY-OUT LAW); BHTF kept as the your-turn handoff, with
the source's truncated bracketed narration replaced by a concrete,
paste-ready scenario so the prompt is actually runnable today; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact` patterns) with B00 as a Composer-UI cold open
(REMOTION `ClaudeComposerAsk`, not AI-VIDEO — the source never called a
generation service). NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00's cold open, which this redo replaces per hai-simple's mandate anyway.
