# Frictional Log -- Chapter 23 Fact-Check Review

**Date:** September 14, 2026
**Fellow:** Kehinde Obidele
**Work:** Fact-check review of Chapter 23

## What I set out to do

Review all flagged claims across three tabs (main chapter, AI-Only, and Editorial) in the Chapter 23 workbook. Apply the verification workflow refined over Chapters 1 and 2.

## What I expected

I expected to move faster with the established workflow. I also expected the AI-Only tab to have fewer issues since those claims were marked as not needing human review.

## Where it resisted

Chapter 23 had 86 rows across all three tabs, which was a large volume. The AI-Only tab did have errors despite being flagged as not needing human review, confirming that every tab needs checking regardless of the AI's confidence level.

The Editorial tab had formatting and encoding issues from AI generation (garbled text, broken characters). These were straightforward to identify but required a different approach than factual verification. They needed encoding fixes as a separate step before content corrections.

## What I did next

I worked through all three tabs systematically. For the main chapter and AI-Only tabs, I followed the standard verification process. For the Editorial tab, I documented the formatting issues and noted that they need encoding fixes as a separate commit before any content edits (per the standing rule in CLAUDE.md).

I created a step-by-step Workbook Update Guide for Chapter 23, the same as I did for Chapter 1.

## What Claude or another person contributed

Claude helped with citation lookups and cross-referencing. I made all verification decisions after reviewing sources directly. The encoding fix approach (separate commit first) was established as a standing workflow rule.

## What I accepted, changed, or rejected

I accepted that the AI-Only tab cannot be trusted and needs the same level of review as the main chapter tab. I accepted the separate-commit approach for encoding vs. content fixes. I rejected the idea of skipping Editorial tab items since they still affect the published text quality.

## Result

Chapter 23 fact-check review complete. 86 rows reviewed across three tabs. Workbook updates done. Text corrections submitted as part of PR #46 on Medhavy/medhavi-cancer.
