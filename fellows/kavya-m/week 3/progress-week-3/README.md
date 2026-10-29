# Brutalist Progress — Week 3 — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template. Third in the sequel series
after `kavya-brutalist-week1-progress` and `kavya-brutalist-week2-progress`.

## This week's contribution

**Question:** six bugs in week 1, one bug in week 2 — is the pipeline
actually trending toward stable, or will week 3 just find a different bug?

**Prediction:** probably at least one more bug, somewhere in a component
not yet exercised.

**What I built/tried:** reused the pipeline to build a third reel
("OpenTelemetry for AI Agents", 8 beats, landscape + portrait), using only
components already proven by the first two reels, then this reel recapping
the three-week trend.

**Observed result:** zero new bugs — the first fully clean build in the
series. But the honest caveat matters: this build reused only
already-exercised components, so a zero here proves the known paths are
solid, not that the pipeline is bug-free for a genuinely new component
shape.

**Next experiment:** a reel that deliberately exercises a new component
shape, to actually test the claim this week's zero doesn't prove.

## Human and AI work

**My decisions, implementation and verification:** I directed the topic,
reviewed the generated beat sheet and narration script, and visually
checked the rendered frames (direct ffmpeg frame extraction) before
accepting the build as done.

**AI tools/voices used and what they generated:** Claude (this session)
wrote the beat sheet, narration script, and all Remotion scene props; Kokoro
`am_onyx` (free, local TTS) generated the narration audio; Remotion rendered
every visual from authored props — no stock footage, no generative
image/video models.

**What I rejected or corrected:** same as weeks 1–2 — the underlying
content originally carried `@NikBearBrown`/claude-liam branding and was
rebuilt under my own name for this submission.

**What remains unverified or failed:** GATE T flagged B02
(`ClaudeScienceLayerStack`) for an "8px text run" — the third consecutive
occurrence of this exact finding across the series (weeks 1, 2, and 3, same
component). Assessed as a checker false positive each time, but logged in
BUILD-LOG.md as something that deserves a real fix rather than being
re-documented a fourth time.

**Known gaps before submission (checked 2026-10-29):**
- No native 4K final export exists yet (see Watch and review).
- `ClaudeScienceLayerStack` is a 1280×720 composition that renders at 2560×1440 and would be upscaled.
  `ShellSession` draws a small fixed-size terminal that fails the final frame gate at 4K. Both need
  swapping (e.g. for `HarnessParts` / `HarnessTerminal`) before `./art final` will pass.
- `FACTCHECK.md` has no claims table, so the fact-check gate (`runtime/qc/factcheck_check.py`) blocks
  final export (FC-1).
- The narration says the script was one "I wrote", but the beat sheet and narration were drafted by
  Claude (see above). Correcting that wording means regenerating B00/last-beat audio.

## Reproduce

**Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7`, 2026-10-10 (repo HEAD at build time, checked 2026-10-28). Note: GitHub `origin/main` has since moved to `a99b5323` (2026-10-23); this build used the older local checkout.

**Source commit used for this export:** same as above — no toolkit code
changes were made in this build.

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files.

**Commands/dependencies:**
```
python3 runtime/scripts/generate_audio_kokoro.py youtube/kavya-brutalist-week3-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-brutalist-week3-progress
python3 runtime/scripts/compile.py youtube/kavya-brutalist-week3-progress --review --no-timecode --force --height 2160
./art vertical youtube/kavya-brutalist-week3-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-brutalist-week3-progress/vertical
python3 runtime/scripts/compile.py youtube/kavya-brutalist-week3-progress/vertical --review --no-timecode --force --height 3840
```
Requires ffmpeg and Node/npx on `PATH`.

**Approvals and checks:** no human sign-off records exist yet. GATE T
report: [TYPECHECK.md](TYPECHECK.md) (7/8 PASS, 1 FAIL assessed as false
positive, 1 advisory). GATE V: spot-checked manually — see
CHECKS-REPORT.md.

## Watch and review

**Status: both renders are now true native 4K review cuts (re-compiled 2026-10-29 with explicit `--height 2160`/`--height 3840` after a resolution bug was found — see BUILD-LOG.md).** They are not gated `./art final` exports — no `.verified.json` receipt, final-frame/fact-check gates have not run.

- Landscape review cut — 3840×2160 (verified via `ffprobe`) — 1:58.54 — SHA-256 `0f89c21fac957e5fec813228c6badbadf03c4e22f4695b0239045882ecd71ae9` (local: `kavya-brutalist-week3-progress-slate.mp4`)
- Vertical review cut — 2160×3840 (verified via `ffprobe`) — 1:58.54 — SHA-256 `20bb44b43d6c78f760dc212d64c2fcee94a205bd8fbb1f504bb7c0aa5a8b61e6` (local: `vertical/kavya-brutalist-week3-progress-vertical-slate.mp4`)
- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
