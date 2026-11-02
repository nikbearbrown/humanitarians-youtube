# Feedback: "The Rally Has a Clock" — Short (9:16), compiled file review 1

**File:** `short/the-rally-has-a-clock-short.mp4`, 2160 x 3840, 30 fps, 79.0 s, h264 + aac 48 kHz. Scene: `short/build_short.py` (one continuous scene as a function of time); audio: `short/make_audio_short.py`; gate: `short/proof_short.py`.
**Verdict:** **12/12 on the Shorts rubric, production gate 12/12 (the 11 checks plus the 1.5 s comparison hold) measured on the compiled file.** Clear-for-public subject to your watch-through.

## The gate on the compiled file
| # | Check | Result |
|---|---|---|
| 1 | 2160 x 3840, 30 fps | 2,370 frames |
| 2 | Safe area, every 0.25 s | ink from 13.3% to 73.7% of the height; right-rail pixels 0 |
| 3 | Type size | smallest 34 px at 1080 wide (sizes 34, 36, 40, 54, 104) |
| 4 | Every spoken figure on screen when spoken | 11 moments checked (shot six counter, 5% faster, 232.5 px, 286 px, 8.4 px, both ticks, the limits, the payoff, the title, the presenter) |
| 4b | Comparisons held at least 1.5 s | two bars together 7.4 s; ticks on shot six 5.4 s; title 3.8 s |
| 5 | Sources inside the safe area | 5/5 phases (essay credit, "Our simulation: 858 x 525, paddle 60, +5%/shot") |
| 6 | No hard cuts | largest frame-to-frame change 2.37 grey levels |
| 7 | No static stretch over 3 s (at 540 x 960) | longest 2.57 s |
| 8 | Loop-friendly last frame | first vs last frame: 0.01 grey levels |
| 9 | Audio | aac 48 kHz mono; -14.6 LUFS; -1.9 dBTP; longest silence 0.92 s (the 0.8 s pauses plus the voice's own tails) |
| 10 | No foreign identity | no handles in the script or scene code |
| 11 | Duration and first frame | 79.0 s; first frame has content |

## What the gate caught and what changed (each fixed, then re-measured)
1. **Check 4 was a test bug, not a picture bug:** the payoff caption wraps onto two drawn lines and the test looked for one string. Fixed the test to join wrapped lines; the caption was on screen.
2. **Check 7, three real failures:** the ending sat still for 5.8 s (the title appeared and nothing moved until the dissolve), then a 5.0 s stretch in S07, then a 3.2 s stretch at the start of S07. Fixes: the rally resumes in S08 and the scene settles back to frame one; the no-speed-up dots land one by one ("shot after shot, no break"); the two limits ("NO SPIN", "NO REAL MACHINE") land on their words.
3. **Check 9:** true peak was -1.4 dBTP against the -1.5 target (the AAC encode adds about 0.5 dB). The normaliser now aims at -2.0 dBTP; the Short measures -1.9, and the long film's recompile measures -14.6 LUFS / -1.9 dBFS.
4. **Earlier, on frames:** the counter overlapped the bars label; the counter read 5 when the bars appeared; the "shot six" caption fired while the counter was at 4; the 8.4 px gap vanished after shot six. All anchored now to word times from the audio.

## Rubric (Shorts)
| Criterion | Score | Reason |
|---|---|---|
| Hook | 2 | The bet starts at 0.3 s; the rally is moving and the headline is up on frame one. |
| Standalone context | 2 | Pong, the essay's claim, why a model and who built it come before the count. |
| One arc with its own ending | 2 | One scene, never cut; the bet is answered in S07; the end settles back to frame one (loop gate 0.01). |
| Phone legibility | 2 | Measured: safe band, no right rail, 34 px minimum, muted-readable headline per phase. |
| Pace | 2 | No static stretch over 3 s at 540 x 960; 3.0 words per second overall; pauses under 1 s. |
| Trailer function | 2 | Closes on the long film's exact searchable title, with its quotation marks on screen. |
| **Total** | **12/12** | |

## Needs your eyes and ears
1. Whether it feels rushed (measured 3.0 words per second overall, like Week 28's approved Short; the count-off and S06 are the dense places).
2. S02's "and I wanted to know" has a weak "and" in the voice; listen once.
3. The count walk in S04 and S06 (the counter runs 1 to 5 and 1 to 6 twice more); is the repetition useful or too much?
