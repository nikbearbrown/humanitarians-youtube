# Frictional log — The Check That Passed

## 2026-11-18 — A recommender that passed its gradient check and still lost to a popularity counter.

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1YE452Ql5N9XSulackFiN93JbQBVtfToC?usp=drive_link
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** github.com/Kenny0bi/pulse-recsys
- **Paired report:** [Fact-Checking Chapters 16, 11 and 15](../2026-11-18-chapters-16-11-15-review/)

**What I was working on.**

The STEM explainer for week 12, built on my own project.

**What I tried, and what I expected.**

On MovieLens 25M, split by time, my two-tower model scored 3.1 percent recall at ten against a popularity counter's 5.8, despite a gradient check that agreed to about a millionth. Training with in-batch negatives treats popular films as wrong answers; only 1.2 percent of its top-ten slots went to the hundred most popular films. The logQ correction took it to 8.6 percent.

**Where it resisted, and what I did next.**

Rerunning this took a full download of 25 million ratings from a server with an expired certificate, validated by the archive's own checksums and row count. And my README says the uncorrected model scored 0.018. The current code without the correction scores 0.031. My first failing run must have differed in more than the correction, so I report the measured number, and I corrected the README to match.

I sent the first script back because it read like a template, and checked every number in the rewrite against `evidence.json`.

**What Claude contributed, and what I did with it.**
- Mine: the project, the choice of idea, and the decisions about what to keep in the video.
- Claude's: running the evidence scripts, drafting the script, the visuals and the render.
- Accepted: the measured numbers in `evidence.json`, reproducible with `evidence_run.py`.
- Rejected/changed: the first script, and any number that did not come from running the code.
- Evidence: `FACTCHECK.md`, `evidence_run.py` and `evidence.json` in this folder.

**What I understand now, and what I still do not.**
- Understood: a passing check only answers the question it asks.
- Not understood: exactly what else differed in my first failing run.
- Open: nothing.
