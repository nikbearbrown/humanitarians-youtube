# FRICTIONAL.md - Does the Fancy Part Earn It? A Tagging Ablation

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-08-09-personalized-roadmap-ablationstudy1`
**Date:** Aug 9, 2026 (week ending August 9, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Tested whether the LLM metadata tagging earns its place against a deterministic baseline.

## What I did (my contribution)

- Designed an ablation of the Stage-2 metadata tagger (deterministic rule-based vs a pinned open LLM) and defined the metrics myself: per-field Jaccard, run-to-run stability, cross-tagger agreement, and difficulty agreement.
- Chose a reproducible, self-hosted model arm (qwen2.5-coder:7b, temperature 0, fixed seed) over a hosted API so both arms are replicable for the paper, and ran the model arm on the Explorer GPU cluster.
- Ran a seeded 60-section sample at K=3 runs per backend, interpreted the results, and wrote up the ablation stating what it can and cannot conclude.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- The first stability and agreement numbers looked too good; I was skeptical, dug in, and found they were inflated by empty-vs-empty matches on sparse fields.
- I added a non-empty-restricted stability metric and found the flagship materials agreement actually rested on only about four to five sections, so I re-framed it as directional, not robust.

## What Claude contributed (assistant)

- Implemented the metric functions and the comparison script to my design.
- Executed the paired runs and tabulated the outputs.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted the deterministic tagger as the reproducible default; I reported the inflated agreement as a caveat rather than a win, and planned a larger re-run to firm it up.
