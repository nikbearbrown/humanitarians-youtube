# CabStream — Week 1 Progress — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template.

## This week's contribution

**Question:** did a real streaming lakehouse actually get built in CabStream's
first week, or does the commit log just make it look that way?

**Prediction:** probably the pipeline shape, not the verified scale.

**What I built/tried:** Kafka producer (day 1) → Delta bronze ingestion,
verified (day 3) → silver parse/validate/dedupe (day 4) → weather join +
dbt Gold layer (day 7) — the full medallion architecture, scaffolded end
to end in six days.

**Observed result:** every stage in the git log confirms itself — producer
first, then bronze, then silver, then weather, then gold, in that order.
The honest caveat: week 1 had no verified scale numbers. The 1.57B-row
count, the 99.9% pass rate, and the Text-to-SQL agent all came in a later
phase (commit `ac80e80` "Phase 2 verified metrics" onward) — this reel
does not backdate them.

**Next experiment:** a week-2-style recap of the Phase 2 scale-verification
work, the same way the Brutalist toolkit reels track their own weekly
progress.

## Human and AI work

**My decisions, implementation and verification:** I directed the topic,
reviewed the generated beat sheet and narration script, and visually
checked the rendered frames before accepting the build as done.

**AI tools/voices used and what they generated:** Claude (this session)
wrote the beat sheet, narration script, and all Remotion scene props; Kokoro
`am_onyx` (free, local TTS) generated the narration audio; Remotion rendered
every visual from authored props — no stock footage, no generative
image/video models.

**What I rejected or corrected:** this reel's original B00 narration
(built earlier in this session) did not include the required submission
intro line or an AI-narration disclosure — both were added this round, and
B00's audio/video were re-rendered to match.

**What remains unverified or failed:** see "Known gaps before submission" below. GATE T initially
flagged B02 for a false-positive "8px text run" (the same component issue
seen in the three Brutalist week reels); this was fixed at the root this
round rather than documented as another instance — see BUILD-LOG.md.

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

**Source commit used for this export:** same as above, plus two toolkit
fixes landed this round — `type_check.py` (GATE T false-positive fix) and
`build_safety.py`/five other scripts (UTF-8 encoding fix) — not yet
committed to the Brutalist repo.

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files.

**Commands/dependencies:** standard Brutalist pipeline (`generate_audio_kokoro.py`
→ `remotion_scenes.py` → `compile.py` → `./art vertical` → repeat for
portrait). Requires ffmpeg and Node/npx on `PATH`.

**Approvals and checks:** no human sign-off records exist yet. GATE T
report: [TYPECHECK.md](TYPECHECK.md) — PASS, 8/8. GATE V: spot-checked
manually — see CHECKS-REPORT.md.

## Watch and review

**Status: both renders are now true native 4K review cuts (re-compiled 2026-10-29 with explicit `--height 2160`/`--height 3840` after a resolution bug was found — see BUILD-LOG.md).** They are not gated `./art final` exports — no `.verified.json` receipt, final-frame/fact-check gates have not run.

- Landscape review cut — 3840×2160 (verified via `ffprobe`) — 2:10.62 — SHA-256 `f7c30f537609b5ebb2f5c7bfe5265f3ff795001f32e30a0eff8361770c9da1b2` (local: `kavya-cabstream-week1-progress-slate.mp4`)
- Vertical review cut — 2160×3840 (verified via `ffprobe`) — 2:10.62 — SHA-256 `b362853f70181cc0a75189835194c48086c9c2d550e01ee54421708f6638e5e1` (local: `vertical/kavya-cabstream-week1-progress-vertical-slate.mp4`)
- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
