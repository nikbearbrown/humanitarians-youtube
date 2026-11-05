# FRICTIONAL — week3 · Foundation model: spec and Plan 1

Append-only. Add new dated entries at the bottom. Never rewrite an earlier one.

---

## 2026-10-01 · *written later, on 2026-10-29*

**Working on**
- Wrote the foundation-model design spec (`docs/superpowers/specs/2026-10-01-raman-foundation-model-design.md`) and Plan 1: data audit and corpus build. Nothing was built yet.
- Plan 1's goal: build `corpus_v1`, public spontaneous-Raman spectra on one 1001-point grid with every Bacteria-ID spectrum kept out, then decide G0 (`2026-10-01-foundation-plan1-data-corpus.md` L5).

**Tried / expected**
- Verified each source's real format against what the spec assumed.
- Set the bar in advance. G0 = at least **150,000** usable pretraining spectra after filtering and deduplication (L35).

**Where it resisted → what I did next**
- The spec and reality disagreed. Deviations D1–D8 (L38–49):
  - **D1:** DeepeR has no cell or image IDs, so a per-image cap is impossible. Used a seeded subsample of 22,000 instead. Needs a manual SharePoint download, so marked optional.
  - **D2:** the airborne-pathogen set comes already baseline-corrected and min–max scaled at 5.33 cm⁻¹. Kept it as the closest domain, and flagged it for a source-ID probe in Plan 2.
  - **D3:** the API CSV has no sample IDs, so it can't be split by sample. Made it pretrain-only. Probe tasks became RRUFF and airborne species.
  - **D4:** RRUFF ships RAW and Processed copies. Kept RAW only.
  - **D5:** `raman_data`'s dependencies could disturb the main venv. Exported to `.npz` from a separate small venv.
  - **D6:** excluded three sources:
    - marine pathogens (no wavenumber axis);
    - locust (resonance Raman);
    - DeepeR super-resolution (5.2 GB).
  - **D7:** MLROD is 130,061 spectra in 41 files, not the 500k the spec assumed.
  - **D8:** the Zenodo bacteria labels file is unverified. Labels are used only if the metadata CSV is found and row-aligned.
- Wrote down five inputs the spec implied but didn't spell out, each with a test (L51–59):
  - wrong-unit axes;
  - cross-source duplicates;
  - NaN/inf intensities;
  - mixed label types;
  - half-finished downloads.

**Understand now / still don't**
- Now: public Raman sources don't share structure. Sample IDs, preprocessing state and axis units vary, so the leakage guard and the sample-level splits have to be designed per source.
- Still don't (as of this week):
  - Whether the corpus clears G0's 150,000.
  - Whether the pre-processed airborne set becomes a source shortcut (D2).

**Evidence:** [`2026-10-01-foundation-plan1-data-corpus.md`](2026-10-01-foundation-plan1-data-corpus.md) L5, L23–59 · outcome in `../2026-10-03-foundation-adaptation-results/report.md` §2.1

### Git Commits

- [`1432a4b`](https://github.com/hspgit/RAMAN-Effect/commit/1432a4b7533ba090d30f95b4424ad69f5f63b148) · Add design spec for Raman foundation model (A -> B1/B2) experiment
- [`e4b3749`](https://github.com/hspgit/RAMAN-Effect/commit/e4b37492ad3544fe7a3c96d37ea4aefae26d7206) · Add Plan 1 (data audit and corpus build) for the foundation model experiment
