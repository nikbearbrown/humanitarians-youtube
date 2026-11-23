# Friction Log: Week 7 (10-19-2026 to 10-23-2026): Placing a figure in an MDX chapter

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: [link to the textbook repository]
Report: Week7_10-19-2026.mp4 https://drive.google.com/file/d/1FReFaSN-WpT9-hvccn0IMZpKVdkT5cvJ/view?usp=drive_link
Hours Log: HOURS.md
Report Week: 10-19-2026 to 10-23-2026


---

## Entry 1: written 10-19-2026 

*This week's video is a how-to about placing figures in MDX chapters. The notes below come from my image-placement chat (last active 11-18-2026) and my earlier reports, so I am not claiming when each figure was placed. I re-read this entry and corrected anything that does not match what happened.*

### 1. Focus of the week

- A how-to video: placing a figure in an MDX chapter, using the CTLA-4 and PD-1/PD-L1 pathway figures as the example. 
- Making the video (10-19-2026).

### 2. What was tried, and what was expected

- I gave Claude the figure data (a Drive link, a reviewer-finalized caption, and revision notes) and the format of my chapter files, and asked for the MDX to place each figure.
- Expectation: the tracking sheet's chapter and section for each image would be right.

### 3. Points of resistance, and next steps taken

- **The same two images had three different homes.** The tracking sheet assigned them to Chapter 25 (sections 25.2.2 and 25.3.1). Those sections cover target validation and TKI classification and contain no checkpoint material, so I read the destination sections before placing anything and found the mismatch. Earlier drafts used Chapter 16 (16.4.4 and 16.5.4). The latest instructions said Chapter 26 (26.2.2 and 26.2.3), "not 25 or 16".
- **A first draft used a component I guessed.** Claude's first MDX used a `<Figure>` component and asked whether my site uses a different one. The real house format is a centered `<img>` plus a justified caption paragraph, so I asked for it in the same format as my existing files.
- **An image that was not approved.** A lung screening image had gone through several failed correction rounds, and its last note still said to check the comments. I held off placing it until a version was approved.
- **A corrected version.** The CTLA-4 figure had to be the corrected one, with the thymus element removed, before it went live.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) wrote the MDX blocks and flagged the unapproved image and the placement mismatch. I supplied the data, the file names and the format.
- Rejected: the guessed `<Figure>` component.

### 5. Understood now, and still unresolved

Understood
- Read the destination section before placing a figure. A tracking sheet can be wrong.
- A figure's approval status is part of the task. An image still marked "not approved" waits.
- The caption's figure number can stay a placeholder (like 26.2.X) until the position is settled, because the book's numbering comes from where the figure sits.

Unresolved
- The lung screening image still needs an approved version.

**Evidence**
- Reel folder in the Brutalist toolkit (`week7-figure-into-mdx`): `beat_sheet.json`
- Final video, 4K 16:9: https://drive.google.com/file/d/1FReFaSN-WpT9-hvccn0IMZpKVdkT5cvJ/view?usp=drive_link
- The chapter files and commits: https://github.com/Medhavy/medhavi-cancer
