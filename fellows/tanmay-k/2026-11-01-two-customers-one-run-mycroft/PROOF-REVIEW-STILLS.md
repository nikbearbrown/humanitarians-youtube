# PROOF review 2: rendered stills (long: 15 slates, Short: 11 frames)

Machine checks: `proof_stills.py`, 23 checks and 0 failures at the final render. It confirms one slate per narration beat (15 and 11); text inside the page margins;
nothing under minimum size (24 on the long film, 32 on the Short); every number on screen is in FACTCHECK.md; no banned phrase ("Week 29", minutes, meeting);
content clear of its box header and box edge; the narrated figures (twelve, eleven, d06 reason, YES/NO, "0 of 4 triggered", DRAFT, 0.3.1, PR 81 and 82) are on the slate that carries them.

## Found and fixed in this review
| # | Finding | Fix |
|---|---|---|
| 1 | Short frames used 24-point secondary text, too small at phone width | minimum 32 on every Short frame |
| 2 | Short content sat in the top half, lower third empty on S0 to S8 | content centred lower (110 px), motion phase will use the rest |
| 3 | checker false positives (row numbers, ids, timestamps) | checker reads ids and timestamps as such, not as figures |

## Beat by beat (narration matches slate)
| Beat | On screen | Source |
|---|---|---|
| B00 / Sm1 | title card with name and "for Humanitarians AI" (no week number) | your note |
| B00b | 12 as a field and as a sentence | log `records_seen`, report Run summary |
| B01 | six real step names; 1,3,5 built earlier; 4,6 this time; 2 next piece | report Steps table |
| B02 / S1 | two readers; SNICKERDOODLE principle five | constitution |
| B03 / S2 | 16 field names, five lit | log keys |
| B04 / S3 | reader and decision verbatim, 15 section names | report |
| B05 | 12, 12, 11, 1 | report Run summary |
| B06 | d06 reason in log and report, word for word | defective log and report |
| B07 / S5 | seven gate rows; YES, NO, YES; flipped set; "sample mode only" | clean and defective report |
| B08 / S6 | `"triggered": true` and no stop-condition line (pull request 81 state) | 9684f46 |
| B09 / S6 | `"triggered": false`, "0 of 4", 30 of 30 | main |
| B10 / S4 | same files to two pages; the two real commands | README-steps-4-and-6 |
| B11 / S7 | three questions | script |
| B12 | DRAFT, todos 3, 0.3.1, PR 81 and 82 | recipe, report |
| B13 / S9 | sign-off | script |

## Carry into the motion phase (not defects in stills)
1. The Short is eleven stills now; the motion build makes it one continuous scene (cards travel, the lit fact moves between pages) with no static stretch over about three seconds.
2. B08 is the pull-request-81 log (the committed version at that time), excerpted with "..." where text is elided; keep that caption on screen when it animates.
3. Long frames with a lot of white (B01, B10, B11) can carry a slow highlight that follows the narration.
4. I looked at every slate at preview size after the last change; please look at full size for anything my previews would not show.

## Scores (rubric: six criteria out of two, plus the production gate)
There are two films (long 16:9 and Short 9:16), not three.
| Criterion | Long | Short |
|---|---|---|
| Purpose: one actionable takeaway shown | 2 | 2 |
| Accuracy: every on-screen figure and quote traced | 2 | 2 |
| Structure: its own shape, one fact through two desks | 2 | 2 |
| Tone: positive, humble | 2 | 2 |
| Clarity: one idea per slate, readable size, balanced layout | 2 | 2 |
| Distinctness from W24 to W28 | 2 | 2 |
| **Total** | **12 of 12** | **12 of 12** |
Production gate at the stills stage: pass (proof_stills.py 23 checks, 0 failures). Short content is now centred on the page (a follow-up pass, after the table above).
Remaining for later phases, not scored here: motion (Short as one continuous scene), loudness near -24 LUFS, 4K masters, Whisper check of numbers.

## Update after the motion build
The Short frames reviewed above were laid out across the whole page. Measuring the compiled file against the Shorts safe-area rule (ink 12% to 75% of the height, nothing in the right-hand strip) showed they did not fit, so every Short frame was redrawn inside that zone (type kept at 32 px or more at 1080 wide); see `MOTION-CHECK.md` and `MOTION-GATE.txt` for the measured result (Short 10 of 10, long 8 of 8).
