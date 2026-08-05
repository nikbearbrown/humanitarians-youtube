# NARRATION — Nine Months at the Data Ceiling

**Vighnesh Sairaman · NeuroVEP — ANN mfVEP response classifier · 2025-W48 through 2026-W32**  
Register: Pragmatist · Voice: Kokoro `af_bella` · @HumanitariansAI

Read this in full before signing GATE P in `PEDAGOGY.md`.

---

### B00 — ASK  ·  ~19s

Nine months on one question: can a neural network read a multifocal visual evoked potential and tell a real visual-field defect from a healthy eye? Here is the method, the numbers that survived review, and the wall I hit. I am Vighnesh Sairaman, on NeuroVEP with Humanitarians AI.

### B01 — SUMMARY  ·  ~19s

The short version first. I built ten model architectures against a seventeen-subject EEG dataset, then eliminated capacity, regularization, and augmentation one at a time as explanations for a performance plateau. What remained was the size of the cohort. That negative result is the most useful thing the project produced.

### B02 — METHOD  ·  ~21s

The method first. A multifocal visual evoked potential drives sixty screen sectors independently and reads the cortical response over EEG. To label defects without harming anyone, twenty-five percent of sectors are blacked out per eye. The classifier sees two eyes, ten channels, six hundred milliseconds at one kilohertz — roughly a thousand paired samples.

### B03 — METHOD  ·  ~20s

Use leave-one-subject-out validation, and use it from the start. Seventeen folds, each holding out one subject entirely. It is expensive and it produces worse numbers than a random split. That is the point. EEG carries strong subject identity, so a random split lets the model recognise the person instead of the pathology.

### B04 — RESULTS  ·  ~26s

Here is the progression, left-eye accuracy under leave-one-subject-out. The dual-eye convolutional baseline, seventy-two point three. Per-eye heads, seventy-four point nine. Full augmentation went down, to sixty-nine point four. Filter-bank C S P with L D A, seventy-two point eight. A T C Net, seventy-seven point three. E E G Net, eighty point one — the best in the project, at two thousand five hundred seventy-eight parameters.

### B05 — RESULTS  ·  ~16s

Note the shape. Fifty-eight thousand parameters with full augmentation lost to two and a half thousand with the right inductive bias. More capacity did not help. When scaling the model stops moving the metric, the model has stopped being the bottleneck.

### B06 — FAILURE  ·  ~28s

Now where it failed, because that matters more. Notebook ten-b split the data at the sector level, which put the same subject in both the augmentation pool and the validation pool. Every headline number under that split was inflated. I caught it during review, corrected to a strict subject-level split, and re-reported the results downward: sensitivity sixty-one point four percent, specificity eighty point six. Those are the numbers the project stands behind.

### B07 — FINDING  ·  ~26s

The finding is causal and falsifiable. Training accuracy sits above ninety-five percent while validation plateaus near seventy. That gap is not generic overfitting — the model is memorising which subject it is looking at, not what the signal means. Capacity ruled out. Regularization ruled out. Augmentation ruled out. What remains is inter-subject variability at n equals seventeen. The prediction: at fifty or more subjects, the ceiling lifts.

### B08 — RECOVERY  ·  ~21s

One interruption. In June the development machine failed and was reformatted. The drive was carved with PhotoRec, which strips filenames and timestamps. A semantic triage pass processed one hundred fifty-one thousand nine hundred twenty-seven files in one hundred twenty-four seconds, with zero errors. Thirty-seven notebooks were rebuilt and validated, and four hundred ninety-nine figures classified.

### B09 — NEXT  ·  ~20s

Next. Complete the stacked meta-learner run — the base models are complementary, the convolutional net carries sensitivity, the random forest carries specificity. Then the gap I have not closed: a clinical decision-threshold analysis. Sixty-one percent sensitivity on a screening instrument for irreversible blindness has a consequence, and nobody has written it down.

### B_CLI — WORKED EXAMPLE  ·  ~27s

Here is what this looks like in a real session, and it runs today on your own data. Ask Claude Code to audit a cross-validation split for subject leakage — pass it your fold indices and subject labels. It returns every fold where a subject appears on both sides. Then add the flag to check the augmentation pool, because that is where mine hid. Run it before you trust a number.

### B_OUTRO — OUTRO  ·  ~6s

NeuroVEP, with Humanitarians AI. The result that mattered was the one that got worse under review.

---

**Estimated runtime ~4m08s** at 155 wpm. Measured Kokoro audio is the real clock and will shift this by a few seconds either way.
