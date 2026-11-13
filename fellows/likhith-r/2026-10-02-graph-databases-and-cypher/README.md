# Graph Databases and Cypher

**Fellow:** Likhith R. · **Week:** 2026-09-28 to 2026-10-04 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on graph databases: they store nodes and edges directly and follow those edges when you query, so a three-hop question is a pattern in Cypher instead of three joins in SQL.

## This week's contribution
- **Question:** Why not keep relationship-heavy data in ordinary tables?
- **Prediction:** I expected the SQL-versus-graph contrast to be mostly about speed, with graphs simply "faster" for connected data.
- **What I built/tried:** 12 beats on what a graph database stores, how SQL needs one join per hop, how a graph follows edges, Cypher patterns, a three-hop query and where graphs fit. Every table, query and result on screen comes from a real run of the same toy network in Kuzu (Cypher) and SQLite (`evidence/graph_demo.py`). Seven custom dual-aspect scenes in `scenes/GraphDb.tsx`.
- **Observed result:** Both cuts render at native 4K (63.8 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Load a real relationship dataset into Kuzu or Neo4j and compare how the same multi-hop question reads and runs in SQL and Cypher.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Joins get slower with depth" stated as "every hop adds a join"; with indexes SQL pays a lookup per hop, not a full scan, so no speed claim is made.
- "Deep queries stay fast" stated as "the work tracks what you visit"; the verdict adds that plain rows and totals are still a job for tables.
- The Beat 2 correction was reworded so the voice names the misconception before correcting it; link labels repositioned so none touches a node or arrow.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/GraphDb.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/GraphDb.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-graph-databases/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9 review
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md) · executable evidence in [`evidence/`](evidence/)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/GraphDatabasesAndCypher_LikhithR.mp4`](https://drive.google.com/file/d/1ZBYDP9I0G9hrcCbxuebPeMMlmiEXtgwA/view?usp=sharing) — 3840×2160 — 63.8 s — SHA-256 `4b0d2881e5de0439adad649b4ebc16aec304fc8abe740d207fd9cf221a5a31a1` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/GraphDatabasesAndCypher_LikhithR.mp4`](https://drive.google.com/file/d/1s8YVoHdLYlYsF6XkhGooEqrOq3bYlZMT/view?usp=sharing) — 2160×3840 — 63.8 s — SHA-256 `5150a3ff11d2a767573cdeb9b466385b414bcd49deb63af3824c474e310f0ed7` (final master, `.verified.json` receipt: ready)
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
