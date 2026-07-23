# PROMPTS — polynomial-factoring

## B02 — Initial claude prompt (ASK)

```bash
claude "write a Manim scene showing the polynomial factoring decision tree: check GCF → count terms → if 2 terms check difference of squares → if 3 terms use ac method or simple trinomial strategy"
```

**Intent**: Generate an animated decision tree in Manim with RoundedRectangle nodes and GrowArrow connectors. Top node: Extract GCF. Middle node: How many terms? Left branch (2 terms): difference of squares. Right branch (3 terms): trinomial strategy with result (x+p)(x+q).

**Expected output file**: `factoring_tree.py`

---

## B05 — Revision claude prompt (CHANGE)

```bash
claude "add a worked example tracing x^2+5x+6 through the tree step by step"
```

**Intent**: Add a second scene that traces x²+5x+6 through the tree in 6 labeled steps: GCF=none, 3 terms, find p·q=6 and p+q=5, check pairs (1×6 fails, 2×3 succeeds), answer (x+2)(x+3), verify by expanding.

**Expected output file**: Updated `factoring_tree.py` with `B06_FactoringExample` class.
