# FRICTIONAL.md - Evaluate, Then Advance

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-09-25-reading-roadmap-evaluate-then-advance`
**Date:** Sep 25, 2026 (week ending September 25, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Ran the full evaluation pipeline: the MCQ gate with item pools and prune-after-evaluate.

## What I did (my contribution)

- Built the end-to-end evaluation engine: the MCQ gate running prune-after-evaluate over the prerequisite graph, emitting an advance / hold / remediate decision plus the specific prerequisite to remediate to.
- Added item pools with deterministic per-student sampling (different students get different questions from the same approved pool) and an open-ended grading seam (defer by default, with keyword and LLM-judge options).
- Made the gate's decisions inspectable with a readable trace and the gate_result and responses CSV artifacts.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- Deciding how the gate reports a gap (remediate to the exact missing prerequisite, not just 'fail') took design.
- Keeping the open-ended path honest (defer to a real judge rather than fake-grade free text offline) mattered for credibility.

## What Claude contributed (assistant)

- Implemented the evaluation engine and the CSV artifacts to my spec.
- Produced the readable trace and the example run.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted defer-by-default open grading; I rejected pretending to grade free text without a judge.
