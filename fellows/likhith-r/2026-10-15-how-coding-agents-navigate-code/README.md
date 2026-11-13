# How Coding Agents Navigate Code

**Fellow:** Likhith R. · **Week:** 2026-10-12 to 2026-10-18 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on how AI coding agents navigate a codebase they have never seen: map the project, search for what the bug mentions, make a small edit, run the tests, and loop on the result.

## This week's contribution
- **Question:** How does a coding agent fix a bug in a codebase it has never seen?
- **Prediction:** I expected an agent to read the whole codebase first and then write a fix.
- **What I built/tried:** 12 beats on the explore, search, edit, verify and iterate loop, using one toy repo throughout. The file tree, search hits, edit, failing test and passing re-run on screen come from a scripted replay of the tool calls with real pytest output (`evidence/agent_loop.py`). Seven custom dual-aspect scenes in `scenes/CodingAgents.tsx`.
- **Observed result:** Both cuts render at native 4K (68.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Watch a coding agent fix a real bug in one of my repos and count how many files it actually opens before editing.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Largely on its own" kept, not upgraded to "on its own"; the verdict adds that a person still reviews the change and the loop is only as good as the tests.
- "Rather than reading every file" means reads are driven by search results, not that the agent never reads broadly.
- Exact-string replacement describes Claude Code's Edit tool; other agents use patches or diffs, and the on-screen note says so. No model names or benchmarks.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/CodingAgents.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/CodingAgents.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-coding-agents/`):
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
- **Landscape** — [Watch `landscape/AICodingAgents_LikhithR.mp4`](https://drive.google.com/file/d/1Rf-OmOW3hoj99Ar-LsFMMEgC9V5DNUrl/view?usp=sharing) — 3840×2160 — 68.0 s — SHA-256 `d6fba0acd0ac48ef79dc9f48e2be44202b59b71b28c57ed73f71bbf548de6a42` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/AICodingAgents_LikhithR.mp4`](https://drive.google.com/file/d/1_8_BpXzeBqm8JzLfnpPIdl_SPbnfpsjQ/view?usp=sharing) — 2160×3840 — 68.0 s — SHA-256 `f97502c121aec05bc9ebbf0be1947d924afc9c5fe0c72d0f366fe282f8c0d30f` (final master, `.verified.json` receipt: ready)
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
