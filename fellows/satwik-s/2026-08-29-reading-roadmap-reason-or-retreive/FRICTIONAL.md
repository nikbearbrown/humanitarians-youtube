# FRICTIONAL.md - Does It Reason, or Just Retrieve?

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-08-29-reading-roadmap-reason-or-retreive`
**Date:** Aug 29, 2026 (week ending August 29, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Showed that the graph constraint, not similarity, is what makes this reasoning rather than retrieval.

## What I did (my contribution)

- Demonstrated the contribution on two dissimilar projects (LNP-siRNA vs photothermal therapy): each produces a visibly different roadmap (section-set Jaccard 0.147), which a similarity ranker cannot do.
- Used the exclusion log as the evidence that the system selects rather than retrieves: for the LNP project, 1,014 high-similarity sections were deliberately excluded (760 generic-only, 245 over a role cap, 9 similar but sharing no specific vocabulary).
- Tuned the selection levers (generic-term suppression, a specific-term requirement, role-aware caps, and core-anchoring) so the two projects diverge for real, inspectable reasons.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- Keeping the demo from reading as top-k search meant foregrounding the dependency ordering and the exclusions rather than the similarity scores.
- Getting two projects to diverge meaningfully without breaking either required iterating on the levers.

## What Claude contributed (assistant)

- Produced the two demo roadmaps and the exclusion analysis from my design.
- Drafted the comparison visuals.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted the exclusion log as core paper evidence; I rejected any framing that reduced the system to retrieval.
