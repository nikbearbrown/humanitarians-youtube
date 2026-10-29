# CabStream — Week 2 Progress — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template. Direct sequel to
`kavya-cabstream-week1-progress`.

## This week's contribution

**Question:** week 1 was a local Kafka pipeline in Docker — what does it
take to move that to real cloud infrastructure, and is clicking through
the Azure portal the right way to do it?

**Prediction:** Terraform, not portal clicks — reproducibility matters more
than speed for a 1-person project I'll have to rebuild or explain later.

**What I built/tried:** six Terraform resources across two files/commits —
Event Hubs (managed Kafka, replacing the local Docker setup), a Databricks
workspace (managed Spark), Storage, and Key Vault for secrets — all
defined in a two-day window.

**Observed result:** every resource is defined and reviewable in code. The
honest caveat: this git log has no evidence `terraform apply` actually ran,
and the pipeline itself hasn't been repointed at Event Hubs yet — it's
still reading from local Docker Kafka. One real gap was found and closed
the next day: Key Vault shipped without a personal read-access policy,
fixed in a follow-up commit.

**Next experiment:** actually run `terraform apply`, confirm the resources
exist in Azure, and repoint the week-1 producer at Event Hubs instead of
local Kafka.

## Human and AI work

**My decisions, implementation and verification:** I directed the topic,
reviewed the generated beat sheet and narration script, and visually
checked the rendered frames before accepting the build as done.

**AI tools/voices used and what they generated:** Claude (this session)
wrote the beat sheet, narration script, and all Remotion scene props — read
directly from the CabStream repo's own git log and Terraform file
comments; Kokoro `am_onyx` (free, local TTS) generated the narration audio;
Remotion rendered every visual from authored props.

**What I rejected or corrected:** nothing — built clean on first pass,
including the required intro line and disclosure from the start.

**What remains unverified or failed:** whether the Terraform plan was ever
actually applied, and whether the Azure resources are live — this reel is
explicit that it cannot confirm either from the commit history alone (see
B04/FACTCHECK.md).

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

**Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7`, 2026-10-10 (repo HEAD at build time, checked 2026-10-29). Note: GitHub `origin/main` has since moved to `a99b5323` (2026-10-23); this build used the older local checkout.

**Source commit used for this export:** same as above.

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files.

**Commands/dependencies:** standard Brutalist pipeline (`generate_audio_kokoro.py`
→ `remotion_scenes.py` → `compile.py` → `./art vertical` → repeat for
portrait). Requires ffmpeg and Node/npx on `PATH`.

**Approvals and checks:** no human sign-off records exist yet. GATE T
report: [TYPECHECK.md](TYPECHECK.md) — PASS, 8/8. GATE V: spot-checked
manually — see CHECKS-REPORT.md.

## Watch and review

**Status: both renders are now true native 4K review cuts (re-compiled 2026-10-29 with explicit `--height 2160`/`--height 3840` after this resolution bug was first caught here — see BUILD-LOG.md).** They are not gated `./art final` exports — no `.verified.json` receipt, final-frame/fact-check gates have not run.

- Landscape review cut — 3840×2160 (verified via `ffprobe`) — 2:17.96 — SHA-256 `f751b3cf8f60ff935b0e01ec8ebf4215e1b5ff39f99c2eb4d20c0c6ecaa59abe` (local: `kavya-cabstream-week2-progress-slate.mp4`)
- Vertical review cut — 2160×3840 (verified via `ffprobe`) — 2:17.96 — SHA-256 `4e32329c3f4386d1f504d7b3fa96eff0bfb5d05b543f12018354065dc0f2efaf` (local: `vertical/kavya-cabstream-week2-progress-vertical-slate.mp4`)
- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
