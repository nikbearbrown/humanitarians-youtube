# PROMPTS — exponent-rules

## B02 — Initial claude prompt (ASK)

```bash
claude "write a Manim scene proving a^0=1 using the quotient rule: show a^3/a^3=a^(3-3)=a^0 and also =1, then animate all six exponent rules"
```

**Intent**: Generate a Manim scene that first proves a⁰ = 1 from the quotient rule in 4 steps, then lists all six exponent rules (product, quotient, power, zero, negative, fractional).

**Expected output file**: `exponent_rules.py`

---

## B05 — Revision claude prompt (CHANGE)

```bash
claude "add a worked example for each rule using base 2 with specific numbers"
```

**Intent**: Add a second scene displaying all six rules in a table with numerical verification using base 2: 2³·2²=32, 2⁵÷2²=8, (2³)²=64, 7⁰=1, 2⁻³=1/8, 8^(1/3)=2.

**Expected output file**: Updated `exponent_rules.py` with `B06_ExponentRules` class.
