# PREMISE — Week 15: Reading the Student (Stage 4a Project Parser)

**Central question.** When a student describes their project in their own words, can the system turn it into structured intent without guessing — and where does plain keyword matching fall short?

**Answer (the spine).** Concrete, named things (materials, techniques, assays, disease) are read perfectly (1.0/1.0); abstract concepts and mechanisms hit a paraphrase recall ceiling (0.69 / 0.71); and the parser never invents a term or fills a field it cannot support (0 invented, 67/67 grounded, 4 empty; overall precision 0.97). Measured against a six-project hand-annotated gold standard, with a swappable LLM backend built to close the gap but not yet measured.

**Why it matters.** Stage 4a is the first time the system reads the student. Everything downstream trusts that reading, so it earns a gold standard and a score, not an assumption.

**Register.** Pragmatist / skeptical-explainer (PROOF): framework first (two guarantees, two backends, the test), then numbers, then the honest boundary.

**Reusable framework.** (1) Measure the reading before trusting it. (2) Separate the two failure modes — precision (guessing) and recall (missing). (3) Make abstention a measured property. (4) Put the fix behind the same interface.
