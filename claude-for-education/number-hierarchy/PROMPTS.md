# PROMPTS — number-hierarchy

## B02 — Initial claude prompt (ASK)

```bash
claude "write a Manim scene showing the number set hierarchy: N ⊂ Z ⊂ Q ⊂ R ⊂ C as nested boxes with labeled examples of each set"
```

**Intent**: Generate a Manim scene with 5 rectangular boxes (ℕ, ℤ, ℚ, ℝ, ℂ) drawn left to right with set symbols, descriptive names, and example members. Arrows connecting adjacent sets to show the subset relation.

**Expected output file**: `number_sets.py`

---

## B05 — Revision claude prompt (CHANGE)

```bash
claude "add one example number in each set ring showing exactly which rings it belongs to: use 3, -2, 1/2, pi, and sqrt(-1)"
```

**Intent**: Add a second scene that places each of the five example numbers and shows its complete membership chain through the hierarchy. 3 appears in all five sets; √(−1) appears only in ℂ.

**Expected output file**: Updated `number_sets.py` or new `number_sets_v2.py` with `B06_NumberHierarchy2` class.
