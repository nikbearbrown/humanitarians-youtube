# AI Content vs. Human Creativity: What Works Better? — Shubham G.

A 2:40 ai-explainer (Plain register) on how AI can turn one human-made long-form video into many
social assets — clips, captions, a blog post, a carousel, social posts — and where people still win.

## This week's contribution
- **Question:** AI content or human creativity — which works better when one piece of content has to become many?
- **Built:** an 11-beat beat sheet (cold open → hesitant-writer summary → human original → clips → cascade → brand voice → AI-vs-people verdict → recap → Your Turn → outro), five new dual-aspect Remotion scenes, and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, frame QC, type-lock). No statistics are used; example captions, voice guide and draft are labelled illustrative.
- **Next:** human watch-through, PM review.

## Human and AI work
- **My decisions:** topic and brief (repurposing one long video across platforms while keeping brand voice); Beat 2 opens "Hi, I'm Shubh… this video is about…"; chip "@Shubh & @HumanitariansAI" on every Claude page (start, middle, end); a new video rather than a variation of earlier reels; 16:9 + 9:16 deliverables.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote the scene code, ran the pipeline and the visual QC; Kokoro `af_bella` generated the narration (AI voice — not a recording of me); Remotion rendered every visual.
- **Rejected or corrected:** the common "AI content beats human creativity" framing is the misconception the Beat 2 writer corrects to "scales"; layout collisions, safe-area bleed and sub-floor type found in QC were fixed in scene source (BUILD-LOG.md).
- **Unverified / open:** a full human watch-and-listen review is still pending. The brief's reference link was the YouTube home page, so no reference video was used.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), Windows 11; exact upstream commit not recorded. Local toolkit changes: TOOLKIT-CHANGES.md.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16). `vertical/portrait_props.py` applies the portrait-only prop overrides after `./art vertical`.
- **Custom scenes:** `scenes/ContentRepurpose.tsx` (16:9) and `scenes/ContentRepurpose916.tsx` (9:16). They import helpers from `SocialAiVisibility.tsx` (see `../2026-09-26-social-ai-brand-visibility/scenes/`).
- **Commands:** see BUILD-PROMPT.md. On Windows set `PYTHONUTF8=1`; review cuts used `ART_NO_DRAWTEXT=1`.
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 2:40.4 — SHA-256 `da61193dccec0b95750e686866e9435f8148bde5dd33f5f81abc05c61457715f` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 2:40.4 — SHA-256 `833ea4cf657725414ccd5ddc054bf833351c74ac188a6a5d177165e65e464bf4` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
