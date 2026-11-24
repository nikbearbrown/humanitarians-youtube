# Week 32 MEASUREMENTS (our own simulation, 2026-11-23)

`experiment/stranded_energy.py` (python3.12 + numpy, seed 32, about 3 s), output `experiment/stranded_energy.json`.
Model: terminal voltage during a burst = Voc(q) - I * R(q); brownout = first burst under the 2.0 V reset line (our chosen, illustrative).
Curves Voc(q) and R(q) are graph readings ("about") from the Energizer and Duracell sheets (FACTCHECK rows 1-9); the plotted run ends near 208 mAh,
which is our reference capacity. Nothing here is a bench measurement of a real cell.

## Result: share of the cell unspent at the first brownout
| burst mA | brownout at mAh used | charge left % | energy left % |
|---:|---:|---:|---:|
| 2, 5, 8 | none before 208 | 0 | 0 |
| 10 | 205.0 | 1.4 | 1.3 |
| 15 | 197.7 | 5.0 | 4.5 |
| 20 | 190.5 | 8.4 | 7.8 |
| 30 | 173.6 | 16.5 | 15.5 |
| 40 | 154.6 | 25.7 | 24.5 |
| 50 | 134.1 | 35.5 | 34.3 |
| 60 | 108.3 | 47.9 | 46.8 |
| 75 | 19.2 | 90.8 | 90.3 |
| 100, 120 | at once | 100 | 100 |

Safe burst (the largest the cell can still pass) as the cell is used: 100 mA fresh, 69 at 25 mAh, 63 at 100, 43 at 150, 26 at 185, 14 at 200, 8.5 at 208 mAh.

## What it says
- The hypothesis holds, with a shape worth stating plainly: a small burst (8 mA or less) strands almost nothing; 30 mA strands about a sixth; 50 to 60 mA strands a third to a half; 100 mA strands all of it. The stranded share rises with the burst, and it rises steeply past about 60 mA.
- "Dies rich" is true for large bursts. For a burst near the datasheet's own 10 mA pulse rating it is about 1%. The film must not imply every coin-cell device wastes much; say who does.
- Energy left tracks charge left within about 1 point (the open-circuit curve is flat).

## Checks run
- **Two methods, same answer:** the grid answer and a burst-by-burst stepping run (0.1 s on, 4.9 s off, 0.005 mA sleep) agree to 0.009 mAh or better at 10, 20, 30, 50 and 75 mA.
- **Sensitivity (charge left %, at 8 / 30 / 100 mA):** reset 1.8 V: 0 / 10 / 94; 2.2 V: 3 / 26 / 100; 2.4 V: 8 / 42 / 100. Flat 2.87 V open-circuit curve: 0 / 17 / 100. Resistance x0.8: 0 / 10 / 93; x1.2: 1 / 23 / 100.
- **Drain-dependent resistance:** with Energizer's 3 uA curve (rises earlier, ends near 90 mAh) the 30 mA case strands about 40%, not 16.5%. The resistance curve depends on how the cell was drained; our main curve is for a 30 mA pulse run. The film says so.
- **Unit spread (assumption: resistance curve scaled by a lognormal, sigma 0.15, 400 draws):** left at 30 mA: 10.8 / 16.8 / 23.3% (10th / median / 90th); at 60 mA: 36 / 49 / 90%, a wide band because the curve is steep there.

## Limits to carry on screen
- Piecewise-linear curves from graph readings; the 75 mA step (fails at 19 mAh) comes from the 10 to 13 ohm rise read near 25 mAh and is not a smooth physical result.
- No temperature (cold raises resistance), no long-pulse polarisation, no capacitor (kept for the library film), no real cell tested.
- The reset line is a chosen parameter, not a cited chip value (FACTCHECK row 14).

## Open question for Tanmay
The title "The Cell Dies Rich" is accurate only for large bursts. Options: keep it and make the film's claim "how rich depends on the burst you ask for", or retitle to something that carries the dependence. Not decided.
