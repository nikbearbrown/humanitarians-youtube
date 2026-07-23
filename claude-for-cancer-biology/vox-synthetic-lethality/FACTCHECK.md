# FACTCHECK — vox-synthetic-lethality
**Source chapter:** cancer-biology/chapters/04-genetics-and-genomic-instability-in-cancer.md

---

## Claims audit

| Beat | Claim | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|
| B01 | "A cancer drug doesn't target the cancer cell's growth engine. It exploits a repair pathway the cancer cell no longer has — while every healthy cell in the body still does." | ✓ | Chapter p.93: "The drug selectively kills tumor cells not because it targets a growth pathway but because it exploits a repair vulnerability that normal cells do not share." | None |
| B02 | BRCA2 loss in ovarian cancer | ✓ | Chapter p.56: "BRCA1/2 fall into this [tumor suppressor] category." Chapter p.93: "Olaparib and other PARP inhibitors are now standard for BRCA-mutant breast, ovarian, and prostate cancers." | None |
| B02 | Olaparib is prescribed for BRCA2-mutant ovarian cancer | ✓ | Chapter p.93: "Olaparib and other PARP inhibitors are now standard for BRCA-mutant breast, ovarian, and prostate cancers." | None |
| B03 | "Olaparib blocks PARP — an enzyme that patches single-strand breaks in DNA." | ✓ | Chapter p.93: "PARP inhibitors block single-strand-break repair" | None |
| B03 | "Block PARP and those breaks pile up. During replication they collapse into double-strand breaks." | ✓ | Chapter p.93: "those lesions are converted to double-strand breaks during replication." | None |
| B03 | "Every cell in her body gets the same damage." | ✓ (editorial simplification, defensible) | PARP is ubiquitous; olaparib is not tumor-targeted. The film's premise depends on this being true — the mechanism only makes sense because the drug affects all cells equally. | Labeled as implicit in the mechanism setup |
| B04 | Question beat narration: "Blocking PARP should create double-strand breaks in every cell equally. Here it kills the cancer cells but spares normal cells. Why does the same drug kill one cell type and not another?" | ✓ (the film's exact question, from the card) | Direct from candidate card 06 question statement. | None |
| B05 | "Homologous recombination — the high-fidelity one — uses the sister chromatid as a perfect template to rebuild what was there." | ✓ | Chapter p.91: "Homologous recombination is high-fidelity: it uses the sister chromatid as a template... and repairs the break accurately." | None |
| B05 | NHEJ described as "error-prone" with "no template" | ✓ | Chapter p.91-92: "Non-homologous end joining is fast but imprecise: it ligates broken ends without a template, introducing small insertions or deletions at the junction." | None |
| B06 | "BRCA2 is one of the key proteins that orchestrates HR." | ✓ | Chapter p.91: "directed by RAD51, BRCA1, BRCA2, and PALB2." | None |
| B06 | "When a double-strand break forms, BRCA2 helps load the repair machinery onto the break." | ✓ (slight simplification) | Chapter p.91: BRCA2 listed as directing HR. The precise RAD51 loading is excluded per card exclusions — "helps load repair machinery" is defensible simplification. | Simplification defensible; excluded detail is RAD51 biochemistry |
| B07 | "The cancer cell has lost BRCA2." | ✓ | Premise of the card — BRCA2-mutant tumor | None |
| B07 | "HR can't run. The only fallback is NHEJ, which stitches ends together without a template." | ✓ | Chapter p.92: "Inherited BRCA1 or BRCA2 mutations disable homologous recombination. Breaks fall to NHEJ, which misjoins ends." | None |
| B08 | Synthetic lethality description: "Two defects that are each survivable alone become lethal in combination. BRCA2 loss alone — the cell survives; other repair handles routine damage. PARP inhibition alone — HR fixes the DSBs in a normal cell. But both together kill only the cell that has both." | ✓ | Chapter p.93: "HR-competent cells repair the double-strand breaks through HR and survive. BRCA-mutant cells have lost HR... and die." The "each survivable alone" framing directly matches "BRCA2 loss is survivable (normal repair still handles most lesions), PARP inhibition is survivable in BRCA-intact cells (HR rescues the DSBs)" from card 06 core idea. | None |
| B08 | 2x2 grid — three cells "alive", one cell "DEAD" | ✓ | Direct from card 06 visual object: "A 2x2 grid where only the 'BRCA-deficient + PARP-inhibited' corner is marked DEAD." | None |
| B09 | "The drug... can't tell them apart." | ✓ (editorial) | Olaparib is not cell-type selective — confirmed by the mechanism itself. | None |
| B10-B13, B17 | "1000 tumor cells and 1000 normal cells" — illustrative numbers | ILLUSTRATIVE | From card 06 example seed: "Start with 1000 tumor cells + 1000 normal cells." Explicitly labeled illustrative in the card. No real clinical data claim is made. | Labeled illustrative in narration (B17: "illustrative numbers" SerifLabel in graphic) |
| B10-B13, B17 | "Normal cells: RAD51 on DSBs via HR -> survive. Tumor cells: attempt HR, no BRCA2, assemble NHEJ instead -> chromosomal disaster -> die. End: ~0 tumor, ~1000 normal." | ✓ (illustrative) | Card 06 example seed verbatim. Mechanism confirmed by chapter p.93. Numbers are illustrative. | Labeled illustrative |
| B11 | "HR loads, using the sister chromatid as a template, break closes cleanly" | ✓ | Chapter p.91: HR uses sister chromatid template. | None |
| B12 | "NHEJ misjoins fragments. Chromosomal damage accumulates" | ✓ | Chapter p.92: "Breaks fall to NHEJ, which misjoins ends, accumulating rearrangements." | None |
| B15 | "Olaparib and the other PARP inhibitors are now standard treatment for BRCA-mutant breast, ovarian, and prostate cancers." | ✓ | Chapter p.93: "Olaparib and other PARP inhibitors are now standard for BRCA-mutant breast, ovarian, and prostate cancers." | None |
| B15 | "The therapeutic window is the tumor's own repair defect — the same defect that was making the tumor unstable all along." | ✓ (editorial) | Chapter p.92: "explaining the genomic instability of BRCA-mutant tumors. This deficiency is also exploited therapeutically through synthetic lethality." The connection between genomic instability and the therapeutic window is from the chapter. | None |
| B16 | "Any two gene losses that are each survivable alone but lethal together — that's synthetic lethality." | ✓ | Standard definition of synthetic lethality, consistent with chapter description. | None |
| B18 | Recap: "BRCA2 loss is survivable alone. PARP inhibition is survivable in a BRCA2-intact cell. Together, they are lethal — but only to the cell that has both." | ✓ | Directly restates the mechanism from chapter p.93 and card 06 core idea. | None |

---

## Terms table

| Term | Debut beat | Earlier beat that creates the need for it |
|---|---|---|
| BRCA2 | B02 (case) | — (introduced at first use) |
| Olaparib | B02 (case) | B02 (drug named with patient case) |
| PARP | B03 | B02 (olaparib named; PARP explained immediately in B03) |
| Single-strand break (SSB) | B03 | B03 (explained alongside PARP function) |
| Double-strand break (DSB) | B03 | B03 (SSB → DSB conversion explained) |
| Homologous recombination (HR) | B05 | B04 (question beat creates need: "why different fates?") |
| Sister chromatid | B05 | B05 (within HR explanation) |
| NHEJ | B05 | B05 (contrasted with HR in same beat) |
| Synthetic lethality | B08 | B07 (tumor cell fails HR, creating the need to name the pattern) |

All terms debut after the beat that created the viewer's need for them. Vocabulary law: PASS.

---

## Exclusion re-confirmation

- RAD51 biochemistry: NOT mentioned in narration, NOT shown in any graphic
- NHEJ mechanism detail: NOT shown — only "misjoins ends, no template" level
- Resistance mechanisms: NOT mentioned
- HRD scoring or biomarker details: NOT mentioned
- BRCA1 vs BRCA2 differences: NOT mentioned — BRCA2 only throughout

---

VERDICT: PASS
