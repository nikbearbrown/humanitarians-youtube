# FRICTIONAL — Week4 · Foundation model A → B1 / B2: results

Append-only. Add new dated entries at the bottom. Never rewrite an earlier one.

---

## Locked test pass 2026-10-03, report 2026-10-09 · *written later, on 2026-10-29*

**Working on**
- Built and evaluated the foundation model (plans 1–3) on branch `amosj`:
  - `corpus_v1`: 242,156 spectra from 25 public sources;
  - model A: a 4.99 M-parameter CNN stem + transformer, pretrained with MAE;
  - four adaptation arms (S, LP, B1, B2) on T1 (30 isolates) and T2 (2018 → 2019 clinical).
- (`report.md` L1–3, §2)

**Tried / expected**
- Pre-registered **Q3** before any test pass: B2 (LoRA) within 1.0 point of the best arm on both tasks, while training ≤5% of the parameters (L152).
- Size trials: base and small tied at 0.672, so I picked small. Adding masked GroupNorm to small gave 0.742 (L35–42).

**Where it resisted → what I did next**
- **Q3 narrowly failed:** B2 was 1.23 points behind B1 on T1, just outside the 1.0 margin. LP failed by 4.89 / 5.11 (L15, L152–153).
- **Edge-of-grid learning rates:** 6 of 8 picks sit at an edge of their 3-value grid, including B2 on both tasks and B1 on T1. I deliberately didn't extend the grids, to keep the tuning budget equal, so the Q3 miss may be a tuning artefact (L78–85, L327).
- 2 of 5 S seeds hit the 30-epoch cap on T1 stage i, so the baseline may have been cut short (L178).
- **Validation didn't predict test:** T1 val ~94% vs test 78–83%. T2 val sat at a ceiling (98.5–99.1%) and couldn't separate the arms (L102–107, L329).
- **Pretraining hurt one class:** T1 class 6 fell from 63% (S) to ~35% (B1/B2), mostly predicted as class 7. Classes 11 and 17 stayed below 60% for every arm (L277–281).
- **My own summary disagrees with my table:** L12 says B2 trains "4.4%" of the parameters; L63 and L199 say 4.52%. Not yet corrected.

**Understand now / still don't**
- Now: pretraining helps, most under shift over time (B2 on T2, +4.1) and with scarce labels (+4 points at 5 spectra per class). The hard part is the shift between measurement sets, not the classes (L11–16, L303).
- Still don't (L345–348):
  - Whether the Q3 miss is tuning (would need one post-hoc LR value below the edge).
  - Why A merges classes 6/7.
  - Run-to-run variation of A: only one pretraining run.
  - Whether a longer stage i changes S.

**Evidence:** [`report.md`](report.md) · test pass `final_test/scored.json` (2026-10-03T23:44:05) · run folders `foundation/runs/adapt/` · spec `docs/superpowers/specs/2026-10-01-raman-foundation-model-design.md`

### Git Commits

- [`c364567`](https://github.com/hspgit/RAMAN-Effect/commit/c36456762c2ad2d7759aab05ff27d34ab30f37e9) 2026-10-03 · foundation: main pretraining run and G1 result
- [`3be759f`](https://github.com/hspgit/RAMAN-Effect/commit/3be759f24c9f695585e22884254d47415c8b71c0) 2026-10-03 · foundation: adaptation results (S/LP/B1/B2 on T1/T2, single test pass)
