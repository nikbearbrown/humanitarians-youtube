# SCRIPT.md — Only the Terminal Says Yes. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-access` (Teardown, walks the Anthropic Discord
`access` Skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed asking on Discord itself was enough to get approved. It
isn't — only a command typed in your own terminal counts. So: if you ask
in the terminal instead, does that work?

*(Text typed on screen: "If I ask in Discord / to be approved, / does
that / work?" — trigger word "Discord" corrects to "the terminal",
landing on: "If I ask in the terminal to be approved, does that work?")*

## Body — the state model, the approval flow, why it refuses

**NB01 — One file, one rule first** (source B01, anatomy + security model)
The skill's state lives in one file: access.json, under
~/.claude/channels/discord/. It holds five fields — the DM policy, the
allow list, per-channel groups, pending pairing codes, and the patterns
that trigger the bot. If the file is missing, Claude just uses safe
defaults. And before any of those fields get touched, one rule runs
first: if the request arrived as a message on Discord rather than
something you typed yourself, Claude refuses it — Discord messages can
carry hidden instructions, so they're never trusted with access changes.

**NB02 — Approve, then guard it** (source B02, command dispatch +
implementation rules)
Approving someone follows one path: pair, with a code. Claude checks the
code hasn't expired, adds that person's ID to the allow list, deletes the
pending entry, and writes a small marker file in an approved folder — the
Discord side watches that folder and sends the confirmation. Two rules
guard this: always read the file fresh before writing, since a new
pairing code might have shown up in between; and never auto-pick a
pending code on its own, even if there's only one.

**NB03 — The attack this stops** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's why that matters. Someone could DM the bot pretending they want
in — that alone creates a pending code, nothing more. But if Claude
trusted Discord messages, that same person could send a second message
posing as you: approve the pending request. Refusing anything that isn't
typed in your own terminal is exactly what stops that second message from
working.

## Close

**BCRY — carry-out**
Claude only trusts an access change typed into your own terminal — never
one that just shows up as a Discord message, no matter how convincing it
looks.

**BHTF — your turn**
Your turn. Paste this into Claude: Design a simple access-control file
for a chat bot I run — one JSON file with a policy, an allow list, and
pending approval codes that expire. Add one rule: only accept an approval
if I type it directly to you, never if it arrives as a message from the
channel itself. Walk me through the file's shape and explain the one
attack that rule stops.

**BOUT — outro**
Only the Terminal Says Yes. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a security question — does asking on Discord itself work? |
| Wrong guess | B00 (WRITER LAW) | "Discord" corrected to "the terminal" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | one state file with five fields, checked against a terminal-only rule before anything else; the pair-approval flow and its two guard rules |
| Anchor | the Discord access skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete attack the terminal-only rule stops (a forged second message); BCRY states the rule's scope (typed-by-you counts, arrived-as-a-message never does) — together they cover what the rule catches and what it never trusts, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the access Skill's SKILL.md specifies (the five-field state file,
the terminal-only refusal rule, the pair/approve flow, the never-auto-pick
rule, and the attack that rule targets) — not an inference about hidden
model internals. Per simple's ONE-FLAG LAW, when the source genuinely
supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
command dispatch) + B05 (teardown analysis) + BVDT (verdict) + BHTF
(your turn) + BOUT (outro). This redo keeps that same 7-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02
kept as one beat each; B05's long "gets it right / where it bites" list
(prompt-injection defense, state shape, pair-flow completeness, the
snowflake distinction — versus the undocumented $ARGUMENTS placeholder,
unbounded mentionPatterns regex, unexplained dmPolicy differences, and
undocumented server re-read mechanism) is compressed into NB03, keeping
only the single fact a general audience needs and can act on — the
concrete forged-message attack the terminal-only rule stops — and
dropping the Claude-Code-implementation-detail gaps ($ARGUMENTS, regex
bounds, re-read polling) that assume a technical audience simple/hai-simple
doesn't target; Teardown framing ("gets it right," "where it bites") is
stripped to a plain mechanism-and-consequence description, per the NO
JUDGMENT register check; BVDT's verdict facts (reliable terminal-only
enforcement, and the never-auto-pick limit) are merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with the
source's Discord-plugin-specific instructions ("set up the Discord
channel plugin and run /discord:access") replaced by a concrete,
paste-ready prompt that needs no Discord setup, so it's actually runnable
by any viewer today; BOUT kept, re-skinned to the Humanitarians AI outro.
Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`DiscordAccessAnatomy` / `DiscordAccessCommands` / `DiscordAccessTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
