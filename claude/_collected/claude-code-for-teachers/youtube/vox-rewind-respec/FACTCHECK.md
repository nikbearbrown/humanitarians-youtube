# FACTCHECK — vox-rewind-respec

Source chapter: `claude-code-for-teachers/chapters/05-handoff-conditions.md`

## Claims verified

| Beat | Claim | Source | Status |
|---|---|---|---|
| B01-B02 | About page link to syllabus 404s; page-relative path worked on local dev, failed on school server | Chapter opening: "The link path was correct relative to the project root — and wrong relative to where the page was being served. The school server served pages from src/; ...The page-relative link had been syllabus.html (no leading slash). On the teacher's local dev server, the relative path worked. On the school server with its outdated mod_rewrite, it did not." | VERIFIED |
| B04 | Forward correction pollutes context | Chapter: "The session's context now contains the failed step, the failure observation, the attempted correction, and Claude's reasoning across all of them. The context is polluted — the next prompt operates against the failure history as if the failure is part of the desired result." | VERIFIED (paraphrase) |
| B05 | /rewind restores both conversation and file system to checkpoint | Chapter: "/rewind. Select the checkpoint before the failed step. Claude restores both the conversation context and the file changes to that point. The failed step is gone — from both Claude's memory and your file system." | VERIFIED (verbatim) |
| B06 | Respecification adds failure mode as explicit negative constraint | Chapter: "Respecify. Rewrite the original specification with the failure mode as an explicit negative constraint...All link paths in the new page must use absolute server-relative paths (leading /); never use page-relative paths that depend on the page's own location." | VERIFIED |
| B07 | Two-failure rule: after two failed corrections, /clear and rewrite from scratch | Chapter: "After two failed corrections on the same step, /clear the session entirely and rewrite the specification from scratch with the failures named as constraints. Two failures is the signal that the context is polluted beyond what /rewind alone can clean." | VERIFIED (verbatim) |
| B08 | Cost comparison: "15-minute bug into a 90-minute one" | Chapter: "The compounding from polluted context is what most often turns a 15-minute bug into a 90-minute one." | VERIFIED (verbatim) |

## Terms table

| Term | Definition in film | Debut beat |
|---|---|---|
| forward correction | asking Claude to fix its own failed output; pollutes context with failure history | B04 |
| context pollution | failure history in session treated as constraint by subsequent prompts | B04 |
| /rewind | restores conversation and file system to checkpoint before the failed step | B05 |
| respecification | rewriting the original spec with the failure mode as an explicit negative constraint | B06 |
| two-failure rule | after two failed corrections on same step, /clear and rewrite from scratch | B07 |

## Exclusions honored

- NO git revert comparison
- NO /clear versus /rewind distinction in depth
- NO context-window token math
- NO formal discussion of context pollution beyond the intuition
- One mechanism only: forward correction pollutes context; /rewind + respecification executes cleanly.

## Status: VERIFIED
