# Spec-Driven Development

**Fellow:** Likhith R. · **Week:** 2026-09-21 to 2026-09-27 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on why spec-driven development makes AI-assisted coding maintainable: write the spec first, treat it (not the prompt history) as the source of truth, and use it to cut guesswork, review changes, keep context, and catch scope drift.

## This week's contribution
- **Question:** Why does spec-driven development make AI-assisted coding maintainable?
- **Prediction:** I expected this one to go faster than the Jev video by reusing its scenes, and an argument-style topic to need little sourcing.
- **What I built/tried:** 12 beats covering seven points I set: the vibe-coding hook; the definition; less guesswork; reviewability; living documentation; visible scope drift; maintainable at scale — one login-feature example throughout. Rendered natively in 16:9 and 9:16, with seven custom dual-aspect scenes in `scenes/SpecDriven.tsx` (which imports shared helpers and the outro from `scenes/JevExplainer.tsx`).
- **Observed result:** Both cuts render at native 4K (61.8 s). 16:9 passes GATE F, L and V (0/0); every 9:16 scene passes GATE V on its own frames.
- **Next experiment:** Try spec-driven development with GitHub Spec Kit on a small real feature and note where the spec caught or missed problems.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: on-screen greeting "Namaskaram, Likhith", the @HumanitariansAI channel, and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- Argument video: no productivity or defect numbers claimed; the B08 curve is labelled "qualitative sketch, not data".
- Example files, code and diff sizes are labelled illustrative on screen.
- 16:9 tag wrapping (B06) and five portrait layout defects (B01, B03, B06, B08, B11) fixed after visual QC.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit and date checked:** nikbearbrown/brutalist.art `6a8380a` (2026-09-20), checked 2026-09-26.
- **Source commit used for this export:** not committed — `6a8380a` plus local changes: `scenes/SpecDriven.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` added under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920, and `durationSeconds` hooks added to `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/SpecDriven.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-spec-driven-development/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  python3 runtime/scripts/compile.py <reel>/vertical --review --height 3840
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/SpecDrivenDevelopment_LikhithR.mp4`](https://drive.google.com/file/d/1lGf3de61dugTHalNJzNHDWfG9TZdGgIM/view?usp=sharing) — 3840×2160 — 61.8 s — SHA-256 `40b2f21a237a104cc10165f98e7b32d9258750feab838da07340bb623fee1a27` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/SpecDrivenDevelopment_LikhithR.mp4`](https://drive.google.com/file/d/16_B1_t10yiRFcdwV7STkAypsUV6Hqw2t/view?usp=sharing) — 2160×3840 — 61.8 s — SHA-256 `9d19afa894403b846ab6dea25523d2fe9cd0b1b2fe58b7ba44f5aeea38e96a96` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `scenes/` — custom Remotion scene code
