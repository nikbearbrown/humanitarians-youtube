# SCRIPT.md — For Claude, Not For You. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-command-development` (Teardown, walks the Anthropic
`command-development` Claude plugin-dev Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a command's body describes what will happen to the user.
It doesn't — it's a directive TO Claude. So: when I write a command body,
am I writing it for Claude?

*(Text typed on screen: "When I write / a command body, / am I writing it /
for the user?" — trigger word "user" corrects to "Claude", landing on:
"When I write a command body, am I writing it for Claude?" Params reused
verbatim from the `agent-development`/`claude-automation-recommender`
siblings' already-proven-safe values (42ms/char, 4% mistakeRate, 8%
hesitateBetween) after the TIMING LAW lesson learned there — no overrun.)*

## Body — anatomy, arguments + file refs, the bash gap

**NB01 — Anatomy: three locations, five fields** (source B01, anatomy)
A slash command is a Markdown file with YAML frontmatter, and its body is a
directive TO Claude — not a message to the user. Commands live in three
places: project commands, shared with the team and available only in that
project; personal commands, available in every project; and plugin
commands, bundled with an installed plugin. Frontmatter carries five
fields: description, allowed-tools, model, argument-hint, and
disable-model-invocation.

**NB02 — Arguments, file references, plugin paths** (source B02, design)
Arguments come two ways. Dollar-ARGUMENTS captures everything typed after
the command as one string. Dollar-1, dollar-2 capture individual pieces — a
PR number, then a priority level. The at-sign reads a file: at-dollar-1
opens whatever path the argument names; a static reference like
at-package-dot-json embeds a known file every time, no argument needed.
Plugin commands get one more trick: CLAUDE_PLUGIN_ROOT resolves to the
plugin's own folder, so a command can point at its own scripts without a
hardcoded path. One note from the skill itself: this whole file format is
now considered legacy — new work is pointed toward a skill file instead.

**NB03 — The gap: bash execution deferred** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
One gap worth knowing: a command can also run a shell command inline before
Claude ever sees the rest — an exclamation mark, then backticks, pulling in
something like the current git diff automatically. That's the single most
useful dynamic trick available. But the guide that teaches command-writing
doesn't show it inline — it's pushed off into a separate reference file
instead.

## Close

**BCRY — carry-out**
A slash command's body is written for Claude, not for you. The words that
matter tell Claude what to do — not what you'll see happen.

**BHTF — your turn**
Your turn. Open a Claude Code session and paste this: Create a slash
command called review-pr that takes a PR number as an argument, reads the
changed files, and reviews them for code quality. Watch four things. First:
does the command body tell Claude what to do, or describe what will happen
to you? Second: does it use dollar-ARGUMENTS or dollar-1 for the PR number,
with the argument-hint field set? Third: does it use allowed-tools to
restrict what the command can touch? Fourth: if you ask it to add bash
execution to pull in the PR diff dynamically, does it show you the
exclamation-mark backtick syntax inline, or send you to a reference file?

**BOUT — outro**
For Claude, Not For You. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an audience question — who is a command body actually written for? |
| Wrong guess | B00 (WRITER LAW) | "user" corrected to "Claude" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the three locations and five frontmatter fields; the argument/file-reference system and CLAUDE_PLUGIN_ROOT |
| Anchor | the slash-command file format itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one file format), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete gap the design creates (the most-used dynamic feature is real but not taught inline); BCRY states the design's payoff and its failure mode together (a directive gets acted on, a description read as user-facing prose does not) — together they cover what the format enables and what it still requires you to go find, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `command-development` Skill's SKILL.md specifies (the for-Claude
framing, the three-location taxonomy, the five-field frontmatter, the
argument and file-reference systems, CLAUDE_PLUGIN_ROOT, the legacy note,
and the bash-execution deferral to a reference file) — not an inference
about hidden model internals. Per simple's ONE-FLAG LAW, when the source
genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B05's long "gets it right / where it bites" list (the for-Claude framing
example, the three-location taxonomy, the five frontmatter defaults, both
argument systems, CLAUDE_PLUGIN_ROOT — versus the bash-execution deferral,
the buried legacy note, the non-syntax $IF pattern, the unexplained
Bash(git:*) scope rules, and the uncompared commands-vs-skills discovery)
is compressed into NB03, keeping only the single fact a general audience
needs and can act on — the bash-execution gap — and dropping the
Claude-harness-internals gaps ($IF misreadability, allowed-tools namespace
scope rules, commands-vs-skills discovery comparison) that assume a
technical audience simple/hai-simple doesn't target; Teardown framing
("gets it right," "where it bites") is stripped to a plain mechanism-and-
consequence description, per the NO JUDGMENT register check; BVDT's verdict
facts (the working file format, and the one real gap in its own
documentation) are merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept
as the your-turn handoff, with the source's prompt ("Create a slash command
called review-pr that takes a PR number as an argument, reads the changed
files, and reviews them for code quality") carried over unchanged — it was
already a concrete, paste-ready prompt needing no extra setup, so it's
actually runnable by any viewer today; BOUT kept, re-skinned to the
Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`CommandDevAnatomy` / `CommandDevContent` / `CommandDevTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
