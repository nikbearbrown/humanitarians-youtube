# CabStream — Week 3 Progress — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template. Third in the CabStream
series, after `kavya-cabstream-week1-progress` and
`kavya-cabstream-week2-progress`.

## This week's contribution

**Question:** week 2 defined the cloud infrastructure in code but never ran
it — did week 3 actually run the pipeline, and did it hold up at real
scale?

**Prediction:** probably at least one real bug on first run, given the
infra had never actually been exercised.

**What I built/tried:** stood up a Databricks cluster with a Key Vault
secret scope, fixed two real infrastructure bugs the same night (a
provider bootstrapping error, then a missing `prevent_destroy` on
storage), then ran Bronze ingestion (NYC taxi data, 2019–2026, resume-safe)
and Silver processing.

**Observed result:** my own commit message describes the result as 1.57
billion rows ingested into Bronze and 252.3 million rows processed into
Silver. The honest caveat: that total is what the commit message says —
this reel did not re-run the Databricks notebook to independently confirm
it. What I can confirm directly from the committed script: it tests one
known-good month (January 2023, verified against a local count of
3,066,766 rows) before ever scaling up.

**Next experiment:** independently re-run the Bronze ingestion and confirm
the 1.57B figure directly, rather than taking the commit message's word
for it — a natural week-4 topic.

## Human and AI work

**My decisions, implementation and verification:** I directed the topic,
reviewed the generated beat sheet and narration script, and visually
checked the rendered frames before accepting the build as done.

**AI tools/voices used and what they generated:** Claude (this session)
wrote the beat sheet and narration script, read directly from the
CabStream repo's own git log and the committed ingestion script; Kokoro
`am_onyx` (free, local TTS) generated the narration audio; Remotion
rendered every visual from authored props.

**What I rejected or corrected:** nothing — built clean, submission-
compliant and at the correct resolution, on the first pass.

**What remains unverified or failed:** the 1.57B/252.3M row counts remain
unverified by this reel — see B04/FACTCHECK.md. This is stated honestly on
screen, not glossed over.

## Reproduce

**Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7`, 2026-10-10 (repo HEAD at build time, checked 2026-10-29).

**Source commit used for this export:** same as above.

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files.

**Commands/dependencies:**
```
python3 runtime/scripts/generate_audio_kokoro.py youtube/kavya-cabstream-week3-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-cabstream-week3-progress
python3 runtime/scripts/compile.py youtube/kavya-cabstream-week3-progress --review --no-timecode --force --height 2160
./art vertical youtube/kavya-cabstream-week3-progress
python3 runtime/scripts/remotion_scenes.py youtube/kavya-cabstream-week3-progress/vertical
python3 runtime/scripts/compile.py youtube/kavya-cabstream-week3-progress/vertical --review --no-timecode --force --height 3840
```
**Note the explicit `--height 2160` / `--height 3840`** — `compile.py`
defaults to 720p; see BUILD-LOG.md for the bug this avoids. Requires
ffmpeg and Node/npx on `PATH`.

**Approvals and checks:** no human sign-off records exist yet. GATE T
report: [TYPECHECK.md](TYPECHECK.md) — PASS, 8/8. GATE V: spot-checked
manually — see CHECKS-REPORT.md.

## Watch and review

- Landscape review cut — **3840×2160 (verified via `ffprobe`)** — 2:22.71 — SHA-256 `fee98985d43e1b3ab251e89e793ebf3948d4ea97fc105a0137a54f62eafa6bca` — **not yet uploaded to Drive** (local at `kavya-cabstream-week3-progress-slate.mp4`)
- Vertical review cut — **2160×3840 (verified via `ffprobe`)** — 2:22.71 — SHA-256 `9e2d3d494ae6fe994dbfbb004abec9a16e89c14d99e3a8bfdb3162a0c77f5de9` — **not yet uploaded to Drive** (local at `vertical/kavya-cabstream-week3-progress-vertical-slate.mp4`)
- These are `--review` cuts, not gated `./art final` exports — no `.verified.json` receipt, final-frame/fact-check gates have not run.
- Sources/large assets Drive link: n/a
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending — not applicable (personal project, not a Humanitarians AI fellow submission)
