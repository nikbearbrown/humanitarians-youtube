# PEDAGOGY — discriminant-three-stories

**Topic**: The Discriminant as a Diagnostic Tool  
**Level**: College Algebra / Intermediate Algebra  
**Audience**: Students learning to solve quadratic equations

## Learning objective

Students will compute the discriminant before solving a quadratic equation, use its sign to predict the number and type of real roots, and connect this prediction to the geometry of the parabola.

## Pedagogical approach

**Diagnostic before computation**: The reel's core argument is that computing Δ = b²−4ac before applying the quadratic formula saves work. If Δ < 0, no real solution exists and the full formula is unnecessary. This is a genuine efficiency gain students can use immediately.

**Three parabolas simultaneously (B04)**: Showing all three cases in one frame allows direct comparison of what each discriminant value "looks like" geometrically. Students connect the algebra (sign of Δ) to the geometry (x-axis crossings) in one visual.

**Formula integration (B06)**: The quadratic formula is not abandoned — it is shown whole, with Δ highlighted as its most informative sub-expression. Students see that the discriminant is already inside the formula they already know.

**Verification practice (B08)**: Computing Δ first, predicting, then solving creates a self-checking loop. Students who consistently use this workflow will rarely be surprised by "no real solutions" during an exam.

## GATE A compliance check

- All `.animate` calls: none used
- x positions: three Axes at −4.5, 0.0, +4.5; each x_length=3.2 → spans ±1.6 from center → max x ≈ ±6.1 — within ±7.1 ✓
- y positions: title 3.4, Axes center 0.5 (y_length=3.0 → spans ±1.5 → 0.5±1.5 = −1.0 to 2.0 on screen), labels at −1.4 — within ±4.0 ✓
- B06: formula at 2.3, box at 1.3, arrow to 0.97→0.35, cases at 0.0, −0.7, −1.4 — all within ±4.0 ✓
- B06 x: case labels at −3.5, arrows −2.8 to −2.0, desc at −1.5 (left-aligned) — within ±7.1 ✓

VERDICT: PASS
