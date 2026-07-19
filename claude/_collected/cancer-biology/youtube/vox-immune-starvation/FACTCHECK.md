# FACTCHECK — vox-immune-starvation

Source chapter: `cancer-biology/chapters/16-cancer-metabolism-lipids-amino-acids-and-the-tumor-microenvironment.md`

---

## Claims Table

| Beat | Claim | Verdict | Source / Fix |
|------|-------|---------|--------------|
| B01 | T cells inside a solid tumor are present but failing | PASS | Ch.16: "Activated T cells, like cancer cells, require glucose and glutamine to proliferate and function. In a nutrient-depleted tumor, the cancer cells outcompete the immune cells, contributing to T-cell exhaustion and failure of immune surveillance." |
| B01 | T cells fail not because of hiding/signaling but because of starvation | PASS | Ch.16: "This is immune evasion grounded in metabolic competition rather than in any molecular signaling program." |
| B02 | Interstitial glucose at 0.5 mM vs serum 5 mM | PASS (illustrative) | Card: "Metabolomics of the tumor interstitium shows glucose depleted to 0.5 mM (vs 5 mM in serum)." These numbers are from the card's key case, labeled illustrative per card format. They are clinically plausible; the chapter confirms "Voracious cancer cells deplete the interstitial glucose...to levels well below serum concentrations." |
| B02 | Checkpoint inhibitor removes molecular brake on T cells | PASS | Card key case states "checkpoint inhibitor therapy has removed the molecular inhibitory signals." |
| B04 | Activated T cells must proliferate to kill cancer | PASS | Prerequisite from card: "that T cells must proliferate to kill cancer." |
| B04 | Proliferation and cytokine synthesis require ATP from glucose | PASS | Ch.16: "Activated T cells, like cancer cells, require glucose and glutamine to proliferate and function." |
| B06 | Cancer cells run Warburg glycolysis at ~10x normal rate | PASS (illustrative) | Card: "Cancer cells (10 million): import glucose at 10x normal rate." Labeled illustrative. Consistent with Ch.16 and Ch.15 context. |
| B06 | Interstitial glucose drops from 5 mM to 0.5 mM | PASS (illustrative) | Card key case numbers; labeled illustrative. |
| B08 | Exported Warburg lactate directly suppresses T-cell and NK-cell cytotoxic function | PASS | Ch.16: "Exported lactate is not merely a metabolic waste product. It directly impairs T-cell and NK-cell function at the concentrations found in tumors." |
| B08 | Lactate polarizes macrophages toward tumor-promoting phenotype | PASS | Ch.16: "polarizes macrophages toward a tumor-promoting rather than tumor-killing phenotype." (mentioned in B08 narration context only, not enumerated on screen) |
| B09 | Cancer-associated fibroblasts perform "reverse Warburg effect" | PASS | Ch.16: "Some cancer-associated fibroblasts produce and secrete lactate that cancer cells take up and oxidize — a 'reverse Warburg' arrangement in which the fibroblast does the glycolysis and the cancer cell does the oxidative phosphorylation." |
| B09 | T cells lose access to both glucose and glutamine | PASS | Ch.16: "Voracious cancer cells deplete the interstitial glucose, glutamine, and arginine to levels well below serum concentrations." |
| B10 | Checkpoint inhibitors release inhibitory receptor signaling | PASS | Standard immunology; generically framed per exclusion (no PD-1/PD-L1 mechanism detail). |
| B10 | Metabolic competition model distinct from signaling model | PASS | Ch.16: "This is immune evasion grounded in metabolic competition rather than in any molecular signaling program." |
| B12 | 48-hour timeline — 10M cancer cells, 50K T cells, 1 cm3 region | ILLUSTRATIVE | Card example seed numbers; labeled illustrative in the graphic chip. Not a measured value from a specific study. |
| B12 | Glucose drops from 5 mM to 0.5 mM in 24 hours | ILLUSTRATIVE | Card key case numbers used in example; labeled illustrative. |
| B12 | T cells transition from activated to exhausted in 48 hours | ILLUSTRATIVE | Card: "T cells go from activated to exhausted in 48 hours." Labeled illustrative. The chapter confirms glucose depletion causes T-cell exhaustion; the specific 48h timeline is illustrative. |
| B12 | T cells express PD-1 and TIM-3 markers of exhaustion | PASS | Card key case: "expressing PD-1 and TIM-3, failing to proliferate or produce cytokines." Standard exhaustion markers. |
| B13 | Reverse Warburg: fibroblasts run glycolysis, feed lactate to cancer cells | PASS | Ch.16 (exact quote above). |
| B14 | Warburg glycolysis depletes shared glucose and glutamine below T cell threshold | PASS | Ch.16 throughout; "contribute to T-cell exhaustion and failure of immune surveillance." |
| B14 | Exported lactate suppresses T cells further | PASS | Ch.16: "directly impairs T-cell and NK-cell function." |

---

## Terms Table

| Term | Debut beat | Prior beat creating need |
|------|-----------|------------------------|
| T cells (cytotoxic) | B01 | B01 (cold open sets up the mystery) |
| checkpoint inhibitor | B02 | B02 (the drug whose failure needs explanation) |
| Warburg effect / glycolysis | B06 | B04–B05 (established T cells need glucose; cancer's behavior is the mechanism) |
| interstitial glucose | B02 | B02 (immediately contextualized with numbers) |
| exhaustion (T cell) | B02 | B01 (T cells "failing" established first) |
| PD-1 / TIM-3 | B12 (example) | B03/B10 (inhibitory signals / brakes named generically before) |
| lactate | B08 | B06 (Warburg glycolysis introduced, waste product then named) |
| cancer-associated fibroblasts (CAF) | B09 | B06 (cancer cells as metabolic actors established first) |
| reverse Warburg effect | B09/B13 | B09 (CAFs introduced with their role simultaneously) |
| NK cells | B08 | B04 (immune system actors established) |

---

## Exclusion Audit

The following content was excluded per card specification and confirmed absent:

- **PD-1/PD-L1 checkpoint mechanism**: Not mechanistically described. PD-1 named once in THE EXAMPLE beat B12 as an exhaustion marker only, not as a signaling mechanism. PASS.
- **IDO tryptophan pathway**: Not mentioned anywhere. PASS.
- **Arginine depletion mechanism**: Not mentioned anywhere. PASS.
- **Combination immunotherapy trial data**: No trial names, trial data, or response rates cited. Mechanistic rationale mentioned (B11, B14) without any trial evidence. PASS.
- **Tumor acidity/pH effect beyond one sentence**: Lactate-induced acidosis not featured as a dedicated beat. B08 narration notes lactate "suppresses T-cell and NK-cell cytotoxic function" — this refers to direct lactate effect, which the card permits. pH/acidity word not used in narration. PASS.

---

## Illustrative numbers labeled

All numbers from the card's example seed (0.5 mM glucose, 5 mM serum, 10M cancer cells, 50K T cells, 10x rate, 24h collapse, 48h exhaustion) are labeled ILLUSTRATIVE in the graphic chip on B12. Confirmed.
