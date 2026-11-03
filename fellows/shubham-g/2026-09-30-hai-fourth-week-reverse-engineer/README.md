# Week 4 Learning: Build It, Then Reverse Engineer It — Shubham G.

A 2:45.7 ai-explainer (Plain register) on building one learning video and then reverse engineering it into a decision log, a template and a six-step playbook so new recruits and editors can work faster and more consistently.

## This week's contribution
- **Question:** how do you turn one finished video into a playbook the next editor can follow?
- **Built:** a 13-beat beat sheet (cold open → hesitant-writer summary → build then reverse → decision log → template → playbook steps → fix to rule → gains → limits → verdict → Your Turn → outro), new dual-aspect Remotion scenes, and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, frame QC, type-lock). No statistics are used; illustrative visuals are labelled.
- **Next:** human watch-through, PM review.

## Human and AI work
- **My decisions:** topic and brief; Beat 2 opens "Hi, I'm Shubh… this video is about…"; chip "@Shubh & @HumanitariansAI" on every Claude page (start, middle, end); a new video rather than a variation of earlier reels; greeting "Jambo"; 16:9 + 9:16 deliverables.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote the scene code, ran the pipeline and the visual QC; Kokoro `af_bella` generated the narration (AI voice — not a recording of me); Remotion rendered every visual.
- **Rejected or corrected:** Beat 2 corrects the starting misconception on screen ("scratch" → "a playbook"); layout and type defects found in QC were fixed in scene source or portrait-only props (BUILD-LOG.md).
- **Unverified / open:** a full human watch-and-listen review is still pending. The brief's reference link was the YouTube home page, so no reference video was used.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), Windows 11; exact upstream commit not recorded. Local toolkit changes: TOOLKIT-CHANGES.md.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16, portrait-only prop overrides; applied with `portrait_props.py`).
- **Custom scenes:** `scenes/Week4Playbook.tsx` — BuildThenReverse, DecisionLog, TemplateSlots, PlaybookSteps, FixToRule, ThreeGains, PlaybookLimits (dual-aspect in one file). Imported helpers, copied as they stood at build time: `scenes/SocialAiVisibility.tsx`, `scenes/ContentRepurpose.tsx`, `scenes/OneIntoTen.tsx`, `scenes/ContentPerformance.tsx`. Copy all into `runtime/remotion/src/scenes/` and register each scene as `<Name>` and `<Name>916` in Root.tsx.
- **Commands:** see BUILD-PROMPT.md. On Windows set `PYTHONUTF8=1`; review cuts used `ART_NO_DRAWTEXT=1`.
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 2:45.7 — SHA-256 `0a69b29fd20edc4713a304b5108ca6c6e51a88e3630e58b958a04fa2b2ec8006` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 2:45.7 — SHA-256 `c778ae8cfe8421322d95c8b67b7327ccfaa4eb2c39f8f30ac1cfdc87f9aa5e5f` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
