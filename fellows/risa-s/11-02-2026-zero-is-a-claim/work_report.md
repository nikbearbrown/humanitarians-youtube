# Week of 11-02-2026: A Zero Is a Claim to Check

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** This report was written on 11-02-2026.
---

## Summary

A how-to on why a dry run that reports "no changes" deserves a second look, using the Chapter 1 miss in my renumbering script as the example. [CONFIRM: what you did this week in your own words]

## The example

- The first dry run said Chapter 1 needed no changes. It has figures. The captions had an extra space after `<strong>`, which the pattern did not allow. Fixing that found three more figures in Chapter 1 and one more in Chapter 14.
- Chapters that still showed zero were searched for the word "figure". Chapter 28 uses a different caption format (no colon after the number), so all six of its figures had been skipped. Chapters 12 and 34 were false alarms.
- After the second fix, Chapter 14 went from 2 detected figures to 10.

## The method

1. Treat a zero, or a low count, as a claim to check.
2. Search the raw files for the keyword in every chapter that reports nothing.
3. Sort the hits into real misses and false alarms.

## Open items

- The Chapter 25 summary file is still skipped silently (no numbered frontmatter title).
- Whether Figure 1.4.1 and Video 1.4.1 sharing a number is the intended convention.

## Hours

35 hours

## Videos this week

- How-to: a zero is a claim to check (cli-explainer, Bella). https://drive.google.com/file/d/1U5XqSPH8PjO_KAHZy2alToTBfqAucltr/view?usp=drive_link
