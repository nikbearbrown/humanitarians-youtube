# PEDAGOGY — medhavy-vox-greedy-knapsack

## What the learner already knows
The knapsack problem, value/weight ratio, what greedy means

## What this reel teaches
Greedy knapsack by value/weight ratio achieves at least 50% of optimal on any input. The two-choice rule (take max of greedy packing and single best item) guarantees ≥50% always. If item size ≤ f×capacity, the guarantee rises to (1-f). DP knapsack is exact but O(n×W) — infeasible for large W.

## Key facts
- Worst case: A(502,501) vs B,C(500,500 each) at capacity 1000; greedy gets 502, optimal 1000 ✓
- Two-choice rule: max(greedy, best_single_item) ≥ 50% of OPT ✓
- 2×max(greedy, best_item) ≥ fractional_OPT ≥ OPT ✓
- Size cap f=0.1: guarantee ≥ 90% ✓
- Greedy: O(n log n); DP: O(n×W) — intractable for large W ✓

## Exclusions honored
- No fractional relaxation exchange-argument proof
- No dynamic-programming knapsack algorithm
- No (1-f) family formal proof

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: hook with "half the gold"; builds from worst-case example to provable guarantee; direct address ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
