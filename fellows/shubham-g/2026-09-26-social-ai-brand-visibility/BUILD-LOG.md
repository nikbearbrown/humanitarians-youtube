# BUILD-LOG — social-ai-brand-visibility

## 2026-09-26 — first build (Windows 11, Git Bash, native toolchain)

Decisions
- Channel: HAI look (claude skin) with the author's chip **@Shubh & @HumanitariansAI** on every
  Claude page (B00, B06, B09, B10) and the outro. Voice: Kokoro `af_bella` (author's choice),
  Plain register. The narrator introduces themself as Shubh in B01 per the brief.
- Outro: `HandleTitleOutro` (new). `ClaudeTitleOutro` is locked to @NikBearBrown by
  OUTRO-LOCK.md and is for claude-liam reels only.
- GATE L library search: generic structural scenes exist (ChipGrid, SourceFlow) but none
  performs fan-out / cadence / trend-window / audience-branch / loop / split for this
  argument with a native 9:16 twin, and `OnSchedule*` scenes carry another reel's baked-in
  content. Built `runtime/remotion/src/scenes/SocialAiVisibility.tsx` (6 C3 scenes + outro),
  each registered as `<Name>` and `<Name>916`.
- ASK→RESULT: one mid-reel pair (B06→B07) instead of a composer before every generated visual;
  see CHECKS-REPORT.md.
- No statistics (author instruction). Illustrative visuals are captioned as such.
- Reference-video link omitted at the author's request.

Toolkit changes made for this build (portable fixes, not reel hacks)
- `runtime/scripts/compile.py` — escape the drawtext font path (Windows `C:\…` broke ffmpeg).
- `runtime/remotion/src/tokens/ebGaramond.ts` + `public/fonts/EBGaramond-*` — load the bundled
  house serif inside the bundle (headless Chrome on Windows ignored the installed font → Georgia).
- `Root.tsx` — `calculateMetadata` on `ClaudeComposerAsk916`, `ClaudeVerdictArtifact916`,
  `BrutalistHesitantWriter916` so portrait renders follow the beat's audio length
  (fallback = the previous fixed length, so other reels are unchanged).

- `runtime/scripts/remotion_scenes.py` — resolve `npx` via `shutil.which` (Windows `npx.cmd`).
- `runtime/scripts/compile.py` — review-label size from the frame's short side (9:16 labels
  spanned ~85% of the width, outside GATE V's burn-in mask).
- `runtime/qc/brand_labels.json` — registered channel `claude-shubh` (chip
  `@Shubh & @HumanitariansAI`, no fixed kicker: per-video topics).
- `ClaudeVerdictArtifact916.tsx` — renders `brandLabel` (the 16:9 twin already did) and an
  optional `largeText`; defaults unchanged for other reels.
- `SocialAiVisibility916.tsx` — native portrait layouts for the six C3 scenes + outro, type sized
  for GATE T's portrait floor (serif ≥ 90, sans ≥ 76 CSS px); portrait-only shorter labels live
  in `vertical/beat_sheet.json` props (same meaning, fewer words).
- Accent discipline: terracotta on shapes only (spark, markers, loop dot, verdict rule) — accent
  text failed WCAG 4.5:1 on cream and was moved to ink.

Gate results (final exports)
- 16:9 `renders/social-ai-brand-visibility.mp4` — 3840×2160, 178.5 s; GATE L/F/V/T pass; receipt
  `social-ai-brand-visibility.verified.json`.
- 9:16 `renders/social-ai-brand-visibility-vertical.mp4` — 2160×3840, 178.5 s; GATE L/F/V/T pass;
  receipt `social-ai-brand-visibility-vertical.verified.json`.
- Review cuts ran with `ART_NO_DRAWTEXT=1` (no running-timecode burn-in, which sits outside the
  title-safe area and fails GATE V on every frame when ffmpeg has drawtext).

Environment notes
- `PYTHONUTF8=1` is required on Windows (Python otherwise reads beat sheets as cp1252).
