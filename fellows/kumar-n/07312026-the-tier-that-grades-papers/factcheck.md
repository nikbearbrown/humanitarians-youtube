# FACTCHECK — The Tier That Grades the Papers

Verified against the uploaded source documents: the SERS-ML review paper
(`Machine_Learning_for_Surface-Enhanced_Raman_Spectroscopy...pdf`) and
`hai-2026-W1.md` through `hai-2026-W6.md`.

## Paper content claims

| Claim | Source (in paper) | Verdict |
|---|---|---|
| SERS spectra: high sensitivity + high measurement variance (substrate/hot-spot/matrix) | Section 1, Introduction | OK — direct paraphrase, own words |
| SVM and ensemble tree methods = strongest validated classical performance | Abstract; Section 3.1 | OK |
| Deep learning (1D/2D CNN, transformers, CNN-LSTM) high accuracy on large single-site datasets; edge narrows on small datasets | Section 4, opening + 4.1 discussion of Huang et al. | OK — paper states this explicitly: "on the small datasets... deep learning offers no consistent advantage" |
| Dong et al. [U-07]: SVM, serum SERS, two independent cohorts, 95.81% accuracy, 95.40% sensitivity, 95.87% specificity, 382 healthy + 1,582 cancer patients, 5 cancer types | Section 3.1 | OK — exact figures quoted in paper |
| Dong et al. approaches Tier 2 (independent cohort validation) | Section 3.4 | OK — paper's own tier assignment |
| Huang et al. [U-20]: 1D-CNN, 66,000 spectra, 22 factories, 97.33% accuracy, single region/time period, boundary of Tier 2/3 | Sections 3.4 and 4.1 | OK — paper's own tier assignment and caveats |
| No published SERS-ML study has achieved Tier 1 (multi-site, prospective, independent) | Section 3.4, Abstract, Conclusion | OK — stated multiple times as the paper's central finding |
| Majority of SERS-ML literature is Tier 3 (hypothesis-generating) | Section 3.4 | OK |
| The field's most pressing need is rigorous external validation, not new architectures | Abstract; Section 6 Conclusion | OK — stated as the paper's central thesis, near-verbatim in places (paraphrased here) |
| Continuous/wastewater monitoring remains an engineering frontier, limited field validation | Section 5.3 | OK |

## Kumar's diagnosis/fix claims

| Claim | Source | Verdict |
|---|---|---|
| Methodology section lists techniques without justifying the choice | W2 report — "It never told me *why*... just a list of names, defined, and left there" | OK |
| Read as AI-generated (dash usage, disconnected sections) | W2 report — named textual signals | OK |
| PM (Edward) confirmed the diagnosis was a real problem | W3 report — "Edward agreed it's a real problem in the paper" | OK |
| Teammate (Kunal) independently reached the same conclusion before comparing notes | W3 report — "hadn't discussed it beforehand... landed on almost exactly the same read" | OK |
| First CRITIQ pass (W3): flagged citation/factual-accuracy problems | W3 report | OK |
| Later CRITIQ pass (W5): clean, no major issues | W5 report | OK |
| Tier-classification overlap in the draft, later confirmed as a real issue | W2/W3 reports | OK — this is about the DRAFT under revision, distinct from the published paper's own tier framework; kept clearly separated in the script (B05/B06 refer to Kumar's diagnostic work on the draft, not a flaw in the final tier framework itself) |

## Friction protected

- Kept: B04 PREDICT commits the viewer before revealing the diagnosis was
  correct — same logic as Claude, Debunked?'s B05.
- Simplified: the paper's real dataset numbers (382/1,582; 66,000/22) are
  used verbatim per REBUILD LAW — no invented figures.
- Removed for pacing: the full preprocessing pipeline (noise reduction,
  baseline correction, normalization, alignment) — genuinely part of the
  paper but a 2-minute cut can't teach it without crowding out the tier
  framework, which is the stronger single idea. Candidate for a longer cut.
- One clarification embedded in the script itself: Kumar's tier-overlap
  diagnosis concerns the *draft under revision*, not a flaw in the paper's
  final published tier framework — B05/B06 keep this distinction intact so
  the video doesn't misrepresent the paper's own contribution as broken.
