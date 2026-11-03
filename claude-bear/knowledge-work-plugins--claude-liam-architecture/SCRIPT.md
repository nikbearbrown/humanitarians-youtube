# SCRIPT.md — Only What The File Says. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-architecture` (Teardown, walks the Anthropic
`architecture` Skill — create or evaluate an architecture decision record) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude's own judgment writes a good architecture call. It
doesn't — a written file does. So: does Claude use its SKILL.md to write a
good architecture call?

*(Text typed on screen: "Does Claude use / judgment / to write a good /
architecture call?" — trigger word "judgment" corrects to "its SKILL.md",
landing on: "Does Claude use its SKILL.md to write a good architecture
call?")*

## Body — anatomy, the pipeline, the one job

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is called
architecture. Its SKILL.md holds the full instruction set, in plain
language — no hidden logic. Claude reads it, then acts on it. The file is
the program.

**NB02 — Read then execute** (source B02, pipeline)
The pipeline lives in the Steps section. Claude reads each step in order,
then executes it — linear, no branching, unless a step says otherwise.

**NB03 — One file, one job** (source B03, design tell — re-registered
Teardown → Plain, kept as the mechanism-and-scope fact rather than the
"gets it right / where it bites" framing)
This skill has exactly one job: create or evaluate an architecture decision
record — choosing between technologies, documenting a trade-off, reviewing
a design proposal, or designing a new component from constraints. All of it
lives inside that one file's script. Nothing outside it is covered.

## Close

**BCRY — carry-out**
A skill runs the same steps every time you call it — never a step beyond
what its file wrote down.

**BHTF — your turn**
Your turn. Paste this into Claude: Create an ADR for choosing between two
technologies for my project. Walk me through your plan before you act.
That last clause matters — explaining the plan first surfaces the real
constraint logic, not just a recommendation.

*(On-screen command text shortened from the first draft to fit the
composer card's 3-line display cap — `ClaudeComposerAsk`'s input area is
`maxHeight: CMD * 1.45 * 3` with `overflow: hidden`, so a 4-line wrap
silently clips its last line off screen. First draft ["I want to create an
architecture decision record for choosing between two technologies for my
project. Read the architecture skill and walk me through what you will do
before you do it."] wrapped to 4 lines and lost "before you do it." from
view — caught by a frame pull mid-BHTF, fixed by shortening to a 3-line-fit
paraphrase, same request and same emphasized clause.)*

**BOUT — outro**
Only What The File Says. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a source-of-authority question — does Claude's own judgment write the architecture call? |
| Wrong guess | B00 (WRITER LAW) | "judgment" corrected to "its SKILL.md" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | a skill is a folder with a SKILL.md instruction set Claude reads before acting; the pipeline reads and executes the Steps section in linear order |
| Anchor | the architecture skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what the one job covers and states plainly that anything outside it isn't covered; BCRY states the design's payoff and its limit together (the same steps run reliably every time, and never a step beyond what the file wrote down) — together they cover what the skill delivers and what it doesn't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the architecture Skill's SKILL.md specifies (the folder/file structure, the
Steps-section pipeline, the linear execute-in-order behavior, and the exact
scope of the one task — ADR creation and evaluation) — not an inference
about hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's Teardown framing ("Here is the Teardown moment... What it gets right:
repeatable results. What it bites: anything outside the spec.") is
compressed into NB03, keeping the same underlying fact — the skill's task
is exactly one job (ADR creation/evaluation, across the four named
scenarios: choosing technologies, documenting a trade-off, reviewing a
proposal, designing from constraints) and nothing beyond that — stripped of
"gets it right / where it bites" verdict language per the NO JUDGMENT
register check; BVDT's verdict facts (repeatable execution, and the limit
that only the file's spec is covered) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW; BHTF kept as the your-turn handoff — the source's prompt
text was garbled by truncation ("I want to create or evaluate an
architecture decision record (adr). use when choosing betw.") and is
rebuilt here as a concrete, paste-ready, ungarbled prompt carrying the same
request (create an ADR, choosing between two technologies) plus the
source's own flagged clause ("walk me through what you will do before you
do it"); BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
