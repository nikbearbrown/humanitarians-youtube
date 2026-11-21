# Friction Log: Week 11 (11-16-2026 to 11-20-2026): A new figure renumbers its neighbors

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer/tree/development
Report: Week11_11-16-2026.mp4 https://drive.google.com/file/d/1l2nU_k5_yJAao69GkhllCIAkMGrDdkba/view?usp=drive_link
Hours Log: HOURS.md
Report Week: 11-16-2026 to 11-20-2026

---

## Entry 1: written 11-19-2026 

### 1. Focus of the week

- Adding the 5-fluorouracil (5-FU) mechanism figure to section 23.3.2 (Antimetabolites) of the Chapter 23 file, and renumbering the figures around it.

### 2. What was tried, and what was expected

- I gave Claude the figure and its caption text and asked for the MDX and the renumbering, saying I would make the edits in the file myself.
- Expectation: the new figure would take the next number.

### 3. Points of resistance, and next steps taken

- **The new figure sits earlier in the file than the two existing figures.** The file already had Figure 23.3.1 (ATR-Induced Damage, in 23.3.3) and Figure 23.3.2 (Taxol Molecule, in 23.3.4). Because numbers follow document order, the new figure becomes 23.3.1, which pushes the other two to 23.3.2 and 23.3.3.
- **A placeholder label.** While reading, Claude used 23.3.3 as a temporary label for the new figure, then gave the exact renumbering table: three captions to edit.
- **The tables in that section did not need changes.** Tables are numbered separately and were already sequential (23.3.1 to 23.3.5). That also means a figure and a table can share a number, such as Figure 23.3.1 and Table 23.3.1.
- Next step: I made the three caption edits by hand. 

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) wrote the MDX, the corrected caption, and the renumbering table.
- Accepted: the renumbering table, applied by hand instead of running the renumbering script, since it was three captions.

### 5. Understood now, and still unresolved

Understood
- A figure added in the middle of a file renumbers every later figure, and the order of the file decides all of it.
- Figures and tables are numbered separately.

Unresolved
- Whether a figure and a table sharing a number is what Evin wants. This is the same kind of question I have open about figures and videos.

**Evidence**
- Reel folder in the Brutalist toolkit (`week11-5fu-figure-numbers`): `beat_sheet.json`
- Final video, 4K 16:9: https://drive.google.com/file/d/1l2nU_k5_yJAao69GkhllCIAkMGrDdkba/view?usp=drive_link
- The commit for the Chapter 23 file: https://github.com/Medhavy/medhavi-cancer/tree/development
