# My First Week at Humanitarians AI — Shubham G.

A 1:54 ai-explainer (Plain register, @HumanitariansAI) on three things I learned in my
first week: the partnership with Homes of Hope, why English as a second language
matters for the girls' studies and job search, and how AI helps create the learning
content, with people at the center.

## This week's contribution
- **Question:** what did I actually learn in my first week at Humanitarians AI?
- **Built:** a 10-beat beat sheet, a new dual-aspect `PartnerBridge` scene, reuse of the scenes from the previous reel (props only), and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, paperwork, frame QC, type-lock).
- **Next:** confirm the lesson-loop description with the team; human watch-through; PM review.

## Human and AI work
- **My decisions:** topic and brief; partner name "Homes of Hope"; keep the AI-content description general; only claims from my brief; reference link omitted; Kokoro `af_bella` voice; chip @HumanitariansAI on every Claude page.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote PartnerBridge and the prop extensions, ran the pipeline and QC; Kokoro `af_bella` narration (AI voice — not a recording of me); Remotion visuals. No photographs or likenesses of real children.
- **Rejected or corrected:** a two-word writer correction ("the technology" → "the people") didn't work because the component matches single words; changed to technology → people and subject → door. Portrait recap lines were shortened to stay legible.
- **Unverified / open:** the lesson loop (idea → AI drafts → review → learn → feedback) is my understanding, framed that way in the narration, and not documented HAI process. Needs confirmation.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), used 2026-09-27 on Windows 11; exact upstream commit not recorded. Local patches: see TOOLKIT-CHANGES.md.
- **Source commit for this export:** this folder on branch `shubham-g`.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16).
- **Custom scenes:** `scenes/PartnerBridge.tsx` (both aspects), plus `scenes/SocialAiVisibility*.tsx` and `scenes/ebGaramond.ts`, which it imports.
- **Commands:** BUILD-PROMPT.md (`PYTHONUTF8=1`, `ART_NO_DRAWTEXT=1` on Windows).
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 1:54.4 — SHA-256 `9eeb328ef514364b14216150ba1d396f421079c86a9200c66ac6f7b80e3c6b9e` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 1:54.4 — SHA-256 `dee4d55cc70d2e20edb5302351262faeda48778bc64f53e6adc2e5a57106de2a` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
