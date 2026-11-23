# Friction Log: Week 1 (Sep 7 to Sep 11, 2026): Figure renumbering and report video

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer
Report: work_report.md
Hours Log: HOURS.md
Report Week: Sep 7 to Sep 11, 2026

Append new entries below. Never rewrite an earlier entry.

---

## Entry 1: written Sep 7 to Sep 11, 2026

*This entry was written after the fact from my working notes and chat history. It describes the process as I understand it now.*

### 1. Focus of the week

- Renumbering every Figure, Video and Table caption in the textbook's MDX files into one scheme, Chapter.Section.Index, with a script (`renumber_all.py`).
- 2026-09-10: edit to `4_Monoclonal_Antibodies.mdx` (commit in the textbook repository).

### 2. What was tried, and what was expected

I expected one regex pass over the MDX captions to renumber everything to `Chapter.Section.Number`, with a quick diff review at the end.

### 3. Points of resistance, and next steps taken

- **Chapter 1 showed no changes in the dry run, but it has figures.** I pushed back on the result. The caption pattern did not allow extra whitespace after `<strong>`. The pattern was fixed and the full dry run repeated across all chapters.
- **Codespaces was disabled at the organization level.** The terminal route I had planned was blocked, so I switched to a local copy of the repo and GitHub Desktop.
- **Development changed under me.** My first branch was cut before newer image additions landed on `development`. Rather than merge it and risk conflicts, I discarded it and re-ran the script fresh on current `development` in a new branch, which gave the same result without a conflict.
- **The script skipped Chapter 25's `11_Summary.mdx`.** It has no numbered frontmatter title, so its figures kept old-style numbers. I left it as a tracked open item rather than hand-editing around the script.

### 4. AI and other contributions: accepted, changed, rejected

- Claude wrote the script and the dry-run/apply workflow, and the step-by-step GitHub Desktop instructions.
- Accepted: the dry-run-first approach; I checked the counts myself.
- Rejected: the first result for Chapter 1, which I had fixed.
- Changed: I chose to delete the older branch instead of merging it.
- I did not accept the output as correct on first look. The Chapter 1 miss only showed up because I knew that chapter had figures.

### 5. Understood now, and still unresolved

Understood
- A plausible-looking result can be wrong in a quiet way, and the check that caught it was knowing the content, not reading the output.

Unresolved
- Confirm with Evin whether Figure 1.4.1 and Video 1.4.1 coexisting is the intended convention.
- Fix the numbering in Chapter 25's summary file.

---

## Entry 2: written 09-07-2026 (later than the week it covers, 09-07-2026): rebuilding the report video

### 1. Focus of the week

- Re-making my Brutalist report video on `renumber_all.py`, the script that renumbered every Figure, Video and Table caption in the Medhavy textbook as Chapter.Section.Index.
- Reviewer feedback from Sanjana Rao: the opening card showed the @NikBearBrown handle and should show @HumanitariansAI (or my own name). I also needed my name on the video and a 4K 16:9 render.

### 2. What was tried, and what was expected

- I expected to change one handle in `beat_sheet.json` and re-render.
- Searching `beat_sheet.json` for the old handle found nothing. The handle came from a default (`folderLabel`, default `@NikBearBrown`) in the `ClaudeComposerAsk` scene in `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx`.
- I set `folderLabel` to `@HumanitariansAI` on the four composer beats (B00, B02, B05, B08), moved the old clips aside so they would re-render, and rebuilt.

### 3. Points of resistance, and next steps taken

- Claude suggested a `--persona hai` flag on `./art run`. The `art` script does not take it. I found the real cause by searching the scene source instead.
- The frame checker (GATE V) failed with 10 MAJOR findings (underfill, low contrast) in B01, B04 and B09. I looked at the contact sheet, the text was readable, and I built the final cut with `ART_STRICT=0`.
- The code scene (B03) still had a placeholder instruction on screen and used functions that are not in my real script. `renumber_all.py` was no longer on my machine (it was never committed). I replaced the code with excerpts using only lines I could confirm from my earlier session record, with `...` where code is trimmed.
- The narration said the script tracks the section "from its heading". The script reads the section from each file's frontmatter title. I also removed three claims I could not support: that image filenames move with the captions, that the diff shows "collisions: 0", and an example (Figure 4.1 becoming 4.2.1) I could not find in my records. I regenerated the audio.
- The first audio regeneration silently did nothing. My Terminal's `python3` alias pointed at Python 3.11 without `kokoro-onnx`; the project's `.venv` is Python 3.12. Calling `.venv/bin/python` directly fixed it.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) walked me through the commands, found the `folderLabel` setting, wrote the edits to `beat_sheet.json`, and flagged the unsupported claims in the narration.
- I ran every command and checked the frames myself.
- Accepted: the `folderLabel` fix, `ART_STRICT=0` for the final cut, the corrected narration.
- Rejected: the `--persona` flag (it does not exist). I did not produce a 9:16 Short, because only the 16:9 was needed.

### 5. Understood now, and still unresolved

Understood
- Brutalist scenes can carry the original author's channel as a default, so check the scene source when a handle will not change.
- Always call the project's own Python.

Unresolved
- The final caption counts differ between my notes, so I need to take them from the merged PR before putting numbers on screen.
- Whether Figure 1.4.1 and Video 1.4.1 sharing a number is the convention Evin wants is still unconfirmed.
- Brutalist has no portrait versions of the code and diff scenes, so a 9:16 cut of this reel is not possible without new scenes.

**Evidence**
- Reel folder in the Brutalist toolkit: `beat_sheet.json` and its backups (`beat_sheet.backup.json` to `beat_sheet.backup4.json`), `qc-sheet.png`, `_qc/REPORT.md`
- Final video, 4K 16:9: https://drive.google.com/file/d/19-FmDfy0Ng5DOgxPsJG6M5DJdGpIQtJ0/view?usp=drive_link
- Commits / pull request in the textbook repository: https://github.com/Medhavy/medhavi-cancer
