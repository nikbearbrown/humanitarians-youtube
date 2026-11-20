# Friction Log: Week 9 (11-02-2026 to 11-06-2026): A zero is a claim to check

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer
Report: Week9_11-02-2026.mp4 https://drive.google.com/file/d/1U5XqSPH8PjO_KAHZy2alToTBfqAucltr/view?usp=drive_link
Hours Log: HOURS.md
Report Week: 11-02-2026 to 11-06-2026


---

## Entry 1: written 11-02-2026 

### 1. Focus of the week

- A how-to video: why a dry run that reports "no changes" deserves a second look, using the Chapter 1 miss in my renumbering script as the example. [CONFIRM: what you actually worked on this week, in your own words]
- Making the video (11-02-2026).

### 2. What was tried, and what was expected

- I ran the renumbering script as a dry run across every chapter before writing any files.
- Expectation: where it said "no changes needed", there would be nothing to renumber.

### 3. Points of resistance, and next steps taken

- **Chapter 1 reported no changes, but it has figures.** I pushed back. The captions were written as `<strong> Figure 1.1:` with an extra space after the tag, and the script's pattern did not allow for it. I had it allow optional whitespace after `<strong>`, and re-ran every chapter. That found three more figures in Chapter 1 and one more in Chapter 14.
- **The chapters that still showed zero.** I searched each one for the word "figure". Chapter 28 uses a different caption format, with no colon after the number (for example `Figure 28.1 Enhanced permeability...`), so the script had silently skipped all six of its figures. Chapters 12 and 34 turned out to be false alarms ("central figure", "mitotic figures").
- **A second fix.** The pattern was relaxed so it no longer requires a colon right after the number. After that, Chapter 14 went from 2 detected figures to 10, so the first pattern had been missing many figures across many chapters.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) wrote the script and both pattern fixes, and ran the checks on the zero-figure chapters.
- I caught the first miss by knowing Chapter 1 has figures. That check came from me, not from the output.

### 5. Understood now, and still unresolved

Understood
- A zero, or a low count, is a claim to check. Search the raw files for the keyword in every chapter that reports nothing, and sort the hits into real misses and false alarms.
- A script that fails silently looks the same as a script that finds nothing.

Unresolved
- The Chapter 25 summary file is still skipped silently, because its frontmatter has no numbered title.
- Whether Figure 1.4.1 and Video 1.4.1 sharing a number is the convention Evin wants.

**Evidence**
- Reel folder in the Brutalist toolkit (`week9-zero-is-a-claim`): `beat_sheet.json`
- Final video, 4K 16:9: https://drive.google.com/file/d/1U5XqSPH8PjO_KAHZy2alToTBfqAucltr/view?usp=drive_link
- The renumbering pull request: https://github.com/Medhavy/medhavi-cancer
