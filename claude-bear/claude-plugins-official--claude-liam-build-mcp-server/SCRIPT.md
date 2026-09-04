# SCRIPT.md — Decide First. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-build-mcp-server` (Teardown, walks the Anthropic
Build MCP Server Claude Code plugin-dev Skill — a discovery-and-routing
skill) — question, facts, and body argument carried over; narration
re-registered to Plain (explain, then stop, no verdict); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed the first step was writing code for an MCP server. It
isn't — discovery comes first. So: what do I decide first for an MCP
server?

*(Text typed on screen: "What do I / code first / for an MCP / server?" —
trigger word "code" corrects to "decide", landing on: "What do I decide
first for an MCP server?" Shorter text and the same already-tuned-safe
typing parameters as the `claude-plugins-official--claude-liam-agent-
development` sibling (42ms/char, 4% mistakeRate, 2%/8% hesitation), so no
separate timing-fix pass was expected — verified anyway per TIMING LAW.)*

## Body — three deployment paths, two tool patterns, a description subtlety

**NB01 — Three deployment paths** (source B01, anatomy)
There are three deployment paths, ranked by preference. Remote HTTP wins by
default for anything wrapping a cloud API: zero install friction, one
server serves all users, and OAuth flows work properly with redirect
handling. Recommend this unless the server must touch the user's local
machine. MCPB — Model Context Protocol Bundle — packages a server with its
runtime for local distribution: the sanctioned way to ship when the server
reads local files, drives a desktop app, or talks to localhost services.
Local stdio via npx or uvx is fine for personal prototypes but painful to
distribute — recommend it only as a stepping stone and flag the MCPB
upgrade path. The decision matrix covers seven scenarios: small SaaS API
goes remote, large SaaS goes remote with search-plus-execute, UI widgets go
MCP app, local desktop goes MCPB.

**NB02 — Two tool-design patterns** (source B02, design)
Tool design has two patterns. Pattern A: one tool per action. When the
action space is under about fifteen operations, give each a dedicated tool
with a tight description and schema. Claude reads the list once and knows
exactly what's possible. Pattern B: search-plus-execute. When wrapping a
large API — dozens to hundreds of endpoints — listing every operation
floods the context window and degrades model performance. Expose two
tools: search-actions to return matching operations for a natural-language
intent, and execute-action to run an operation by ID. Context stays lean.
The hybrid option promotes the three to five most-used actions to dedicated
tools, keeping the long tail behind search and execute. Beyond tools, the
other three primitives are resources — host-browsable docs and data —
prompts — user-triggered slash commands — and elicitation — spec-native
mid-tool user input without building UI. Most servers only need tools;
knowing the others prevents reinventing wheels.

**NB03 — The description decides** (source B05 + BVDT, teardown/verdict —
re-registered Teardown → Plain, compressed to the single most teachable,
general-audience fact rather than the full "gets it right / where it
bites" + gaps inventory)
There's a subtlety in how well this works once the server exists: Claude
picks a tool by reading its description, not its name. A description that
just restates the tool's name — "creates an issue" for create-issue —
doesn't tell Claude when to reach for it over a similar tool, like
update-issue. The more specific the description, the more reliably Claude
calls the right one at the right moment.

## Close

**BCRY — carry-out**
Build MCP Server asks four questions — deployment, users, how many
actions, and auth — before it writes any code. Get that order backwards
and you're not tweaking the server later, you're rewriting it.

**BHTF — your turn**
Your turn. Paste this into Claude: Build an MCP server that wraps the
GitHub API — tools for creating issues, searching repositories, and
getting pull request details. Then watch four things. Does it ask
discovery questions before writing any code, or start scaffolding right
away? Does it recommend remote HTTP as the default, and say why? Does it
use one tool per action, since three tools is well under the
search-plus-execute threshold? And are the tool descriptions specific
enough to tell create-issue apart from update-issue? A description that
just repeats the tool's name is the tell that it skipped the tool-design
guidance.

**BOUT — outro**
Build MCP Server. Liam, in for Bear.

*(Title card: "Decide First." — chosen over the working title "Discovery
Before Code." after GATE T's first pass flagged a min-size §8.1 FAIL on
that render: diagnostic showed the only qualifying "text run" blob after
filtering was an accidental 2-letter merge inside "Discovery" (38px,
under the 41px floor), while every genuinely individual glyph in the
frame measured 41-89px — a known false-positive class where the word-run
width filter (`w >= h*1.5`) discards correctly-sized non-touching serif
letters and, on this unlucky frame, one merged pair squeaked past the
filter and reported a misleadingly low height instead of the checker's
own individual-char fallback path (see B00's own PASS note: "individual-
char fallback at 2x") triggering. Retitling to "Decide First." — which
also ties the outro directly to B00's wrong-guess correction and BCRY's
sparkline "Decide first. Code second." — shifted the glyph layout enough
to avoid the accidental merge; GATE T re-ran clean, 0 FAILs, without
touching the validator.)*

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a build-order question — do you write server code first, or does something get decided first? |
| Wrong guess | B00 (WRITER LAW) | "code" corrected to "decide" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the three deployment paths ranked by preference and the seven-scenario matrix; the two tool-design patterns keyed to action-count, plus the other three primitives |
| Anchor | the Build MCP Server skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states what a specific tool description gets you (Claude calls the right tool) and what a vague one costs (ambiguity between similar tools); BCRY states the design's payoff and its failure mode together (four questions answered means the right shape gets built once; skipped, it means a rewrite) — together they cover what the discovery step catches and what skipping it costs, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the Build MCP Server Skill's SKILL.md specifies (the three-path deployment
ranking and its exceptions, the seven-scenario decision matrix, the two
tool-design patterns and the action-count threshold between them, the three
non-tool primitives, and the description field's role in tool selection) —
not an inference about hidden model internals. Per simple's ONE-FLAG LAW,
when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (deployment
anatomy / tool-design) + B05 (teardown analysis) + BVDT (verdict) + BHTF
(your turn) + BOUT (outro). This redo keeps that same 7-beat shape: B00
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02
kept as one beat each with their content carried over near-verbatim (both
were already factual descriptions of the skill's own stated guidance, not
this reel's design judgment, so Plain re-registration required no content
change); B05's long "gets five things right / where it bites" list (the
discovery-before-code structure, the remote-HTTP default, the
search-plus-execute pattern, elicitation framed as spec-native with a
capability-check caveat, the seven-scenario matrix — versus the elicitation
capability check being buried, the FastMCP jlowin-PyPI-vs-frozen-1.0
version split, tool description guidance being deferred to a references
file, the OAuth CIMD/DCR distinction being deferred, and the "load Claude
docs first" invariant having no enforcement) is compressed into NB03,
keeping only the single fact a general audience needs and can act on — that
Claude selects a tool by its description, not its name, so a vague
description blurs similar tools together — and dropping the
Claude-harness-internals gaps (the FastMCP package split, the elicitation
capability-check mechanics, the OAuth protocol distinction) that assume a
technical audience simple/hai-simple doesn't target; Teardown framing
("gets it right," "bites") is stripped to a plain mechanism-and-consequence
description, per the NO JUDGMENT register check; BVDT's verdict facts (the
three-path ranking, the two tool patterns, the description caveat) are
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's prompt ("Build an MCP server that
wraps the GitHub API — tools for creating issues, searching repositories,
and getting pull request details") carried over unchanged — it was already
a concrete, paste-ready prompt needing no extra setup, so it's actually
runnable by any viewer today; BOUT kept, re-skinned to the Humanitarians AI
outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the
source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`BuildMcpServerDeployment` / `BuildMcpServerPatterns` / `BuildMcpServerTell`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
