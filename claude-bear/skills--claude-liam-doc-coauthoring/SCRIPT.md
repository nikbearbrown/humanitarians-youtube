# SCRIPT.md — Claude, Tested by a Stranger (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-doc-coauthoring` (Teardown, source skill
`anthropics/skills/skills/doc-coauthoring/SKILL.md`) — question, facts, and
body argument carried over unchanged; narration re-registered to Plain
(explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

Carry-out written first — see CARRY-OUT.md (GATE C).

## B00 — cold open (BrutalistHesitantWriter)
People ask if Claude can just write their doc for them. Not quite — can
Claude write my technical doc with me? That's the real question, and
there's a specific three-stage way it answers it.

Typed text: "Can Claude write\nmy technical doc\nfor me?" — trigger word
"for" corrects to "with", landing on "Can Claude write my technical doc
with me?"

## Act I — Stakes and the wrong guess

**NB01 — The spec reads great, to you** (source B01/B02 — ANCHOR PLANTED)
Say you ask Claude for a technical spec on the new payments API. It comes
back polished and confident — and it reads perfectly, because you already
know what "the settlement window" means.

**NB02 — More detail doesn't fix a blind spot** (WRONG-GUESS, falsified)
The obvious fix is more detail — describe it better and the doc improves.
But you can't explain a term you don't know needs explaining. More words
from you don't touch a blind spot that's yours.

## Act II — The three-stage mechanism

**NB03 — Stage 1: close the gap** (source B02)
Stage one closes the knowledge gap before any writing starts. Claude asks
five meta-questions — document type, audience, impact, template,
constraints — then asks for the full context dump. It stops once it can
ask about edge cases without needing the basics explained.

**NB04 — Stage 2: per-section loop** (source B03)
Stage two builds section by section, in a repeating loop: clarify with
questions, brainstorm five to twenty options, then you curate — keep, cut,
or combine.

**NB05 — The quality gate** (source B03)
After three rounds with no real change, Claude asks what can be cut. Near
the end, it re-reads the whole document, hunting for redundancy and
anything that reads like generic filler.

**NB06 — Stage 3: a reader who wasn't there** (source B04)
Stage three hands the finished sections to a fresh Claude — no memory of
this conversation. It reads cold and asks what a real reader would ask. In
Claude Code that runs automatically, as a sub-agent; elsewhere, you open a
new chat and do it yourself.

## Act III — Anchor payoff and both directions

**NB07 — The reader stops here** (ANCHOR PAYOFF)
Back to that payments spec: the fresh Claude stops cold at "the settlement
window" — it has no idea what that means, because nobody ever defined it.
That's the blind spot you couldn't see, caught by someone who wasn't in the
room.

**NB08 — What the test proves** (DIRECTION A)
When the fresh Claude stops finding new questions, that's the exit signal —
a structural test, not a guess. It catches exactly the kind of gap a reader
as familiar as you would walk straight past.

**NB09 — What it doesn't fix** (DIRECTION B)
It doesn't fix everything. This is a long workflow, built for documents
that get reviewed at scale — not a five-minute update. And if you patch the
doc yourself without saying so, the next refine step is working from a
draft that's already gone stale.

## Close

**BCRY — carry-out**
Writing sounds finished when it's actually just familiar to you. The
doc-coauthoring skill won't call it done until a Claude with none of your
context can read it cold and get it right.

**BHTF — your turn**
Your turn. Paste this into Claude: I need to write a decision doc about
migrating our auth service to OAuth 2.0 — walk me through the
doc-coauthoring workflow. Then watch what happens before it writes a single
word: does it ask you five context questions first? Does it wait for your
full context dump before drafting? That's the whole gate.

**BOUT — outro**
Doc Co-Authoring — writing with Claude, tested by a reader who wasn't in
the room. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–NB01 | a draft that reads fine to its author looks finished; the reader hasn't been asked yet |
| Wrong guess | NB02 | "just describe it better" falsified — you can't name a blind spot you don't know you have |
| Mechanism | NB03–NB06 | Stage 1 context gathering, Stage 2 per-section loop + quality gate, Stage 3 reader testing |
| Anchor | NB01 → NB07 | the payments-API spec and its undefined "settlement window", planted early, paid off when the fresh Claude stalls on the same term |
| Both directions | NB08 → NB09 | what a clean reader-test proves (a real structural signal) / what it doesn't fix (long workflow, and it breaks if edits bypass the loop) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim — the trigger conditions, the
three stages, the five meta-questions, the six-step per-section loop, the
three-iteration quality gate, the reader-testing exit condition, the
Claude Code vs. claude.ai mechanics — is a direct description of documented
skill behavior (see SOURCES.md), not an inference about hidden internals.
Per ONE-FLAG LAW, when the source genuinely supports everything as stated,
no flag is fabricated.

## Beat-count note (redo)

Source is 9 beats (claude-explainer + skill-teardown chassis: B00 cold open,
B01 anatomy, B02–B04 the three stages, B05 teardown moment, BVDT verdict,
BHTF handoff, BOUT outro). hai-simple's spine has no separate verdict-recap
beat (Plain register carries one carry-out sentence, not a bulleted recap —
CARRY-OUT LAW) and no design-judgment beat (NO JUDGMENT check), so: BVDT's
verdict bullets are re-expressed as BCRY's single carry-out sentence rather
than kept as a recap; B05's Teardown "what it gets right / what it costs"
framing is split into its factual halves and re-homed as NB08 (what the
reader-test structurally proves — was "gets right") and NB09 (the two real
limits: workflow length, and the str-replace/direct-edit fragility — was
"costs"), stated as mechanism and limits rather than a verdict on the
skill's design. B01's anatomy content (trigger conditions, doc types) is not
carried as its own beat — the video opens directly on the anchor scenario
(NB01) instead of a separate trigger/taxonomy card, since "PRD vs. RFC vs.
decision doc" is a list with no payoff of its own in a 2–3 minute Plain cut.
Net: 9 source beats -> 13 hai-simple beats (B00, NB01–NB09, BCRY, BHTF,
BOUT) — more granular, not fewer, because the source's three stage-beats
(B02–B04) each carried enough distinct mechanism (meta-questions info dump,
six-step loop, quality gate, reader-testing exit condition, Claude
Code/claude.ai split) to warrant splitting Stage 2 into NB04/NB05 for
pacing (one idea per beat, per BODY GRAPHIC beat law) rather than
compressing. No source beat was ai-video-prompt, pantry, or a human-drop
slot — the source was already entirely REMOTION (DocCoauthoringAnatomy/
Stage1/Stage2/Stage3/Tell, all custom Claude-palette components) — but
those components hardcode the Claude token palette with no palette prop,
so the CHANNEL SKIN law (humanitarians palette throughout, not just B00/
outro) required rebuilding the body as GRAPHIC/manim chip-row beats in the
humanitarians palette rather than reusing the source components as-is.
Logged per BUILD-LOG.md.
