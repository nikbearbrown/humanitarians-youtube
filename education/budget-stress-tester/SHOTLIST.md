# SHOTLIST — budget-stress-tester

## Rhythm histogram
| Type | Beats | % |
|---|---|---|
| SLATE | B00, B01, B07, B08 | 4/10 = 40% |
| REMOTION | B02, B03, B05, B09 | 4/10 = 40% |
| MANIM | B04, B06 | 2/10 = 20% |

## Act map
| Act | Beat |
|---|---|
| INTRO | B00 SLATE |
| PROBLEM | B01 SLATE |
| ASK (TerminalAsk) | B02 |
| CODE (CodeBlock) | B03 |
| OUTPUT | B04 MANIM — B04_BudgetChart |
| CHANGE (TerminalAsk) | B05 |
| OUTPUT | B06 MANIM — B06_RaiseScenario |
| SUMMARY | B07 SLATE |
| NEXT | B08 SLATE |
| OUTRO (NikBearBrownOutro) | B09 |

## Open slots
B04 and B06 are MANIM scenes rendered by vox_run.sh via vox_scenes.py.
All SLATE beats are text-slate cards filled by vox_fill_slates.py.
