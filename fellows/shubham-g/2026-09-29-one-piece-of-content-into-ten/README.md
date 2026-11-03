# How to Turn 1 Piece of Content Into 10? — Shubham G.

A 2:25.7 ai-explainer (Plain register) on breaking one long-form video into atoms and reshaping them — not copying them — into ten platform-native pieces.

## This week's contribution
- **Question:** how do you turn one long video into ten pieces that each feel native to their platform?
- **Built:** a 11-beat beat sheet (cold open → hesitant-writer summary → atoms → ten formats → reshape, don’t copy → release runway → quality gate → verdict → Your Turn → outro), new dual-aspect Remotion scenes, and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, frame QC, type-lock). No statistics are used; illustrative visuals are labelled.
- **Next:** human watch-through, PM review.

## Human and AI work
- **My decisions:** topic and brief; Beat 2 opens "Hi, I'm Shubh… this video is about…"; chip "@Shubh & @HumanitariansAI" on every Claude page (start, middle, end); a new video rather than a variation of earlier reels; greeting "Bonjour"; 16:9 + 9:16 deliverables.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote the scene code, ran the pipeline and the visual QC; Kokoro `af_bella` generated the narration (AI voice — not a recording of me); Remotion rendered every visual.
- **Rejected or corrected:** Beat 2 corrects the starting misconception on screen ("copied" → "reshaped" (the film’s thesis)); layout and type defects found in QC were fixed in scene source or portrait-only props (BUILD-LOG.md).
- **Unverified / open:** a full human watch-and-listen review is still pending. The brief's reference link was the YouTube home page, so no reference video was used.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), Windows 11; exact upstream commit not recorded. Local toolkit changes: TOOLKIT-CHANGES.md.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16, portrait-only prop overrides).
- **Custom scenes:** `scenes/OneIntoTen.tsx`, `scenes/OneIntoTen916.tsx` — AtomSplit, TenFormats, ReshapeNotCopy, ReleaseRunway, QualityGate. Imported helpers, copied as they stood at build time: `scenes/SocialAiVisibility.tsx`, `scenes/ContentRepurpose.tsx`. Copy all into `runtime/remotion/src/scenes/` and register each scene as `<Name>` and `<Name>916` in Root.tsx.
- **Commands:** see BUILD-PROMPT.md. On Windows set `PYTHONUTF8=1`; review cuts used `ART_NO_DRAWTEXT=1`.
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 2:25.7 — SHA-256 `f3a1e46ea37faa99312c29e49aac8231148565ea573c67af1f8e255213a748c3` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 2:25.7 — SHA-256 `6f3b061f3041f174193136e7be5daa3d884c5015e0aa8d92f4c4e3f3c4aef369` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
