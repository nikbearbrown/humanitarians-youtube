# Week 27: match-rate results (angle D)

Script: `compute_match_rates.py` (seed 2701, 400,000 simulated groups per cell). Output: `match-rates.json`.
Exact values come from a closed-form DP over the real day probabilities. Simulation and exact agree to about 0.1 point in every cell, so the simulation is trustworthy.

## Uniform model (every day equally likely, 365 days)

| People | P(at least one shared birthday) |
|---|---|
| 10 | 11.7% |
| 23 | **50.7%** |
| 30 | 70.6% |
| 40 | 89.1% |
| 50 | 97.0% |
| 57 | 99.0% |
| 70 | 99.9% |

"Someone shares *my* birthday": 50% needs **253** people. With 23 people (22 others), it is only **5.9%**.

## Real US calendars (births pooled by calendar day)

| Calendar | 23 people | 30 | 50 | People for 50% |
|---|---|---|---|---|
| NCHS 1994–2003 (with Feb 29) | 50.79% | 70.69% | 97.05% | 23 |
| NCHS 1994–2003 (no Feb 29) | 50.83% | 70.73% | 97.07% | 23 |
| SSA 2000–2014 (with Feb 29) | 50.79% | 70.70% | 97.06% | 23 |
| SSA 2000–2014 (no Feb 29) | 50.84% | 70.74% | 97.07% | 23 |

Busiest day is about 12% above the mean daily share. Feb 29 runs at about 21–25% of a normal day.

## What this means for the film

- The model's assumption (uniform days) is false, and the real calendar *does* push the match chance up, as theory says it must. But by only **about 0.1 point at 23 people**. The honest finding is robustness: a wrong assumption barely moves the answer here.
- This is the "which way the mess pushes, and by how much" teachable move. It also means the film cannot promise a dramatic gap between model and reality. The surprise is that there isn't one, so the open question can be "what would make the real world differ much more?" (strongly clustered groups, for example), which we would need to compute before claiming.
- Not yet tested: groups that are not random draws from the national population (for example one school year, where birth dates cluster). Any such claim needs its own computation before it enters narration.

## Sources and licences (for FACTCHECK)

- Data: US federal births-by-day counts, NCHS (1994–2003) and SSA (2000–2014), as redistributed in the `fivethirtyeight/data` repo, `births/` folder. The repo's top-level `LICENSE` is CC BY 4.0. The `births/` README states no separate terms, and the underlying numbers are US government statistics. Credit in the video description: "Births data: US NCHS and SSA via FiveThirtyEight (CC BY 4.0)".
- Everything else (simulation, closed-form probabilities) is our own work. No third-party text, images, rosters or named individuals. No political content.
- Files kept locally in `data/`. The CSVs are public sources; whether they go in the pushed folder follows the README rule (text and code only), so link them instead of copying.

## Clustered groups (`cluster_rates.py`, exact, SSA 2000–2014, Feb 29 dropped)

Group of 23, everyone born inside one W-day window of the calendar. Mean over all 365 window starts:

| Window W | P(shared birthday), real weights | Uniform within window | People for 50% |
|---|---|---|---|
| 365 days (a full school-year cohort) | 50.84% | 50.73% | 23 |
| 180 days | 77.05% | 76.96% | n/a (not computed) |
| 90 days | 95.44% | 95.40% | 12 |
| 60 days | 99.24% | 99.23% | 10 |
| 30 days (born in the same month) | above 99.99% | about 100% | 7 |
| 14 days | 100% (certain; 23 > 14 days) | | 5 |
| 7 days | 100% (certain; 23 > 7 days) | | 4 |

Spread over start dates is under 0.1 point at every width, so *which* window barely matters.

### Findings

- **What moves the answer is how many distinct days the group can occupy, not seasonality.** Real weights inside a window add about 0.1 point over a uniform window of the same width.
- **A school-year cohort does not cluster the calendar.** A cohort with a cutoff date spans every month-day once, so it behaves like the full calendar (about 50.8%). Matching on full date including year would be a different, much weaker question.
- **A same-month or same-quarter group is where reality departs sharply.** 23 people born in the same month will almost certainly include a shared day. Half a group of 7 is enough.
- Caveat: "born in a W-day window" groups are a modelling device. Real groups with that property exist (age-banded programmes, for example) but we have not sourced any, and the film should present this as a calculation, not as a claim about a named real group.

Implication for angle D: the three trials become (1) the uniform model, (2) the real national calendar (tiny difference, the model survives), (3) narrow windows (the model breaks, and the breaking variable is days available, not seasonality). That keeps the "which way and how much" move, with a real contrast to land on.
