# SCRIPT.md — Four Layers, Not One File. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-config-guide` (Teardown, walks the `config-guide`
Skill) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians
AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude's settings live in one file. They don't — they
live in four layered objects, and the skill routes each question to one
of five reference files. So: where's the layer that holds mine?

*(Text typed on screen: "Where's the file / with Claude's / settings?" —
trigger word "file" corrects to "layer", landing on: "Where's the layer
with Claude's settings?")*

## Body — the four-layer model, the index design, the silent-failure risk

**NB01 — Four layers, one index** (source B01, anatomy)
Claude's configuration model has four layers. Agents sit at the top.
Agent scopes control how settings resolve and inherit, field by field,
across a workspace. Identity profiles carry scopes, rules, credentials,
and repo permissions. And presets, connections, GitHub repos, and custom
instructions attach to each profile. The skill itself doesn't hold the
answer — it's an index. Ask a question, and it opens one of five
reference files: agents and scopes, identity profiles, connections and
presets, GitHub and instructions, or best practices.

**NB02 — Slack only, verify fresh** (source B02, design + Slack scope +
debug-plugins handoff)
Splitting the skill into five short files instead of one long one is
deliberate — each reference stays focused. Right now, the guide covers
only the Slack surface; it doesn't say what changes elsewhere. And after
explaining any of this, the skill always closes the same way: it points
you to debug-plugins, run in a brand-new Slack thread — a fresh thread
means a fresh container, reflecting your current configuration instead of
a cached one.

**NB03 — Quiet when a file's missing** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's the risk worth knowing: this only works because all five reference
files are actually there. If one goes missing, nothing breaks loudly — the
skill just doesn't answer that part of your question, and you won't get
an error telling you why.

## Close

**BCRY — carry-out**
Claude's settings live across four layers, not one file — the guide's
whole job is routing you to the right one, and it goes quiet, not loud,
if that file is missing.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm designing settings for an app with
company-wide defaults, team overrides, and per-user overrides layered on
top of each other. Walk me through structuring that as layered objects —
like agents, scopes, and profiles — so a user's change never gets silently
overwritten by a team default. Then show me one way the design could
quietly fail if a piece of it goes missing.

**BOUT — outro**
Four Layers, Not One File. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a lookup question — where's the file with my settings? |
| Wrong guess | B00 (WRITER LAW) | "file" corrected to "layer" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the four-layer model and the five-file index it routes questions to; the Slack-only scope and the debug-plugins verify step |
| Anchor | the config-guide Skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what happens when the index is missing a file (goes quiet, not loud); BCRY states the rule's scope (four layers, one router, silent on a gap) — together they cover what the design does and what it never does, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the config-guide Skill's source material specifies (the four-layer
model, the five reference files, the Slack-only scope, the debug-plugins
new-thread handoff, and the silent-failure behavior of a missing
reference) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02
(anatomy/design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your
turn) + BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced
1:1 with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per
WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one
beat each; B05's "gets it right / where it bites" list (four-layer model
named, Slack caveat stated upfront, index pattern is good design, the
read-only tool restriction, the debug-plugins handoff — versus the silent
index failure, the Slack-only caveat's silence on other surfaces, the
topic table not being self-describing, no admin-permissions guidance, and
the unexplained new-thread reason) is compressed into NB03, keeping only
the single fact a general audience needs and can act on — the index goes
quiet rather than erroring when a reference file is missing — and dropping
the Claude-Code-implementation-detail gaps (admin permissions, the topic
table's self-describing-ness) that assume a technical/admin audience
simple/hai-simple doesn't target; the new-thread reason (source's stated
gap: "says new thread without explaining why") is in fact answered
in-reel at NB02 (container isolation), so it is not re-listed as a gap;
Teardown framing ("gets it right," "where it bites") is stripped to a
plain mechanism-and-consequence description, per the NO JUDGMENT register
check; BVDT's verdict facts (the four-layer/five-file structure, the
Slack scope, the debug-plugins handoff, the silent-failure gap) are merged
into the single BCRY carry-out sentence rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn
handoff, with the source's admin-only, Slack-workspace-specific
instructions ("ask how agents and agent scopes work in @Claude") replaced
by a concrete, paste-ready prompt that needs no @Claude admin access, so
it's actually runnable by any viewer today; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ConfigGuideAnatomy` / `ConfigGuideDesign` / `ConfigGuideTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
