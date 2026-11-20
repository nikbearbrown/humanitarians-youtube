# Frictional log — The Answer Did Not Move

## 2026-11-18 — Proving my graph compiler's rewrites leave the answers unchanged.

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1xuJiVtZS1ToZprp0ChjTPXiLxS5OCGc5?usp=drive_link
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** github.com/Kenny0bi/fuse
- **Paired report:** [Fact-Checking Chapters 5, 7 and 12](../2026-11-18-chapters-5-7-12-review/)

**What I was working on.**

The STEM explainer for week 11, built on my own project.

**What I tried, and what I expected.**

My compiler takes resnet18 from 141 operations to 32. I ran the original and the rewritten network on the same image and compared all 1,000 outputs: largest difference about one millionth, same top prediction. Before trusting that, my runtime had been checked against onnxruntime, an engine I did not write: about two millionths. The fold of normalization into the convolution was also checked directly in double precision.

**Where it resisted, and what I did next.**

Exporting the model took several attempts: the system PyTorch on my Mac cannot talk to its NumPy, so the export had to run in a separate environment with versions that cooperate. My README quotes 2.6 millionths for the runtime check; this run measured 2.4, from a newer export. Same conclusion, but I note it rather than quote the old figure.

I sent the first script back because it read like a template, and checked every number in the rewrite against `evidence.json`.

**What Claude contributed, and what I did with it.**
- Mine: the project, the choice of idea, and the decisions about what to keep in the video.
- Claude's: running the evidence scripts, drafting the script, the visuals and the render.
- Accepted: the measured numbers in `evidence.json`, reproducible with `evidence_run.py`.
- Rejected/changed: the first script, and any number that did not come from running the code.
- Evidence: `FACTCHECK.md`, `evidence_run.py` and `evidence.json` in this folder.

**What I understand now, and what I still do not.**
- Understood: check the checker against something that does not share its mistakes.
- Not understood: whether the 2.4 versus 2.6 gap is the exporter or the input.
- Open: nothing.
