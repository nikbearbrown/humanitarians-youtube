# Feedback: "Minus Seventy-Eight" — Short (9:16), rendered beats, review 3

**Rubric:** the Shorts-specific rubric (hook, standalone context, one arc with its own ending, phone legibility, pace, trailer function; 0–2 each, /12). Not the long film's rubric.
**Reviewed:** the 20 rendered 2160×3840 stills (`short/_stills/`, after the chip fix and the larger bars), the narration track (`short/mp3/narration.wav`, `am_onyx`, re-generated with trimmed silence), Whisper's check, and measured checks (pixel check, collision check, 2.5 s change measure). **No video exists yet**, so the 11-point compiled-file gate is not measured.
**Prior reviews:** `PROOF-REVIEW-SHORT-1.md` (draft 1), `PROOF-REVIEW-SHORT.md` (draft 2 script, 12/12). **Gate P:** passed 2026-10-25 (`short/GATE-P-SIGNOFF-SHORT.md`).
**Verdict: 11/12.** One criterion holds at 1/2 until you have listened: the pace of two brisk lines (below). Everything else passes on measurement.

## Rubric

| Criterion | Score | Reason (measured or viewed) |
|---|---|---|
| Hook | 2 | S01-a: the number "−78%" at full size with the question "Where does −78% come from?" from frame one; the first spoken words state it; the first block drifts into the empty stack outline at 0 s. |
| Standalone context | 2 | S01 says what a stress test says and about what; S02 who made it and what Mycroft is; S03 defines a scenario as a short list of named shocks and shows the four; S04–S06 the sum; S07 the check; S08 the question and the title. A viewer who never sees the long film has the whole idea. |
| One arc with its own ending | 2 | One scene, never cut: the number, its list, the first bar, the other two, the shares, the check, and the number returning at full size with its parts under it. The last frame (S08-d) differs from frame 0 in 0.32% of pixels. |
| Phone legibility | 2 | Pixel check on all 20 stills: **0 flagged**, nothing outside the safe box (x 60–900, y 230–1440) and none in the right rail; type ≥ 34 px; bars ≥ 112 px tall with 52 px numerals; the running total 150 px. **Collisions: 0** in the stills and 0 over 315 timeline samples (21 collisions found in the moving parts and fixed; the S01 chip overlap you spotted is among them). |
| Pace | **1** | Visual pace passes: the 2.5 s change measure has a minimum of 0.321%, median 1.666%, **no window under 0.3%** (measured on scene frames); no sentence under five words. **Silence: found and fixed in this review.** The first narration track had 0.85–1.0 s of dead air between every line (Kokoro's own lead and tail, plus the 0.35 s gap); with no music bed that breaks the "no silence of 1 s or more" rule and the script's promised 0.4 s. After trimming, silent runs are 0.3–0.6 s (the longest, 0.6 s, is a pause inside S03). **Held at 1:** two lines read fast, S05 (3.87 words per second) and S08 (3.95); the others run 2.76–3.30. You asked that the Short not feel rushed, so I hold this at 1 until you listen. |
| Trailer function | 2 | The name is in S02, inside the answer; the exact searchable long-film title is in S08 and on the closing card for about 3 s; the long film is the related video to set at upload. |
| **Total** | **11/12** | |

## Audio (measured)

| Measure | Result |
|---|---|
| Track / narration | 78.8 s / 78.0 s (was 82.4 / 81.6 s before the silence was trimmed) |
| Silent runs ≥ 0.3 s | 0.3–0.6 s, none at or above 1 s (before: eight runs of 0.85–1.0 s) |
| Words per second by line | S01 3.30 · S02 2.76 · S03 2.91 · S04 3.29 · **S05 3.87** · S06 3.12 · S07 3.25 · **S08 3.95** |
| Whisper vs the signed text | 0.932; differences are numerals only ("78 %" for "seventy-eight percent"); "Mycroft", "Tanmay Kulkarni" and the closing title were heard correctly |

## Findings

1. **[EDIT, applied] Dead air between lines.** Fixed by trimming Kokoro's own lead and tail silence and setting the gap to the promised 0.4 s. The narration text is unchanged, so your Gate P read stands. The old track is kept as `narration-v1-untrimmed.wav`.
2. **[EDIT, applied] Chips ran into the stack outline** (S01 and the loop frame). The chips now sit on two rows under the number; 21 timeline collisions were found and fixed with a new overlap check.
3. **Pace, for your listen:** S05 ("A second chip stock gets the same ninety. The third is off the AI list, so it gets fifty, and that is a different sum.") and S08 (the closing line with the film's title) are the brisk ones. If they feel fast, the lever is a slower Kokoro speed on those two lines only (about 0.9).
4. **Optional:** ticker symbols on screen, labelled "Invented portfolio · scenario arithmetic, not a prediction"; the alternative is "chip stock A / B / C".
5. **Not yet measured (needs video):** the 11-point compiled-file gate (4K portrait, ink zones, type size, figures on screen when spoken, no hard cuts, loop frame, loudness, duration) and the retimed schedule's fit to the video.

## What works

- One scene, one idea per line; the opening number is the object that is explained and then returned.
- The blocks land on their words and the arithmetic types in term by term, so the sum can be followed with the sound off.
- The README's sum is credited on screen; nothing in the Short reads negatively.

## Do next

1. Listen to the Short's narration (attached) and say whether S05 and S08 need slowing.
2. Encode to video and run the 11-point gate; re-run this review on the video.
3. Captions and the YouTube metadata.
