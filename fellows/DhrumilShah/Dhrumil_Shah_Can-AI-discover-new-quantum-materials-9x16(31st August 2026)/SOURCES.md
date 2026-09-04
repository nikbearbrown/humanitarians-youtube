# SOURCES — Can AI Discover New Quantum Materials?

> **Shared with the 16:9 cut.** This document describes the film's *content* —
> its claims, sources, and narration — which is identical in both aspect
> ratios. It is copied here so this folder is self-contained. If you change a
> claim, change it in both cuts; nothing here is 9:16-specific.

Every factual claim made on screen traces to an entry below. Entries are
grouped by the scene that asserts them. The film displays a persistent
`SOURCE ·` tag at the moment of each claim; this file is the long form of
those tags.

Confidence column:
- **HIGH** — a foundational, uncontested result the presenter can defend from
  standard references.
- **VERIFY** — correct to the best of the author's knowledge, but the exact
  figure shown on screen should be checked against the primary paper before
  the film is made public. These are listed again in `FACTCHECK.md`.

---

## Scene 02 — the problem and the measured Tc record

| # | Claim on screen | Source | Confidence |
|---|---|---|---|
| 1 | Superconductivity discovered 1911; mercury, ~4.2 K | Kamerlingh Onnes, H. (1911). *Communications from the Physical Laboratory of the University of Leiden*, No. 120b, 122b, 124c. | HIGH |
| 2 | Below Tc electrons bind into pairs; resistance is exactly zero | Bardeen, J., Cooper, L. N., & Schrieffer, J. R. (1957). "Theory of Superconductivity." *Physical Review* 108(5), 1175–1204. | HIGH |
| 3 | Pb ~7.2 K (1913) | Standard reference value; Kamerlingh Onnes, Leiden. | HIGH |
| 4 | NbN ~16 K (1941) | Aschermann, G., Friederich, E., Justi, E., & Kramer, J. (1941). *Physikalische Zeitschrift* 42, 349. | VERIFY |
| 5 | Nb₃Sn ~18 K (1954) | Matthias, B. T., Geballe, T. H., Geller, S., & Corenzwit, E. (1954). *Physical Review* 95, 1435. | VERIFY |
| 6 | Nb₃Ge ~23.2 K (1973) | Gavaler, J. R. (1973). "Superconductivity in Nb–Ge films above 22 K." *Applied Physics Letters* 23, 480. | HIGH |
| 7 | La–Ba–Cu–O ~35 K (1986) — the cuprate break | Bednorz, J. G., & Müller, K. A. (1986). "Possible high Tc superconductivity in the Ba−La−Cu−O system." *Zeitschrift für Physik B* 64, 189–193. Nobel Prize in Physics 1987. | HIGH |
| 8 | YBCO ~92 K (1987) — first above liquid nitrogen | Wu, M. K., et al. (1987). "Superconductivity at 93 K in a new mixed-phase Y-Ba-Cu-O compound system at ambient pressure." *Physical Review Letters* 58, 908. | HIGH |
| 9 | BSCCO ~110 K (1988) | Maeda, H., Tanaka, Y., Fukutomi, M., & Asano, T. (1988). *Japanese Journal of Applied Physics* 27, L209. | VERIFY |
| 10 | Hg–Ba–Ca–Cu–O ~133 K (1993) — ambient-pressure record | Schilling, A., Cantoni, M., Guo, J. D., & Ott, H. R. (1993). "Superconductivity above 130 K in the Hg–Ba–Ca–Cu–O system." *Nature* 363, 56–58. | HIGH |
| 11 | MgB₂ 39 K (2001) | Nagamatsu, J., Nakagawa, N., Muranaka, T., Zenitani, Y., & Akimitsu, J. (2001). "Superconductivity at 39 K in magnesium diboride." *Nature* 410, 63–64. | HIGH |
| 12 | LaFeAsO(F) 26 K (2008) — the iron-pnictide break | Kamihara, Y., Watanabe, T., Hirano, M., & Hosono, H. (2008). "Iron-Based Layered Superconductor La[O₁₋ₓFₓ]FeAs (x = 0.05–0.12) with Tc = 26 K." *Journal of the American Chemical Society* 130, 3296–3297. | HIGH |
| 13 | H₃S 203 K at 155 GPa (2015) | Drozdov, A. P., Eremets, M. I., Troyan, I. A., Ksenofontov, V., & Shylin, S. I. (2015). "Conventional superconductivity at 203 kelvin at high pressures in the sulfur hydride system." *Nature* 525, 73–76. | HIGH |
| 14 | LaH₁₀ ~250 K at ~170 GPa (2019) | Drozdov, A. P., et al. (2019). "Superconductivity at 250 K in lanthanum hydride under high pressures." *Nature* 569, 528–531. See also Somayazulu, M., et al. (2019). *Physical Review Letters* 122, 027001. | HIGH |
| 15 | 77 K reference line = liquid nitrogen boiling point | Standard physical constant (77.36 K at 1 atm). | HIGH |
| 16 | 293 K reference line = room temperature | Conventional value (20 °C). | HIGH |

---

## Scene 03 — what enters the model

| # | Claim on screen | Source | Confidence |
|---|---|---|---|
| 17 | The standard public training table: 21,263 superconductors, 81 features, 1 measured Tc target | Hamidieh, K. (2018). "A data-driven statistical model for predicting the critical temperature of a superconductor." *Computational Materials Science* 154, 346–354. DOI: 10.1016/j.commatsci.2018.07.052 | HIGH |
| 18 | Mirrored as the UCI "Superconductivty Data" set | UCI Machine Learning Repository, *Superconductivty Data* Data Set (donated 2018). | HIGH |
| 19 | Underlying measurements come from NIMS SuperCon | National Institute for Materials Science (Japan), SuperCon database. | HIGH |
| 20 | Features are elemental properties averaged/weighted across the formula — atomic mass, electron affinity, thermal conductivity, valence, atomic radius, fusion heat, density, electronegativity | Hamidieh 2018, §2 (feature construction). | HIGH |
| 21 | Crystal structure, phonon spectrum, band structure and synthesis route are **not** in the table | Hamidieh 2018, §2 — the feature set is composition-derived only. | HIGH |

---

## Scene 04 — the method

| # | Claim on screen | Source | Confidence |
|---|---|---|---|
| 22 | Gradient-boosted trees regressing Tc from composition features | Hamidieh 2018, §3. | HIGH |
| 23 | **±9.5 K out-of-sample RMSE on a held-out split** | Hamidieh 2018, §4 (reported XGBoost out-of-sample performance). | **VERIFY** |

> Claim 23 is the single most prominent number in the film (rendered at
> 190 px). Check it against the published table before the film is made
> public. See `FACTCHECK.md`.

---

## Scene 06 — the extrapolation limit

| # | Claim on screen | Source | Confidence |
|---|---|---|---|
| 24 | The cuprates (1986) arrived from outside what was then known | Bednorz & Müller 1986 (as #7). Interpretation that this was out-of-distribution is the presenter's, and is labelled as such. | HIGH (fact) / PRESENTER (interpretation) |
| 25 | The iron pnictides (2008) arrived from outside what was then known | Kamihara et al. 2008 (as #12). Same labelling. | HIGH (fact) / PRESENTER (interpretation) |

---

## Scene 07 — the confirmation chain

| # | Claim on screen | Source | Confidence |
|---|---|---|---|
| 26 | Field expulsion (the Meissner effect) is a defining test, distinct from zero resistance | Meissner, W., & Ochsenfeld, R. (1933). "Ein neuer Effekt bei Eintritt der Supraleitfähigkeit." *Naturwissenschaften* 21, 787–788. | HIGH |
| 27 | Four-probe resistivity is the standard zero-resistance measurement | Standard experimental practice. | HIGH |
| 28 | DFT / formation-energy screening estimates whether a candidate can exist | Jain, A., et al. (2013). "Commentary: The Materials Project: A materials genome approach to accelerating materials innovation." *APL Materials* 1, 011002. | HIGH |

---

## Scene 08–09 — the LK-99 test case

| # | Claim on screen | Source | Confidence |
|---|---|---|---|
| 29 | July 2023: a preprint claimed a room-temperature, ambient-pressure superconductor (LK-99, a copper-doped lead apatite) | Lee, S., Kim, J.-H., & Kwon, Y.-W. (2023). "The First Room-Temperature Ambient-Pressure Superconductor." arXiv:2307.12008. Companion: arXiv:2307.12037. | HIGH |
| 30 | Multiple independent groups failed to reproduce superconductivity | Broad replication record, August–September 2023, reported across the physics literature and in *Nature* news coverage. | HIGH |
| 31 | The sharp resistivity drop was attributed to a Cu₂S impurity phase transition | Replication analyses identifying copper sulfide as the origin of the resistivity feature, August 2023. | HIGH |
| 32 | Partial levitation was attributed to ferromagnetic impurity rather than flux pinning | Replication analyses, August 2023. | HIGH |
| 33 | No Meissner effect was confirmed | Replication record, 2023. | HIGH |

---

## Explicitly NOT used in this film

The project brief supplied two 2026 results — an Oak Ridge National Laboratory
autonomous thin-film discovery loop reporting 10–100× acceleration, and a
system screening more than 1.3 million candidate structures with two
experimentally confirmed superconductors.

**Neither claim appears in this film.** No citation, DOI, or paper was supplied
for either, and neither could be verified at build time. Under the project's own
rule — no source, no verdict — an unverifiable claim does not go on screen.

If the primary references become available, both belong in Scene 05 (the funnel)
as the strongest available evidence that the funnel is more than a schematic.
`FACTCHECK.md` holds a prepared, empty slot for each.

---

## Presenter-authored material (not sourced, and labelled on screen)

| Item | Where | On-screen label |
|---|---|---|
| The **CLAIM** five-axis review framework | Scenes 02, 09, 10 | `PRESENTER FRAMEWORK · CLAIM` |
| The Search → Rank → Synthesize → Measure → Confirm pipeline | Scene 01 | Stated in the source tag as this film's review structure |
| The screening funnel proportions | Scene 05 | `ILLUSTRATIVE SCREENING SCHEMATIC` |
| "It learned to interpolate a table of things we already found" | Scene 04 | Presenter interpretation of the training objective |
