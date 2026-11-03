# Verifying AI-Generated Code

**Fellow:** Rishika Bhat Kuthyar
**Project:** Mycroft — multi-agent verification for AI-generated code
**Date:** 2026-07-27

## Subject

A short explainer on why an AI can't be trusted to check its own code,
and how separating the code-writer from an independent, human-authored
answer key (the oracle) catches a class of error self-checking misses.

The video covers: the "grading your own exam" problem, the separated-
verification design (a human answer key written before any code), a real
caught error (the AI silently defining an undefined rule term as "90 days"
and then validating its own assumption), and the honest takeaway —
self-checking isn't useless, but it's blind to the assumptions it invents.

## Contents

- README.md — this file
- beat_sheet.json — beat sheet driving narration and timing
- [video / storyboard file]

## Notes

- Core result: a counterfactual experiment comparing a human-authored
  oracle against an AI-generated oracle on the same ambiguous rule. The
  human oracle caught the mismatch; the AI self-check passed its own
  assumption.
- Scope: demonstrates the mechanism on one class of error (undefined-term
  ambiguity), not a universal claim that self-checking always fails.
- Project code and design doc: github.com/RishikaBhatKuthyar/mycroft
