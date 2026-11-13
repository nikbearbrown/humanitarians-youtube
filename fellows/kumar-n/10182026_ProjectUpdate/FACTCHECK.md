# FACTCHECK — sers-ml-4-6-update

**Reel:** What Changed in Section 4.6? (1:50)
**Subject:** two-week revision of §4.6 "Practical Deployment Considerations" in *Machine Learning for Surface-Enhanced Raman Spectroscopy: From Preprocessing to Deployment* (Paper 2 of 3, draft).
**Checked:** 2026-10-18. Every narrated or on-screen factual claim is listed below.

## Sources

| ID | Source | Status |
|----|--------|--------|
| S1 | Original §4.6 draft (author) | internal |
| S2 | Revised §4.6 + change log (author) | internal |
| S3 | Zaki, J. K., Tomasik, J., McCune, J. A., Bahn, S., Lió, P., & Scherman, O. A. (2025). Explainable deep learning framework for SERS bioquantification. *ACS Sensors* 10(9), 6597–6606. doi:10.1021/acssensors.5c01058 (arXiv:2411.08082) | peer-reviewed; abstract checked |
| S4 | Yang, Z., Meng, L., Rui, W., Shen, L., Zhao, S., & Shi, L. (2026). Enhancing explainability in Raman spectroscopy classification with SHAP and spectral segmentation. *Spectrochim. Acta A* 344(Pt 1), 126394. doi:10.1016/j.saa.2025.126394 | peer-reviewed; abstract checked |
| S5 | Mahmud, S., Sayem, F. R., Hassan, M., Yang, Y., Chowdhury, M. E. H., Zughaier, S. M., et al. Deep learning-based cross-device standardization of surface-enhanced Raman spectroscopy for enhanced bacterial recognition. PMID 40991976 | abstract checked; **added to the video during this check — not yet in the paper** |

## Claims

| Beat | Claim (as narrated / shown) | Source | Verdict |
|------|-----------------------------|--------|---------|
| B00 | §4.6 covers compute, interpretability, generalization; each got a different kind of fix | S1, S2 + change log | ✓ |
| B01 | Not every part needed rewriting; each needed checking | change log | ✓ paraphrase of the author's stated approach |
| B02 | Pruning, quantization, distillation can shrink a model dramatically | S1, S2 | ✓ qualitative only — the paper's "one to two orders of magnitude" is **not shown** because it is uncited in both drafts |
| B02 | Revision makes compression the default path to field deployment | S2 | ✓ |
| B02 | That evidence comes from general deep learning, not SERS | S2 | ✓ paper's stated position |
| B02 | The paper found no published result on compressed SERS models under real substrate/hot-spot variability | S2, change log (author's search) | ✓ attributed to the paper; not independently searched in this check |
| B03 | Draft called mechanistic explanation an open problem | S1 | ✓ |
| B03 | Zaki et al. built CRIME for SERS mixture explainability | S3 abstract | ✓ |
| B03 | GRASS segments a Raman spectrum into continuous regions, then scores each with SHAP, instead of individual points | S4 abstract | ✓ |
| B03 | Region-grouped attribution is "cleaner" (on-screen caption) | S4 highlights report superior regional-contribution analysis | ✓ qualitative; no GradCAM/LIME comparison figures are shown |
| B03 | Use a dedicated spectral method, not unmodified GradCAM | S2 | ✓ paper's recommendation |
| B03 | Spectrum and attribution bars | — | **Illustrative** — labeled on screen |
| B04 | Models trained at one site/instrument/batch often fail when those change | S2 citing [U-29]; S5 abstract describes limited cross-device reproducibility and poor generalizability in SERS | ✓ — but [U-29] is still "CITATION NEEDED" in the paper (see Outstanding) |
| B04 | Mahmud et al. translated spectra from four portable instruments into lab-grade equivalents | S5: four portable Raman systems → one lab-grade reference, AgNR substrates | ✓ |
| B04 | That covers devices on one substrate type | S5 (single AgNR substrate type) | ✓ |
| B04 | Cross-site and cross-substrate generalization still open | S2; S5 does not test either | ✓ |
| B05 | Six verdict lines | S2 + this check | ✓ — line 5 describes the agreed revision (Mahmud et al.), pending in the paper |
| B06 | Viewer prompt | — | no factual claim |

## Corrections made during checking

1. **Generalization softened.** The revision says a literature search "did not surface a SERS-specific application" and that this is the one area in Section 4 without "even an initial proof-of-concept." This check found S5, a SERS-specific cross-device standardization study. The video states this; the author agreed to revise the paper to match.
2. **Compression figure dropped from screen** (uncited 1–2 orders of magnitude).
3. **Kalatzis & Nega (2026) review omitted** from the video; it could not be located during this check.

## Outstanding — paper, not video

1. Revise the generalization paragraph to cite S5, e.g. "Early SERS-specific work on cross-device standardization now exists (Mahmud et al.), but cross-site and cross-substrate generalization remain largely unevaluated." Remove "not yet produced even an initial proof-of-concept."
2. Add a citation for "one to two orders of magnitude" compression savings.
3. Resolve [U-29] (still marked CITATION NEEDED in the reference list).
4. Confirm the Kalatzis & Nega (2026) reference and the GRASS-vs-GradCAM/LIME comparison against the full texts.

## Disclosure

Narration is synthetic (Kokoro TTS, voice `am_liam`), presented as "Liam, in for Kumar Karthik." Scripts, scenes, and this check were AI-assisted (Claude) and reviewed by the author.
