# SCRIPT.md — Same Data, Same Packet. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-client-review` (Teardown, walks the Anthropic
`client-review` financial-services Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude's client-review capability was a built-in portfolio
analysis app. It isn't — it's a plain-text skill Claude reads. So: does
Claude's client-review skill analyze the portfolio, or does it just
assemble the meeting?

*(Text typed on screen: "Does Claude's / client-review app / analyze the
portfolio, / or build the packet?" — trigger word "app" corrects to
"skill", landing on: "Does Claude's client-review skill analyze the
portfolio, or build the packet?" Rates (42ms/char, 4% mistakeRate, 8%
hesitateBetween) taken directly from the already-validated hai-simple fix
pattern proven on the `client-report` and `agent-development` siblings.)*

## Body — anatomy, pipeline, spec vs. gaps

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it works. This one is
client-review. The SKILL.md file holds the full instruction set — plain
language, no hidden logic. Claude reads it, then acts. The file is the
program.

**NB02 — Read, execute, return** (source B02, pipeline)
The pipeline lives in the file's Steps section. Claude reads the file, runs
each step in order, and returns the result — linear, no branching unless a
step itself says so.

**NB03 — Spec it, or Claude reasons past it** (source B03 design tell +
BVDT verdict facts — re-registered Teardown → Plain, and reframed as the
reel's BOTH-DIRECTIONS beat: what the file's coverage guarantees, and what
it doesn't)
Client-review's SKILL.md spells out exactly what to produce: a portfolio
performance summary, allocation analysis, talking points, and action items,
ready before quarterly reviews, annual checkups, or an ad-hoc client
meeting. Feed it the same account data twice, and it builds the same
meeting-ready packet twice. Ask for something the file doesn't cover — a
comparison it never mentions, a chart it doesn't list — and there's no
instruction to fall back on, so Claude reasons past the file on its own.

## Close

**BCRY — carry-out**
A Claude skill isn't a hidden analysis app — it's a plain-text file of
instructions, so the same account data builds the same meeting-ready packet
every time. Whatever that file doesn't say, Claude has to work out on its
own.

**BHTF — your turn**
Your turn. Paste this into Claude: write a SKILL.md for a recurring meeting
you prep for. List exactly what must appear every time, then list what
would be left to my judgment because the file doesn't cover it. Read back
what Claude wrote — the first list is what repeats identically every run;
the second is where it's reasoning past the file, not following it.

**BOUT — outro**
Same Data, Same Packet. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is whether a repeatable, finance-specific capability implies a built-in portfolio analysis app |
| Wrong guess | B00 (WRITER LAW) | "app" corrected to "skill" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | a skill is a folder holding one file (SKILL.md), read in plain language, no hidden logic; the pipeline is linear — read, execute each step in order, return the result |
| Anchor | the client-review skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 | states both what happens when the file covers the request (same account data, same meeting-ready packet, every run) and what happens when it doesn't (no instruction to fall back on, so Claude reasons past the file) — this is the same pair of facts the source's design-tell/verdict beats stated as "gets it right / where it bites" and "know the limit," now stripped of that verdict framing and read as a direct mechanism-and-consequence description |
| Carry-out | BCRY | one sentence pair, survives repetition, directly answers B00's corrected question |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the client-review Skill's SKILL.md specifies (its purpose, its trigger
phrases, the plain-text instruction format, the linear read-execute-return
pipeline, and the consequence of asking for something outside its stated
scope) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design-tell mechanism) + BVDT (verdict) + BHTF (your turn)
+ BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each,
narration already close to Plain in the source (no verdict language to
strip); B03's Teardown framing ("Here is the Teardown moment," "what it
gets right... what it bites") is stripped to a plain mechanism-and-
consequence description in NB03, keeping the same two facts (repeatable on
covered input, no fallback on uncovered input) without the "gets it
right/bites" register; BVDT's verdict facts (repeatable execution, same
input → same output, the limit being only what the file specifies) are
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF is re-purposed
from the source's skill-specific paste-in (which named the exact client-
review trigger phrase, not runnable by a general viewer without that
specific Skill installed) to a generalized, actually-paste-ready prompt —
asking Claude to draft a SKILL.md for the viewer's OWN recurring meeting and
separate what repeats from what needs judgment — which exercises the same
mechanism (file coverage vs. judgment gaps) the video just taught, without
requiring the financial-services plugin; BOUT kept, re-skinned to the
Humanitarians AI outro (`OutroSeries`). Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.

## GATE T fix note

First `type_check.py` pass FAILed on NB01 (§8.1 min-size, 19px < 20px
floor). Root cause traced (not the caption, as the tool's generic message
guessed): the lowercase "i" in the chip label "client-review" rendered with
its dot detached from the stem at the default chip font size (26pt for
≤14-char labels), producing an isolated ~19px blob just under the floor —
an EB Garamond/Manim anti-aliasing artifact, not a genuine legibility
defect (the word reads clearly to a human at every beat's actual on-screen
size, confirmed by frame inspection). Fixed by raising `_chip()`'s font-size
brackets from 26/22/18 to 30/24/20 across all three chip-row beats
(NB01–NB03), which cleared the floor by 3-5px margin on every beat without
changing layout, wording, or the underlying content. Re-rendered all three
Manim beats and recompiled; `type_check.py` went FAIL(1) → PASS(0).
