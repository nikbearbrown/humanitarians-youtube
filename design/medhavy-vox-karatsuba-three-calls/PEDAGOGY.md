# PEDAGOGY — medhavy-vox-karatsuba-three-calls

## What the learner already knows
Recursion, big-O notation, multiplication

## What this reel teaches
The running time exponent for divide-and-conquer algorithms equals log₂(number of recursive calls). Karatsuba saves one call via Gauss's identity, dropping the exponent from 2 to 1.585.

## Key facts
- T(n) = 4T(n/2) + O(n) → O(n²) ✓
- T(n) = 3T(n/2) + O(n) → O(n^log₂3) ≈ O(n^1.585) ✓
- Exponent = log₂(a) where a = recursive call count ✓
- (a+b)(c+d) - ac - bd = ad + bc: 3 multiplies recover 4 products ✓

## Exclusions honored
- No master method formal proof
- No Schönhage-Strassen algorithm
- No implementation details

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: recursive exponent from first principles ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
