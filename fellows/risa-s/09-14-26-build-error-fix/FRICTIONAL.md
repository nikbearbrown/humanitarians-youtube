# Friction Log: Week 2 (09-14-26 to 09-18-26): Figure mapping and a failed build

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer
Report: Week2_09-14-26.mp4 
Hours Log: HOURS.md
Report Week: 09-14-26 to 09-18-26

Append new entries below. Never rewrite an earlier entry.

---

## Entry 1: week of 09-14-26 

Work done for this week. Video made 09-14-26. Drafted from my commit log and build-error chat.

### 1. Focus of the week

- Mapping images into the textbook: Chapter 16 and Chapter 19 subsections (09-16-26), and a table plus images in Chapter 11 (09-16-26 and 09-17-26).
- Fixing a failed build in a Chapter 16 file (09-17-26): `Unexpected end of file in name`, line 76, column 727.
- Merging `development` into my `visual-edits` branch (09-17-26).
- Making the report video on the build fix (11-15-26).

### 2. What was tried, and what was expected

- The build failed and named one file. The error wording, "unexpected end of file in name", means the parser ran out of file in the middle of reading a tag.
- First attempt: look at line 76. It is one very long line (a figure caption), so reading the line did not show the problem.

### 3. Points of resistance, and next steps taken

- The line number alone was not useful because the line is so long. The column number was: I printed only the characters around column 727 (about characters 690 to 800).
- The end of the caption showed a closing paragraph tag missing its final bracket: `</p` instead of `</p>`. I added the `>` and committed the fix (09-17-26, "Update 6_Clinical_Implications_and_Therapeutic_Applications.mdx").
- Video: the 7-scene reel rendered at 3840 x 2160, 105.2 seconds. The frame-level quality check (GATE V) reported 10 MAJOR findings, as it did for my Week 1 video; I built the final cut with `ART_STRICT=0`.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) explained what the error wording meant, suggested printing only the characters around the reported column, and helped spot the missing bracket. I made the edit and committed it myself.
- Claude generated the video's beat sheet from my commit log and the build-error chat, keeping the narration to what those support. I ran the render commands and checked the output.
- Not used: the video makes no claim about the build result after the fix, because I had not re-checked it.

### 5. Understood now, and still unresolved

Understood
- For very long lines, the column number matters more than the line number.
- "Unexpected end of file in name" points to an unfinished tag, not to the end of the file.

Unresolved
- Did the build pass after the fix? [CONFIRM and write the answer here]
- The same chat also mentioned a duplicate figure label (16.6.2). This entry does not cover it.
- CAJAL reports for Chapters 8, 22, 23 and 24 may belong to this week or the previous one. This entry does not claim them.

**Evidence**
- Reel folder in the Brutalist toolkit (`week2-build-fix`): `beat_sheet.json`
- Final video, 4K 16:9: https://drive.google.com/file/d/1MfxanfTGfR6zT4zsYW7UBUnX3C4zX28X/view?usp=drive_link
- Commits in the textbook repository (09-16-26 and 09-17-26, including the build fix)
