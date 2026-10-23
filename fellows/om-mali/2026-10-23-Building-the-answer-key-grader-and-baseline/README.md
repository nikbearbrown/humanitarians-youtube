# 2026-10-23 - Building the answer key, grader and baseline

**Week covered:** 2026-10-19 - 2026-10-25

**Video:** [Mycroft_OmMali_23_10_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The AI Debt Tracker is an AI agent, run entirely on a laptop, that reads companies' public
filings to keep an up to date record of every bond and loan owed by 25 AI-sector companies, and
is graded against the debt each company later reports officially.

This week built the tools that will score the agent, before the agent itself exists.

- **An answer key for every report.** 1,093 quarterly and annual reports from 100 companies,
  January 2024 to September 2026, each turned into a list of the bonds and loans it shows.
- **A grader that scores at three levels of detail:** bond by bond, by offering, and on totals,
  each with a confidence range.
- **The grader was checked against the reports themselves.** Compared with the debt tables
  printed in 10 reports, it first agreed on 8. All of the disagreements were bugs in this
  project, not in the companies' data. After fixing them it agreed on all 10, and on 2 of 3
  fresh reports picked in advance. The one remaining cause is recorded for next week.
- **Doing nothing scores high and catches nothing new.** Copying last quarter's debt forward
  gets 90.7% of bonds right, because most debt does not change in a quarter. But it caught
  0 of 36 new bonds. That gap is what the agent has to close.
- **The changes are there to be found.** 30 of 32 new bonds and 5 of 6 early repayments were
  announced in a filing before the report showed them.
- **The test stays fixed.** Frozen test files can no longer be overwritten by accident, and the
  cutoff dates no longer depend on timestamps that moved by 4 to 5 hours on the SEC's own index.

---

## The built reel

Built with `brutalist.art`, skill `ai-explainer`, channel `claude-hai`. Free and local end to
end, `$0.00`.

| | |
|---|---|
| 16:9 master | `Mycroft_OmMali_23_10_2026.mp4` — 3840×2160, 24fps |
| 9:16 master | `vertical/building-the-answer-key-grader-and-baseline-916.mp4` — 2160×3840, same length |
| review cuts | `*-slate.mp4` in each folder — beat IDs and running timecode burned in |
| beats | 12 — 4 bookends, 8 body beats, 0 slates |
| voice | Kokoro `am_onyx`, local, the fellow's persistent voice since week 1 of the earlier series |

**The agent in this video does not exist yet.** Week 2 built the things that will judge it: the
answer key, the grader, and the do-nothing baseline. B02's subtitle says so on the frame,
because a reel full of scores otherwise reads as a reel about a working system.

---

## Figure → beat map

| Beat | Act | Scene (`BuildingTheAnswerKey.tsx`) | Source figure | What it argues |
|---|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | — | *Build what will grade it, before it exists* — lands ANSWERED with the three findings |
| B01 | The answer key | `AKScale` | `adt-w2-answerkey` (top) | 1,093 reports, and they do not all give the same detail |
| B02 | The grader | `AKGrader` | `adt-w2-answerkey` (bottom lines) | The exact rule a bond must satisfy, and the once-only pairing |
| B03 | Checking the checker | `AKBugs` | `adt-w2-handcheck` (bug list) | **Every disagreement was my bug, not theirs** |
| B04 | Calibrated vs measured | `AKCalibration` | `adt-w2-handcheck` (bars) | 10 of 10 is a calibration; 2 of 3 is the score |
| B05 | The floor | `AKFloor` | `adt-w2-headroom` (top bar + stats) | A flattering 90.7% with a zero inside it |
| B06 | The headroom | `AKHeadroom` | `adt-w2-headroom` (red bars) | The distance between doing nothing and reading the filings |
| B07 | One surprise | `AKClock` | — (`logs/RUN_LOG.md`) | The timestamps moved, so the cut-off stopped trusting a clock |
| B08 | The limits | `AKNext` | — (the script's Notes) | Every number above, paired with what narrows it |
| B09 | Verdict | `ClaudeVerdictArtifact` | — | Five findings, one per spoken clause |
| B10 | Handoff | `ClaudeComposerAsk` | — | Check the harness, not the model |
| B11 | Outro | `ClaudeTitleOutro` | — | Title restate |

The three PNGs and their SVG sources in `pantry/` are reference only; every body beat is
rebuilt natively in Remotion (REBUILD LAW) and never slots a PNG as media.

## Four things not to get wrong

1. **The agent is not built.** Week 2 built its judge. FACTCHECK row 5.
2. **10 of 10 is a calibration, not a score.** The same ten printed tables found the five
   grader bugs, so the grader agrees with them by construction. The measurement is 2 of 3 on
   three reports picked before reading and graded once — and three is a small check, said as
   one. FACTCHECK row 12; this is the build's framing assertion.
3. **90.7% is what doing nothing scores**, and it is high for exactly the reason the zero is
   zero: a quarter's debt mostly does not move. The agent is not being asked to beat it.
   FACTCHECK rows 14–15.
4. **30 of 32, not 30 of 36.** Four new bonds carry no tagged interest rate, so there is
   nothing to search a filing for. Both numbers are on the frame. FACTCHECK row 17.

## Three drawings that are the argument

- **B05 is an outlined track held EMPTY**, with the word inside it. A bar of width zero reads
  as "nothing was caught"; an absent bar reads as a rendering fault, which this series has
  shipped before. Never put a bar in it, and never delete the outline.
- **B04's dashed rule** separates the reports that *found* the fixes from the ones that only
  tested them. Merge the three bars into one group and the beat stops arguing.
- **B06 draws a span**, not two bars. The distance between what copying forward catches and
  what the filings announced is the thing being claimed.

## Files

```
beat_sheet.json        the edit — 12 beats, every figure a prop, durations locked to the mp3s
build_beat_sheet.py    writes it from figdata.json, under assertions (--check runs them alone)
figdata.json           the data; nothing on screen is typed by hand
lock_durations.py      writes measured Kokoro durations into durationInSeconds
make_vertical.py       derives vertical/beat_sheet.json and copies the mp3s across
FACTCHECK.md           20 rows; read 5, 8, 9, 12, 14 and 17 first
CHECKS-REPORT.md       PROOF GATE, written before the first compile
PEDAGOGY.md            GATE P — what the author is asked to sign
BUILD-LOG.md           decisions, defects found and fixed, toolkit changes
BUILD-PROMPT.md        the single prompt that rebuilds this reel end to end
description.txt        the long-form description
pantry/                the three source figures — REFERENCE, never slotted as media
_qc/                   GATE V frames and REPORT.md
```
