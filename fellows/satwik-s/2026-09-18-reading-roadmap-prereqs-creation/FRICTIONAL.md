# FRICTIONAL.md - Read the Book, Draft the Graph

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-09-18-reading-roadmap-prereqs-creation`
**Date:** Sep 18, 2026 (week ending September 20, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Built the prerequisite dependency graph from the textbook as a reviewable draft for faculty.

## What I did (my contribution)

- Built the prerequisite dependency graph as a reviewable draft: a two-pass build (faculty-authoritative prerequisites first, then auto-proposed conceptual and method links), with provenance and a needs_review flag on every edge.
- Made cycles impossible by construction (every prerequisite must come earlier in the book) and enforced cycle validation as a hard gate that halts the build and names the offending nodes.
- Set up the faculty-review workflow: a review CSV with an approve column, plus a GraphML export so the graph opens in standard network tools.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- Prerequisite cycles had to be impossible, not merely discouraged; I made the earlier-in-book rule a hard constraint and validated it on every build.
- Keeping every edge reviewable (provenance, confidence, needs_review) rather than a black box took deliberate design.

## What Claude contributed (assistant)

- Implemented the graph builder, the validation, and the GraphML export to my design.
- Ran the build and produced the review files.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted the two-pass, provenance-tracked design; I rejected any edge a faculty member could not open and correct.
