# FACTCHECK — "Why Your Track Sounds Thin On A Phone"

Every factual claim, its basis, its verdict. Verified 2026-09-16 against the
final 7-beat cut.

**Both measurements came before the script**, and the second one was
**predicted before it was measured**. Raw log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt); method and limits:
[SOURCES.md](./SOURCES.md).

| # | Claim | Where | Basis | Verdict |
|---|---|---|---|---|
| 1 | A track can sound full in headphones and thin on a phone, with nothing broken | B00 | The consequence of claims 3–7. Framed as the viewer's experience, which is what makes it the reel's question | **PASS** |
| 2 | Recorded music has two sides, a left and a right, slightly different from each other | B01 | Definition of a stereo recording | **PASS** |
| 3 | That difference is what makes music feel wide | B01 | Established: interaural level and time differences are the primary cues for perceived source width and position | **PASS** |
| 4 | Headphones keep the two sides apart — left side to the left ear, right to the right | B01 | Definitional for headphone playback | **PASS** |
| 5 | A phone, laptop or smart speaker is one speaker, and one speaker cannot play two things at once — it has to add them together first | B01 | True of any single-driver playback: the fold-down sums the channels before the driver moves. Single-driver phones and smart speakers are the common case | **PASS** |
| 6 | Two people pushing a door the same way swing it open; pushing against each other, just as hard, it does not move | B02 | Analogy, and an exact one — superposition of two forces, and of two signals, is the same addition | **PASS** — analogy, stated as one |
| 7 | Where two sides agree you get sound; where they are opposite you get nothing | B02 | Linear superposition. Two equal-and-opposite signals sum to zero | **PASS** |
| 8 | A centred bass at 110 Hz came through a mono fold-down unchanged | B03 | Measured: **−13.4 dB one side, −13.4 dB summed, 0.0 dB change** | **PASS** — measured |
| 9 | A centred vocal at 440 Hz came through unchanged | B03 | Measured: **−16.2 / −16.2, 0.0 dB** | **PASS** — measured |
| 10 | A wide layer spread across both sides dropped by almost fifty decibels — effectively gone | B03 | Measured: **−17.0 → −66.5, a −49.5 dB change**. The frame prints −49.5 | **PASS** — measured |
| 11 | What survives one speaker is whatever sits in the middle | B03, B06 | Generalisation of claims 8–10, and the direct consequence of claim 7 | **PASS** |
| 12 | It is rarely that dramatic in a real track | B04 | Total cancellation requires an exactly inverted layer, which is a constructed case. Case 1 in the log *is* that constructed case, and the reel says so on screen | **PASS** — and volunteered |
| 13 | Most stereo width comes from delaying one side by a fraction of a millisecond | B04 | True of the common widener designs (Haas/delay-based and all-pass). Hedged as "most", not "all" | **PASS** — hedged |
| 14 | When a delayed side is added back, only certain frequencies cancel | B04 | **Predicted, then measured.** A 0.6 ms delay predicts nulls at odd multiples of 833 Hz; measured −10.2 dB at 830 Hz, −0.4 at 1660, −9.8 at 2500, −0.6 at 3300. All four predicted positions landed | **PASS** — predicted and measured |
| 15 | You lose holes out of the layer, not the whole layer — which is why a folded mix sounds hollow rather than silent | B04 | Follows from claim 14, and is exactly what the measured nulls at ~−10 dB rather than −∞ show | **PASS** — measured |
| 16 | Switching to mono and listening once will reveal it | B05 | The fold-down is exactly what a single speaker performs, so a mono monitor reproduces the failure | **PASS** |
| 17 | Usual culprits: stereo wideners, doubled parts, wide reverb on a centre element | B05 | All three introduce inter-channel difference on material that should be centred. Offered as the common cases, not an exhaustive list | **PASS** — advice |
| 18 | Narration voice is Kokoro `af_bella`, local and free | description.txt | `generate_audio_kokoro.py` reported `cost $0.00` | **PASS** |

## Why the nulls measured ~−10 dB and not −∞

Neither reason is an error, and both are why the reel says **holes** rather than
**silence**:

1. **The analysis bandpass is 120 Hz wide**, so each measurement collects energy
   from neighbouring frequencies that are *not* cancelling.
2. **The delayed layer is broadband noise, not a pure tone**, so only the
   component exactly at the null frequency cancels completely.

A narrower filter and a pure tone would drive these toward −∞. The wide-band
figure is the honest one for a real mix, which is the case the reel is about.

## What is measured but deliberately not on screen

**The whole comb-filter frequency table.** Predicting 830 Hz and 2500 Hz and then
landing on all four positions is the strongest result in either week-04 reel. It
is not in the video. From Rohan's review of the plan:

> These are too detailed. Keep it high level. Use details only where necessary.

B04's axis is therefore labelled only LOW NOTES to HIGH NOTES and carries no
numbers at all. The shape of the result — solid teeth with holes punched between
them — is the lesson a beginner can use. The numbers are in
[MEASUREMENTS.txt](./MEASUREMENTS.txt) for anyone who wants them.

Also cut: the three-column before/after comparison, and the per-band waveform
rows in B03 (position and outcome only).

## Honesty notes carried in the graphics themselves

- **B03's footnote names the method on screen** — a MEASURED badge reading
  "measured with ffmpeg on a track built for this: one side alone, then the same
  track summed to a single speaker." The track was *built* for the measurement,
  and the frame says so rather than implying a real mix was tested.
- **B04 opens by volunteering its own caveat**, before any of its evidence:
  *"Total silence is the clean example. In a real track it is almost never that
  dramatic."* The strongest version of the claim is stated as the constructed case
  it is.
- **B04's segment strip is a shape, not data.** 26 segments in landscape, 18 in
  portrait, comb-spaced by a deterministic function of the segment count. It is
  an illustration of the *pattern*, and carries no axis numbers that would invite
  reading it as a measurement.

## A measurement footgun worth recording

The first pass of the Case 2 measurement returned nothing. `volumedetect` prints
its results at ffmpeg's *info* level, so passing `-v error` suppresses the very
numbers being measured. The commands in MEASUREMENTS.txt carry a note about it.

VERDICT: **PASS** — 18 of 18 claims verified. 4 measured here (one of them
predicted first), 9 definitional or established, 5 appropriately hedged framing
or advice claims.
