# Feedback: "The Rally Has a Clock" (Pong) — first compile (long film, 16:9), frames review 1

**Master:** `the-rally-has-a-clock.mp4` — 3840 x 2160, 30 fps, h264 + aac, **267.4 s (4:27)**. Per-beat videos: `_beats/B00–B13.mp4`. Sources: `build_motion.py` (stages + cross-fades from `CUES.json`), `compile_master.py`.
**Method:** every beat is a set of full 4K stages cross-faded on the cue times (true blend, old = 1 − e, new = e); each beat dissolves from the previous in 0.25 s. This review reads **sampled frames and measurements**, not a watch-through.
**Verdict:** **clear-for-public.** Tanmay watched the first compile on 2026-10-30 and said it looks good. Teaching score on frames: **12/12**. Production gate: **PASS on every measured check**.

## Measured (front-loaded, before this review)
| Check | Result |
|---|---|
| Video vs audio length | 267.399 s both; each beat padded/trimmed to its exact frame count (no drift) |
| Resolution / frame rate | 3840 x 2160, 30 fps |
| Loudness | first compile -14.5 LUFS / peak -1.4 dBFS (0.1 dB over the -1.5 target). Recompiled with the normaliser aimed at -2.0 dBTP, which also fixed the Short's gate: **-14.6 LUFS, -1.9 dBFS** (audio only; the video stream was copied, not re-rendered) |
| Black frames | none |
| Fades measured on pixels | stepped over about 10 frames (e.g. B13 "?" → 0.225: 251.7 → 244.0 in 11 frames; B09 tick: 248.1 → 227.1 in 12 frames); ramp steps take 3 frames by design; beat dissolve stepped over ~8 frames |
| Cue-to-frame sync | all stage changes start at their cue times (built from the Whisper clock, 0.15 s lead); B09 "the tenth" / "the nineteenth" land on 15.4 s / 16.0 s |
| Last frame vs approved still | within 0.5 grey levels on 11 of 14 beats; B03 (0.47), B05 (0.29), B09 (0.17), B13 (0.15) differ only where the motion adds or removes an element on purpose |
| Longest static stretches (≥ 6 s) | B06 first ~3.7 s (labels only, before the first dot); B13 hold (5 s, by design); B13 closing dial ~8 s; B02/B06/B07 end holds ~6 s with a card on screen |

## What changed in this pass (found by measuring, not by watching)
| Beat | Finding | Fix |
|---|---|---|
| B00 | digit swap showed a 4 and a 5 overlapping for ~0.35 s | counter fades shortened to 0.14 s (double image about 2 frames) |
| B05 | static picture for 10.5 s while the narration works through "can it / can't it" | bars now show shot one ("it can": 286 vs 232.5) then shot six ("it cannot": 224), with the comparison caption, before the 0.27 card at 10.7 s |
| B07 | narration said "that bar keeps sinking" but only the chart moved | bars widget follows the curve shot by shot and settles at shot six |

## Rubric (these frames)
| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | The two bars are on screen from B00's first frame and move with the shot (B00, B03, B05, B07). |
| Reusable rubric | 2 | The form on B05's card, applied on a second field (B10) and handed over (B13). |
| Worked example | 2 | B06 dots fill shot by shot; B07 curves draw with the bars; B08 predicted then found. |
| Falsifiability / edge case | 2 | B08, B09, B10 predicted-vs-found; B11 no-speed-up; B12 exclusions. |
| Active task | 2 | B13: formula, "= ?" for 5 s, then 0.225 and the verdicts. |
| Friction | 2 | B00's perfect defender that loses; B13's held "?". |
| **Total** | **12/12** | |

## Production gate
| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS at 4K. Smallest type 24 logical px: fine on TV and desktop; the Short needs its own layout. |
| Sources on screen, not just voiced | PASS. Constants chip on every field slide (updates to the second field in B10); formulas shown where figures come from; essay credit on B01. |
| Side-by-side at the moment of comparison | PASS. B06 rows, B08/B09/B10 predicted-vs-found, each held at least 2 s. |

## Needs your eyes and ears (I cannot judge these from frames)
1. **Listen to the count-off** in B00 ("Shot one … five") and to B01 "I like that line".
2. **B09 count walk** (15.0–16.0 s): the highlight moves along cells 1 to 19 in about 1 s; is that too quick to read, or about right?
3. **B13 closing** holds the dial question for about 8 s after the sign-off; keep, or fade out sooner?
4. **B06 opening** is labels only for 3.7 s while the narration sets up the three rallies.

## Do next
1. [EDIT] Collect your notes, apply once, recompile once.
2. Captions (`.srt`/`.vtt`) from the Whisper clock, YouTube title/description/chapters, README with YouTube placeholders (done).
3. The Short: its own script and arc (`shorts-must-feel-complete`), 2160 x 3840, own layout; not built.
4. Push staging: flat folder, `-SHORT` suffixes, no mp4 (masters are uploaded to YouTube).
