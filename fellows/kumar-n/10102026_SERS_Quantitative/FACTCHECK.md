# FACTCHECK — sers-quantitative

**Reel:** Why SERS Is Hard to Make Quantitative
**Type:** standalone explainer
**Checked:** 2026-10-18. Every narrated or on-screen factual claim is listed below.

## Sources

| ID | Source | Status |
|----|--------|--------|
| S1 | Nanogap-engineered core-shell-like nanostructures for comprehensive SERS analysis. arXiv:2412.13882 | preprint; used only for the observation that SERS signal saturates with concentration in a Langmuir-consistent way |
| S2 | Bell, S. E. J., Charron, G., Cortés, E., Kneipp, J., Lamy de la Chapelle, M., Langer, J., Procházka, M., Tran, V., & Schlücker, S. (2020). Towards reliable and quantitative SERS: from key parameters to good analytical practice. *Angew. Chem. Int. Ed.* 59(14), 5454–5462. doi:10.1002/anie.201908154 | peer-reviewed |
| S3 | Plasmonic electronic Raman scattering as internal standard for spatial and temporal calibration in quantitative SERS. *J. Phys. Chem. Lett.* (2020). doi:10.1021/acs.jpclett.0c03056 (NIST publication record) | peer-reviewed |
| S4 | Fang, Seong & Dlott (2008), *Science* 321 — hot-spot distribution (see sers-hot-spots FACTCHECK) | peer-reviewed |

## Claims

| Beat | Claim (as narrated / shown) | Source | Verdict |
|------|-----------------------------|--------|---------|
| B00 | SERS can detect tiny amounts of a molecule, but quantifying is hard | S2, S3 | ✓ |
| B01 | Signal keeps rising with analyte only up to a point, then plateaus | S1 | ✓ |
| B02 | SERS mostly sees molecules on the metal surface; sites are finite | S1 (surface adsorption), S2 | ✓ |
| B02 | Signal climbs at low concentration, then levels off; Langmuir isotherm shape | S1: quasi-plateau ≥10⁻⁵ M, "typical of surface adsorption", consistent with Langmuir | ✓ — shape is typical, not universal; the curve is labeled illustrative |
| B02 | Calibration curve and site-filling graphic | — | **Illustrative** |
| B03 | Same sample at different spots gives different intensities because each spot samples different hot spots | S3 (local optical field variations at hot spots hinder quantitation), S4 | ✓ |
| B03 | Bar heights | — | **Illustrative** |
| B04 | Internal standard = reference molecule on the same surface; ratio is steadier than raw signal | S2, S3 (internal standards for spatial/temporal calibration) | ✓ |
| B04 | Caveats: competes for surface sites, can overlap analyte peaks, can photodegrade | S3 (limitations of Raman-tag standards: spatial occupation competition, spectral interference, photodegradation) | ✓ |
| B04 | Ratio bars drawn equal | — | **Idealized**, labeled on screen |
| B05 | Results still differ between labs; good analytical practice matters | S2 ("can differ significantly" between laboratories) | ✓ |
| B05 | "Calibrate within the range where the response is still rising" | standard analytical practice; follows from S1 | ✓ as recommendation |
| B06 | Viewer prompt | — | no factual claim |

## Disclosure

Narration is synthetic (Kokoro TTS, voice `am_liam`), presented as "Liam, in for Kumar Karthik." Scripts, scenes, and this check were AI-assisted (Claude) and reviewed by the author.
