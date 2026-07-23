# PEDAGOGY — domain-restrictions

**Topic**: Domain Restrictions — Vertical Asymptotes vs Removable Holes  
**Level**: College Algebra / Precalculus  
**Audience**: Students studying rational functions and domain/range

## Learning objective

Students will distinguish vertical asymptotes from removable discontinuities (holes) in rational functions by factoring, identify the domain restriction in each case, and correctly plot the open circle for a hole.

## Pedagogical approach

**Concrete comparison**: The reel uses two functions that share the restriction x ≠ 2 but for structurally different reasons. Placing them side by side in B06 makes the difference visible in the same frame, preventing the confusion of treating all "x ≠ k" restrictions as equivalent.

**The "hole that travels" metaphor**: The hook (B01) frames the hole as a permanent feature of the original function that cannot be erased by simplification. This is more accurate than the common shorthand "cancel and simplify" — simplification changes the formula, not the domain of the original.

**Step-by-step factoring (B06 right panel)**: Showing g(x) = (x²−4)/(x−2) = (x+2)(x−2)/(x−2) = x+2 for x≠2 in sequential steps models how students should work the simplification themselves.

**Open circle visualization**: The GrowFromCenter circle at (2, 4) makes the hole concrete. Students who have only seen open circles in textbook graphs often do not connect them to domain restrictions — this scene makes the connection explicit.

## GATE A compliance check

- All `.animate` calls: none used
- x positions: axes centered at 0; asymptote label at va_x + 0.8 ≈ 3.0; B06 panels at −3.0 and +3.0; divider at x=0 — within ±7.1 ✓
- y positions: title 3.4, axes center −0.3 (y_range −4 to 4 → ~5.5 height spans −3.05 to 2.45 on screen); domain text −3.3; B06 rows 1.7 to −1.05; hole −1.05 — within ±4.0 ✓

VERDICT: PASS
