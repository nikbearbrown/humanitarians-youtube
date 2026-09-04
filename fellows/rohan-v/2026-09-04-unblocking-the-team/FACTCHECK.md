# FACTCHECK — "Unblocking the Team."

Every factual claim the narration or a graphic makes, its source, and its
verdict. Verified 2026-08-29.

Claims about work Rohan personally did are first-hand accounts from his brief;
they are marked as such. Claims with numbers on screen were verified by
execution, not by recollection.

| # | Claim | Where | Source | Verdict |
|---|---|---|---|---|
| 1 | Suno Part 1 runs 3:57 | B02 card | `ffprobe` → 236.55s = 3:56.55 | **PASS** (rounds to 3:57) |
| 2 | Suno Part 2 runs 3:09 | B02 card | `ffprobe` → 188.94s = 3:08.94 | **PASS** |
| 3 | Suno Part 3 runs 3:29 | B02 card | `ffprobe` → 209.21s = 3:29.21 | **PASS** |
| 4 | The three parts total 10:35 | B02 total bar, B04 card | 236.55 + 188.94 + 209.21 = 634.70s = 10:34.70 | **PASS** (rounds to 10:35) |
| 5 | "About ten and a half minutes" | B02 narration | 10:34.7 | **PASS** — hedged with "about", correctly |
| 6 | All three parts are 4K | B02 badges | `ffprobe` → 3840×2160 on all three streams | **PASS** |
| 7 | All three parts are finished | B02 "DONE" chips | `suno-part-{1,2,3}.mp4` all present on disk | **PASS** |
| 8 | Part titles and skills as shown | B02 cards | `lyrical-literacy/SERIES-PLAN.md` series structure table | **PASS** |
| 9 | Suno UI is rebuilt in code, not screen-recorded | B02 footnote + narration | `SERIES-PLAN.md`: "No screenshots — all UI is programmatic Remotion" | **PASS** |
| 10 | The marketing team is non-technical and was blocked at the GitHub step | B01 narration | Rohan's brief, first-hand | **PASS** — first-hand |
| 11 | A workshop was given at the start of the week | B01 narration | Rohan's brief, first-hand | **PASS** — first-hand |
| 12 | The setup was packaged as a video | B01 bridge label | `week-01/2026-08-28-agent-first-brutalist/` exists and shipped in the week-01 packet | **PASS** |
| 13 | A fellow needs four accounts: Discord, Suno, Midjourney, Adobe CC | B03 cards + narration | Rohan's brief, first-hand | **PASS** — first-hand |
| 14 | The signup guide is in progress, not finished | B03 status stamp, B04 due chip | No such document on disk as of 2026-08-29 | **PASS** — correctly labelled in-progress |
| 15 | The Midjourney series is due end of next week | B04 due chip + narration | Rohan's brief — a stated commitment | **PASS** — framed as a commitment, on the dashed side of the NOW pin |
| 16 | Narration voice is Kokoro `af_bella`, local and free | description.txt | Toolkit default; `generate_audio_kokoro.py` reported `cost $0.00` | **PASS** |

## Numbers that were re-derived rather than trusted

The runtimes in B02 were **not** taken from `SERIES-PLAN.md`, which estimates
Part 1 at "~3:30" and Parts 2 and 3 at "~3–4 min". Those were planning targets.
The built masters came out at 3:57 / 3:09 / 3:29, so the reel reports the probed
values. The plan document is stale on this point and the reel does not inherit
its error.

## Tense discipline

Every claim in B02 is past tense and verified. Every claim in B03 and B04 that
is not yet true is marked on screen (`IN PROGRESS`, `END OF NEXT WEEK`) and
sits visually behind the NOW pin in B04. No forward-dated work is stated as
complete.

VERDICT: **PASS** — 16 of 16 claims verified. No corrections required.
