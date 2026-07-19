# PROMPTS — pemdas-ambiguity

## B02 — Initial claude prompt (ASK)

```bash
claude "write a Manim scene showing two interpretations of 8÷2(2+2): one where implicit multiplication binds tighter than division (answer=1) and one where left-to-right division applies first (answer=16)"
```

**Intent**: Generate a Manim scene with two evaluation columns side by side, each showing the step-by-step evaluation of 8÷2(2+2) under a different precedence convention.

**Expected output file**: `pemdas_debug.py`

---

## B05 — Revision claude prompt (CHANGE)

```bash
claude "add the fix: rewrite the expression unambiguously as both (8÷2)(2+2) and 8÷(2(2+2)) and show which answer each gives"
```

**Intent**: Add a scene with a PEMDAS rule table and two explicitly parenthesized versions of the expression in separate boxes, showing (8÷2)(2+2) = 16 and 8÷(2(2+2)) = 1. Demonstrates that explicit parentheses eliminate the ambiguity.

**Expected output file**: Updated `pemdas_debug.py` or new `pemdas_fix.py` with `B06_PEMDASFixed` class.
