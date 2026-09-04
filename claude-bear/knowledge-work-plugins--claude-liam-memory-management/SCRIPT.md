# SCRIPT.md — Notes, Not Recall. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-memory-management` (Teardown, walks the Anthropic
`memory-management` productivity Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude just remembers your team, the way a person would.
It doesn't — it reads notes you write down. So: does Claude actually read
notes about our team?

*(Text typed on screen: "Does Claude / actually remember / our team?" —
trigger word "remember" corrects to "read notes about", landing on: "Does
Claude actually read notes about our team?")*

## Body — two files, the read-then-decode pipeline, what's actually in there

**NB01 — Two files, one job** (source B01, anatomy — also carries the
two-tier fact originally stated in the source's B00 cold open, since that
beat is replaced here per WRITER LAW and its facts must survive somewhere)
A skill is a folder Claude reads before it works. This one is
memory-management, and it runs on two files. CLAUDE.md holds working
memory — the handful of facts Claude keeps in view on every request. The
memory directory holds the fuller knowledge base, the details CLAUDE.md
doesn't have room for. Claude reads both, then acts. The files are the
program.

**NB02 — Read, then decode** (source B02, pipeline — also carries the
source B00 fact about decoding shorthand/acronyms/nicknames, for the same
reason as NB01)
The steps run in order: read CLAUDE.md, then check the memory directory
for anything relevant to the request. That's what lets Claude decode a
team's shorthand — an acronym, a nickname, an inside phrase — the same way
a colleague who'd been there a while would, instead of asking what it
means every time.

**NB03 — What's actually in there** (source B03, design tell — re-registered
Teardown → Plain: the source's framing, "the interesting constraint... a
deliberate trade-off," is a design verdict and is cut; the underlying fact,
the example memory entry itself, is kept unchanged)
Here's what a memory entry actually looks like: "Cubs fan, likes talking
baseball." That's the kind of personal, informal detail the memory
directory stores about a colleague — not just their title or their last
ticket — so Claude can recognize the small talk and the shorthand, not
only the task.

## Close

**BCRY — carry-out** (source BVDT, verdict — re-registered Teardown → Plain:
the source's "same input, same output, every run... know the limit" is a
reliability verdict and is cut; the underlying fact, that the memory files
are what Claude reads rather than something the model has on its own, is
kept and compressed to one carry-out sentence, per CARRY-OUT LAW)
Claude's memory isn't something it has — it's notes your team wrote down,
that Claude reads before it acts. Same notes, same read, every time.

**BHTF — your turn**
Your turn. Paste this into Claude: Read the memory-management skill, then
set up a starter CLAUDE.md and a memory directory for my team, using three
real facts I give you about a teammate. Then check what Claude put where.
Did the quick, every-request facts land in CLAUDE.md, and the fuller
background in the memory directory? Did it actually read the SKILL.md's
steps in order, or skip straight to writing files? That's the real test of
whether the two-tier split is doing its job.

**BOUT — outro**
Notes, Not Recall. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a recall question — does Claude just remember your team on its own? |
| Wrong guess | B00 (WRITER LAW) | "remember" corrected to "read notes about" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the two-file split (CLAUDE.md / memory directory) and the read-CLAUDE.md-then-check-memory pipeline that lets Claude decode a team's shorthand |
| Anchor | the memory-management skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete kind of detail the memory directory actually stores (personal/informal, not just title or ticket history); BCRY states what that buys and what it depends on together (Claude acts like it knows you because the notes are there; it knows nothing you or your team never wrote down) — together they cover what the two-tier design catches and what it can't, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the memory-management Skill's SKILL.md specifies (the two-tier CLAUDE.md /
memory directory split, the read-then-decode pipeline, and the kind of
detail — like the "Cubs fan" example — that the memory directory holds) —
not an inference about hidden model internals. Per simple's ONE-FLAG LAW,
when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat, and absorbing the source B00 cold open's two
facts — the two-tier system and the shorthand-decoding purpose — into
NB01/NB02 since that beat no longer exists); B01→NB01, B02→NB02 kept as
one beat each; B03's design-tell fact (the "Cubs fan, likes talking
baseball" example entry) is kept unchanged in NB03, with the source's
Teardown framing ("the interesting constraint," "a deliberate trade-off")
stripped to a plain description of what the entry is and why it matters,
per the NO JUDGMENT register check; BVDT's verdict facts (files as the
source of truth, same input/same output, the limit being only what the
file says) are merged into the single BCRY carry-out sentence rather than
kept as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as
the your-turn handoff — the source's prompt was a garbled, non-runnable
fragment ("I want to two-tier memory system that makes claude a true
workplace collaborator. decodes ."), so a new, genuinely paste-ready prompt
was written carrying the same teaching point (set up the two-tier files,
then check that Claude actually split the facts CLAUDE.md-vs-memory the
way the Skill specifies); BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway. NB01–NB03 were rebuilt as a
generic Manim "chip row" template (rather than reusing
`SkillTeardownAnatomy`/`Pipeline`/`Mechanism` verbatim) because
`ClaudeVerdictArtifact`'s verdict framing and the Teardown-genre visual
language of that template family carry design-judgment connotations this
Plain-register redo needs to avoid; the chip row is a neutral structural
diagram with no built-in verdict semantics.

## Source data-quality note

The source narration for B00 and BHTF contained garbled, apparently
mis-substituted text (e.g. "CLAUDE.md for working memory, memory/ directory
for the full knowledge base.." with a stray double period; BHTF's "I want
to two-tier memory system that makes claude a true workplace collaborator.
decodes ." trailing off mid-sentence) — template placeholder substitution
that did not fully resolve. This redo keeps the underlying facts (two-tier
file split; decodes shorthand/acronyms/nicknames) unchanged but restates
them as grammatical sentences rather than reproducing the garbling
verbatim, since the LOCKED SCRIPT contract binds facts and argument, not a
transcription defect.
