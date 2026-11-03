# FACTCHECK — What the Measure Was Hiding

Every figure that appears on screen or in narration, and how it was checked.
Repo cloned at `2e38c9e`. Nothing below is taken from the changelog on trust;
where the changelog is the only source, the figure is **not used**.

## Counts

| Claim | On screen | How verified | Result |
|---|---|---|---|
| Nine representations | B00, B01, B06 | `find src/prot2vec/embedders -name '*.py'` minus `__init__`/`base` | composition, ctd, dipeptide, esm, huggingface, kmer, llm, onehot, physicochemical = **9** ✓ |
| Thirteen projections | B00, B01, B06 | `grep 'class .*Reducer' src/prot2vec/reduction/reducers.py` minus the ABC | PCA, UMAP, TSNE, TruncatedSVD, NMF, RandomProjection, KernelPCA, Isomap, MDS, Spectral, LLE, PHATE, PaCMAP = **13** ✓ |
| Thirty-one metrics | B00, B06 | Counted key by key out of `evaluation/suite.py`: projection 5, classification 9, retrieval 4, clustering 10, confound 3 | **31** ✓ |
| Five metric groups | implied by B06 | `METRIC_GROUPS` tuple, `suite.py:62` | **5** ✓ |
| 411 tests, up from 208 | B00, B06 | Static AST count of `def test_*` with `@parametrize` argvalue lists expanded. HEAD: 318 plain + 93 parametrised = **411**. At `405b00e` (v0.2.0): **208** ✓ Both reconcile exactly with the changelog. |
| Six of nine need no PyTorch | B01 narration | README "Install" section; the six descriptor embedders have no torch import | ✓ |

## The coverage measurement (B04)

Recorded by `evidence/coverage_exclusion.py`, output in
`evidence/coverage_exclusion.out`. coverage 7.8.2, Python 3.11.

The script never imports or executes Prot2Vec. It drives `coverage.parser.PythonParser`
directly, which is what decides exclusions — the same static decision that misfired.

| Claim | Value | Note |
|---|---|---|
| Old pattern | `"\.\.\."` | `pyproject.toml` @ `405b00e`, line 119. Unanchored. |
| New pattern | `"^\s*\.\.\.$"` | `pyproject.toml` @ `40ff686`, line 137. |
| Statements hidden, whole tree | **61** | 2199 measured anchored vs 2138 unanchored, of 2203 total |
| Statements hidden, `suite.py` | **47** | 60 statements measured anchored, 13 unanchored |
| `cli.py` / `pipeline.py` | **9** / **2** | also in the table |
| The matching annotation | `tuple[str, ...]` | `suite.py:157`, in `evaluate()`'s own signature |

The headline coverage percentage moves only ~2.8 points tree-wide, which is the
point B04 makes: the aggregate looked fine while 78% of the scoring module was
unmeasured. **The changelog's "84% coverage" figure is NOT used** — reproducing
it requires running the full suite under the optional extras, which was not done.

## The algebra (B02)

Read from `src/prot2vec/evaluation/projection.py`, not from the changelog.

- `neighborhood_preservation` computes, per point, `len(high_set & low_set) / k`
  and returns the mean over n points. Typeset as
  NP(k) = (1/nk) · Σᵢ |N_k^H(i) ∩ N_k^L(i)|. **Equivalent** ✓
- `local_continuity_meta_criterion` returns `overlap - k / (n_samples - 1)`.
  Typeset as LCMC(k) = NP(k) − k/(n−1). **Exact** ✓
- Domain: `k = max(1, min(n_neighbors, n_samples - 1))`, so k < n holds. Stated
  in the conditions line.
- Range: the docstring gives `0.0` = chance and `1 - k/(n-1)` as the maximum,
  consistent with the subtraction shown.

**Reproducible numerical case**, recorded in `evidence/lcmc_chance.out` by
running the shipped functions on seeded independent random matrices
(seed 20260918, n=90, d=64, k=10, 40 trials):

| Quantity | Predicted | Measured |
|---|---|---|
| NP(k) on pure noise | k/(n−1) = 10/89 = 0.1124 | 0.1092 ± 0.0108 |
| LCMC(k) on pure noise | 0 | −0.0032 ± 0.0108 |

The third typeset row, `k/(n−1) = 10/89 ≈ 0.1124`, uses n=90 because that is
the sequence count in the README's own `quick.yaml` example output, and k=10
because that is `n_neighbors`' default in `compute_trustworthiness`.

Typography: the three rows are outlined SVG from `runtime/scripts/typeset_math.py`
(matplotlib mathtext, STIX, `svg.fonttype=path`) — real fraction bars, a real
summation with bound index i and limits 1..n, real sub/superscripts, sized
delimiters around the intersection. `NP`, `LCMC` are upright (`\mathrm`);
n, k, i are italic. **No raw TeX appears in any text card.**

### Rendered-frame review (MATH-TYPESETTING.md) — DONE

B02's equation frames were inspected in **both** output aspects. Frames kept in
`_qc/look/` (landscape) and `vertical/_qc/look/` (portrait).

| Aspect | Frames inspected | Result |
|---|---|---|
| 16:9 (3840×2160) | 15% (2.88s), 50% (9.60s), 85% (16.30s) | **pass** |
| 9:16 (2160×3840) | 85% (16.30s), bottom strip at 18.0s | **pass** |

Checked at each reveal and at ordinary viewing size, not only at 4K:

- Fraction bars render as real rules on `1/nk`, `k/(n−1)` and `10/89`; numerator
  and denominator stay visibly grouped in both aspects.
- The summation carries its bound index `i = 1` below and limit `n` above, both
  legible and unclipped.
- Superscripts `H`/`L` and subscript `k` on `N` are correctly placed and do not
  collide with the adjacent parentheses.
- Sized delimiters `|…|` enclose the intersection at full expression height.
- `NP` and `LCMC` are upright; `n`, `k`, `i` are italic. `∩` and `≈` both resolve
  to real glyphs — no tofu, no fallback.
- Nothing is clipped at any frame edge in either aspect; the portrait stack keeps
  clear margins and the note/conditions text below it does not overlap.
- Staged reveal verified: row 1 alone at 15%, all three by 85%. No invalid
  intermediate equality is ever displayed.

**One observation, not a defect.** Row 1 renders at a smaller glyph size than
rows 2–3. `TypesetMath` fixes each row's box height and scales width by aspect
ratio, so an expression with more vertical extent — row 1 has the summation —
gets smaller glyphs inside the same box. It remains legible at 1080p. Left as
is; changing it would mean editing the component, not the beat.

## Claims deliberately softened

| Tempting claim | Why it is not made |
|---|---|
| "117 method pairs" | 9 × 13 is arithmetic, but not every pair is valid — B05's whole subject. Narration says "a full matrix". |
| "84% coverage" | Changelog-only; not reproduced. Omitted. |
| "faster than v0.2.0" | No benchmark was run or supplied. |
| "caught a real confound in Pfam" | The confound group is new; no run demonstrating a caught confound was supplied. B03 describes what it checks, not a finding. |
| "the bug hid evaluate() from the test suite" | Coverage exclusion hides lines from *the report*, not from execution. The tests still ran; nobody could see whether they covered it. B04's narration says "left the report". |
