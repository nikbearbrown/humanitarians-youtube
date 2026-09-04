# What Is MCP? — Beat Sheet

**Title:** What Is MCP?
**Slug:** hai-what-is-mcp
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** cli-explainer (16:9 long cut, full CLI → CODE → OUTPUT with one revision cycle) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision — goes straight to the working v2 server and points back to the long cut for the before/after)

Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock. DOUBLE-CHECK LAW: every code listing and every output figure was produced by actually running `server_v1.py` / `server_v2.py` against `expenses.csv` — nothing on screen is illustrative-but-invented.

## 16:9 — long cut (11 beats, 3:36 / 215.9s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 21.3s | ClaudeComposerAsk | type-on | Cold open — the ask ("smallest possible MCP server over a CSV I have") types in, answered |
| B01 | PROBLEM | 0:21 | 21.8s | McpScaleShift | illustrate | 4 apps × 4 tools → 16 hand-wired integrations; MCP bar drops in → 8 |
| B02 | CLI | 0:43 | 16.9s | ClaudeComposerAsk | type-on | Cycle 1 ask: smallest possible server, one tool, official SDK, no framework |
| B03 | CODE | 1:00 | 21.4s | ClaudeCodeBeat | illustrate | `server_v1.py` reveals line by line — the `@mcp.tool()` decorator holds as the one accent |
| B04 | OUTPUT | 1:21 | 23.1s | ClaudeCodeBeat | illustrate | Real `tools/list` JSON — empty parameters, then the whole CSV floods back, every row |
| B05 | CLI | 1:45 | 16.9s | ClaudeComposerAsk | type-on | Cycle 2 ask (the revision): real parameter, a docstring that says *when*, plus a resource |
| B06 | CODE | 2:01 | 21.2s | ClaudeCodeBeat | illustrate | `server_v2.py` reveals — typed parameter, "Use when…" docstring, `@mcp.resource` |
| B07 | OUTPUT | 2:23 | 23.4s | McpToolCall | illustrate | Real calls resolve on the spoken figures: software $46.00/3, travel $436.20/2, crypto clean-fails |
| B08 | SUMMARY | 2:46 | 25.2s | ClaudeVerdictArtifact | stagger | Verdict artifact: N×M→N+M, the description is what you author, access ≠ trust (lands last) |
| B09 | NEXT STEPS | 3:11 | 20.8s | ClaudeComposerAsk | type-on | Handoff — "Your turn." prompt types in, verbatim |
| B10 | OUTRO | 3:32 | 3.9s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline |

## 9:16 — Shorts cut (7 beats, 1:22 / 81.9s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision — skips straight to the working `server_v2.py` and its real output, and points back to the long cut for the full before/after.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 12.1s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | PROBLEM | 0:12 | 13.3s | McpScaleShift916 | 16 integrations → 8, condensed |
| B02 | CODE | 0:25 | 12.9s | ClaudeCodeBeat916 | The working tool — docstring is the accent |
| B03 | OUTPUT | 0:38 | 13.0s | McpToolCall916 | Real calls: software, travel, clean-fail on crypto |
| B04 | SUMMARY | 0:51 | 15.1s | ClaudeVerdictArtifact916 | Verdict, condensed — access ≠ trust lands last |
| B05 | NEXT STEPS | 1:06 | 9.8s | ClaudeComposerAsk916 | Handoff, condensed |
| B06 | OUTRO | 1:16 | 5.9s | ClaudeTitleOutro916 | Title, "full build on the channel" |

`beat_sheet.json` in each reel's own folder is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
