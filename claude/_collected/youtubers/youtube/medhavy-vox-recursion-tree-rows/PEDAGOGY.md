# PEDAGOGY — medhavy-vox-recursion-tree-rows

## What the learner already knows
Recursion, merge sort, logarithm as repeated halving

## What this reel teaches
In merge sort's recursion tree, row j has 2^j pieces each of size n/2^j. The merge cost per piece is 6×(n/2^j), so total per row = 2^j × 6 × (n/2^j) = 6n — the 2^j factors cancel exactly. With log₂n rows, the total is 6n log₂n. Doubling n adds exactly one row.

## Key facts
- Row j: 2^j pieces × n/2^j size → 6n total cost per row ✓
- The 2^j numerator and denominator cancel exactly ✓
- Number of rows = log₂n ✓
- Total: 6n log₂n + 6n ✓
- Doubling n from 1024 to 2048: ratio ≈ 2.2× (not 4×) ✓

## Exclusions honored
- No proof that merge costs 6m (taken on faith)
- No non-power-of-two extension
- No sorting algorithm comparison

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: genuine curiosity about why doubling barely doubles work; builds from concrete n=8 example to general principle ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
