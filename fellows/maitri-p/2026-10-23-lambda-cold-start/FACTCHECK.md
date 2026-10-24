# FACTCHECK — lambda-cold-start

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Lambda runs code in an execution environment: isolated, with code, dependencies and runtime | TRUE | AWS Lambda developer guide — execution environment lifecycle |
| 2 | Cold start: no ready environment → start runtime and run init code before the handler | TRUE | AWS — Init phase |
| 3 | Environments may be kept and reused (warm start); reuse not guaranteed | TRUE | AWS — execution environment reuse |
| 4 | Traffic growth needs more concurrent environments; new ones start cold | TRUE | AWS — Lambda scaling and concurrency |
| 5 | Concurrency ≈ requests per second × average duration | TRUE | AWS — "concurrency = average requests per second × average request duration" |
| 6 | 100 × 0.2 s = 20 | COMPUTED (asserted); illustrative numbers |
| 7 | Lighter init and provisioned concurrency reduce cold starts; provisioned concurrency is billed while configured | TRUE | AWS — provisioned concurrency pricing |
