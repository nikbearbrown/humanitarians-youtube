# Why Great Content Doesn't Always Perform? — Shubham G.

A 2:57.9 ai-explainer (Plain register) on why strong content can still underperform — audience fit, distribution, timing, format, algorithms and paid reach — and when the content itself is the problem.

## This week's contribution
- **Question:** why doesn’t great content always perform, and how do you find the weak link?
- **Built:** a 14-beat beat sheet (cold open → hesitant-writer summary → reach chain → audience fit → distribution → timing → format → signal loop → paid reach → diagnose flow → verdict → Your Turn → outro), new dual-aspect Remotion scenes, and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, frame QC, type-lock). No statistics are used; illustrative visuals are labelled.
- **Next:** human watch-through, PM review.

## Human and AI work
- **My decisions:** topic and brief; Beat 2 opens "Hi, I'm Shubh… this video is about…"; chip "@Shubh & @HumanitariansAI" on every Claude page (start, middle, end); a new video rather than a variation of earlier reels; greeting "Aloha"; 16:9 + 9:16 deliverables.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote the scene code, ran the pipeline and the visual QC; Kokoro `af_bella` generated the narration (AI voice — not a recording of me); Remotion rendered every visual.
- **Rejected or corrected:** Beat 2 corrects the starting misconception on screen ("always" → "still", "finds" → "has to reach"); layout and type defects found in QC were fixed in scene source or portrait-only props (BUILD-LOG.md).
- **Unverified / open:** a full human watch-and-listen review is still pending. The brief's reference link was the YouTube home page, so no reference video was used.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), Windows 11; exact upstream commit not recorded. Local toolkit changes: TOOLKIT-CHANGES.md.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16, portrait-only prop overrides; applied with `portrait_props.py`).
- **Custom scenes:** `scenes/ContentPerformance.tsx` — ReachChain, AudienceFit, DistributionPaths, TimingWindow, FormatFit, SignalLoop, PaidReach, DiagnoseFlow (dual-aspect in one file). Imported helpers, copied as they stood at build time: `scenes/SocialAiVisibility.tsx`, `scenes/ContentRepurpose.tsx`, `scenes/OneIntoTen.tsx`. Copy all into `runtime/remotion/src/scenes/` and register each scene as `<Name>` and `<Name>916` in Root.tsx.
- **Commands:** see BUILD-PROMPT.md. On Windows set `PYTHONUTF8=1`; review cuts used `ART_NO_DRAWTEXT=1`.
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 2:57.9 — SHA-256 `13a826fa6f9dd58b169d760b9c0ca33ef581b6e65782fed878f548a56e8751f7` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 2:57.9 — SHA-256 `069e35ba2e3ef830476d966f2b7353fde35bbe38854e8dcbb84f14e7dd20e4d3` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
