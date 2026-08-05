# PEDAGOGY — Nine Months at the Data Ceiling (hai cut)

**GATE P — awaiting human signature. Audio will not be generated until the
VERDICT line at the bottom reads PASS and carries your name.**

Retrospective volunteer work report for Humanitarians AI, covering
2025-W48 → 2026-W32 on NeuroVEP / ANN mfVEP response classifier.
Register: Pragmatist (hai). Voice: Kokoro `af_bella`. Channel: @HumanitariansAI.

## What this reel is — and is not

This is **one honest retrospective**, not a backdated weekly report. It does not
claim to be the contemporaneous weekly cadence the renewal gate asks for, and it
must not be filed as though it were. `Work Chronology.md` §5 is explicit that the
chronology "cannot substitute for the weekly `/hai` reports" — the same applies
here. Go-forward weekly cadence is described in the fellow README.

## Act structure
- B00 cold open, `ClaudeComposerAsk`, ASK→RESULT lines present ✓
- B01 executive summary in one breath before any specific (EXECUTIVE-SUMMARY LAW) ✓
- B02–B03 method and the decision trigger (when to use LOSO) ✓
- B04–B05 results, then the diagnostic reading of the results ✓
- B06 **where it fails** — required by the Pragmatist register, not optional ✓
- B07 the causal finding with its falsifiable counterfactual ✓
- B08 the hardware-loss interruption, reported rather than hidden ✓
- B09 next steps including the gap that is *not* closed ✓
- B_CLI worked exercise, second-to-last, BUILD lane, runnable today ✓
- B_OUTRO Humanitarians AI outro, last ✓
- No two consecutive beats share a visual state; B04 is the only chart ✓
- Stock toolkit scenes only (`ClaudeComposerAsk`, `SlateCard`, `BarChart`,
  `OutroSeries`) — no custom TSX, so this rebuilds on a clean install ✓
- No Manim equation beats — LaTeX/dvisvgm is not installed on this machine and
  the reel is authored to not need it ✓

## Evidence discipline

Every number below traces to an artifact in `~/Desktop/NeuroVEP` or
`~/Documents/Humanitarians`. Nothing is estimated, rounded up, or inferred.

| Claim (beat) | Source | Verdict |
|---|---|---|
| AD25 = 25% of sectors blacked out per eye (B02) | `03_mfvep60_cohort_AD25_labeled_database.ipynb` | OK |
| Input `(2, 10, 600)`, ~1,020 paired samples (B02) | dataset spec, Combo_VEP_PsyLink_Study | OK |
| 17 subjects, CVPL001–018 excl. 015 (B01/B07) | cohort database | OK |
| 17-fold LOSO (B03) | `docs/progress_report.md` | OK |
| DualEye CNN acc 0.723 (B04) | NB04, `docs/progress_report.md` | OK |
| Per-eye heads acc_L 0.749 (B04) | NB06 | OK |
| + nnlib augmentation acc 0.694 (B04) | NB09, Exec Summary §57 | OK |
| FBCSP-LDA acc_L 0.728 (B04) | recovered notebook, Chronology §4 | OK |
| ATCNet acc_L 0.773 (B04) | recovered notebook, Chronology §4 | OK |
| EEGNet acc_L 0.801, AUC_L 0.892, 2,578 params (B04/B05) | `EEGNet/`, mtimes May 4–5 | OK |
| NB10b sector-level leakage; corrected to subject-level (B06) | `docs/progress_report.md` §NB10b | OK |
| Corrected sens 61.4% / spec 80.6% (B06/B09) | same | OK |
| Train >0.95 vs val ~0.70 gap (B07) | `docs/progress_report.md` | OK |
| Counterfactual "50+ subjects lifts the ceiling" (B07) | `docs/architecture_alternatives.md` | OK — stated as prediction, not result |
| 151,927 files / 124 s / 1,342 placed / 58,689 dupes / 0 errors (B08) | `merge_report.md` | OK |
| 37 notebooks rebuilt; 499 figures classified (B08) | `ipynbs/INDEX.md`, 6× `ANALYSIS.md` | OK |
| CNN carries sensitivity, RF carries specificity (B09) | `docs/progress_report.md` | OK |
| Clinical-threshold analysis does not exist yet (B09) | Exec Summary §8, stated as a gap | OK |

**Deliberately NOT claimed:** no hour totals, no completion percentage, no
statement that the weekly reporting requirement was met during the period, and
no attribution of the W20–W24 work to specific dates — those timestamps do not
survive (Chronology §4).

## Friction protected
- **Kept:** B06, the leakage beat. It is the least flattering thirty seconds in
  the reel and the single most load-bearing item in the report. Cutting it to
  save time would invert the whole point.
- **Kept:** B09's admission that the clinical-threshold analysis is unwritten.
- **Removed:** the nnlib PR #3 / `src/mfvep_classifier` package-extraction work.
  Real and substantial, but it is engineering scaffolding and it does not serve
  the reel's one idea. It belongs in a later weekly report.
- **Removed:** per-ring error analysis. Too fine-grained for a 3-minute cut.

## Register check (Pragmatist — `brands/hai.md`)
- Leads with method (B02) before any result ✓
- States the decision trigger explicitly (B03: "use LOSO from the start") ✓
- **States when it fails** (B06) — required, present, not softened ✓
- No academic hedging, no personality tax, no vacuous caveats ✓
- Facts unchanged from source documents; only the register is authored ✓

---

## Human sign-off

Read the narration in full before signing. You are signing that the pedagogy is
sound and every claim above is one you will stand behind in a review.

VERDICT: PASS

Signed: Vighnesh Sairaman   Date: 2026-08-04

Sign-off recorded on the signer's explicit instruction (name and date dictated
2026-08-04). Attests that the narration was reviewed and that every claim in the
evidence table above is one the signer stands behind.
