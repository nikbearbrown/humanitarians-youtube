# NARRATION — GATE P — Week 15: Reading the Student

Voice: Kokoro `af_bella` ("Bella"). Register: pragmatist / skeptical-explainer. Numbers spelled out for TTS; digits live in the on-screen props. Greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI."

- **B00 (hook/ASK):** read the student first — free text in, structured fields out; the parser had no measurement; this week, a gold standard.
- **B01 (two guarantees):** never guess (empty beats wrong) / never miss (read the idea, not just the word); fields use the textbook's controlled vocabulary.
- **B02 (two backends):** rule-based offline default / optional LLM strict-JSON over the same vocabulary; swap by config.
- **B03 (the test):** six-project hand-annotated gold standard; precision, recall, F1, never-guessed audit — named first.
- **B04 (concrete solved):** materials/techniques/assays/disease at 1.0; 8/8, 16/16, 6/6, 16/16.
- **B05 (recall ceiling):** concepts 0.69, mechanisms 0.71; all 8 misses paraphrase ("new blood vessels" → angiogenesis, etc.).
- **B06 (never-guessed):** 0 invented, 67/67 grounded, 4 empty; overall precision 0.97.
- **B07 (polysemy):** the two false positives are "cell cycle regulation" (from "cell cycle") and "tissue organization" (from "tissue") — polysemy, not invention.
- **B08 (honest boundary):** LLM backend code-complete but not measured; rule-based numbers are the result; no learning claim.
- **B09 (outro):** structured intent without guessing; build a gold standard, audit what it refuses to fill.

GATE P: PASS (see PEDAGOGY.md). Cleared for audio.
