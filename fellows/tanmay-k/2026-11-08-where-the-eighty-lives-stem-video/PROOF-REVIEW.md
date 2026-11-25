# Feedback: "Where the Eighty Lives" — compiled films after fixes 1 to 5, video review 2

> Final-stage review of the compiled films (earlier stage reviews are kept locally; this one supersedes them).

> **Update 2026-11-08, figures corrected.** FACTCHECK found the first timing comparison was not like for like (the recurrent side did more gate work), so every figure quoted below that comes from it is superseded: 5.7x is now 3.7x, 1.4x is 1.3x, the band 4.8x to 5.7x is 3.3x to 3.8x, "about 6x" is "about 4x", 6.9 and 6.7 ms are 6.1 and 6.4 ms (see `FACTCHECK.md`, `MEASUREMENTS.md`). Gate P was re-signed on draft 3, and both films were rebuilt and re-measured. The structure, findings and scores of this review are unchanged. Re-run results on the rebuilt files: **long** 3840 x 2160, 226.20 s, -14.6 LUFS, no hard cuts, longest still 7.1 s, 20 of 21 voiced figures on screen when spoken (the exception is the B05 back-reference), B09 source line at 10.2 s against "memory" at 10.6 s, side-by-side held B04 10.7 s, B05 8.4 s, B07 4.5 s; **Short** 2160 x 3840, 102.27 s, -14.6 LUFS, 9 of 9 figures on screen when spoken, longest still 2.5 s, longest silence 0.91 s, 48% to 91% of the picture carried across line changes, loop 0.01. All measured checks pass (`check_video.out`, `proof_video.out`).

**Reviewed:** the rebuilt 4K masters, `where-the-eighty-lives.mp4` (3840 x 2160, 3:47) and `where-the-eighty-lives-short.mp4` (2160 x 3840, 1:43), against the signed narration and the Whisper word clock. All numbers are measured from the compiled files or the audio timings (`check_video.out`, `proof_video.out`).
**Prior:** `PROOF-REVIEW-VIDEO.md` (review 1: long 12/12 with one failing gate item, Short 10/12). Its five findings are applied; this review checks that they worked.
**Still not judged:** delivery by ear, and whether the motion feels smooth. The motion is still reveals, fades and the two dial sweeps, not continuous animation.

## What changed since review 1
1. **B09's source line now lands before the claim:** 10.3 s, against "memory" voiced at 10.7 s (was 11.4 s, 0.6 s late).
2. **S05's figures are on screen when voiced:** the Short now shows 9 of 9 voiced measurements at or before the word (was 8 of 9, one 2.5 s late). "A hundred" and "twenty million" are pinned to their words.
3. **The Short's hook moves sooner:** the first visible change against frame 1 is at 0.45 s (was 0.9 s); the voice starts at about 0.3 s.
4. **The Short is one persistent scene:** the two model containers, the weight block, the dial and the panels stay put and change state. Between the last frame of a line and the first of the next, 48% to 91% of the picture is the same (was 0.7% to 17%). The Short still dissolves at each line change, but over a shared layout; the end frame equals the first (mean difference 0.01 of 255).
5. **The dial visibly turns:** in B07 it sweeps ZERO to 8 ROWS before the 1.40x bar and on to MATRIX UNIT before the 5.7x bar (1.0 s each); in S07 it sweeps from ZERO to MATRIX UNIT in 1.4 s.

## Long film (16:9)
**Verdict:** **clear-for-public at frame and gate level, pending your listen.** Teaching **12/12** (unchanged). Production gate **PASS**.
| Check | Result |
|---|---|
| Native 4K, 30 fps, audio in step | PASS (6,797 frames; audio 226.60 s = video 226.60 s) |
| Loudness | PASS, -14.6 LUFS, true peak -1.9 dBFS |
| Margins; hard cuts | PASS; largest frame-to-frame change 3.32 of 255 |
| Sources on screen at the claim | PASS: B00 library title at 0.0 s ("eighty" at 1.2 s); B09 memory-map line at 10.3 s ("memory" at 10.7 s); "NOT MEASURED ON A CHIP" at 12.2 s ("measured" at 14.4 s) |
| Figures on screen when voiced | PASS: 20 of 21. The one exception is B05's "eighty" (14.4 s), a back-reference to the figure shown in B00; low, not a gate item. |
| Side-by-side held at least 2 s | PASS: B04 10.7 s, B05 8.6 s, B07 4.5 s |
| Longest stretch with no visible change | 7.1 s (B01, 23.8 s); no rule applies to the long film |

## Short (9:16)
**Verdict:** **clear-for-public at frame and gate level, pending your listen.** Shorts rubric **12/12**. All nine measured checks pass.
| Criterion | Score | Evidence |
|---|---|---|
| Hook | 2 | The headline is on screen at frame 1; the first change is at 0.45 s, about 0.15 s after the first word. It is the nearest this build gets to "moves from frame 1"; a pin at 0.0 s would not be visible any sooner (a fade needs about 0.35 s to read). |
| Standalone context | 2 | S02 and S03 define the recurrent model and the weights before any figure; the operation is defined in S05. |
| One arc with its own ending | 2 | Own question (S01), answer (S07 to S09), ending (S10), exact title (S11); one scene with state carried (48% to 91%); loops back to frame 1. |
| Phone legibility | 2 | All ink inside x 120 to 1800, y 461 to 2880; type at least 68 px at 2160 wide; nothing in the right rail; contrast 15.7:1 text, 7.0:1 labels. |
| Pace | 2 | Longest still 2.5 s; longest silence 0.90 s (rule: under 1 s); 2.94 words per second; figures 9 of 9 on screen when voiced; side-by-side held S05 4.0 s, S06 3.4 s, S07 2.7 s. |
| Trailer function | 2 | Exact searchable title with "SEARCH THIS TITLE" in S11; channel and presenter in S03; library-title card visible 0.5 s to 9.0 s (rule: at least 2 s). |
| **Total** | **12/12** | |
| Gate: 2160 x 3840 at 30 fps, audio 48 kHz in step, -14.6 LUFS / -2.0 dBFS, safe zone, type, no hard cuts (largest change 1.04 of 255), duration 102.6 s | all PASS |

## Findings
1. **[LOW] B05 voices "eighty" with no figure on screen.** A faint 80x in the corner would show it; optional.
2. **[LOW] The Short's lowest carry-over is at the ends** (S01 to S02 49%, S10 to S11 48%), where the library card and the panels replace what was there. That is the story changing, not a break in the scene.
3. **[FOLLOW-UP] The storyboard stills for the Short are out of date.** The approved Short frames in `storyboard/` and the picture plan in `SHORT-SCRIPT.md` describe the earlier slide-per-line layout, not the persistent scene in the video. They need regenerating from the new scene before the folder is staged.
4. **[NOTE] The Short is denser than the long film.** The persistent layout keeps the containers, weights and counters on screen together, with type at the 68 px floor (34 px at 1080). It passes the measured legibility checks; your eye is the real test.
5. **Recorded decisions stand:** weight/wait kept; B00 and B09 pace kept; Gate P stands (no narration changed).

## What works
- The Short is now one thing: the same two boxes carry the story from "small vs bigger" to the three numbers.
- The dial turns when the narration says to turn it, in both formats.
- Every figure and every source line is on screen at or before the word that needs it, except one back-reference.
- Both films were built audio-first, so reveals follow the voice.
