# Friction Log: Week 6 (10-12-2026 to 10-16-2026): From a report table to a textbook table

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer
Report: Week6_10-12-2026.mp4 https://drive.google.com/file/d/1dQgfo1mCXDn-rZmYvVDhU7vOxL7our3E/view?usp=drive_link
Hours Log: HOURS.md
Report Week: 10-12-2026 to 10-16-2026


---

## Entry 1: written 10-12-2026 

*This week's video is a how-to about building textbook tables. The notes below come from my table-building chat, which was last active on 11-10-2026, so I am not claiming when each table was built. I re-read this entry and corrected anything that does not match what happened.*

### 1. Focus of the week

- A how-to video: turning a table from a CAJAL report into a finished MDX table with a PDF preview. 
- Making the video 10-12-2026.

### 2. What was tried, and what was expected

- The method: give Claude one finished table file (`ch14_visual11.mdx`) and its preview as the style template, plus the chapter's audit file, whose entries are marked "Type: Table". Ask for matching MDX files and a PDF preview.
- For Chapter 25 this produced two tables: Visual 6 (TKI Target Classification) and Visual 18 (Biomarker Type Classification), with `ch25_tables_preview.pdf`.

### 3. Points of resistance, and next steps taken

- **No red in the Chapter 25 tables.** I asked why. In the Chapter 14 table, red marks the one row where the source text names a negative finding, and blue marks a working mechanism. The Chapter 25 tables contain nothing negative, so they have no red. I left them as they were.
- **A color legend that did not fit.** I pasted a four-tier legend (including "absence defines CSC") that belongs to a different table. Claude checked the Chapter 25 file, found no matching text, and asked what I meant before recoloring anything.
- **No G1 row in the chemotherapy table (Table 23.2.1).** The chapter mentions G1 only as checkpoint biology and names no G1-specific drug class, so a G1 row would have no source text behind it. A reply to Evin was drafted offering to add one if she wants it, with a matching sentence in the text.
- **Chapter 32 subtypes.** For the Mesenchymal and Neural subtypes the source gives no treatment response, so the table carries a gray italic note instead of an invented answer.
- **A missing preview.** At one point I could not see a table preview. The file was still there, and Claude presented the current version again.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) built the table files and the PDF previews, and checked each table against the chapter text.
- Accepted: leaving red out of the Chapter 25 tables, and leaving the G1 row out.
- Changed: in Table 23.5.2, "Hypoxic cells are non-proliferating" became "slow cycling" (Evin's note). The cross-reference to Table 23.5.3 changed because of the renumbering.
- [CONFIRM: anything else I checked, accepted or rejected]

### 5. Understood now, and still unresolved

Understood
- A table's colors can carry meaning, so a missing color is a question to ask, not a bug.
- "Say only what the chapter says" is the rule that matters most. A missing row is a visible decision someone can reverse.

Unresolved
- Line 124 of the 23.5 file still says "non-proliferating". Evin may want it to say "slow cycling" too.
- Whether Evin wants a G1 row in Table 23.2.1.

**Evidence**
- Reel folder in the Brutalist toolkit (`week6-table-to-mdx`): `beat_sheet.json`
- Final video, 4K 16:9: [add Drive link, sharing set to Anyone with the link can view]
- The table files and previews: [add links]
