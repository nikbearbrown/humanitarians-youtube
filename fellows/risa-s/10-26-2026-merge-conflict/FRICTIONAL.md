# Friction Log: Week 8 (10-26-2026 to 10-30-2026): Reading a merge conflict

Project: Medhavy cancer textbook (CAJAL figure workflow)
Collaborative Project Repository: https://github.com/Medhavy/medhavi-cancer
Report: Week8_10-26-2026.mp4 https://drive.google.com/file/d/1OIxC8k6vanyyjZgVpVy19nnREnIl222S/view?usp=drive_link
Hours Log: HOURS.md
Report Week: 10-26-2026 to 10-30-2026

Append new entries below. Never rewrite an earlier entry.

---

## Entry 1: written 10-26-2026 

*This week's video is a how-to about reading and checking a merge conflict. The notes below come from my table-building chat (last active 11-10-2026), so I am not claiming when the conflict happened. I re-read this entry and corrected anything that does not match what happened.*

### 1. Focus of the week

- A how-to video: reading a merge conflict, and checking the file after resolving it, using the conflict in my Chapter 23.4 file as the example. [CONFIRM: what you actually worked on this week, in your own words]
- Making the video (10-26-2026).

### 2. What was tried, and what was expected

- I had inserted Tables 23.4.1 and 23.4.2 into the 23.4 file on my `visual-edits` branch, then merged `development` into it.
- Expectation: a clean merge. I got a conflict and asked why.

### 3. Points of resistance, and next steps taken

- **The conflict was one line.** My branch inserted Table 23.4.1 directly above the `Concentration × Time (C×T) Pharmacodynamics` heading, and my copy of that heading still had garbled characters. The `development` branch had fixed those characters. Git could not tell which version to keep, so it marked both. Table 23.4.2 merged cleanly because it was not next to a changed line.
- **My first resolution looked right but was not.** The conflict markers were gone and both tables sat in the right places. But the garbled heading had survived, along with about 40 other garbled spots, and the body text was the old wording from before `development`'s fixes (for example the chlorambucil volume of distribution, the capecitabine absorption wording, the UGT1A1 sentence, and the missing DOACs in the warfarin paragraph). Committing it would have overwritten `development`'s fixes.
- **Next step:** check which version I had by searching the file for `chlorambucil, Vd ~0.3`, abort the merge, merge `development` again, and keep both parts: the table block and the clean heading.
- **Other glitches noticed in the file, from the `development` side:** an encoding error in the Blood-Brain Barrier section, missing punctuation in the Vd bullet, and misplaced brackets in the capecitabine, UGT1A1 and DOAC lines. These are not caused by the tables.

### 4. AI and other contributions: accepted, changed, rejected

- Claude (claude.ai) explained the conflict, gave the four things to delete, and then checked my resolved file against `development`'s wording, which is how the problem was found.
- Accepted: abort and re-merge, and the three checks (markers, garbled characters, a phrase only `development` has).

### 5. Understood now, and still unresolved

Understood
- A merge conflict is two edits to the same spot. Resolving it means keeping the right parts of each.
- "The markers are gone" does not mean the file is right. Check for garbled characters, and for a phrase only the other branch has.
- Pull `development` into the branch before inserting tables, so the work starts from the corrected text.

Unresolved
- The stray glitches in the 23 file from `development` (listed above), which Evin may want fixed.


**Evidence**
- Reel folder in the Brutalist toolkit (`week8-merge-conflict`): `beat_sheet.json`
- Final video, 4K 16:9: https://drive.google.com/file/d/1OIxC8k6vanyyjZgVpVy19nnREnIl222S/view?usp=drive_link
- The merge commits in the textbook repository: https://github.com/Medhavy/medhavi-cancer
