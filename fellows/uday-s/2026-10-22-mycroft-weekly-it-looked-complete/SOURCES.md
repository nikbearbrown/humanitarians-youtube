# SOURCES - It Looked Complete

Single-source reel. Everything comes from the `mycroft` repository at `93485c4`
on `feat/gate-records`. No web sources.

| On screen | Beat | Where it came from |
|---|---|---|
| the five absent fields | B01 | commit body of `93485c4`, confirmed against the diff |
| residual_risk present but generic | B01 | commit body |
| gate 3's test, verbatim | B05 | `git show 93485c4:recipes/market-sentiment-analysis-part-1.md` line 65 |
| the two directory paths the test names | B04, B05 | the same line |
| 26 JSON files | B04 | `git ls-tree -r 93485c4` over the two trees - 14 + 12 |
| depth-1 stop missed them | B04 | the same listing: 3 and 1 top-level entries, JSON two levels down |
| gate 4's loop values, gate 6's [DATE] | B06 | commit body |
| residual_risk_stated / run_log / mode / scope | B07 | commit body and the committed source |
| +147 -3 | B07 | `git show --stat 93485c4` |
| the UTC date bug | B08 | commit body, reconstructed from the commit's own timestamp |
| six distinct evidence sets, four refusals, run/check/verify unaffected | B09 | commit body - the commit's own verification |

## The one command that was deliberately not run

Last episode's evidence came from **running** the committed checker, because
`check` only reads and prints. That was the strongest evidence available and it
was safe.

`gate` is different: **it writes a decision record into the repository.** Running
it to confirm a count would have left a file in someone's repo for the sake of a
video. So this week's figures come from counting the tree instead, and the one
figure that could only be obtained by running the writer - the "32 evidence
files" - is recorded in FACTCHECK.md and appears in no frame.

## How the date bug was confirmed rather than quoted

The commit says a decision made on 22 October was recorded as the 23rd. That is
checkable from the commit itself:

```
git show --format=%ad 93485c4
  Thu Oct 22 22:28:21 2026 -0400
```

22:28 at UTC-4 is 02:28 on the 23rd in UTC. A date field formatted with
`toISOString()` would print `2026-10-23`. The offset reproduces exactly, so the
bug is confirmed rather than taken on trust.

## Claims NOT sourced here, and therefore not made

- Nothing about whether any gate decision was correct - only about what the
  record carries.
- Nothing about recipes other than market-sentiment, which is the one whose
  gate tests are quoted.
- No comparison to any other repository or audit format.
