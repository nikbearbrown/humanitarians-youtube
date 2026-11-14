# Every Group Went The Other Way

**Track:** educational (STEM / AI) · **Week ending:** 2026-11-13

> Add the groups together and you can get the opposite. Not a rounding error
> and not a trick — a total and every single group inside it can point in
> different directions, and every one of those numbers is correct.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:30. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

This one runs on **published outside data**, not a simulation written for the
episode: the six largest departments of the UC Berkeley 1973 graduate
admissions round (Bickel, Hammel & O'Connell, *Science* 187(4175), 1975 — the
table distributed as `UCBAdmissions` in R).

Across those six departments, men were admitted at **44.5%** and women at
**30.4%**. A 14-point gap.

Split it by department:

| Dept | Men | Women | Leads |
|---|---|---|---|
| A | 62.1% | **82.4%** | women |
| B | 63.0% | **68.0%** | women |
| C | **36.9%** | 34.1% | men |
| D | 33.1% | **34.9%** | women |
| E | **27.7%** | 23.9% | men |
| F | 5.9% | **7.0%** | women |

Women were admitted at the higher rate in **four of the six**. Both readings
are arithmetically correct.

**Why.** Two things the total cannot show. First, the departments are nothing
alike — A admitted 64.4% of everyone who applied, F admitted 6.4%, about ten
times harder. Second, the two groups did not apply to the same places: A and B
took **51%** of men's applications and **7%** of women's, while 72% of women's
applications went to C, E or F.

**The test that settles the mechanism.** Hold every department's decisions
exactly as they were, and give women the men's application pattern. Their rate
goes from 30.4% to **51.6%** — above the men's 44.5%. A 14-point deficit
becomes a 7-point surplus, and not one admissions decision changed.

## What this reel does not conclude

It does not say the data shows there was no bias. The landing beat argues the
opposite of the comfortable reading: the aggregate asked whether admissions
committees were biased, the departments answered that question, and the
question then **moved upstream** — to why women were applying to the most
crowded and least funded departments in the first place. That is where the
original authors pointed too.

Disaggregating relocated the problem. It did not dissolve it.

## Reproduce it

```bash
python simpson_evidence.py
```

`numpy` only, seconds to run. It prints the department table, the aggregate,
the selectivity and application shares, and the standardisation — plus a
seeded synthetic check (not shown in the reel) establishing that a reversal
requires a confounder correlated with both the grouping and the outcome. With
the groups routed identically, the total essentially never contradicts every
stratum.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Two correct numbers that disagree |
| B01 | BLUF | `BrutalistHesitantWriter` | types **answer**, deletes it, types **opposite** |
| B02 | SETUP | `PairedBars` | Six rows marked WOMEN ×4 · the rule · the total marked MEN |
| B03 | BODY | `ClaudeBarChart` | Selectivity, 64.4% down to 6.4% |
| B04 | BODY | `CardSet` | Where the applications went: 51% against 7% |
| B05 | BODY | `ClaudeBarChart` | 30.4 → 51.6 standardised, passing men's 44.5 |
| B06 | LAND | `StageRail` | The question moved upstream |
| B07 | HANDOFF | `ClaudeComposerAsk` | Run it on a number you actually report |
| B08 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

`PairedBars` and `PairedBars916` — two series across N categories with the
aggregate set apart behind a rule. GATE L found nothing reusable:
`ClaudeBarChart` plots one series, and the only genuine grouped chart in the
library is hardcoded to another reel. Logged in `TEMPLATE-MISSES.md`.

The separation is the design: drawing the total as just another row would
quietly assert that it *is* one of them, which is the exact misconception the
reel dismantles.

## Honesty notes

- **The data is real and external.** Counts transcribed from the published
  table; every rate computed from those counts, so no percentage can drift
  from its source.
- **No sentence of the paper is quoted on screen.** Its conclusion is
  paraphrased and attributed. The full text could not be retrieved to verify
  wording, and an approximate quotation is worse than an honest paraphrase.
- **B00 was rescoped during the build.** It originally opened on the famous
  full-pool figures (~44% men, ~35% women) while every other beat analyses the
  six-department subset. Both are correct and they are different populations —
  but a reel about misread aggregates should not put two different aggregates
  in front of a viewer. It now speaks about one population throughout, and the
  total row is labelled "All six", not "overall".
- **An invented figure was caught in card prose.** B04 read "74%" where the
  data says 72.3%. The pass that rewrites numeric props from the JSON reported
  everything matching — correctly, because that number lived inside a sentence.
  Figures in prose need a separate read against the source.
- **The simulation's numbers are deliberately absent from the reel.** They are
  synthetic; placed beside real data they invite being read as part of it. The
  reel states only the qualitative fact they establish.
- **Scope.** Six departments, one university, one year, used to demonstrate a
  general arithmetic phenomenon — not to characterise admissions anywhere else.

Full ledger in `FACTCHECK.md`, method and sourcing in `SOURCES.md`, build
record in `FRICTIONAL.md`.
