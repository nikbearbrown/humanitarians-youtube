# Brutalist Progress — Week 1 — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template.

## This week's contribution

**Question:** does the Brutalist toolkit actually work end to end on this
machine, out of the box?

**Prediction:** probably not without some setup friction.

**What I built/tried:** set up the toolkit (Kokoro voice model, ffmpeg, Node
dependencies — none pre-installed), authored and built the first reel
(`claude-liam-schema-scout`, 10 beats, landscape + portrait), then this
reel recapping that work under my own name.

**Observed result:** six real pipeline bugs surfaced and were fixed at the
root (not worked around) — two Windows-specific crashes (file encoding,
`npx` resolution), one missing dependency install, an ffmpeg filtergraph
parser bug on Windows drive-letter paths, a visual-QC false positive, and a
chart fed the wrong kind of number. Two more environment bugs surfaced
while building *this* reel specifically — see BUILD-LOG.md. One reel shipped
clean, two formats, zero blocking defects.

**Next experiment:** week 2 — a real second week of further use/changes to
this toolkit, not another setup pass.

## Human and AI work

**My decisions, implementation and verification:** I directed every topic,
reviewed the generated beat sheets and narration scripts, and visually
checked the rendered frames (via direct ffmpeg frame extraction) before
accepting the build as done.

**AI tools/voices used and what they generated:** Claude (this session)
wrote the beat sheet, narration script, and all Remotion scene props; Kokoro
`am_onyx` (free, local TTS) generated the spoken narration audio; Remotion
rendered every visual from authored props — no stock footage, no
generative image/video models, no AI-generated stills.

**What I rejected or corrected:** an earlier draft of the underlying content
(from the claude-liam-branded version of this reel) used `@NikBearBrown`
branding and a "Liam, in for Bear" framing throughout — rejected for this
submission and rebuilt under my own name with no toolkit-persona branding,
per BUILD-LOG.md.

**What remains unverified or failed:** GATE T flagged one advisory finding
on B03 (an "8px text run"); visually inspected and assessed as a false
positive on a structural element, not corrected at the component level —
see FACTCHECK.md and BUILD-LOG.md for the full reasoning.

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
changes were required for the reel content itself; one toolkit bug fix
landed in `runtime/scripts/shorts.py` during this build (see BUILD-LOG.md),
not yet committed.

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files — every beat uses existing library components (`ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownPipeline`, `ClaudeScienceLayerStack`, `ShellSession`, `ClaudeVerdictArtifact`, all with their `916` portrait variants).

**Commands/dependencies:**
```
python3 runtime/scripts/generate_audio_kokoro.py youtube/kavya-brutalist-week1-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-brutalist-week1-progress
python3 runtime/scripts/compile.py youtube/kavya-brutalist-week1-progress --review --no-timecode --force --height 2160
./art vertical youtube/kavya-brutalist-week1-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-brutalist-week1-progress/vertical
python3 runtime/scripts/compile.py youtube/kavya-brutalist-week1-progress/vertical --review --no-timecode --force --height 3840
```
**Note the explicit `--height 2160` / `--height 3840`** — `compile.py`
defaults to 720p, which is what was used on first build. Requires ffmpeg
and Node/npx on `PATH` (see BUILD-LOG.md for two environment-specific
workarounds needed on this machine).

**Approvals and checks:** no human sign-off records exist yet for this
reel — it has not gone through fellow/PM review. GATE T report:
[TYPECHECK.md](TYPECHECK.md) (8/9 PASS, 1 advisory). GATE V: spot-checked
manually, not run as the full automated frame-sampling pass — see
CHECKS-REPORT.md.

## Watch and review

**Status: both renders are now true native 4K review cuts (re-compiled 2026-10-29 with explicit `--height 2160`/`--height 3840` after a resolution bug was found — see BUILD-LOG.md).** They are not gated `./art final` exports — no `.verified.json` receipt, final-frame/fact-check gates have not run.

- Landscape review cut — 3840×2160 (verified via `ffprobe`) — 2:16.96 — SHA-256 `08ff8231f1dd48215108d7c6d83e0bada39111a615fefe7eb210b808ef91f8da` (local: `kavya-brutalist-week1-progress-slate.mp4`)
- Vertical review cut — 2160×3840 (verified via `ffprobe`) — 2:16.96 — SHA-256 `a4835a2d945c030f1148c581336be2136c299a80f101cf308f5f615d9b645d27` (local: `vertical/kavya-brutalist-week1-progress-vertical-slate.mp4`)
- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
