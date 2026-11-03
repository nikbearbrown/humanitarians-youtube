# Friction Log: Week 10 (Phase 10)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** August 30 – September 5, 2026

---

## 1. Focus of the week

- **Qwen completion:** final extraction across the remaining tickers and a final three-model Scorecard comparison.
- **Second QLoRA round:**
  - training triples with reasoning traces
  - NF4 loading via Unsloth
  - rank-16 LoRA training
  - before/after Scorecard
  - adapter integration
- **Six new features:**
  - abstention calibration
  - section-weighted extraction
  - signal decay tracking
  - negation detection
  - keyword density
  - duplicate transcript detection
- **Pipeline:** re-run with the fine-tuned model and all features; full base vs. fine-tuned evaluation.
- **Research:** analysis of fine-tuning results; post-training methods.
- **Outputs:**
  - two Claude artifacts
  - two Substack articles
  - two videos

## 2. What was tried, and what was expected

- **Reasoning traces:** the hypothesis was that corrected reasoning traces in the training data would teach the model discrimination, so resolution would move, not just calibration.
- **Abstention penalty:** expected a penalty proportional to vote spread to express uncertainty better than the flat 0.15.
- **Duplicate detection:** expected hashing normalized transcript text to cleanly identify duplicate transcripts.
- **Signal decay:** expected signal accuracy to behave similarly across 30-, 90- and 180-day horizons.
- **Integration:** expected the six small features to compose without interfering with each other.

## 3. Points of resistance, and next steps taken

### Resolution movement: signal or noise? (load-bearing)
- **What happened:** for the first time, resolution moved slightly.
  - The skill score improved by 0.09 and calibration improved further.
  - In Week 7, by contrast, the first QLoRA round improved calibration but left resolution flat.
- **What resisted:** the improvement is small enough to be noise at this sample size.
- **Next step:** assessed as "promising, not proven". A larger sample is needed to decide whether reasoning traces are genuinely teaching discrimination.

### Abstention calibration produced negative confidence
- **What happened:** the proportional penalty produced negative confidence values on extreme vote spreads (majority 0.9, minority 0.1). The penalty exceeded the base confidence.
- **Next step:** clamped the penalty so confidence never drops below 0.05.
- **Why 0.05 rather than 0.0:** a signal that survives extraction and triangulation has some non-zero evidence.
  - Zero would mean "this signal has no information".
  - That is different from "this signal has very uncertain information".
- **Function choice:** linear, logarithmic and step functions were tested.
  - Logarithmic penalized moderate disagreements too heavily.
  - Step lost granularity.
  - Linear improved ECE without raising the abstention rate.

### Duplicate detection flagged amended filings
- **What happened:** amended filings were flagged as duplicates when only the filing wrapper changed. Legitimate amendments with actual transcript corrections were being skipped.
- **Next step:** hash only the transcript body after boilerplate stripping, not the full normalized text.
- **Lesson:** universal rules applied to EDGAR filings keep producing edge cases where filing structure and content don't move in lockstep.

### Signal decay: what does "predictive" mean?
- **What happened:**
  - Raised signals are mostly correct at 30 days but degrade by 180 days, as the market prices in the information.
  - Reversals show the opposite pattern: a delayed signal that becomes more accurate over time.
- **What resisted:** whether to weight the Scorecard toward short-horizon accuracy, which favors the system's current strengths, or long-horizon persistence, where the harder and more valuable signals live.
- **Next step:** the observation is recorded without claiming predictive power. The horizon weighting decision is carried forward.

### Composing many features
- **What resisted:** the integration was harder than the features. Each feature was small, but the integration complexity exceeded their sum.
- **Next step:** the full evaluation was tested systematically to confirm three things work together without interfering:
  - the five weight dimensions
  - the negation routing overrides
  - the fine-tuned adapter

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Five-Dimension Weight Calculator:** an explorer for the multiplicative composition, with sliders showing threshold effects and confidence cliffs.
- **QLoRA Before-and-After Dashboard:** base vs. fine-tuned metrics with animated transitions and a drill-down into the maintained/none boundary.

### Gru (SDD session)
- Documented the five-dimension triangulator composition, the abstention calibration design, and the signal decay analysis.

### Eddy
- Reviewed both Week 10 articles before publication.

## 5. Understood now, and still unresolved

### Understood
- **Reasoning traces:** they may move resolution, not just calibration. This is the first evidence that training data composition can push past the Week 7 plateau.
- **Penalty functions:** they need floors. A mathematically valid output can still be semantically meaningless.
- **Hashing:** must target the content that matters (the transcript body), not the container (the filing).
- **Horizon matters:** different signal types carry their information at different horizons. This is a finding about the domain, not just the system.
- **Small features:** composing many small features is an architectural problem in its own right.

### Unresolved
- **Resolution movement:** whether it is real or noise; it needs a larger sample.
- **Horizon weighting:** short-horizon accuracy vs. long-horizon persistence.
- **Routing:** the complexity decision is informed by the three-model and fine-tuning results but not finalized.
- **Gate ordering:** the quality score + confidence gate ordering is still being monitored.
