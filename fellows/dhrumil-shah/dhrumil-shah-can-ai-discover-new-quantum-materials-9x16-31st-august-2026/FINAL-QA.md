# FINAL QA — rendered portrait master verification

Master: `output/Can-AI-discover-new-quantum-materials-4k(9x16)_Dhrumil_Shah.mp4`
Verified: 2026-09-01, against the rendered file — not against the plan.

## Technical contract

| Property | Required | Measured | Status |
|---|---|---|---|
| Resolution | 2160 × 3840 | 2160 × 3840 | PASS |
| Orientation | portrait 9:16 | portrait 9:16 | PASS |
| Frame rate | 24 fps | 24/1 | PASS |
| Video codec | H.264 | h264 | PASS |
| Audio codec | present | aac | PASS |
| Duration | 180.000 s ± 0.5 | **180.011 s** | PASS |
| File size | — | 21.95 MiB | — |

Verified by `scripts/check-video.ps1`, which fails the build on wrong
resolution, landscape orientation, missing audio, or a duration more than
0.5 s from the 03:00 contract.

The duration matches the 16:9 master to the millisecond (180.011 s in both),
which is the expected result of both cuts being driven by the same measured
audio.

## Audio integrity

| Check | Result | Reading |
|---|---|---|
| Sample count | 17,281,024 | Exactly 180 s of 48 kHz stereo — **identical to the 16:9 master**, confirming the reuse worked and no re-encode drifted |
| Mean volume | −26.9 dB | Identical to the 16:9 master |
| Max volume | −4.3 dB | Identical; adequate headroom, no clipping |
| Silence gaps > 1.5 s | **none detected** | No dropped or missing narration beat anywhere in the timeline |

Three figures matching the landscape master exactly is the evidence that the
narration was genuinely reused rather than regenerated or re-encoded.

## Visual review

Eleven stills inspected from the encoded master in `_qc/final/`:

| Still | Time | Scene | Result |
|---|---:|---|---|
| `01-executive-summary` | 00:09 | 01 | Title, answer card, and the **vertical** five-token pipeline with down-arrows all legible |
| `02-framework` | 00:32 | 02 | Tc chart clean at 860 px; high-pressure callout readable; `YBCO 92K` clear of the BSCCO point; CLAIM 3+2 grid complete |
| `03-data` | 00:55 | 03 | Full bibliographic citation legible; 2×2 stats; features and exclusions stacked. Source plate wraps to two lines as designed |
| `04-method` | 01:13 | 04 | ±9.5 K at 200 px with model, task, and status cards stacked beneath |
| `05-funnel` | 01:31 | 05 | Five proportional bars collapsing; labels in their own column, no overflow; disclosure adjacent |
| `06-limit` | 01:46 | 06 | Inside/outside cards and both dated discoveries stacked and legible |
| `07-chain` | 02:07 | 07 | Five-link vertical chain flows continuously into the boundary labels and rule card |
| `08-lk99-stacked` | 02:30 | 08 | **Both comparison panels on screen together, fully readable** |
| `09-scoring` | 02:43 | 09 | Five scored rows at portrait scale; all verdict chips legible and distinguishable |
| `10-scaffold` | 02:52 | 10 | Five scaffold rows plus decision rule readable |
| `11-close` | 02:59.5 | 10 | Outro at full opacity; title, subline, disclaimer, and credit all legible |

No clipped headline, no overlapping text, no card overflow, no obscured source
plate, and no element outside the 120 / 170 px safe area in any inspected
frame.

## Defects found and fixed before this master

| # | Beat | Defect | Caught by | Fix |
|---|---|---|---|---|
| 1 | B01 | Portrait narrows the plot, pushing the centred `YBCO 92K` label underneath the unlabelled BSCCO point at 110 K | preflight still | Per-point label anchoring added to `TC_DATA`; YBCO left-anchored |
| 2 | B01/B02 | Scene 02 chart squashed into the top third with dead column beneath the CLAIM grid | preflight still | Chart height 700 → 860 px; framework block moved down |
| 3 | all scenes | **Systemic.** Fixed tops carried over from landscape left content in roughly the top 40 % of the 3840 px column. Scene 09 was worst: rubric card ending at y≈1520, footer stranded at y≈2580 | **QC stills of a completed master** | `ContentColumn` primitive centring each scene's content between headline and source plate; Scene 09 rows scaled up |

**Defect 3 is the one worth recording.** A complete portrait master had already
rendered and passed every check in the technical contract above — correct
resolution, correct orientation, correct duration, correct audio. The probe had
nothing to say about it. Only the QC stills showed that the bottom 60 % of
every frame was empty. That master was discarded and the cut re-rendered.

This is the clearest case in either cut for the workspace rule that renders are
verified by looking at frames, not by probe output.

## Inherited defects that did not recur

The two defects fixed in the 16:9 cut — colliding high-pressure chart labels,
and funnel bars narrower than their own labels — do not reappear here, because
both fixes were structural rather than positional. High-pressure values live in
a callout; the funnel label sits in its own column. A fix that survives a
layout change was a real fix.

## Timeline integrity

- 16 narration beats, 16 unique beat IDs, 0 duplicates.
- Measured audio total 179.44 s; master 180.011 s; the difference is a
  deliberate 0.58 s silent title hold.
- The composition's `AUDIO_BEATS` table matches the 16:9 cut's
  `mp3/timings.json` exactly. No timing value was set by hand in either cut.

## Non-blocking

The Remotion CLI prints a version-mismatch banner (`@remotion/paths` 4.0.490
against 4.0.486 elsewhere) on every invocation. It does not affect this
composition and did not affect this render. Recorded in `INTEGRATION.md`.

## Result

**No blocking visual or technical defect in the rendered portrait master.**

The production gate passes on all three rows, including the simultaneous-
comparison row that the rotation to portrait put at risk. The ship verdict is
nevertheless `unlisted-until-fixed` on a **content** item shared with the 16:9
cut: the ±9.5 K figure in Scene 04 has not been verified against its source.
Verifying it once clears both masters. See `PROOF-COMPLIANCE.md` and
`FACTCHECK.md`.
