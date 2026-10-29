# Brutalist Progress — Week 2 — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template. Direct sequel to
`kavya-brutalist-week1-progress`.

## This week's contribution

**Question:** did last week's six pipeline-bug fixes actually hold, or did
building a new reel on top of them just surface the bugs somewhere else?

**Prediction:** probably mostly held, but something in the newly-touched
code would likely crack.

**What I built/tried:** reused the fixed pipeline to build a second reel
("Semantic Layers Become AI Context", 8 beats, landscape + portrait), then
this reel recapping that work.

**Observed result:** none of the six week-1 bugs came back. One new bug did
surface — a layout overlap in `SkillTeardownPipeline916`, caused by week
1's own GATE T font-size fix making two text lines taller than the box had
room for. The first fix attempted (shortening the footer text) was a false
lead — the real fix was the layout math itself (`colBottom` and footer-top
constants), verified by extracting a real frame from the compiled video
rather than trusting the QC contact-sheet thumbnail.

**Next experiment:** week 3 — see if the layout-math fix holds under a third
week of changes, same as week 1's fix was tested this week.

## Human and AI work

**My decisions, implementation and verification:** I directed the topic,
reviewed the generated beat sheet and narration script, and visually
checked the rendered frames (direct ffmpeg frame extraction) before
accepting the build as done — including specifically re-checking the beat
that GATE T flagged.

**AI tools/voices used and what they generated:** Claude (this session)
wrote the beat sheet, narration script, and all Remotion scene props; Kokoro
`am_onyx` (free, local TTS) generated the narration audio; Remotion rendered
every visual from authored props — no stock footage, no generative
image/video models.

**What I rejected or corrected:** same as week 1 — the underlying content
originally carried `@NikBearBrown`/claude-liam branding (from
`claude-liam-brutalist-week2-progress`) and was rebuilt under my own name
for this submission, per BUILD-LOG.md.

**What remains unverified or failed:** GATE T flagged B02 (`ClaudeScienceLayerStack`)
for an "8px text run" — the same false-positive class already documented in
week 1, visually inspected and not treated as a real defect; not fixed at
the component level. See FACTCHECK.md and BUILD-LOG.md.

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
changes were required for this reel specifically (the one toolkit fix from
week 1, in `runtime/scripts/shorts.py`, carried forward and was reused, not
repeated).

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files — every beat uses existing library components with their `916` portrait variants.

**Commands/dependencies:**
```
python3 runtime/scripts/generate_audio_kokoro.py youtube/kavya-brutalist-week2-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-brutalist-week2-progress
python3 runtime/scripts/compile.py youtube/kavya-brutalist-week2-progress --review --no-timecode --force --height 2160
./art vertical youtube/kavya-brutalist-week2-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-brutalist-week2-progress/vertical
python3 runtime/scripts/compile.py youtube/kavya-brutalist-week2-progress/vertical --review --no-timecode --force --height 3840
```
**Note the explicit `--height 2160` / `--height 3840`** — `compile.py`
defaults to 720p, which is what was used on first build. Requires ffmpeg
and Node/npx on `PATH`.

**Approvals and checks:** no human sign-off records exist yet — not gone
through fellow/PM review. GATE T report: [TYPECHECK.md](TYPECHECK.md)
(7/8 PASS, 1 FAIL assessed as false positive, 1 advisory). GATE V:
spot-checked manually — see CHECKS-REPORT.md.

## Watch and review

**Status: both renders are now true native 4K review cuts (re-compiled 2026-10-29 with explicit `--height 2160`/`--height 3840` after a resolution bug was found — see BUILD-LOG.md).** They are not gated `./art final` exports — no `.verified.json` receipt, final-frame/fact-check gates have not run.

- Landscape review cut — 3840×2160 (verified via `ffprobe`) — 1:56.08 — SHA-256 `ced80a08dd9994c952961ee9262c1916996ed53505a34d90e12df39b0401f9be` (local: `kavya-brutalist-week2-progress-slate.mp4`)
- Vertical review cut — 2160×3840 (verified via `ffprobe`) — 1:56.08 — SHA-256 `c967b216d29fa703288059b825677a1d1f74d5e49502231edf7f45303cdb3465` (local: `vertical/kavya-brutalist-week2-progress-vertical-slate.mp4`)
- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
