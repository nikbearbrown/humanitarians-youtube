# FACT-CHECK — Week 15: Reading the Student (Stage 4a Project Parser)

**Audited:** beat_sheet.json beat-by-beat against `sources/` (project_parse_quality.json / .md, project_parse_gold.json, weekly_report_2026-11-07.md, project_parser_upgrade.md).
**Signed:** 2026-11-07 · **VERDICT: PASS** (with 1 correction, below).

## Claim table

| Beat | Claim | Verdict | Evidence (source) |
|------|-------|---------|-------------------|
| B00/B06 | overall precision 0.97, recall 0.89, F1 0.93 | SUPPORTED | quality.json micro: precision 0.97, recall 0.89, f1 0.929 (tp 65, fp 2, fn 8) |
| B03 | gold standard = 6 projects, hand-annotated (LNP-siRNA, photothermal, CAR-T, polymeric chemo, iron-oxide MRI, CRISPR) | SUPPORTED | quality.json n_projects 6, per_project keys; weekly_report §2 |
| B04 | materials 8/8, techniques 16/16, assays 6/6, disease 16/16 all at P/R 1.0 | SUPPORTED | quality.json per_field: materials tp8 fp0 fn0; techniques tp16; assays tp6; disease_contexts tp16; all P/R/F1 = 1.0 |
| B05 | concepts recall 0.69, mechanisms recall 0.71 | SUPPORTED | quality.json concepts recall 0.692, mechanisms recall 0.714 |
| B05 | all 8 misses are paraphrase | SUPPORTED | quality.md "Recall ceiling" lists 8: apoptosis, drug resistance, pharmacokinetics, angiogenesis, biomarker, metastasis, DNA damage and repair, DNA repair (fn: concepts 4 + mechanisms 4 = 8) |
| B05 | paraphrase examples: "new blood vessels"→angiogenesis, "spread to the bone"→metastasis, "stop responding to the drug"→drug resistance | SUPPORTED | weekly_report §3 and README beat 6 give these three examples |
| B06 | never-guessed: 0 invented, 67/67 grounded, 4 empty | SUPPORTED | quality.json never_guessed_audit: terms_total 67, terms_out_of_vocab 0, terms_surface_grounded 67, empty_fields_preserved 4 |
| B07 | exactly 2 precision slips (false positives), from polysemy | SUPPORTED | quality.json micro fp 2; quality.md "Precision slips": photothermal concepts "tissue organization", car_t mechanisms "cell cycle regulation" |
| B08 | LLM backend code-complete but not measured here; rule-based is the result; no learning claim | SUPPORTED | weekly_report §4, §6; project_parser_upgrade.md; README source status |

## Correction applied (1)

- **Precision-slip example terms.** The README's beat-8 prose named the polysemy slips as `"checkpoint"` (immune, not cell-cycle) and `"tissue"` (tumor tissue). The **actual two false positives** recorded in `project_parse_quality.json` / `.md` are **`cell cycle regulation`** (car_t_leukemia · mechanisms, spurious) and **`tissue organization`** (photothermal · concepts, spurious). The video (B07) uses the **data's actual terms**, framed by the same polysemy mechanism: `cell cycle regulation` produced from the surface form "cell cycle"; `tissue organization` from the surface form "tissue". This keeps the on-screen terms traceable to the JSON. The underlying point (precision slips are polysemy, not invention; 2 FP in 67 terms) is unchanged and fully supported.

## Guardrails honored
- Every on-screen number traces to `project_parse_quality.json`.
- The LLM backend is never presented as measured; rule-based numbers are labelled the result and the LLM gain a prediction (B08 stamp).
- No learning-outcome claim anywhere.
