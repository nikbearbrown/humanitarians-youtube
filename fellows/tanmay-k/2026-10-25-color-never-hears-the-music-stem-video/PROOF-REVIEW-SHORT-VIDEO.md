# Feedback: "The Sky Switch" — Short (9:16), video review 5

**Rubric:** the Shorts-specific rubric (hook, standalone context, one arc with its own ending, phone legibility, pace, trailer function; 0–2 each, /12) and the 11-point compiled-file gate. Not the long film's rubric.
**Reviewed:** the compiled video `color-never-hears-the-music-short.mp4` (2160×3840, 30 fps, 75.53 s, narration `am_onyx`), its measured gate (`VIDEO-GATE-SHORT.md`, `proof_short.py`), frames extracted from the file (S01, S03, S04, S06, S08, the loop fade and the last frame, plus the first frame), and Tanmay's watch and listen (2026-10-25, no changes requested).
**Prior reviews:** `PROOF-REVIEW-SHORT-RENDERED.md` (12/12, provisional on this gate).
**Verdict: 12/12, and the 11-point gate passes 11/11, measured on the compiled file.** The provisional condition from the stills review is now closed.

## Rubric

| Criterion | Score | Reason (measured or viewed on the video) |
|---|---|---|
| Hook | 2 | Frame 0 is the opening grey sky (colour distance 1 from the intended grey; not black, mean luminance 211); the question starts at 0.0 s; clouds move from the first frame; the headline "Which sky goes with which?" is up from frame one. |
| Standalone context | 2 | A viewer who has not seen the long film gets both tunes (A quick, B slow), the question, the answer, what the study did (Berkeley, Bach/Mozart/Brahms, 97 listeners, two countries), why (the strip and the paper's two scales), an example (Bach, Brahms), the swap, the limit and where to test it. |
| One arc with its own ending | 2 | One scene, no hard cuts (largest frame-to-frame change 2.78 grey levels; a cut is 20+). The closing card fades out and the sky eases back to the opening grey; the last frame differs from frame 0 in 3.40% of pixels, all of them clouds. |
| Phone legibility | 2 | Ink x 59–899, y 230–1438 on 151 sampled frames; zero right-rail pixels; smallest type 34 px logical across 2,266 frames; 8 of 8 lines show a 34 px source line in y 1335–1440; contrast ≥ 4.5. |
| Pace | 2 | Longest static run 0.97 s; frame change 2.5 s apart never below 0.56%; no silence ≥ 0.7 s; labels now arrive on their spoken words (the first render had some up to 2.5 s late). The voice reads brisk (3.1–3.8 words per second) and Tanmay's listen cleared it. |
| Trailer function | 2 | Name in S02; the exact searchable long-film title spoken in S08 and shown on the closing card; captions (`.srt`, `.vtt`) built; the long film is the related video to set at upload. |
| **Total** | **12/12** | |

## The 11-point gate (measured on the compiled file)

1 resolution and first frame PASS · 2 ink zones PASS · 3 type size ≥ 34 px PASS · 4 figures on screen when spoken (97, Bach, Brahms, the 0.99 counter, the source range, the title; 8 of 8) PASS · 5 sources in the safe area (8 of 8) PASS · 6 no hard cuts PASS (2.78 vs 3.0) · 7 no static stretch over 3 s PASS · 8 loop-friendly last frame PASS · 9 audio PASS (aac 48 kHz mono, −14.5 LUFS, −1.9 dBTP) · 10 no foreign text or handle PASS (72 strings, none outside the script) · 11 duration PASS (video 75.533 s, audio 75.533 s).

## What the build changed from the script, and why

1. **[recorded] Label timing.** Labels now appear on their spoken words (Brahms, the title card). The first render had them 1.5–2.5 s late.
2. **[recorded] Closing card.** It now appears on the word "Color" and stays about 4.4 s (the script said about 3 s); the fade back to grey is 1.0 s (the script said 0.7 s, which measured 3.05 grey levels per frame, the film's largest). `SHORT-SCRIPT.md` is updated to match.
3. **[recorded] Text hand-offs.** Old text fades out, then new text fades in, so no two lines of text overlap at half strength.
4. **[recorded] Hard cut removed.** The ratings chip no longer vanishes in a single frame.

## Findings

1. **No defects open.** Everything the gate and the frame review found was fixed before this review.
2. **[EDIT, optional]** The lower third of the frame under the source line is empty by design (it is the app's caption and button zone). If you want a fuller composition, enlarge the strip; the safe-area gate would need re-running.
3. **[EDIT, optional]** The S02–S03 strip hint is a pale, unlabelled card. Labelling it would help a first-time viewer; not required.
4. **At upload:** set the long film as the related video, and put the synthetic-voice and synthesized-tune disclosures in the description (the Week 26 pattern).

## What works

- One continuous scene, one idea per line, with the headline carrying the argument for muted viewers.
- The paper's own example (Bach, Brahms) gives the claim a picture before the swap; the limit is in the Short.
- It loops: the ending returns to the opening grey sky.

## Do next

1. Upload metadata (`short/…-youtube.md`) in the Week 26/27 pattern; related video set at upload.
2. [EDIT] Delete `short/_frames` (495 MB, temporary) once you confirm.
