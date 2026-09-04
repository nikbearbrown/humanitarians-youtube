# FACTCHECK — "Claude, Halved."

| Claim (beat) | Verdict | Source / derivation |
|---|---|---|
| A monotonic yes/no predicate over a range can be binary-searched directly (B01/B02) | ✓ | Standard generalization of binary search ("binary search on the answer" / "binary search on value" in competitive-programming references) |
| Minimum ship capacity within D days solvable via `feasible(capacity)` + binary search (B03/B04) | ✓ | Canonical instance of this pattern (LeetCode 1011, "Capacity To Ship Packages Within D Days") |
| `feasible(capacity)` is monotonic — true for all capacities ≥ the true minimum, false below (B02-B04) | ✓ | Structural fact: any capacity greater than a working one is only easier to pack |
| A non-monotonic predicate gives binary search a wrong, confident-looking answer (B05) | ✓ | Correct — without monotonicity, `lo`/`hi` narrowing converges on an arbitrary point determined by comparison order, not a "true" boundary |

## Corrections applied

None needed.

## Numbers on screen

The worked-example weights (`[3,5,2,6,4,7]`) and the capacity-10 walkthrough
are a clearly illustrative toy instance, not a citation to a specific
dataset.
