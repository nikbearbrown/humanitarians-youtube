# Foundation Model — Plan 1: Data Audit and Corpus Build

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `corpus_v1`, the pretraining corpus for model A: public spontaneous-Raman spectra on one shared grid, with every Bacteria-ID spectrum kept out. Also build loaders for our two downstream tasks. End with the G0 go/no-go decision.

**Architecture:** This is a new, self-contained `foundation/` package that imports nothing from `src/`, `legacy_baseline/` or the old tools. The pipeline:

1. **Harmonise:** each source adapter yields raw spectra, which are put on the 1001-point grid (350–1850 cm⁻¹, step 1.5) with a validity mask and min–max normalised.
2. **Filter:** drop spectra that aren't usable or that are copies of Bacteria-ID.
3. **Cap and deduplicate.**
4. **Split** into pretrain, probe-train and probe-test.
5. **Write** the result to disk with a manifest.

A separate audit command reads the manifest and decides G0.

**Tech Stack:**
- Python 3.12 in the repo's `venv` (torch 2.11 with CUDA, numpy, scipy, pandas).
- Added: pyarrow, pytest, pyyaml, requests and h5py.

**Spec:** `docs/superpowers/specs/2026-10-01-raman-foundation-model-design.md`. This plan implements §2, §3, §4 and phase 0 of §7. Plan 2 covers the model and pretraining (§5); Plan 3 covers adaptation and evaluation (§6, §8). Those plans are written after this one passes G0.

## Global Constraints

- **Separate code:** nothing in `foundation/` imports from `src/`, `legacy_baseline/`, `main.py`, `evaluate_kfold.py` or `generate_heatmaps.py`.
- **"Our data":** every Bacteria-ID file: `X/y_reference`, `X/y_finetune`, `X/y_test`, `X/y_2018clinical`, `X/y_2019clinical`, plus `wavenumbers.npy`. These files are read-only, and none of it may enter the pretraining corpus.
- **Grid:** 350–1850 cm⁻¹, ascending, step 1.5 cm⁻¹, **1001 points**.
- **Preprocessing order:** clean the axis, remove cosmic spikes (Whitaker–Hayes), anti-alias and resample, then min–max over valid points only. **No baseline correction.**
- **No extrapolation:** grid points outside a source's range are 0 *and* masked.
- **Leakage guard:** drop exact hash matches and near-duplicates (cosine > 0.999) of any of our spectra.
- **DeepeR cap:** at most 2,000 spectra per image or map.
- **Source sampling weight:** proportional to √n_source, stored per spectrum.
- **Probe slice:** split by sample or map, never by spectrum. Taken only from labelled probe sources.
- **Excluded data:** all SERS, all IR, all simulated spectra, and every Bacteria-ID copy (including PB2/PB30 and `raman_data`'s Bacteria-ID entry).
- **G0:** at least **150,000** usable pretraining spectra after filtering and deduplication.
- **Python:** run everything with the repo venv, `venv/Scripts/python.exe`, from the repo root.

## Deviations from the spec (found while verifying source formats)

| # | Spec said | Reality | What this plan does |
|---|---|---|---|
| D1 | DeepeR: at most 2,000 spectra per image | The denoising set is shuffled, with no cell or image IDs (11 cells) | Use the high-SNR *Outputs* only, as a seeded random subsample of 11 × 2,000 = **22,000**. DeepeR needs a **manual download** (SharePoint can't be scripted reliably) and is marked optional |
| D2 | Consistent preprocessing across sources | The airborne-pathogen set comes already **baseline-corrected and min–max scaled**, at a coarse **5.33 cm⁻¹** spacing | Kept, because it's the closest domain (bacteria, single cells). The source-ID probe in Plan 2 checks whether it becomes a source shortcut. The augmented `U_aug` files are excluded |
| D3 | API compounds as a probe task | The API CSV has no replicate or sample IDs, so it can't be split by sample | API is **pretrain-only**. The probe tasks are **RRUFF species** and **airborne species** (each airborne file is a separate cell) |
| D4 | — | RRUFF ships RAW and Processed (baseline-corrected) copies of each specimen | Keep **RAW only** |
| D5 | `raman_data` as a source | Its dependencies are heavy (datasets, spectrochempy, kagglehub, …) and could disturb the main venv | Export the chosen datasets to `.npz` using a **separate small venv**. The main env never imports `raman_data` |
| D6 | — | Marine pathogens have no wavenumber axis in the source; locust data is resonance Raman; DeepeR super-resolution is 5.2 GB | All three are **excluded** |
| D7 | MLROD in the corpus | Its size is confirmed at 130,061 spectra in 41 files (not 500k) | Pretrain-only, grouped by file |
| D8 | — | The labels file inside the Zenodo bacteria zip is unverified | Labels are used only if the metadata CSV is found and row-aligned; otherwise the spectra stay unlabelled. Not a probe |

## Review Focus

These are inputs the spec implies but doesn't spell out. Each gets a test in the task that owns the code.

1. **A source axis in absolute wavenumbers or the wrong unit.** It should raise `AxisError`, not silently produce a garbage spectrum. Test in Task 1.
2. **The same spectrum hosted by two sources, or twice in one source.** The duplicate must be removed. A copy must never sit in pretrain while its twin is in the probe slice. Tests in Task 5.
3. **NaN or inf intensities inside an otherwise good spectrum.** Those points are dropped; NaN must never spread into the output. Test in Task 1.
4. **Mixed label types across sources** (int, float, str, None or NaN). They're normalised to `str` or `None`, so the parquet write never fails. Tests in Tasks 4 and 5.
5. **A download interrupted halfway.** It must never be mistaken for a complete file on the next run. Test in Task 4.

---

## File Structure

```
foundation/
  __init__.py
  requirements.txt            extra deps for this package
  README.md                   how to build the corpus and run the audit
  configs/
    corpus_v1.yaml            source list and build parameters
  data/
    __init__.py
    harmonize.py              grid, clean_axis, despike, resample, minmax_valid, harmonize, harmonize_many, is_usable
    tasks.py                  load_ours, stratified_split, load_t1, load_t2 (our tasks on the grid)
    leakage.py                spectrum_hash, LeakageGuard
    build_corpus.py           cap_per_sample, assign_splits, sampling_weights, build, main
    audit.py                  summarize, main (G0 decision)
    sources/
      __init__.py             REGISTRY; imports every adapter module
      base.py                 RawBatch, Source protocol, ManualDownloadRequired, fetch, register
      rruff.py                Task 7
      api_flanagan.py         Task 8
      airborne.py             Task 9
      zenodo_guo.py           Task 10 (zenodo_bacteria, zenodo_oil)
      mlrod.py                Task 11
      deeper.py               Task 12 (manual download)
      raman_data_export.py    Task 13 (reads .npz exported by the tool below)
  configs/raman_data_whitelist.yaml   Task 13
  tools/export_raman_data.py          Task 13 (runs in foundation/.venv-raman-data)
tests/foundation/
  test_harmonize.py
  test_tasks.py
  test_leakage.py
  test_sources_base.py
  test_build_corpus.py
  test_audit.py
  test_source_<name>.py       one per adapter, using a tiny fixture in the real format
  fixtures/                   tiny sample files in each source's real format
```

All tests run from the repo root with `venv/Scripts/python.exe -m pytest tests/foundation -v`.

---

### Task 1: Package scaffold and harmonisation

**Files:**
- Create: `foundation/__init__.py`, `foundation/data/__init__.py`, `foundation/requirements.txt`
- Create: `foundation/data/harmonize.py`
- Modify: `.gitignore` (append)
- Test: `tests/foundation/test_harmonize.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `GRID: np.ndarray` (1001,) float64; `N_GRID = 1001`; `GRID_START = 350.0`, `GRID_STOP = 1850.0`, `GRID_STEP = 1.5`; `HARMONIZE_VERSION = 1`; `MIN_VALID_POINTS = 200`.
  - `class AxisError(ValueError)`.
  - `clean_axis(x, y) -> (x_sorted_unique: np.ndarray, y: np.ndarray)`.
  - `despike(y, threshold=8.0, window=3) -> np.ndarray`.
  - `resample(x, y, grid=GRID) -> (values: float32 (1001,), mask: bool (1001,))`.
  - `minmax_valid(y, mask) -> float32 (1001,)`.
  - `harmonize(x, y) -> (spectrum: float32 (1001,), mask: bool (1001,))`.
  - `harmonize_many(axes, spectra) -> (S: float32 (n,1001), M: bool (n,1001))`. `axes` is either one shared 1D axis or a sequence of per-spectrum axes.
  - `is_usable(spectrum, mask) -> bool`.

- [ ] **Step 1: Create the scaffold and install the extra dependencies**

`foundation/__init__.py`:
```python
"""Raman foundation model experiment (A -> B1/B2). Self-contained: imports nothing from src/."""
```

`foundation/data/__init__.py`:
```python
```

`foundation/requirements.txt`:
```
pyarrow>=15
pytest>=8
pyyaml>=6
requests>=2.31
h5py>=3.10
```

Append to `.gitignore`:
```
# foundation experiment: raw downloads, built corpora, caches, runs
foundation/data/raw/
foundation/data/cache/
foundation/data/corpus_*/*
!foundation/data/corpus_*/manifest.json
foundation/runs/
```

Run: `venv/Scripts/python.exe -m pip install -r foundation/requirements.txt`
Expected: ends with `Successfully installed ...`, or every requirement reports "Requirement already satisfied".

- [ ] **Step 2: Write the failing tests**

`tests/foundation/test_harmonize.py`:
```python
import numpy as np
import pytest

from foundation.data.harmonize import (GRID, N_GRID, AxisError, despike, harmonize,
                                       harmonize_many, is_usable)


def gaussian(x, center, sigma, height=1.0):
    return height * np.exp(-0.5 * ((x - center) / sigma) ** 2)


def peak_center(spec):
    """Sub-grid peak position by a parabola through the max and its neighbours."""
    i = int(np.argmax(spec))
    y0, y1, y2 = spec[i - 1], spec[i], spec[i + 1]
    offset = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
    return GRID[i] + offset * (GRID[1] - GRID[0])


def test_grid_is_1001_points_350_to_1850():
    assert N_GRID == 1001
    assert GRID[0] == 350.0 and GRID[-1] == 1850.0
    assert np.allclose(np.diff(GRID), 1.5)


@pytest.mark.parametrize("step", [0.7, 1.41, 3.0])
def test_peak_position_preserved_within_half_wavenumber(step):
    x = np.arange(300.0, 2000.0, step)
    y = 0.1 + gaussian(x, 1001.3, 4.0)
    spec, _ = harmonize(x, y)
    assert abs(peak_center(spec) - 1001.3) < 0.5


def test_descending_axis_gives_identical_output():
    x = np.linspace(381.98, 1792.4, 1000)
    y = 0.2 + gaussian(x, 1450.0, 6.0)
    a_spec, a_mask = harmonize(x, y)
    b_spec, b_mask = harmonize(x[::-1], y[::-1])
    np.testing.assert_array_equal(a_spec, b_spec)
    np.testing.assert_array_equal(a_mask, b_mask)


def test_never_extrapolates_outside_source_range():
    x = np.arange(600.0, 1800.0, 1.0)
    spec, mask = harmonize(x, 1 + gaussian(x, 1000, 5))
    assert not mask[GRID < 600].any()
    assert not mask[GRID > 1800].any()
    assert mask[(GRID >= 601) & (GRID <= 1799)].all()
    assert (spec[~mask] == 0).all()


def test_gap_in_source_sampling_is_masked():
    x = np.arange(400.0, 1800.0, 1.0)
    x = x[(x < 1000) | (x > 1050)]
    _, mask = harmonize(x, 1 + gaussian(x, 1200, 5))
    assert not mask[np.argmin(np.abs(GRID - 1025.0))]
    assert mask[np.argmin(np.abs(GRID - 900.0))]


def test_bacteria_id_axis_covers_940_grid_points():
    x = np.linspace(1792.4, 381.98, 1000)          # descending, like data/wavenumbers.npy
    _, mask = harmonize(x, 1 + gaussian(x, 1000, 5))
    assert mask.sum() == 940                        # grid points 383.0 .. 1791.5


def test_minmax_uses_valid_points_only():
    x = np.arange(600.0, 1800.0, 1.0)
    spec, mask = harmonize(x, 5 + 3 * gaussian(x, 1000, 5))
    assert spec[mask].min() == pytest.approx(0.0, abs=1e-6)
    assert spec[mask].max() == pytest.approx(1.0, abs=1e-6)


def test_despike_removes_cosmic_spike_and_keeps_real_band():
    rng = np.random.default_rng(0)
    x = np.arange(1000)
    clean = gaussian(x, 300, 10) + rng.normal(0, 0.01, x.size)
    spiky = clean.copy()
    spiky[700] += 1.0
    out = despike(spiky)
    assert abs(out[700] - clean[700]) < 0.05
    np.testing.assert_allclose(out[250:350], clean[250:350])


def test_nan_and_inf_points_are_dropped_not_propagated():
    x = np.arange(400.0, 1800.0, 1.0)
    y = 1 + gaussian(x, 1000, 5)
    y[100] = np.nan
    y[200] = np.inf
    spec, mask = harmonize(x, y)
    assert np.isfinite(spec).all()
    assert mask.sum() > 900


def test_absolute_wavenumber_axis_is_rejected():
    x = np.linspace(11000.0, 12700.0, 500)          # absolute cm^-1, not Raman shift
    with pytest.raises(AxisError):
        harmonize(x, np.ones_like(x))


def test_flat_or_short_spectra_are_not_usable():
    x = np.arange(400.0, 1800.0, 1.0)
    spec, mask = harmonize(x, np.ones_like(x))
    assert not is_usable(spec, mask)
    xs = np.arange(1000.0, 1100.0, 1.0)
    spec, mask = harmonize(xs, 1 + gaussian(xs, 1050, 3))
    assert not is_usable(spec, mask)
    spec, mask = harmonize(x, 1 + gaussian(x, 1000, 5))
    assert is_usable(spec, mask)


def test_harmonize_many_shared_axis_matches_per_spectrum_axes():
    x = np.arange(400.0, 1800.0, 1.2)
    Y = np.stack([1 + gaussian(x, c, 5) for c in (700, 1000, 1500)])
    S1, M1 = harmonize_many(x, Y)
    S2, M2 = harmonize_many([x, x, x], list(Y))
    assert S1.shape == (3, 1001) and S1.dtype == np.float32 and M1.dtype == bool
    np.testing.assert_array_equal(S1, S2)
    np.testing.assert_array_equal(M1, M2)
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_harmonize.py -v`
Expected: collection error, `ModuleNotFoundError: No module named 'foundation.data.harmonize'`.

- [ ] **Step 4: Write the implementation**

`foundation/data/harmonize.py`:
```python
"""Put any Raman spectrum onto the shared wavenumber grid (spec section 4.3).

Order: clean axis -> despike -> anti-alias + resample -> min-max over valid
points. No baseline correction, by design (spec section 4.3).
"""
from __future__ import annotations

import numpy as np
from scipy.ndimage import gaussian_filter1d

HARMONIZE_VERSION = 1  # bump whenever output changes; part of every cache key

GRID_START = 350.0
GRID_STOP = 1850.0
GRID_STEP = 1.5
GRID = np.linspace(GRID_START, GRID_STOP, 1001)
N_GRID = GRID.size

MIN_VALID_POINTS = 200            # under 300 cm^-1 of coverage is not worth keeping
AXIS_MIN, AXIS_MAX = -100.0, 5000.0  # plausible Raman-shift range in cm^-1


class AxisError(ValueError):
    """The axis is not a plausible Raman-shift axis in cm^-1."""


def clean_axis(x, y):
    """Drop non-finite points, sort ascending, drop duplicate wavenumbers."""
    x = np.asarray(x, dtype=np.float64).ravel()
    y = np.asarray(y, dtype=np.float64).ravel()
    if x.shape != y.shape:
        raise ValueError(f"axis has {x.size} points but spectrum has {y.size}")
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    if x.size and (x.min() < AXIS_MIN or x.max() > AXIS_MAX):
        raise AxisError(f"axis spans {x.min():.1f}..{x.max():.1f}; "
                        "expected a Raman shift in cm^-1")
    order = np.argsort(x, kind="stable")
    x, y = x[order], y[order]
    x, first = np.unique(x, return_index=True)
    return x, y[first]


def despike(y, threshold=8.0, window=3):
    """Whitaker-Hayes cosmic-ray removal.

    A modified z-score of the first difference flags spikes; each flagged point
    is replaced by the mean of the unflagged points within `window`.
    """
    y = np.asarray(y, dtype=np.float64)
    if y.size < 3:
        return y.copy()
    d = np.diff(y)
    med = np.median(d)
    mad = np.median(np.abs(d - med))
    if mad == 0:
        return y.copy()
    z = 0.6745 * (d - med) / mad
    spikes = np.zeros(y.size, dtype=bool)
    spikes[1:] = np.abs(z) > threshold
    out = y.copy()
    for i in np.flatnonzero(spikes):
        nb = np.arange(max(0, i - window), min(y.size, i + window + 1))
        nb = nb[~spikes[nb]]
        if nb.size:
            out[i] = y[nb].mean()
    return out


def _resample_clean(x, y, grid):
    """x must already be sorted, unique and finite (see clean_axis)."""
    out = np.zeros(grid.size, dtype=np.float32)
    mask = np.zeros(grid.size, dtype=bool)
    if x.size < 2:
        return out, mask
    step = float(np.median(np.diff(x)))
    grid_step = float(grid[1] - grid[0])
    if step < grid_step:
        # anti-alias: smooth to the grid's resolution (FWHM = one grid step)
        y = gaussian_filter1d(y, sigma=(grid_step / 2.3548) / step, mode="nearest")
    inside = np.flatnonzero((grid >= x[0]) & (grid <= x[-1]))
    g = grid[inside]
    pos = np.searchsorted(x, g)
    d_left = np.abs(g - x[np.clip(pos - 1, 0, x.size - 1)])
    d_right = np.abs(x[np.clip(pos, 0, x.size - 1)] - g)
    near = np.minimum(d_left, d_right) <= max(1.5 * step, grid_step)  # gaps stay masked
    keep = inside[near]
    out[keep] = np.interp(g[near], x, y)
    mask[keep] = True
    return out, mask


def resample(x, y, grid=GRID):
    x, y = clean_axis(x, y)
    return _resample_clean(x, y, grid)


def minmax_valid(y, mask):
    out = np.zeros(np.shape(y), dtype=np.float32)
    if not mask.any():
        return out
    v = np.asarray(y, dtype=np.float64)[mask]
    lo, hi = v.min(), v.max()
    if hi - lo <= 0:
        return out
    out[mask] = (v - lo) / (hi - lo)
    return out


def harmonize(x, y):
    x, y = clean_axis(x, y)
    if x.size < 2:
        return np.zeros(N_GRID, dtype=np.float32), np.zeros(N_GRID, dtype=bool)
    y = despike(y)
    spec, mask = _resample_clean(x, y, GRID)
    return minmax_valid(spec, mask), mask


def harmonize_many(axes, spectra):
    """axes: one shared 1D axis, or a sequence (or 2D array) of per-spectrum axes."""
    n = len(spectra)
    S = np.zeros((n, N_GRID), dtype=np.float32)
    M = np.zeros((n, N_GRID), dtype=bool)
    shared = isinstance(axes, np.ndarray) and axes.ndim == 1
    for i in range(n):
        S[i], M[i] = harmonize(axes if shared else axes[i], spectra[i])
    return S, M


def is_usable(spectrum, mask):
    return int(mask.sum()) >= MIN_VALID_POINTS and float(spectrum[mask].max()) > 0.0
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_harmonize.py -v`
Expected: 14 passed (the parametrized test counts as 3).

- [ ] **Step 6: Commit**

```bash
git add foundation/__init__.py foundation/data/__init__.py foundation/requirements.txt foundation/data/harmonize.py tests/foundation/test_harmonize.py .gitignore
git commit -m "foundation: scaffold package and harmonise spectra onto the shared grid"
```

---

### Task 2: Our tasks (T1, T2) on the grid

**Files:**
- Create: `foundation/data/tasks.py`
- Test: `tests/foundation/test_tasks.py`

**Interfaces:**
- Consumes: `harmonize_many`, `HARMONIZE_VERSION` from Task 1.
- Produces:
  - `OUR_NAMES = ("reference", "finetune", "test", "2018clinical", "2019clinical")`; `SPLIT_SEED = 0`; `VAL_FRACTION = 0.1`.
  - `@dataclass Split(X: float32 (n,1001), M: bool (n,1001), y: int64 (n,))`.
  - `@dataclass Task(name: str, classes: np.ndarray, splits: dict[str, Split])`.
  - `load_ours(data_dir="data", cache_dir="foundation/data/cache") -> dict[str, tuple[X, M, y_raw]]`, keyed by `OUR_NAMES`.
  - `stratified_split(y, val_fraction=0.1, seed=0) -> (train_idx, val_idx)`.
  - `load_t1(data_dir="data", cache_dir=..., ours=None) -> Task`, with split keys `ref_train`, `ref_val`, `ft_train`, `ft_val`, `test`.
  - `load_t2(data_dir="data", cache_dir=..., ours=None) -> Task`, with split keys `train`, `val`, `test`.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_tasks.py`:
```python
from pathlib import Path

import numpy as np
import pytest

from foundation.data.tasks import load_ours, load_t1, load_t2

AXIS = np.linspace(1792.4, 381.98, 1000)       # descending, like the real file


def _spectra(labels, rng):
    centers = {lab: 500 + 37 * (i + 1) for i, lab in enumerate(sorted(set(labels)))}
    return np.stack([0.2 + np.exp(-0.5 * ((AXIS - centers[l]) / 6) ** 2)
                     + rng.normal(0, 0.01, AXIS.size) for l in labels])


@pytest.fixture
def fake_data(tmp_path):
    rng = np.random.default_rng(0)
    d = tmp_path / "data"
    d.mkdir()
    np.save(d / "wavenumbers.npy", AXIS)
    sets = {
        "reference": np.repeat([0.0, 1.0, 2.0], 20),
        "finetune": np.repeat([0.0, 1.0, 2.0], 10),
        "test": np.repeat([0.0, 1.0, 2.0], 10),
        "2018clinical": np.repeat([0.0, 2.0, 3.0, 5.0, 6.0], 10),
        "2019clinical": np.repeat([0.0, 2.0, 3.0, 5.0, 6.0], 4),
    }
    for name, y in sets.items():
        np.save(d / f"X_{name}.npy", _spectra(y, rng))
        np.save(d / f"y_{name}.npy", y)
    return d


def test_t1_shapes_dtypes_and_mask(fake_data, tmp_path):
    t1 = load_t1(fake_data, cache_dir=tmp_path / "cache")
    assert t1.classes.tolist() == [0.0, 1.0, 2.0]
    assert set(t1.splits) == {"ref_train", "ref_val", "ft_train", "ft_val", "test"}
    s = t1.splits["ref_train"]
    assert s.X.shape[1] == 1001 and s.X.dtype == np.float32
    assert s.M.dtype == bool and s.y.dtype == np.int64
    assert (s.M.sum(axis=1) == 940).all()


def test_t2_maps_treatment_labels_to_0_through_4(fake_data, tmp_path):
    t2 = load_t2(fake_data, cache_dir=tmp_path / "cache")
    assert t2.classes.tolist() == [0.0, 2.0, 3.0, 5.0, 6.0]
    assert set(np.unique(t2.splits["test"].y)) == {0, 1, 2, 3, 4}
    assert len(t2.splits["test"].y) == 20


def test_validation_split_is_stratified_disjoint_and_fixed(fake_data, tmp_path):
    a = load_t1(fake_data, cache_dir=tmp_path / "cache")
    b = load_t1(fake_data, cache_dir=tmp_path / "cache")
    assert np.bincount(a.splits["ref_val"].y).tolist() == [2, 2, 2]     # 10% of 20 per class
    assert len(a.splits["ref_train"].y) + len(a.splits["ref_val"].y) == 60
    np.testing.assert_array_equal(a.splits["ref_val"].X, b.splits["ref_val"].X)


def test_unknown_test_label_raises(fake_data, tmp_path):
    y = np.load(fake_data / "y_test.npy")
    y[0] = 7.0
    np.save(fake_data / "y_test.npy", y)
    with pytest.raises(ValueError, match="not in task classes"):
        load_t1(fake_data, cache_dir=tmp_path / "cache")


def test_cache_is_reused_without_rereading_spectra(fake_data, tmp_path):
    load_ours(fake_data, tmp_path / "cache")
    for name in ("reference", "finetune", "test", "2018clinical", "2019clinical"):
        (fake_data / f"X_{name}.npy").unlink()
    ours = load_ours(fake_data, tmp_path / "cache")
    assert ours["reference"][0].shape == (60, 1001)


@pytest.mark.skipif(not Path("data/X_2018clinical.npy").exists(), reason="real data absent")
def test_real_clinical_task_loads(tmp_path):
    t2 = load_t2("data", cache_dir=tmp_path / "cache")
    assert len(t2.splits["train"].y) == 9000 and len(t2.splits["val"].y) == 1000
    assert len(t2.splits["test"].y) == 2500
    assert (t2.splits["test"].M.sum(axis=1) == 940).all()
```

Note: `test_cache_is_reused...` deletes the `X_*.npy` files but keeps the `y_*.npy` files, because the cache key is built from the `y` file sizes (see the implementation). The real-data test harmonises all five files the first time, about 79k spectra, which takes roughly a minute.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_tasks.py -v`
Expected: collection error, `ModuleNotFoundError: No module named 'foundation.data.tasks'`.

- [ ] **Step 3: Write the implementation**

`foundation/data/tasks.py`:
```python
"""Our Bacteria-ID tasks on the common grid (spec section 3).

Reads data/*.npy read-only. Model A's corpus build uses load_ours() only to
know what to KEEP OUT (leakage guard); nothing here feeds pretraining.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .harmonize import HARMONIZE_VERSION, harmonize_many

OUR_NAMES = ("reference", "finetune", "test", "2018clinical", "2019clinical")
SPLIT_SEED = 0       # fixed: every arm and every seed sees the same validation split
VAL_FRACTION = 0.1


@dataclass
class Split:
    X: np.ndarray    # (n, 1001) float32
    M: np.ndarray    # (n, 1001) bool
    y: np.ndarray    # (n,) int64 class index


@dataclass
class Task:
    name: str
    classes: np.ndarray            # raw label value for each class index
    splits: dict


def _cache_key(data_dir: Path) -> str:
    sizes = [(n, (data_dir / f"y_{n}.npy").stat().st_size) for n in OUR_NAMES]
    return hashlib.sha1(repr(sizes).encode()).hexdigest()[:8]


def load_ours(data_dir="data", cache_dir="foundation/data/cache"):
    """Harmonise every Bacteria-ID file once. Returns {name: (X, M, y_raw)}."""
    data_dir = Path(data_dir)
    cache = Path(cache_dir) / f"ours_h{HARMONIZE_VERSION}_{_cache_key(data_dir)}.npz"
    if cache.exists():
        z = np.load(cache)
        return {n: (z[f"{n}_X"], z[f"{n}_M"], z[f"{n}_y"]) for n in OUR_NAMES}
    axis = np.load(data_dir / "wavenumbers.npy")
    out = {}
    for n in OUR_NAMES:
        X = np.load(data_dir / f"X_{n}.npy")
        y = np.load(data_dir / f"y_{n}.npy")
        S, M = harmonize_many(axis, X)
        out[n] = (S, M, y)
    cache.parent.mkdir(parents=True, exist_ok=True)
    arrays = {}
    for n, (S, M, y) in out.items():
        arrays[f"{n}_X"], arrays[f"{n}_M"], arrays[f"{n}_y"] = S, M, y
    np.savez(cache, **arrays)
    return out


def stratified_split(y, val_fraction=VAL_FRACTION, seed=SPLIT_SEED):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    val = []
    for c in np.unique(y):
        idx = np.flatnonzero(y == c)
        rng.shuffle(idx)
        val.append(idx[: int(round(val_fraction * idx.size))])
    val = np.sort(np.concatenate(val))
    train = np.setdiff1d(np.arange(y.size), val)
    return train, val


def _encode(y_raw, classes):
    lookup = {float(c): i for i, c in enumerate(classes)}
    try:
        return np.array([lookup[float(v)] for v in y_raw], dtype=np.int64)
    except KeyError as e:
        raise ValueError(f"label {e.args[0]} not in task classes {classes.tolist()}") from None


def _split(X, M, y, idx=None):
    if idx is None:
        return Split(X, M, y)
    return Split(X[idx], M[idx], y[idx])


def load_t1(data_dir="data", cache_dir="foundation/data/cache", ours=None) -> Task:
    ours = ours or load_ours(data_dir, cache_dir)
    Xr, Mr, yr_raw = ours["reference"]
    classes = np.unique(yr_raw)
    yr = _encode(yr_raw, classes)
    Xf, Mf, yf_raw = ours["finetune"]
    yf = _encode(yf_raw, classes)
    Xt, Mt, yt_raw = ours["test"]
    yt = _encode(yt_raw, classes)
    rtr, rva = stratified_split(yr)
    ftr, fva = stratified_split(yf)
    return Task("T1_isolates", classes, {
        "ref_train": _split(Xr, Mr, yr, rtr), "ref_val": _split(Xr, Mr, yr, rva),
        "ft_train": _split(Xf, Mf, yf, ftr), "ft_val": _split(Xf, Mf, yf, fva),
        "test": _split(Xt, Mt, yt),
    })


def load_t2(data_dir="data", cache_dir="foundation/data/cache", ours=None) -> Task:
    ours = ours or load_ours(data_dir, cache_dir)
    Xa, Ma, ya_raw = ours["2018clinical"]
    classes = np.unique(ya_raw)
    ya = _encode(ya_raw, classes)
    Xb, Mb, yb_raw = ours["2019clinical"]
    yb = _encode(yb_raw, classes)
    tr, va = stratified_split(ya)
    return Task("T2_clinical", classes, {
        "train": _split(Xa, Ma, ya, tr), "val": _split(Xa, Ma, ya, va),
        "test": _split(Xb, Mb, yb),
    })
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_tasks.py -v`
Expected: 6 passed. If `data/` is absent, it reports 5 passed, 1 skipped.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/tasks.py tests/foundation/test_tasks.py
git commit -m "foundation: load Bacteria-ID tasks T1/T2 onto the shared grid"
```

---

### Task 3: Leakage guard

**Files:**
- Create: `foundation/data/leakage.py`
- Test: `tests/foundation/test_leakage.py`

**Interfaces:**
- Consumes: `harmonize_many` (Task 1), only in the tests.
- Produces:
  - `spectrum_hash(spec: np.ndarray, mask: np.ndarray) -> str`.
  - `LeakageGuard(ref_X, ref_M, cos_threshold=0.999, min_overlap=0.5, device=None, batch_size=1024)` with `.find(X, M) -> np.ndarray[bool]`, where True means "matches a reference spectrum, drop it".
  - The same class is reused in Task 5, with probe spectra as the reference, for probe isolation.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_leakage.py`:
```python
import numpy as np

from foundation.data.harmonize import harmonize_many
from foundation.data.leakage import LeakageGuard, spectrum_hash

AXIS = np.linspace(1792.4, 381.98, 1000)


def _random_spectra(n, seed):
    rng = np.random.default_rng(seed)
    g = lambda c, s: np.exp(-0.5 * ((AXIS - c) / s) ** 2)
    raw = np.stack([0.2 + g(rng.uniform(500, 1700), rng.uniform(3, 15))
                    + g(rng.uniform(500, 1700), 8) + rng.normal(0, 0.01, AXIS.size)
                    for _ in range(n)])
    return harmonize_many(AXIS, raw)


def test_hash_is_stable_and_sensitive():
    S, M = _random_spectra(2, 0)
    assert spectrum_hash(S[0], M[0]) == spectrum_hash(S[0].copy(), M[0].copy())
    assert spectrum_hash(S[0], M[0]) != spectrum_hash(S[1], M[1])


def test_exact_copy_is_caught():
    S, M = _random_spectra(50, 0)
    guard = LeakageGuard(S, M, device="cpu")
    assert guard.find(S[:3], M[:3]).all()


def test_noisy_copy_is_caught_by_cosine():
    S, M = _random_spectra(50, 0)
    rng = np.random.default_rng(1)
    noisy = (S[:5] + rng.normal(0, 0.002, S[:5].shape) * M[:5]).astype(np.float32)
    guard = LeakageGuard(S, M, device="cpu")
    assert guard.find(noisy, M[:5]).all()


def test_unrelated_spectra_are_not_flagged():
    S, M = _random_spectra(50, 0)
    other_S, other_M = _random_spectra(20, 99)
    guard = LeakageGuard(S, M, device="cpu")
    assert not guard.find(other_S, other_M).any()


def test_small_overlap_is_not_flagged():
    S, M = _random_spectra(50, 0)
    from foundation.data.harmonize import GRID
    window = (GRID >= 1000) & (GRID <= 1100)
    crop_M = M[:1] & window
    crop_S = np.where(crop_M, S[:1], 0).astype(np.float32)
    guard = LeakageGuard(S, M, device="cpu")
    assert not guard.find(crop_S, crop_M).any()


def test_empty_input_returns_empty():
    S, M = _random_spectra(5, 0)
    guard = LeakageGuard(S, M, device="cpu")
    out = guard.find(S[:0], M[:0])
    assert out.shape == (0,) and out.dtype == bool
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_leakage.py -v`
Expected: collection error, `ModuleNotFoundError: No module named 'foundation.data.leakage'`.

- [ ] **Step 3: Write the implementation**

`foundation/data/leakage.py`:
```python
"""Keep reference spectra out of a candidate set (spec section 4.2).

Used twice: our Bacteria-ID spectra vs the corpus (leakage guard), and probe
spectra vs pretrain spectra (probe isolation, build_corpus).
"""
from __future__ import annotations

import hashlib

import numpy as np
import torch


def spectrum_hash(spec, mask) -> str:
    mask = np.asarray(mask, dtype=bool)
    h = hashlib.sha1()
    h.update(np.packbits(mask).tobytes())
    h.update(np.round(np.asarray(spec, dtype=np.float64)[mask], 4).astype(np.float32).tobytes())
    return h.hexdigest()


class LeakageGuard:
    """Flags candidates that are an exact hash match or a cosine near-duplicate
    (over the points valid in both) of any reference spectrum.

    A near-duplicate only counts if the candidate covers at least `min_overlap`
    of the reference spectrum's valid points, so a tiny cropped window cannot
    trigger a 0.999 match by chance.
    """

    def __init__(self, ref_X, ref_M, cos_threshold=0.999, min_overlap=0.5,
                 device=None, batch_size=1024):
        ref_M = np.asarray(ref_M, dtype=bool)
        self.hashes = {spectrum_hash(x, m) for x, m in zip(ref_X, ref_M)}
        self.cos_threshold = cos_threshold
        self.min_overlap = min_overlap
        self.batch_size = batch_size
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        O = np.where(ref_M, ref_X, 0.0).astype(np.float32)
        self.O = torch.from_numpy(O).to(self.device)
        self.O2 = self.O * self.O
        self.Om = torch.from_numpy(ref_M.astype(np.float32)).to(self.device)
        self.O_count = self.Om.sum(dim=1).clamp_min(1.0)

    @torch.no_grad()
    def find(self, X, M) -> np.ndarray:
        X = np.asarray(X)
        M = np.asarray(M, dtype=bool)
        leaked = np.array([spectrum_hash(x, m) in self.hashes for x, m in zip(X, M)],
                          dtype=bool).reshape(len(X))
        for s in range(0, len(X), self.batch_size):
            e = s + self.batch_size
            C = torch.from_numpy(np.where(M[s:e], X[s:e], 0.0).astype(np.float32)).to(self.device)
            Cm = torch.from_numpy(M[s:e].astype(np.float32)).to(self.device)
            dot = C @ self.O.T                 # both are zero outside their own masks
            c2 = (C * C) @ self.Om.T           # |candidate|^2 over the intersection
            o2 = Cm @ self.O2.T                # |reference|^2 over the intersection
            cos = dot / torch.sqrt(c2 * o2).clamp_min(1e-12)
            overlap = (Cm @ self.Om.T) / self.O_count
            cos = torch.where(overlap >= self.min_overlap, cos, torch.zeros_like(cos))
            leaked[s:e] |= (cos.max(dim=1).values >= self.cos_threshold).cpu().numpy()
        return leaked
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_leakage.py -v`
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/leakage.py tests/foundation/test_leakage.py
git commit -m "foundation: leakage guard (hash + masked cosine near-duplicate)"
```

---

### Task 4: Source interface, registry and safe download

**Files:**
- Create: `foundation/data/sources/__init__.py`, `foundation/data/sources/base.py`
- Test: `tests/foundation/test_sources_base.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `DOMAINS = ("bio", "mineral", "chem")`.
  - `@dataclass RawBatch(axes, spectra, sample_id, label, laser_nm)`.
    - `axes` is one shared 1D axis or one axis per spectrum.
    - `__post_init__` validates lengths and normalises the fields: `sample_id` becomes `list[str]`; `label` becomes `list[str | None]` (None, float NaN and empty string all become None); `laser_nm` becomes a float array of length n.
  - `class Source(Protocol)` with attributes `name`, `domain`, `licence`, `url`, `probe_label_kind` (a str describing what the label is, or None if unlabelled), and methods `download(raw_dir: Path) -> None` and `iter_batches(raw_dir: Path) -> Iterator[RawBatch]`.
    - **Adapter contract:** a batch holds at most 50,000 spectra, and **all spectra of one sample/map are in the same batch**, so per-sample caps work.
  - `class ManualDownloadRequired(RuntimeError)`. `download()` raises it when a source can't be fetched automatically; the message says how to get the files.
  - `fetch(url, dest: Path, sha256=None, timeout=60, retries=3, backoff=2.0) -> Path`.
    - It downloads through `dest.part` and renames only on success. If `dest` already exists it skips the download.
    - On a network error it retries up to `retries` times, waiting `backoff × attempt` seconds between tries.
  - `REGISTRY: dict[str, Source]` and `register(source) -> source`.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_sources_base.py`:
```python
import numpy as np
import pytest

from foundation.data.sources import base
from foundation.data.sources.base import RawBatch, fetch


def test_rawbatch_normalises_labels_ids_and_laser():
    b = RawBatch(axes=np.arange(10.0), spectra=np.zeros((4, 10)),
                 sample_id=[1, 1, 2, 2], label=[3, None, float("nan"), "quartz"],
                 laser_nm=532)
    assert b.sample_id == ["1", "1", "2", "2"]
    assert b.label == ["3", None, None, "quartz"]
    assert b.laser_nm.tolist() == [532.0] * 4


def test_rawbatch_rejects_length_mismatch():
    with pytest.raises(ValueError):
        RawBatch(axes=np.arange(10.0), spectra=np.zeros((3, 10)),
                 sample_id=["a", "b"], label=[None, None, None], laser_nm=532)


class _FakeResponse:
    def __init__(self, chunks, fail_after=None):
        self.chunks, self.fail_after = chunks, fail_after

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def raise_for_status(self):
        pass

    def iter_content(self, chunk_size):
        for i, c in enumerate(self.chunks):
            if self.fail_after is not None and i == self.fail_after:
                raise ConnectionError("connection dropped")
            yield c


def test_interrupted_download_never_looks_complete(tmp_path, monkeypatch):
    dest = tmp_path / "file.zip"
    monkeypatch.setattr(base.requests, "get",
                        lambda *a, **k: _FakeResponse([b"aa", b"bb"], fail_after=1))
    with pytest.raises(ConnectionError):
        fetch("http://example.invalid/file.zip", dest, retries=2, backoff=0)
    assert not dest.exists()
    monkeypatch.setattr(base.requests, "get",
                        lambda *a, **k: _FakeResponse([b"aa", b"bb"]))
    fetch("http://example.invalid/file.zip", dest)
    assert dest.read_bytes() == b"aabb"
    assert not (tmp_path / "file.zip.part").exists()


def test_existing_file_is_not_downloaded_again(tmp_path, monkeypatch):
    dest = tmp_path / "file.zip"
    dest.write_bytes(b"done")

    def boom(*a, **k):
        raise AssertionError("should not download")

    monkeypatch.setattr(base.requests, "get", boom)
    assert fetch("http://example.invalid/file.zip", dest) == dest


def test_checksum_mismatch_is_rejected(tmp_path, monkeypatch):
    dest = tmp_path / "file.zip"
    monkeypatch.setattr(base.requests, "get", lambda *a, **k: _FakeResponse([b"aabb"]))
    with pytest.raises(IOError, match="checksum"):
        fetch("http://example.invalid/file.zip", dest, sha256="0" * 64)
    assert not dest.exists()


def test_transient_failure_is_retried(tmp_path, monkeypatch):
    dest = tmp_path / "file.zip"
    calls = {"n": 0}

    def flaky(*a, **k):
        calls["n"] += 1
        return _FakeResponse([b"aa", b"bb"], fail_after=1 if calls["n"] == 1 else None)

    monkeypatch.setattr(base.requests, "get", flaky)
    fetch("http://example.invalid/file.zip", dest, retries=3, backoff=0)
    assert dest.read_bytes() == b"aabb" and calls["n"] == 2
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_sources_base.py -v`
Expected: collection error, `ModuleNotFoundError: No module named 'foundation.data.sources'`.

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/base.py`:
```python
"""Source adapter interface (spec section 4.1).

Adapter contract: iter_batches yields RawBatch objects of at most 50,000
spectra, and all spectra of one sample/map are in the same batch, so that
build_corpus can apply per-sample caps.
"""
from __future__ import annotations

import hashlib
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Protocol, Sequence

import numpy as np
import requests

DOMAINS = ("bio", "mineral", "chem")
MAX_BATCH = 50_000


def _norm_label(v):
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    s = str(v).strip()
    return s or None


@dataclass
class RawBatch:
    axes: object                       # 1D shared axis, or one axis per spectrum
    spectra: object                    # (n, p) array, or a sequence of 1D arrays
    sample_id: Sequence
    label: Sequence
    laser_nm: object                   # scalar or length-n sequence; NaN = unknown

    def __post_init__(self):
        n = len(self.spectra)
        if n > MAX_BATCH:
            raise ValueError(f"batch of {n} spectra exceeds {MAX_BATCH}")
        shared = isinstance(self.axes, np.ndarray) and self.axes.ndim == 1
        if not shared and len(self.axes) != n:
            raise ValueError(f"{len(self.axes)} axes for {n} spectra")
        if len(self.sample_id) != n or len(self.label) != n:
            raise ValueError(f"sample_id/label lengths {len(self.sample_id)}/"
                             f"{len(self.label)} do not match {n} spectra")
        self.sample_id = [str(s) for s in self.sample_id]
        self.label = [_norm_label(v) for v in self.label]
        if np.isscalar(self.laser_nm):
            self.laser_nm = np.full(n, float(self.laser_nm))
        self.laser_nm = np.asarray(self.laser_nm, dtype=np.float64)
        if self.laser_nm.shape != (n,):
            raise ValueError(f"laser_nm has shape {self.laser_nm.shape}, expected ({n},)")


class Source(Protocol):
    name: str
    domain: str                        # one of DOMAINS
    licence: str
    url: str
    probe_label_kind: str | None       # what `label` means, or None if unlabelled

    def download(self, raw_dir: Path) -> None: ...

    def iter_batches(self, raw_dir: Path) -> Iterator[RawBatch]: ...


class ManualDownloadRequired(RuntimeError):
    """The source cannot be fetched automatically; the message says how to get it."""


def fetch(url, dest, sha256=None, timeout=60, retries=3, backoff=2.0) -> Path:
    """Download to `dest` via `dest.part`; rename only on success. Retries on
    network errors (some hosts, e.g. rruff.net, drop connections)."""
    dest = Path(dest)
    if dest.exists():
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    for attempt in range(1, retries + 1):
        try:
            with requests.get(url, stream=True, timeout=timeout) as r:
                r.raise_for_status()
                with open(part, "wb") as fh:
                    for block in r.iter_content(chunk_size=1 << 20):
                        fh.write(block)
            break
        except (requests.RequestException, ConnectionError, TimeoutError):
            part.unlink(missing_ok=True)
            if attempt == retries:
                raise
            time.sleep(backoff * attempt)
    if sha256 is not None:
        digest = hashlib.sha256(part.read_bytes()).hexdigest()
        if digest != sha256:
            part.unlink()
            raise IOError(f"checksum mismatch for {url}: got {digest}")
    part.replace(dest)
    return dest


REGISTRY: dict = {}


def register(source):
    if source.domain not in DOMAINS:
        raise ValueError(f"{source.name}: domain {source.domain!r} not in {DOMAINS}")
    REGISTRY[source.name] = source
    return source
```

`foundation/data/sources/__init__.py`:
```python
"""Source registry. Each adapter module registers itself on import (Tasks 7+)."""
from .base import (REGISTRY, ManualDownloadRequired, RawBatch, Source,  # noqa: F401
                   fetch, register)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_sources_base.py -v`
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/__init__.py foundation/data/sources/base.py tests/foundation/test_sources_base.py
git commit -m "foundation: source adapter interface, registry and atomic download"
```

---

### Task 5: Corpus builder

**Files:**
- Create: `foundation/data/build_corpus.py`
- Test: `tests/foundation/test_build_corpus.py`

**Interfaces:**
- Consumes:
  - `harmonize_many`, `is_usable`, the grid constants and `HARMONIZE_VERSION` (Task 1);
  - `load_ours` (Task 2);
  - `LeakageGuard`, `spectrum_hash` (Task 3);
  - `REGISTRY`, `RawBatch` (Task 4).
- Produces:
  - `cap_per_sample(sample_ids: np.ndarray, max_per_sample: int, rng) -> np.ndarray[bool]` (keep mask).
  - `assign_splits(source, label, sample_id, probe_sources, probe_fraction, probe_test_fraction, min_class_spectra, seed) -> np.ndarray[object]`. Values are `"pretrain"`, `"probe_train"` or `"probe_test"`.
  - `sampling_weights(source, split) -> np.ndarray[float64]`. These are zero off pretrain and sum to 1 over pretrain. The total weight of each source is proportional to √n_source.
  - `raw_fingerprint(directory) -> str | None`: sha256 over the relative paths and sizes of the downloaded files. It's stored per source in the manifest (spec §4.6 "checksum").
  - `build(cfg: dict) -> dict` (the manifest).
  - `main(argv=None)`, the CLI: `python -m foundation.data.build_corpus --config <yaml>`.
  - **On-disk artefacts** in `cfg["out_dir"]`, which Plan 2 reads:
    - `spectra.npy`: float16 (N, 1001).
    - `mask.npy`: bool (N, 1001).
    - `meta.parquet`: columns `source`, `domain`, `laser_nm`, `sample_id`, `label` (str or null), `split`, `sample_weight`.
    - `splits.json`: `{"pretrain": [...], "probe_train": [...], "probe_test": [...]}`.
    - `manifest.json`.

**Config keys** used by `build` (the real file is written in the last task):
- `version`, `out_dir`, `raw_dir`, `cache_dir`, `our_data_dir`, `seed`, `device`;
- `leakage_cos_threshold` (0.999), `probe_fraction` (0.15), `probe_test_fraction` (0.4), `min_probe_class_spectra` (5);
- `sources`: a list of `{name, probe: bool, max_per_sample: int|null, optional: bool}`.
  - If a source raises `ManualDownloadRequired` and is `optional: true`, the build skips it and records `status: "skipped: ..."` in the manifest.
  - If it isn't optional, the build fails.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_build_corpus.py`:
```python
import json

import numpy as np
import pandas as pd
import pytest

from foundation.data import build_corpus as bc
from foundation.data.harmonize import harmonize_many
from foundation.data.sources.base import RawBatch

OUR_AXIS = np.linspace(1792.4, 381.98, 1000)


def _g(x, c, s):
    return np.exp(-0.5 * ((x - c) / s) ** 2)


def _our_raw(n=10, seed=0):
    rng = np.random.default_rng(seed)
    return np.stack([0.3 + _g(OUR_AXIS, rng.uniform(600, 1700), 6)
                     + _g(OUR_AXIS, rng.uniform(600, 1700), 10)
                     + rng.normal(0, 0.01, OUR_AXIS.size) for _ in range(n)])


class LabelledMinerals:
    """3 classes x 5 samples x 4 spectra, plus a flat spectrum and an exact
    duplicate of row 0. Labels are ints to test label normalisation."""
    name, domain, licence, url, probe_label_kind = "fake_min", "mineral", "CC0", "x", "species"

    def download(self, raw_dir):
        pass

    def iter_batches(self, raw_dir):
        rng = np.random.default_rng(1)
        x = np.arange(300.0, 1900.0, 2.0)
        spectra, ids, labels = [], [], []
        for cls, center in enumerate((500, 900, 1400)):
            for s in range(5):
                for _ in range(4):
                    spectra.append(0.1 + _g(x, center + rng.normal(0, 2), 5)
                                   + rng.normal(0, 0.01, x.size))
                    ids.append(f"c{cls}s{s}")
                    labels.append(cls)
        spectra.append(np.ones_like(x)); ids.append("flat"); labels.append(None)
        spectra.append(spectra[0].copy()); ids.append("c0s0"); labels.append(0)
        yield RawBatch(axes=x, spectra=np.stack(spectra), sample_id=ids,
                       label=labels, laser_nm=532)


class UnlabelledCells:
    """One big map (30 spectra, capped to 10) and one small map (5), plus one
    planted copy of an 'our' spectrum on our own axis."""
    name, domain, licence, url, probe_label_kind = "fake_cells", "bio", "?", "y", None

    def download(self, raw_dir):
        pass

    def iter_batches(self, raw_dir):
        rng = np.random.default_rng(2)
        x = np.arange(500.0, 1800.0, 1.0)
        big = [0.2 + _g(x, 1000 + 5 * i, 8) + rng.normal(0, 0.01, x.size) for i in range(30)]
        small = [0.2 + _g(x, 1300 + 7 * i, 8) + rng.normal(0, 0.01, x.size) for i in range(5)]
        yield RawBatch(axes=[x] * 35, spectra=big + small,
                       sample_id=["map_big"] * 30 + ["map_small"] * 5,
                       label=[None] * 35, laser_nm=785)
        yield RawBatch(axes=OUR_AXIS, spectra=_our_raw()[:1], sample_id=["planted"],
                       label=[None], laser_nm=633)


@pytest.fixture
def built(tmp_path, monkeypatch):
    our_S, our_M = harmonize_many(OUR_AXIS, _our_raw())
    y = np.zeros(len(our_S))
    ours = {n: (our_S, our_M, y) for n in ("reference", "finetune", "test",
                                            "2018clinical", "2019clinical")}
    monkeypatch.setattr(bc, "load_ours", lambda *a, **k: ours)
    monkeypatch.setattr(bc, "REGISTRY", {"fake_min": LabelledMinerals(),
                                         "fake_cells": UnlabelledCells()})
    cfg = {
        "version": "corpus_test", "out_dir": str(tmp_path / "corpus"),
        "raw_dir": str(tmp_path / "raw"), "cache_dir": str(tmp_path / "cache"),
        "our_data_dir": "unused", "seed": 0, "device": "cpu",
        "leakage_cos_threshold": 0.999, "probe_fraction": 0.4,
        "probe_test_fraction": 0.5, "min_probe_class_spectra": 5,
        "sources": [{"name": "fake_min", "probe": True, "max_per_sample": None},
                    {"name": "fake_cells", "probe": False, "max_per_sample": 10}],
    }
    manifest = bc.build(cfg)
    out = tmp_path / "corpus"
    meta = pd.read_parquet(out / "meta.parquet")
    return manifest, out, meta


def test_artefacts_are_consistent(built):
    manifest, out, meta = built
    S = np.load(out / "spectra.npy")
    M = np.load(out / "mask.npy")
    assert S.dtype == np.float16 and S.shape == (len(meta), 1001)
    assert M.dtype == bool and M.shape == S.shape
    splits = json.loads((out / "splits.json").read_text())
    assert sum(len(v) for v in splits.values()) == len(meta)
    assert set(meta.columns) == {"source", "domain", "laser_nm", "sample_id",
                                 "label", "split", "sample_weight"}


def test_planted_copy_of_our_data_is_removed(built):
    manifest, _, meta = built
    assert manifest["sources"]["fake_cells"]["n_leaked"] == 1
    assert "planted" not in set(meta["sample_id"])


def test_flat_spectrum_is_dropped_and_duplicate_removed(built):
    manifest, _, meta = built
    src = manifest["sources"]["fake_min"]
    assert src["n_unusable"] == 1
    assert src["n_duplicate"] == 1
    assert (meta["source"] == "fake_min").sum() == 60


def test_per_sample_cap_is_respected(built):
    manifest, _, meta = built
    cells = meta[meta["source"] == "fake_cells"]
    assert (cells["sample_id"] == "map_big").sum() == 10
    assert (cells["sample_id"] == "map_small").sum() == 5
    assert manifest["sources"]["fake_cells"]["n_capped"] == 20


def test_probe_groups_never_shared_with_pretrain_or_each_other(built):
    _, _, meta = built
    probe = meta[meta["split"] != "pretrain"]
    assert len(probe) > 0
    by_split = {s: set(meta.loc[meta["split"] == s, "sample_id"]) for s in
                ("pretrain", "probe_train", "probe_test")}
    assert not by_split["probe_train"] & by_split["probe_test"]
    assert not (by_split["probe_train"] | by_split["probe_test"]) & by_split["pretrain"]


def test_labels_are_strings_or_null(built):
    _, _, meta = built
    mins = meta[meta["source"] == "fake_min"]["label"]
    assert set(mins) == {"0", "1", "2"}
    assert meta[meta["source"] == "fake_cells"]["label"].isna().all()


def test_sampling_weights_follow_sqrt_n(built):
    _, _, meta = built
    pre = meta[meta["split"] == "pretrain"]
    assert meta.loc[meta["split"] != "pretrain", "sample_weight"].eq(0).all()
    assert pre["sample_weight"].sum() == pytest.approx(1.0)
    totals = pre.groupby("source")["sample_weight"].sum()
    counts = pre.groupby("source").size()
    ratio = totals / np.sqrt(counts)
    assert ratio.max() == pytest.approx(ratio.min())


class NeedsManualDownload:
    name, domain, licence, url, probe_label_kind = "manual_src", "bio", "?", "z", None

    def download(self, raw_dir):
        from foundation.data.sources.base import ManualDownloadRequired
        raise ManualDownloadRequired("put files in raw/manual_src")

    def iter_batches(self, raw_dir):
        raise AssertionError("must not be called")


def _cfg(tmp_path, sources):
    return {"version": "t", "out_dir": str(tmp_path / "c2"), "raw_dir": str(tmp_path / "raw"),
            "cache_dir": str(tmp_path / "cache"), "our_data_dir": "unused", "seed": 0,
            "device": "cpu", "leakage_cos_threshold": 0.999, "probe_fraction": 0.4,
            "probe_test_fraction": 0.5, "min_probe_class_spectra": 5, "sources": sources}


def test_optional_manual_source_is_skipped_and_recorded(tmp_path, monkeypatch):
    our_S, our_M = harmonize_many(OUR_AXIS, _our_raw())
    ours = {n: (our_S, our_M, np.zeros(len(our_S))) for n in
            ("reference", "finetune", "test", "2018clinical", "2019clinical")}
    monkeypatch.setattr(bc, "load_ours", lambda *a, **k: ours)
    monkeypatch.setattr(bc, "REGISTRY", {"fake_min": LabelledMinerals(),
                                         "manual_src": NeedsManualDownload()})
    manifest = bc.build(_cfg(tmp_path, [
        {"name": "fake_min", "probe": True},
        {"name": "manual_src", "probe": False, "optional": True}]))
    assert manifest["sources"]["manual_src"]["status"].startswith("skipped")
    assert manifest["sources"]["fake_min"]["status"] == "ok"


def test_required_manual_source_fails_the_build(tmp_path, monkeypatch):
    our_S, our_M = harmonize_many(OUR_AXIS, _our_raw())
    ours = {n: (our_S, our_M, np.zeros(len(our_S))) for n in
            ("reference", "finetune", "test", "2018clinical", "2019clinical")}
    monkeypatch.setattr(bc, "load_ours", lambda *a, **k: ours)
    monkeypatch.setattr(bc, "REGISTRY", {"manual_src": NeedsManualDownload()})
    from foundation.data.sources.base import ManualDownloadRequired
    with pytest.raises(ManualDownloadRequired):
        bc.build(_cfg(tmp_path, [{"name": "manual_src", "probe": False}]))


def test_raw_fingerprint_changes_when_files_change(tmp_path):
    d = tmp_path / "raw" / "src"
    assert bc.raw_fingerprint(d) is None
    d.mkdir(parents=True)
    (d / "a.txt").write_text("1")
    first = bc.raw_fingerprint(d)
    assert first == bc.raw_fingerprint(d)
    (d / "a.txt").write_text("12")
    assert bc.raw_fingerprint(d) != first


def test_assign_splits_is_deterministic_and_skips_small_classes():
    source = np.array(["a"] * 12 + ["a"] * 4, dtype=object)
    label = np.array(["x"] * 12 + ["y"] * 4, dtype=object)
    sample = np.array([f"s{i // 2}" for i in range(12)] + ["t0", "t0", "t1", "t1"], dtype=object)
    args = dict(probe_sources={"a"}, probe_fraction=0.5, probe_test_fraction=0.5,
                min_class_spectra=2, seed=3)
    s1 = bc.assign_splits(source, label, sample, **args)
    s2 = bc.assign_splits(source, label, sample, **args)
    assert (s1 == s2).all()
    assert (s1[12:] == "pretrain").all()            # class y has only 2 groups
    assert set(s1[:12]) == {"pretrain", "probe_train", "probe_test"}
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_build_corpus.py -v`
Expected: collection error, `ImportError` (no module `foundation.data.build_corpus`).

- [ ] **Step 3: Write the implementation**

`foundation/data/build_corpus.py`:
```python
"""Build the pretraining corpus for model A (spec section 4).

    python -m foundation.data.build_corpus --config foundation/configs/corpus_v1.yaml

Pipeline: per source -> harmonise -> drop unusable -> leakage guard against
ALL our Bacteria-ID spectra -> per-sample cap; then corpus-wide exact
de-duplication -> probe/pretrain split by sample -> probe isolation (drop
pretrain near-duplicates of probe spectra) -> sqrt(n) sampling weights ->
write artefacts + manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from .harmonize import (GRID_START, GRID_STEP, GRID_STOP, HARMONIZE_VERSION, N_GRID,
                        harmonize_many, is_usable)
from .leakage import LeakageGuard, spectrum_hash
from .sources import REGISTRY, ManualDownloadRequired
from .tasks import load_ours


def cap_per_sample(sample_ids, max_per_sample, rng):
    sample_ids = np.asarray(sample_ids, dtype=object)
    keep = np.ones(sample_ids.size, dtype=bool)
    for sid in np.unique(sample_ids):
        rows = np.flatnonzero(sample_ids == sid)
        if rows.size > max_per_sample:
            drop = rng.choice(rows, size=rows.size - max_per_sample, replace=False)
            keep[drop] = False
    return keep


def assign_splits(source, label, sample_id, probe_sources, probe_fraction,
                  probe_test_fraction, min_class_spectra, seed):
    """Probe slice per (source, class), split by sample group. Classes with
    fewer than 3 groups, or too few spectra, stay in pretrain."""
    split = np.full(len(source), "pretrain", dtype=object)
    rng = np.random.default_rng(seed)
    labelled = np.array([v is not None for v in label], dtype=bool)
    for src in sorted(probe_sources):
        in_src = (source == src) & labelled
        for cls in sorted(set(label[in_src])):
            rows = np.flatnonzero(in_src & (label == cls))
            groups = np.array(sorted(set(sample_id[rows])), dtype=object)
            if groups.size < 3:
                continue
            rng.shuffle(groups)
            n_probe = max(2, int(round(probe_fraction * groups.size)))
            probe_groups = groups[:n_probe]
            n_test = max(1, int(round(probe_test_fraction * n_probe)))
            test_g = list(probe_groups[:n_test])
            train_g = list(probe_groups[n_test:])
            te = rows[np.isin(sample_id[rows], test_g)]
            tr = rows[np.isin(sample_id[rows], train_g)]
            if tr.size + te.size < min_class_spectra:
                continue
            split[tr] = "probe_train"
            split[te] = "probe_test"
    return split


def sampling_weights(source, split):
    w = np.zeros(len(source), dtype=np.float64)
    pre = split == "pretrain"
    for src in np.unique(source[pre]):
        rows = pre & (source == src)
        w[rows] = rows.sum() ** -0.5            # per-source total = sqrt(n)
    total = w.sum()
    return w / total if total > 0 else w


def _git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return None


def raw_fingerprint(directory):
    """sha256 over (relative path, size) of every downloaded file, so a manifest
    pins exactly which raw files built the corpus without hashing gigabytes."""
    directory = Path(directory)
    if not directory.exists():
        return None
    h = hashlib.sha256()
    for p in sorted(q for q in directory.rglob("*") if q.is_file()):
        h.update(f"{p.relative_to(directory).as_posix()}\t{p.stat().st_size}\n".encode())
    return h.hexdigest()


def _native_range(axes):
    if isinstance(axes, np.ndarray) and axes.ndim == 1:
        return float(np.nanmin(axes)), float(np.nanmax(axes))
    lo = min(float(np.nanmin(a)) for a in axes)
    hi = max(float(np.nanmax(a)) for a in axes)
    return lo, hi


def build(cfg: dict) -> dict:
    out_dir, raw_dir = Path(cfg["out_dir"]), Path(cfg["raw_dir"])
    rng = np.random.default_rng(cfg["seed"])
    device = cfg.get("device")

    ours = load_ours(cfg["our_data_dir"], cfg.get("cache_dir", "foundation/data/cache"))
    our_X = np.concatenate([v[0] for v in ours.values()])
    our_M = np.concatenate([v[1] for v in ours.values()])
    guard = LeakageGuard(our_X, our_M, cos_threshold=cfg["leakage_cos_threshold"],
                         device=device)

    S_parts, M_parts, meta_parts, stats = [], [], [], {}
    for entry in cfg["sources"]:
        src = REGISTRY[entry["name"]]
        st = {"status": "ok", "domain": src.domain, "licence": src.licence, "url": src.url,
              "label_kind": src.probe_label_kind, "n_raw": 0, "n_unusable": 0,
              "n_leaked": 0, "n_capped": 0, "native_min": None, "native_max": None,
              "lasers": set()}
        stats[src.name] = st
        try:
            src.download(raw_dir / src.name)
        except ManualDownloadRequired as e:
            if not entry.get("optional"):
                raise
            st["status"] = f"skipped: {e}"
            print(f"[corpus] {src.name}: {st['status']}")
            continue
        st["raw_fingerprint"] = raw_fingerprint(raw_dir / src.name)
        for batch in src.iter_batches(raw_dir / src.name):
            S, M = harmonize_many(batch.axes, batch.spectra)
            lo, hi = _native_range(batch.axes)
            st["native_min"] = lo if st["native_min"] is None else min(lo, st["native_min"])
            st["native_max"] = hi if st["native_max"] is None else max(hi, st["native_max"])
            st["lasers"].update(float(v) for v in np.unique(batch.laser_nm) if np.isfinite(v))
            st["n_raw"] += len(S)
            keep = np.array([is_usable(s, m) for s, m in zip(S, M)], dtype=bool)
            st["n_unusable"] += int((~keep).sum())
            idx = np.flatnonzero(keep)
            leaked = guard.find(S[idx], M[idx])
            keep[idx[leaked]] = False
            st["n_leaked"] += int(leaked.sum())
            sample_id = np.asarray(batch.sample_id, dtype=object)
            if entry.get("max_per_sample"):
                idx = np.flatnonzero(keep)
                capped = cap_per_sample(sample_id[idx], entry["max_per_sample"], rng)
                keep[idx[~capped]] = False
                st["n_capped"] += int((~capped).sum())
            S_parts.append(S[keep].astype(np.float16))
            M_parts.append(M[keep])
            meta_parts.append(pd.DataFrame({
                "source": src.name, "domain": src.domain,
                "laser_nm": batch.laser_nm[keep], "sample_id": sample_id[keep],
                "label": np.asarray(batch.label, dtype=object)[keep],
            }))

    if not S_parts:
        raise RuntimeError("no source produced any spectra; nothing to build")
    S = np.concatenate(S_parts)
    M = np.concatenate(M_parts)
    meta = pd.concat(meta_parts, ignore_index=True)

    # corpus-wide exact de-duplication (keep first occurrence)
    hashes = np.array([spectrum_hash(s.astype(np.float32), m) for s, m in zip(S, M)])
    _, first = np.unique(hashes, return_index=True)
    unique = np.zeros(len(S), dtype=bool)
    unique[first] = True
    for name in stats:
        stats[name]["n_duplicate"] = int(((meta["source"] == name).to_numpy() & ~unique).sum())
    S, M, meta = S[unique], M[unique], meta[unique].reset_index(drop=True)

    source = meta["source"].to_numpy(dtype=object)
    label = meta["label"].to_numpy(dtype=object)
    sample_id = meta["sample_id"].to_numpy(dtype=object)
    probe_sources = {e["name"] for e in cfg["sources"] if e.get("probe")}
    split = assign_splits(source, label, sample_id, probe_sources, cfg["probe_fraction"],
                          cfg["probe_test_fraction"], cfg["min_probe_class_spectra"],
                          cfg["seed"])

    # probe isolation: no pretrain spectrum may near-duplicate a probe spectrum
    probe_rows = np.flatnonzero(split != "pretrain")
    pre_rows = np.flatnonzero(split == "pretrain")
    drop = np.zeros(len(S), dtype=bool)
    if probe_rows.size and pre_rows.size:
        pguard = LeakageGuard(S[probe_rows].astype(np.float32), M[probe_rows],
                              cos_threshold=cfg["leakage_cos_threshold"], device=device)
        drop[pre_rows[pguard.find(S[pre_rows], M[pre_rows])]] = True
    for name in stats:
        stats[name]["n_probe_isolation"] = int(((source == name) & drop).sum())
    S, M, meta, split = S[~drop], M[~drop], meta[~drop].reset_index(drop=True), split[~drop]
    source = meta["source"].to_numpy(dtype=object)

    meta["split"] = split
    meta["sample_weight"] = sampling_weights(source, split)
    for name, st in stats.items():
        rows = source == name
        st["lasers"] = sorted(st["lasers"])
        for s in ("pretrain", "probe_train", "probe_test"):
            st[f"n_{s}"] = int((rows & (split == s)).sum())

    out_dir.mkdir(parents=True, exist_ok=True)
    np.save(out_dir / "spectra.npy", S)
    np.save(out_dir / "mask.npy", M)
    meta.to_parquet(out_dir / "meta.parquet", index=False)
    splits = {s: np.flatnonzero(split == s).tolist()
              for s in ("pretrain", "probe_train", "probe_test")}
    (out_dir / "splits.json").write_text(json.dumps(splits))
    manifest = {
        "version": cfg["version"], "git_sha": _git_sha(),
        "harmonize_version": HARMONIZE_VERSION,
        "grid": {"start": GRID_START, "stop": GRID_STOP, "step": GRID_STEP, "n": N_GRID},
        "config": cfg, "sources": stats,
        "totals": {s: len(v) for s, v in splits.items()},
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, default=str))
    return manifest


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True)
    args = ap.parse_args(argv)
    cfg = yaml.safe_load(Path(args.config).read_text())
    manifest = build(cfg)
    print(json.dumps(manifest["totals"], indent=2))
    print(f"wrote {cfg['out_dir']}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_build_corpus.py -v`
Expected: 11 passed.

If `test_flat_spectrum_is_dropped_and_duplicate_removed` fails on the count of 60, print `manifest["sources"]["fake_min"]` to see which stage removed the extra rows. The 60 rows are the 3 × 5 × 4 synthetic spectra; only the flat spectrum and the duplicate may be removed. A minority of the 60 may move to probe splits, but they stay in `meta`. Probe isolation must not remove any of them, because their noise makes them distinct at cosine 0.999. If it does remove some, the synthetic spectra are too similar: increase the noise in `LabelledMinerals` to `rng.normal(0, 0.03, ...)`. Don't loosen the threshold.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/build_corpus.py tests/foundation/test_build_corpus.py
git commit -m "foundation: corpus builder with leakage guard, caps, dedup, probe split"
```

---

### Task 6: Audit and the G0 decision

**Files:**
- Create: `foundation/data/audit.py`
- Test: `tests/foundation/test_audit.py`

**Interfaces:**
- Consumes: `manifest.json` from Task 5.
- Produces:
  - `summarize(corpus_dir) -> (pd.DataFrame, dict)`. The DataFrame has one row per source with the columns `status`, `domain`, `n_raw`, `n_unusable`, `n_leaked`, `n_capped`, `n_duplicate`, `n_probe_isolation`, `n_pretrain`, `n_probe_train`, `n_probe_test`, `native_min`, `native_max`, `lasers`, `licence`. The dict is `manifest["totals"]`.
  - `main(argv=None) -> int`, the CLI `python -m foundation.data.audit --corpus <dir> [--min-pretrain 150000]`. It prints the table and `G0 PASS ...` or `G0 FAIL ...`, and returns exit code 0 or 1.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_audit.py`:
```python
import json

from foundation.data import audit


def _write_manifest(path, n_pretrain):
    src = {"domain": "bio", "n_raw": n_pretrain + 10, "n_unusable": 5, "n_leaked": 1,
           "n_capped": 0, "n_duplicate": 2, "n_probe_isolation": 0,
           "n_pretrain": n_pretrain, "n_probe_train": 1, "n_probe_test": 1,
           "native_min": 500.0, "native_max": 1800.0, "lasers": [532.0], "licence": "CC-BY"}
    path.mkdir()
    (path / "manifest.json").write_text(json.dumps({
        "sources": {"cells": src},
        "totals": {"pretrain": n_pretrain, "probe_train": 1, "probe_test": 1}}))


def test_g0_passes_at_threshold(tmp_path, capsys):
    _write_manifest(tmp_path / "c", 150_000)
    assert audit.main(["--corpus", str(tmp_path / "c")]) == 0
    assert "G0 PASS" in capsys.readouterr().out


def test_g0_fails_below_threshold(tmp_path, capsys):
    _write_manifest(tmp_path / "c", 149_999)
    assert audit.main(["--corpus", str(tmp_path / "c")]) == 1
    out = capsys.readouterr().out
    assert "G0 FAIL" in out and "cells" in out


def test_summarize_has_one_row_per_source(tmp_path):
    _write_manifest(tmp_path / "c", 10)
    table, totals = audit.summarize(tmp_path / "c")
    assert list(table.index) == ["cells"] and totals["pretrain"] == 10
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_audit.py -v`
Expected: collection error, `ImportError` (no module `foundation.data.audit`).

- [ ] **Step 3: Write the implementation**

`foundation/data/audit.py`:
```python
"""Phase 0 audit and gate G0 (spec section 7).

    python -m foundation.data.audit --corpus foundation/data/corpus_v1
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

COLUMNS = ["status", "domain", "n_raw", "n_unusable", "n_leaked", "n_capped", "n_duplicate",
           "n_probe_isolation", "n_pretrain", "n_probe_train", "n_probe_test",
           "native_min", "native_max", "lasers", "licence"]


def summarize(corpus_dir):
    manifest = json.loads((Path(corpus_dir) / "manifest.json").read_text())
    table = pd.DataFrame.from_dict(manifest["sources"], orient="index")
    table = table.reindex(columns=COLUMNS)
    return table, manifest["totals"]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--min-pretrain", type=int, default=150_000)
    args = ap.parse_args(argv)
    table, totals = summarize(args.corpus)
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(table.to_string())
    print(f"\ntotals: {totals}")
    n = totals["pretrain"]
    if n >= args.min_pretrain:
        print(f"G0 PASS: {n:,} pretraining spectra >= {args.min_pretrain:,}")
        return 0
    print(f"G0 FAIL: {n:,} pretraining spectra < {args.min_pretrain:,}. "
          "Stop and revisit the source list (spec section 7).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_audit.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/audit.py tests/foundation/test_audit.py
git commit -m "foundation: corpus audit and G0 gate"
```

---

### Task 7: RRUFF adapter

**Files:**
- Create: `foundation/data/sources/rruff.py`
- Modify: `foundation/data/sources/__init__.py` (append an import)
- Test: `tests/foundation/test_source_rruff.py`

**Interfaces:**
- Consumes: `RawBatch`, `fetch`, `register` (Task 4); `AXIS_MIN`, `AXIS_MAX` (Task 1).
- Produces:
  - A registered source `"rruff"` (domain `mineral`, probe-capable; the label is the mineral name; the group is the RRUFF ID without its `-n` suffix).
  - `parse_rruff_text(text) -> (header: dict, x, y)`.
  - `parse_laser(*candidates) -> float` (NaN if no candidate parses).
  - `parse_filename(name) -> dict | None`.

Verified format facts:
- **Location:** `https://www.rruff.net/zipped_data_files/raman/` (the version without `www` times out). The server drops connections intermittently.
- **Archives:** flat `.txt` files, no subfolders.
- **Filename:** 8 fields separated by `__`: `Mineral__RRUFFID[-n]__{Raman|Broad_Scan}__LASER__ORIENT__POL__Raman_Data_{Processed|RAW|Raw}__hash.txt`.
- **Content:**
  - `##KEY=value` header lines, then `x, y` rows, ending in `##END=`.
  - CRLF line endings and `E+00` notation.
  - Some files are UTF-8.
- **Laser values are messy:** `514-5`, `632-8`, `532SP9`, `532nm`, `53`, and empty strings all occur.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_rruff.py`:
```python
import math
import zipfile

import numpy as np

from foundation.data.sources import REGISTRY
from foundation.data.sources.rruff import parse_laser, parse_rruff_text


def _txt(header, xs, ys):
    lines = [f"##{k}={v}" for k, v in header.items()] + [""]
    lines += [f"{x:.4f}, {y:.7E}" for x, y in zip(xs, ys)] + ["##END="]
    return "\r\n".join(lines) + "\r\n"


def _make_zips(raw):
    raw.mkdir(parents=True)
    x = np.linspace(100.0, 1500.0, 800)
    corundum = _txt({"NAMES": "Corundum", "RRUFFID": "R060020", "RAMAN WAVELENGTH": "514"},
                    x, 1 + np.exp(-0.5 * ((x - 417) / 4) ** 2))
    with zipfile.ZipFile(raw / "excellent_unoriented.zip", "w") as zf:
        zf.writestr("Corundum__R060020-4__Raman__514__0-000____Raman_Data_RAW__5210.txt", corundum)
        zf.writestr("Corundum__R060020-4__Raman__514__0-000____Raman_Data_Processed__5211.txt",
                    corundum)
    with zipfile.ZipFile(raw / "fair_unoriented.zip", "w"):
        pass
    quartz = _txt({"NAMES": "Quartz"}, x, 1 + np.exp(-0.5 * ((x - 465) / 4) ** 2))
    bogus_x = np.linspace(11000.0, 12000.0, 300)
    bogus = _txt({"NAMES": "Bogus", "RRUFFID": "R1"}, bogus_x, np.ones_like(bogus_x))
    with zipfile.ZipFile(raw / "LR-Raman.zip", "w") as zf:
        zf.writestr("Quartz__R040031__Broad_Scan__532SP9__0____Raman_Data_Raw__9999.txt", quartz)
        zf.writestr("Bogus__R1__Raman__532__0____Raman_Data_RAW__1.txt", bogus)


def test_parse_text_reads_header_and_rows_until_end():
    text = _txt({"NAMES": "Corundum", "RRUFFID": "R060020"}, [100.0, 101.5], [3.0, 0.0])
    header, x, y = parse_rruff_text(text + "999, 999\r\n")
    assert header["NAMES"] == "Corundum"
    assert x.tolist() == [100.0, 101.5] and y.tolist() == [3.0, 0.0]


def test_parse_laser_handles_messy_values():
    assert parse_laser("632-8") == 632.0
    assert parse_laser("532nm") == 532.0
    assert parse_laser("", "785") == 785.0
    assert math.isnan(parse_laser("53", ""))


def test_iter_batches_keeps_raw_only_and_skips_implausible_axes(tmp_path):
    raw = tmp_path / "rruff"
    _make_zips(raw)
    (batch,) = list(REGISTRY["rruff"].iter_batches(raw))
    assert batch.label == ["Corundum", "Quartz"]
    assert batch.sample_id == ["R060020", "R040031"]
    assert batch.laser_nm.tolist() == [514.0, 532.0]
    assert np.all(np.diff(batch.axes[0]) > 0)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_rruff.py -v`
Expected: `ImportError` (no module `foundation.data.sources.rruff`).

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/rruff.py`:
```python
"""RRUFF mineral spectra (spec section 4.1; plan deviation D4).

https://www.rruff.net/zipped_data_files/raman/ : flat .txt files named
Mineral__RRUFFID[-n]__{Raman|Broad_Scan}__LASER__ORIENT__POL__Raman_Data_{Processed|RAW|Raw}__hash.txt
with '##KEY=value' headers, 'x, y' rows and a final '##END='.

Only RAW files are kept: every specimen also ships a Processed copy, which is
baseline-corrected (spec: no baseline correction) and would duplicate it.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

import numpy as np

from ..harmonize import AXIS_MAX, AXIS_MIN
from .base import RawBatch, fetch, register

BASE_URL = "https://www.rruff.net/zipped_data_files/raman/"
ZIPS = ("excellent_unoriented.zip", "fair_unoriented.zip", "LR-Raman.zip")
_LASER = re.compile(r"(\d{3})")
_SPLIT = re.compile(r"[,\s]+")


def parse_rruff_text(text):
    header, xs, ys = {}, [], []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("##"):
            key, _, val = line[2:].partition("=")
            if key.strip() == "END":
                break
            header[key.strip()] = val.strip()
            continue
        parts = [p for p in _SPLIT.split(line) if p]
        if len(parts) < 2:
            continue
        try:
            x, y = float(parts[0]), float(parts[1])
        except ValueError:
            continue
        xs.append(x)
        ys.append(y)
    return header, np.asarray(xs), np.asarray(ys)


def parse_laser(*candidates):
    for c in candidates:
        m = _LASER.search(c or "")
        if m:
            return float(m.group(1))
    return float("nan")


def parse_filename(name):
    fields = Path(name).name.split("__")
    if len(fields) != 8:
        return None
    return {"mineral": fields[0], "rruff_id": fields[1], "laser": fields[3],
            "data_type": fields[6]}


class RRUFF:
    name = "rruff"
    domain = "mineral"
    licence = "CC BY-SA 4.0 per FAIRsharing (RRUFF's own terms unclear); cite Lafuente et al. 2015"
    url = BASE_URL
    probe_label_kind = "mineral species"

    def download(self, raw_dir):
        for z in ZIPS:
            fetch(BASE_URL + z, Path(raw_dir) / z, retries=5)

    def iter_batches(self, raw_dir):
        axes, spectra, ids, labels, lasers = [], [], [], [], []
        for z in ZIPS:
            with zipfile.ZipFile(Path(raw_dir) / z) as zf:
                for member in zf.namelist():
                    info = parse_filename(member)
                    if (not member.lower().endswith(".txt") or info is None
                            or not info["data_type"].lower().endswith("_raw")):
                        continue
                    header, x, y = parse_rruff_text(zf.read(member).decode("utf-8", "replace"))
                    if x.size < 2 or x.min() < AXIS_MIN or x.max() > AXIS_MAX:
                        continue
                    rid = header.get("RRUFFID") or info["rruff_id"]
                    axes.append(x)
                    spectra.append(y)
                    ids.append(re.sub(r"-\d+$", "", rid))
                    labels.append(header.get("NAMES") or info["mineral"])
                    lasers.append(parse_laser(header.get("RAMAN WAVELENGTH"), info["laser"]))
        yield RawBatch(axes=axes, spectra=spectra, sample_id=ids, label=labels, laser_nm=lasers)


register(RRUFF())
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import rruff  # noqa: E402,F401
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_rruff.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/rruff.py foundation/data/sources/__init__.py tests/foundation/test_source_rruff.py
git commit -m "foundation: RRUFF source adapter (RAW files only)"
```

---

### Task 8: Pharmaceutical API adapter

**Files:**
- Create: `foundation/data/sources/api_flanagan.py`
- Modify: `foundation/data/sources/__init__.py` (append an import)
- Test: `tests/foundation/test_source_api.py`

**Interfaces:**
- Consumes: `RawBatch`, `fetch`, `register` (Task 4).
- Produces:
  - A registered source `"api_flanagan"` (domain `chem`, 785 nm, pretrain-only per deviation D3).
  - `parse_api_csv(path) -> (axis, X, labels)`.

Verified format facts:
- **File:** `raman_spectra_api_compounds.csv` (193,164,182 bytes) at `https://ndownloader.figshare.com/files/50881917`. Licence CC BY 4.0.
- **Layout:** wide. The header is `150.0,151.0,…,3425.0,label` (3,276 wavenumber columns), and there's one row per spectrum.
- **Labels:** the compound name. Some contain commas and are quoted.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_api.py`:
```python
import numpy as np

from foundation.data.sources import REGISTRY
from foundation.data.sources.api_flanagan import FILENAME, parse_api_csv


def _write_csv(path):
    axis = np.arange(150.0, 1650.0, 1.0)
    header = ",".join(f"{v:.1f}" for v in axis) + ",label"
    rows = []
    for name in ('"1,3-Dimethyl-2-imidazolidinone"', "Toluene"):
        rows.append(",".join(f"{v:.3f}" for v in 1 + np.sin(axis / 50)) + "," + name)
    path.write_text("\n".join([header] + rows) + "\n")


def test_parse_wide_csv_with_quoted_labels(tmp_path):
    _write_csv(tmp_path / FILENAME)
    axis, X, labels = parse_api_csv(tmp_path / FILENAME)
    assert axis[0] == 150.0 and axis.size == 1500
    assert X.shape == (2, 1500)
    assert labels == ["1,3-Dimethyl-2-imidazolidinone", "Toluene"]


def test_iter_batches_groups_by_compound(tmp_path):
    _write_csv(tmp_path / FILENAME)
    (batch,) = list(REGISTRY["api_flanagan"].iter_batches(tmp_path))
    assert batch.sample_id == ["compound:1,3-Dimethyl-2-imidazolidinone", "compound:Toluene"]
    assert batch.laser_nm.tolist() == [785.0, 785.0]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_api.py -v`
Expected: `ImportError` (no module `foundation.data.sources.api_flanagan`).

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/api_flanagan.py`:
```python
"""Pharmaceutical API Raman set, Flanagan et al. 2025 (figshare 27931131, CC BY 4.0).

One wide CSV: header '150.0,...,3425.0,label', one row per spectrum, compound
name in the last column. 785 nm, Kaiser Rxn2. There is no replicate/sample
column, so this source is pretrain-only (plan deviation D3).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .base import RawBatch, fetch, register

URL = "https://ndownloader.figshare.com/files/50881917"
FILENAME = "raman_spectra_api_compounds.csv"


def parse_api_csv(path):
    df = pd.read_csv(path)
    if df.columns[-1] != "label":
        raise ValueError(f"{path}: last column is {df.columns[-1]!r}, expected 'label'")
    axis = np.array([float(c) for c in df.columns[:-1]])
    X = df.iloc[:, :-1].to_numpy(dtype=np.float64)
    return axis, X, df["label"].astype(str).tolist()


class APIFlanagan:
    name = "api_flanagan"
    domain = "chem"
    licence = "CC BY 4.0"
    url = "https://doi.org/10.6084/m9.figshare.27931131"
    probe_label_kind = "compound"

    def download(self, raw_dir):
        fetch(URL, Path(raw_dir) / FILENAME, retries=5)

    def iter_batches(self, raw_dir):
        axis, X, labels = parse_api_csv(Path(raw_dir) / FILENAME)
        yield RawBatch(axes=axis, spectra=X, sample_id=[f"compound:{l}" for l in labels],
                       label=labels, laser_nm=785)


register(APIFlanagan())
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import api_flanagan  # noqa: E402,F401
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_api.py -v`
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/api_flanagan.py foundation/data/sources/__init__.py tests/foundation/test_source_api.py
git commit -m "foundation: pharmaceutical API source adapter"
```

---

### Task 9: Airborne-pathogen adapter

**Files:**
- Create: `foundation/data/sources/airborne.py`
- Modify: `foundation/data/sources/__init__.py` (append an import)
- Test: `tests/foundation/test_source_airborne.py`

**Interfaces:**
- Consumes: `RawBatch`, `fetch`, `register` (Task 4).
- Produces:
  - A registered source `"airborne"` (domain `bio`, 532 nm, probe-capable: the label is the species folder, the group is the file, i.e. one cell).
  - `local_relpath(url) -> str`.
  - `classify(relpath) -> (keep: bool, label: str | None)`.
  - `SPECIES` tuple.

Verified format facts:
- **No bundle.** The ScienceDB API `getAllUrl?dataSetId=5a1b7adb362d4064a3dedd01e5c40d90&type=&version=V1&global=` returns one direct URL per line, in the form `https://download.scidb.cn/download?fileId=…&path=…&fileName=…`.
- **Paths:** they contain `&` and `'`.
- **Files:** each file is one cell, 225 rows of `x y`, space-separated, CRLF, `%.18e`. The axis runs 608–1802.67 at about 5.33 cm⁻¹.
- **Labels:** the species name comes from the folder (`A.baylyi`, `E.coli`, `P.aeruginosa`, `S.aureus`, `S.enterica`). The `Others`, `unknown`, `Unknown` and `Test_set_4` real-air folders are unlabelled.
- **Exclusions:** `Test_set_3/Unknown` holds 12,200 augmented `U_aug_ N.txt` files, which are excluded.
- **Licence:** CC BY-NC 4.0.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_airborne.py`:
```python
import numpy as np

from foundation.data.sources import REGISTRY
from foundation.data.sources.airborne import classify, local_relpath


def test_local_relpath_handles_ampersand_and_apostrophe():
    url = ("https://download.scidb.cn/download?fileId=abc&path=%2FTraining_set_2%26Test_set_2"
           "%2Fnew_data%2Funknown%27&fileName=7.txt")
    assert local_relpath(url) == "Training_set_2&Test_set_2/new_data/unknown'/7.txt"


def test_local_relpath_handles_unencoded_ampersand_in_path():
    url = ("https://download.scidb.cn/download?fileId=abc&path=/Training_set_1&Test_set_1"
           "/new_data/train_test/E.coli&fileName=12.txt")
    assert local_relpath(url) == "Training_set_1&Test_set_1/new_data/train_test/E.coli/12.txt"


def test_local_relpath_does_not_repeat_filename_already_in_path():
    url = "https://download.scidb.cn/download?fileId=x&path=%2Fa%2Fb%2F3.txt&fileName=3.txt"
    assert local_relpath(url) == "a/b/3.txt"


def test_classify_labels_species_and_drops_augmented():
    assert classify("Training_set_1&Test_set_1/new_data/train_test/E.coli/1.txt") == (True, "E.coli")
    assert classify("Test_set_3/Pathogen/S.aureus/5.txt") == (True, "S.aureus")
    assert classify("Training_set_1&Test_set_1/new_data/train_test/Others/2.txt") == (True, None)
    assert classify("Test_set_3/Unknown/U_aug_ 12.txt") == (False, None)
    assert classify("Test_set_4/readme.md") == (False, None)


def test_iter_batches_reads_listed_files(tmp_path):
    rows = "\r\n".join(f"{x:.18e} {y:.18e}" for x, y in
                       zip(np.linspace(608, 1802.67, 225), np.linspace(0, 1, 225)))
    files = {"Test_set_3/Pathogen/S.aureus/5.txt": rows,
             "Training_set_1&Test_set_1/new_data/train_test/Others/2.txt": rows,
             "Test_set_3/Unknown/U_aug_ 12.txt": rows}
    urls = []
    for rel, content in files.items():
        p = tmp_path / "files" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        folder, name = rel.rsplit("/", 1)
        urls.append(f"https://download.scidb.cn/download?fileId=1&path=/{folder}&fileName={name}")
    (tmp_path / "urls.txt").write_text("\n".join(urls))
    (batch,) = list(REGISTRY["airborne"].iter_batches(tmp_path))
    assert batch.label == ["S.aureus", None]
    assert batch.sample_id[0] == "Test_set_3/Pathogen/S.aureus/5.txt"
    assert batch.axes[0].size == 225
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_airborne.py -v`
Expected: `ImportError` (no module `foundation.data.sources.airborne`).

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/airborne.py`:
```python
"""Airborne pathogens, single-cell Raman (Sci. Adv. 2025; ScienceDB
10.57760/sciencedb.15628; CC BY-NC 4.0). 532 nm, LabRAM Aramis.

No bundle: one direct URL per file from the ScienceDB file-tree API. Each file
is one cell: 225 rows 'x y', axis 608-1802.67 cm^-1 at ~5.33 cm^-1. The
source already baseline-corrected and min-max scaled these (plan deviation
D2). Test_set_3/Unknown ('U_aug_ N.txt') holds augmented/blended spectra and
is excluded.
"""
from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import unquote

import numpy as np

from .base import RawBatch, fetch, register

DATASET_ID = "5a1b7adb362d4064a3dedd01e5c40d90"
LIST_URL = ("https://www.scidb.cn/api/sdb-filetree-service/getAllUrl"
            f"?dataSetId={DATASET_ID}&type=&version=V1&global=")
SPECIES = ("A.baylyi", "E.coli", "P.aeruginosa", "S.aureus", "S.enterica")
# 'path' may contain a raw '&' (e.g. 'Training_set_1&Test_set_1'), so a normal
# query-string parser would cut it short. fileName is always the last parameter.
_PATH_NAME = re.compile(r"[?&]path=(?P<path>.*)&fileName=(?P<name>[^&]*)$")


def local_relpath(url):
    m = _PATH_NAME.search(url.strip())
    if not m:
        raise ValueError(f"unexpected download URL: {url}")
    path, name = unquote(m.group("path")), unquote(m.group("name"))
    parts = [p for p in path.replace("\\", "/").split("/") if p]
    if parts and parts[-1] == name:
        parts = parts[:-1]
    return "/".join(parts + [name])


def classify(relpath):
    parts = relpath.split("/")
    name = parts[-1]
    if not name.lower().endswith(".txt"):
        return False, None
    if "U_aug" in name or ("Test_set_3" in parts and "Unknown" in parts):
        return False, None
    label = next((p for p in parts[:-1] if p in SPECIES), None)
    return True, label


def _kept(raw_dir):
    lines = (Path(raw_dir) / "urls.txt").read_text(encoding="utf-8").splitlines()
    for url in (u.strip() for u in lines):
        if not url:
            continue
        rel = local_relpath(url)
        keep, label = classify(rel)
        if keep:
            yield url, rel, label


class Airborne:
    name = "airborne"
    domain = "bio"
    licence = "CC BY-NC 4.0"
    url = "https://doi.org/10.57760/sciencedb.15628"
    probe_label_kind = "pathogen species"

    def download(self, raw_dir):
        raw_dir = Path(raw_dir)
        fetch(LIST_URL, raw_dir / "urls.txt", retries=5)
        jobs = [(url, raw_dir / "files" / rel) for url, rel, _ in _kept(raw_dir)]
        todo = [(u, p) for u, p in jobs if not p.exists()]
        print(f"[airborne] {len(jobs)} files kept, {len(todo)} to download")
        with ThreadPoolExecutor(max_workers=8) as pool:
            for i, _ in enumerate(pool.map(lambda j: fetch(j[0], j[1], retries=5), todo), 1):
                if i % 1000 == 0:
                    print(f"[airborne] {i}/{len(todo)}")

    def iter_batches(self, raw_dir):
        axes, spectra, ids, labels = [], [], [], []
        for _, rel, label in _kept(raw_dir):
            arr = np.loadtxt(Path(raw_dir) / "files" / rel)
            axes.append(arr[:, 0])
            spectra.append(arr[:, 1])
            ids.append(rel)
            labels.append(label)
        yield RawBatch(axes=axes, spectra=spectra, sample_id=ids, label=labels, laser_nm=532)


register(Airborne())
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import airborne  # noqa: E402,F401
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_airborne.py -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/airborne.py foundation/data/sources/__init__.py tests/foundation/test_source_airborne.py
git commit -m "foundation: airborne-pathogen source adapter"
```

---

### Task 10: Zenodo (Guo) bacteria and oil adapters

**Files:**
- Create: `foundation/data/sources/zenodo_guo.py`
- Modify: `foundation/data/sources/__init__.py` (append an import)
- Test: `tests/foundation/test_source_zenodo.py`

**Interfaces:**
- Consumes: `RawBatch`, `fetch`, `register` (Task 4).
- Produces:
  - Registered sources `"zenodo_bacteria"` (domain `bio`) and `"zenodo_oil"` (domain `chem`). Both are pretrain-only; laser is unknown (NaN).
  - `read_bacteria(zip_path) -> (axis, X, labels, groups)`.
  - `read_oil(zip_path) -> (axis, X, labels, groups)`.

Verified format facts:
- **Files:** `https://zenodo.org/records/15279321/files/Bacterial_data.zip` (30.6 MB) and `…/Oil_data.zip` (4.8 MB). Licence CC BY 4.0.
- **Oil:**
  - `Oil_data/spec.csv` has no header; row 0 is the axis (353–3098, step 3).
  - `Oil_data/metadata.csv` has columns `batches,labels,category` and is row-aligned.
- **Bacteria:**
  - `Bacterial_data/data.csv` is R `write.csv` style: header `"","V1",…`, the first data row is the axis (400–3150, step 2), and later rows are spectra.
  - **Unverified:** the metadata CSV. The authors' code reads `meta_all.csv` with `labels`/`batches` columns (deviation D8).

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_zenodo.py`:
```python
import zipfile

import numpy as np
import pandas as pd
import pytest

from foundation.data.sources import REGISTRY
from foundation.data.sources.zenodo_guo import read_bacteria, read_oil


def _bacteria_zip(path, meta_rows=None):
    axis = np.arange(400.0, 1800.0, 2.0)
    spectra = np.vstack([axis, np.ones((3, axis.size)), 2 * np.ones((1, axis.size))])
    df = pd.DataFrame(spectra, index=[str(i) for i in range(1, 6)],
                      columns=[f"V{i}" for i in range(1, axis.size + 1)])
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("Bacterial_data/data.csv", df.to_csv())
        if meta_rows is not None:
            meta = pd.DataFrame({"labels": ["E.coli"] * meta_rows,
                                 "batches": [f"b{i % 2}" for i in range(meta_rows)]})
            zf.writestr("Bacterial_data/meta_all.csv", meta.to_csv(index=False))


def test_bacteria_with_metadata(tmp_path):
    _bacteria_zip(tmp_path / "Bacterial_data.zip", meta_rows=4)
    axis, X, labels, groups = read_bacteria(tmp_path / "Bacterial_data.zip")
    assert axis[0] == 400.0 and X.shape == (4, axis.size)
    assert labels == ["E.coli"] * 4 and groups == ["b0", "b1", "b0", "b1"]


def test_bacteria_without_metadata_is_unlabelled(tmp_path):
    _bacteria_zip(tmp_path / "Bacterial_data.zip")
    _, X, labels, groups = read_bacteria(tmp_path / "Bacterial_data.zip")
    assert labels == [None] * 4 and set(groups) == {"guo_bacteria"}


def test_bacteria_metadata_row_mismatch_raises(tmp_path):
    _bacteria_zip(tmp_path / "Bacterial_data.zip", meta_rows=3)
    with pytest.raises(ValueError, match="rows"):
        read_bacteria(tmp_path / "Bacterial_data.zip")


def test_oil_and_registered_sources(tmp_path):
    axis = np.arange(353.0, 1900.0, 3.0)
    spec = np.vstack([axis, np.ones((2, axis.size))])
    with zipfile.ZipFile(tmp_path / "Oil_data.zip", "w") as zf:
        zf.writestr("Oil_data/spec.csv", pd.DataFrame(spec).to_csv(header=False, index=False))
        zf.writestr("Oil_data/metadata.csv", "batches,labels,category\nbatch_0,olive,train\n"
                                             "batch_1,olive,test\n")
    axis2, X, labels, groups = read_oil(tmp_path / "Oil_data.zip")
    assert axis2[0] == 353.0 and X.shape == (2, axis.size)
    assert labels == ["olive", "olive"] and groups == ["batch_0", "batch_1"]
    (batch,) = list(REGISTRY["zenodo_oil"].iter_batches(tmp_path))
    assert REGISTRY["zenodo_oil"].domain == "chem" and len(batch.label) == 2
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_zenodo.py -v`
Expected: `ImportError` (no module `foundation.data.sources.zenodo_guo`).

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/zenodo_guo.py`:
```python
"""Single-cell bacteria and edible oils, Guo et al. (Zenodo 15279321, CC BY 4.0).

Bacterial_data.zip: Bacterial_data/data.csv in R write.csv style; the first
data row is the wavenumber axis, later rows are spectra. Labels/batches come
from a metadata CSV in the zip (meta_all.csv in the authors' code); without
one the spectra stay unlabelled (plan deviation D8).
Oil_data.zip: Oil_data/spec.csv (no header; row 0 = axis) and
Oil_data/metadata.csv (batches,labels,category), row-aligned.
"""
from __future__ import annotations

import zipfile
from pathlib import Path

import pandas as pd

from .base import RawBatch, fetch, register

BASE_URL = "https://zenodo.org/records/15279321/files/"
META_NAMES = ("meta_all.csv", "metadata.csv", "meta.csv")


def _member(zf, basename):
    for n in zf.namelist():
        if n.rsplit("/", 1)[-1] == basename:
            return n
    return None


def _labels_groups(zf, meta_name, n, default_group):
    labels, groups = [None] * n, [default_group] * n
    if meta_name is None:
        return labels, groups
    with zf.open(meta_name) as fh:
        meta = pd.read_csv(fh)
    if len(meta) != n:
        raise ValueError(f"{meta_name} has {len(meta)} rows for {n} spectra")
    if "labels" in meta:
        labels = meta["labels"].tolist()
    if "batches" in meta:
        groups = meta["batches"].astype(str).tolist()
    return labels, groups


def read_bacteria(zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        data = _member(zf, "data.csv")
        if data is None:
            raise ValueError(f"{zip_path}: data.csv not found")
        with zf.open(data) as fh:
            df = pd.read_csv(fh, index_col=0)
        axis = df.iloc[0].to_numpy(dtype=float)
        X = df.iloc[1:].to_numpy(dtype=float)
        meta = next((m for m in (_member(zf, b) for b in META_NAMES) if m), None)
        labels, groups = _labels_groups(zf, meta, len(X), "guo_bacteria")
    return axis, X, labels, groups


def read_oil(zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        spec, meta = _member(zf, "spec.csv"), _member(zf, "metadata.csv")
        if spec is None or meta is None:
            raise ValueError(f"{zip_path}: spec.csv or metadata.csv not found")
        with zf.open(spec) as fh:
            df = pd.read_csv(fh, header=None)
        axis = df.iloc[0].to_numpy(dtype=float)
        X = df.iloc[1:].to_numpy(dtype=float)
        labels, groups = _labels_groups(zf, meta, len(X), "guo_oil")
    return axis, X, labels, groups


class _Guo:
    licence = "CC BY 4.0"
    url = "https://doi.org/10.5281/zenodo.15279321"
    probe_label_kind = None

    def download(self, raw_dir):
        fetch(BASE_URL + self.zip_name, Path(raw_dir) / self.zip_name, retries=5)

    def iter_batches(self, raw_dir):
        axis, X, labels, groups = self.reader(Path(raw_dir) / self.zip_name)
        yield RawBatch(axes=axis, spectra=X, sample_id=groups, label=labels,
                       laser_nm=float("nan"))


class ZenodoBacteria(_Guo):
    name, domain, zip_name = "zenodo_bacteria", "bio", "Bacterial_data.zip"
    reader = staticmethod(read_bacteria)


class ZenodoOil(_Guo):
    name, domain, zip_name = "zenodo_oil", "chem", "Oil_data.zip"
    reader = staticmethod(read_oil)


register(ZenodoBacteria())
register(ZenodoOil())
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import zenodo_guo  # noqa: E402,F401
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_zenodo.py -v`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/zenodo_guo.py foundation/data/sources/__init__.py tests/foundation/test_source_zenodo.py
git commit -m "foundation: Zenodo (Guo) bacteria and oil source adapters"
```

---

### Task 11: MLROD adapter

**Files:**
- Create: `foundation/data/sources/mlrod.py`
- Modify: `foundation/data/sources/__init__.py` (append an import)
- Test: `tests/foundation/test_source_mlrod.py`

**Interfaces:**
- Consumes: `RawBatch`, `fetch`, `register` (Task 4).
- Produces:
  - A registered source `"mlrod"` (domain `mineral`, 532 nm, pretrain-only; group = file stem).
  - `FILES: dict[str, str]` (filename to URL) and `LABELS: dict[int, str]`.
  - `parse_header_axis(tokens) -> np.ndarray`.
  - `parse_mlrod_csv(path) -> (axis, X, y_int)`.

Verified format facts:
- **Files:** 41 CSVs from `https://www.odr.io/view/downloadfile/<id>?error_type=json`, no auth. The file list and the integer-to-mineral map come from `raman_data` (MIT, commit c92289e).
- **Layout:** the header is `og-idx,<wavenumbers…>,label`, with one row per spectrum. The axis differs per file.
- **Known corrupt header token:** `1630.89.1`.
- **Size:** 130,061 spectra in total. Licence CC BY-NC.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_mlrod.py`:
```python
import numpy as np

from foundation.data.sources import REGISTRY
from foundation.data.sources.mlrod import FILES, LABELS, parse_header_axis, parse_mlrod_csv


def test_file_list_and_labels_are_complete():
    assert len(FILES) == 41
    assert LABELS[0] == "Quartz" and LABELS[15] == "Granite slab - 50% dust"


def test_header_tolerates_malformed_token():
    axis = parse_header_axis(["95.49", "1630.89", "1630.89.1", " 1631.5"])
    assert axis.tolist() == [95.49, 1630.89, 1630.89, 1631.5]


def test_parse_csv_and_iter_batches(tmp_path, monkeypatch):
    axis = np.linspace(95.49, 1100.97, 600)
    header = "og-idx," + ",".join(f"{v:.2f}" for v in axis) + ",label"
    rows = [f"hb_train_060s_104-{i}," + ",".join("1.0" for _ in axis) + ",2" for i in range(3)]
    name = "hb_train_060s_104.csv"
    (tmp_path / name).write_text("\n".join([header] + rows) + "\n")
    ax, X, y = parse_mlrod_csv(tmp_path / name)
    assert ax.size == 600 and X.shape == (3, 600) and y == [2, 2, 2]
    import foundation.data.sources.mlrod as mlrod
    monkeypatch.setattr(mlrod, "FILES", {name: "unused"})
    (batch,) = list(REGISTRY["mlrod"].iter_batches(tmp_path))
    assert batch.label == ["Amphibole - Hornblende"] * 3
    assert batch.sample_id == ["hb_train_060s_104"] * 3
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_mlrod.py -v`
Expected: `ImportError` (no module `foundation.data.sources.mlrod`).

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/mlrod.py`:
```python
"""MLROD, Mars-analogue minerals (Berlanga et al. 2022; CC BY-NC; DOI 10.48484/PWRB-R137).

41 CSVs from odr.io. File list and integer->mineral map copied from the
raman_data package (MIT, github.com/ml-lab-htw/raman_data @ c92289e,
MiscLoader._load_mlrod). Layout: header 'og-idx,<wavenumbers...>,label', one
row per spectrum; the axis differs per file; one header token is known to be
malformed ('1630.89.1'), so tokens are parsed by their leading number.
532 nm Horiba LabRAM HR Evolution, raw spectra. Group = file (one acquisition set).
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

from .base import RawBatch, fetch, register

_ODR = "https://www.odr.io/view/downloadfile/{}?error_type=json"
FILES = {name: _ODR.format(i) for name, i in {
    "qtzalb_train_60s_3000.csv": 63653, "qtzalb_train_30s_2000.csv": 63652,
    "qtz_train_003s_4760.csv": 63758, "qtz_train_003s_1148.csv": 63757,
    "qtz_train_015s_625.csv": 63756, "qtz_train_005s_1000.csv": 63754,
    "qtz_train_005s_0900.csv": 63753, "qtz_train_003s-1599.csv": 63752,
    "ms_train_015s_5900.csv": 63755, "mc_train_015s_3243.csv": 63750,
    "mc_train_3s_2357.csv": 63651, "hb_train_120s_1225_01.csv": 63751,
    "hb_train_015s_2500.csv": 63749, "hb_train_120s_1225_02.csv": 63748,
    "hb_train_060s_104.csv": 63650, "gyp_train_12s_3320.csv": 63746,
    "gyp_train_15s_1680.csv": 63649, "foaug_train_60s_3520.csv": 63648,
    "foaug_train_30s_1640.csv": 63647, "foalb_train_15s_5220.csv": 63745,
    "fo_train_030s_5040.csv": 63747, "fo_train_015s_1100.csv": 63646,
    "en_train_015s_5600.csv": 63744, "cal_train_1s_2732.csv": 63743,
    "cal_train_1s_2300.csv": 63645, "bt_train_120s_1225.csv": 63741,
    "bt_train_015s_5600.csv": 63644, "bt_train_015s_1100.csv": 63643,
    "aug_train_20s_5103.csv": 63738, "aug_train_15s_1000.csv": 63642,
    "an_train_015s_5600.csv": 63740, "albite_train_015s_5250.csv": 63739,
    "albite_train_015s_625.csv": 63737, "albite_train_015s_1100.csv": 63641,
    "L_raw_gabbro50dust_test_015s_9740.csv": 63659,
    "L_raw_granite50dust_test_015s_10000.csv": 63245,
    "L_raw_granite0dust_test_015s_4084_final.csv": 63658,
    "L_raw_granite0dust_test_030s_1373_final.csv": 63657,
    "L_raw_granite0dust_test_015s_5571_final.csv": 63656,
    "L_raw_gabbro0dust_test_015s_8906_final.csv": 63655,
    "L_raw_gabbro0dust_test_015s_46_final.csv": 63654,
}.items()}

LABELS = {
    0: "Quartz", 1: "Feldspar - Albite", 2: "Amphibole - Hornblende", 3: "Mica - Biotite",
    4: "Mica - Muscovite", 5: "Olivine - Forsterite", 6: "Pyroxene - Augite",
    7: "Pyroxene - Enstatite", 8: "Feldspar - Anorthite", 9: "Feldspar - Microcline",
    10: "Carbonate - Calcite", 11: "Sulfate - Gypsum", 12: "50% Quartz / 50% Albite Mix",
    13: "50% Forsterite / 50% Augite Mix", 14: "50% Forsterite / 50% Albite Mix",
    15: "Granite slab - 50% dust",
}

_NUM = re.compile(r"^\s*(-?\d+(?:\.\d+)?)")


def parse_header_axis(tokens):
    vals = []
    for t in tokens:
        m = _NUM.match(t)
        if not m:
            raise ValueError(f"unparseable wavenumber {t!r}")
        vals.append(float(m.group(1)))
    return np.array(vals)


def parse_mlrod_csv(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        header = fh.readline().strip().split(",")
    if header[0].strip() != "og-idx" or header[-1].strip() != "label":
        raise ValueError(f"{path}: unexpected header {header[0]!r}...{header[-1]!r}")
    axis = parse_header_axis(header[1:-1])
    df = pd.read_csv(path, header=None, skiprows=1)
    X = df.iloc[:, 1:-1].to_numpy(dtype=np.float64)
    y = df.iloc[:, -1].astype(int).tolist()
    return axis, X, y


class MLROD:
    name = "mlrod"
    domain = "mineral"
    licence = "CC BY-NC"
    url = "https://doi.org/10.48484/PWRB-R137"
    probe_label_kind = "mineral"

    def download(self, raw_dir):
        for fname, url in FILES.items():
            fetch(url, Path(raw_dir) / fname, retries=5)

    def iter_batches(self, raw_dir):
        for fname in FILES:
            axis, X, y = parse_mlrod_csv(Path(raw_dir) / fname)
            yield RawBatch(axes=axis, spectra=X, sample_id=[Path(fname).stem] * len(X),
                           label=[LABELS.get(v, str(v)) for v in y], laser_nm=532)


register(MLROD())
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import mlrod  # noqa: E402,F401
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_mlrod.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/mlrod.py foundation/data/sources/__init__.py tests/foundation/test_source_mlrod.py
git commit -m "foundation: MLROD source adapter"
```

---

### Task 12: DeepeR adapter (manual download)

**Files:**
- Create: `foundation/data/sources/deeper.py`
- Modify: `foundation/data/sources/__init__.py` (append an import)
- Test: `tests/foundation/test_source_deeper.py`

**Interfaces:**
- Consumes: `RawBatch`, `register`, `ManualDownloadRequired` (Task 4).
- Produces:
  - A registered source `"deeper"` (domain `bio`, 532 nm, unlabelled).
  - `DeepeR(max_spectra=22_000, seed=0)`.
  - `REQUIRED` file tuple.

Verified format facts:
- **Folder:** `Raman Spectral Denoising/Dataset` holds `Train_Outputs.mat` (598.8 MB) and `Test_Outputs.mat` (46.4 MB). Both are MATLAB 5 files, so `scipy.io.loadmat` reads them. Each contains a variable of the same name (shapes (159618, 500) and (12694, 500)).
- **Axis:** `axis.txt` is 500 lines, ascending 498.3–1799.9 cm⁻¹.
- **No cell IDs** (deviation D1).

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_deeper.py`:
```python
import numpy as np
import pytest
from scipy.io import savemat

from foundation.data.sources.base import ManualDownloadRequired
from foundation.data.sources.deeper import REQUIRED, DeepeR


def _fixture(raw):
    raw.mkdir(parents=True)
    axis = np.linspace(498.265, 1799.9, 500)
    np.savetxt(raw / "axis.txt", axis, fmt="%.18e")
    rng = np.random.default_rng(0)
    savemat(raw / "Train_Outputs.mat", {"Train_Outputs": rng.random((40, 500))})
    savemat(raw / "Test_Outputs.mat", {"Test_Outputs": rng.random((10, 500))})


def test_missing_files_ask_for_manual_download(tmp_path):
    with pytest.raises(ManualDownloadRequired, match="Train_Outputs.mat"):
        DeepeR().download(tmp_path / "deeper")


def test_subsample_is_capped_unique_and_deterministic(tmp_path):
    _fixture(tmp_path / "deeper")
    DeepeR().download(tmp_path / "deeper")              # files present: no error
    (a,) = list(DeepeR(max_spectra=20, seed=0).iter_batches(tmp_path / "deeper"))
    (b,) = list(DeepeR(max_spectra=20, seed=0).iter_batches(tmp_path / "deeper"))
    assert len(a.spectra) == 20
    np.testing.assert_array_equal(a.spectra, b.spectra)
    assert len({row.tobytes() for row in a.spectra}) == 20
    assert a.axes.size == 500 and a.label == [None] * 20


def test_cap_larger_than_data_keeps_everything(tmp_path):
    _fixture(tmp_path / "deeper")
    (batch,) = list(DeepeR(max_spectra=1000).iter_batches(tmp_path / "deeper"))
    assert len(batch.spectra) == 50
    assert set(REQUIRED) == {"Train_Outputs.mat", "Test_Outputs.mat", "axis.txt"}
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_deeper.py -v`
Expected: `ImportError` (no module `foundation.data.sources.deeper`).

- [ ] **Step 3: Write the implementation**

`foundation/data/sources/deeper.py`:
```python
"""DeepeR breast-cancer-cell spectra, Horgan et al. 2021 (denoising set), 532 nm.

MANUAL DOWNLOAD (SharePoint is not reliably scriptable): put Train_Outputs.mat,
Test_Outputs.mat and axis.txt from the 'Raman Spectral Denoising/Dataset'
folder of SHARE_URL into foundation/data/raw/deeper/. Only the high-SNR
*Outputs* are used; the *Inputs* are noisy copies of the same spectra. The set
is shuffled with no cell/image ids (11 cells), so the spec's 2,000-per-image
cap is approximated by a seeded subsample of 11 x 2,000 = 22,000 (deviation D1).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.io import loadmat

from .base import ManualDownloadRequired, RawBatch, register

SHARE_URL = ("https://emckclac-my.sharepoint.com/:f:/g/personal/k1919691_kcl_ac_uk/"
             "EqZaY-_FrGdImybIGuMCvb8Bo_YD1Bc9ATBxbLxdDIv0RA?e=5%3aHhLp91&fromShare=true&at=9")
REQUIRED = ("Train_Outputs.mat", "Test_Outputs.mat", "axis.txt")


class DeepeR:
    name = "deeper"
    domain = "bio"
    licence = "code MIT; data licence not stated (research use)"
    url = SHARE_URL
    probe_label_kind = None

    def __init__(self, max_spectra=22_000, seed=0):
        self.max_spectra, self.seed = max_spectra, seed

    def download(self, raw_dir):
        missing = [f for f in REQUIRED if not (Path(raw_dir) / f).exists()]
        if missing:
            raise ManualDownloadRequired(
                f"DeepeR needs a manual download of {', '.join(missing)} from {SHARE_URL} "
                f"(folder 'Raman Spectral Denoising/Dataset') into {Path(raw_dir).resolve()}")

    def iter_batches(self, raw_dir):
        raw_dir = Path(raw_dir)
        axis = np.loadtxt(raw_dir / "axis.txt")
        X = np.vstack([loadmat(raw_dir / "Train_Outputs.mat")["Train_Outputs"],
                       loadmat(raw_dir / "Test_Outputs.mat")["Test_Outputs"]])
        if X.shape[1] != axis.size:
            raise ValueError(f"DeepeR: {X.shape[1]} points per spectrum, axis has {axis.size}")
        n = min(self.max_spectra, len(X))
        idx = np.sort(np.random.default_rng(self.seed).choice(len(X), size=n, replace=False))
        yield RawBatch(axes=axis, spectra=X[idx], sample_id=["deeper_cells"] * n,
                       label=[None] * n, laser_nm=532)


register(DeepeR())
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import deeper  # noqa: E402,F401
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_deeper.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/data/sources/deeper.py foundation/data/sources/__init__.py tests/foundation/test_source_deeper.py
git commit -m "foundation: DeepeR source adapter (manual download, capped subsample)"
```

---

### Task 13: raman_data datasets (separate-venv export plus adapter)

**Files:**
- Create: `foundation/configs/raman_data_whitelist.yaml`
- Create: `foundation/tools/export_raman_data.py`
- Create: `foundation/data/sources/raman_data_export.py`
- Modify: `foundation/data/sources/__init__.py` (append an import), `.gitignore` (append)
- Test: `tests/foundation/test_source_raman_data.py`

**Interfaces:**
- Consumes: `RawBatch`, `register`, `ManualDownloadRequired`, `MAX_BATCH` (Task 4).
- Produces:
  - One registered source per whitelisted dataset, named `rd_<id>`. These are pretrain-only. The domain and laser come from the whitelist.
  - `RamanDataExport(ds_id, domain, laser_nm)`.
  - The `.npz` contract written by the exporter: `spectra` float32 (n, p), `axis` float64 (p,), `labels` str array (length n, or 0 if unlabelled), `group_ids` str array (length n, or 0).

Why a separate venv (deviation D5): `raman_data` depends on `datasets`, `spectrochempy`, `kagglehub`, `mlcroissant`, `gdown` and `zenodo-get`. Any of them could change numpy, scipy or pandas in the experiment's venv. The exporter is a standalone script with no `foundation` imports, so it runs anywhere.

- [ ] **Step 1: Write the failing tests**

`tests/foundation/test_source_raman_data.py`:
```python
import numpy as np
import pytest

from foundation.data.sources import REGISTRY, base
from foundation.data.sources.base import ManualDownloadRequired
from foundation.data.sources.raman_data_export import RamanDataExport


def _npz(raw, ds_id, n, labels=True):
    d = raw / "raman_data"
    d.mkdir(parents=True, exist_ok=True)
    np.savez(d / f"{ds_id}.npz", spectra=np.ones((n, 300), np.float32),
             axis=np.linspace(400, 1800, 300),
             labels=np.array(["pos", "neg"] * (n // 2)) if labels else np.array([], dtype=str),
             group_ids=np.array([], dtype=str))


def test_whitelisted_sources_are_registered():
    assert "rd_covid19_salvia" in REGISTRY
    assert REGISTRY["rd_covid19_salvia"].domain == "bio"


def test_missing_export_asks_for_export_step(tmp_path):
    src = RamanDataExport("x", "bio", 785)
    with pytest.raises(ManualDownloadRequired, match="export_raman_data"):
        src.download(tmp_path / "rd_x")


def test_reads_labels_and_defaults_group(tmp_path):
    _npz(tmp_path, "x", 4)
    src = RamanDataExport("x", "bio", 785)
    src.download(tmp_path / "rd_x")
    (batch,) = list(src.iter_batches(tmp_path / "rd_x"))
    assert batch.label == ["pos", "neg", "pos", "neg"]
    assert set(batch.sample_id) == {"rd_x"}
    assert batch.laser_nm.tolist() == [785.0] * 4


def test_unlabelled_and_chunked(tmp_path, monkeypatch):
    _npz(tmp_path, "y", 10, labels=False)
    monkeypatch.setattr(base, "MAX_BATCH", 4)
    import foundation.data.sources.raman_data_export as rde
    monkeypatch.setattr(rde, "MAX_BATCH", 4)
    batches = list(RamanDataExport("y", "chem", None).iter_batches(tmp_path / "rd_y"))
    assert [len(b.spectra) for b in batches] == [4, 4, 2]
    assert all(l is None for b in batches for l in b.label)
    assert np.isnan(batches[0].laser_nm).all()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_raman_data.py -v`
Expected: `ImportError` (no module `foundation.data.sources.raman_data_export`).

- [ ] **Step 3: Write the whitelist, the adapter and the exporter**

`foundation/configs/raman_data_whitelist.yaml`:
```yaml
# raman_data datasets used as pretraining sources (spontaneous Raman only).
# id: {domain, laser_nm}. Checked against raman_data @ c92289e descriptions.
# Excluded on purpose: every SERS set, bacteria_identification (= our data),
# pharmaceutical_ingredients (= api_flanagan), deepr_* and mlrod (own adapters),
# rruff_* (own adapter), locust_phase_hemolymph (resonance Raman),
# marine_pathogens* (no wavenumber axis), time-gated and synthetic-mix sets,
# and Kaggle-only sets (need credentials).
covid19_salvia: {domain: bio, laser_nm: 785}
parkinson: {domain: bio, laser_nm: null}
alzheimer: {domain: bio, laser_nm: null}
wheat_lines: {domain: bio, laser_nm: 785}
head_neck_cancer: {domain: bio, laser_nm: null}
ecoli_fermentation: {domain: chem, laser_nm: 785}
yeast_fermentation: {domain: chem, laser_nm: null}
bioprocess_substrates: {domain: chem, laser_nm: null}
kaiser_ecoli_fermentation: {domain: chem, laser_nm: null}
kaiser_ecoli_fermentation_supernatant: {domain: chem, laser_nm: null}
streptococcus_thermophilus_fermentation_kaiser: {domain: chem, laser_nm: null}
bioprocess_analytes_anton_532: {domain: chem, laser_nm: 532}
bioprocess_analytes_anton_785: {domain: chem, laser_nm: 785}
bioprocess_analytes_kaiser: {domain: chem, laser_nm: null}
bioprocess_analytes_metrohm: {domain: chem, laser_nm: null}
bioprocess_analytes_mettler_toledo: {domain: chem, laser_nm: null}
bioprocess_analytes_tec5: {domain: chem, laser_nm: null}
bioprocess_analytes_tornado: {domain: chem, laser_nm: null}
ecoli_metabolites_dig4bio: {domain: chem, laser_nm: null}
bioprocess_analytes_ecoli_metabolites: {domain: chem, laser_nm: null}
```

`foundation/data/sources/raman_data_export.py`:
```python
"""Datasets from the raman_data package, read from .npz files exported by
foundation/tools/export_raman_data.py in its own venv (plan deviation D5).
One source per whitelisted dataset id, named rd_<id>.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import yaml

from .base import MAX_BATCH, ManualDownloadRequired, RawBatch, register

WHITELIST = Path(__file__).resolve().parents[2] / "configs" / "raman_data_whitelist.yaml"
EXPORT_HINT = ("python -m venv foundation/.venv-raman-data; "
               "foundation/.venv-raman-data/Scripts/python.exe -m pip install "
               "\"git+https://github.com/ml-lab-htw/raman_data@c92289e\" pyyaml; "
               "foundation/.venv-raman-data/Scripts/python.exe foundation/tools/export_raman_data.py")


class RamanDataExport:
    url = "https://github.com/ml-lab-htw/raman_data"
    licence = "per dataset; see raw/raman_data/export_report.json"
    probe_label_kind = None

    def __init__(self, ds_id, domain, laser_nm):
        self.ds_id = ds_id
        self.name = f"rd_{ds_id}"
        self.domain = domain
        self.laser_nm = float("nan") if laser_nm is None else float(laser_nm)

    def _file(self, raw_dir):
        return Path(raw_dir).parent / "raman_data" / f"{self.ds_id}.npz"

    def download(self, raw_dir):
        if not self._file(raw_dir).exists():
            raise ManualDownloadRequired(
                f"{self._file(raw_dir)} missing; run the export_raman_data step: {EXPORT_HINT}")

    def iter_batches(self, raw_dir):
        z = np.load(self._file(raw_dir))
        X, axis = z["spectra"], z["axis"]
        n = len(X)
        labels = z["labels"].tolist() if z["labels"].size == n else [None] * n
        groups = z["group_ids"].tolist() if z["group_ids"].size == n else [self.name] * n
        for s in range(0, n, MAX_BATCH):
            e = min(n, s + MAX_BATCH)
            yield RawBatch(axes=axis, spectra=X[s:e], sample_id=groups[s:e],
                           label=labels[s:e], laser_nm=self.laser_nm)


for _id, _cfg in (yaml.safe_load(WHITELIST.read_text()) or {}).items():
    register(RamanDataExport(_id, _cfg["domain"], _cfg.get("laser_nm")))
```

`foundation/tools/export_raman_data.py`:
```python
"""Export whitelisted raman_data datasets to plain .npz (plan deviation D5).

Runs in its OWN venv so raman_data's dependencies never touch the main env:
    python -m venv foundation/.venv-raman-data
    foundation/.venv-raman-data/Scripts/python.exe -m pip install "git+https://github.com/ml-lab-htw/raman_data@c92289e" pyyaml
    foundation/.venv-raman-data/Scripts/python.exe foundation/tools/export_raman_data.py
Writes foundation/data/raw/raman_data/<id>.npz and export_report.json.
Standalone on purpose: imports nothing from the foundation package.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import yaml


def to_labels(ds):
    task = str(getattr(ds.info, "task_type", ""))
    targets = getattr(ds, "targets", None)
    if targets is None or "Classification" not in task:
        return None
    t = np.asarray(targets)
    names = getattr(ds, "target_names", None)
    if names is not None and len(names) and np.issubdtype(t.dtype, np.integer):
        return np.array([str(names[int(v)]) for v in t])
    return np.array([str(v) for v in t])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--whitelist", default="foundation/configs/raman_data_whitelist.yaml")
    ap.add_argument("--out", default="foundation/data/raw/raman_data")
    ap.add_argument("--cache-dir", default="foundation/data/raw/raman_data/_cache")
    args = ap.parse_args(argv)
    from raman_data import raman_data

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report = {}
    for ds_id in yaml.safe_load(Path(args.whitelist).read_text()):
        try:
            ds = raman_data(ds_id, cache_dir=args.cache_dir)
            labels = to_labels(ds)
            groups = getattr(ds, "group_ids", None)
            np.savez_compressed(
                out / f"{ds_id}.npz",
                spectra=np.asarray(ds.spectra, dtype=np.float32),
                axis=np.asarray(ds.raman_shifts, dtype=np.float64),
                labels=labels if labels is not None else np.array([], dtype=str),
                group_ids=(np.asarray(groups).astype(str) if groups is not None
                           else np.array([], dtype=str)))
            report[ds_id] = {"status": "ok", "n": int(len(ds.spectra)),
                             "licence": str(getattr(ds.info, "license", "")),
                             "description": ds.info.metadata.get("description", "")}
        except Exception as e:  # keep going; the report says what failed
            report[ds_id] = {"status": f"failed: {type(e).__name__}: {e}"}
        print(f"{ds_id}: {report[ds_id]['status']}")
    (out / "export_report.json").write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
```

Append to `foundation/data/sources/__init__.py`:
```python
from . import raman_data_export  # noqa: E402,F401
```

Append to `.gitignore`:
```
foundation/.venv-raman-data/
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/Scripts/python.exe -m pytest tests/foundation/test_source_raman_data.py -v`
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add foundation/configs/raman_data_whitelist.yaml foundation/tools/export_raman_data.py foundation/data/sources/raman_data_export.py foundation/data/sources/__init__.py tests/foundation/test_source_raman_data.py .gitignore
git commit -m "foundation: raman_data datasets via separate-venv export"
```

---

### Task 14: Build corpus_v1 for real and decide G0

**Files:**
- Create: `foundation/configs/corpus_v1.yaml`, `foundation/README.md`
- Commit after the build: `foundation/data/corpus_v1/manifest.json`

**Interfaces:**
- Consumes: everything above.
- Produces: `foundation/data/corpus_v1/` (the artefacts listed in Task 5) and the G0 decision. Plan 2 starts from here.

- [ ] **Step 1: Write the corpus config**

`foundation/configs/corpus_v1.yaml`:
```yaml
version: corpus_v1
out_dir: foundation/data/corpus_v1
raw_dir: foundation/data/raw
cache_dir: foundation/data/cache
our_data_dir: data
seed: 0
device: cuda
leakage_cos_threshold: 0.999
probe_fraction: 0.15
probe_test_fraction: 0.4
min_probe_class_spectra: 5
sources:
  - {name: rruff, probe: true}
  - {name: airborne, probe: true}
  - {name: api_flanagan, probe: false}
  - {name: mlrod, probe: false}
  - {name: zenodo_bacteria, probe: false}
  - {name: zenodo_oil, probe: false}
  - {name: deeper, probe: false, optional: true}
  - {name: rd_covid19_salvia, probe: false, optional: true}
  - {name: rd_parkinson, probe: false, optional: true}
  - {name: rd_alzheimer, probe: false, optional: true}
  - {name: rd_wheat_lines, probe: false, optional: true}
  - {name: rd_head_neck_cancer, probe: false, optional: true}
  - {name: rd_ecoli_fermentation, probe: false, optional: true}
  - {name: rd_yeast_fermentation, probe: false, optional: true}
  - {name: rd_bioprocess_substrates, probe: false, optional: true}
  - {name: rd_kaiser_ecoli_fermentation, probe: false, optional: true}
  - {name: rd_kaiser_ecoli_fermentation_supernatant, probe: false, optional: true}
  - {name: rd_streptococcus_thermophilus_fermentation_kaiser, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_anton_532, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_anton_785, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_kaiser, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_metrohm, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_mettler_toledo, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_tec5, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_tornado, probe: false, optional: true}
  - {name: rd_ecoli_metabolites_dig4bio, probe: false, optional: true}
  - {name: rd_bioprocess_analytes_ecoli_metabolites, probe: false, optional: true}
```

`foundation/README.md`:
````markdown
# Raman foundation model experiment (A -> B1 / B2)

Spec: `docs/superpowers/specs/2026-10-01-raman-foundation-model-design.md`.
This package is self-contained and imports nothing from `src/` or `legacy_baseline/`.

## Phase 0: build the pretraining corpus

1. Optional sources:
   - **DeepeR** is a manual download. Put `Train_Outputs.mat`, `Test_Outputs.mat` and `axis.txt` into `foundation/data/raw/deeper/`. The link is in `foundation/data/sources/deeper.py`.
   - **raman_data datasets** are exported in a separate venv:
     ```
     python -m venv foundation/.venv-raman-data
     foundation/.venv-raman-data/Scripts/python.exe -m pip install "git+https://github.com/ml-lab-htw/raman_data@c92289e" pyyaml
     foundation/.venv-raman-data/Scripts/python.exe foundation/tools/export_raman_data.py
     ```
2. Build (downloads the automatic sources the first time):
   `venv/Scripts/python.exe -m foundation.data.build_corpus --config foundation/configs/corpus_v1.yaml`
3. Audit and gate G0:
   `venv/Scripts/python.exe -m foundation.data.audit --corpus foundation/data/corpus_v1`

Our Bacteria-ID files are read only to keep them out of the corpus (leakage guard).
````

- [ ] **Step 2: Run the whole test suite**

Run: `venv/Scripts/python.exe -m pytest tests/foundation -v`
Expected: every test passes (one real-data test may be skipped if `data/` is absent). Any failure blocks the steps below.

- [ ] **Step 3: STOP and get the user's permission to download**

Tell the user, and wait for an explicit yes before continuing:

| Source | What gets downloaded | Size |
|---|---|---|
| RRUFF | 3 zips from rruff.net | ~515 MB |
| API (Flanagan) | 1 CSV from figshare | ~193 MB |
| Airborne pathogens | ~11.4k small files from scidb.cn | < 205 MB |
| Zenodo (Guo) | 2 zips | ~35 MB |
| MLROD | 41 CSVs from odr.io | not listed by the source; expect up to ~2 GB |
| raman_data | `pip install` of the package and its deps into `foundation/.venv-raman-data`, plus 20 datasets (Hugging Face, Zenodo, GitHub) | not listed; reported by the export |
| DeepeR | manual, by the user, optional | ~645 MB |

Also tell the user that MLROD, the airborne set and marine data are **non-commercial** licences. That's fine for research and is recorded in the manifest.

- [ ] **Step 4: Export the raman_data datasets** (only after permission)

```bash
python -m venv foundation/.venv-raman-data
foundation/.venv-raman-data/Scripts/python.exe -m pip install "git+https://github.com/ml-lab-htw/raman_data@c92289e" pyyaml
foundation/.venv-raman-data/Scripts/python.exe foundation/tools/export_raman_data.py
```

Expected: one `<id>: ok` or `<id>: failed: ...` line per dataset, and `foundation/data/raw/raman_data/export_report.json`.

Open the report and read every `description`. **If one mentions SERS, delete that dataset's line from `raman_data_whitelist.yaml` and from `corpus_v1.yaml`.** Note any failures for the user. Failed datasets are skipped automatically, because they're `optional`.

- [ ] **Step 5: Build the corpus**

Run: `venv/Scripts/python.exe -m foundation.data.build_corpus --config foundation/configs/corpus_v1.yaml`

Expected:
- the downloads run and their progress prints;
- `[corpus] deeper: skipped: ...` if DeepeR wasn't placed manually;
- finally a JSON with `pretrain`, `probe_train` and `probe_test` counts, then `wrote foundation/data/corpus_v1`.

If a download fails after its retries (odr.io and rruff.net are flaky), rerun the same command. Finished files are skipped.

- [ ] **Step 6: Audit and decide G0**

Run: `venv/Scripts/python.exe -m foundation.data.audit --corpus foundation/data/corpus_v1`

Expected: a per-source table, then `G0 PASS: N pretraining spectra >= 150,000` (exit 0) or `G0 FAIL ...` (exit 1).

Report the table to the user and point out three things:
- `n_leaked` per source: non-zero means copies of our data were found and removed;
- each source's share of `n_pretrain`;
- the probe class counts (`n_probe_train` and `n_probe_test` for `rruff` and `airborne`).

**On G0 FAIL, stop. Plan 2 must not start.** Discuss the source list with the user.

- [ ] **Step 7: Commit the config, README and manifest**

```bash
git add foundation/configs/corpus_v1.yaml foundation/README.md foundation/data/corpus_v1/manifest.json
git commit -m "foundation: build corpus_v1 and record G0 audit"
```
