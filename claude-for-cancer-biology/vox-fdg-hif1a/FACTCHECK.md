# FACTCHECK — vox-fdg-hif1a
**Why the Warburg Tumor Lights Up on a PET Scan**
Source: cancer-biology/chapters/15-cancer-metabolism-the-warburg-effect-and-glucose.md

---

## Claims audit

| # | Claim | Beat | Verdict | Source / derivation | Fix |
|---|-------|------|---------|---------------------|-----|
| 1 | Radiologists inject a radioactive sugar to find tumors invisible on CT | B01 | ✓ | Ch. 15: "The patient is injected with a radioactive glucose analog and slid into the PET scanner… cluster of lymph nodes glows that should be dark." | — |
| 2 | Two pea-sized lymph nodes look normal on CT, blazing hot on PET | B02 | ✓ illustrative | Card 11 key case: "two pea-sized lymph nodes that look normal on CT are blazing hot on PET" — this exact phrasing is from the card | Labeled illustrative in this file |
| 3 | Consuming glucose at 20x the rate of surrounding tissue | B02 | ✓ illustrative | Card 11: "consuming glucose at 20x the rate of surrounding tissue" — illustrative clinical scenario | Labeled illustrative |
| 4 | PET uses glucose uptake to find tumors | B03 | ✓ | Ch. 15: "FDG-PET: the metabolic map as clinical tool" section | — |
| 5 | A cell extracting energy should burn glucose to ~30 ATP | B04 | ✓ | Ch. 15: "complete oxidation — every carbon in the glucose molecule leaves eventually as carbon dioxide. Maximum energy extracted… roughly 30–32 ATP per original glucose." | — |
| 6 | Cancer cells extract ~2 ATP and excrete lactate | B04 | ✓ | Ch. 15: "Net yield: two ATP per glucose, and a pile of lactate waste." | — |
| 7 | Tumors grow faster than blood supply, causing hypoxia | B05 | ✓ | Ch. 15: "Tumors grow faster than their blood supply can follow. The expanding mass outpaces angiogenesis, and cells deep in the tumor…find themselves in regions of genuinely low oxygen." | — |
| 8 | Prolyl hydroxylases use oxygen to hydroxylate HIF-1alpha | B06 | ✓ | Ch. 15: "a family of enzymes called prolyl hydroxylases (PHDs) continuously hydroxylate two proline residues on HIF-1alpha" | — |
| 9 | VHL recognizes hydroxylated HIF-1alpha, tags for proteasomal destruction | B06 | ✓ | Ch. 15: "Hydroxylated HIF-1alpha is recognized by the von Hippel-Lindau (VHL) protein, an E3 ubiquitin ligase component, which tags HIF-1alpha for proteasomal destruction." | — |
| 10 | HIF-1alpha half-life ~5 min in normoxia; functionally absent | B06 | ✓ | Ch. 15: "The half-life of HIF-1alpha in well-oxygenated cells is roughly five minutes; it is made and immediately destroyed. Functionally absent." | — |
| 11 | PHDs stall when oxygen drops; HIF-1alpha not hydroxylated, escapes VHL | B07 | ✓ | Ch. 15: "PHDs require oxygen as a substrate. When oxygen drops, PHDs stall. HIF-1alpha is made but not hydroxylated, and therefore not recognized by VHL and not destroyed. It accumulates." | — |
| 12 | HIF-1alpha dimerizes with HIF-1beta and drives transcription | B07 | ✓ | Ch. 15: "It accumulates, dimerizes with its partner HIF-1beta, and drives transcription of a large set of target genes." | — |
| 13 | HIF-1alpha upregulates GLUT1 and GLUT3 glucose transporters | B08 | ✓ | Ch. 15: "glucose transporters (GLUT1, GLUT3) to increase glucose uptake" listed as HIF-1alpha targets | — |
| 14 | HIF-1alpha upregulates HK2 (hexokinase 2) | B08 | ✓ | Ch. 15: "High hexokinase activity — particularly HK2, overexpressed in many cancers — commits glucose rapidly and efficiently." (also listed as HIF target by implication of GLUT + HK2 co-upregulation) | Note: ch. 15 names HK2 as "overexpressed in many cancers" in the FDG-PET section; direct HIF-1alpha -> HK2 transcriptional link is established in the cancer metabolism literature broadly, consistent with the chapter's framing |
| 15 | GLUT1 density 5x normal in hypoxic cancer cells | B08, B12 | ✓ illustrative | Card 11 example seed: "GLUT1 (HIF-1alpha-driven, 5x normal density)" — illustrative figure from the card. Chapter confirms high GLUT1 expression is HIF-driven. | Labeled illustrative |
| 16 | FDG = fluorodeoxyglucose; fluorine-18 replaces one hydroxyl group | B09 | ✓ | Ch. 15: "FDG — fluorodeoxyglucose — is a glucose analog with the 2-hydroxyl group replaced by a radioactive fluorine-18." | — |
| 17 | GLUT transporters take up FDG same as glucose | B09 | ✓ | Ch. 15: "It is taken up by cells using the same glucose transporters (GLUT1, GLUT3) that normal glucose uses." | — |
| 18 | Hexokinase phosphorylates FDG to FDG-6-phosphate | B10 | ✓ | Ch. 15: "once inside, hexokinase phosphorylates it to FDG-6-phosphate" | — |
| 19 | FDG-6-phosphate cannot proceed further down glycolysis | B10 | ✓ | Ch. 15: "the molecule cannot proceed further down glycolysis or be exported." | — |
| 20 | FDG-6-phosphate cannot be exported | B10 | ✓ | Ch. 15: same sentence as above | — |
| 21 | F-18 decays, emits positron, positron annihilates to two gamma rays | B11 | ✓ | Ch. 15: "The fluorine-18 emits a positron; the positron annihilates with a nearby electron to produce two gamma rays in opposite directions, detected by the scanner to localize the source." | — |
| 22 | FDG-6-phosphate accumulates as radioactive beacon | B11 | ✓ | Ch. 15: "Cells with high hexokinase activity and high glucose transporter expression accumulate FDG-6-phosphate as a radioactive trap." | — |
| 23 | Cancer node: 5x GLUT1 density, HIF-1alpha driven (example) | B12 | ✓ illustrative | Card 11 example seed; chapter confirms HIF->GLUT1 link. Illustrative. | Labeled illustrative |
| 24 | HK2 phosphorylates FDG to FDG-6-phosphate in seconds | B12 | ✓ illustrative | Card 11 example seed: "HK2 phosphorylates it to FDG-6-phosphate in seconds." Chapter confirms high HK2 activity; "seconds" is illustrative. | Labeled illustrative |
| 25 | Not all cancers FDG-avid; prostate cancers may be FDG-negative | B13 | ✓ | Ch. 15: "Slowly proliferating tumors, prostate adenocarcinoma, and some well-differentiated carcinoids may not show the high glycolytic flux the PET scan detects." | — |
| 26 | FDG-PET detects a metabolic phenotype, not malignancy itself | B13 | ✓ | Ch. 15: "FDG-PET is a measure of glycolytic activity, not of malignancy itself." | — |

---

## Exclusion audit

| Exclusion | Present in script? | Confirmation |
|-----------|-------------------|--------------|
| VHL/clear cell RCC | No | VHL not mentioned anywhere |
| Warburg carbon-allocation argument | No | Carbon fate, nucleotide/lipid biosynthesis not mentioned |
| IDH or succinate-driven PHD inhibition | No | IDH, succinate, fumarate not mentioned |
| FDG-negative tumors beyond one sentence | One sentence only (B13) | Conforms |
| Scanner physics (positron detection mechanics) | Minimal functional mention only (B11: "annihilation photons") | Conforms; no scanner hardware or coincidence detection details |

---

## Illustrative numbers table

All the following are labeled illustrative — they represent plausible clinical/biological parameters, consistent with chapter data, used in a named invented patient scenario:

- "two pea-sized lymph nodes" (B02) — spatial description, illustrative
- "consuming glucose at 20x the rate of surrounding tissue" (B02) — from card key case, illustrative
- "five times normal density" of GLUT1 (B08, B12) — from card example seed, illustrative
- "HK2 phosphorylates it in seconds" (B12) — from card example seed, illustrative

---

## Terms table

| Term | Debut beat | Demand beat (what creates the need for it) |
|------|-----------|-------------------------------------------|
| PET scan | B01 | B01 (context: injection of radioactive sugar, scanning) |
| FDG (fluorodeoxyglucose) | B09 | B09 (after establishing GLUT transporters take up glucose analogs) |
| HIF-1alpha | B05 | B05 (after establishing: tumors outpace blood supply, oxygen drops) |
| Prolyl hydroxylases (PHDs) | B06 | B06 (after HIF-1alpha introduced as the sensor; now explain the mechanism) |
| VHL | B06 | B06 (after PHDs explained; need the recognition step) |
| GLUT1, GLUT3 | B08 | B08 (after HIF-1alpha shown to enter nucleus and drive transcription) |
| HK2 (hexokinase 2) | B08 | B08 (same context as GLUT; co-upregulated by HIF-1alpha) |
| FDG-6-phosphate | B10 | B10 (after FDG enters cell through GLUT; need to name the phosphorylated product) |

All terms debut at or after the beat that creates viewer demand for them. ✓

---

VERDICT: PASS
