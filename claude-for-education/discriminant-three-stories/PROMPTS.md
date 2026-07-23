# PROMPTS — discriminant-three-stories

## B02 — Initial claude prompt (ASK)

```bash
claude "write a Manim scene showing three parabolas side by side: one with discriminant>0 (2 roots), one with discriminant=0 (1 root), one with discriminant<0 (0 real roots), and show the discriminant value below each"
```

**Intent**: Generate a Manim scene with three mini Axes objects side by side. Left (x²−3x+2, D=1, CRIMSON): crosses x-axis twice. Center ((x−1)², D=0, INK): touches x-axis at one point. Right (x²+x+1, D=−3, SLATE): does not touch x-axis. Label below each shows "D > 0 / 2 real roots" etc.

**Expected output file**: `discriminant_plots.py`

---

## B05 — Revision claude prompt (CHANGE)

```bash
claude "add the quadratic formula with the discriminant highlighted and arrow pointing to each case"
```

**Intent**: Add a second scene showing the full quadratic formula at top, with the b²−4ac part in a GOLD highlight box labeled "Δ (the Discriminant)" in CRIMSON. An arrow points down to a list of three cases: Δ>0 (two distinct real roots), Δ=0 (one repeated real root), Δ<0 (no real roots, complex).

**Expected output file**: Updated `discriminant_plots.py` with `B06_DiscriminantFormula` class.
