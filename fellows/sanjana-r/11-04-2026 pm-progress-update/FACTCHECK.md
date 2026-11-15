# FACTCHECK — Week of Nov 4 (weekly progress)

Register: Teardown (Liam / Kokoro am_onyx). Stats-only, NO personal names. Numbers aggregated
from the week's task log.

| # | Claim (on screen / narrated) | Status | Basis |
|---|---|---|---|
| 1 | 28 videos reviewed | VERIFIED | 4+4+4+3+2+1+2+2+2+4 = 28 |
| 2 | 24 cleared for approval | VERIFIED | 28 − 4 sent-back = 24 |
| 3 | 4 sent back (not in 4K) | VERIFIED | one creator, two entries of 2 videos = 4, "Needs Modifications" |
| 4 | ~9 creators | VERIFIED | 9 unique people in the log |
| 5 | 4K auto-check built & tested, now live | TRUE | task log items 1 & 2 (AppScript 4K check, working; tested with team) |
| 6 | 2 new reviewers onboarded & trained | TRUE | task log item 3 |
| 7 | 1 video non-standard project name, cleared to upload | TRUE | log comment (name not "Humanitarian AI"; YT final check, OK to upload) |
| 8 | code-on-GitHub tracked per project | VERIFIED | GitHub column recorded per entry |
| 9 | 22 total hours (9 / 6 / 4 / 3 by track) | SELF-REPORTED | allocation across tracks; total ≥ 21h |

Continuity note: the 4K auto-check closes the exact gap flagged in the Week-of-Oct-25 report
("push 4K checks upstream"). The watermark check is noted as not-yet-automated (next week).

On the AppScript evidence (B02B code, B02C log): the real screenshots (the `4KVideoChecker`
Apps Script editor and the `HAI 4K check` log sheet) were provided and are **rebuilt as native
on-brand graphics**, not pasted — per the toolkit's REBUILD LAW and to keep the log sheet's
fellow names out of a public video. The code beat reflects the real logic (reads width/height;
PASS when 3840×2160 or 2160×3840, either orientation; reason string like "3840×2160 — 4K"). The
log beat shows representative rows (real resolutions/durations from the sheet, all PASS, plus one
illustrative FAIL to show what a non-4K row logs). No fellow names appear anywhere in the film.
