# FACTCHECK — vox-protein-level-loss
## Why a Cancer With Intact Tumor Suppressor Genes Still Behaves As If They Are Missing

Source chapter: `cancer-biology/chapters/10-cancer-etiology-viral-and-bacterial-carcinogens.md`

---

## Claim-by-claim audit

| # | Beat | Claim | Verdict | Source / derivation | Fix if needed |
|---|------|-------|---------|---------------------|---------------|
| 1 | B01 | TP53 and RB1 are tumor suppressor genes | ✓ | Chapter 10, standard oncology; p53 and Rb are the canonical tumor suppressors | — |
| 2 | B01 | Sequencing can report TP53 and RB1 as wild-type | ✓ | Standard clinical sequencing; confirmed by card premise and chapter framing | — |
| 3 | B02 | HPV-positive cervical cancer biopsy with wild-type TP53 and RB1 coding sequences | ✓ | Chapter 10: "E6 and E7 do to a cell what mutations in TP53 and RB1 would do — but acutely, as a consequence of infection rather than through accumulated mutations." The premise is that HPV achieves functional loss without sequence mutation. | — |
| 4 | B03 | p53 protein is undetectable in HPV-positive cervical cancer | ✓ | Chapter 10: "E6 recruits a cellular ubiquitin ligase — E6AP — and redirects it to target p53 for proteasomal destruction." Active destruction of the protein is the mechanism. | — |
| 5 | B03 | Cells enter S phase without restraint | ✓ | Chapter 10: "E7 forces this release regardless of growth signals. The cell enters S phase whether it should or not." | — |
| 6 | B05 | Standard tumor suppressor loss requires a mutation | ✓ | Chapter 10: "What takes years of somatic mutation in other cancers happens in one step here." Implies that somatic mutation is the standard route. | — |
| 7 | B08 | E6 recruits E6AP (a cellular ubiquitin ligase) to redirect the ubiquitin machinery toward p53 | ✓ | Chapter 10: "E6 recruits a cellular ubiquitin ligase — E6AP — and redirects it to target p53 for proteasomal destruction." Exact match. | — |
| 8 | B08 | The proteasome degrades p53 | ✓ | Chapter 10: "target p53 for proteasomal destruction." Direct quote. | — |
| 9 | B08 | The TP53 gene remains intact / no sequence change | ✓ | Chapter 10: "The genome's guardian is eliminated, quietly, by a protein that contains no mutated DNA and leaves no sequence change behind." Direct quote. | — |
| 10 | B09 | Normally Rb sequesters E2F until cyclin D–CDK4/6 phosphorylates Rb | ✓ | Chapter 10: "Rb sequesters the transcription factor E2F, preventing it from activating S-phase genes until cyclin D–CDK4/6 phosphorylates Rb and releases E2F as a controlled signal" | — |
| 11 | B09 | E7 binds Rb and forces release of E2F regardless of growth signals | ✓ | Chapter 10: "E7 binds the retinoblastoma protein Rb and disrupts the Rb–E2F complex… E7 forces this release regardless of growth signals." | — |
| 12 | B10 | Genome sequencing reads nucleotide sequence and cannot detect protein-level inactivation | ✓ | Chapter 10: "The genome's guardian is eliminated, quietly, by a protein that contains no mutated DNA and leaves no sequence change behind." The logic is direct: if there is no sequence change, sequencing cannot detect the event. | — |
| 13 | B11 | Illustrative example: 100 cervical cancers sequenced; TP53 mutations in 10; 90 wild-type by sequencing; 70 of 90 wild-type have absent p53 protein by IHC | ILLUSTRATIVE | Explicitly labeled as illustrative. The discordance between sequencing and IHC in HPV-positive cervical cancer is real and documented; the specific proportions (10/90/70) are invented for pedagogical clarity and labeled as such. | Label "illustrative" in narration ✓ already done. |
| 14 | B11 | Discordance traces to E6 in HPV-positive cases | ✓ | Chapter 10: the E6 mechanism is the entire explanation for absent p53 in HPV-positive tumor with intact TP53 gene. | — |
| 15 | B12 | The gene is a blueprint; E6/E7 destroy the product | Editorial metaphor | This is a simplified pedagogical metaphor, not a molecular claim. Labeled as an editorial framing device. | None — metaphor is accurate in spirit |

---

## Terms table

| Term | Debuts at beat | Prior beat that created the need |
|------|----------------|----------------------------------|
| tumor suppressor | B01 | — (prerequisite; stated in card) |
| TP53 / RB1 (gene names) | B01 | B01 |
| wild-type | B01 | B01 (sequencing context makes meaning clear) |
| p53 protein | B03 | B01 introduced the gene; B03 introduces the protein distinction |
| Rb protein | B03 | B01 introduced RB1 gene; B03 introduces protein |
| E2F | B09 | B09: "E7 binds Rb and forces E2F loose" — need for name created by the mechanism |
| S phase | B09 | B05 (cells cycle without restraint) creates the need; B09 names S phase |
| ubiquitin | B08 | B07 ("virus expresses proteins that act on proteins") creates the need for the disposal mechanism |
| E6AP | B08 (spoken as "cellular ubiquitin ligase — E6AP") | B08 |
| proteasome | B08 | B08 (introduced alongside ubiquitin in same beat) |
| immunohistochemistry / IHC | B11 | B10 (the implication that a different assay is needed creates the need for its name) |
| precision oncology | B13 | B04 question beat sets up the clinical framing |

---

## Exclusion audit

- No HPV life cycle beyond E6/E7 mechanism: ✓ absent
- No HPV vaccine: ✓ absent
- No CIN staging: ✓ absent
- No high-risk vs low-risk HPV type taxonomy: ✓ absent (HPV named but type taxonomy omitted)
- No insertional mutagenesis: ✓ absent
- No HBV/HCV: ✓ absent

---

## Illustrative number audit

All numbers in B11 (100 cancers, 10 TP53 mutated, 90 wild-type, 70 absent by IHC, 20 present by IHC) are:
- Invented for pedagogy
- Labeled "illustrative" in narration ("Here's an illustrative example")
- Consistent with the card's example seed
- Directionally plausible (IHC-sequencing discordance in HPV+ cervical cancer is documented in the literature; specific proportions are made up)

---

VERDICT: PASS
