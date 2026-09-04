# SCRIPT.md — A Router, Not A Writer. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-internal-comms` (Teardown, walks the Anthropic
`internal-comms` Claude Skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude just writes a team update however it sounds best.
It doesn't — it identifies the comm type, then follows a fixed format.
Does it just write it, or format it?

*(Text typed on screen: "I ask Claude / for a weekly / update. Will it /
just write it?" — trigger word "write" corrects to "format", landing on:
"I ask Claude for a weekly update. Will it just format it?" Params reused
verbatim from the `claude-plugins-official--claude-liam-command-development`
sibling's already-proven-safe values (42ms/char, 4% mistakeRate, 8%
hesitateBetween) — no overrun.)*

## Body — routing anatomy, the 3P format, clear vs. unclear type

**NB01 — Seven types, four files** (source B01, routing)
The skill covers seven kinds of internal writing, all mapped to four
guideline files. A 3P update routes to the 3P guide. A company newsletter,
an FAQ answer, and the rest — status reports, leadership updates, project
updates, incident reports — route to their matching file, or to a
general-comms file if nothing else fits. The rule: the guideline file is
authoritative. Identify the type first, load the file, then follow its
instructions exactly.

**NB02 — The 3P format, verbatim** (source B02, self-demo)
The 3P format is the most constrained of the four. Always the same
structure: one emoji that captures the team's vibe, the team name, and the
dates covered. Then three sections — Progress, Plans, Problems — each one
to three sentences, data-driven, metrics where possible. Bigger teams need
bigger 3Ps; the company level covers hiring and deals, not individual
tasks. Total read time: thirty to sixty seconds.

**NB03 — Clear type, unclear type** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as a both-directions mechanism
description rather than a "gets it right / where it bites" verdict list)
When the type matches one of the seven exactly, the format is fixed and
strict — the guideline file settles it. When nothing matches cleanly, it
falls to general-comms, a looser catch-all, and the result is less
consistent. And when even that's unclear, the skill is built to ask what
type this is, rather than guess.

## Close

**BCRY — carry-out** (absorbs source BVDT verdict)
A team update isn't something Claude writes from scratch — it's a format
Claude looks up first. Identify the type, then follow that file exactly.

**BHTF — your turn**
Your turn. Open a Claude session and paste this: Write a 3P update for the
Product Design team covering last week. Include progress on the onboarding
redesign, plans for user testing, and mention that we are blocked on design
system approvals. Use the internal-comms skill. Then watch whether Claude
uses the exact 3P format: emoji first, then team name and dates, then three
sections — no bullet lists, no prose headers, no more than three sentences
per section. If it writes four sentences in Progress or skips the emoji,
the format was not followed exactly.

**BOUT — outro**
A Router, Not A Writer. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an audience question — does Claude just write the update, or look up a format first? |
| Wrong guess | B00 (WRITER LAW) | "write" corrected to "format" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the seven-type-to-four-file routing table; the 3P format's exact structure and sentence limits |
| Anchor | the internal-comms routing system itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one routing system), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 | states what happens when the type matches exactly (fixed, strict format) versus when it doesn't (looser general-comms catch-all, or an explicit ask) — the source's teardown insight (router works cleanly / general-comms is fuzzier / ask when unclear) restated as mechanism, not verdict |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `internal-comms` Skill's SKILL.md and its example files specify (the
seven-type taxonomy, the four guideline files, the 3P format's exact fields
and sentence limits, the general-comms fallback, and the ask-when-unclear
rule) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (routing anatomy) +
B02 (3P self-demo) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your
turn) + BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced
1:1 with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per
WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one
beat each; B05's "router insight + gets-right/bites" analysis is compressed
into NB03, keeping the two facts a general audience needs and can act on —
the routing works cleanly on an exact match, and is looser on a fallback —
while dropping the Claude-internals-flavored gaps (that guideline files
must be populated and maintained by the team, that the FAQ format needs
company-wide source access Claude may not have) that assume a
producer/maintainer audience simple/hai-simple doesn't target; Teardown
framing ("what it gets right," "where it bites") is stripped to a plain
mechanism-and-consequence description, per the NO JUDGMENT register check;
BVDT's verdict facts (format router, 3P structure, ask when unclear) are
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's prompt (a 3P update for the Product
Design team, covering onboarding redesign / user testing / design-system
blocker) carried over unchanged — it was already a concrete, paste-ready
prompt needing no extra setup, so it's actually runnable by any viewer
today; BOUT kept, re-skinned to the Humanitarians AI outro (`OutroSeries`).
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source
exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`InternalCommsAnatomy` / `InternalComms3P` / `InternalCommsTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
