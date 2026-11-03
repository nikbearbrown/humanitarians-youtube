# Process notes — What Is MCP? (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1BS4mqXHacyxOIfFH9vQwKDVt2q36ZS23
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-08-28

Build log for `hai-what-is-mcp` (16:9) and `hai-what-is-mcp-916` (9:16 Shorts). Chronological; append-only going forward.

## Build — cli-explainer script → both cuts

**GATE L:** searched the scene library before authoring. Only 2 new components were genuine punts — `McpScaleShift` (the N×M-integrations-become-N+M diagram) and `McpToolCall` (the real tool-call results rows) — each with a `916` portrait variant. Everything else reused existing house components as-is: `ClaudeComposerAsk`, `ClaudeCodeBeat` / `ClaudeCodeBeat916`, `ClaudeVerdictArtifact` / `916`, `ClaudeTitleOutro` / `916`.

**DOUBLE-CHECK LAW:** every code listing and every output figure on screen (the `tools/list` schema, the CSV dump, the `$46.00`/`$436.20`/clean-fail results) was produced by actually running `server_v1.py` then `server_v2.py` against `expenses.csv` — nothing illustrative-but-invented. FastMCP's API was checked against the installed package directly after a fetched README summary claimed a class (`MCPServer`) that doesn't exist in the SDK.

**9:16 Shorts cut** designed per THE SHORTS LAW + the cli-explainer REVISION LAW: single cycle, no revision shown — skips straight to the working `server_v2.py` and its real output (a Short has no room to earn a failure and then fix it), and the outro points back to the long cut for the full before/after.

## Pre-final-render QC — `CHECKLIST-what-is-mcp.md`

Before the final true-4K render, a PM-approval checklist pass (`CHECKLIST-what-is-mcp.md`, kept alongside this file) logged the honest state against 6 acceptance criteria and caught 3 real gaps:

1. **Resolution** — all 11 16:9 beats had been rendered at review-pass `ART_SCALE=1` (1080p) to iterate quickly on the new components; the toolkit's actual master scale is `ART_SCALE=2` (true 4K). Flagged as not-yet-met, needing a full re-render.
2. **Stale persona/intro text** — the master beat sheets had been corrected to open B00 with the required verbatim line ("Hi, I am Simba, and this video is about...") but the working pipeline copies (`reels/hai-what-is-mcp/beat_sheet.json`, `reels/hai-what-is-mcp-916/beat_sheet.json`) still carried an older persona's text, and B00's already-rendered audio/video for both cuts reflected the stale copy.
3. **Incomplete 9:16** — only 3 of 7 Shorts beats (B00–B02) were rendered at checklist time; B03–B06 remained.

Component-level QC in that same pass had already caught and fixed defects in the new components before this checklist was written — a bar-span error, an accent-law violation (a second, redundant terracotta moment), off-safe-area text, and an under-filled canvas — each verified against rendered stills, not just code.

**Resolution of all 3 gaps, confirmed against the final artifacts:** both `beat_sheet.json` working copies now open B00 with the corrected Simba narration verbatim (confirmed by reading the final JSON); `ffprobe` on both final mp4s reports true 4K (16:9 at 3840×2160, 9:16 at 2160×3840); both cuts show `filled: 11/11` and `filled: 7/7` respectively in their `build` stamps. All 3 items closed.

**Non-blocking lint carried from the compile logs (flagged, not treated as blocking — same pattern as the 916 skin-lint notes on the Mycroft build):**
- 16:9: SPARK-LINE LAW warnings on B02 and B05 — both are the CLI-ask beats mid-revision-cycle, and their spark line is intentionally empty (they're a pure ask, not a landing statement).
- 9:16: SKIN LINT on B00/B06 — `ClaudeComposerAsk916` / `ClaudeTitleOutro916` flagged against COLD OPEN LAW / OUTRO LAW, which check for the unsuffixed pattern name. Same naming-convention false positive noted on the Mycroft build — doesn't account for the `916` responsive-variant convention.

## Final specs

| Cut | Resolution | Duration | Delivered as |
|---|---|---|---|
| 16:9 | 3840×2160 | 3:36 (215.9s) | `what-is-mcp-16x9.mp4` |
| 9:16 | 2160×3840 | 1:22 (81.9s) | `what-is-mcp-9x16.mp4` |

**Delivered:** both masters committed into `youtube/hai-what-is-mcp/` on the connected device, alongside the source materials the on-screen figures came from (`server_v1.py`, `server_v2.py`, `expenses.csv`).

## Open item — publishing not yet possible from this repo

Same open item logged on the Mycroft build: this toolkit checkout (`brutalist.art`) stops at render, and `./art final` / `./art post` / the `youtube-publisher` script aren't present here — see `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the repo root. Actual YouTube upload needs a separate, private `brutalist.yt` sibling repo with real OAuth credentials, which doesn't exist yet on this machine.
