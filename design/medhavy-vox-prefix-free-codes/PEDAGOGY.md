# PEDAGOGY — medhavy-vox-prefix-free-codes

## What the learner already knows
Binary tree, bits, what encoding means

## What this reel teaches
A letter on an internal node of a binary tree means its code is a prefix of every code below it — causing ambiguity. Restricting all letters to leaf nodes eliminates this: leaves have no extensions, so each code terminates unambiguously. Average code length = sum(p_i × depth_i). Self-delimiting decoding: trace root to leaf, emit, restart.

## Key facts
- Internal node → code is prefix of all descendants → ambiguity ✓
- Leaf only → no extensions → unambiguous ✓
- Decode "0110111": A, C, D without lookahead ✓
- Example: A=60%, B=25%, C=10%, D=5%; lopsided tree averages 1.55 bits vs 2 bits balanced ✓
- Prefix-free = self-delimiting (no separator needed) ✓

## Exclusions honored
- No Huffman algorithm
- No Shannon entropy connection
- No alphabet-size generalization

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: concrete decoding trace; clean insight that leaf = no extensions = no ambiguity ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
