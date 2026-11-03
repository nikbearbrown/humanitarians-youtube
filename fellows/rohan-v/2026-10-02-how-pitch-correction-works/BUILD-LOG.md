# BUILD-LOG — "How Pitch Correction Works"

What broke, what it cost, and what changed because of it. Built 2026-10-05 (late for the week
of 28 Sep – 2 Oct).

## 1 — Toolkit update first

`git fetch` brought three upstream commits (show-tell, tldr and lecture skills, Claude Code
scene templates). The merge conflicted in `Root.tsx`, `scenes.json`, `type_check.py` and
`SCENE-DOC-TODO.md`; every conflict was two independent additions, kept from both sides, and
`scenes.json` regenerated with `./art scene-index` (839 renderable). `tsc` reports two errors,
both in upstream files untouched here (`ChatReplyMock.tsx`, `SeisSongReadAlong.tsx`); the
bundler does not type-check, and none of this reel's scenes is affected.

## 2 — The evidence is a program, not a picture

EXECUTABLE-EVIDENCE.md: anything that can be computed is run. `pitch_demo.py` synthesises a
seven-note melody with drift, scoops and vibrato, detects pitch with YIN, snaps to a note
(chromatic or C major), glides with a time constant, shifts the audio with TD-PSOLA, and then
runs the detector **again** on each corrected file. Sanity checks on the corrected audio: RMS
within 1% of the input, no sample step larger than the input's own (no clicks). Detector
accuracy against the synthesised truth: median 1.7 cents. `export_pitch_data.py` turns the run
into `scenes/pitch/pitchData.ts` and typesets the cents rule with `typeset_math.py`.

## 3 — The wrong-note example flickered

With the last note 62 cents flat, the vibrato (±22 cents) reached 66.6 on its peaks, past the
F♯/G midpoint, so the chromatic re-measured curve jumped to G4 on every peak. Real, but it
contradicted "lands on F sharp". Moved to 75 cents flat: the chromatic result is now F♯4 on
100% of held frames (66.0 ± 0.05) and the C-major result G4 on 100%. Changed numbers re-voiced
(`retune_numbers.py`, `generate_audio_kokoro.py --only B04 B05 B06`), re-aligned, re-mixed,
cues re-synced (all resolved).

## 4 — Hearing it: listening clips in the beat audio

The beat's own `audio_file` is the clock, so B04 and B05 carry a mixed track
(`mix_listen.py`): narration, then the run's WAVs (level-matched to the narration's RMS,
otherwise unedited). `actual_duration_s` is re-measured from the mix; `props.listen` gives
the clip windows as beat fractions so the scene can show what is playing. Alignment runs on
the narration-only files before mixing.

## 5 — Portrait layouts, rebuilt

The first portrait probes failed by eye before any gate ran: two-line titles overlapped the
first label, the period caption collided with the next label, and the lower third was empty.
Each scene now has its own phone layout on the PHONE scale with content across y 21–78% and
the spark at 80%; titles and spark lines are shortened in `vertical/beat_sheet.json`. Probe
stills of every portrait beat were rechecked.

## 6 — Small fixes from the landscape probes

- B01: the octave frame and the ruler sit as faint shells from the first frame (no empty
  lower third at a QC sample).
- B02: the one-period caption and the lower plot's label no longer share a line.
- B03: the readout shows the measured frequency before the needle moves, and "0.0" rather
  than "−0.0" once in tune.
- B06: the in-panel "not in C major" label covered the curves; the fact stays in the outcome
  rows and the struck lane.

## 7 — GATE T blocked the first final: data curves read as accent text

§8.3 flagged B04 and B06: thick and dashed #D97757 strokes (the corrected curves; the chromatic
curve is dashed) form text-like blobs in the brand terracotta at 2.74:1 on cream. Fixed in the
component rather than exempted: corrected curves and the playhead are drawn in `SPARK_TEXT`
(#A9482B, 5.5:1) in B04, B05 and B06, so the three beats stay consistent. Re-rendered both aspects.

## 8 — The first renders played on the wrong clock

The new scenes size themselves from `props.durationSeconds`, which `sync_cues.py` does not write.
The probes passed it in, so every probe still looked right; the real renders fell back to the
20 s default and were freeze-held to the beat length. Visible worst in B04 and B05 (33.5 s and
35.8 s): the animation finished early and the listening clips played over a frozen frame. Fix:
`durationSeconds = actual_duration_s` written into every beat of both sheets, and B01–B06
re-rendered in both aspects. Caught on the first rendered frame of a listening window, before any
final was built.

## 9 — Gate V refused the first landscape final; the portrait was underfilled

- **§8.1 on the curves.** At 4K the thin pitch curves in B04–B06 split into short segments that
  the size check reads as sub-floor text. They are data, not type, so `PitchMelodyFix`,
  `PitchRetuneSpeed` and `PitchWrongNote` (+ `916`) were added to type_check's
  DIEGETIC_PALETTE_PATTERNS with a comment saying why. The real labels around them still pass.
- **Landscape contrast (B05, B06).** Gate V measures ink against background over every non-
  background pixel; the large tinted lane fills behind the target note pulled that under 0.30.
  The highlight is now a faint tint (6–15%) plus a solid centre line on the target note, which
  reads better too.
- **Landscape B03 underfill (55% of the safe box).** A ghost baseline hairline at 84% of the
  height closes the empty lower band; fill is now 80%.
- **Portrait underfill (B02, B03, B05, B06 at 48–54%).** All six portrait scenes carry the same
  ghost hairline at 78%; B01's brackets became shaded bands and B02's copied wave and dot use
  `SPARK_TEXT`. 4K probe stills of all nine re-rendered beats: Gate V clean (fill 64–80%),
  GATE T size and contrast pass.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/PitchCorrection_RohanV.mp4` | 3840×2160 | 197.38 s | `4f5e7b5c45f5005e2947494ccd344aad1545d702d902024af634de2a219d2001` |
| 9:16 | `vertical/PitchCorrection_RohanV.mp4` | 2160×3840 | 197.38 s | `492264e767ec41c49f272d709350086af37cc981269a197ee5357d03812c6042` |

Gates on the accepted finals: GATE F pass; GATE T pass ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(18 landscape and 18 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png).

Landscape: accepted on the fourth final (refused by GATE T §8.3, §7; GATE T §8.1 on the curves, §9; Gate V, §9). Portrait: accepted on the third (refused by GATE T; then GATE F, because the vertical folder lacked FACTCHECK, SHOTLIST and PROMPTS, now copied in). All on 2026-10-05.

Uploaded to Google Drive `2026-10-02/landscape/` and `2026-10-02/vertical/`; md5 of each Drive copy
matches the local master.
