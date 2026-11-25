# Frictional Log — reading-a-twentieth-of-a-pixel (Week 31 topic video, long and Short)

**Record provenance:** drafted 2026-11-17 with Claude from this folder's records and the session's own measurements, after the work was done rather than while it happened. **Reviewed by Tanmay.** Every entry points at the record it comes from.

## 2026-11-16 — A topic filter that ran out of topics, and a rejected first draw
- **Work and expectation:** draw a topic that no fellow (including us) has covered, from the `claude-for-*` folders.
- **Where it resisted:** the first, stricter filter (a name must appear once in the whole library) left no candidates. The relaxed rule (no fellow folder or our own notes use it) gave 264. The first draw, `stationary-phase`, was then rejected by Tanmay.
- **What was done:** a redraw landed on `galaxy-doppler`; the draws and checks are in `TOPIC-DECISION.md`.

## 2026-11-16 — A wrong number caught by arithmetic, not by the film
- **Work and expectation:** state how far Andromeda's light is shifted at H-alpha.
- **Where it resisted:** the first draft said 0.24 nm. From 300 km/s and 656.28 nm the shift is 300 / 299,792 x 656.28 = **0.66 nm**, thirteen of our pixels. Caught while fact-checking, before any narration was recorded (`FACTCHECK.md`, `ANGLE.md`).
- **Similar:** "about four and a half" (B05, B07) was corrected to the measured "four point six".

## 2026-11-16 — Four places where the picture lagged the words
- **Where it resisted:** reading the rendered stills against the signed narration found B02 never named Andromeda, B04 compared a two-sided error bracket with a one-sided pixel width, B08 did not say what the minus sign means, and S01 showed "away" but not "toward".
- **What was done:** each was fixed and re-rendered before the score was recorded (`PROOF-REVIEW.md`).

## 2026-11-16 to 17 — Measuring the motion changed the answer three times
- Codec noise was first read as motion (a 122-pixel change on one keyframe); the change threshold was set above it. With the stricter threshold a caption the plan listed for S04 turned out never to have been drawn.
- Tanmay asked that no beat sit still for much more than 5 s unless an animation needs it: B00 8.7 s, B09 8.9 s and B06 7.1 s became steps tied to the narration.
- The preview passed but the compiled 4K file, decoded at quarter size, showed two faint dashed lines (B01, S02) that disappear at that size, so those stretches were longer than the preview said. Making the lines brighter fixed it. Lesson: the gate runs on the compiled file.

## 2026-11-17 — The name was mispronounced, and the respelling that was meant to fix it
- Tanmay: it is said "Cool-car-knee". The earlier respelling `kul-KAR-nee`, carried from earlier weeks, came out of Kokoro's tokenizer as the letters "kay-ay" (phonemes `kˈʌlkˌeɪˌeɪˈɑːɹnˈiː`); `Cool-car-knee` gives `kˈuːlkˈɑːɹnˈiː`. Both films were re-synthesized (only B01 and S02 changed, by under a quarter of a second), the plan rebound, and everything recompiled and re-measured; Whisper now hears "Kulkarni" in both.

## 2026-11-17 — Audio shorter than the estimate
- Kokoro ran at 3.47 words per second (long) and 3.28 (Short), shorter than the planned 226 s and 125 s (209.8 s and 104.4 s). The plan was rescaled to the real speech and every voiced figure pinned to its Whisper word time; one new still stretch (B11, 5.3 s) appeared and was fixed.
- B06 is the densest beat (about 4.0 words per second). Tanmay's call after the previews: keep as is.
