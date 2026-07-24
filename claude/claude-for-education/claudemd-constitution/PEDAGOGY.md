# PEDAGOGY — claudemd-constitution

## Concept
CLAUDE.md as active constraint document — not documentation but the active context Claude reads at every session start.

## Core question
What prevents Claude from proposing a backend in a static-site project?

## Answer
An explicit architectural constraint in CLAUDE.md — without it, Claude draws from training data that includes backends. With it, the constraint is read at session start and shapes every proposal.

## Teaching pattern
- B00: concrete outcome — one line prevents the wrong proposal
- B01: reframe — CLAUDE.md is not docs, it is context
- B02-B03: show the generation — five-section constitution built from requirements
- B04: show the outcome — mailto link proposed, not a form endpoint
- B05-B06: contrastive test — remove one constraint, observe the change
- B07: consolidate the five sections
- B08: forward link to next mechanism (hooks)

## Bloom's level
Understanding → Applying: students can name the five sections and write a CLAUDE.md for a constrained project.

## Common misconception addressed
Teachers often treat CLAUDE.md as a README for humans. The video reframes it as active context that mechanically shapes Claude's proposals — the distinction between advice and constraint.
