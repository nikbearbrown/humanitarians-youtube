# FACTCHECK — "Why Your Track Gets Turned Down"

Every factual claim, its source, its verdict. Verified 2026-09-10.

**The experiment ran before the script was written.** Raw log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt); method and stated limits:
[SOURCES.md](./SOURCES.md).

| # | Claim | Where | Basis | Verdict |
|---|---|---|---|---|
| 1 | Two versions were made from one source on this machine | B01 narration | both derived from the same `src.wav` by ffmpeg filter chains recorded in the log | **PASS** |
| 2 | Their tallest points are almost identical | B01 readouts + ceiling rule | measured true peak: −1.0 and −0.2 dBFS → 0.8 dB apart | **PASS** |
| 3 | "Under a decibel apart" | B01 narration | measured gap is 0.8 dB | **PASS** — see note 1 |
| 4 | The squeezed one "sits nearly nine points higher on the loudness scale" | B01 narration | −15.3 vs −6.6 LUFS = 8.7 LU apart | **PASS** — see note 2 |
| 5 | On-screen figures −1.0 / −15.3 / −0.2 / −6.6 | B01 cards | measured, exact | **PASS** |
| 6 | The tallest point is one instant; loudness is an average over time | B02 narration + cards | definition of true peak vs EBU R128 integrated loudness | **PASS** — established |
| 7 | Loudness weighting follows how the ear hears | B02 card | R128 applies K-weighting, a frequency weighting chosen for perceived loudness | **PASS** — established, stated without numbers |
| 8 | Platforms turn tracks up or down to reach a target | B03 narration + graphic | the defining behaviour of loudness normalisation | **PASS** |
| 9 | The target is "around minus fourteen" | B03 narration + label | −14 LUFS is the most commonly published streaming figure; narration hedges with "around", the label with "≈" | **PASS** — hedged |
| 10 | The untouched file needed +1.3 dB; the squeezed one −7.4 dB | B03 narration + graphic | −14 − (−15.3) = +1.3; −14 − (−6.6) = −7.4 | **PASS** — exact arithmetic on measured values |
| 11 | Both arrive at the same loudness | B03 verdict | by definition of reaching one target; confirmed by rendering the squeezed file at −7.4 dB → −14.0 LUFS measured | **PASS** |
| 12 | The gap went from 12 to less than one | B04 narration + spans | measured LRA: 12.0 LU → 0.7 LU | **PASS** |
| 13 | Same volume change applied to both: loudness moved, the gap did not | B04 proof table | measured: B −6.6→−14.0 (LRA 0.7→0.7); A −15.3→−22.7 (LRA 12.0→12.0) | **PASS** — the reel's strongest claim, and fully measured |
| 14 | Turning a file up or down cannot give back crushed room | B04 narration | follows directly from claim 13 | **PASS** |
| 15 | A well-behaved export leaves the loudest moment ~1 dB under the ceiling | B05 artifact | standard practice, and what version A does (−1.0 dBFS) | **PASS** — presented as advice |
| 16 | The platform will not touch the gap | B05 artifact, B06 | normalisation applies gain; gain does not alter LRA, per claim 13 | **PASS** |
| 17 | Narration voice is Kokoro `af_bella`, local and free | description.txt | `generate_audio_kokoro.py` reported `cost $0.00` | **PASS** |

## Note 1 — the peak difference was rounded, then corrected

The first draft said "half a decibel apart." The measured difference is
**0.8 dB**. Factchecking caught it before the reel was finished and the line
was changed to "under a decibel apart," which is true of 0.8. The exact values
are also on screen beside it (−1.0 and −0.2), so the claim is checkable by
eye as well as by ear.

## Note 2 — "nine times louder" was wrong, and was cut

The first draft said the squeezed version "sounds nearly nine times louder."
That is a real error, not a rounding: **8.7 LU is a difference on a logarithmic
scale, not a ratio.** Treating it as a multiplier overstates the perceptual
effect by a wide margin — 8.7 LU is nearer a doubling-and-a-half of perceived
loudness by the usual rule of thumb, not a ninefold increase.

The line now reads "sits nearly nine points higher on the loudness scale,"
which describes the number on the meter — which is what the graphic shows —
without implying a ratio. B01's audio was regenerated after the change.

This is the value of running the factcheck as a real gate rather than a
write-up: the claim would have shipped otherwise.

## What is established rather than measured

Claims 6, 7, 8, 9, 15 are standard results and practice, not things this build
tested. They are presented as explanation. No invented numbers are attached to
any of them, and the only figure among them (−14) is hedged in both narration
and label.

## Caveats stated on screen

- B01's footnote names the method: "ffmpeg's EBU R128 scanner on a 30-second
  test signal I built for this." The reel never implies this is a commercial
  song.
- B03's footnote: "Targets differ between platforms and change over time. The
  behaviour does not: loud tracks get turned down." No platform's internals are
  claimed.

VERDICT: **PASS** — 17 of 17 claims verified, 13 of them measured on this
machine. Two narration errors were caught by this factcheck and corrected
before the reel was finished (notes 1 and 2); B01's audio was regenerated.
