# Week of 10-05-26: Tracker Config Sheet and Switchover

**Fellow:** Risa Samanta
**Project:** Medhavy cancer textbook (CAJAL)
**Role:** Machine Learning Engineer
**Note on dating:** This report was written on 10-05-2026.

---

## Summary

The second stage of the visual tracker: every team setting moved onto one Config sheet, a problem checker, and switching the live Google Sheet over to the new version. [CONFIRM: what you did on it this week in your own words]

## What was done

- **Config sheet:** holds the statuses and colors, team names and emails, visual types, chapters, Data column names, and a CAJAL link per chapter. The script reads everything from there.
- **Problem checker:** looks for duplicate names, a status with no color, a badly formed email, and Data values that are not on any Config list.
- **Status names:** the script had assumed "Needs Review" and "Published". The Config, Validate and Alerts files were updated to read the team's own names, "In Review" and "Done".
- **Switchover:** import the workbook with Replace spreadsheet, replace the three script files, run Set up / repair, run Check for problems, create a filter view for each person. The original Excel file stays as a backup for about a week.

## Reuse

Make a copy of a working tracker (the script comes with it), edit Config, run setup, run the checker. No code changes are needed.

## Open items

- Not built yet: a sidebar form for adding an item, and an import helper that turns the AI chapter report into Data rows.

## Hours

32 hoours 

## Videos this week

- Progress update: the tracker Config sheet (cli-explainer, Bella). [Drive link]
