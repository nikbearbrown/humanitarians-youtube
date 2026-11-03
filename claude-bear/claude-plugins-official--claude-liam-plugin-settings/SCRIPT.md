# SCRIPT.md — Restart Required. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-plugin-settings` (Teardown, walks the Anthropic
`plugin-settings` Claude plugin-dev Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed flipping a plugin's enabled flag in its settings file takes
effect the moment you save the file. It doesn't — Claude Code has to
restart first. So: when I toggle a setting, does it take effect later?

*(Text typed on screen: "When I toggle / a setting, / does it take / effect
now?" — trigger word "now" corrects to "later", landing on: "When I toggle
a setting, does it take effect later?" Params reused verbatim from the
`command-development`/`agent-development` siblings' already-proven-safe
values (42ms/char, 4% mistakeRate, 8% hesitateBetween) after the TIMING LAW
lesson learned there — no overrun.)*

## Body — the file, the safe patterns, the one gap

**NB01 — Anatomy: the file** (source B01, content model)
The pattern lives in one file: dot-claude slash plugin-name dot local dot
md, in the project root. It has two parts — YAML frontmatter for
structured settings, and a markdown body for prompts and instructions.
Three things read it: bash hooks, command files, and agent instructions.
It's per-project, user-managed, and never committed to git.

**NB02 — Built to fail safe** (source B02, design/workflow patterns)
Four things make it work well. Design the schema first, and decide
sensible defaults for when the file doesn't exist — most users never
create it. Hooks should quick-exit: check the file exists, check it's
enabled, otherwise exit immediately. And every project needs its own
gitignore entry for the file — that step is manual, not automatic.

**NB03 — The gap: no carryover** (source B05 + BVDT, teardown/verdict —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
One gap worth knowing: a setting you configure in one project doesn't
carry over to any other project — there's no plugin-wide switch. Every
project keeps its own file, its own flags, its own restart. If you
expected one setting to follow you everywhere, it won't.

## Close

**BCRY — carry-out**
A plugin's settings file works per project, not globally, and no change
takes effect until Claude Code restarts. Set it, save it, restart it —
that's the whole contract.

**BHTF — your turn**
Your turn. Ask Claude to add configurable settings to a project: an
enabled flag, a validation level, and a max-retries count. Watch three
things. First: does the file land in a per-project location, kept out of
git? Second: does the code guard with a quick-exit — check the file
exists, check it's enabled, before doing anything else? Third: does
everything still work correctly when the settings file doesn't exist at
all?

**BOUT — outro**
Restart Required. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an audience question — does a toggled setting apply right away? |
| Wrong guess | B00 (WRITER LAW) | "now" corrected to "later" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the file's location and two-part structure, its three consumers, its lifecycle; the schema-first/quick-exit/gitignore patterns that make it safe |
| Anchor | the settings file itself (`.local.md`), named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one file format), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete gap the design creates (a setting stays local to its project, no plugin-wide carryover); BCRY states the design's payoff and its failure mode together (the file works reliably when you respect both boundaries — per-project scope and the restart — and quietly doesn't when you assume either one away) — together they cover what the pattern enables and what it still requires you to remember, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the `plugin-settings` Skill's SKILL.md specifies (the file's location and
two-part structure, the three consumers, the three real-world patterns, the
quick-exit convention, the lifecycle rules, and the per-project scope) —
not an inference about hidden model internals. Per simple's ONE-FLAG LAW,
when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B05's long "gets it right / where it bites" list (frontmatter+body pattern,
three-consumer documentation, three worked patterns, the quick-exit
convention, and documented security considerations — versus the restart
requirement, the CRLF parser failure, the array-parsing failure, manual
gitignore, and per-project-not-global scope) is compressed into NB03,
keeping only the single fact a general audience needs and can act on — the
per-project, no-carryover gap — and dropping the Claude-harness-internals
gaps (sed's CRLF failure mode, the grep/sed array-parsing bug) that assume
a technical, script-authoring audience simple/hai-simple doesn't target;
Teardown framing ("gets it right," "where it bites") is stripped to a plain
mechanism-and-consequence description, per the NO JUDGMENT register check;
BVDT's verdict facts (the working file format, and the two real
constraints on it) are merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW;
BHTF kept as the your-turn handoff, with the source's prompt intent
carried over (add an enabled flag, a validation level, and a max-retries
count to a plugin's settings) but trimmed from five watch-items to three,
dropping the two that assume the viewer is authoring the plugin's own
hooks in bash (the exact quick-exit code shape, the README's restart
wording) in favor of three any-viewer-can-check items; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`PluginSettingsAnatomy` / `PluginSettingsPatterns` / `PluginSettingsTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
