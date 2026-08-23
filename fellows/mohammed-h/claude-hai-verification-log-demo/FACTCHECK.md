# FACTCHECK.md — claude-hai-verification-log-demo

Wrapper build: body beats (B01–B08) are inherited verbatim from
`../verification-log-demo/beat_sheet.json`. This file audits only what that
inheritance surfaces; it does not re-derive the body's own numbers from
scratch (that's the canonical reel's job).

## Flagged: B06 narration is internally inconsistent with the B05 flag rule

**Claim (B06):** "The primary source shows a Sharpe of 1.52. Two of three
model responses are flagged: one is 9% below primary, one is 7% above."

**The rule that produces the flag (B05's own prompt):** "Flag rows where
model value deviates from primary by more than 10%."

**Check:** with primary = 1.52 and model runs 1.38 / 1.41 / 1.62:

| run | value | deviation from 1.52 |
|---|---|---|
| Run 1 | 1.38 | −9.2% |
| Run 2 | 1.41 | −7.2% |
| Run 3 | 1.62 | +6.6% |

All three deviations are under the stated 10% threshold — under the rule
the script itself sets, **none** of the three rows would flag, not two.
The 9%/7% figures in the narration look like they were meant to illustrate
"close but not identical," but "flagged" is the wrong word given the >10%
rule stated one beat earlier.

**Verdict:** QUALIFY — not a fabricated number, but an inconsistent label.
**Proposed fix (for the canonical reel, not applied here):** either (a)
change "flagged" to something like "off by," since none actually cross the
stated line, or (b) tighten the flag rule (e.g. >5%) if the intent was for
two rows to genuinely flag. Left unresolved in this wrapper per policy —
the body is locked and inherited, not rewritten.

## Everything else

All other figures in the inherited body (1.38, 1.41, 1.62 as the three
model Sharpes; 0.24 as their spread; the >10% absolute-difference flag rule
in the B02/B03 script) are internally consistent and are carried through
unchanged in this wrapper's B00 cold-open recap.
