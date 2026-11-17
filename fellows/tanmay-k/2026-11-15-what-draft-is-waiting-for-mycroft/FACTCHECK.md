# Week 31 work video: fact-check (draft 1)

Every number and claim in `READ-ALOUD.md` (long) and `READ-ALOUD-SHORT.md` (Short), read from `nikbearbrown/mycroft` `main` @ `894be6c` (the committed files, through `git show upstream/main` and an export of `main`, read-only) by a read-only script (not included in this folder).
Result: **26 of 26 facts as expected.** It was re-run before Gate P and again before audio.

Verdicts: **VERIFIED** (read from a committed file or the repository's own command), **FRAMING** (the film's teaching move), **INFERRED** (a reading the film labels as one).

## Claim by claim
| # | Where | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | three of my last four films said, near the end, that the recipe was a draft | Week 27 B10, Week 28 B09, Week 30 B10; Week 29 does not | VERIFIED (our own beat sheets) |
| 2 | B01 | Mycroft is a public repository | `gh repo view` -> PUBLIC | VERIFIED |
| 3 | B01, B11 | pull request ninety is merged and adds two steps to one recipe | `gh pr view 90`: MERGED; step 4 and step 6 scripts among 50 added files | VERIFIED |
| 4 | B02 | five statuses, in this order | `SNICKERDOODLE.md` Recipe Lifecycle line | VERIFIED |
| 5 | B02 | a status is a claim; changing it without evidence is not climbing | `SNICKERDOODLE.md`: "The status is a claim"; "a violation, not a promotion" | VERIFIED |
| 6 | B03 | draft to specified needs zero open to-dos, each closure with its evidence | lifecycle table | VERIFIED |
| 7 | B03 | the stress-test recipe: six steps, six dated closing lines, zero open to-dos, status draft | recipe frontmatter and step blocks | VERIFIED |
| 8 | B04 | the next rung asks for a full sample run, checks that pass, audits generated and read | lifecycle table | VERIFIED |
| 9 | B04 | the contradiction detector is runnable on sample data, promoted on the fourth of October | frontmatter; RUN_LOG heading 2026-10-04 | VERIFIED |
| 10 | B04, S04 | six gate records, each naming the person who decided | `logs/gate-decisions/contradiction-detection-agent-gate-1..6.json`, `decided_by` | VERIFIED |
| 11 | B05, S04 | a record states what it covers (sample mode, invented data), the risk left over, and that any edit to the recipe voids it | gate record fields `scope`, `residual_risk`, `voids_if` | VERIFIED |
| 12 | B06, S05 | the records name version 0.2.0; the recipe is 0.2.1; one small edit since | records; frontmatter; `git log`: one commit after 2026-10-04 | VERIFIED |
| 13 | B07 | contradiction detector third rung; stress-test six of six; price fetcher five of six; what-if three; dashboard one | the repository's `snickerdoodle list` run on an export of `main` | VERIFIED-RUN |
| 14 | B08 | the self-test has twenty-four rows | `quality-report-self-test-results.json`: 24 checks, all as expected | VERIFIED |
| 15 | B08, S06 | the repository requires a "did not test" section | constitution: the Did not test section is mandatory | VERIFIED |
| 16 | B08, S06 | what I did not test: a live call, real market data, my three thresholds on a real portfolio, step two | the committed results' own "Did not test" section | VERIFIED |
| 17 | B08 | three thresholds | `quality-checked.json` parameters: 0.15, 3.0, one third | VERIFIED |
| 18 | B08, S06 | step two does not exist | no ingest script on `main` | VERIFIED |
| 19 | B09 | the pull request added files and edited none | `gh api` on the merge commit: 50 added, nothing else | VERIFIED |
| 20 | B09 | the price-fetcher recipe still says draft and its to-do markers still stand | frontmatter; `[TODO: DEV]` markers in the body | VERIFIED |
| 21 | B09 | the repository's check lists ten rows the recipe will need | `snickerdoodle check portfolio-price-fetcher`: 10 built-not-documented lines | VERIFIED-RUN |
| 24 | S01 | a recipe is a written-out piece of work for an agent and a person; the agent does the doing, a person the deciding | `recipes/README.md`; constitution P1 | VERIFIED |
| 25 | S03 | sample data is invented data | fixture note "Invented price ... Not market data"; gate record scope "frozen synthetic corpus" | VERIFIED (for our recipes' corpora) |
| 26 | B04 | a gate is a checkpoint where a named person decides | constitution P4: gates are hard stops cleared by a named human | VERIFIED |
| 22 | B10, S07 | the three questions | the film's own teaching move | FRAMING |
| 23 | B03, B07 | the stress-test recipe's next rung "looks within reach" | inference from the written test; no promotion record exists | INFERRED (the film says so) |

## Qualifications to keep in the wording
- **Do not say** the contradiction detector's status is verified for its current version. The film says only that its records name 0.2.0 and the recipe is 0.2.1 (item 12).
- **Say "one small edit"**, with no author and no judgment (the edit changed the recipe's command table and version).
- **Week 25 ground:** the contradiction recipe was Week 25's subject (porting, rounding, the declined live mode). This film uses only the status, the records' scope and the version.
- **Our five recipes only:** no other fellow's recipe or status appears.
