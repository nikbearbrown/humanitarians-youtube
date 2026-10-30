# FRICTIONAL — week1 · RamanSPy reproducibility and variance

Append-only. Add new dated entries at the bottom. Never rewrite an earlier one.

---

## Week of 2026-09-14 → 2026-09-18 · *written later, on 2026-10-29*

**Working on**
- Stage 0 reproducibility infrastructure, the preprocessing ablation and an architecture re-test on the RAMAN-Effect repo (`hai_2026-09-20_weekly-report.md` L8, L16–30).

**Tried / expected**
- Removing ASPLS from the pipeline. Claude predicted +2–5 accuracy points, from a validation-to-test ratio measured on seed variance (L48). Actual: **+7.61** (pooled McNemar p = 2.5e-57).
- Ran the unseen-label guard expecting a `ValueError` on clinical files. It loaded 10,000 samples cleanly (L70).
- Claude argued twice that "smaller models win" was an ASPLS artefact. I ran 12 runs to test it (L54).

**Where it resisted → what I did next**
- `ds_kwargs` NameError at line 106: the block was placed after its first use. Diagnosed from the traceback and moved above the reference dataset load (L22, L41).
- The label guard validated nothing. Both label sets use integers 0–29, so the value check can't see that clinical labels are antibiotic-level and the rest are isolate-level. A patch exists but is **not applied** (L42, L70).
- `check_variance_source.py` reported "stdev 6.60, noise band 19.83" pooled across 5 architectures. Its "per-seed" table was really 5 models × 3 seeds. Both outputs were meaningless, caught by reading them against known per-model numbers (L58).
- Six `DIFF` rows in the variance check came from batch size 256 vs 128 changing float accumulation order. Benign, but the earlier "all checks passed" was "luckier than rigorous" (L72).
- Phase 2 verification: same seed, bit-identical checkpoint, **66.90% vs 71.20%**. I wanted to explain it before launching the 12-run grid, which turned into a "speculation spiral". Deprioritised the grid (L66, L78).

**Claude / others**
- Claude drafted the new modules (`repro.py`, `runmeta.py`, `cache.py`, `metrics.py`) and the integration patches. I applied them (L38).
- **Rejected:** Claude's placement of `ds_kwargs`, and its acceptance test 4 for the label guard. I supplied the correct model of the problem: label *spaces*, not label values (L41–42).
- **Rejected:** Claude's ASPLS-artefact hypothesis. LegacyCNN still won, 83.89 ± 0.33 vs ResNet 79.56 ± 1.78 (L54).
- Claude's +2–5 prediction was wrong in number *and* in reasoning. A variance-derived ratio doesn't transfer to a change in input representation (L50).
- PM: publishing strategy (compare two models vs best model) is unresolved and deferred to the PM (L20, L80).

**Understand now / still don't**
- Now: why the ASPLS prediction failed. The reasoning pattern didn't apply, not just the number.
- Still don't:
  - The cause of the Phase 2 4.3-point regression. Candidates: a 10% smaller training set (2700 vs 3000), or augmentation slowing early convergence. Neither confirmed (L66).
  - Transformer1D seed bimodality: sd 5.65 (66.23 / 76.10 / 75.93). Either unscaled `torch.randn` init or early stopping. Deprioritised; I should have written down why at the time (L68, L82).

**Evidence:** [`hai_2026-09-20_weekly-report.md`](hai_2026-09-20_weekly-report.md)

### Git Commits

- [`f4e1e29`](https://github.com/hspgit/RAMAN-Effect/commit/f4e1e29e2d43f1ddc51b40ddc1626d3d86ebb701) 2026-09-15 · testing more models
- [`fb58ad3`](https://github.com/hspgit/RAMAN-Effect/commit/fb58ad36f897214d25bf489e15c6f1336936ac93) 2026-09-16 · k fold verification and heatmaps. The 2026-09-17 ablation runs were made from uncommitted changes on top of this commit (`git_dirty: true`, `../2026-10-23-paper-section-iii/report.md` L175)
