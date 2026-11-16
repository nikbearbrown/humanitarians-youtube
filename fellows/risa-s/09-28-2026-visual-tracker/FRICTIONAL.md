# Friction Log: Week 4 (09-28-26 to 10-02-26): Visual tracker

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: (https://github.com/Medhavy/medhavi-cancer)
Report: Week4_09-28-26.mp4 (https://drive.google.com/file/d/15YD_lUKasZ7B8oKdGvM-lx81CsTJ58Cx/view?usp=drive_link)
Hours Log: HOURS.md
Report Week: 09-28-26 to 10-02-26

---

### 1. Focus of the week

- A new tracker for all the textbook's visuals, requested by Evin: one Google Sheet instead of separate tables per chapter. 
- Importing the real figure data (187 figures) and cleaning free-typed values.
- Making the report video about it.

### 2. What was tried, and what was expected

- Evin's first idea was an Excel file with three tables in every chapter sheet. Claude suggested one table with status-based coloring instead, and Evin forwarded the suggestion with a project brief and asked whether I wanted to build it.
- The design rule I worked to: formulas where the sheet can do it, script only where it can't.
- Plan: a plain Google Sheet first so the team could use it quickly, then Apps Script automation.

### 3. Points of resistance, and next steps taken

- The existing data had free-typed values. "good to upload", "ready to upload" and "done good to upload" all had to become one status, Good to Upload (10 figures). "chart", "graph" and "bar chart" became Chart, and "risa" became "Risa".
- 140 approved figures had an owner but no status. I set them to Not Started.
- Questions only the team could answer: Figure 1.6 had "good to upload" but no decision; Figure 1.5 was rejected but still assigned to Shishir; Figures 14.4 and 16.10 had no information, so they are marked Suggested. I also assumed "Good to Upload" means Evin approved and "Done" means placed in the document, and flagged that to check. 

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) wrote the spreadsheet and the Apps Script files, and the install and import steps. I followed them, imported the data, and replaced the Config, Validate and Alerts files when the design changed.
- Changed: the status words, because my sheet used "In Review" and "Done" where Claude had assumed other names.

### 5. Understood now, and still unresolved

Understood
- One table with dropdowns and one Config list stops values from drifting, because they can only come from that list.
- Letting the sheet do the counting (plain COUNTIF formulas) keeps the dashboard working without script permissions.

Unresolved
- The four open questions above for Evin.

**Evidence**
- Reel folder in the Brutalist toolkit (`week4-visual-tracker`): `beat_sheet.json`
- Final video, 4K 16:9: https://drive.google.com/file/d/15YD_lUKasZ7B8oKdGvM-lx81CsTJ58Cx/view?usp=drive_link
