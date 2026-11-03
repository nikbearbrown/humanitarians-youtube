# SCRIPT.md — Match The Transport, Not The Key. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-mcp-integration` (Teardown, walks the Anthropic
`mcp-integration` Claude Code plugin-dev Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed the only thing that matters is which key to use. It isn't
— the real choice is which transport your plugin needs. So: what kind of
transport does my plugin need for a service?

*(Text typed on screen: "What kind of / key does my plugin / need for / a
service?" — trigger word "key" corrects to "transport", landing on: "What
kind of transport does my plugin need for a service?")*

## Body — the four transports, the naming rules, the silent-failure gotcha

**NB01 — Four transport types, one per server** (source B01, anatomy)
Four transport types, and each server uses exactly one. Stdio spawns a
local process — Claude Code starts it, talks over standard input and
output, and shuts it down when it's done; that's for custom servers and
local tools. SSE connects to a hosted server, and handles OAuth
automatically — you log in once in a browser, and Claude Code manages the
tokens after that; that's the type for official hosted services like
GitHub or Linear. HTTP calls a REST API with a token in the request
headers, for stateless one-off calls. WebSocket keeps a live, two-way
connection open, for real-time updates. All four load lazily — nothing
connects until you actually use one of its tools — and a config change
needs a restart before it takes effect.

**NB02 — Portable paths, exact tool names** (source B02, design)
A few patterns keep a multi-server plugin manageable. Put server config in
its own dot-mcp-dot-json file instead of burying it inline in plugin.json —
it stays isolated and easier to maintain as servers are added. Use the
CLAUDE_PLUGIN_ROOT variable for every file path, never a hardcoded one, so
the plugin still works after it's installed somewhere else. And when you
pre-allow tools for a command, list the exact tool names instead of a
wildcard — the format is mcp, double underscore, the plugin name, the
server name, double underscore, the tool name, all stitched together. Run
slash-mcp first to see the real names before you write that list.

**NB03 — Wrong by one character, and no warning** (source B05, teardown
analysis — re-registered Teardown → Plain, kept as the single most
teachable fact rather than the full "gets it right / where it bites" list)
Here's the catch: that tool name has to match character for character. Get
one letter wrong in the pre-allow list, and the tool doesn't show up — no
error, no warning, it's just not there. And for stdio or HTTP servers, the
credentials they need are just environment variables — nothing checks them
until the first real call, so a broken setup can look perfectly healthy
right up until that moment.

## Close

**BCRY — carry-out**
Match the transport to where the service actually lives — stdio for local,
SSE for hosted OAuth, HTTP for tokens, WebSocket for real-time. Then
pre-allow the exact tool name, because one character off and it fails
silently, not loudly.

**BHTF — your turn**
Your turn. Paste this into Claude: Add a GitHub SSE MCP server and a local
custom stdio server to my plugin. Then check what it wrote: did it use
dot-mcp-dot-json, kept separate from plugin.json? Does every path use the
CLAUDE_PLUGIN_ROOT variable instead of something hardcoded? And before it
pre-allows any tools, did it tell you to run slash-mcp first, to get the
exact names? That's the real test of a working setup.

**BOUT — outro**
Match The Transport, Not The Key. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is an auth question — is picking a key the thing that decides whether the connection works? |
| Wrong guess | B00 (WRITER LAW) | "key" corrected to "transport" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the four transport types matched to where a service runs, plus the config/naming patterns (`.mcp.json`, `CLAUDE_PLUGIN_ROOT`, exact pre-allowed tool names) that keep a multi-server plugin working |
| Anchor | the mcp-integration skill itself, named at B00 and carried through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete failure a mismatch creates (a typo'd tool name is invisible, not errored; an unset env var looks healthy until first use); BCRY states the design's working path and its failure mode together (matched transport + exact name works, one wrong character fails silently) — together they cover what the setup gets right and what it misses, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence pair, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the mcp-integration Skill's source material specifies (the four transport
types and their use cases, the lazy-load and restart-on-config-change
lifecycle, the `.mcp.json` and `CLAUDE_PLUGIN_ROOT` patterns, the exact
pre-allow tool-name format, and the unvalidated-env-var gap) — not an
inference about hidden Claude Code internals. Per simple's ONE-FLAG LAW,
when the source genuinely supports everything as stated, no flag is
fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B05's long "gets it right / where it bites" list (four transports with
documented trade-offs, the portable-path variable, automatic OAuth, the
`.mcp.json` separation, scoped pre-allow lists — versus the fragile tool-name
format, no live reload, stdio servers needing a pre-existing build/install
step, wildcard pre-allow tempting despite defeating the permission model,
and env var tokens going unvalidated at load time) is compressed into NB03,
keeping only the single fact a general audience needs and can act on — the
exact-match tool name with no error on mismatch, plus the unvalidated env
var — and dropping the Claude-Code-internals gaps (no live reload, the
verbose full strengths inventory) that assume a technical audience
simple/hai-simple doesn't target; Teardown framing ("gets it right," "where
it bites") is stripped to a plain mechanism-and-consequence description,
per the NO JUDGMENT register check; BVDT's verdict facts (the four
transports, the naming and path patterns, the gaps) are merged into the
single BCRY carry-out sentence pair rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's prompt ("Add GitHub SSE MCP server and a local custom stdio
server to my plugin") carried over unchanged — it was already a concrete,
paste-ready prompt needing no extra setup, so it's actually runnable by any
viewer today; BOUT kept, re-skinned to the Humanitarians AI outro. Total:
B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`McpIntegrationAnatomy` / `McpIntegrationDesign` / `McpIntegrationTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
