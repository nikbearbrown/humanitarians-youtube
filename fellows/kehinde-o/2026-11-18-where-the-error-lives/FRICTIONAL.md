# Frictional log — Where the Error Lives

## 2026-11-18 — My IVF-PQ index tops out near 46 percent recall however many cells it searches.

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1f8Z0WM-Y6Q0zLh6vhZEnR6skycg4RNB3?usp=drive_link
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** github.com/Kenny0bi/hive-index
- **Paired report:** [Fact-Checking Chapters 10 and 13](../2026-11-18-chapters-10-13-review/)

**What I was working on.**

The STEM explainer for week 8, built on my own project.

**What I tried, and what I expected.**

I reran the index at its benchmark settings (100,000 SIFT vectors, 1,000 queries). Searching more cells raised recall from 30 to 46 percent and then stopped. To prove the search was not the problem, I counted how many true neighbours sat inside the searched cells: at 128 cells, all of them. The codes were losing them. Re-checking the top hundred against the real vectors took recall to 93 percent.

**Where it resisted, and what I did next.**

The SIFT download mirror served error pages instead of data when I first built this repo, so I compute ground truth myself rather than trust a downloaded file. For this video only the first 100,000 vectors were needed, so I fetched just that slice.

I sent the first script back because it read like a template, and checked every number in the rewrite against `evidence.json`.

**What Claude contributed, and what I did with it.**
- Mine: the project, the choice of idea, and the decisions about what to keep in the video.
- Claude's: running the evidence scripts, drafting the script, the visuals and the render.
- Accepted: the measured numbers in `evidence.json`, reproducible with `evidence_run.py`.
- Rejected/changed: the first script, and any number that did not come from running the code.
- Evidence: `FACTCHECK.md`, `evidence_run.py` and `evidence.json` in this folder.

**What I understand now, and what I still do not.**
- Understood: find where an error lives before trying to fix it.
- Not understood: how much a better codebook would raise the ceiling.
- Open: nothing.
