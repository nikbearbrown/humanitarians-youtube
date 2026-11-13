# Friction Log: Week 9 (Phase 9)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** August 23 – August 29, 2026

---

## 1. Focus of the week

- **New features**, each built with a before/after Scorecard evaluation:
  - speaker-weighted extraction
  - chunk quality scoring
  - retrospective temporal linking
- **Model expansion:**
  - Qwen2.5-14B extraction across additional tickers
  - refined Qwen prompts
  - updated three-model Scorecard comparison
- **Pipeline:**
  - re-run with all new features enabled
  - full Scorecard evaluation on the updated signal set
- **Research:**
  - architecture review of how the features interact
  - Qwen technical research
  - fine-tuning methodology
- **Outputs:**
  - two Claude artifacts: Speaker Weight Impact Visualizer, Scorecard Comparison Grid
  - two Substack articles
  - two videos

## 2. What was tried, and what was expected

- **Speaker weighting:** expected weighting by speaker role to cut noise from analyst speculation in Q&A without losing real guidance.
- **Quality scoring:** expected a composite chunk quality score to reduce overconfident wrong extractions.
- **Temporal linking:** expected trend patterns across quarters, such as consecutive raises and reversals, to carry more information than isolated signals.
- **Speaker roles:** expected speaker normalization to map every speaker to a role cleanly.
- **Feature interaction:** expected the new features to slot into the triangulator independently.

## 3. Points of resistance, and next steps taken

### Choosing weight values with no prescribed answer (load-bearing)
- **What resisted:** no literature prescribes speaker weights for guidance extraction.
- **Next step:** started from intuition, since CFO guidance language is the most authoritative, and validated against the Scorecard.
  - Final weights: CFO 1.0, CEO 0.8, analyst 0.3.
- **The analyst weight:** 0.3 rather than 0.0 was the key judgment.
  - Zeroing analysts out lost cases where an analyst surfaced guidance that the company then confirmed.
  - At 0.3, those cases are kept at low confidence instead of discarded.
- **Result:** Brier score improved, driven almost entirely by suppressing Q&A false positives.

### Composite quality score weights
- **What resisted:** how much each quality dimension should contribute.
  - Boilerplate ratio turned out to be the strongest predictor of extraction error.
  - Section completeness mattered less than expected, because the chunker already handles most boundary cases.
- **Next step:** iterated the formula against the Scorecard until the before/after showed calibration improvement without suppressing valid signals.

### Speaker normalization: first-name-only references
- **What happened:** some transcripts identify Q&A speakers by first name only.
- **Next step:** fuzzy matching against the prepared-remarks speaker list, where full titles appear.
  - Missed matches default to the CEO weight (0.8), not the analyst weight (0.3).
- **Why default high:** suppressing a company statement (false negative) is worse than slightly overweighting an analyst comment (a low-impact false positive at 0.3).

### Quality score and confidence gate double-filtering
- **What happened:** a low-quality chunk producing a high-confidence signal was downweighted below the confidence gate, so the same signal was penalized twice for the same problem.
- **Next step:** quality scoring applied before the gate, so the gate sees quality-adjusted confidence.
- **Consequence:** quality scoring now affects which signals enter the Scorecard at all, not just how they are weighted. A consequential ordering decision.

### Temporal linking across fiscal calendars
- **What happened:** "Q1" for a company with a January fiscal year end is a different calendar quarter than "Q1" for a March year end.
- **Next step:** sort by actual transcript date rather than fiscal quarter label.
- **Lesson:** the Week 3 fiscal calendar problem resurfaced in a new feature. Calendar normalization is a system-wide concern, not a one-time fix.

### Small sample in trend evaluation
- **What happened:**
  - Consecutive raises showed marginally higher information ratios than isolated raises.
  - Reversals showed the strongest signal, but only 12 exist in the dataset.
- **Next step:** reported as "directionally interesting, insufficient sample" rather than claimed as validated predictive power.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** Claude assembled the videos, using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Speaker Weight Impact Visualizer:** toggle speaker weighting on or off and see the triangulated confidence shift per signal.
- **Scorecard Comparison Grid:** side-by-side before/after metrics with animated deltas for each new feature.

### Gru (SDD session)
- Documented the speaker weighting rationale, the quality score composite design, and the temporal linking architecture.

### Eddy
- Reviewed both Week 9 articles before publication.

## 5. Understood now, and still unresolved

### Understood
- **Who is speaking:** speaker role is a strong signal. Treating analyst speculation as company guidance was a major source of false positives.
- **Chunk quality:** boilerplate ratio is the best single predictor of extraction error, and low-quality chunks drive most overconfident mistakes.
- **Feature ordering:** the order in which features are applied, such as quality before the gate, changes what the Scorecard sees.
- **Asymmetric defaults:** when matching fails, defaulting toward the safer error, keeping company statements, is a deliberate design choice.
- **Evaluation method:** the before/after Scorecard pattern (build → measure → interpret → decide) is now standard for every new feature.

### Unresolved
- **Trend signals:** whether they reach statistical significance with a larger sample.
- **Gate ordering side effects:** whether applying quality scoring before the confidence gate produces unintended suppression patterns.
- **Routing:** whether the routing benefit justifies the operational complexity of multi-model production. Carried forward.
