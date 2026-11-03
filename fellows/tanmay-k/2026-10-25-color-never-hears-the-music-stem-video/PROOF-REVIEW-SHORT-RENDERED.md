# Feedback: "The Sky Switch" — Short (9:16), rendered beats, review 4

**Rubric:** the Shorts-specific rubric (hook, standalone context, one arc with its own ending, phone legibility, pace, trailer function; 0–2 each, /12). Not the long film's rubric.
**Reviewed:** the 23 rendered 2160×3840 stills (`short/_stills/`, strip box moved down 50 px at your request), the mixed audio (`short/mp3/short.mix.wav`, 75.55 s) and measured checks from `proof_check_beats.py` (log `_proof_check.log`). **No video exists yet**, so motion and the 11-point compiled-file gate are not measured.
**Prior reviews:** `PROOF-REVIEW-SHORT-1.md` (10/12), `PROOF-REVIEW-SHORT-2.md` (12/12 on draft 2), the script review of draft 3 (12/12).
**Verdict: 12/12 on the rendered beats and audio**, after Tanmay's listen (2026-10-25: "Audio looks good"). It was 11/12 on measurement alone, because the voice runs at 3.1–3.8 words per second; the ear check cleared it. **Provisional on the video:** the 11-point compiled-file gate has not run, so the score is for stills and audio, not for the encode.

## Rubric

| Criterion | Score | Reason (measured) |
|---|---|---|
| Hook | 2 | S01 starts the question at 0.0 s; the grey sky and the clouds move from the first frame; the headline "Which sky goes with which?" is up from frame one (S01-a). |
| Standalone context | 2 | The stills carry both tunes' labels (A: quick, bright / B: slow, low), the two skies, the study's labels (composers, 97 listeners, two countries), the strip with the paper's two scales, a concrete example (Bach / Brahms), the swap, the limit and the title. |
| One arc with its own ending | 2 | One scene, never cut. The last frame (S08-d) eases the sky back to the opening grey; it differs from frame 0 in 3.6% of pixels, all cloud positions. Loop-friendly. |
| Phone legibility | 2 | Pixel check on all 23 stills: **no ink outside the safe box** (x 60–900, y 230–1440 logical) and **none in the right rail**. The 1–2 px "outside" readings are the card's edge exactly on the boundary (S08-b/c, 435 px in a 1-px column at x = 1800) and anti-aliasing (S03, 2 px); neither is a violation. All text ≥ 34 px logical (builder asserts), strip dots 24 px, contrast ≥ 4.5 (INK_SOFT 4.73, SPARK_TEXT 4.70, white on the blue-grey sky 4.70). |
| Pace | **2** | Visual pace passes: a visible change in every 2.5-s window, minimum frame-change 0.575% (at 40.0 s), no window under 0.3%; no silent run of 1 s or more in the audio (the tune bed runs under every gap). **But the voice is fast: 3.1–3.8 words per second within lines** (S08 3.79, S01 3.51, S04 3.47, S06 3.36), not the 2.4 the script planned. The plan divided words by the line budgets, which include gaps; the voice itself runs at Kokoro's natural 3.5 wps. You asked that the Short not feel rushed, so this was held at 1 until you listened; you listened and approved the audio, so it stands at 2. The measured rate stays on record: the voice is brisk, and it is your ear, not the plan's 2.4, that clears it. |
| Trailer function | 2 | The name is in S02 (inside the answer); the exact searchable long-film title is in S08 (spoken once and shown on the closing card for about 2.9 s); the related video is set at upload. |
| **Total** | **12/12** | provisional on the video gate |

## Findings and punch list

1. **Voice rate: resolved by ear.** Tanmay listened to the mix and approved it, so the Short stays at Kokoro speed 1.0 (75.55 s); no re-synthesis. If the encoded video later feels fast against the picture, the lever is `speed` about 0.92.
2. **[EDIT] Lower third of the frame is empty** in S01–S03 (below the source line) and below the strip in S04–S07. It is inside the unsafe zone for a Short (the app's captions and buttons live there), so this is by design, but the composition reads top-heavy. Optional: lower the landscape or enlarge the strip.
3. **[EDIT] S02–S03 strip hint** is a pale, unlabelled card. Either label it faintly (HAPPY/SAD) or hold it off until S04.
4. **Checked and fine:** S01 swatches read "1 blue-grey, 2 yellow" (the order does not give away the answer). The S05 stills say "happy" and "sad" ends only, matching the paper's words ("happy, energetic", "sad").
5. **Not yet measured (needs video):** the whole 11-point compiled-file gate (4K portrait encode, no hard cuts, loudness on the master, 48 kHz audio, frame-0 fade pops, loop last frame in motion).

## What works

- One continuous scene reads as one idea per line, with the headline carrying the argument for muted viewers.
- The paper's own example (Bach, Brahms) gives the claim a picture before the swap.
- The limit is in the Short, not just the long film.

## Do next

1. [EDIT, optional] Findings 2–3 (top-heavy composition, unlabelled strip hint).
3. Encode to video and run the 11-point gate (`short/proof_short.py` pattern from Week 27).
