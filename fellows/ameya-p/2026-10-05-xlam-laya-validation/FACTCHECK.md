# FACTCHECK — 2026-10-05-xlam-laya-validation (Fine-Tuning Platform)

Every claim the narration makes, mapped to the source document:
`work_report.md` ("Fine-Tuning Platform: End-to-End Validation Report — xLAM Dataset & Laya Model").

## B00 — Cold open

- **"Following the runtime implementation, Ameya Padwad tested the RLCD pipeline end-to-end on the Laya model using a 60,000-row dataset."**
  Source §1 & §2: end-to-end validation conducted using `Salesforce/xlam-function-calling-60k` (60,000 rows of tool-selection and function-calling decisions) on `convaiinnovations/laya`.

## B01 — BLUF

- **"Routing accuracy surged from ~73% baseline to 99.10% after RLCD fine-tuning."**
  Source §3: "Prior to fine-tuning, the base Laya model achieved an accuracy of approximately 73% on the xLAM tool-selection tasks. After processing the 60,000-row dataset through our RLCD pipeline, the model's routing accuracy surged to 99.10%."

## B02 — Calibration Error (0.83% ECE)

- **"Expected Calibration Error dropped to 0.83% on the held-out test split."**
  Source §3: "Alongside the massive accuracy gain, the model demonstrated exceptional confidence calibration (0.83% Expected Calibration Error), proving that the RLCD reward strategy effectively prevents overconfident misrouting."

## B03 — Live GPU Validation Logs & Next Steps

- **"Live GPU execution logs are documented in `docs/PIPELINE_VALIDATION_REPORT.md`, setting up multi-model and multi-primitive testing."**
  Source §3 & §4: live GPU execution documented in `docs/PIPELINE_VALIDATION_REPORT.md`; next steps target multiple decision models (`Von`, `Decision 1.0`, `Typical`) and primitives (`choice`, `score`, `noul`).

## B04 — Outro

- Title restate (`Validation Report: Laya & RLCD`).
