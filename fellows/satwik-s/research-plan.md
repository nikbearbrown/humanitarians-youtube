# Research Plan - Satwik Reddy Sripathi

**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Supervision:** Prof. Nik Bear Brown and Dr. Evin Gultepe
**Last updated:** October 26, 2026

## Problem

Cancer-nanomedicine trainees need to read across a fixed 38-chapter textbook in an order matched to their
own lab project. Standard semantic search returns the top-k most similar sections; it cannot express
learning dependency ("read A before B"). My thesis is that this is a reordering problem, not a retrieval
problem: select sections by relevance, then sequence them by conceptual dependency under a graph constraint.

## Approach (four-stage pipeline)

1. **Section extraction** - parse the textbook into stable, hierarchical section IDs with an audit log.
2. **Metadata tagging** - LLM-assisted, human-editable tags with per-field confidence and needs_review.
3. **Dependency graph** - typed, provenance-tracked learning-dependency edges; acyclic by construction;
   validated on every build.
4. **Personalized sequencing** - parse the student's project, match sections (multi-signal, role-labeled),
   and order by topological sort over the prerequisite subgraph, with an exclusion log.

On top of the pipeline: a **test-to-advance gate** (evaluate a prerequisite before trusting it; prune on
pass, descend on fail), **three-tier prerequisites** (required / recommended / curious), and an **optional,
formative concept-matching knowledge-check**.

## Research commitments

- Reproducible: pinned models, saved intermediate artifacts, prompts in-repo.
- Explainable: every selected section carries a reason and the lab task it supports.
- Reviewable: faculty can open and correct metadata and edges; a bad edit fails loudly.
- Evaluable: outputs support personalization, exclusion, and with/without-graph ablation analyses.

## Grounding

Knowledge Space Theory (Doignon & Falmagne), Bayesian Knowledge Tracing (Corbett & Anderson), relational
concept-map scoring (McClure, Sonak & Suen), partial-credit knowledge tracing (Wang, Heffernan & Beck),
prerequisite extraction from textbook structure, and transitive reduction of dependency graphs.

## Plan for the renewal period

- Strengthen later-chapter prerequisites and complete the faculty review loop.
- Run the with/without-graph ablation and the personalization analysis for the paper.
- Continue weekly Brutalist research videos.
- Publish a research paper on this architecture
