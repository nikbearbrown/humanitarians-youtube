# Week of 10-26-2026: Reading a Merge Conflict

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** This report was written on 10-26-2026.

---

## Summary

A how-to on reading a merge conflict and checking the file after resolving it, using the conflict in my Chapter 23.4 file as the example. [CONFIRM: what you did this week in your own words]

## The example

- My branch (`visual-edits`) inserted Table 23.4.1 above a heading with garbled characters. `development` had fixed those characters. Git marked both versions of that one line.
- Table 23.4.2 merged cleanly, because it was not next to a changed line.
- My first resolution removed the markers but kept the garbled heading and the old wording. Committing it would have overwritten `development`'s fixes.

## The checks

1. Search the file for the three marker lines.
2. Search for garbled characters.
3. Search for a phrase that only `development` has, to prove its text is in the file.

If the third search finds nothing, abort the merge and merge again, keeping both parts.

## Prevention

Pull `development` into the branch before inserting tables.

## Open items

- Stray glitches in the 23 file from `development` (an encoding error, missing punctuation, misplaced brackets) may need fixing by Evin.

## Hours

34 hours

## Videos this week

- How-to: reading a merge conflict (cli-explainer, Bella). https://drive.google.com/file/d/1OIxC8k6vanyyjZgVpVy19nnREnIl222S/view?usp=drive_link
