# SOURCES — The Status Is A Claim

Single-source reel: everything comes from the `mycroft` repository at commit
`8c13b87`, on `feature/market-sentiment-human-report`. No web sources.

`8c13b87` is both the branch head and `origin/feature/market-sentiment-human-report`,
confirmed with `git rev-parse` on each — so it is the last pushed commit.

| On screen | Beat | File in the repo |
|---|---|---|
| 7 files, +177 / -12 | B01 | `git show --stat 8c13b87` |
| attestation 125 lines, RUN_LOG 40 lines | B01 | same |
| `status: RUNNABLE-SAMPLE` | B01, B07 | `recipes/market-sentiment-analysis-part-1.md:2` |
| 17 rows / 7 break tests | B04 | `logs/attestations/market-sentiment-analysis-part-1-v0.2.0.md` - Tested |
| 18/18 defects, 8 in step 3 + 10 in step 4 | B04 | same, defect-coverage row |
| 0 leaks between steps | B04 | same, negative-check row |
| 10 Did-not-test entries | B05 | same - Did not test |
| 782 purged rows | B05 | same, citing `DATA_CONTRACT.md` |
| gate 5's four break-test cases | B06 | same, gate-5 break-test row |
| the five-stage lifecycle | B07 | `SNICKERDOODLE.md:51` |
| `decision: deny` / `approved_for_live_action: false` | B07 | `logs/gate-decisions/market-sentiment-analysis-part-1-gate-5.json` |
| 9 defects fixed during testing | B08 | attestation - Broke during testing, fixed |
| the five steps to VERIFIED | B09 | attestation - What VERIFIED would require, in order |

## The recount

Counts were not taken from the commit message. The message claims 17 / 7 / 10 / 9;
each was independently recounted by parsing the committed file:

```python
t = section('Tested', '### Did not test')
rows = [l for l in t.splitlines() if l.startswith('|') and not re.match(r'^\|\s*-+', l)]
# 17 data rows; 7 contain '**Break test:**'
```

All four counts matched the message. Had they not, the file would have won:
P6 of the constitution puts truth in the artifact, not the description.

## Why no second source

This is a weekly work report on one commit. A second source would not make the
count of rows in a table more true. What *is* independently sourced is the
lifecycle rule (`SNICKERDOODLE.md`) and the gate decision (its own JSON record),
because those are the two things the episode's verdict rests on — the reel does
not take the attestation's word for either.

## Claims NOT sourced here, and therefore not made

- Nothing about whether the market-sentiment numbers are any good.
- Nothing about live behaviour, because nothing live has ever run.
- No comparison to any other repository, tool or workflow.
