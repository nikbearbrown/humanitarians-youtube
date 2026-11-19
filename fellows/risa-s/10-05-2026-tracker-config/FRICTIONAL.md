# Friction Log: Week 5 (10-05-26 to 10-09-26): Tracker Config sheet and switchover

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer
Report: Week5_10-05-2026.mp4 https://drive.google.com/file/d/1s7PPbWjYdkI0PyrmjsHy-ek3pjlIU1a7/view?usp=drive_link
Hours Log: HOURS.md
Report Week: 10-05-26 to 10-09-26

Append new entries below. Never rewrite an earlier entry.

---

## Entry 1: written 05-10-2026 


### 1. Focus of the week

- Finishing the visual tracker: moving every team setting onto one Config sheet, the problem checker, and switching the live Google Sheet over to the new version. [CONFIRM: which parts fell this week, and anything else you worked on]
- Making the report video about it.

### 2. What was tried, and what was expected

- Expected the same script to work for our team without changes.
- Plan: keep my existing Google Sheet, import the new workbook with "Replace spreadsheet", replace the three updated script files, then run the setup and checker.

### 3. Points of resistance, and next steps taken

- The script had assumed two status names ("Needs Review" and "Published"), but my sheet uses "In Review" and "Done". The Config, Validate and Alerts files were updated to read those two names from the Config sheet, so the checker and the email alerts follow the team's wording.
- I did not understand what the three script files were for, so I asked, and got the answer: Config reads the settings, Validate runs the problem check, Alerts sends the optional emails. That is what let me replace just those three.
- The switchover took five steps: import and replace the sheet, replace the three script files, run Set up / repair, run Check for problems, create a filter view for each person. The original Excel file stays as a backup until everyone has used the new sheet for about a week.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) wrote the script files and the workbook, explained what Config, Validate and Alerts do, and gave the switchover steps. I followed them.
- Changed: the "In Review" and "Done" status names, to match the team's wording.

### 5. Understood now, and still unresolved

Understood
- Putting every setting on one Config sheet means the team can change statuses, people, types and chapters by editing cells, not code.
- A checker that reports anything on the Data sheet that is not on a Config list catches silent errors, such as a leftover misspelled status.
- To reuse the tracker: make a copy, edit Config, run setup, run the checker.

Unresolved
- Roadmap items not built: a sidebar form for adding an item, and an import helper that turns the AI chapter report into Data rows.

**Evidence**
- Reel folder in the Brutalist toolkit (`week5-tracker-config`): `beat_sheet.json`
- Final video, 4K 16:9: https://github.com/Medhavy/medhavi-cancer
- The tracker sheet and the script files: https://drive.google.com/file/d/1s7PPbWjYdkI0PyrmjsHy-ek3pjlIU1a7/view?usp=drive_link
