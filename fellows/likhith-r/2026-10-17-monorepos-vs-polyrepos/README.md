# Monorepos vs. Polyrepos

**Fellow:** Likhith R. · **Week:** 2026-10-12 to 2026-10-18 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on monorepos versus polyrepos: one repository with a single history and atomic cross-project commits, versus one repository per project with independent ownership, and the tooling (sparse checkout, build caching) monorepos need at scale.

## This week's contribution
- **Question:** Should a company keep its code in one repository, or many?
- **Prediction:** I expected one approach to be clearly better, with big tech's monorepos proving the case.
- **What I built/tried:** 12 beats on polyrepos, monorepos, atomic commits, scale problems, sparse checkout and remote build caching. The atomic commit across three projects and the sparse-checkout file counts come from a real toy monorepo (`evidence/mono_demo.sh`), and the cache counts from `evidence/build_cache_toy.py`. Seven custom dual-aspect scenes in `scenes/MonoPoly.tsx`.
- **Observed result:** Both cuts render at native 4K (69.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Set up sparse checkout and a remote build cache on a mid-size repo and measure the time saved.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- Google's Piper is not a git repository; the video says "big tech" for the tooling and dates Google's figures on screen (Jan 2015, approximate).
- "Dependencies stay in sync automatically" softened to "stay in sync": one version of each internal library per commit, but third-party pinning still takes work.
- The verdict says there's no universal winner; build-time bars are illustrative.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/MonoPoly.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/MonoPoly.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-monorepos-polyrepos/`):
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
- **Landscape** — [Watch `landscape/MonoreposVsPolyrepos_LikhithR.mp4`](https://drive.google.com/file/d/16tJUixU1YwyD2Td6-qA0RSeTmZx3AcTd/view?usp=sharing) — 3840×2160 — 69.0 s — SHA-256 `afb5f54cff560ab1512d42ae0d7f26746400c1d919cd387b0e3eec4054e70989` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/MonoreposVsPolyrepos_LikhithR.mp4`](https://drive.google.com/file/d/13Gg8e8KlvQ_1x2zRWFWQU2cIXaA5VNUo/view?usp=sharing) — 2160×3840 — 69.0 s — SHA-256 `364ae677d628f6ae682d8e9a69f58494d2b4bd42519dbee35e71689eb0e593b0` (final master, `.verified.json` receipt: ready)
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
