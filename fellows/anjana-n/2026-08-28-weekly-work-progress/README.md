**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 9 — New Features and Signal Enrichment

**Timeline:** August 23, 2026 – August 29, 2026

**Scope:** Expanded Qwen extraction, speaker-role weighting, chunk quality scoring, and retrospective temporal linking, each evaluated individually and in combination.

---

## Qwen2.5-14B Expanded Extraction
- Extraction extended to additional tickers
- Prompt templates refined based on earlier results
- Three-model comparison refreshed with the broader dataset

## Speaker Role Classification
- **Canonical roles:** CFO, CEO, COO, IR, analyst, operator
- **Primary signal:** title keywords in speaker attribution (e.g. "Chief Financial Officer" maps to CFO)
- **Edge cases:**
  - Multiple titles
  - Name-only speakers, resolved through a company officer lookup table built from filing metadata
  - Generic labels ("Management", "Executive")

## Speaker Weighting
- **Configurable multipliers:**

| Role | Multiplier | Rationale |
|---|---|---|
| CFO | 1.0 | Most authoritative on financial guidance |
| CEO | 0.8 | Authoritative, but more prone to general optimism |
| COO | 0.7 | Operational focus |
| IR | 0.6 | Supporting role |
| Analyst | 0.3 | Speculation, not company guidance |
| Operator | 0.0 | Call logistics only |

- **Triangulator integration:** the multiplier scales the signal's contribution to triangulated confidence
  - Example: an analyst signal with 0.75 reader confidence drops to 0.225 (0.75 × 0.3)
- **Evaluation:**
  - Before/after Brier score, skill score, and ECE
  - Reduction in Q&A false positives caused by analyst language

## Chunk Quality Scoring
- **Sub-scores (each 0–1):**
  - **Boilerplate ratio:** share of tokens matching safe-harbour, disclaimer, legal, logistics, or operator patterns
  - **Token count:** penalizes chunks well below the 400-token target
  - **Section completeness:** whether the chunk starts and ends at natural boundaries
  - **Speaker transitions:** penalizes multiple speaker changes within one chunk
- **Composite:** weighted average producing a single 0–1 quality score
- **Triangulator integration:** applied as a multiplier alongside reader and speaker weights
  - Example: a 0.95-quality chunk keeps most of its influence, while a 0.4-quality chunk is heavily downweighted
- **Evaluation:** before/after Scorecard comparison of calibration and skill

## Retrospective Temporal Linking
- **Data query:**
  - Decision log grouped by ticker and ordered by `transcript_date`
  - Handles quarterly gaps
  - Uses the highest-confidence signal per direction per quarter as the representative
- **Trend labels:**

| Label | Definition |
|---|---|
| `consecutive_raise` | Raised in the current and prior quarter |
| `consecutive_lower` | Lowered in the current and prior quarter |
| `reversal` | Direction changed from the prior quarter |
| `stable_maintained` | Maintained for two or more consecutive quarters |
| `single` | No prior-quarter data; always applied to a ticker's first quarter |

- **Persistence:** written as an enrichment column during post-extraction enrichment, preserving the append-only integrity of the log
- **Evaluation:**
  - Information ratio of consecutive vs. single-quarter signals
  - Predictive value of reversals
  - Reader comparison table split by trend label

## Combined Evaluation
- All three features enabled together on a representative subset to confirm they compose cleanly
- Full Scorecard run across 25 tickers, producing:
  - Reader comparison table
  - Calibration curves
  - Per-ticker breakdown with speaker, quality, and trend dimensions
