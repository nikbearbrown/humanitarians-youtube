# Week 29 work video: fact-check

Every number and claim the narration may use, read from `nikbearbrown/mycroft` `main` (the committed files, via `git show upstream/main`) by
`factcheck_numbers.py` in this folder. Result: **35 of 35 facts as expected.** Re-run it before Gate P and again before audio.

## Reproduction (verified)
Exporting `main` to a clean folder and running step 4 and step 6 with the clock pinned (`--now 2026-11-01T09:00:00Z`) produced files that are
**byte-identical** to the committed `quality-check.json`, agent log and report. So "clone it, run two commands, get both pages" is true.

## Numbers and claims (source: committed files in `mycroft`)
```
ok    agent log: number of fields                                                16
ok    report: number of sections                                                 15
ok    report: first section / last section                                       Run summary / Decision recommendation
ok    clean: records_seen in the log                                             12
ok    clean: report says 12 request(s) read                                      True
ok    clean: accepted at step 3                                                  True
ok    clean: stress-tested / stopped at the handoff                              True
ok    clean: reconciled on every step-4 check                                    11
ok    clean: handed off                                                          1
ok    clean: checks run on every result                                          14
ok    clean: failures / duplicates / rejects                                     (0, 0, 0)
ok    clean: advisory flags                                                      11
ok    clean: steps_completed in the log                                          [1, 3, 4, 5, 6]
ok    clean: gate decisions in the log (six gates + human clearance)             7
ok    clean: gate 5 reads                                                        NOT NEEDED (sample mode)
ok    clean: human clearance entry                                               none recorded
ok    clean: stop conditions evaluated / triggered                               (4, 0)
ok    clean: report's summary line on stop conditions                            True
ok    clean: condition 1 evidence says 41 files scanned, none found              True
ok    clean: typed TODOs in the log                                              3
ok    clean: recommendation lines                                                [('Approve for the next phase (sample mode only)', 'YES'), ('Request source or schema fixes', 'NO'), ('Block l
ok    clean: recipe frontmatter                                                  [('status', 'DRAFT'), ('todos_open', '3'), ('recipe_version', '0.3.1')]
ok    defective: records_seen / rejects in the log                               (10, 10)
ok    defective: d06 reject stage and reason                                     ('step 3', ['weights total 0.0: rescaling by a zero total gives NaN weights (gate addition)'])
ok    defective: report carries the same reason                                  True
ok    defective: recommendation lines                                            [('Approve for the next phase (sample mode only)', 'NO'), ('Request source or schema fixes', 'YES'), ('Block l
ok    defective: 'No request was accepted' in the report                         True
ok    self-test (steps 4 and 6): checks, all passed                              (30, True)
ok    self-test: deliberate breaks (caught) / refusals                           (12, 4)
ok    the earlier report showed sixteen steps (logged in the committed RUN_LOG)  True
ok    the stop-condition correction is logged                                    True
ok    the recipe's own stop condition 1 text                                     Stop if credentials, API keys, database destinations, email addresses, or tokens are hardcoded instead of read
ok    PR #82 state / merge commit                                                ('MERGED', '255ddf8')
ok    PR #81 state / merge commit                                                ('MERGED', '9684f46')
ok    PR #74 state / merge commit                                                ('MERGED', '5d60312')

35/35 facts as expected
```

## Wording rules for the narration
- Say "sixteen fields" (agent log) and "fifteen sections" (report); the report's first section is Run summary, its last Decision recommendation.
- Clean run: twelve requests read, twelve accepted, eleven stress-tested, one stopped at the hand-off; eleven reconciled on fourteen checks.
- Defective run: ten requests, ten rejects; use `d06-all-weights-zero` and its reason word for word.
- The correction: stop condition 1 was recorded as triggered although nothing was hardcoded (its test matched its own line); now each of the
  four is judged from evidence and the report says "Stop conditions: 0 of 4 triggered". Merged as #82 (`255ddf8`); #81 is `9684f46`; #74 is `5d60312`.
- Frame the correction as reading the page as its reader and a check now guarding it. Thirty checks, all passing.
- "None recorded" (human approvals) and status DRAFT, three TODOs open: closing beat only, as design, never as a gap.
- Avoid: minutes, meeting, what an AI is handed, refuse/fail-closed as a thesis, assertion-count theses, take-a-number-apart.
