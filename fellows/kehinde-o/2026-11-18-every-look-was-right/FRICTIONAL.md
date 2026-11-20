# Frictional log — Every Look Was Right

## 2026-11-18 — Peeking at A/B tests, and a flaw in my own sequential test.

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1uzsEqyuOdUHjgOWCFHAsc-94NnuNb2bm?usp=drive_link
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** github.com/Kenny0bi/product-analytics-engine
- **Paired report:** [Fact-Checking Chapters 31 and 32](../2026-11-18-chapters-31-32-review/)

**What I was working on.**

The STEM explainer for week 10, built on my own project.

**What I tried, and what I expected.**

I ran my analytics engine on 1,000 experiments with no real difference, checked ten times each. Checking once gave 4.0 percent false alarms; stopping at the first significant look gave 18.7. My engine's sequential test, which should hold near 5, gave 12.9. It re-estimates the control rate from the same experiment at every look and treats the estimate as exact. With the rate fixed in advance, 3.2.

**Where it resisted, and what I did next.**

The flaw is in my own code, and I kept it in the video. My first simulation also kept checking a sequential test after it had already stopped, which would have overstated the problem; that was corrected before any number was used.

I sent the first script back because it read like a template, and checked every number in the rewrite against `evidence.json`.

I fixed the engine the same day. It now compares users in pairs, so the null needs no estimate,
and on the same 1,000 experiments it gave 1.7 percent false alarms. The last scene of the video
says so.

**What Claude contributed, and what I did with it.**
- Mine: the project, the choice of idea, and the decisions about what to keep in the video.
- Claude's: running the evidence scripts, drafting the script, the visuals and the render.
- Accepted: the measured numbers in `evidence.json`, reproducible with `evidence_run.py`.
- Rejected/changed: the first script, and any number that did not come from running the code.
- Evidence: `FACTCHECK.md`, `evidence_run.py` and `evidence.json` in this folder.

**What I understand now, and what I still do not.**
- Understood: a sequential test is only safe when its null is fixed before the data arrives; pairing users makes that exact.
- Not understood: how much power a mixture test (mSPRT) would buy over the paired test at the same error rate.
- Open: compare the two on the same simulation.
