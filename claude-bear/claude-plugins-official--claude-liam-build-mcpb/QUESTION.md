# QUESTION.md

**Question:** Claude can package my local MCP server as an MCPB — does
bundling it that way mean it's now sandboxed, or otherwise safer to run than
the raw script?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-build-mcpb`, a Teardown skill-explainer
under `anthropics/claude-plugins-official/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json narration is fully
self-contained — every fact used in this redo (bundle = zip of
`manifest.json` + `server/` + `icon.png`; the host launches
`server.mcp_config`'s command verbatim; `${__dirname}` for bundle-relative
paths and `${user_config.*}` for install-time values; env var names carry NO
auto-prefix, so a name mismatch is a silent `undefined`/nil with no error;
MCPB ships with no sandbox and no permissions block, so path validation and
spawn allowlisting are the developer's own responsibility; the Node build
uses `esbuild` and the Python build vendors dependencies, with native
extensions needing a per-platform build; and shipping should be tested on a
machine without the dev toolchain, since a "works on my machine" failure
almost always traces to an unbundled dependency) comes directly from the
source's own `narration_text` (B00/B01/B02). No skill file on disk was
consulted or needed — the source script itself is the fact base, exactly as
the `claude-for-legal--claude-liam-matter-intake` sibling redo used its
source's own narration. The one fact this redo does NOT carry over is the
source's own Teardown VERDICT judgment (BVDT/B05: "gets five things right /
here's where it bites," ranking the skill file's documentation quality) —
that is design judgment, which Plain register drops per hai-simple's
register-rewrite rule; only the underlying mechanism facts survive.

**The anchor:** one made-up but representative environment-variable example
(`ROOT_DIR`) is used to carry two of the source's real, generic facts (the
no-auto-prefix trap and the no-sandbox/no-path-validation trap) through a
single concrete case, planted at B03 and paid off at B06 — the ANCHOR LAW's
"one running example" requirement. `ROOT_DIR` itself is illustrative (the
source never names a specific variable), but the two traps it demonstrates
are both stated directly in the source's own narration, not invented.
