# Week of 2026-09-07: Textbook-Wide Figure, Video and Table Renumbering

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** This report was written on 09-07-2026. 

---

## Summary

Figure captions across the MDX textbook had drifted into inconsistent formats as new images were added by different people. I wrote and ran a script that standardizes every figure, video and table caption to a `Chapter.Section.Number` scheme (for example, Figure 4.2.1), delivered through a feature branch and a pull request into `development`.

## The problem

- Recent image additions had introduced hyphenated and lettered names such as `4-4-2b`, `6-3-3a` and `14-2-2` into captions.
- Evin flagged the naming inconsistency and asked for one scheme across the whole book.
- The target format agreed was `Figure Chapter.Section.ImageNumber`, for example Figure 4.2.1.

## What I built

- A Python script that finds caption lines of the form `<strong>Figure X: ...</strong>` in every chapter's MDX files and rewrites only the number.
- A dry-run mode that lists every proposed change per chapter before any file is touched.
- A second version that handles figures, videos and tables in one pass and recalculates all numbers from scratch rather than adjusting existing ones.

## How I checked it

1. Ran the dry run and compared the counts against my own reading of the chapters.
2. Noticed Chapter 1 showed no changes even though it has figures. The pattern missed captions with extra whitespace after `<strong>`, so I had the pattern fixed and re-ran across all chapters.
3. Applied the changes, then reviewed the diff in GitHub Desktop to confirm only the number text changed (for example `Figure 1.1` to `Figure 1.2.1`), not captions, image tags or sources.
4. Committed to a new branch off `development` and opened a pull request for Evin to review.

## Results

- Figures renumbered: https://github.com/Medhavy/medhavi-cancer
- Chapters touched: https://github.com/Medhavy/medhavi-cancer
- Files changed: https://github.com/Medhavy/medhavi-cancer
- Pre-existing numbering bugs found along the way: duplicate numbers, and figures labeled under the wrong chapter.

## Open items

- **Chapter 25 summary file:** `11_Summary.mdx` was skipped by the script, so Figures 25.5, 25.6 and 25.7 inside it still have old-style numbers. It needs a numbered frontmatter title or a manual fix.
- **Figure/Video collision:** Figure 1.4.1 and Video 1.4.1 can now coexist. I need to confirm with Evin that this is the intended convention.

## Hours

30 hours

## Videos this week

- Progress update: figure renumbering (cli-explainer, Bella) - https://drive.google.com/file/d/19-FmDfy0Ng5DOgxPsJG6M5DJdGpIQtJ0/view?usp=drive_link
