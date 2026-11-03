# FRICTIONAL.md - The Links That Weren't There

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-10-25-prereq-recall-gap`
**Date:** Oct 25, 2026 (week ending October 24, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Diagnosed why the later, applied chapters came out with almost no required prerequisites, and built a content-grounded fix.

## What I did (my contribution)

- Ran a failure analysis on the prerequisite graph after Dr. Gultepe's feedback: I ruled out the redundancy cleanup as the cause and separated two distinct failures, mis-tiering and missing edges. 13 of 19 applied chapters had only 0-1 required cross-chapter prerequisite (for example, Chemotherapy required only Chapter 1 and never linked to Metabolism or the Tumor Microenvironment).
- Named the problem in research terms: a recall problem in prerequisite extraction, compounded by a generality bias toward a few foundational chapters, which is why the gap grows for the later, integrative chapters.
- Designed and built a content-grounded fix: derive each applied chapter's prerequisites from the concepts it actually uses in the text. This produced 146 proposals (127 add, 10 promote, 9 already present) and dropped all 13 under-connected chapters to zero; for Chapter 23, Metabolism and Principles of Cancer Therapy are recovered as required.
- Added a gap-check script that flags under-connected applied chapters so this cannot silently recur (25 issues on the current graph), and kept the whole fix as a reviewable proposal, not an applied change, pending faculty confirmation of the tiers.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- Dr. Gultepe's Chapter 23 example looked like it might be caused by my redundancy cleanup; I checked the pre-cleanup graph and proved the gap predated it, which redirected the fix to the real cause rather than the symptom.
- I had to recover the missing edges without hand-authoring each one; grounding them in every chapter's own concept tags made the proposal principled and reviewable instead of guesswork.

## What Claude contributed (assistant)

- Implemented the failure-analysis scripts, the content-grounded proposal generator, and the gap-check to my design.
- Drafted the tables comparing before and after.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted the content-grounded recall fix as a reviewable proposal and the gap-check as prevention; I rejected the assumption that the redundancy cleanup caused the gap, and I did not apply the new edges without faculty sign-off.
