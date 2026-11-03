# FRICTIONAL.md - What an Ablation Can (and Can't) Decide - Full-Book Tagging

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-08-17-reading-roadmap-ablation-aug17`
**Date:** Aug 17, 2026 (week ending August 16, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Scaled the tagging ablation to the whole book and stated honestly what it decides.

## What I did (my contribution)

- Scaled the ablation to the full book: all 1,340 sections tagged by both taggers, with the LLM pass run across resumed GPU-cluster sessions.
- Measured the real stakes: at full scale the materials-tag agreement held up (Jaccard 0.919, recall 0.921 over 102 sections), but tagger choice changes about 74% of a student's reading list (roadmap Jaccard 0.257 on both demo projects).
- Drew the honest boundary: the ablation settles reproducibility and that the choice matters, but not which tagger is correct, which needs a gold standard.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- My earlier 'deterministic is basically free' line was too simple; the full-book run showed the taggers are reproducible but not equivalent, so I corrected the claim.
- I kept the narrative explicit about what remained undecided rather than overclaiming a winner.

## What Claude contributed (assistant)

- Ran the full-book tagging passes and the downstream-impact comparison.
- Drafted the result tables from the runs.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted the reproducibility-and-impact conclusion; I rejected naming a better tagger without truth to measure against.
