# Video Report: ECIS Episode 12 — How Long Does a Signal Last?

**Type:** Weekly Implementation Video


**Project:** [Mycroft — ECIS + Decision Scorecard](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

**Week:** Week 17 (Phase 17) · October 18 – October 24, 2026

---

## Summary
This episode presents the Week 17 progress on the ECIS project. It covers four areas:
- how long different signals stay useful
- why confident predictions can still be wrong
- how executive language reveals intent
- how the feature set was refined

**Credits:**
- **Concept, script, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

## Episode Outline
1. **Introduction:** opens with the episode's central question.
2. **Recap:** summarizes the system as built in Episodes 1–11.
3. **Signal decay:** shows how quickly each type of signal loses predictive value.
4. **False positives:** explains why high-confidence predictions are sometimes wrong, and how sustained trends are tracked across quarters.
5. **Speech acts and discourse:** shows how the system separates promises from hedged statements and deflections, and detects when bad news is placed to draw less attention.
6. **Feature engineering:** covers how weak features are removed, how useful feature combinations are found, and how the system monitors for drift.
7. **Closing summary**, followed by key takeaways and a prompt for viewers.

## Key Points Presented
- **Signals lose value at different rates.** Measured by half-life, the time until predictive value falls by half:
  - evasive answers in Q&A: about 5 days
  - hedging language: about 20 days
  - forward-looking statements: about 25 days, the longest
- **Confidence is not the same as accuracy.** Incorrect high-confidence predictions were grouped by root cause, and their confidence is reduced when the same patterns appear again.
- **Sustained trends matter more than single spikes.** Three quarters of rising hedging are treated as one sustained signal, not three separate ones.
- **The way executives speak carries meaning.** "We will deliver" and "we hope to" can read as equally positive, but they signal very different levels of commitment.
- **Weak features are removed only when three independent methods agree.**

## Production Notes
- **Script:** kept word for word. Several sections run longer than the target length, and this was accepted because each one covers several ideas.
- **Visuals:** colors follow the established series style.
- *
- **Review:** the production plan was reviewed and approved before narration was recorded.

## Links
- **Video:**
  - GitHub: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-23-ecis-explained
  - Drive: https://drive.google.com/drive/folders/1C3bVEFbFXSPx_5HNcWsR8mjMULJ6WKLW
- **Week 17 work folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-23-weekly-work-progress

## Status
- Complete
