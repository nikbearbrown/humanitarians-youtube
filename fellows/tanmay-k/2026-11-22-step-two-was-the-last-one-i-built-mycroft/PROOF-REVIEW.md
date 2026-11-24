# PROOF review: Week 32 work video (final, on the COMPILED masters; earlier stages below) — "Step Two Was the Last One I Built", Week 32 work video

**Files reviewed:** the long master (3840x2160, 30 fps, 4:26.30, 18.1 MB) and the Short master (2160x3840, 30 fps, 1:43.30, 6.9 MB). Kokoro `am_onyx` at natural speed; narration of record = the Gate P signed text (`READ-ALOUD-v1-signed.md`, `READ-ALOUD-SHORT-v1-signed.md`, with the logged B08 and B01 amendments).

**Verdict:** clear on this review. Teaching rubric 12/12 (long), Shorts rubric 12/12 (Short); every measured gate PASS. Publishing is Tanmay's call.

## Measured on the masters
| Check | Long | Short |
|---|---|---|
| Resolution, frame rate | 3840x2160, 30/1 | 2160x3840, 30/1 |
| Colour | H.264 High yuv420p, BT.709 matrix, primaries, transfer, tv range (tagged) | same |
| Colour fidelity (decoded master vs the renderer's own frame) | solid fills within 1 level (amber box 70,56,28 -> 70,56,27; panel 26,31,40 -> 25,31,39; background 14,17,22 -> 13,17,23); 0.8 to 1.0 mean difference over whole frames | 0.73 to 0.76 |
| Duration vs plan | 266.30 s (plan 266.30 s) | 103.30 s (103.30 s) |
| Audio | AAC 48 kHz mono | same |
| Loudness / true peak | -14.7 LUFS / -1.9 dBTP | -14.6 LUFS / -1.9 dBTP |
| Black frames | none; frame 0 luma 22.2, minimum 16.7 | none; frame 0 luma 21.5, minimum 20.3 |
| Luma pops (beat cuts excluded) | 0 (designed beat-to-beat cuts step up to 13.8) | 0 |
| Silence | none of 2.5 s or more | none of 1.0 s or more |
| Longest still stretch | 4.13 s (B12; limit 5.0), all 13 beats pass | 2.20 s (limit 3.0) |
| Hard cut / loop / safe area | n/a | largest one-frame change 2.05; last frame vs first 0.015; ink x 60..901, y 256..1425, right-rail ink 0 px |
| No foreign handle | pass | pass |

## Checked on the masters themselves
- **Narration intact.** Whisper on the masters' audio: every beat and line matches the signed text; lowest are the number-heavy ones because digits count as one heard word (B05 0.78, B04 0.88, S03 0.80, S04 0.82); B00, B07, S00 exact.
- **Picture-to-word sync in the master.** 47 of 58 long-film anchored elements and 24 of 35 Short elements are matched by word: mean offset -0.01 s and +0.01 s, worst 0.56 s and 0.25 s (limit 0.6). The remaining 11 per film have a number or a split word in their anchor and cannot be matched by word; they were bound to Whisper word times on the audio pass and the plan contract passes on that clock (every voiced figure on screen at or before its word).
- **Layout.** Geometry audit of the 21 end-state frames: 0 issues; legibility 0 warnings.
- **Figures and sources.** Every figure on screen comes from a rerun of our own scripts (`FACTCHECK.md`): 504.5625 / 540.5625, 66,898.13, 65,098.13, +1,800.00, 24.35% against 21%, the two hashes, the six-set table. Source line on every beat B01 to B09. The wrong file is called a scratch copy on screen and aloud (B04, S03). No other fellow named, no outside media, no @ handles.

## Teaching and Shorts rubrics
Long 12/12: framework shown and voiced before the worked example (B01 three-question check, bar through B02 to B10); reusable rubric (B10); worked example (B03 to B07, all six sets then one wrong file); falsifiability (B03 the stand-in right 6 of 6, B06 step 1 did stop, B11 limits); active task (B10); friction (B06 "nobody was wrong", B09 the unpaid second stand-in). Short 12/12: hook (claim at the first words, picture moving from frame 1), standalone context (S01 to S02 before any number), one arc with its own ending (question S00 to answer S04 to S05, limits S06, task S07), phone legibility (measured: safe area, right rail empty, type 34 px or more), pace (longest still 2.20 s), trailer function (exact title in the S07 box and spoken).

## Open items for the ear (not defects of the files)
B05 "from two switched digits" (Whisper heard "switch"; Kokoro's phonemes are correct), B07 "N-V-D-A" (heard once as "in vda"), and the long number runs in B04, B05, S03 and S04. B01's closing three questions are the rhythm check.

## The earlier stages (what each found, all fixed before the next)
**Script (draft 1, before Gate P).** Two overclaims and one ambiguity: B07 said the wrong file's price "never reaches step three" although step 3 still reads the sample folder directly (now: the step whose job is to ask stops it, and wiring step 3 to step 2's output is the next change, not made); B03 hid that step 3 rejects all five defective files (rerun on all six sets, the counts are now stated exactly); S07 said "give it" without saying what (now "the stand-in and the real step"). The word-run check against all earlier work videos: 0.6% of words in shared runs, only the standing sign-on line; every banned word absent.
**Frames (21 stills).** Spacing fixes (S00, B01, B09); one substance item: B08 said step 3 asked only whether a file parsed and had a price, but step 3 also checks the ticker is one of the five (a coarse "is this one of ours" that cannot tell a changed value). Fixed with Tanmay's go-ahead (Gate P amendment, B08 only). Rubric re-score: framework was 1 because the three-question check only appeared at B08 and B10, after the worked example; B01 now voices and shows it (amendment, B01 only) and a three-chip bar carries it through B02 to B10: 12/12.
**Motion.** Four fixes: B06 showed "step 3 never reads that file" before the file was introduced (reordered); B04 and B05 opened on an empty frame (card and caption now there from frame 1); B03 sat 8 s with only the table re-outlining (a pulse on the clean row added); a 4 px spacing slip. After audio, the Short's loop failed (first frame already held the first caption; 1.589 grey levels against 0.5): captions now fade in, loop 0.015.
**Audio.** Whisper heard every line; the lowest matches are number-heavy (digits as one heard word). Ear items: B05 "from two switched digits" (heard "switch"), B07 "N-V-D-A", the number runs in B04, B05, S03 and S04.
