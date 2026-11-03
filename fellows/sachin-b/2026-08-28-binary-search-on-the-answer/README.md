# Claude, Halved.

Week 4 STEM video: binary search on the answer — the DSA pattern for
searching a range of possible answers via a monotonic feasibility check,
not the classic sorted-array search. Falsifiability: it silently gives a
wrong answer if the predicate isn't actually monotonic.

| | |
|---|---|
| **Runtime** | 1:36 (96.2s) |
| **Format** | 16:9, 3840×2160 (4K), 24 fps, h264/aac |
| **9:16 cut** | Not yet built (flagged — see BUILD-LOG.md) |
| **Voice** | Kokoro `am_onyx` — local, free, no API |
| **Beats** | 9 · Claude-skin bookends + 5 purpose-built Manim scenes |
| **Presenter** | Sachin Vishaul B |
| **Channel** | @HumanitariansAI (Mycroft) |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd (GATE V: 0 BLOCKER) · solo build, no independent reviewer · not published |

## What this video covers

| Beat | | |
|---|---|---|
| B00 | Cold open | Not the sorted-array search — the other one |
| B01 | Executive summary | A one-time-flip yes/no question can be binary-searched directly |
| B02 | Framework | The answer range, laid out on a line, with the flip point |
| B03 | Worked example | Minimum ship capacity — guess, simulate, narrow |
| B04 | Mechanism in motion | Each guess halves the range |
| B05 | Falsifiability | Only works if the predicate is truly monotonic |
| B06 | Verdict | Recognition matters more than the code |
| B07 | Handoff | Your turn: solve it, and verify the flip happens exactly once |
| B08 | Outro | "Claude, Halved." |

## Sourcing

The worked example is the canonical instance of this pattern (LeetCode
1011). No invented numbers beyond the illustrative toy weights. See
`FACTCHECK.md`.
