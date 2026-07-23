# PROMPTS — domain-restrictions

## B02 — Initial claude prompt (ASK)

```bash
claude "write a Manim scene showing two rational functions: f(x)=1/(x-2) with vertical asymptote, and g(x)=(x^2-4)/(x-2) which simplifies to x+2 but has a removable hole at x=2"
```

**Intent**: Generate a Manim scene plotting f(x) = 1/(x-2) on an Axes object with two separate branches (x<2 and x>2), a dashed vertical asymptote at x=2, and domain annotation.

**Expected output file**: `domain_holes.py`

---

## B05 — Revision claude prompt (CHANGE)

```bash
claude "show g(x)=(x^2-4)/(x-2) simplified step by step and plot it with an open circle at x=2 to show the removable discontinuity"
```

**Intent**: Add a two-panel comparison scene. Left panel: f(x) asymptote facts. Right panel: g(x) factored step-by-step, simplified to x+2, then marked with an open circle at the point (2,4) to show the removable discontinuity (hole).

**Expected output file**: Updated `domain_holes.py` with `B06_DomainHole2` class.
