# FACTCHECK: One Missing Character, One Failed Build (report video, week of 09-14-26)

Format: claim | verdict | source | fix. Written 09-14-26.
Verdicts: VERIFIED = matches my commit log. CONFIRM = from my build-error chat or memory; check before relying on it.

## Narration

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | The week's work was mapping figures into three chapters | VERIFIED | Commits 09-16-26 and 09-17-26: Chapters 11, 16, 19 | None |
| B00, B06 | One missing character broke the build | CONFIRM | Build-error chat; check that the before and after line differs by only the `>` | Run the check in the notes below |
| B01 | Images went into Chapters 16 and 19; a table and images into Chapter 11 | VERIFIED | "Mapping images to Chapter 16", "Mapping images to chapter 19 subsection", "Updating Chapter 11 by adding the table", "Uploading Chapter 11 image" | None |
| B01 | Then a build failed | CONFIRM | Build error reported on 09-17-26; exact order against the commits not checked | Confirm the order |
| B02 | Error text: "Unexpected end of file in name..." at line 76, column 727 of a Chapter 16 file | CONFIRM | Build-error chat; check against the saved build log if I still have it | Check the log |
| B03 | Line 76 is one very long figure caption, and the end of it shows `</p` without `>` | CONFIRM | Build-error chat | Run the check in the notes below |
| B04 | The fix is one character, committed as an update to the Chapter 16 file | CONFIRM | Commit "Update 6_Clinical_Implications_and_Therapeutic_Applications.mdx" (09-17-26); confirm that commit is the fix | Check the commit diff |
| B05 | How-to advice (ask Claude to print the characters around the column and check tags) | Advice, not a claim about my work | n/a | None |

## On screen

| Beat | Item | Verdict | Fix |
|---|---|---|---|
| B01 | Four commit messages shown as added lines | VERIFIED against my git log | None |
| B03, B04 | Before and after text of the end of line 76 | CONFIRM until I compare it with the file | Compare with the git show output |
| B00, B02, B05 | Composer shows model label "Fable 5 High" | Dates the video | Leave, or change to "Claude" |
| B00, B02, B05 | Folder chip shows @HumanitariansAI | Check in frame | Look at the intro frame |

## Not claimed anywhere
Whether the build passed after the fix, the duplicate Figure 16.6.2 label, and the CAJAL reports.

## Notes: how to run the checks
In the textbook repo, find the Sep 17 commit that touched the Chapter 16 file and compare line 76 before and after:
`git show <commit>^:<file> | sed -n 76p | cut -c690-800` and the same with `<commit>:<file>`.
