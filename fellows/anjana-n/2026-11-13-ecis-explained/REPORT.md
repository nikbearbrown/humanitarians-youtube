# Video Report: ECIS Episode 15 — Signals That Remember

**Type:** Weekly Implementation Video

**Project:** [Mycroft — ECIS + Decision Scorecard](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

**Week:** Week 20 (Phase 20), November 8 – 14, 2026

---

## Summary
This episode shows ECIS using context to read its signals. The system now:
- reads signals as a sequence over several quarters
- detects the market conditions a company is in
- adjusts scores for how tough each analyst's questions are
- answers questions using both transcripts and structured data

## Main Ideas
- **Sequence matters.** A slow rise and a sudden spike can end on the same value but mean different things.
- **Market regimes:** a Hidden Markov Model labels each quarter as bullish, bearish or transitional, and that label becomes context for predictions.
- **Analyst difficulty:** the same avoidance score means less against a tough analyst than an easy one.
- **Answers with sources:** the agent pulls quotes from transcripts and figures from a database, so each part of an answer can be traced.

## Links
- **GitHub:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-13-ecis-explained
- **Drive:** https://drive.google.com/drive/folders/1VuL_1Lpa8AA0eVSAJeNUrWUkF4Abus-L
- **Week 20 work folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-13-weekly-work-progress

## Status
Complete