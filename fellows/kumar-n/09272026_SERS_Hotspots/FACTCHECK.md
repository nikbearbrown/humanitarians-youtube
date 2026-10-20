# FACTCHECK — sers-hot-spots

**Reel:** Hot Spots: Where SERS Signal Comes From
**Type:** standalone explainer (not a paper update)
**Checked:** 2026-10-18. Every narrated or on-screen factual claim is listed below.

## Sources

| ID | Source | Status |
|----|--------|--------|
| S1 | Fang, Y., Seong, N.-H., & Dlott, D. D. (2008). Measurement of the distribution of site enhancements in surface-enhanced Raman scattering. *Science* 321, 388–392. Summarised in Fang's dissertation (Univ. of Illinois, 2011, hdl:2142/24454) and the university's 2008 release | peer-reviewed; figures checked against dissertation abstract and release |
| S2 | Le Ru, E. C., Etchegoin, P. G., & Meyer, M. (2006). Enhancement factor distribution around a single SERS hot-spot and its relation to single molecule detection. *J. Chem. Phys.* 125, 204701. doi:10.1063/1.2390694 | peer-reviewed |
| S3 | Dewanjee, U., et al. (2026). Next-generation SERS probes. *Nanomaterials* 16(10), 628 — cited in the author's paper for the |E|⁴ scaling | peer-reviewed (via author's paper) |
| S4 | Author's Paper 2 draft, §2.6 and §3.4 (validation practice) | internal |

## Claims

| Beat | Claim (as narrated / shown) | Source | Verdict |
|------|-----------------------------|--------|---------|
| B00 | The same substrate measured at different spots can give different spectra | S1, S2, S4 | ✓ |
| B01 | Most SERS signal comes from a tiny number of hot spots | S1 (63 ppm of sites → 24% of signal; reversed power-law distribution) | ✓ — "most" is the general picture; S1's specific figure is 24% from the very hottest sites, stated precisely in B04 |
| B02 | Enhancement scales roughly with the fourth power of the local field | S3 | ✓ shown as "approximately" |
| B02 | Field ×2 → signal ×16; field ×10 → signal ≈ ×10,000 | arithmetic (2⁴, 10⁴) under the |E|⁴ approximation | ✓ |
| B03 | Strongest fields occur mostly in nanometre-scale gaps between metal particles | S2 (gap hot spots), S3 | ✓ |
| B03 | Elsewhere the enhancement is far weaker | S1 (broad distribution with a long tail), S2 | ✓ |
| B03 | Two-particle diagram | — | **Schematic**, labeled on screen |
| B04 | Fang, Seong & Dlott, 2008, silver-coated nanospheres | S1: benzenethiolate on 330 nm Ag-coated nanospheres, 532 nm | ✓ |
| B04 | Hottest sites: 63 molecules per million (0.0063%) | S1 | ✓ (63 / 1,000,000 = 0.0063%) |
| B04 | Those sites produced 24% of the total signal | S1 | ✓ |
| B05 | Each spot samples a different set of hot spots, so spectra vary within a substrate | S1, S2 | ✓ |
| B05 | Splitting one substrate's spectra across train and test lets a model learn the substrate | S4 §2.6, §3.4 | ✓ as the paper's methodological argument |
| B05 | Spectra and hot-spot dots | — | **Illustrative**, not data |
| B06 | Six summary lines | S1–S4 | ✓ |
| B07 | Viewer prompt | — | no factual claim |

## Notes

- S1's result is for one substrate type and one probe molecule; the video presents it as a measured example of how lopsided enhancement can be, not as a universal constant.
- S2 additionally notes that no known substrate shows single-molecule-level enhancement (~10⁸–10¹⁰) uniformly across its surface; consistent with, but not quoted in, the video.

## Disclosure

Narration is synthetic (Kokoro TTS, voice `am_liam`), presented as "Liam, in for Kumar Karthik." Scripts, scenes, and this check were AI-assisted (Claude) and reviewed by the author.
