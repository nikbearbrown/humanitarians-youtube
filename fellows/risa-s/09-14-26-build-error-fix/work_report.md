# Week of 09-14-26: Image Mapping and a Failed Build Fix

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** The textbook work below was done on 09-16-26 and 09-17-26. This report was written on 09-14-26, after the week it covers.

---

## Summary

This week I mapped images into three chapters of the textbook (Chapters 11, 16 and 19) and fixed a failed build in a Chapter 16 file. The build error pointed at a very long line, and the cause was one unfinished closing tag.

## The problem

- The build failed with `Unexpected end of file in name`, at line 76, column 727 of a Chapter 16 file (`6_Clinical_Implications_and_Therapeutic_Applications.mdx`).
- Line 76 is a single very long line (a figure caption), so reading the line did not show where the problem was.

## What I did

- **Image mapping (09-16-26 and 09-17-26):** images mapped into Chapter 16 and Chapter 19 subsections; a table added to Chapter 11; a Chapter 11 image uploaded and mapped.
- **Build fix (09-17-26):** printed only the characters around column 727 (about characters 690 to 800). The end of the caption had a closing paragraph tag missing its final bracket (`</p` instead of `</p>`). I added the `>` and committed the fix.
- **Branch housekeeping (09-17-26):** merged `development` into my `visual-edits` branch.

## How I checked it

1. Read the error wording: "unexpected end of file in name" means the parser ran out of file while reading a tag.
2. Used the column number, not the line number, to find the spot.
3. Compared the end of line 76 before and after the fix. [CONFIRM: re-ran the build after the fix, and say whether it passed]

## Results

- Commits (all by me): mapping images to Chapter 16, mapping images to a Chapter 19 subsection, adding the Chapter 11 table, uploading and mapping a Chapter 11 image, the Chapter 16 file fix, and the `development` merge. [add commit links]
- Build after the fix: [CONFIRM]

## Open items

- Whether the build passed after the fix is not yet recorded here.
- The same chat mentioned a duplicate figure label (16.6.2). I have not covered it in this report.

## Hours

28 hours

## Videos this week

- Progress update: the build error fix (cli-explainer, Bella). https://drive.google.com/file/d/1MfxanfTGfR6zT4zsYW7UBUnX3C4zX28X/view?usp=drive_link
