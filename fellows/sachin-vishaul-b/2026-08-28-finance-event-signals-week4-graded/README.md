# Claude, Graded.

Week 4 build-log — the finale: `outcome-grader` scores human-cleared
signals against realized price moves, pre-registered before it existed,
and never guesses. Falsifiability: the author's own prediction error
(BCAB, mis-dated by a day), caught by the pre-registration discipline and
disclosed rather than quietly fixed. Recipe promoted `DRAFT → RUNNABLE-LIVE`.

| | |
|---|---|
| **Runtime** | 1:59 (119.0s) |
| **Format** | 16:9, 3840×2160 (4K), 24 fps, h264/aac |
| **9:16 cut** | Not yet built (flagged — see BUILD-LOG.md) |
| **Voice** | Kokoro `am_onyx` — local, free, no API |
| **Beats** | 12 · Claude-skin bookends + GitHub-dark skin for code/diff/pipeline beats |
| **Presenter** | Sachin Vishaul B |
| **Channel** | @HumanitariansAI (Mycroft) |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd (GATE V: 0 BLOCKER) · solo build, no independent reviewer · not published |

## What this video covers

| Beat | | |
|---|---|---|
| B00 | Cold open | Pre-register the grading rule before looking at a single price |
| B01 | Framework | The rule was written down before the grader existed |
| B02 | Ask | Never guess — write `correct=NULL` when ungradeable |
| B03 | Code | Every failure path in `grader.py` returns a note, never a guess |
| B04 | Output | 19 signals in, 3 gradeable, 3/3 correct, 16 honestly pending |
| B05 | Change | The deliberate break attempt — two exotic ticker types |
| B06 | Code (revision) | A bad ticker becomes a caught exception, not a crash |
| B07 | Output (revision) | Both exotic tickers: a note, never a crash, never a guessed price |
| B08 | Falsifiability | The author's own prediction error, caught and disclosed |
| B09 | Summary | Recipe promoted to `RUNNABLE-LIVE` — not `VERIFIED`, no independent reviewer |
| B10 | Handoff | Your turn: pre-register your own falsify conditions before you look |
| B11 | Outro | "Claude, Graded." |

## Source of every claim

See `FACTCHECK.md` and `SOURCES.md` — every number traces to a real
`RUN_LOG.md` entry or commit in the underlying project.
