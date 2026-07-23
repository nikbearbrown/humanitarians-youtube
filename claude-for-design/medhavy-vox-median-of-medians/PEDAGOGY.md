# PEDAGOGY — medhavy-vox-median-of-medians

## What the learner already knows
What it means to find the kth-smallest element, what a pivot does in quicksort

## What this reel teaches
Median-of-medians guarantees a pivot between the 30th and 70th percentile by grouping into 5s, sorting each group, and finding the median of medians. This ensures the larger recursive call is at most 7n/10 elements. The recurrence T(n) ≤ O(n) + T(n/5) + T(7n/10) converges to O(n) because 1/5 + 7/10 = 9/10 < 1.

## Key facts
- Groups of 5 sorted → medians extracted → median of medians = pivot ✓
- Pivot guaranteed between 30th and 70th percentile ✓
- Larger sub-call: at most 7n/10 elements ✓
- Recurrence: T(n) ≤ cn + T(n/5) + T(7n/10); 9/10 < 1 → O(n) ✓
- 20-element example: max 14 (70%) on either side ✓

## Exclusions honored
- No recurrence solution proof (stated as consequence)
- No comparison with randomized rselect
- No additive-error details

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: genuine curiosity about two recursive calls still being O(n); builds from steps to guarantee to recurrence ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
