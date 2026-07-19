# PEDAGOGY — pretooluse-grade-blocker

## Concept
PreToolUse hooks as deterministic enforcement vs probabilistic instruction — the difference between "do not" and "cannot."

## Core question
Why is a hook more reliable than a CLAUDE.md instruction for blocking grade output?

## Answer
CLAUDE.md is weighted probabilistically — Claude may override it depending on prompt phrasing. A hook executes mechanically before every Write call regardless of how the request is phrased. The enforcement is below the language layer.

## Teaching pattern
- B00: outcome first — the hook turns "do not" into "cannot"
- B01: reframe the reliability problem — probabilistic vs deterministic
- B02-B03: build the hook — twenty lines, stdin JSON, regex, exit 1
- B04: test the hook — B+ blocked, regenerated without grade
- B05-B06: refine the pattern — context-sensitive percentile distinction
- B07: two-layer model — CLAUDE.md for transparency, hook for reliability
- B08: forward link to subagents

## Bloom's level
Applying → Analyzing: students can wire a PreToolUse hook and explain why it enforces more reliably than an instruction.

## Common misconception addressed
Teachers often believe a strong CLAUDE.md instruction is sufficient. The video establishes that hooks operate at a different layer — mechanical enforcement, not weighted compliance.
