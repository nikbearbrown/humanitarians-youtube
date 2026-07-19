# PEDAGOGY — number-hierarchy

**Topic**: Number Set Hierarchy (N ⊂ Z ⊂ Q ⊂ R ⊂ C)  
**Level**: College Algebra (prerequisite review)  
**Audience**: Students entering first-semester algebra or precalculus

## Learning objective

Students will be able to classify any given number into its smallest containing set (ℕ, ℤ, ℚ, ℝ, or ℂ) and explain why it belongs there, including verifying rational numbers as explicit p/q fractions.

## Pedagogical approach

**Conceptual scaffolding**: The reel builds the hierarchy left to right, mirroring the historical development (counting → negative → fractional → irrational → imaginary). This spatial metaphor ("nesting") makes the subset relationships concrete and memorable.

**Misconception addressed**: Students often think "real" means "actual/tangible" and misplace numbers like π or √2. By showing π explicitly as real-but-not-rational, the reel corrects this.

**CLI framing**: The Claude Code prompt → generated code → Manim output loop models the skill of using LLM tools to visualize abstract mathematical structures. Students see that even formal set theory can be rendered as code.

**Active task (B08)**: Classifying 5 self-chosen numbers and writing rationals explicitly as p/q requires recall and verification, not just recognition.

## GATE A compliance check

- All `.animate` calls: none used (FadeIn, GrowFromCenter, GrowArrow only)
- x positions: −4.8, −2.4, 0.0, 2.4, 4.8 — all within ±7.1 ✓
- y positions: title at 3.4, boxes at 0.4, subtitle at −1.4; rows at 2.1 to −2.3 — all within ±4.0 ✓
- B06 left-edge text at x=−5.2 — within ±7.1 ✓

VERDICT: PASS
