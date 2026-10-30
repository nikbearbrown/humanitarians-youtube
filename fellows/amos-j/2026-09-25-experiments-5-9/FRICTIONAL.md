# FRICTIONAL — Week2 · Experiments 5–9 and corrections

Append-only. Add new dated entries at the bottom. Never rewrite an earlier one.

---

## Week ending 2026-09-25 · *written later, on 2026-10-29*

**Working on**
- Experiments 5–9 on LegacyCNN with the corrected pipeline (`DEFAULT_PIPELINE = (MinMax,)`):
  - 5: phase-2 tuning
  - 6: longer fine-tuning
  - 7: incremental learning
  - 8: seed ensemble
  - 9: stage-1 augmentation
- Plus the corrections table. Experiments 1–4 are week1's (see `../2026-09-14-ramanspy-reproducibility/FRICTIONAL.md`). (`EXPERIMENT_RECORD.md` §1, §7–11, §15)

**Tried / expected**
- **Exp 6:** best fine-tune epoch was always at or near 20 of 20, so I tried 60 epochs. Gave it a 40% chance of helping (L276, L311).
- **Exp 7:** predicted catastrophic forgetting in Config A, and that a larger replay buffer would help (L368–370).
- **Exp 9:** at n=3, augmentation looked like a real +0.84, p = 0.012 (L463–464).

**Where it resisted → what I did next**
- **Exp 5 was null:** +0.02 / −0.03 / +0.16. `p2_valaugwd`'s t-interval *excluded* zero while its McNemar p was 0.47, because three per-seed differences landed close together. Trusted McNemar and treated it as zero (L264–274).
- **Exp 6 lost a point:** −1.01, pooled p = 3.4e-05. Best epoch tracked ~90% of whatever budget it got (17–20 of 20, 54–57 of 60). Re-diagnosed as a 300-sample validation set unable to tell late epochs apart, not a model still converging (L300–309).
- **Exp 7 contradicted both predictions:**
  - Config A gave plasticity failure, not forgetting.
  - A bigger replay buffer made new-class recall *fall*, 23.2 → 8.6.
  - The frozen backbone lost 63.5 points with every backbone parameter locked, so the forgetting is logit competition in the head, not representation drift (L359–370).
- **Exp 9 reversed at n=6:** +0.16, p = 0.531. All three signals at n=3 were small-sample artefacts driven by seed 2. The noise floor went from 0.33 to 0.6–0.8 points (L59–61, L456–470).
- **Exp 8:** ensemble +0.80 over the best member, p = 0.059. One measurement, and the best of three combination rules was the one reported (L418–426).
- **Corrections (§15):**
  - `docs/10`'s 18 results all used ASPLS, so they are invalid.
  - "Augmentation worth +1.40" is falsified.
  - "73.23% ± 0.11%" was a last-epoch number with overlapping folds.
  - The wavenumber axis is descending, not ascending as the docs said.
  - `compare_runs.py` pools across model types.

**Understand now / still don't**
- Now: three seeds is not enough for sub-point effects. Anything under ~1 point needs ≥6 paired seeds and a per-sample test.
- Still don't (§16):
  - Whether head normalisation fixes the new-class case. It follows from the frozen-backbone result but is untested.
  - The antibiotic-treatment task: never run.
  - Why classes 11 and 8 fail for every design and seed.
  - Whether the Transformer1D init causes its sd of 5.65: unconfirmed.
  - The mechanism figure (raw vs full pipeline vs minmax_only): not yet made (L189–196).

**Evidence:** [`EXPERIMENT_RECORD.md`](EXPERIMENT_RECORD.md) §7–11, §15, §16 · per-run data in `runs/<run_id>/` and `results/ablation/*.json` in the RAMAN-Effect repo (L540–548)

### Git Commits

- [`709541e`](https://github.com/hspgit/RAMAN-Effect/commit/709541ea4178da2aeedeba2967988f2a1ad32272) 2026-09-24 · results after 6 experiments
- [`d4a2ace`](https://github.com/hspgit/RAMAN-Effect/commit/d4a2ace64b075fe692f0dc101658cf00046db598) · runs: legacy CNN noaug and p2_base runs of 2026-09-24 (the Exp 9 and Exp 5 runs). Committed 2026-10-29
