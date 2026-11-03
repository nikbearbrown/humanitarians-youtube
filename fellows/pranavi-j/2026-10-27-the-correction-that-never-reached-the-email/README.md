# Weekly Work Report: The Correction That Never Reached The Email

**Fellow:** Sai Pranavi J.
**Week ending:** October 27, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`scripts/regulatory-intel/workflow.dev.json`)
**Source status:** Real engineering work. Every claim traces to this week's C3 fix in
`workflow.dev.json`'s `Generate Email` node (closed 2026-10-27), `Layer 2 - LLM Re-Score`'s real
fields, `High Priority Filter`'s real conditions, and this session's own live Node.js
verification harness (`verification/verify_effective_severity.mjs`) — confirmed the pre-fix
bucketing really does keep a recategorized item under its stale label, and the post-fix bucketing
really does read the LLM's correction.

## Watch

- Landscape (4K 16:9): [pending Drive upload — publishing not authorized this session]
- Vertical (4K 9:16): [pending Drive upload — publishing not authorized this session]

This video covers a bug found and fixed this week (C3) in Project 29's regulatory intelligence
pipeline: `Layer 2 - LLM Re-Score` reviews any item with `urgency_score > 6` and writes back
`llm_reviewed`, `llm_verdict`, `llm_corrected_impact_level`, and `llm_downgrade` so it can correct a
keyword-scorer severity that's wrong — e.g. recategorize a false "Critical" to "High" without
rejecting the item outright. But `Generate Email`, the node that actually buckets and counts items
for the alert email, never read `llm_corrected_impact_level` — only the original `impact_level`. An
item the LLM confirmed but recategorized still passed `High Priority Filter` (which only gates on
the binary `llm_downgrade` flag) and landed back in the email under its stale, pre-LLM label — since
the day the Layer 2 LLM step shipped. The fix: `Generate Email` now computes an effective severity,
`effectiveImpact()`, that prefers the LLM's correction when one exists, falling back to the
original label otherwise.

## What this covers (and what it deliberately leaves out)

Covered: the real fields `Layer 2 - LLM Re-Score` writes, shown verbatim; the real pre-fix two-line
bucketing that never read them; the exact diff that adds `effectiveImpact()`; the real before/after
results from a live Node.js harness built and run this session against a 3-item batch covering
every real case (confirmed-and-recategorized, confirmed-unchanged, never-reviewed); and two honest
items at full weight: what this fix does NOT touch in this same node, and a separate, unrelated
defect found the same week but not fixed.

Deliberately left out: no claim about how many real historical alert emails were actually affected
in production by the stale-label bug — this closes a confirmed defect, verified against a
synthetic batch built to cover every real case this node sees, not a measured incident count.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-27
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both honest limits kept at full weight, no
  softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-10-27
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `EffectiveSeverity_SaiPranaviJ.mp4`, 3840x2160, 24fps,
  h264/aac, **159.79s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `EffectiveSeverity_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **159.79s** (identical duration
  to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the true clean
  master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames
  from both final deliverables — B00's title card, B03's fields/code panels with the
  `impact_level` boxes highlighted, B04's struck-through diff and `effectiveImpact()` addition,
  B05's real harness table with the gold-boxed recategorized row, B06's honest-limits cards, B07's
  takeaway, and B08's sign-off — in both aspects. No text-rendering artifacts, no clipping, no
  overlap; "Sai Pranavi J." and "@HumanitariansAI" confirmed correct everywhere they appear.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`,
effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (finding the
Layer-2-correction-discarded gap, the `effectiveImpact()` fix, and closing it this week as C3) is
my own work on Project 29, done before this video session.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both
aspects), built and ran the live Node.js `vm` verification harness used in B05 (extracting the
real, current `jsCode` from `Generate Email` in `workflow.dev.json` on disk, and a faithful
reconstruction of the pre-fix bucketing by undoing the exact diff to reproduce the real
miscounting), generated the Kokoro `af_bella` narration audio, ran the full render/compile/QC
pipeline, and wrote this paperwork set. Nothing in the pipeline fabricated or altered the
underlying code, numbers, or verification results.

**What I rejected or corrected:** none — the beat sheet and fact-check were already approved
before the build began; the build work focused on authoring the visuals accurately against the
approved claims and fixing real layout/timing defects caught by GATE A/B/V (documented in
`BUILD-LOG.md` and, contemporaneously, in `FRICTIONAL.md`).

**What remains unverified or failed:** this session's harness uses a synthetic 3-item batch
matching the 3 real cases this node sees, not a replay of real historical email-generation runs —
it confirms the mechanism (the bucketing logic itself, extracted verbatim from the real file), not
a measured count of how many past alert emails actually shipped a stale label. A separate defect
(dashboard `get_stats()` re-bucketing) was found the same week and is flagged in B06 as NOT fixed
this week (see `FACTCHECK.md` #8). Both final masters are GATE V clean and personally
frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build,
  2026-10-27
- Source: `mycroft` repo, `scripts/regulatory-intel/workflow.dev.json` (`Generate Email`,
  `Layer 2 - LLM Re-Score`, `High Priority Filter` nodes, read-only — not modified by this video
  session), `scripts/regulatory-intel/C3-VERIFICATION.md`, `logs/RUN_LOG.md`'s 2026-10-27 entry —
  see `SOURCES.md`/`FACTCHECK.md`
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape),
  `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Live verification: `verification/verify_effective_severity.mjs` (run via
  `node verification/verify_effective_severity.mjs`), captured in
  `verification/verify_effective_severity_output.txt`
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS),
  `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC
  gates), `ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav ...` (manual true
  final master, both aspects — `./art final`'s own embedded GATE V has no `--lenient` escape
  hatch and refuses on any MAJOR finding), `./art vertical <reel>` + `./art run <reel>/vertical`
  (vertical review + QC gates), `final_frame_check.py --lenient` (standalone GATE V re-check on
  both true finals, run from inside the reel folder)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md`
  (build history, bugs found/fixed, GATE V results), `FRICTIONAL.md` (contemporaneous build-time
  log)

## Watch and review

- Landscape — `deliverables/landscape/EffectiveSeverity_SaiPranaviJ.mp4` — 3840x2160 — 159.79s —
  SHA-256 `13c3a30644d9c5a1d5b1a5fa7ab5055eef320050b9934fb83bb2b612960abfc0` (sidecar
  `.verified.json`)
- Vertical — `deliverables/vertical/EffectiveSeverity_SaiPranaviJ.mp4` — 2160x3840 — 159.79s —
  SHA-256 `f11c036c7caa06a3255403277b4ec45037dbd3545ce849da0c9dc6668e024c32` (sidecar
  `.verified.json`)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review against the real nodes, the real diff, and this session's
  own verification harness
- `SOURCES.md` — claim -> source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and
  pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `verification/verify_effective_severity.mjs` / `verification/verify_effective_severity_output.txt`
  — the live Node.js harness and its captured real output
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous, dated build-time friction log
