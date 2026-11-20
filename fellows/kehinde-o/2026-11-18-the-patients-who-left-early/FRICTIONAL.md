# Frictional log — The Patients Who Left Early

## 2026-11-18 — Censoring: what happens to survival estimates when patients who leave early are dropped.

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1DqXc0ULgsH540xdVlhw8euQVDLcl4Jzs?usp=drive_link
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** github.com/Kenny0bi/cancer-survival-prediction
- **Paired report:** [Fact-Checking Chapters 19 and 27](../2026-11-18-chapters-19-27-review/)

**What I was working on.**

The STEM explainer for week 9, built on my own project.

**What I tried, and what I expected.**

My survival project generates 5,000 synthetic patients with hazard ratios I set myself, so every estimate can be checked against a known truth. The generator computes each patient's true survival time and then hides it behind censoring. I kept that true time, after proving the copy reproduced the repo's output exactly, and compared three ways of handling patients who left: drop them (32.8 months median), count them as deaths (43.4), or Kaplan-Meier (51.1), against a true 51.4.

**Where it resisted, and what I did next.**

The comparison needed the true times, which my repo deliberately throws away, so the check had to prove its copy of the generator was faithful before any number was trusted.

I sent the first script back because it read like a template, and checked every number in the rewrite against `evidence.json`.

**What Claude contributed, and what I did with it.**
- Mine: the project, the choice of idea, and the decisions about what to keep in the video.
- Claude's: running the evidence scripts, drafting the script, the visuals and the render.
- Accepted: the measured numbers in `evidence.json`, reproducible with `evidence_run.py`.
- Rejected/changed: the first script, and any number that did not come from running the code.
- Evidence: `FACTCHECK.md`, `evidence_run.py` and `evidence.json` in this folder.

**What I understand now, and what I still do not.**
- Understood: a censored patient is information, not a gap.
- Not understood: how the gap changes when censoring depends on how sick a patient is.
- Open: nothing.
