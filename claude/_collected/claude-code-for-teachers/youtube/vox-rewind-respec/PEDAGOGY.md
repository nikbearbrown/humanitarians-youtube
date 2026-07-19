# PEDAGOGY — vox-rewind-respec
## Why Rewriting the Wrong Fix Makes the Build Worse, Not Better

## One-mechanism rule
This film teaches exactly one mechanism: forward correction after a failed build step adds failure history to the session context, and Claude reasons against that history as if it is constraint — producing variations on what failed rather than clean solutions; /rewind removes the failure from both conversation and file system, and a respecification that includes the failure mode as an explicit negative constraint executes cleanly.

## Audience
Teachers who use Claude Code to build classroom tools. They have experienced iterating on a failing build step only to make things worse. They may not have identified context pollution as the mechanism. They do not need to understand token math — only that the session's "memory" of failures gets in the way.

## Learning outcome
After watching, the viewer should be able to: (1) recognize that forward correction accumulates context pollution, (2) know to use /rewind to restore a clean state, and (3) add the failure mode as an explicit negative constraint in the respecification.

## Beat-by-beat check

| Beat | Pedagogical function | Passes? |
|---|---|---|
| B01 | Cold open: hook in the result (two fixes, build worse) — creates curiosity | PASS |
| B02 | Concrete failure: the session log makes the compounding visible | PASS |
| B03 | Question card: "Two fixes. Worse than the original failure. Why?" | PASS |
| B04 | Mechanism: failure history as constraint — explains WHY forward correction fails | PASS |
| B05 | Resolution: /rewind split diagram shows what "clean state" means | PASS |
| B06 | Detail: respecification — the handwritten amendment makes it concrete | PASS |
| B07 | Two-failure rule: gives the viewer a clear decision rule | PASS |
| B08 | Cost comparison: makes the time savings quantitative and memorable | PASS |
| B09 | Endcard: three-line summary crystallizes the three-step discipline | PASS |

## Exclusion compliance
- NO git revert comparison
- NO /clear versus /rewind distinction in depth
- NO context-window token math
- NO formal discussion of context pollution beyond the intuition
- One mechanism only: forward correction pollutes; /rewind + respecification resolves

## Accuracy
- All factual claims sourced from chapter 5; see FACTCHECK.md
- "15-minute bug into a 90-minute one" quoted verbatim from chapter
- /rewind restoration of conversation + file system sourced verbatim from chapter
- Two-failure rule sourced verbatim from chapter

VERDICT: PASS
