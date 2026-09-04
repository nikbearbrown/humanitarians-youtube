# SCRIPT.md — Claude, Competitive Analysis. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-competitive-analysis` (Teardown, walks the Anthropic
`competitive-analysis` market-researcher plugin Skill) — question, facts, and
body argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumes a finished competitive-analysis deck means Claude judged the
market itself. It doesn't — the skill just processes a fixed set of steps
written in a file. So does it judge, or process?

*(Text typed on screen: "A finished deck / means Claude judged / my market. /
Right?" — trigger word "judged" corrects to "processed", landing on: "A
finished deck means Claude processed my market. Right?")*

## Body — anatomy, the pipeline, the scope limit

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
competitive-analysis: a SKILL.md file and a references folder, two files
total. The SKILL.md contains the full instruction set — plain language, no
hidden logic. Claude reads it, then acts. The file is the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The pipeline is in the Steps section. Claude reads SKILL.md, executes each
step in order, and returns the result. Linear — no branching unless a step
says so.

**NB03 — Only what the file says** (source B03, design tell — re-registered
Teardown → Plain: the "gets it right / what it bites" framing is stripped to
a plain description of scope, no verdict)
The skill answers only within what SKILL.md specifies. Ask it something
inside that scope — a market map, a peer comparison, a positioning
assessment — and it runs the same steps every time. Ask it something outside
that written scope, and there's nothing there to answer with.

## Close

**BCRY — carry-out** (folds in source BVDT's verdict facts, per CARRY-OUT LAW)
A skill runs the same steps on every request — read the file, execute in
order, return the result. It only knows what's written in that file, nothing
more.

**BHTF — your turn**
Your turn. Paste this into Claude: Build a competitive landscape deck
comparing three regional business-banking platforms I'm evaluating. Read the
competitive-analysis skill and walk me through what you will do before you do
it. Then check: did it name the steps it read from the file, or did it just
start improvising? That's the actual test of whether it's running the skill.

**BOUT — outro**
Claude, Competitive Analysis. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a judgment-vs-procedure question — does a finished deck mean Claude judged the market, or ran a fixed process? |
| Wrong guess | B00 (WRITER LAW) | "judged" corrected to "processed" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill is a folder (SKILL.md + references) Claude reads before acting; the pipeline reads the file, executes each step in order, returns the result, with no branching unless a step says so |
| Anchor | the competitive-analysis skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what's inside the written scope (answered every time) and what's outside it (nothing there); BCRY states the same design's payoff and its limit together (same steps every run; only what the file says) — together they cover what the skill can and can't do, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the competitive-analysis Skill's SKILL.md specifies (the SKILL.md +
references file structure, the read → execute → return pipeline, the linear
no-branching rule, and the scope limit that the skill only answers what the
file covers) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each; B03's
"what it gets right / what it bites" framing is compressed into NB03 as a
plain scope description (inside the file's scope vs. outside it), stripping
the Teardown "gets it right"/"bites" verdict language per the NO JUDGMENT
register check; BVDT's verdict facts (same input → same output every run;
limit is only what the file says) are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per CARRY-OUT
LAW; BHTF kept as the your-turn handoff — the source's prompt was garbled
mid-template ("I want to framework for building competitive landscape decks
— market positioning, competi. Read the competitive-analysis skill...") and
is rewritten here as a concrete, grammatical, paste-ready prompt (a
regional-business-banking competitive deck) that keeps the source's own
"walk me through what you will do before you do it" clause (the LENS-AUDIT's
noted Plato move: artifact-vs-world, forcing the plan before the run); BOUT
kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 +
BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
