# Fact check

| Claim | Basis / boundary |
|---|---|
| Leakage compromises held-out evaluation | scikit-learn common pitfalls; no claim that every high score is leakage. |
| Preprocessing must be fitted within training partitions | Same source; cross-validation documentation supports distinct tuning and final testing roles. |
| Split depends on intended use | scikit-learn cross-validation: time and group dependence matter. |
| Two of four versus four of four | Executable fictional example; a deliberately leaked lookup, not a real trained-model result. |

All examples are labeled fictional. No empirical performance statistic or real customer data is asserted.
