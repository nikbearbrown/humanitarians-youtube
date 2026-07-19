# FACTCHECK — vox-handoff-conditions

Source chapter: `claude-code-for-teachers/chapters/05-handoff-conditions.md`

## Claims verified

| Beat | Claim | Source | Status |
|---|---|---|---|
| B01-B02 | Teacher pushes About page; student reports syllabus link broken three days later | Chapter opening: "The teacher reviewed Claude's output... Three days later, a student emailed: the link to the syllabus from the About page does not work." | VERIFIED |
| B02 | Link used page-relative path; worked on local dev; failed on school server | Chapter: "The school server served pages from src/; the About page was at /about.html; the link should have been /syllabus.html. The page-relative link had been syllabus.html (no leading slash). On the teacher's local dev server, the relative path worked. On the school server with its outdated mod_rewrite, it did not." | VERIFIED |
| B04 | Three properties of a handoff condition: specific, testable, binary | Chapter: "Three properties make a handoff condition load-bearing. Specific... Testable... Binary..." | VERIFIED |
| B04 | "Looks good" fails all three | Chapter: "If the only verification is 'squint and feel okay,' the condition is a feeling, not a handoff condition." | VERIFIED (explicit in chapter) |
| B07 | Forward correction pollutes context | Chapter: "The session's context now contains the failed step, the failure observation, the attempted correction, and Claude's reasoning across all of them. The context is polluted." | VERIFIED |
| B07 | After two failed corrections: context is the problem | Chapter: "After two failed corrections on the same step, /clear the session entirely and rewrite the specification from scratch." | VERIFIED |
| B08 | /rewind removes failed step from both context and file system | Chapter: "Claude restores both the conversation context and the file changes to that point. The failed step is gone — from both Claude's memory and your file system." | VERIFIED |

## Terms table

| Term | Definition in film | Debut beat |
|---|---|---|
| handoff condition | specific, testable, binary condition before proceeding to next step | B04 |
| revert-and-respecify | /rewind then rewrite spec with failure as negative constraint | B08 |
| /rewind | Claude Code command to restore context and files to a checkpoint | B08 |

## Exclusions honored

- NO git diff walkthrough
- NO full deployment pipeline explanation
- NO CI/CD discussion
- NO formal five handoff-condition questions listed in full
- One mechanism: "looks good" fails the three tests; strong condition is specific/testable/binary.

## Status: VERIFIED
