# FRICTIONAL.md - Which One Is Right? Scoring Taggers Against a Gold Set

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-08-23-personalized-roadmap-goldenset`
**Date:** Aug 23, 2026 (week ending August 24, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Built a gold standard so tagger quality could be judged against truth, not just against another tagger.

## What I did (my contribution)

- Designed and built the gold-standard protocol: a sampler that prioritises materials tags and rule-vs-LLM disagreements, and a scorer reporting precision, recall, and F1 per field against faculty truth.
- Decided which fields faculty must judge versus which I could author-grade, and built a blind-grading mode (the tag's source hidden in a separate key file) so my own grading stayed unbiased.
- Built a two-annotator workflow (Cohen's kappa plus a disagreement-adjudication file) and an evidence locator that quotes the supporting sentence for each tag (191 of 333 tags were literally present in the text).
- Generated the final 20-section, 333-tag gold sheet ready for grading.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- I realised a tagger-vs-tagger comparison can never declare a quality winner; I added gold-vs-truth scoring to fix the gap.
- Designing the blind split so I could grade honestly without seeing which tagger produced a tag took deliberate care.

## What Claude contributed (assistant)

- Implemented the gold-review builder, the blind-mode split, the scorer, and the evidence locator to my spec.
- Generated the sampled sheets.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted author-grading only for objective fields and only blind, reserving faculty review for genuine judgment; I rejected any quality verdict drawn from taggers alone.
