# Frictional Log -- Chapter 1 Fact-Check Review

**Date:** September 4, 2026
**Fellow:** Kehinde Obidele
**Work:** Fact-check review of Chapter 1 (Introduction to Cancer Biology)

## What I set out to do

Review every flagged claim in the Chapter 1 workbook (`01_factcheck_review.xlsx`). For each row, verify the claim against authoritative sources and record a Reviewer Decision, Reviewer Comments with source URLs, and a Suggested Phrase for any corrections.

## What I expected

I expected most TRUE-flagged claims to be accurate and the FALSE/FLAGGED ones to need corrections. I assumed the AI-generated citations would point to real papers.

## Where it resisted

The biggest friction was fabricated citations. The AI generated real-looking PMCIDs paired with wrong author names. For example, "Otto and Bhatt, 2022" was assigned to PMC9583502, but those are not the actual authors of that paper. I had to look up each PMCID on PubMed to verify the real authors.

Some statistics were close but not accurate. The textbook said "10-30%" in places where the source actually said "25-30%." These near-misses are harder to catch than outright errors because they sound plausible.

Outdated figures were another issue. The textbook cited 10^14 cells in the human body, but modern estimates put the number at 3 x 10^13. Deciding which version of a number is "correct" required finding the most current consensus.

## What I did next

I built a systematic workflow: read the flagged sentence, locate the cited source on PubMed or FDA databases, confirm whether the citation is real and the claim is supported, then record my decision and comments. I created a step-by-step Workbook Update Guide so the process is repeatable.

## What Claude or another person contributed

Claude helped me look up PMCIDs and cross-reference author names against PubMed records. I verified every result myself before recording it. Evin (PM) provided the workbook and initial guidance on what the review columns should contain.

## What I accepted, changed, or rejected

I reviewed 136 rows total: 105 TRUE, 21 FALSE, 10 FLAGGED. I accepted claims that matched their cited sources. I marked claims as Needs Revision when the citation was wrong, the statistics were inaccurate, or the authors were fabricated. I rejected claims with no supporting evidence at all. I created an Evidence Document (Word format) with the full source chain for every claim checked.

## Result

Chapter 1 fact-check review complete. Workbook updates done. Evidence document created. Text corrections submitted as part of PR #46 on Medhavy/medhavi-cancer.
