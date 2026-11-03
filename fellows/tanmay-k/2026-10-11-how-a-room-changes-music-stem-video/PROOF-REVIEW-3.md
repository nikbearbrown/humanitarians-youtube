# Feedback 3: the compiled masters — Tanmay Kulkarni, Week 26 topic film

**Stage:** final files (2026-10-10).
- **Long:** `how-a-room-changes-music-final.mp4`, 3840×2160, 6:19.
- **Short:** `short/how-a-room-changes-music-short-final.mp4`, 2160×3840, 1:50.

**Method:** every frame reviewed here comes out of the compiled master, not a component render or
a still (BEATS.md #18). `assertion_frames.py` pulls one frame at each timed reveal, plus one at the
moment each quote or figure is *spoken* (`cue_align.spoken_at` + 0.7 s), plus a steady-state
frame: 61 frames (long), 27 (Short), in `_qc/assertion-long/` and `short/_qc/assertion-short/`.
Beat starts come from the paced clips themselves; the reconstructed timeline matches both files
(379.2 s / 379.2 s; 109.5 s / 109.6 s), so the frames sit at the real moments.

**Verdict:**
- **Long: production gate PASS, teaching 12/12.** Clear for public **once the three
  VERIFY-BOOK rows (FACTCHECK A1, A5, A18) are checked against the book**. Until then the film
  shows its sources, but three of them haven't been read first-hand, and the film's own rule is
  no source, no verdict.
- **Short: production gate PASS, teaching 8/12** (meets the ship bar as a trailer). Same
  book-check condition, because S02 carries A1.

## Production gate, on the masters

| Check | Long | Short |
|---|---|---|
| **Evidence legible at the moment of assertion** | **PASS.** At the spoken moment: B05 "mush in a Gothic cathedral", B06 "didn't sound all that great", B07 1752, B09 the dry side drawing in on "In the driest halls" and 74% on "seventy-four percent", B11 8.73% beside 74.36% and "very individual", B12 both studies, B14 2003, B15 1925 / 78 rpm / three minutes, B16 303, 1986–2015, 20 s → 5 s and the AFP quote. Framework (B04) and test (B13) legible | **PASS.** S02 Byrne's claim, S03 2015 (source line) and Quantz 1752 (caption), S04 the dry side and 74% on their words, S05 his words vs the researchers' reading, S08 the pointer's cases in the caption |
| **Sources on screen, not just voiced** | **PASS.** Every external-claim frame shows its source; our own material carries its label in the master ("Simulated echo… Not a measured room", "Shape only…", "Our test", "Our listening heuristic, not a measurement") | **PASS** |
| **Side-by-side at the moment of comparison** | **PASS.** B10, B11, B23 | **PASS.** S05, SD3/S08 (both passes held) |
| **Toolkit Gate V** (frame-level, full master) | PASS at compile | PASS at compile (0 BLOCKER, 0 MAJOR) |
| **Shorts UI zones** | n/a | **PASS.** Portrait pixel gate 11/11; Gate V's 9:16 safe area clean |

## Audio, on the masters

| Check | Long | Short |
|---|---|---|
| Loudness (ebur128, independent) | −14.7 LUFS integrated | −14.8 LUFS |
| True peak (normalise.py) | −1.9 dBTP | −1.9 dBTP |
| Silences ≥ 1 s | **exactly two**: 2.64 s at 320.9 s (end of B18) and 4.16 s at 331.1 s (end of B19), the clap task's holds | **none** |
| Sample rate / codec | 48 kHz AAC | 48 kHz AAC |
| Spoken words vs signed script | Whisper small.en ≥ 0.925 per beat (names aside) | ≥ 0.955 |

## Rubric

**Long: 12/12** (unchanged from review 2, now confirmed on the master). The task's holds exist in
the shipped file at the right places, which was review 1's open condition for the active-task
score.

**Short: 8/12**, scored honestly as a film rather than waved through as a trailer:

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 1 | Demonstrated in the cold open; the asks → hears → answer graphic comes at S05, after the example |
| Reusable rubric | 1 | The three stations appear once, applied to the cellist; the decide/ask test is in the long film only |
| Worked example | 2 | The cellist, wet side, then dry side |
| Falsifiability / edge | 2 | The dry hall breaks the simple "echo → slower" story |
| Active task | 0 | None by design: the Short points to the full film, which carries the task |
| Friction | 2 | Why slow down in a dry room? Resolved in S05, attribution kept apart |

## The problem

None in the films themselves. **The one open item is outside the pixels:** FACTCHECK A1 (Byrne's
chapter-1 argument), A5 (CBGB: very little echo) and A18 (Edison's cylinders) are still sourced
from reviews and summaries of the book, not the book itself. A5 is the one most at risk: one
online summary garbles it.

## Do X next

1. **[NEW SOURCE] Check A1, A5, A18 against *How Music Works*.** If one fails, only that beat's
   audio, render and compile change (B05/B06/B15, S02). Everything else is fixed.
2. **[NEW SOURCE]** Read the 20 s → 5 s intro figures in Léveillé Gauvin (2018) itself (A20), or
   keep the Ohio State citation that's on screen now.
3. **[EDIT]** Captions (`.srt`/`.vtt`) for both cuts, from the signed narration and the measured
   timeline. A Short without captions is unwatchable muted (BEATS.md #21).
4. **[RECORD]** Both masters sit 0.7–0.8 LU under −14 LUFS (the linear loudnorm is capped by the
   −2 dBTP ceiling). YouTube only turns loud uploads down, so these play marginally quieter.
   Accepted and logged.

## What works

- **Every claim is on screen when it's said, in the file that ships**, not just in the stills.
  The reveals moved onto the measured audio clock and it shows: the 74% lands on "seventy-four".
- **The honesty labels survived into the masters** in both aspects.
- **The task's silences exist in the audio**, measured where they should be, and nowhere else is
  there dead air.
- **The Short stands on its own:** name at both ends, Byrne introduced, the study set up before
  its result, and its own payoff heard.
