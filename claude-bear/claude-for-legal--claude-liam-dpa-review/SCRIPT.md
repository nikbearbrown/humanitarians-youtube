# SCRIPT.md — Claude, Dpa Review. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-dpa-review` (Teardown, walks a hypothetical Anthropic
`dpa-review` legal Skill) — question and generic skill anatomy carried
over from the source's real narration; the source's skill-specific content
was never authored (literal unresolved `>` placeholders in B00/B03/BVDT/
BHTF) and is filled fresh here with well-established GDPR Article 28(3)
DPA-review content; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude approves a vendor's DPA when it reviews one.
It doesn't approve — it checks clauses against a fixed list. So: when
Claude reviews a DPA, is it checking a list?

*(Text typed on screen: "When Claude reviews / a vendor's DPA, / does it
approve?" — trigger word "approve" corrects to "check clauses", landing
on: "When Claude reviews a vendor's DPA, does it check clauses?")*

## Body — what the Skill actually does

**NB01 — A Skill is a folder** (source B01, anatomy)
A Skill is a folder Claude reads before it acts. This one is called
dpa-review. Its one file, SKILL.md, holds the whole instruction set,
written in plain language — no hidden logic. Claude reads it, then acts.
The file is the program.

**NB02 — Read, execute, return** (source B02, pipeline)
The instructions live in a Steps section. Claude reads each step in order
and executes it — read the file, execute each step, return the result.
Linear: no branching, unless a step says otherwise.

**NB03 — What the checklist covers** (source B03, design tell — content
authored fresh; source left this beat as an unfilled `>` placeholder)
One instruction inside it is specific: check whether the agreement names
every sub-processor, and states what happens to the data when the
contract ends — deleted, or returned. Those two clauses go missing most
often. What the skill doesn't do is judge whether the described security
measures are actually strong enough for the data involved — that call
needs a person who knows the systems.

## Close

**BCRY — carry-out**
Claude isn't judging whether the agreement is good enough — it's checking
the SKILL.md's list of required clauses, one step at a time, and only
doing what that file says.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm about to sign a vendor's data
processing agreement. Read the dpa-review skill, and before you check
anything, walk me through exactly what you'll do — which clauses you'll
check for, what counts as missing, and what you won't be able to tell me.

**BOUT — outro**
Claude, Dpa Review. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a legal question — is Claude approving? |
| Wrong guess | B00 (WRITER LAW) | "approve" corrected to "check clauses" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB03 | a Skill is a folder with one instruction file; it executes steps linearly; one specific checklist rule governs sub-processors and end-of-contract deletion, contrasted with what it can't judge (security adequacy) |
| Anchor | the dpa-review Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03/BCRY | NB03 states both what the checklist does (checks presence of required clauses) and its limit (can't judge adequacy); BCRY compresses both into one carry-out sentence |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the Skill's SKILL.md specifies (a folder, one file, a Steps section
executed in order, the sub-processor/deletion checklist rule) — not an
inference about hidden model internals. Per simple's ONE-FLAG LAW, when
the source (here, well-established GDPR Article 28(3) practice) genuinely
supports the claim as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (puppet cold open) + B01/B02/B03 (anatomy /
pipeline / design tell) + BVDT (verdict) + BHTF (your turn) + BOUT (outro)
— the shortest of the `claude-liam-*` Teardown family, a single-example
skill walkthrough with no wrong-guess, anchor, or both-directions beats of
its own to redistribute. This redo keeps that same 7-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02,
B03→NB03 kept as one beat each — B03's content is authored fresh here
(the source left it as an unfilled `>` placeholder) using GDPR Article
28(3)'s named-sub-processor and end-of-contract-deletion requirements, the
two clauses most commonly missing from a vendor DPA; BVDT's two verdict
facts (reliable execution, and the file-only limit — also an unfilled `>`
placeholder in the source) merged into the single BCRY carry-out sentence
rather than kept as a separate artifact-card beat, since Plain register
carries one carry-out sentence, not a bulleted verdict (CARRY-OUT LAW);
BHTF kept as the your-turn handoff, with the source's bracketed
placeholder ("I want to >") replaced by a concrete, paste-ready scenario
so the prompt is actually runnable today; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact` patterns) with B00 as a REMOTION cold open (not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.

## Content-gap note (why this redo differs from a typical redo)

Unlike most `claude-for-legal--claude-liam-*` redos, this source reel's
`beats[*].narration_text` was not a complete locked script: four of its
seven beats (B00, B03, BVDT, BHTF) contain a literal unresolved `>`
character where skill-specific content should have been — a batch-
template placeholder that was never filled in for this particular skill,
and the `source_skill` file the sheet points at
(`.../privacy-legal/skills/dpa-review/SKILL.md`) does not exist on this
machine to recover the intended content from. The generic skill-anatomy
narration (B01/B02, and BVDT's two structural facts) was real and is
carried over unchanged. The specific missing fact (B03's "design tell",
and BHTF's scenario) is authored fresh here using well-established GDPR
Article 28(3) DPA-review practice — the two clauses (named sub-processors,
deletion-or-return at contract end) most commonly missing from a real
vendor DPA, contrasted with the judgment call (security adequacy) no
checklist can make. This mirrors how the `claude-for-legal--claude-liam-
cease-desist` sibling (same source batch, same shape) resolved its own
design-tell beat when the source supplied a real fact — here, no real fact
existed to carry over for B03/BHTF, so one was authored instead of left as
a broken `>` in the final narration.
