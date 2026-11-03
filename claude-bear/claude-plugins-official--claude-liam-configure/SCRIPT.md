# SCRIPT.md — Saved Isn't Live. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-configure` (Teardown, walks the Anthropic Discord
plugin's `configure` skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed saving a fresh Discord bot token makes it live right away.
It doesn't — the credential file only gets read once, at startup. So: I
saved a new token. It's live now, right?

*(Text typed on screen: "I saved a new / token. It's live / now, right?" —
trigger word "now" corrects to "after restart", landing on: "I saved a new
token. It's live after restart, right?" Rates copied from the already-tuned
`claude-plugins-official--claude-liam-agent-development` sibling — 42ms/char,
8% hesitateBetween, 4% mistakeRate — which reliably finished a similarly
short 3-line text inside its audio window.)*

## Body — anatomy, the lockdown/restart design, the validation gap

**NB01 — Three modes, two files** (source B01, anatomy)
The skill reads whatever argument you give it. No arguments: show status —
read both files, tell you whether a token is set, what the access policy
is, who's already paired, and give you one concrete next step. Give it a
token: it trims stray whitespace, creates the channel folder if it's
missing, updates the credential file without disturbing anything else
already in it, and locks that file to owner-read-only. Give it the word
clear: it deletes the token line, or the whole file if that's all there
was. Two files carry all of this. The credential file holds the token,
read once, when the session starts. The access file holds the policy, and
it's read again on every single incoming message.

**NB02 — Push toward lockdown** (source B02, design)
The rule here is explicit: always push toward an allowlist, never let
pairing become permanent. Pairing exists only to capture the Discord IDs
you don't know yet. Once everyone you want is captured, the skill offers
to flip the switch itself — without waiting to be asked. One detail is
easy to miss. Save a new token, and it doesn't take effect until you
restart the session — the credential file is only read once, at startup.
Update the allowlist, though, and it's live on your very next message.
Skip the restart after saving a token, and you'll think you're running
the new one when you're not.

**NB03 — No validation** (source B05, teardown analysis — re-registered
Teardown → Plain, kept as the single most teachable fact rather than the
full "gets it right / where it bites" list)
Here's the gap worth knowing. The skill never checks that what you paste
actually looks like a token — no length check, no format check, nothing.
Paste a grocery list, and it gets written to the credential file exactly
the same way a real token would. The skill trusts you completely at the
one moment it probably shouldn't.

## Close

**BCRY — carry-out**
A saved token isn't a live token — the credential file is only read once,
at restart. The access policy has no such wait; it's checked on your very
next message.

**BHTF — your turn**
Your turn. Open a Claude Code session with the Discord configure skill,
and paste a token that's obviously fake — something like
'not-a-real-token'. Watch two things: does it save that string without
any complaint at all, and after you tell it your allowlist is complete,
does it offer to lock down access itself, or does it wait for you to ask?

**BOUT — outro**
Saved Isn't Live. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a timing question — does saving a token make the bot live right now? |
| Wrong guess | B00 (WRITER LAW) | "now" corrected to "after restart" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the three-mode dispatch and two-file split; the lockdown-push rule and the restart-vs-instant asymmetry that makes B00's correction true |
| Anchor | the configure skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB02 + BCRY | NB02/BCRY state both timing failure modes together: a saved token you *think* is live but isn't (restart pending), and an access-policy change you might assume needs a restart but is already live — together they cover both ways the two-clock design can surprise you |
| Carry-out | BCRY | one sentence, survives repetition, directly resolves B00's question |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `configure` skill's SKILL.md specifies (the three-mode dispatch, the
two-file split and their different read timings, the lockdown-push rule,
and the absence of token-format validation) — not an inference about hidden
Discord or Claude-harness internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat, built directly from the source's own
observation that "a user who saves a new token and doesn't restart will
think the configuration worked but be running the old token"); B01→NB01,
B02→NB02 kept as one beat each; B05's five-item "gets it right / where it
bites" list (three-mode dispatch coverage, the proactive lockdown rule,
chmod 600 hygiene, the two restart behaviors, concrete next-step guidance
— versus no token validation, unspecified other .env keys, no restart
command given, access.json schema stated only by example, and Discord's
own gates left unexplained) is compressed into NB03, keeping only the
single fact a general audience needs and can act on — the missing token
validation — and dropping the Claude-harness/Discord-internals gaps (the
unspecified .env key schema, the unstated access.json schema, Discord's
shared-server and Public Bot gates) that assume a technical audience
simple/hai-simple doesn't target; Teardown framing ("gets it right,"
"where it bites") is stripped to a plain mechanism-and-consequence
description, per the NO JUDGMENT register check; BVDT's verdict facts (the
working three-mode/two-file design, and the restart asymmetry) are merged
into the single BCRY carry-out sentence rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn
handoff, re-scoped from the source's five-point checklist (paste a fake
token; watch validation, masked display, proactive lockdown offer, restart
command, and Developer Portal guidance) down to the two checks that match
what NB01–NB03 actually taught (validation and the proactive lockdown
offer) rather than introducing untaught checks (masked display, restart
command wording, Developer Portal guidance) that this shorter Plain cut
never covers; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ConfigureAnatomy` / `ConfigureDesign` / `ConfigureTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
