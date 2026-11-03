# Why MCP Exists

**Fellow:** Likhith R. · **Week:** 2026-09-09 to 2026-09-13 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on why the Model Context Protocol exists when APIs already let software talk to software: each tool becomes one MCP server that any agent can discover and call the same way, on top of the real API.

## This week's contribution
- **Question:** If APIs already connect software, why do AI agents need MCP?
- **Prediction:** I expected the difference between APIs and MCP to be easy to show in 60 seconds.
- **What I built/tried:** 12 beats covering seven points I set: the API hook; per-tool auth, formats and docs; one server per tool; runtime tool discovery; adding a tool without hardcoding; agents chaining tools; the checkout/terminal analogy. Tool discovery is shown from a real run of a toy MCP server (`evidence/mcp_discovery.py`). Seven custom dual-aspect scenes in `scenes/McpProtocol.tsx`.
- **Observed result:** Both cuts render at native 4K (63.9 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Connect an agent to a real vendor's MCP server and compare the setup effort with a direct API integration.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, and the required opening line.
- Watched both cuts and signed off every claim in `FACTCHECK.md`.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- MCP does not remove authentication: each server still authenticates to the API it wraps. The verdict card says so.
- "No custom code per tool" is true from the agent's side; someone still writes each server once. The "3 + 4 = 7, each built once" count makes that explicit.
- The payment-terminal analogy is mine and is labelled as an analogy; tool names and formats on screen are illustrative.
- Portrait layouts redesigned so every text cluster clears the 9:16 type floor; McpStandard's bar fill darkened for contrast.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `6a8380a`.
- **Source commit used for this export:** not committed — `6a8380a` plus local changes: `scenes/McpProtocol.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` added under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920, and `durationSeconds` hooks added to `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/McpProtocol.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-mcp-protocol/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9 review
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
  ```bash
  # executable evidence (see SOURCES.md for the exact environment)
  ls evidence/
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/MCPProtocol_LikhithR.mp4`](https://drive.google.com/file/d/1XgCF1TcB2SXm0boignP44NhPpXfPC4ll/view?usp=sharing) — 3840×2160 — 63.9 s — SHA-256 `8b7ab181b4265e7f13f810f5188f0b5467f611329653129045c8211a6f5db39a` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/MCPProtocol_LikhithR.mp4`](https://drive.google.com/file/d/12da0N5sWIHYEPASazZzt_4JBonPygMEZ/view?usp=sharing) — 2160×3840 — 63.9 s — SHA-256 `57ad39fccc10072da5a3c744590932ee13fcdbbb32e17ddd3a5a55c94eca9ce5` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `BUILD-PROMPT.md` — the build prompt
- `scenes/` — custom Remotion scene code (`JevExplainer.tsx` holds the shared stage helpers; `HaiOutro.tsx` is the outro)
- `evidence/` — the executed code and its real output shown on screen
