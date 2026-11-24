# FACTCHECK — claude-liam-embeddings

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (numpy; deterministic). Toy 2-D vectors: cat (4,1), dog (3,2), car (1,4), cat×3 = (12,3).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02 | cat (4,1), dog (3,2), car (1,4) | PASS | definition | labelled "a toy plane", not a trained model |
| 2 | B03 | Distance cat–car = 4.243; cat–cat×3 = 8.246 | PASS | run | "four point two", "eight point two" |
| 3 | B03 | cat×3 = (12,3) is farther from cat than car is | PASS | 8.246 > 4.243 | — |
| 4 | B04 | Angles: cat 14.04°, dog 33.69°, car 75.96° | PASS | run | "fourteen, thirty-four, seventy-six" |
| 5 | B04 | cat–dog 19.65° (≈20°), cat–car 61.93° (≈62°), cat–cat×3 0° | PASS | run | — |
| 6 | B05 | cat·dog = 14; |cat| = 4.123, |dog| = 3.606; product 14.866 | PASS | run | "fourteen point nine" |
| 7 | B05 | cos(cat,dog) = 0.9417 ≈ 0.94 | PASS | run | — |
| 8 | B06 | cos(dog,car) = 0.7399 ≈ 0.74; cos(cat,car) = 0.4706 ≈ 0.47; cos(cat,cat×3) = 1.0000 | PASS | run | — |
| 9 | B07 | A zero vector has undefined cosine (0/0) | PASS | run: nan | — |
| 10 | B00, BVDT | Real embeddings are learned and have hundreds of dimensions | EXEMPT | not claimed; film uses 2-D toy vectors | stated as "toy plane" |
| 11 | BHTF | Distance ranks dog (1.41), car (4.24), cat×3 (8.25); cosine ranks cat×3 (1.00), dog (0.94), car (0.47) | PASS | run | — |
