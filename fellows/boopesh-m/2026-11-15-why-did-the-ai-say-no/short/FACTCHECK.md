# FACTCHECK — Why Did the AI Say No? (Short, 9:16)

Same sources and evidence as [../FACTCHECK.md](../FACTCHECK.md) ([RUN] = `../code/credit_reasons.py`, synthetic
applicants, seed 42; [REG B] = 12 CFR 1002.9, read verbatim from a GitHub mirror of the official eCFR bulk data).

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | results from my own experiment on synthetic applicants; two models deny A; 2 of 3 reasons shared | [RUN] | ✅ |
| B10 | US lending rules: a denial needs specific reasons; "the model said no" doesn't count | [REG B] (a)(2)(i), (b)(2) (quote on screen verbatim) | ✅ (paraphrase in narration) |
| B10 | made-up Applicant A: DTI 44 %, cards 72 %, 1 missed payment, 4 years, $52k; scorecard 53 %, black box 34 % vs a 30 % line (my choice) | [RUN] 53.2 % / 34.1 % | ✅ |
| B20 | scorecard top 3: debt-to-income, card use, missed payments (exact, 5 multiplications) | [RUN] | ✅ |
| B20 | black box: 16,000 model runs (Shapley, 32 × 500); top 3 missed payments, card use, credit history; 2 of 3 shared | [RUN] | ✅ |
| B30 | pay card balances down about $3,850 (72 % → 34 % of an assumed $10,000 limit) → both say yes (29.9 %, 28.7 %) | [RUN] | ✅ (limit assumed, labelled) |
| B30 | "that's a reason a person can act on" | editorial | opinion |
| B90 | "Rule: Regulation B · not legal advice" | [REG B] | ✅ |
