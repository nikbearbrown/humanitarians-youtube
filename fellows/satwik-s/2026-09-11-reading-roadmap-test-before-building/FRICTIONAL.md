# FRICTIONAL.md - Test Before You Advance

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-09-11-reading-roadmap-test-before-building`
**Date:** Sep 11, 2026 (week ending September 11, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Designed the test-to-advance gate: never assume prior knowledge, evaluate first, prune on pass, descend on fail.

## What I did (my contribution)

- Designed the test-to-advance gate: never assume a student knows a prerequisite, evaluate it first, prune (trust and skip) its whole subtree on a pass, and on a fail descend into its own prerequisites to localise how deep the gap goes.
- Grounded the design in Knowledge Space Theory (surmise relations) and Bayesian Knowledge Tracing (the mastery threshold), and specified hard (gating) versus soft (diagnostic) prerequisites.
- Wrote the design up with a worked example (the LaTeX note and PDF) so faculty and the paper can follow the gate's logic step by step.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- The naive 'assume the basics are known' approach is wrong here; I made evaluate-first the core rule so no prior knowledge is ever presumed.
- Deciding how a failure localises (descend into sub-prerequisites rather than just fail) took real design work.

## What Claude contributed (assistant)

- Implemented the gate engine and item-pool sampling to my specification.
- Drafted the worked example from my design.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted prune-after-evaluate and descend-on-fail; I rejected any pre-declared 'known' set.
