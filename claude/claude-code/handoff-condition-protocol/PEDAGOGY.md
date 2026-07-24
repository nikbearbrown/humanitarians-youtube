# PEDAGOGY — handoff-condition-protocol

## Concept

Machine-checkable handoff conditions via automated validator. How do you prevent the dangerous middle from opening between Claude's output and the next build step?

## Question

How do you prevent the dangerous middle from opening between Claude's output and the next build step?

## Answer

Run a machine-checkable condition before authorizing the next step — subprocess exit code, not human judgment. The validator converts a process question ("did Claude finish?") into an engineering fact ("did the test pass?"). When the validator runs, the dangerous middle cannot open because there is no gap between completion and verification.

## Key Insight

The dangerous middle opens in the gap between "Claude said it's done" and "we checked that it's done." The validator closes that gap mechanically.

## Source

Chapter 09: Handoff Conditions and the Dangerous Middle — claude-code-for-students
