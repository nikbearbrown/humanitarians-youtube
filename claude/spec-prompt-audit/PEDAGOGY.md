# PEDAGOGY — spec-prompt-audit

## Concept

Specification prompts vs. vague requests: what makes a specification prompt different from a longer prompt.

## Question

What makes a specification prompt different from a longer prompt?

## Answer

A specification prompt is not more words — it is invariants, a context pointer, and an output contract. It leaves Claude nothing to invent from training data that doesn't know the project constraints. The difference shows up in two ways: the output is deterministic (same library, same edge-case behavior across runs), and the output satisfies the actual constraints (stdlib only, BOM handling, empty cells as None) rather than the most common pattern from training data.

## Key Concept: The five elements of a specification prompt

1. Invariants — what must be true regardless of approach (stdlib only, no pandas)
2. Context pointer — what existing code is off-limits (do not modify models/grade.py)
3. Output contract — what the function must return (list[Grade])
4. Test gate — how correctness is measured (python -m pytest tests/ -q)
5. Edge cases — what corner cases are explicitly handled (UTF-8 BOM, empty cells as None)

## Source

Chapter 08: Prompts as Specifications — claude-code-for-students
