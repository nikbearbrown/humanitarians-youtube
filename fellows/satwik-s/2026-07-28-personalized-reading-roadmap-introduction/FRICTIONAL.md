# FRICTIONAL.md - Personalized, Project-Driven Reading Roadmaps (Introduction)

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-07-28-personalized-reading-roadmap-introduction`
**Date:** Jul 28, 2026 (week ending July 27, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Introduced the project and the framing that governs every design decision: this is a reordering problem, not a retrieval problem.

## What I did (my contribution)

- Defined the research problem and the governing framing: reorder a 38-chapter cancer-biology textbook by learning dependency rather than return the top-k most similar sections, and wrote this up as the 14-page method draft the video is built from.
- Designed the four-stage pipeline (section extraction -> metadata tagging -> dependency graph -> personalized sequencing) and specified the seven typed artifacts that form the contract between stages (sections, metadata, edges, student project, matches, roadmap items, roadmap output).
- Set the reproducibility rules for a methods paper: stable hierarchical section IDs (CH##-S##-SS##) that survive textbook updates, every intermediate artifact human-inspectable and editable, and a swappable embedding/LLM interface so the system runs offline with no API key.
- Stood up the repository skeleton and runnable dummy-data examples so the pipeline was demonstrable before the real textbook was wired in.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- The central risk was the system quietly collapsing back into semantic search; I fixed reordering-not-retrieval as a hard constraint and designed the stage boundaries around it before any code was written.
- I had to choose a section-ID scheme that keeps faculty edits and graph edges valid across textbook versions, which later proved essential when the textbook was renumbered.

## What Claude contributed (assistant)

- Scaffolded the repository skeleton and the Pydantic schema file from my specification.
- Drafted the video beat sheet from my report.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted the staged, inspectable-artifact design and the stable-ID scheme; I rejected any shortcut that would make Stage 4 a plain similarity ranker.
