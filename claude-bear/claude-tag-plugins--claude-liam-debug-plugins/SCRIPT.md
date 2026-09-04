# SCRIPT.md — Stale, Not Broken. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-debug-plugins` (Teardown, walks the Claude Code
`debug-plugins` Skill — a six-step diagnostic ladder for plugin/skill
loading run from inside the session container) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a plugin that won't show up means broken configuration.
Usually it's just stale, read once, when the session started. So: is my
config broken, or just out of date?

*(Text typed on screen: "My plugin isn't / showing up. Is my / config
broken?" — trigger word "broken" corrects to "stale", landing on: "My
plugin isn't showing up. Is my config stale?")*

## Body — three steps, five causes, two limits

**NB01 — Three steps, in order** (source B01, anatomy — compressed)
Before deciding anything, Claude checks three things in order: what
actually arrived in the plugin mount (the plugin zip, a standalone skill
folder, or a pre-seeded marketplace mount), what flags Claude Code was
actually launched with, and what the startup log recorded at load time.
All three get collected before any explanation is offered — not
diagnose-as-you-go.

**NB02 — Five ways a plugin goes missing** (source B02/B05, the failure
ladder — compressed)
Then it walks a short list of causes. The zip simply isn't there — not
enabled for this scope, or configuration changed after the session
started. It's there, but Claude Code wasn't launched with a matching
flag — a launcher problem, not something fixable from inside a chat. The
zip failed to extract — it hit a size or file-count limit. The plugin's
manifest file is malformed — often just a stray capital letter or a space
in the name. Or the zip and folder are both fine, but the skill file's own
header is broken.

**NB03 — Two limits** (source B02/B05, session snapshot + stdout gap —
reframed as BOTH-DIRECTIONS)
Two limits worth knowing. First: a session reads your configuration once,
when it starts — flip a setting mid-chat, and the fix is a new
conversation, not a refresh of this one. Second: some of Claude Code's own
startup errors go to a channel this diagnostic can't see inside the
container — so a clean-looking log doesn't guarantee nothing went wrong,
it just means this particular channel didn't catch it.

## Close

**BCRY — carry-out**
If a plugin won't show up, check what actually arrived and what actually
loaded before assuming it's broken — and if you just flipped a setting,
open a new chat before you diagnose anything else.

**BHTF — your turn**
Your turn. Paste this into Claude Code: A plugin zip is sitting in
/mnt/account-plugins, but the skill inside it isn't showing up. Walk me
through what actually arrived, what you were launched with, and what the
startup log says, before telling me what's wrong. Then check three things:
does it collect all three before explaining anything? Does it say so if
the log file is missing? And if you flipped the setting a few minutes ago,
does it ask for a fresh conversation?

**BOUT — outro**
Stale, Not Broken. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a diagnostic question — is a missing plugin proof of broken config? |
| Wrong guess | B00 (WRITER LAW) | "broken" corrected to "stale" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the three-step evidence collection, then the five failure causes that explain a missing plugin |
| Anchor | a missing plugin/skill, named at B00 and carried through NB01–NB03 | source is a single worked example throughout (one diagnostic ladder), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 | a caught startup error doesn't mean total failure, and a clean-looking log doesn't prove nothing went wrong — the stdout channel this diagnostic reads isn't the only channel that can fail |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the debug-plugins Skill's source narration specifies (the three-step
evidence order, the five failure-ladder causes, the session-snapshot rule,
and the stdout-gap limitation) — not an inference about hidden model
internals. Per simple's ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 keeps the three-step evidence order;
B02's failure-ladder content and B05's teardown analysis are merged into
NB02 (the five failure causes) — B05's separate security note (treat log
content as untrusted, use Read/Grep not cat) and its list of Teardown gaps
(unzip-via-Bash-vs-read-only tension, no report template, no missing-log
fallback, seed-mounts uninspectable) are dropped as assuming a technical,
Claude-Code-internals audience simple/hai-simple doesn't target, not as a
verdict on the skill's quality; B02's session-snapshot rule and the
stdout-gap limitation are kept and reframed as NB03's BOTH-DIRECTIONS beat
(a caught error isn't proof of total failure; a clean log isn't proof of
none); BVDT's verdict facts are merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff, with the source's
concrete scenario (a zip present in /mnt/account-plugins whose skill isn't
showing up) carried over, trimmed from five things-to-watch to three so it
stays paste-ready and runnable by any viewer today without a live
Claude-Code-internals audit; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`DebugPluginsAnatomy` / `DebugPluginsDesign` / `DebugPluginsTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
