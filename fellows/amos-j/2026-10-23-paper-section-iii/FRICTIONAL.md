# FRICTIONAL — Week6 · Paper Section III: methods rewritten against the code

Append-only. Add new dated entries at the bottom. Never rewrite an earlier one.

---

## 2026-10-23 · *written later, on 2026-10-29*

**Working on**
- Rewrote Section III, "Model Architectures and Experimental Setup", of the IEEE paper *"Do Residual Connections Matter?…"*. Also verified the bibliography (`report.md` L8–27).

**Tried / expected**
- Goal: every sentence in Section III should match the code and the run records. Checked every claim against `src/model.py`, `legacy_baseline/model.py`, `main.py` and the run manifests (L23–27, L61–62).

**Where it resisted → what I did next**
- **The old Section III described work that doesn't exist** (L31–41):
  - The 25-layer ResNet reimplementation: not in the repo. Our `resnet` is `Raman1DCNN`.
  - Plain-5/10/25 networks and the ablations: none implemented, none run.
  - Batch size 10 → actually 64. Betas (0.5, 0.999) → defaults.
  - 10% validation → actually a 67/33 split.
  - Five 90/10 splits → one fine-tuning run, last-epoch weights, no validation.
  - Holm–Bonferroni: not implemented.
  - 12 GB GPU: not confirmed.
- **The `bacteria-ID/` folder in the repo is empty.** Downloaded `csho33/bacteria-ID` from GitHub to check Ho's code directly (L43–45).
- **References:** of 14, two were wrong (L75–83):
  - `pan2021review` is a 2022 *J. Raman Spectrosc.* article, not an arXiv preprint, and its fifth author was missing;
  - `paszke2019pytorch` had an unsupported page range.
  - Bibliography is now 33 entries, all cited.
- Removed the old diagram, which showed a model that was never run. Replaced Table IV's three placeholder rows with the two models actually trained (L118, L124–134).

**Claude / others**
- Subagents gathered facts, verified references and drafted. The main agent checked every claim against the code, the run records and the original sources (L24–27).

**Understand now / still don't**
- Now: the draft was ahead of the code. Section III now says this is a family-vs-family comparison differing in seven factors, not a single-factor ablation of residual connections (L101).
- Still don't (§4, L157–179). Sections left unchanged on purpose, which now disagree with Section III:
  - The abstract still claims ResNet-25 and Plain-N ablations.
  - II-C still says five 90/10 splits.
  - II-B says no pre-processing, but the code re-applies min–max.
  - The results text cites a macro-F1 column that Table IV doesn't have.
- Treatment-group, MRSA AUC, confusion, ROC, noise and cost results are still placeholders.
- The 2026-09-17 runs came from uncommitted code (`git_dirty: true` at fb58ad3), so they can't be reproduced exactly from a commit.
- Nothing in this report is committed to git yet (L6).

**Evidence:** [`report.md`](report.md) · `paper/overleaf/main.tex`, `paper/overleaf/references.bib` · paper compiles to 10 pages with MiKTeX, no errors (L138–140)

### Git Commits

- [`bf6aa0e`](https://github.com/hspgit/RAMAN-Effect/commit/bf6aa0e09b1d565f800fdb6eecb1c16853892ac6) · paper: Overleaf draft, figures and spectra figure script. This is where the paper work landed; it was committed 2026-10-29
- [`fb58ad3`](https://github.com/hspgit/RAMAN-Effect/commit/fb58ad36f897214d25bf489e15c6f1336936ac93) 2026-09-16 · the commit the reported runs were built on, with uncommitted changes (L175–177)
