# Feedback: "The Sum Behind the Number" — long film (16:9), video review 3

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** the compiled video `the-sum-behind-the-number.mp4` (3840×2160, 30 fps, 208.4 s, `am_onyx`), the 11 beat clips (`_beats/`), the measured gate (`VIDEO-GATE-LONG.md`, `measure_long_video.py`), the low-resolution pre-checks over all 6,253 frames, and frames I extracted from the beats myself (B01, B03, B04, B05, B06, B07, B08, B10) as well as the nine the agent viewed. Tanmay approved every beat's stills and the audio before the render.
**Prior reviews:** `PROOF-REVIEW.md` (script, 12/12), `PROOF-REVIEW-RENDERED.md` (stills and audio, 12/12).
**Verdict: clear-for-public.** Teaching **12/12**. Production gate **PASS, measured on the video**. The film passes its own standard: every claim carries a visible source or a visible artifact. The conditions under Do next do not block.
One line: this film attempts to teach that a stress-test percentage is a sum of named shocks, and delivers it by rebuilding the workflow's own number block by block, on the word, with every term traceable to a committed file.

## Where it improved vs the stills review

| Item | Stills review | Video |
|---|---|---|
| Hold times | not measurable | **measured:** B03's guess on screen 5.38 s, B05's three bars 8.53 s, B06's four bars 6.03 s, B07's columns and counter 4.63 s (all ≥ 3 s); B05's total 2.7 s (all the narration leaves after "seventy-eight"; ≥ 2 s) |
| Timing against the words | planned | **measured at 960×540 over every frame:** 253 cues, 0 early, 0 late (≤ 0.45 s after the word) |
| Collisions | 0 in stills | **0 hard collisions and 0 gaps under 12 px over every frame of every beat** |
| Black frames, loudness, sync | not measurable | none (lowest frame luminance 235.5); master −14.7 LUFS, −1.9 dBTP; video and audio within 0.001 s per beat, 0.007 s on the master |

## Rubric (on the video)

| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | The headline number and the empty stack outline "made of: ?" are on screen from the opening; B03 states the rule on the scenario card before the first worked example. |
| Reusable rubric | 2 | B10 reveals the three questions one per phrase over the opening number and holds "A good answer names the terms." for the closing 2 s. |
| Worked example | 2 | B04: blocks land on "fifteen", "thirty-five", "forty", the number fading in after each block grows; B05: three bars on their sentences, the arithmetic typed term by term; B06 repeats the rule with the technology block ringed where the narration says it lands. |
| Falsifiability / edge case | 2 | B05's third holding is a different sum; B06's fourth holding takes a third block; B04's README card notes another way to combine; B08 accepts weight totals 0.6 and 1.2 and rescales them. The weakest of the six. |
| Active task | 2 | B03 holds the guess (5.38 s with the empty bar); B10 hands over the three questions with their standard. |
| Friction | 2 | The opening question and the guess before the answer. |
| **Total** | **12/12** | |

## Production gate (measured)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS.** The PROOF still-checks on the last frame of every beat, extracted from the video: 0 flags; lowest ink inside the evidence band; margins ≥ 60 px; type ≥ 28 px logical over every frame; contrast ≥ 4.5 for small text. Last frames match their approved stills to within 0.12%. |
| Sources on screen, not just voiced | **PASS.** Every beat carries its evidence caption; the figures spoken are on screen at their words (the cue check). |
| Side-by-side at the moment of comparison, held | **PASS (measured)** for B05, B06 and B07 (above). |
| Technical | 3840×2160, 30 fps, H.264, yuv420p, AAC 48 kHz mono, 208.433 s; per-beat durations within 0.001 s of the audio; no black frames; longest static stretch 4.4 s (B03's guess hold, by design); nothing over 6 s. |
| Positive framing (standing instruction) | **PASS.** Nothing negative on screen; "critical" only as the workflow's label; the −90 credited as the README's worked example. |

## The problem

None that blocks release. The film's softest point is the **weakest rubric line, edge cases**: it shows the rule on variations of the same case, not on a case that breaks it. B04's mention that the README names another combining rule is the nearest it comes, and it is deliberate.

## Findings

1. **Deviations from the approved stills, all for timing against the narration:** B07 ends on a merged layout (both columns and the "24 of 24" counter held while the twelve breaks tick); B06 rings the technology block; B05's total is on screen for 2.7 s.
2. **Ticker symbols on screen**, each use labelled "Invented portfolio · tickers from the workflow's own map"; the narration never says one. Optional: "chip stock A / B / C".
3. **B04 reads at 3.92 words per second** (the brisk spot). The video's blocks land on the words, so it follows; if it feels fast on a watch, the lever is Kokoro speed for that beat only.
4. **No captions file for the long film yet**, and no YouTube metadata for either format.
5. **Housekeeping:** the agent deleted its 2.1 GB of temporary frames; the folder is 169 MB.

## What works

- The running total is the argument, and in the video it is also the pacing: each block lands on its word.
- Every number is read from a committed file; the check on my own adder is a result (24 of 24, 12 of 12).
- The close hands the viewer a standard for a good answer.

## Do next

1. [EDIT] Captions (`.srt`, `.vtt`) and the YouTube metadata for the long film and the Short.
2. Stage the final folder (flat, with masters and a MANIFEST), per the Week 26–28 convention.
3. Optional: the ticker labels (finding 2).
