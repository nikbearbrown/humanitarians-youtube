# PEDAGOGY — three-pass-verification

## Concept

Three-pass verification: functional, edge-case, SDD needs. What does Pass 3 catch that tests can't?

## Question

What does Pass 3 catch that tests can't?

## Answer

The gap between what the code does and what the user need specifies — only caught by reading the SDD user needs aloud while the running build is in front of you. A test suite is incapable of catching this gap because the gap exists at the level of natural-language user needs, not code behavior. Pass 3 is the pass that requires a human.

## Key Insight: Done is relative to the spec

Amending the SDD to remove a need is a valid resolution for a Pass 3 failure — a smaller spec, fully satisfied, beats a larger spec, partially satisfied. The SDD is not fixed; it is the current contract, and changing the contract is a valid engineering decision.

## Source

Chapter 13: Verification — claude-code-for-students
