# PEDAGOGY — solve-verify-asymmetry

## Concept

Solve-verify asymmetry: solve speed grows with each model generation, verify speed doesn't.

## Question

If Claude solves faster every generation, what is the student's job?

## Answer

Verification — the human side of the asymmetry that Claude cannot self-supply, especially for bugs it generated. Claude's self-audit uses the same weights as Claude's production; it shares the same production failure mode. The probe the student must add is the one Claude cannot generate for itself.

## Key Insight: The structural gap

- Claude solves by pattern completion — fast, fluency-optimized, scales with model generations
- Verification requires deliberate judgment — scales with human effort, approximately constant
- Every model generation widens the gap between solve speed and verify speed
- Competing on solve speed is the wrong game; investing in verify skill is the right one

## Source

Chapter 02: Division of Labor — claude-code-for-students
Pearce et al. 2022 "Asleep at the Keyboard" — self-audit limitation documentation
