# Feedback: "Minus Seventy-Eight" — Short (9:16), video review 4

**Rubric:** the Shorts-specific rubric (hook, standalone context, one arc with its own ending, phone legibility, pace, trailer function; 0–2 each, /12) and the 11-point compiled-file gate. Not the long film's rubric.
**Reviewed:** the compiled video `short/the-sum-behind-the-number-short.mp4` (2160×3840, 30 fps, 78.8 s, `am_onyx`), its measured gate (`short/VIDEO-GATE-SHORT.md`, `proof_short.py`), nine frames the agent viewed and nine I extracted myself (the opening, "It's a sum", the S03 scenario card, S04 blocks, S05 bars, S06 shares, S07 columns, the closing and the last frame). Tanmay listened to the narration and cleared its pace.
**Prior reviews:** `PROOF-REVIEW-SHORT.md` (script, 12/12), `PROOF-REVIEW-SHORT-RENDERED.md` (stills and audio, 11/12 pending the listen).
**Verdict: 12/12, and the 11-point gate passes 11/11, measured on the compiled file.** The two conditions from the earlier review (the dead air and the pace) are closed.

## Rubric

| Criterion | Score | Reason (measured or viewed on the video) |
|---|---|---|
| Hook | 2 | Frame 0 is the opening state on the cream page (not black); the number "−78%" at full size and the question are on screen from frame one; the first spoken words state it. |
| Standalone context | 2 | A viewer who never sees the long film gets what a stress test says (S01), who made it and what Mycroft is (S02), what a scenario is (S03), the sum (S04–S06), the check (S07) and the question and title (S08). |
| One arc with its own ending | 2 | One scene, no hard cuts (largest frame-to-frame change 2.47 against a limit of 3.0); a closing 1.0 s ease returns the number, the chips and the empty stack to the opening state; the last frame differs from frame 0 in 0.36% of pixels. |
| Phone legibility | 2 | Ink x 59–899, y 230–1439 over 158 sampled frames; none in the right rail; smallest type 34 px logical across 2,364 frames and 24,838 text draws; all 8 lines show their source line in y 1335–1440; collisions: 0 over the timeline. |
| Pace | 2 | The 2.5 s change measure has a minimum of 0.315%, median 1.658%; the longest static run is 1.53 s; no silence of 1 s or more (one internal pause of 0.73 s); labels appear 0–0.4 s after their words; no sentence under five words. Tanmay's listen cleared S05 and S08. |
| Trailer function | 2 | Name in S02; the exact searchable long-film title in S08 and on the closing card for about 3 s; the long film is the related video to set at upload. |
| **Total** | **12/12** | |

## The 11-point gate (measured on the compiled file)

1 resolution and first frame PASS · 2 ink zones PASS · 3 type size PASS (34 px floor) · 4 figures on screen when spoken PASS · 5 sources in the safe area PASS (8 of 8) · 6 no hard cuts PASS (2.47 vs 3.0) · 7 no static stretch over 3 s PASS · 8 loop-friendly last frame PASS (0.36%) · 9 audio PASS (aac 48 kHz mono, −14.6 LUFS, −2.0 dBTP) · 10 no foreign text PASS (71 strings, none outside the script) · 11 duration PASS (video 78.800 s, audio 78.800 s).

## What the build changed along the way, and why

1. **[recorded] Dead air.** The narration had 0.85–1.0 s between lines; Kokoro's own lead and tail were trimmed so the gap is the promised 0.4 s (silent runs now 0.3–0.6 s).
2. **[recorded] Collisions.** The S01 chips ran into the stack outline; 21 collisions in the moving parts were found by a timeline check and fixed.
3. **[recorded] Off-script words.** Typing partials and a few off-script words ("made", "my", "semis") were found by the vocabulary check and changed; a hard cut at 8.7 s was smoothed; labels that appeared before their word were re-anchored.

## Findings

1. **No defects open.**
2. **Optional:** ticker symbols on screen, each time labelled "Invented portfolio · scenario arithmetic, not a prediction"; the alternative is "chip stock A / B / C".
3. **At upload:** set the long film as the related video; put the synthetic-voice disclosure in the description.

## What works

- One continuous scene; the blocks land on their words and the arithmetic types in term by term, so the sum can be followed with the sound off.
- It loops: the ending is the opening object, now explained.
- Nothing in it reads negatively; the README's sum is credited on screen.

## Do next

1. Captions and the YouTube metadata (long film and Short).
2. Stage the final folder (flat, with masters and a MANIFEST).
