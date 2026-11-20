# Week of 09-28-26: Visual Tracker

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** This report was written on 09-28-2026

---

## Summary

A new tracker for all the textbook's visuals, requested by Evin: one Google Sheet with every figure in one table, in place of separate tables per chapter. 

## What was built

- One Data table with all 187 figures, with dropdowns for status, assignee, type and chapter, all taken from one Config list.
- Automatic Last Updated stamps and a change log.
- Comments that stack instead of overwriting, per-person filter views, a setup checker, optional email alerts, and a dashboard made from plain count formulas.
- Design rule: formulas where the sheet can do it, script only where it can't.

## Data cleanup

- "good to upload", "ready to upload" and "done good to upload" became Good to Upload (10 figures).
- "chart", "graph" and "bar chart" became Chart.
- 140 approved figures with an owner but no status became Not Started.

## Open questions for Evin

- Figure 1.6 had "good to upload" but no decision.
- Figure 1.5 is rejected but still assigned to Shishir.
- Figures 14.4 and 16.10 had no information and are marked Suggested.
- Whether "Good to Upload" means approved and "Done" means placed in the document, or the reverse.

## Hours

30 hours

## Videos this week

- Progress update: the visual tracker (cli-explainer, Bella). https://drive.google.com/file/d/15YD_lUKasZ7B8oKdGvM-lx81CsTJ58Cx/view?usp=drive_link
