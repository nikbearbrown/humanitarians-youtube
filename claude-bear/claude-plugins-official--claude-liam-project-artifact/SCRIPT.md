# SCRIPT.md — Snapshot, Not Sensor. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-project-artifact` (Teardown, walks the Anthropic
`project-artifact` Claude Code plugin Skill — tabbed HTML status pages
published via Claude's Artifact tool) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a status page watches your data and updates itself. It
doesn't — it waits until you ask. So: does my project page wait for my data,
and update only when I ask?

*(Text typed on screen: "My project page / watches my data / and updates /
itself?" — trigger words "watches" and "itself" correct to "waits for" and
"when I ask", landing on: "My project page waits for my data and updates
when I ask?" Two corrections in one beat, positionally matched
(`triggerWords: "watches, itself"` / `replacementWords: "waits for, when I
ask"`), both landing the same wrong guess: the page does not watch, it
waits.)*

## Body — tab catalog, config and state, the refresh mechanism

**NB01 — Two tabs always, five that earn it** (source B01, anatomy — tab
catalog half)
Open a project page and two tabs are always there: Overview, with the
project name, a status badge, and a one-line summary — and Workstreams, the
named tracks of work with their status, owner, and dates. Five more tabs
exist, but they only appear when there's something to put in them:
Attention, for blockers that need a decision now; Background, for context
that would clutter the Overview; Plan, for what's coming; Risks and open
questions; and Decisions and FAQ, for choices already made and why.

**NB02 — One config file, and a saved record** (source B01, config-structure
half + B02, "gather sources first" pattern)
All of it comes from one config file, in four parts. Project holds the name
and a running summary. Sources lists exactly what to read before writing a
single tab — documents, data, anything live — and everything gets gathered
before any tab gets written. People lists who owns what. And every time the
page publishes, something else gets saved with it: a block of stored data,
tucked inside the page itself, recording exactly what was shown. That stored
block is what makes the next update possible without starting from nothing.

**NB03 — Nothing updates on its own** (source B02, refresh/delta pattern +
B05, "delta requires previous render on disk" gap — re-registered Teardown →
Plain, kept as the single most teachable fact rather than the full "gets it
right / where it bites" list; this is the beat that resolves B00's wrong
guess)
Here's the part that surprises people: nothing updates on its own. The page
doesn't watch your data — it waits. You have to ask for a refresh. When you
do, it looks for that stored block from last time. If it's there, the page
compares old to new and shows only what changed. If it isn't — because the
page was never saved, or got deleted — there's nothing to compare against,
and the whole page gets rebuilt from scratch, with no change summary at all.

## Close

**BCRY — carry-out**
A project status page is a snapshot, not a sensor — it never watches your
data on its own. It only updates when you ask, and it only knows what
changed because it saved a record of what it looked like last time.

**BHTF — your turn**
Your turn. Paste this into Claude: Build a project status page for my API
migration, with workstreams, an open risk, and a decisions log. Once it's
built, ask for a refresh without changing anything — does it say nothing
changed, or does it silently rewrite the whole page? Then close out that
risk and refresh again. Does it call out exactly that change, or does it act
like it's starting from zero? That's the real test of whether the page
remembers.

**BOUT — outro**
Snapshot, Not Sensor. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a currency question — does a status page keep itself current, or does something else have to happen? |
| Wrong guess | B00 (WRITER LAW) | "watches"/"itself" corrected to "waits for"/"when I ask" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the two-always/five-conditional tab catalog, and the config file plus stored state block that makes a later refresh possible |
| Anchor | the project-artifact skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states both outcomes of asking for a refresh (a stored block present → delta only; a stored block missing → full rebuild, no change summary); BCRY states the design's payoff and its dependency together (a saved record makes delta possible; no saved record, no delta) — together they cover what a refresh can and cannot do, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the project-artifact Skill's SKILL.md specifies (the two-always/five-
conditional tab catalog, the four-section config file, the state block
embedded in every publish, and the delta-vs-rebuild refresh behavior) — not
an inference about hidden model internals. Per simple's ONE-FLAG LAW, when
the source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01's two halves (tab catalog, config
structure) split across NB01/NB02; B02's four patterns compressed — "gather
sources first" folded into NB02, "delta vs. re-narrative on refresh" folded
into NB03, and the two patterns aimed at a technical builder audience
("pick tabs before generating HTML", "embed the state block in every
publish" as an authoring instruction) dropped as build-time guidance a
general viewer doesn't act on; B05's long "gets it right / where it bites"
list (five strengths, five gaps including claude.ai-login requirement,
machine-local config, delta's disk-state precondition, template-vs-in-place
refresh behavior, and pattern-based injection flagging) is compressed into
NB03, keeping only the single fact a general audience needs and can act on
— the concrete "no stored record, no delta" mechanism — and dropping the
Claude-harness/security-internals gaps (claude.ai account requirement,
machine-local config sync, entity-encoding and CSP details, injection-
flagging limits) that assume a technical or security-reviewer audience
simple/hai-simple doesn't target; Teardown framing ("gets it right," "where
it bites") is stripped to a plain mechanism-and-consequence description, per
the NO JUDGMENT register check; BVDT's verdict facts (the tab catalog, the
config/state-block architecture, and the delta precondition) are merged into
the single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's prompt ("Build a live project status page for my API migration
with workstreams, risks, and a decisions log") carried over in substance
(trimmed to "an open risk" and "a decisions log" to match a single concrete
worked example) — already a concrete, paste-ready prompt needing no extra
setup, so it's actually runnable by any viewer today; BOUT kept, re-skinned
to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT =
7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ProjectArtifactAnatomy` / `ProjectArtifactDesign` / `ProjectArtifactTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
