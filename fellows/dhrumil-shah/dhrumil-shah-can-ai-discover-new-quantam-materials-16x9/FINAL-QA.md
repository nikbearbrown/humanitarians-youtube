# FINAL QA — rendered master verification

Master: `output/can-ai-discover-new-quantum-materials-4k.mp4`
Verified: 2026-09-01, against the rendered file — not against the plan.

## Technical contract

| Property | Required | Measured | Status |
|---|---|---|---|
| Resolution | 3840 × 2160 | 3840 × 2160 | PASS |
| Aspect ratio | 16:9 | 16:9 | PASS |
| Frame rate | 24 fps | 24/1 | PASS |
| Video codec | H.264 | h264 | PASS |
| Audio codec | present | aac | PASS |
| Duration | 180.000 s ± 0.5 | **180.011 s** | PASS |
| File size | — | 23.96 MiB | — |

Verified by `scripts/check-video.ps1`, which fails the build on resolution,
missing audio, or a duration more than 0.5 s from the 03:00 contract.

## Audio integrity

| Check | Result | Reading |
|---|---|---|
| Sample count | 17,281,024 | Exactly 180 s of 48 kHz stereo — the track spans the full master with no truncation |
| Mean volume | −26.9 dB | Normal speech level |
| Max volume | −4.3 dB | Adequate headroom; no clipping |
| Silence gaps > 1.5 s | **none detected** | No dropped or missing narration beat anywhere in the timeline |

The silence scan matters more than the probe: an MP4 can carry an AAC stream
that is silent, or that stops early, and still pass a format check. It does not
here.

## Visual review

Twelve stills inspected from the encoded master in `_qc/final/`:

| Still | Time | Scene | Result |
|---|---:|---|---|
| `01-executive-summary` | 00:09 | 01 | Title, thesis card, five-token pipeline all legible; source plate readable |
| `02-framework` | 00:32 | 02 | Tc chart clean, high-pressure callout readable, five CLAIM cards fully revealed |
| `03-data` | 00:55 | 03 | Full bibliographic citation legible; NOT-IN-THE-TABLE column distinct |
| `04-method` | 01:13 | 04 | RMSE stat, model, task, status, and reframe card all clear |
| `05-funnel` | 01:31 | 05 | Proportional bars with labels in a fixed column — no overflow; disclosure banner readable |
| `06-limit` | 01:46 | 06 | Two-column contrast plus both dated discoveries legible |
| `07-chain` | 02:07 | 07 | Five-link chain with the AI boundary divider readable end to end |
| `08-lk99-sidebyside` | 02:30 | 08 | **Both columns on screen together, fully readable** |
| `09-scoring` | 02:43 | 09 | Five scored rows; all verdict chips legible and distinguishable |
| `10-scaffold` | 02:52 | 10 | Five scaffold rows plus decision rule readable |
| `11-close` | 02:58 | 10 | Mid-crossfade — outro at partial opacity, as designed |
| `12-close-final` | 02:59.5 | 10 | Outro at full opacity; title, subline, disclaimer and credit all legible |

No clipped headline, no overlapping text, no card overflow, no obscured source
tag, and no element outside the 230 / 150 px safe area in any inspected frame.

## Defects found and fixed before this master

Both were caught by rendering stills and looking at them, not by probe output.

| # | Beat | Defect | Fix | Re-verified |
|---|---|---|---|---|
| 1 | B01 | Tc chart: the `LaH10` and `H3S` point labels collided with the 293 K room-temperature line and with each other; one ran to the plot edge | Point labels removed for the two high-pressure records; values moved to an accent callout in the plot's empty upper-left | `_qc/preflight/s02.png`, then `_qc/final/02-framework.png` |
| 2 | B07 | Funnel: the two narrowest bars were smaller than their own labels — "Screened for synthesizability" and "Shortlist for the laboratory" overflowed their cards into the note column | Layout restructured so the label sits in a fixed-width column and the bar is a pure proportional block; text is no longer inside a bar and cannot overflow one | `_qc/preflight/funnel-fixed.png`, then `_qc/final/05-funnel.png` |

## Timeline integrity

- 16 narration beats, 16 unique beat IDs, 0 duplicates.
- Measured audio total 179.44 s; master 180.011 s; the difference is a
  deliberate 0.58 s silent title hold.
- Composition `AUDIO_BEATS` matches `mp3/timings.json` exactly. No timing value
  was set by hand at any point.

## Non-blocking

The Remotion CLI prints a version-mismatch banner (`@remotion/paths` 4.0.490
against 4.0.486 elsewhere in the workspace) on every invocation. It does not
affect this composition and did not affect this render. Recorded in
`INTEGRATION.md`.

## Result

**No blocking visual or technical defect in the rendered master.**

The production gate passes on all three rows. The ship verdict is nevertheless
`unlisted-until-fixed`, on a content item rather than a technical one: the
±9.5 K figure in Scene 04 has not been verified against its source. See
`PROOF-COMPLIANCE.md` and `FACTCHECK.md`.
