# SCRIPT.md — Describe When, Not What. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-agent-development` (Teardown, walks the Anthropic
`agent-development` Claude Code plugin-dev Skill, prose-trigger version) —
question, facts, and body argument carried over; narration re-registered to
Plain (explain, then stop, no verdict); cold open replaced with the
BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed listing an agent's skills was enough for Claude to know when
to use it. It isn't — only its triggers do. So: does listing my agent's
triggers tell Claude when to use it?

*(Text typed on screen: "Does listing / my agent's skills / tell Claude /
when to use it?" — trigger word "skills" corrects to "triggers", landing on:
"Does listing my agent's triggers tell Claude when to use it?" First render
attempt (48ms/char, 14% hesitateBetween, 6% mistakeRate, a longer 4-line/67-
char text) ran out of its window before the final line finished typing,
caught by a frame pull at the clip's last frame; fixed by shortening the
text, dropping the mistake/hesitation rates, and speeding the performance
(42ms/char) — reverified the correction lands by t≈2.2-4s and the full
corrected question is settled and legible for the remaining ~6s of the
10.1s clip.)*

## Body — anatomy, the description's real job, the sync problem

**NB01 — Frontmatter: five fields** (source B01, anatomy)
An agent file is two things: YAML frontmatter, then a markdown system-prompt
body. Frontmatter has five fields. Name — lowercase with hyphens, three to
fifty characters, starting and ending alphanumeric: code-reviewer,
test-generator, security-analyzer. Description — the field that matters most,
because it's loaded into context whenever the agent is registered, so it's
what decides whether Claude dispatches this agent at all. Model — inherit is
the recommended default. Color is just visual distinction in the interface.
And tools — the array of permissions the agent actually gets; give it only
what the task needs. The body underneath spells out the agent's role and
output format, plus a When to invoke section with worked scenarios.

**NB02 — Two locations, one job each** (source B02, design)
The description has one job: state exactly when Claude should reach for this
agent — not just what it can do. The format here is: 'Use this agent
when...', then 'Typical triggers include' two to four concrete scenarios,
then a pointer to a When to invoke section in the body. That prose names real
triggers — proactive and reactive, different phrasings of the same request —
and says when not to use the agent. The body's own When to invoke section
repeats this in more depth: a bold scenario name, what the situation looks
like, and what the agent should actually do. Two different jobs: the
description is for Claude's dispatch decision; the body is for the agent
once it's already running.

**NB03 — The sync problem** (source B05, teardown analysis — re-registered
Teardown → Plain, kept as the single most teachable fact rather than the
full "gets it right / where it bites" list)
Here's the catch with two locations: nothing keeps them in sync. If the
trigger scenarios change and only the description gets updated, the body's
When to invoke section goes stale — or the other way around. And it's the
description alone that Claude reads to decide whether to dispatch the agent
at all, so a scenario that only lives in the stale body section never even
gets checked at that moment. Keeping both current, by hand, every time
triggers change, is the actual maintenance cost of this design.

## Close

**BCRY — carry-out**
A subagent only gets called when its description says exactly when to use
it — not just what it does. The best agent in the world never fires if its
description only lists capabilities.

**BHTF — your turn**
Your turn. Paste this into Claude: Create an agent for my plugin that
reviews pull request diffs for security issues. Then check the description
Claude wrote: does it say 'Use this agent when...' with two to four concrete
trigger scenarios, or does it just list what the agent does? Does the body
have a When to invoke section with worked scenarios? Are the tools it picked
the minimum needed — probably Read and Bash, not Write? That's the actual
test of a good agent file.

**BOUT — outro**
Describe When, Not What. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a dispatch question — does listing what the agent does get it used at the right time? |
| Wrong guess | B00 (WRITER LAW) | "skills" corrected to "triggers" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the five frontmatter fields and where the body picks up; the description's dispatch-only job and the body's own When to invoke section for the agent itself |
| Anchor | the agent-development skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete drift risk the two-location design creates (a scenario that's stale in one place never gets checked at dispatch); BCRY states the design's payoff and its failure mode together (a well-written trigger fires it, a capability-only description never does) — together they cover what the description catches and what it misses, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the agent-development Skill's SKILL.md specifies (the five-field frontmatter,
the description's dispatch role, the two-location prose-trigger format, the
body's When to invoke section, and the maintenance coupling between the two
locations) — not an inference about hidden model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy / design)
+ B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) + BOUT (outro).
This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each; B05's
long "gets it right / where it bites" list (file structure fully specified
with concrete constraints, the two-location approach explicitly motivated,
complete name-field constraints, the tools-minimum-permission principle, the
workable system-prompt template — versus prose being less machine-parseable
than structured examples, the trigger-dispatch mechanism itself being
unexplained, no model-override guidance, no system-prompt length guidance) is
compressed into NB03, keeping only the single fact a general audience needs
and can act on — the concrete two-location sync problem — and dropping the
Claude-harness-internals gaps (pattern-match vs. LLM-judgment dispatch, model
override guidance, prompt length limits) that assume a technical audience
simple/hai-simple doesn't target; Teardown framing ("gets it right," "where
it bites") is stripped to a plain mechanism-and-consequence description, per
the NO JUDGMENT register check; BVDT's verdict facts (the working two-location
format, and the maintenance gap it creates) are merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW; BHTF kept as the your-turn handoff, with the source's prompt
("Create an agent for my plugin that reviews pull request diffs for security
issues") carried over unchanged — it was already a concrete, paste-ready
prompt needing no extra setup, so it's actually runnable by any viewer today;
BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 +
BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`AgentDevAnatomy` / `AgentDevTriggerProse` / `AgentDevTell2` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
