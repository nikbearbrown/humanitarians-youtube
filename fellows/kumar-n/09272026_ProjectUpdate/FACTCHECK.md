# FACTCHECK — sers-ml-4-4-update

**Reel:** What Changed in Section 4.4? (2:18)
**Subject:** two-week revision of §4.4 "Hybrid and Multi-Task Architectures" in *Machine Learning for Surface-Enhanced Raman Spectroscopy: From Preprocessing to Deployment* (Paper 2 of 3, Kumar Karthik et al., draft).
**Checked:** 2026-10-18, against primary sources listed below. Every narrated or on-screen factual claim is listed. Claims about the paper's own text were checked against the original and revised §4.4 drafts supplied by the author.

## Sources

| ID | Source | Status |
|----|--------|--------|
| S1 | Original §4.4 draft (author) | internal |
| S2 | Revised §4.4 + change log (author) | internal |
| S3 | Shamim, M. M. R., et al. (2026). *Leakage-Robust Evaluation and Data-Scale Sensitivity of Attention-Enhanced Multi-Task Learning for Joint Fault Diagnosis and Remaining Useful Life Estimation.* arXiv:2607.16493 (v1, 17 Jul 2026) | **preprint, not peer-reviewed; not SERS/Raman** |
| S4 | Tan, A., He, Y., Shi, B., Mu, H., Zhang, Y., & Zhao, Y. (2026). ResFusionNet-TSMT. *Talanta*, 298(Pt A), 128852. doi:10.1016/j.talanta.2025.128852 (PMID 40972279) | peer-reviewed |
| S5 | Georgiev, D., Fernández-Galiana, Á., Vilms Pedersen, S., Papadopoulos, G., Xie, R., Stevens, M. M., & Barahona, M. (2024). Hyperspectral unmixing for Raman spectroscopy via physics-constrained autoencoders. *PNAS*, 121. doi:10.1073/pnas.2407439121 (published 5 Nov 2024) | peer-reviewed |

## Claims

| Beat | Claim (as narrated / shown) | Source | Verdict |
|------|-----------------------------|--------|---------|
| B00 | Kumar spent two weeks rewriting §4.4, hybrid and multi-task architectures | Author | ✓ author statement |
| B01 | The draft said multi-task learning "often" helps and cited nothing | S1: "often improving performance on both tasks relative to single-task models trained separately" — no citation attached | ✓ |
| B02 | Original was two paragraphs; revision is four | S1, S2 (counted) | ✓ |
| B02 | Revised paragraph roles: design rationale, counter-evidence, mechanism, rule for readers | S2 | ✓ paraphrase of revision |
| B03 | On-screen quote "…often improving performance on both tasks…" | S1 | ✓ verbatim |
| B03 | Shamim et al. (2026) preprint compared a multi-task model against the strongest single-task baseline on a leakage-audited split | S3 abstract; §3.5 Table 3 (AMTLNet vs CNN-LSTM-STL) | ✓ |
| B03 | Multi-task model scored 84.12% | S3 abstract; Table 6: AMTLNet 84.12 ± 0.96% accuracy, C-MAPSS FD001 | ✓ |
| B03 | Single-task baseline statistically indistinguishable; "Tukey p = 1.0" | S3 abstract: Tukey p = 1.0 vs CNN-LSTM; Table 6: CNN-LSTM 84.20 ± 1.33% | ✓ |
| B03 | On-screen labels "preprint · non-SERS" | S3 | ✓ disclosed on screen |
| B04 | Same data, same model, different split | S3 §4.1, Table 5: identical AMTLNet architecture, identical IMS Bearing raw data | ✓ |
| B04 | Naive splitting swung accuracy from 0% to 99.9% | S3 abstract ("inflate… to an artefactual 99.9%, or conversely collapse it to 0%"); Table 5: window-level random split 99.90 ± 0.20%; degenerate coarse chunking 0–65% across seeds | ✓ — note: in Table 5 the 0% end comes from a degenerate (coarse) chunked split, which the abstract groups with naive strategies; narration follows the abstract's framing |
| B04 | Leakage-audited track settles at ≈30% (±15) | S3 Table 5: refined chunk-based split 30.00 ± 15.49% (same Bearing data) | ✓ |
| B04 | "The protocol mattered as much as the architecture" | S3 §4.1 (~78-point range from protocol choice alone) | ✓ supported characterisation |
| B04 | Default: two separately trained models when tasks aren't naturally coupled | S2 | ✓ — the paper's recommendation, presented as such |
| B05 | Unconstrained autoencoders can reconstruct well while producing physically impossible outputs (e.g. negative concentrations); non-negativity removes this | S2 reasoning; S5 builds physics-inspired constraints into unmixing autoencoders and reports improved accuracy/robustness over standard methods | ✓ as mechanism; no S5 figures are quoted |
| B05 | Bar values | — | **Illustrative, not data** — labeled "illustrative" on screen |
| B05 | Wastewater SERS spectra are mixtures of contaminants | S2 | ✓ paper's framing |
| B06 | Lines 1–3, 5 summarise revisions | S2 | ✓ |
| B06 | ResFusionNet: dual-stream inputs and attention pooling | S4 | ✓ |
| B06 | [U-55] corrected to Georgiev et al., PNAS 2024 | S5 (title, authors, DOI match) | ✓ |
| B07 | Viewer prompt (split by sample or by spectrum?) | — | no factual claim |

## Corrections made during checking

1. **B03 narration rewritten.** An earlier cut said the preprint "kept the backbone identical" while quoting 84.12% / p = 1.0. Those figures compare AMTLNet (shared CNN + BiLSTM + BiGRU-attention encoder) against a single-task CNN-LSTM — *different* encoders (S3 Table 3). S3 has a separate identical-backbone section (§4.5) whose figures were not used. Narration and on-screen labels now describe the comparison as reported.
2. **B04 audited value changed** from 84.12% (C-MAPSS) to ≈30% (Bearing), so the "same data, same model" frame holds.
3. **B06 line 4 narrowed.** The draft's claim that ResFusionNet includes a class-attention mechanism for low-concentration samples could not be confirmed from the available abstract; the line now states only verified design features.

## Outstanding — paper, not video

- Revised §4.4 still describes the Shamim comparison as "identical-backbone." Recommend rewording to "compared an attention-enhanced multi-task model against the strongest single-task baseline," or citing S3 §4.5 directly after reading it.
- Confirm the low-concentration class-attention claim in §4.4 paragraph 1 against the full text of S4.

## Disclosure

Narration is synthetic (Kokoro TTS, voice `am_liam`), presented as "Liam, in for Kumar Karthik." Scripts, scenes, and this check were AI-assisted (Claude) and reviewed by the author. The author is affiliated with the RAMAN Effect project (see the paper's Declarations).
