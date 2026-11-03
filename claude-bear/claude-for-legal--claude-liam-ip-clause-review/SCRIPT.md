# SCRIPT.md — Claude, Ip Clause Review. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-ip-clause-review` (Teardown, walks the Anthropic
`ip-clause-review` legal Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude decides on its own whether an IP clause is any
good. It doesn't decide — it checks a list. So: when Claude reviews an IP
clause, is it checking a list?

*(Text typed on screen: "When Claude reviews / an IP clause, / is it
judging?" — trigger word "judging" corrects to "checking a list", landing
on: "When Claude reviews an IP clause, is it checking a list?")*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is called
ip-clause-review. Its one file, SKILL.md, holds the whole instruction
set — what to look for in an IP clause, written in plain language, no
hidden logic. Claude reads it, then acts. The file is the program.

**NB02 — Read, check, return** (source B02, pipeline)
The checks live in a Steps section. Claude reads each step in order and
applies it to the clause — read the file, apply each check, return the
result. Linear: no branching, unless a step says otherwise.

**NB03 — Licenses it, or assigns it** (source B03/BVDT, design tell /
verdict fact — re-registered Teardown → Plain)
One check inside it is specific: a clause that only grants a license
doesn't move ownership at all. Only a clause that assigns the IP outright —
all right, title, and interest, transferred — actually hands it over. A
clause can read like it hands over ownership and still leave the work with
whoever created it.

## Close

**BCRY — carry-out**
Claude isn't judging whether the clause is good — it's checking, one item
at a time, whether the clause actually assigns the IP instead of just
licensing it.

**BHTF — your turn**
Your turn. Paste this into Claude: here's an IP clause from a contract I'm
reviewing — paste the clause. Read the ip-clause-review skill, and before
you tell me anything's wrong with it, walk me through exactly what you're
checking for.

**BOUT — outro**
Claude, Ip Clause Review. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a legal question — is Claude judging the clause? |
| Wrong guess | B00 (WRITER LAW) | "judging" corrected to "checking a list" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes checks linearly; one specific check governs licensing vs. assignment |
| Anchor | the ip-clause-review Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into BCRY | "checking, not judging — assigns vs. licenses" states both what the mechanism does (a specific check applied) and its limit (only that check, not a verdict on the whole contract), matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: NB01–NB02 are direct descriptions of how any
Skill runs (a folder, one file, steps executed in order) — the same
mechanism already established, unchanged, across the `claude-liam-*` family.
NB03's licensing-vs-assignment distinction is stated as a fact about
contract drafting, not an inference about the Skill's hidden internals, and
needs no flag. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (puppet cold open) + B01/B02/B03 (anatomy / pipeline
/ design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro) — the
shortest shape in the `claude-liam-*` Teardown family, a single-example
skill walkthrough with no wrong-guess, anchor, or both-directions beats of
its own to redistribute. This redo keeps that same 7-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02
kept as one beat each; B03 and BVDT (design tell and verdict) are merged
into the single NB03 mechanism beat plus the BCRY carry-out sentence,
because the source's actual content behind those two beats never got past
an unfilled placeholder (literal `>` marks in `narration_text` — see
QUESTION.md) — there is no locked specific fact to preserve there beyond
"the SKILL.md defines a specific check," so this redo supplies the one
concrete, generically-true check that any IP-clause-review task is actually
for: distinguishing a license grant from an outright assignment. BHTF kept
as the your-turn handoff, with the source's bracketed placeholder
("I want to >") replaced by a concrete, paste-ready scenario so the prompt
is actually runnable today; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (SkillTeardownAnatomy /
SkillTeardownPipeline / SkillTeardownMechanism / ClaudeVerdictArtifact /
ClaudeComposerAsk / ClaudeTitleOutro patterns) with B00 as a typed-UI cold
open (REMOTION `ClaudeComposerAsk`, not AI-VIDEO — the source never called a
generation service). NO-GENAI/NO-PANTRY LAW required no substitution beyond
B00's cold open, which this redo replaces per hai-simple's mandate anyway.
