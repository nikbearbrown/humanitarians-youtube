# FACTCHECK — "Use the Tool First."

Every factual claim, its source, its verdict. Verified 2026-09-10.

Claims about work Rohan did are first-hand and marked as such. Every number on
screen was obtained by running something, not by reading the plan document.

| # | Claim | Where | Basis | Verdict |
|---|---|---|---|---|
| 1 | Six Midjourney parts are finished | B00, B01 | all six `.mp4` masters present on disk | **PASS** |
| 2 | All six are 4K | B01 badges, footnote | `ffprobe` → 3840×2160 on all six | **PASS** |
| 3 | Part runtimes 3:20 / 3:16 / 3:02 / 3:23 / 2:59 / 2:56 | B01 cards | `ffprobe` → 200.30 / 196.20 / 182.42 / 203.94 / 179.23 / 176.88 s | **PASS** |
| 4 | Total **18:59** | B01 bar, B04 card, B00 output line | sum = 1138.96s → 18:58.96, rounds to 18:59 | **PASS** — see note below |
| 5 | "nearly nineteen minutes" | B01 narration | 18:59 | **PASS** |
| 6 | **29** screenshots of the interface | B02 narration + title, B03 stat | file count in `Midjourney Screenshots/` = 29 | **PASS** — see discrepancy below |
| 7 | The series was planned from web research before access | B00, B02 narration | Rohan's brief; `MIDJOURNEY-SERIES-PLAN.md` states the scaffolding plan was built on web research | **PASS** — first-hand |
| 8 | Five things in the plan were wrong | B02 rows | `MIDJOURNEY-SERIES-PLAN.md` "What the captures changed" table lists exactly five rows | **PASS** |
| 9 | No Chat section | B02 row 1 | plan table: sections are Explore, Create, Edit, Organize, AESTHETICS, COMMUNITY — no Chat | **PASS** |
| 10 | One row of four, not a 2×2 | B02 row 2 | plan table: "One row of four, with the prompt in a right rail" | **PASS** |
| 11 | A six-row action grid with a hidden menu | B02 row 3 | plan table: "six-row action grid, plus a hidden-by-default menu holding Pan, Zoom and Remix" | **PASS** |
| 12 | Settings are a 2×2 of four cards, twelve controls | B02 row 4 | plan table: "2x2 grid of four cards, twelve controls" | **PASS** |
| 13 | Video is first-class throughout | B02 row 5 | plan table: "Animate is on every hover, Animate Image is in every rail, three of twelve settings are video settings" | **PASS** |
| 14 | Two whole surfaces were missing from the plan | B02 narration | plan: "Two whole surfaces were missing from the plan entirely: Style Creator and video" | **PASS** |
| 15 | **23** new reusable components | B03 count + chips | `Mj*.tsx` file count in `runtime/remotion/src/scenes/` = 23; all 23 named on screen | **PASS** |
| 16 | **863** lines of UI spec | B03 stat | `wc -l MIDJOURNEY-UI-SPEC.md` → 863 | **PASS** |
| 17 | **0** screen recordings | B03 stat, narration | no video captures in the series; every screen is a registered Remotion composition | **PASS** |
| 18 | Each part has its own beat check | B01 footnote, narration | `check_beats.py` present in all six part folders | **PASS** |
| 19 | Each part has its own factcheck | B01 footnote | `FACTCHECK.md` present in all six part folders | **PASS** |
| 20 | Signup documentation is still open | B04 due chip, narration | no such document on disk | **PASS** — correctly labelled open |
| 21 | Both tools together by end of next week | B04 due chip | Rohan's brief — a stated commitment, shown on the dashed side | **PASS** — framed as a commitment |
| 22 | Narration voice is Kokoro `af_bella`, local and free | description.txt | `generate_audio_kokoro.py` reported `cost $0.00` | **PASS** |

## The 18:59 / 18:58 question

`MIDJOURNEY-SERIES-PLAN.md` states **18:58**. The true sum is 1138.96s, which
is 18 minutes 58.96 seconds:

- **truncated** → 18:58 (what the plan document says)
- **rounded** → 18:59 (what the reel says)

The reel rounds, following the convention fixed in the week-02 MP3 reel after a
truncation bug put 10:34 on screen against 10:35 in the docs. Both figures
describe the same measurement; the reel is internally consistent at 18:59 in
all three places it appears, and the narration says "nearly nineteen minutes",
which is true either way.

## The capture-count discrepancy

`MIDJOURNEY-SERIES-PLAN.md` says **"23 captures, all read directly"** in its
header and **"29 captures"** further down — it contradicts itself. The
directory contains **29 files**.

The reel uses 29 because that is what is on disk and countable. The plan
document's header is stale, most likely written when 23 captures existed and
not updated when six more arrived. This is the same class of error as the Suno
runtime figures in week-02: **the planning document drifts, so the reel measures
instead of quoting it.**

## What is first-hand rather than measured

Claims 7, 20 and 21 come from Rohan's own account of the week. They are
presented as his report, not as independently verified fact, and the two
forward-looking items are shown on screen as open or due rather than done.

VERDICT: **PASS** — 22 of 22 claims verified. Two upstream document
inconsistencies found and resolved in favour of what could be measured.
