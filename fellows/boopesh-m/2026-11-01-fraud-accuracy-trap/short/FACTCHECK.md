# FACTCHECK — The 99.9% Accuracy Trap (Short, 9:16)

Same sources and evidence as [../FACTCHECK.md](../FACTCHECK.md) ([KAGGLE-DESC] / [IEEE] / [RUN]).

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | 492 frauds in 284,807 card transactions | [KAGGLE-DESC] (verbatim copy; kaggle.com blocked) | ✅ |
| B00 | results from my own experiment on synthetic data | [RUN] | ✅ |
| B10 | about 1 in 580; "almost two hundred eighty-five thousand" | 284,807 / 492 = 578.9 | ✅ |
| B10 | ULB + Worldline (kicker) | [KAGGLE-DESC] | ✅ |
| B20 | synthetic data with the real fraud rate; always-legit model 99.8 % accurate, 0 of 148 caught | [RUN] 0.99827, 0/148 | ✅ |
| B20 | small boosted model 99.9 % accurate, catches 127 of 148 | [RUN] 0.99896, 127/148 (68 false alarms, not spoken) | ✅ |
| B30 | "for rare events, check recall, precision and what each mistake costs" | editorial takeaway | opinion |
| B30 | "synthetic data · real systems use far more signals" | honest limit | opinion |
