# SOURCES — Testing AI Video Editors, and a Setup Guide for New Fellows

## Primary: Rohan's own work

| Source | What it supports |
|---|---|
| Claude Code session, project `D:\Rohan\Claude\HyperFrames`, 2026-09-16 (transcript `5ac80453-…`) | the whole HyperFrames test: the ask, the glass-on-cream conflict, the phonetic caption fix, the 61 GB render scratch, the 94-line / 0-overlap caption check |
| `D:\Rohan\Claude\HyperFrames\videos\suno-part-1-glass\out\suno-part-1-glass.mp4` | the test's output: 1920 × 1080, 245.17 s. SHA-256 in `pantry/hf-source.sha256`. Not committed (a render); frames used in B03 are in `pantry/` |
| `pantry/hf-t002.png`, `hf-t012.png`, `hf-t044.png`, `hf-t078.png` | four frames extracted from that output with `ffmpeg -ss <t> -frames:v 1`; Rohan's own footage re-edited by the agent |
| `pantry/hf-captions-clip.mp4` | a 6 s excerpt (76–82 s) kept as evidence of the word-by-word captions; not shown in the reel |
| `~/.claude.json` → `mcpServers.openreel` | OpenReel Desktop's MCP shim is installed and registered with Claude Code |
| Rohan, in chat, 2026-09-25 | the four tools he looked at; the guide's scope (Discord, Suno, Midjourney, Canva, account access, how to use each); that the guide is not written yet |
| Rohan, 2026-08-29 | Suno Pro access: log into the HAI Discord, then choose Discord as the Suno sign-in method |
| `fellows/rohan-v/2026-09-11-midjourney-part-1-your-first-image/` | Midjourney access through the Humanitarians AI Discord |

## Secondary: the tools

| Tool | Source |
|---|---|
| Remotion | remotion.dev; Brutalist's own `runtime/remotion/` |
| HyperFrames | github.com/heygen-com/hyperframes — README, v0.8.43 (cloned 2026-09-16) |
| OpenReel | github.com/Augani/openreel-video (MIT) — "The open source CapCut alternative. Professional video editing in your browser." |
| DaVinci Resolve MCP | github.com/samuelgursky/davinci-resolve-mcp — MCP server over Resolve's scripting API; external scripting gated to Studio, free edition via an in-app bridge |

No third-party logos are reproduced: B02 draws each tool's *idea* (code, a web
page, a timeline, a grading wheel) instead of its mark.
