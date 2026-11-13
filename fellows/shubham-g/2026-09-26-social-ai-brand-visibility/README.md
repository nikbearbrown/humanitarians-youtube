# Can AI Content Automation Pace Brand Visibility? — Shubham G.

A 2:58 ai-explainer (Plain register) on five ways AI content automation can support a
brand's social-media visibility, and the limit that keeps it honest.

## This week's contribution
- **Question:** can AI content automation help a brand get seen more on social media, and where does it stop helping?
- **Built:** a 12-beat beat sheet (cold open → hesitant-writer summary → five levers → honest limit → verdict → Your Turn → outro), six new dual-aspect Remotion scenes, and native 16:9 + 9:16 4K exports.
- **Result:** both exports pass the toolkit gates (beat lint, paperwork, frame QC, type-lock). No statistics are used anywhere (author constraint); illustrative visuals are labelled.
- **Next:** human watch-through, PM review.

## Human and AI work
- **My decisions:** topic and the five-lever brief; no unverifiable statistics; narrator introduced as Shubh with the Kokoro `af_bella` voice; chip "@Shubh & @HumanitariansAI" on every Claude page; reference-video link omitted; 16:9 + 9:16 deliverables.
- **AI tools/voices:** Claude (Claude Code) drafted the script and beat sheet, wrote the scene code, ran the pipeline and the visual QC; Kokoro `af_bella` generated the narration (AI voice — not a recording of me); Remotion rendered every visual.
- **Rejected or corrected:** an "algorithms reward regular posting" line was cut (unverifiable); accent-coloured text was moved to ink after failing WCAG contrast; landscape-only layouts were rebuilt as native portrait scenes. See FACTCHECK.md and BUILD-LOG.md.
- **Unverified / open:** a full human watch-and-listen review is still pending.

## Reproduce
- **Brutalist version:** `brutalist.art` main-branch download (zip, no `.git`), used 2026-09-26 on Windows 11; exact upstream commit not recorded. Local toolkit patches are listed in TOOLKIT-CHANGES.md.
- **Source commit for this export:** this folder on branch `shubham-g`.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16, portrait-only prop overrides).
- **Custom scenes:** `scenes/SocialAiVisibility.tsx` (16:9), `scenes/SocialAiVisibility916.tsx` (9:16), `scenes/ebGaramond.ts` (bundled-font loader). Copy into `runtime/remotion/src/scenes/` (ebGaramond into `tokens/`) and register the compositions as described in TOOLKIT-CHANGES.md.
- **Commands:** see BUILD-PROMPT.md. On Windows set `PYTHONUTF8=1`; review cuts used `ART_NO_DRAWTEXT=1`.
- **Checks:** CHECKS-REPORT.md, FACTCHECK.md, TYPECHECK.md, vertical/TYPECHECK.md. No approvals are claimed.

## Watch and review
- Landscape — 3840×2160 — 2:58.5 — SHA-256 `3be7de2a3d59d45c0e25615cb53ac39916c4fe14f001cab118238f6f2f9c8c67` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- Vertical — 2160×3840 — 2:58.5 — SHA-256 `4aa414d2fd41973289fcf356c91d41010b77b6f986321d06b9e8dfabf6abf889` — Drive: [folder](https://drive.google.com/drive/folders/1jaMH-evfMVNSUNBv1dTEjlj8meVvyngm?usp=sharing)
- PM review status: pending
- YouTube 4K processing check: pending YouTube upload
- Professors' publication decision: pending
