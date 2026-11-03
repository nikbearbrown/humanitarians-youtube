# FACTCHECK — The Status Is A Claim

Status: **GATE F SIGNED — 2026-10-02. 16 rows PASS, 0 FAIL.**

Subject: `mycroft` @ `8c13b87` on `feature/market-sentiment-human-report`.
The branch head and `origin/feature/market-sentiment-human-report` are the same
commit, so this is the last *pushed* commit, which is what was asked for.

Every figure was recounted from the committed files, not from the commit
message. The recount script is in `SOURCES.md`.

| # | Beat | Claim | Verdict | How it was checked |
|---|---|---|---|---|
| 1 | B01 | 7 files changed, +177 / -12 | ✓ PASS | `git show --stat 8c13b87` |
| 2 | B01 | the attestation adds 125 lines; RUN_LOG adds 40 | ✓ PASS | same `--stat` |
| 3 | B01 | `status:` is still `RUNNABLE-SAMPLE` after the commit | ✓ PASS | `recipes/market-sentiment-analysis-part-1.md` line 2 |
| 4 | B04 | 17 rows in the Tested table | ✓ PASS | parsed the table, counted data rows — 17 |
| 5 | B04 | 7 of the 17 are break tests | ✓ PASS | rows containing `**Break test:**` — 7 |
| 6 | B04 | 18 of 18 catalogued defects detected at declared locators | ✓ PASS | the row reads **18/18**; split verified below |
| 7 | B04 | the split is 8 in step 3, 10 in step 4 | ✓ PASS | literal string `8 in step 3, 10 in step 4` |
| 8 | B04 | 0 of step 4's 10 leaked into step 3's output | ✓ PASS | the negative-check row |
| 9 | B05 | 10 entries under Did not test | ✓ PASS | counted top-level bullets — 10 |
| 10 | B05 | live execution has never run; step 2 hard-stops before any fetch | ✓ PASS | Did-not-test entry 1, and the gate-5 record's `actions_declined` (all `performed: false`) |
| 11 | B05 | the scoring weights carry no derivation, backtest or author | ✓ PASS | Did-not-test entry 2 |
| 12 | B05 | the wrong-entity class cost 782 purged rows | ✓ PASS | Did-not-test entry 3, citing `DATA_CONTRACT.md` |
| 13 | B06 | gate 5's four break-test cases, and which one must FAIL | ✓ PASS | the gate-5 break-test row, quoted verbatim |
| 14 | B07 | lifecycle is DRAFT → SPECIFIED → RUNNABLE-SAMPLE → RUNNABLE-LIVE → VERIFIED | ✓ PASS | `SNICKERDOODLE.md:51` |
| 15 | B07 | gate 5 is `decision: deny`, `approved_for_live_action: false` | ✓ PASS | read the JSON record directly |
| 16 | B08 | 9 defects broke during testing and were fixed; 2 were gates 4 and 5; gate 5 was fixed twice | ✓ PASS | counted bullets — 9; the gate-5 bullet says "Fixed twice" |

## The one thing on screen that is an editorial reading, not a figure

B08's spark line says **"Last week I called that gate fixed."** That is my
characterisation, and it is fair: episode 5 shipped on commit `4157a8e`, whose
subject is *"give gates 4 and 5 real failure paths"*, and this commit's
attestation records that gate 5 then still cleared on the mere existence of a
decision record. So the gate episode 5 presented as fixed was not yet correct.
It is labelled as a judgment in the narration ("which means"), not as a count.

## Precision notes

- **"17 rows" is rows, not assertions.** Several rows carry multiple
  observations. The reel says "rows", which is what was counted.
- **The 18/18 figure is defect *detection*, not correctness.** It says every
  catalogued defect was found where the manifest said it would be. It says
  nothing about defects not in the catalogue — which is why B05 exists.
- **"Never run" is scoped to this recipe.** Other parts of the repo are not in
  scope and the reel does not imply otherwise.
- **The 782 purged rows are historical**, from the incident
  `DATA_CONTRACT.md` records on 2026-08-26. The reel presents it as what the
  class has already cost, not as something this pipeline did.

## Claims deliberately NOT made

- **No claim that the recipe works.** The reel's verdict is the opposite: it is
  thoroughly tested in sample mode and unverified for live use.
- **No claim that the sentiment score is meaningful.** B05 says explicitly that
  nobody has checked.
- **No claim that the status *should* be VERIFIED, or that the denial was
  wrong.** Gate 5's refusal is treated as the correct outcome of a gate.
- **No performance, accuracy or business claim of any kind.**

## Repo hygiene

Nothing was written to `D:/Projects/mycroft`. All verification was reads:
`git show`, `git rev-parse`, and reading committed files. `git status` on the
subject repo was clean before and after.
