# FRICTIONAL — Week5 · Paper preparation and the base-size rerun

Append-only. Add new dated entries at the bottom. Never rewrite an earlier one.

---

## Week ending 2026-10-16 · *written later, on 2026-10-29*

**Working on**
- Checked the proposed paper outline (plain 1D CNN vs 1D ResNet on Ho et al. 2019) against our data and code, and built the Overleaf project.
- Set up configs for a base-size (14.6 M) rerun of model A. Nothing launched yet. (`WEEKLY_REPORT_2026-10-16.md` L5–21)

**Tried / expected**
- Expected most of the outline to be doable as written (§1.1).
- For base A, wrote expectations and decision rules *before* running:
  - probe score 0.80–0.83 (small reached 0.796);
  - downstream gains of only 0–2 points, because domain shift, not capacity, is the limit;
  - adopt base only if its trial beats 0.742 by more than 0.03.
  - (L166–170, L179–183, L198–200)

**Where it resisted → what I did next**
- **Outline §6.4 (noise across 1s/2s/3s):** "The data has no such splits". Redesigned as a simulated SNR sweep plus the real 1s → 2s instrument shift (L38).
- **"5-fold CV across samples":** the release has no sample IDs. Switched to the original protocol of 5 random 90/10 splits (L40).
- **The core ResNet-vs-plain contrast can't run yet.** Our "ResNet" isn't the paper's architecture, and it differs from our CNN in about seven ways at once, so skip connections can't be isolated (L41).
- **Current evidence cuts against the paper's premise:** plain CNN 83.9%, our ResNet 79.6%, Ho et al. 82.2%. Reframed the paper neutrally: "Do residual connections matter?" (L43–46).
- **Found a gap in last week's size choice:** small and base tied *before* the masked-GroupNorm fix. Base + masked GroupNorm was never run (L89–100).
- The 14 references are still unchecked (L58–59).

**Understand now / still don't**
- Now: the size decision rested on a trial run on the old stem, so "small is enough" isn't established for the current model.
- Still don't:
  - Whether base A beats small. It may tie again if 242k spectra can't use the extra capacity.
  - Whether base encodes more source identity: source-ID probe 0.950 vs 0.941 (L167–175).
  - Next week's plan, all open: base trial, overnight pretraining, controlled-experiment code, reference checks (L216–219).

**Evidence:** [`WEEKLY_REPORT_2026-10-16.md`](WEEKLY_REPORT_2026-10-16.md) · `paper/overleaf/`, `paper/overleaf.zip`, `paper/scripts/make_fig_spectra.py` · configs `foundation/configs/pretrain_trial_base_mgn.yaml`, `pretrain_main_base.yaml`, `adapt_base.yaml` (branch `amosj`)

### Git Commits

- [`bf6aa0e`](https://github.com/hspgit/RAMAN-Effect/commit/bf6aa0e09b1d565f800fdb6eecb1c16853892ac6) · paper: Overleaf draft, figures and spectra figure script
- [`a85ba27`](https://github.com/hspgit/RAMAN-Effect/commit/a85ba27a4c1398c330bce596c8fe5d6f43bf8cbe) · foundation: base-size model A (pretrain, adaptation, single test pass) and final report. Includes the base configs set up this week, plus the runs made after it
