# SCRIPT.md — Only Four of the Nine. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-hook-development` (Teardown, walks the Anthropic
`hook-development` Claude Code plugin-dev Skill) — question, facts, and
body argument carried over; narration re-registered to Plain (explain,
then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumes the recommended hook type fires on every event. It
doesn't — it only works on four of the nine. So: does a Prompt-Based hook
fire on only four of the nine events I use?

*(Text typed on screen: "Does a Prompt-Based hook / fire on any of / the
nine events / I use?" — trigger word "any" corrects to "only four",
landing on: "Does a Prompt-Based hook fire on only four of the nine events
I use?")*

## Body — anatomy, the taxonomy, the gap

**NB01 — Two types, two formats** (source B01, anatomy)
Two hook types, two places to put them. Prompt-Based is the recommended
type — it sends context to Claude, who decides what to do; the matcher
names the tools it applies to, the prompt field tells Claude how to
respond, and it times out at thirty seconds by default. Command hooks are
deterministic: they run a bash script, capture stdout and stderr, and use
the exit code to decide what happens. Exit zero means success — stdout
goes into the transcript. Exit two means block — Claude sees the stderr
message and stops. Any other code is non-blocking, and the default timeout
is sixty seconds. For portability, always use the CLAUDE_PLUGIN_ROOT
environment variable in the command path, never a hardcoded absolute one.
The two config formats aren't interchangeable either: plugin hooks.json
wraps everything under a description and a hooks key; the settings file
skips that wrapper, and event names sit right at the top level.

**NB02 — Nine events, four rules** (source B02, design)
Nine lifecycle events exist. PreToolUse fires before a tool call, Stop
when Claude's about to finish, SubagentStop for subagents, and
UserPromptSubmit when you submit a message — those four support
Prompt-Based hooks. The other five — PostToolUse, SessionStart,
SessionEnd, PreCompact, and Notification — are Command-hook only. Four
rules govern execution. All matching hooks run in parallel: there's no
ordering, and hooks can't see each other's output. Hooks load once, at
session start — there's no hot-swap, so you restart Claude after editing
hooks.json. Matchers are case-sensitive: Write is not write. And the
security defaults: quote every bash variable, validate inputs, and deny
path traversal and access to files like dot-env and private keys.

**NB03 — The gap** (source B05, teardown analysis — re-registered
Teardown → Plain, kept as the single most teachable fact rather than the
full "gets it right / where it bites" list)
Here's the catch. Prompt-Based is the type the skill recommends — but it
only fires on those same four events: PreToolUse, Stop, SubagentStop, and
UserPromptSubmit. Add a Prompt-Based hook to PostToolUse, expecting it to
review a tool's output after the fact, and nothing happens — no error, no
warning. It just never runs. If a hook needs to catch something after the
tool call, that has to be a Command hook.

## Close

**BCRY — carry-out**
Prompt-Based hooks are the recommended type, but they only fire on four of
the nine lifecycle events — put one on PostToolUse and it silently never
runs.

**BHTF — your turn**
Your turn. Give Claude a plugin that logs every Write tool call to a JSON
file, and blocks any Write to a dot-env file. Watch four things. For the
logging hook — it fires after the write happens, on PostToolUse — does
Claude reach for a Command hook, since Prompt-Based won't run there at
all? Does it use the CLAUDE_PLUGIN_ROOT environment variable in the
command path, instead of a hardcoded one? Does it put the hook in the
plugin's hooks.json wrapper format, or does it slip into the flat settings
format by mistake? And after it edits hooks.json, does it tell you to
restart the session before you test it?

**BOUT — outro**
Only Four of the Nine. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a coverage question — does the recommended hook type fire on every event? |
| Wrong guess | B00 (WRITER LAW) | "any" corrected to "only four" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the two hook types and two config formats; the nine lifecycle events, which four support prompt hooks, and the four execution rules |
| Anchor | the hook-development skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete failure mode the four-event restriction creates (a PostToolUse prompt hook that silently never runs); BCRY states the design's recommendation and its coverage limit together (Prompt-Based is the recommended type, but it only reaches four of nine events) — together they cover what the recommended type handles and what it never touches, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the hook-development Skill's SKILL.md specifies (the two hook types
and their exit-code semantics, the two config formats, the nine lifecycle
events and which four support prompt hooks, the parallel-execution and
no-hot-swap rules, and the security defaults) — not an inference about
hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each (B01's anatomy and B02's nine-event taxonomy are both dense,
single-idea mechanism content the source itself treats as one beat each,
so no further split is warranted); B05's long "gets it right / where it
bites" list (five rights: Prompt-Based as the recommended default,
CLAUDE_PLUGIN_ROOT for portability, clear exit-code semantics, the
documented parallel-execution model, explicit security patterns — versus
five gaps: the unstated four-event restriction on prompt hooks, the
easy-to-miss hot-swap restriction, the unspelled-out no-hook-collaboration
implication of parallel execution, the two silently-confusable config
formats, and case-sensitive matchers) is compressed into NB03, keeping
only the single fact a general audience needs and can act on — the
concrete four-of-nine restriction and its silent-failure mode — and
dropping the other four gaps (hot-swap timing, hook-collaboration limits,
format confusion, matcher case-sensitivity) as secondary to the one
restriction that most directly contradicts the "recommended type" framing;
Teardown framing ("gets it right," "where it bites") is stripped to a
plain mechanism-and-consequence description, per the NO JUDGMENT register
check; BVDT's verdict facts (the two types, two formats, nine events, the
four-event prompt-hook restriction, the execution model, and exit codes)
are merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's already-concrete, already-runnable
prompt ("Give Claude a plugin that logs every Write tool call to a JSON
file and blocks any Write to a dot-env file") carried over unchanged, and
its five watch-points compressed to four by folding the source's
standalone "restart reminder" point into the PostToolUse/Command-hook
point it actually explains; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`HookDevelopmentAnatomy` / `HookDevelopmentDesign` / `HookDevelopmentTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
