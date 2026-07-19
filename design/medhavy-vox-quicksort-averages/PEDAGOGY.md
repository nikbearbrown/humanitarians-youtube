# PEDAGOGY — medhavy-vox-quicksort-averages

## What the learner already knows
Quicksort (what it does), the idea of expected value, integration as area

## What this reel teaches
Each pair of elements in quicksort is compared with probability 2/(window size), which decreases for distant pairs. Summing these probabilities yields a harmonic series bounded by the integral of 1/x = ln n, giving 2n ln n total average comparisons — O(n log n) proven by direct probability counting.

## Key facts
- Pair (i,j) compared with probability 2/(j-i+1) ✓
- Adjacent pairs: probability 1; distant pairs: small probability ✓
- Per-element harmonic sum ≈ 2 ln n ✓
- H_n ≤ ln n + 1 (rectangles fit under y=1/x curve) ✓
- Total: 2n ln n ≈ 2.88 n log₂ n average comparisons ✓

## Exclusions honored
- No indicator-variable derivation (taken on faith)
- No worst-case analysis
- No in-place sorting detail

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: scale-building from probability to harmonic sum to integral; genuine curiosity about why it's so much better than n² ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
