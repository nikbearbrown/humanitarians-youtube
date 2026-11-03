# Week 3 Learning: How to Use Midjourney? — Shubham G.

A 2:30.3 ai-explainer (Plain register) a hands-on Midjourney how-to for content creation: prompt → generate → refine → upscale and use → check before posting.

## This week's contribution
- **Question:** how do you actually use Midjourney, step by step, to make images for content?
- **Built:** a 11-beat beat sheet (cold open → hesitant-writer summary → prompt anatomy → four-image grid → refine loop → upscale and use → post check → verdict → Your Turn → outro), new dual-aspect Remotion scenes, and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, frame QC, type-lock). No statistics are used; illustrative visuals are labelled.
- **Next:** human watch-through, PM review.

## Human and AI work
- **My decisions:** topic and brief; Beat 2 opens "Hi, I'm Shubh… this video is about…"; chip "@Shubh & @HumanitariansAI" on every Claude page (start, middle, end); a new video rather than a variation of earlier reels; greeting "Olá"; 16:9 + 9:16 deliverables.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote the scene code, ran the pipeline and the visual QC; Kokoro `af_bella` generated the narration (AI voice — not a recording of me); Remotion rendered every visual.
- **Rejected or corrected:** Beat 2 corrects the starting misconception on screen ("for" → "with" (you pick, refine and re-prompt)); layout and type defects found in QC were fixed in scene source or portrait-only props (BUILD-LOG.md).
- **Unverified / open:** a full human watch-and-listen review is still pending. The brief's reference link was the YouTube home page, so no reference video was used.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), Windows 11; exact upstream commit not recorded. Local toolkit changes: TOOLKIT-CHANGES.md.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16, portrait-only prop overrides).
- **Custom scenes:** `scenes/MidjourneySteps.tsx`, `scenes/MidjourneySteps916.tsx` — PromptAnatomy, FourGrid, RefineLoop, UpscaleToUse, PostCheck. Imported helpers, copied as they stood at build time: `scenes/SocialAiVisibility.tsx`, `scenes/ContentRepurpose.tsx`, `scenes/OneIntoTen.tsx`. Copy all into `runtime/remotion/src/scenes/` and register each scene as `<Name>` and `<Name>916` in Root.tsx.
- **Commands:** see BUILD-PROMPT.md. On Windows set `PYTHONUTF8=1`; review cuts used `ART_NO_DRAWTEXT=1`.
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 2:30.3 — SHA-256 `f520e374141c9f5e5faf77d31d4f85001688ea6396551618185d340c13cd4165` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 2:30.3 — SHA-256 `53c87ed3d482fff050327814fd28ae581627d852d933ea84ac7423656d59b442` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
