# Build MCPB — Packaged, Not Sandboxed

Package a local MCP server as an MCPB and it's easy to assume the bundle
itself got safer along with the packaging — like putting the code in a
container. Open the manifest and there's no permissions block and no
sandbox field to check: a packaged MCPB runs with exactly the same file
access as the original, unpackaged script. Watch the anchor: one
environment variable, `ROOT_DIR`, carries two real traps through the
reel — the manifest's env var name has to match the server code's read
exactly (no auto-prefix, no transform; get it wrong and the value comes
back silently empty, no error), and even a correctly-named variable flows
into your handler with no path check on it, because there's no sandbox
to add one for you. Neither "works on my machine" nor "fails on a clean
machine" is proof of anything about the packaging step itself.

**Topic:** CLAUDE · PLUGIN DEV · MCPB
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-build-mcpb

---

## Chapters

0:00 Does bundling it as an MCPB make it easy to run?
0:10 Sounds like a safer container
0:19 Same access as the raw script
0:35 The anchor — one env variable
0:45 Zip, then launch exactly
1:03 Wrong name, no error
1:18 The anchor returns — no check on it
1:31 Neither one is proof
1:48 Carry-out
1:59 Your turn
2:23 Outro

---

## YOUR TURN

"Build an MCPB that reads files from a directory I configure at install
time. Watch three things: does the env var name in the manifest's
mcp_config exactly match what the server code reads? Does the server
validate that every requested path stays inside that configured root, or
would a dot-dot-slash escape it? And does the build script bundle
dependencies with esbuild, or does it assume node_modules will already be
there?"

Why it's worth running: it forces you to check both traps the reel just
named — the silent name-mismatch and the missing path check — against a
Claude Code build you actually watch happen.

---

## Deliberately not claimed

This reel names the manifest's real sections and tokens (`server.mcp_config`,
`${__dirname}`, `${user_config.*}`, `user_config` with `type: "directory"`
and `sensitive: true`, `compatibility`) and the build pipeline (esbuild for
Node, vendored dependencies for Python, native extensions needing a
per-platform build) exactly as the source script states them — no manifest
file was read from disk. `ROOT_DIR` is an illustrative variable name built
to carry the ANCHOR LAW's one running example, not a documented example
from the source; the two traps it demonstrates (silent name-mismatch, no
path validation) are both stated directly in the source's own narration. It
never ranks whether the source skill's documentation buries any particular
trap well or badly — that's a design judgment, and this register states the
mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudePlugins #MCP #MCPB #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
