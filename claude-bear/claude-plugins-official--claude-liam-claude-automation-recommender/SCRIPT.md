# SCRIPT.md — Recommend, Not Install. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-claude-automation-recommender` (Teardown, walks the
Anthropic `claude-automation-recommender` Claude Code plugin-dev Skill) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed you could just ask Claude to build your Claude Code
automations for you. You can't — it only recommends them. So: can I ask
Claude to recommend my Claude Code automations?

*(Text typed on screen: "Can I ask Claude / to build my / Claude Code /
automations?" — trigger word "build" corrects to "recommend", landing on:
"Can I ask Claude to recommend my Claude Code automations?" Timing chosen
to match the fix already proven on this family's `agent-development`
sibling after its pilot overran its window: short text (51 chars, 4 short
lines), charMs 42, mistakeRate 4%, hesitateWithin 2%, hesitateBetween 8% —
comfortably inside the correction-lands-on-screen budget. Narration 33
words + lead_silence_s 1.0 gives the typing a >=9s window per TIMING LAW;
verify media/B00.mp4 >= 8s and pull a late frame to confirm the corrected
question is settled and legible.)*

## Body — the five types, how it decides, the gap it leaves

**NB01 — Five automation types** (source B01, anatomy)
There are five automation types, covering the whole Claude Code
extensibility surface. Hooks run automatically on tool events — format on
save, block a risky edit, run tests after a change. Subagents are
specialized agents Claude can run in parallel — a code reviewer, a
security auditor, a test writer. Skills are packaged workflows invoked by
Claude or by a slash command. Plugins bundle related skills together for
one-step install. MCP servers connect external tools — databases, APIs,
browsers, documentation. Same question for all five: what triggers it, and
how wide is its scope? Hooks are automatic and event-driven. Subagents run
in parallel. Skills are invoked deliberately. Plugins group skills. MCP
servers reach outside Claude entirely.

**NB02 — Analyze, then cap** (source B02, design)
The skill works in three phases. First, it reads your codebase — package
files for language and framework, existing Claude config, test setup, CI
files, database and API code. Second, it matches what it found to a
specific recommendation, one type at a time, then caps it: one or two per
category, the single most valuable pick, not everything possible — and it
tells you that you can ask for more. Third, it writes a report: your
codebase profile, then one section per automation type, each with what to
add, why it fits, and how to install it. Prettier configured means a
format-on-save hook. A GitHub repo means the GitHub MCP server. Code
touching auth or payments means a security-reviewing subagent.

**NB03 — Recommend, not install** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's the catch: recommending isn't the same as handing you a runnable
step. For a subagent, it points at a template file instead of writing the
scaffold inline. For a plugin, it names the plugin but not the install
command — that's still a separate lookup. It's read-only end to end: it
never edits your files, and it never finishes that last step either. The
distance between "here's what to add" and "here's the exact command" is
yours to close.

## Close

**BCRY — carry-out**
It analyzes your codebase and tells you what to add and why — it never
creates a file, and it doesn't always hand you the exact command to run
either. Recommending isn't installing.

**BHTF — your turn**
Your turn. Paste this into Claude, in any real project: Analyze this
codebase and recommend Claude Code automations. Then check two things the
recommender doesn't always give you: for any subagent it suggests, does it
write the actual agent file, or just point you at a template? And for any
plugin, does it give you the exact install command, or just the plugin's
name? That gap between the recommendation and the runnable step is the
real test.

**BOUT — outro**
Recommend, Not Install. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a build-vs-recommend question — will Claude set up my automations, or just tell me about them? |
| Wrong guess | B00 (WRITER LAW) | "build" corrected to "recommend" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the five automation types and their distinct triggers/scope; the three-phase analyze-match-cap workflow with concrete signal-to-recommendation examples |
| Anchor | the automation recommender skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete gap the read-only design leaves (a subagent recommendation stops at a template pointer, a plugin recommendation stops at a name); BCRY states what the design does and what it doesn't do together (it tells you what to add and why; it doesn't always tell you the exact command) — together they cover what the recommendation gives and what it withholds, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
what the claude-automation-recommender Skill's SKILL.md specifies (the
five automation types, the read-only three-phase workflow, the 1-2-per-
category cap, the concrete signal-to-recommendation examples, and the gap
between naming a subagent/plugin and giving a runnable scaffold/install
command) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01 kept as one beat, trimmed of its
trailing skill-invocation-control paragraph (disable-model-invocation /
user-invocable:false) — a tangent about authoring skills, not about what
the automation recommender itself does, and a technical detail that
assumes a skill-building audience simple/hai-simple doesn't target; B02→
NB02 kept as one beat; B05's long "gets it right / where it bites" list
(explicit read-only framing, full five-type taxonomy, the 1-2-per-category
discipline, complete signal-to-recommendation tables, three documented
invocation-control modes — versus the unenforced beyond-reference-files
instruction, no monorepo guidance, subagent creation deferred to a
reference file, plugin recommendations missing install commands, no
when-not-to-recommend guidance) is compressed into NB03, keeping only the
single fact a general audience needs and can act on — the concrete
recommendation-vs-runnable-step gap (subagent template pointer, plugin
name without install command) — and dropping the Claude-harness-internals
gaps (beyond-reference-files enforcement, monorepo layouts, when-not-to-
recommend guidance) that assume a technical audience simple/hai-simple
doesn't target; Teardown framing ("gets it right," "where it bites") is
stripped to a plain mechanism-and-consequence description, per the NO
JUDGMENT register check; BVDT's verdict facts (the working read-only
analyze-then-recommend design, and the runnable-step gap it leaves) are
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's prompt ("Analyze this codebase and
recommend Claude Code automations") carried over unchanged — it was
already a concrete, paste-ready prompt needing no extra setup, so it's
actually runnable by any viewer today, in any real project rather than the
source's specific React TypeScript setup (generalized so the check works
regardless of what language or framework the viewer's own project uses);
BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03
+ BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`AutomationRecommenderTypes` / `AutomationRecommenderSignals` /
`AutomationRecommenderTell` / `ClaudeVerdictArtifact`) with B00 as a typed
composer ask (REMOTION, not AI-VIDEO — the source never called a
generation service). NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's cold open, which this redo replaces per hai-simple's mandate
anyway.
