# PEDAGOGY — boondoggle-score

## Concept

Boondoggle Score for pre-build risk diagnosis: how to know which step is highest-risk before writing any code.

## Question

How do you know which step is highest-risk before writing any code?

## Answer

Score each step's handoff condition for machine-checkability. The step with no machine-checkable condition is the one that will block the build — because there's no way to know when it's done. The critical path is the chain of steps where each one blocks the next; the highest-risk step on the critical path is the one that can halt the entire build.

## Key Concept: Machine-checkable handoff conditions

A handoff condition is machine-checkable if it:
1. Names a specific test file (pytest tests/test_models.py)
2. Names an exit code (exits 0)
3. Names a specific artifact count (3 apps survive reload)
4. Names a screenshot comparison (matches wireframe.png)

It is NOT machine-checkable if it is:
- Subjective ("Claude finishes")
- Vague ("looks good")
- Human-judgment-dependent without a clear threshold

## Source

Chapter 11: Planning the First Build — claude-code-for-students
