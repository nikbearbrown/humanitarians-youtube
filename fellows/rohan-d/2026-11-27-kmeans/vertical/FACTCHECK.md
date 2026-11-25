# FACTCHECK — claude-liam-kmeans

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (numpy; deterministic). Points: (1,1), (1.5,2), (3,4), (5,7), (3.5,5), (4.5,5), (3.5,4.5); k = 2; Lloyd's algorithm (assign to nearest, move to mean).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02, B03 | Start centers (1,1) and (5,6) | PASS | experiment | (5,6) chosen so (3,4) is not equidistant from the two centers |
| 2 | B03 | Point (3,4): distance 3.606 to (1,1), 2.828 to (5,6); joins the second | PASS | run | "three point six", "two point eight" |
| 3 | B03 | After assignment: 2 points in group 1, 5 in group 2 | PASS | run: labels [0,0,1,1,1,1,1] | — |
| 4 | B04 | Group 1 mean (1.25, 1.5); group 2 mean (3.9, 5.1) | PASS | run | — |
| 5 | B05 | A second assignment changes nothing: converged in 2 rounds | PASS | run | — |
| 6 | B06 | Inertia at the starting centers 19.25; after one update 8.525 | PASS | run | "eight point five three" |
| 7 | B06 | Inertia never increases under Lloyd's algorithm | PASS | standard (each step is a minimization) | — |
| 8 | B07 | Rectangle (0,0),(0,2),(4,0),(4,2): start (0,1),(4,1) is stable with inertia 4 | PASS | run | — |
| 9 | B07 | Start (2,0),(2,2) is stable with inertia 16 | PASS | run | — |
| 10 | B07 | Run from several starts and keep the lowest inertia | EXEMPT | standard practice (n_init) | stated as advice |
| 11 | B00 | K-means needs no labels | PASS | definition | — |
