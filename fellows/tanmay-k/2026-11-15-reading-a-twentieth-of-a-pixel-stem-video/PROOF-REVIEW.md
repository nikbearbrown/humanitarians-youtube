# Feedback: "Reading a Twentieth of a Pixel", Week 31 topic video, long (16:9) and Short (9:16), final review on the compiled files (2026-11-17)

**Rubrics:** `PROOF.md` teaching rubric /12 plus production gate (long); the Shorts rubric /12 plus the measured compiled-file gate (Short). Narration of record: the Gate P signed text (`READ-ALOUD.md`, `READ-ALOUD-SHORT.md`). Figures: `FACTCHECK.md` and `MEASUREMENTS.md`.
**What was reviewed, in order:** the script (long 11/12 then 12/12 once the picture contract was written; Short 10/12 then 12/12), the 20 rendered stills (both 12/12, four places where the picture lagged the narration found and fixed), the silent motion previews, and the compiled files `long.mp4` (3840x2160) and `short.mp4` (2160x3840) with the Kokoro `am_onyx` narration. The scores below stand because the compiled files pass the measured gate.

## Verdicts
| | Rubric | Production gate (measured on the compiled file) | Verdict |
|---|---|---|---|
| Long (16:9) | **12/12** | **PASS** on every check below | clear on this review; publishing is Tanmay's call |
| Short (9:16) | **12/12** | **PASS** on every check below | clear on this review; publishing is Tanmay's call |

## Long: rubric
| Criterion | Score | Evidence |
|---|---|---|
| Explicit framework | 2 | The three-panel frame (MOVED / WIDE / COUNTED) is on screen empty from frame one, fills as each number is earned (B02 to B05) and lights panel by panel in B06 beside the rule. |
| Reusable rubric | 2 | B06: error = width / square root of photons; B11 works N = (42.5 / 5)^2 = 72 step by step. |
| Worked example | 2 | B04 to B05: the same line at 10, 100 and 1,000 photons with guess, error and pixel for scale; B02: Andromeda's 0.66 nm as 13 pixels. |
| Falsifiability / edge case | 2 | B06 plots our measured errors against the rule over four decades (ratio 1.06 to 1.09); B10 shows where it bends (sky glow, 1.4 to 3.4 km/s) and a ledger of what was not tested and that there is no telescope data. |
| Active task | 2 | B11. |
| Friction | 2 | B00 poses a ruler finer than its own marks (23 marks of 1 km/s fit in one pixel, shown); B08 puts -300 and -109 side by side and splits 300 into 192 plus 109. |
| **Total** | **12** | |

## Short: rubric
| Criterion | Score | Evidence |
|---|---|---|
| Hook | 2 | First words state the condition (a speed to within 1 km/s from light alone); the picture is moving from frame 1. |
| Standalone context | 2 | S01 says what a Doppler shift is and how color becomes speed before any photon; S02 says "no telescope: simulated". |
| One arc, own ending | 2 | Question, context, setup, ten photons, a thousand, rule, limit, close; one persistent pixel row; the last frame equals the first. |
| Phone legibility | 2 | Ink measured at x 60..901, y 256..1429 (safe 60..900, 230..1440); right rail empty; type at least 34 px logical. |
| Pace | 2 | Longest still stretch 2.07 s; no silence of 1 s or more. |
| Trailer function | 2 | S07 says and shows the exact title, "Reading a Twentieth of a Pixel". |
| **Total** | **12** | |

## Measured gate on the compiled files (`measure_final.py`)
```
  [PASS] no foreign handle in any on-screen text: no @ in either plan

LONG 16:9  (long.mp4)
  [PASS] resolution: 3840x2160 (want 3840x2160)
  [PASS] frame rate: 30/1
  [PASS] duration matches plan: 209.50 s (plan 209.50 s)
  [PASS] audio 48 kHz AAC mono: 48000 Hz aac x1
  [PASS] loudness near -14 LUFS, true peak <= -1.5 dBTP: -14.6 LUFS, true peak -1.8 dBTP
  [PASS] frame 0 not black, no black frame anywhere: frame 0 luma 20.0, minimum over 6285 frames 19.2 (background 16.6)
  [PASS] no luma pop between frames (beat cuts excluded): 0 pops; beat-cut steps up to 16.4
  [PASS] no silence of 2.5 s or more in the long film: 0 found
  per beat: longest still stretch (gate 5.0 s)
  [PASS] B00 still stretch: 3.60 s at 12.1 s
  [PASS] B01 still stretch: 4.20 s at 1.1 s
  [PASS] B02 still stretch: 3.60 s at 6.5 s
  [PASS] B03 still stretch: 3.87 s at 7.3 s
  [PASS] B04 still stretch: 3.40 s at 7.6 s
  [PASS] B05 still stretch: 3.87 s at 13.7 s
  [PASS] B06 still stretch: 3.60 s at 8.7 s
  [PASS] B07 still stretch: 3.53 s at 2.5 s
  [PASS] B08 still stretch: 4.27 s at 1.5 s
  [PASS] B09 still stretch: 0.67 s at 0.8 s
  [PASS] B10 still stretch: 4.33 s at 18.1 s
  [PASS] B11 still stretch: 3.47 s at 4.3 s

SHORT 9:16  (short.mp4)
  [PASS] resolution: 2160x3840 (want 2160x3840)
  [PASS] frame rate: 30/1
  [PASS] duration matches plan: 104.17 s (plan 104.20 s)
  [PASS] audio 48 kHz AAC mono: 48000 Hz aac x1
  [PASS] loudness near -14 LUFS, true peak <= -1.5 dBTP: -14.6 LUFS, true peak -1.9 dBTP
  [PASS] frame 0 not black, no black frame anywhere: frame 0 luma 17.5, minimum over 3125 frames 17.0 (background 16.6)
  [PASS] no luma pop between frames (beat cuts excluded): 0 pops; beat-cut steps up to 0.0
  [PASS] no silence of 1.0 s or more in the Short: 0 found
  [PASS] M1 visible change at least every 3.0 s: longest still 2.13 s at 64.9 s
  [PASS] M2 no hard cut: largest one-frame change 1.69 grey levels
  [PASS] M3 loop: last frame equals first: mean abs difference 0.008
  [PASS] M5 ink in safe area, none in right rail: x 60..901, y 256..1429 logical; right-rail ink 0 px

ALL MEASURED GATES PASS
```
Beat-to-beat cuts in the long film are designed hard cuts (the largest luma step at one, 16.4, is the B08 to B09 cut); the check counts only steps that are not at a beat boundary.

## Review of the compiled masters (2026-11-17, after the name correction)
Read from frames pulled out of `long.mp4` (the end state of each of the 12 beats) and `short.mp4` (the end of each of the 8 lines), against the signed narration and `FACTCHECK.md`, plus the measured gate above.
- **Found and fixed in the long film:** B04, the label "the error covers 64% of one pixel" sat touching "one pixel: 22.8 km/s" (moved apart); B09, the sweep outlines around the six bars covered the radius labels 1, 3, 5, 8, 11, 15 (outline bottoms raised). B04 and B09 were re-rendered, the film re-assembled, and the gate re-run: still all pass.
- **Checked and fine:** every voiced figure is on screen at or before its word on the measured clock (25 long, plus the Short's); sources are on screen in B02 and B08; our own choices carry labels ("my pixel", "my choice", "toy disk: assumed. Not a measured galaxy."); the Short's last frame equals its first and it ends on the exact long-film title; the name is voiced "Cool-car-knee" and appears as "Kulkarni" in text.
- **Scores:** unchanged, long 12/12 and Short 12/12.
- **Not covered by this review:** I measured the audio (loudness, silence, Whisper word check) but did not listen to the full masters; Tanmay's listening is the ear check. Whisper's two flags remain (S04 "guess" heard as "guest", S07 "finely" heard as "finally"), kept as is by Tanmay.

## What the measuring caught before this pass (all fixed, re-measured)
1. A caption in the Short (S04) that the plan listed but the picture never drew, found when the change threshold was set above codec noise.
2. Faint dashed lines in B01 and S02 that passed on the preview but vanished on a quarter-size decode of the 4K file, leaving 8.8 s and 3.7 s without a visible change. They are now brighter and thicker, and B01 carries a "one line of light" label.
3. Long stretches with nothing moving (B00 8.7 s, B09 8.9 s, B06 7.1 s) cut to no more than 4.4 s (measured on the compiled file) after Tanmay asked for about 5 s; each added step is tied to what the narration says at that moment.
4. After the audio was measured the plan was rescaled to the real speech and every spoken figure pinned to its Whisper word time; B11 then showed a 5.3 s stillness, fixed with one added step.

## Not claimed
Nothing was measured on a telescope; sky glow is the only real-spectrum complication tested. The film says so (B10, S06). Whisper flagged two spots to listen to (S04 "guess steadies" heard as "guest studies", S07 "finely" heard as "finally"); the name, voiced from `Cool-car-knee` after Tanmay's correction, is heard as "Kulkarni" in B01 and S02. Tanmay's decision on the audio, after the preview files were sent: keep as is. Loudness is -14.6 LUFS, true peak -1.8 / -1.9 dBTP.
