# SCRIPT.md — It Scores Before It Edits. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-claude-md-improver` (Teardown, walks the Anthropic
`claude-md-improver` plugin skill) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed asking Claude to improve a CLAUDE.md file means an instant
rewrite. It doesn't — it scores the file first, before touching anything.
So: will asking Claude to improve my CLAUDE.md just score the file?

*(Text typed on screen: "Will asking Claude / to improve my CLAUDE.md /
just rewrite / the file?" — trigger word "rewrite" corrects to "score",
landing on: "Will asking Claude to improve my CLAUDE.md just score the
file?")*

## Body — where the file lives, the gate, the practical cap

**NB01 — Five locations, one score** (source B01, anatomy)
CLAUDE.md files can live in five places. The project root — shared with the
team, checked into git. A local override — gitignored, for personal
settings only. A global file — your defaults across every project. A
package-specific file inside each folder of a monorepo. And any
subdirectory, for feature-specific context. Claude discovers all of these by
walking parent directories automatically. Before anything changes, each file
gets scored against six criteria — commands and workflows documented,
architecture clarity, non-obvious patterns, conciseness, currency, and
actionability — and comes back as a letter grade, A through F.

**NB02 — Report, then a diff** (source B02, design)
The process runs in phases. First, discovery — Claude finds every CLAUDE.md
file. Second, it scores each one against the rubric. Third — and this is a
hard rule in the skill — it shows you the full report before it changes a
single line. Only after you say go does it propose updates, and those
updates come as a diff: which file, exactly what to add, and one line on why
it helps future sessions. Minimal, targeted additions — never a rewrite of
what's already there.

**NB03 — The fifty-file cap** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
One practical limit worth knowing: the discovery step caps at fifty files.
In a small project that never matters. In a large monorepo with more
CLAUDE.md files than that, the ones past the cutoff don't get read — quietly,
with no notice in the report.

## Close

**BCRY — carry-out**
Claude scores your CLAUDE.md against a fixed rubric before it touches a
single line, and every change after that arrives as a diff with a reason —
never a silent rewrite.

**BHTF — your turn**
Your turn. Paste this into Claude: Check and improve my CLAUDE.md files.
Watch for three things. Does it output a quality report, with a grade,
before proposing any change? Are the proposed changes shown as a diff, each
with a one-line reason? And if your repo has more than fifty CLAUDE.md
files, does anything tell you some got skipped?

**BOUT — outro**
It Scores Before It Edits. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is whether asking Claude to "improve" a CLAUDE.md means an immediate rewrite |
| Wrong guess | B00 (WRITER LAW) | "rewrite" corrected to "score" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the five file locations and the six-criterion rubric; the phase order (discover → score → report → approve → diff) and the diff-with-why format |
| Anchor | the Claude MD Improver skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete cost of the fifty-file cap (files past it are silently unscored); BCRY states the design's payoff and its boundary together (you always get a report and a diff-with-why, but that report can itself be incomplete past fifty files) — together they cover what the gate catches and what it can miss, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the source Claude MD Improver skill specifies (the five-location taxonomy,
the six-criterion rubric with A–F grades, the report-before-update hard
gate, the diff-with-why format, and the `head -50` discovery cap) — not an
inference about hidden model internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B05's full "gets it right / where it bites" list (five-location taxonomy,
the report-before-update hard gate, the weighted six-criterion rubric, the
diff-with-why format, the user tips — versus the unattended-confirmation
gap, unclear weight arithmetic, the external template reference with no
fallback, the `head -50` silent truncation, and no guidance for when the
structure itself is the problem) is compressed into NB03, keeping only the
single fact a general audience needs and can act on — the concrete
fifty-file discovery cap — and dropping the Claude-harness-internals gaps
(unattended-session confirmation, criterion weight arithmetic, external
template fallback, "preserve structure" ambiguity) that assume a technical
audience simple/hai-simple doesn't target; Teardown framing ("gets it
right," "where it bites") is stripped to a plain mechanism-and-consequence
description, per the NO JUDGMENT register check; BVDT's verdict facts (the
five-location taxonomy, the report-before-update gate, the diff-with-why
format) are merged into the single BCRY carry-out sentence rather than kept
as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's prompt ("Check and improve my
CLAUDE.md files.") carried over unchanged — it was already a concrete,
paste-ready prompt needing no extra setup, so it's actually runnable by any
viewer today; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ClaudeMdImproverLocations` / `ClaudeMdImproverWorkflow` /
`ClaudeMdImproverTell` / `ClaudeVerdictArtifact`) with B00 as a typed
composer ask (REMOTION, not AI-VIDEO — the source never called a generation
service). NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's cold
open, which this redo replaces per hai-simple's mandate anyway.
