# PEDAGOGY — medhavy-vox-growth-rate-all-that-survives

## Learner Profile
Learner knows: algorithm runtime, basic polynomial functions

## Teaching Goals
Teaches:
- Big-O/Omega/Theta definitions and the sandwich bound
- T₁=n vs T₂=4n²+3n comparison at n=1000 and n=10^6
- 4× faster CPU running T₂ still 1000× slower than T₁ at n=1000
- Dividing by highest-order term: constants and lower-order terms vanish
- Growth shape is permanent — hardware can't reverse it

## Gate Numbers
- T₁(1000) = 1000, T₂(1000) ≈ 4M ✓
- 4× CPU on T₂: 1M, still 1000× slower ✓
- O/Omega/Theta sandwich ✓
- At n=10^6: T₁=10^6, T₂=4×10^12; 1000× CPU on T₂: still 4000× worse ✓

## Exclusions Honored
- No formal proof of dominance
- No little-o/little-omega
- No historical Big-O origin

## Color Semantics Check
- TEAL (growth shape / O(n) / Big-Theta / permanent verdict): correctly applied ✓
- CRIMSON (constants / lower-order terms / what gets absorbed): correctly applied ✓

## Beat Structure Check
- B00: MedhavyOpen with exact narration_text ✓
- B01–B10: 10 content beats with t_start and estimated_duration_s ✓
- B11: MedhavyOutro with exact narration_text ✓
- B03: CARD kind:question ✓
- B10: CARD kind:endcard ✓
- Graphic beats use ["#009E73"] or ["#009E73","#D55E00"] ✓

VERDICT: PASS
