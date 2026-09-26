# FACTCHECK — The Weights Were Never the Risk

Every figure that appears on screen or in narration, and how it was checked.
Repo cloned fresh at `78b383e`; the pre-Rust pipeline checked out at `663feeb`
(first parent of the port commit `9cace7b`). All runs made 2026-09-25 on this
machine (macOS, Apple Silicon). Outputs in `evidence/`.

## Environment

| Side | Toolchain |
|---|---|
| Rust | rustc 1.97.1, cargo 1.97.1, `--release` profile, ort 2.0.0-rc.13 |
| Python | Python 3.11.5 in a scratch venv; onnxruntime 1.29.0, numpy 2.4.6, Pillow 12.3.0 — the exact pins in `backend/requirements.txt` @ `663feeb` |
| Data | `loonnet_v1/val.txt`: 26 photos, 33 labelled loons (local, not published) |

## Size, platforms, CI (B00, B01, B07)

| Claim | On screen | Verified by | Result |
|---|---|---|---|
| Mac download 84 → 45 MB | B00, B01, B07 | GitHub Releases API + `stat` on last week's DMG (`release_and_ci.out`) | 0.1.0: 87,879,427 B = 83.8 MiB → 0.2.0: 47,183,690 B = **45.0 MiB** ✓ (README's "43 MB" ✗ — not used) |
| "almost half" | B00 narration | ratio | 0.537 — a 46% reduction ✓ |
| macOS · Windows · Linux | B00, B01, B07 | Release assets: `.dmg`, `-setup.exe`, `.deb`, `.rpm`, `.AppImage`, all uploaded by `github-actions[bot]` | ✓ |
| "every change builds installers" | B01 | `.github/workflows/desktop.yml` @ `1f1a1e6`; run `35841358212`: rust (macOS/Windows/Linux), frontend, audit, installers ×3 — all `success` | ✓ |
| no server, port or token | B01, B07 | `src/lib.rs:6`, `src/protocol.rs:4` — assets served over `gavia://`; no HTTP listener in `src/` | ✓ |
| Six removed items | B01 | CHANGELOG §0.2.0 Changed/Removed; `backend/` and `frontend/e2e/` deleted in `9cace7b` | ✓ |

## The weights (B02, B05)

| Claim | Verified by | Result |
|---|---|---|
| Model file byte-identical | `shasum -a 256` on `backend/models/loon_v1.onnx` @ `663feeb` and `resources/models/loon_v1.onnx` @ `78b383e` (`model_sha256.out`) | both `172fa54f…2e2029` ✓ — also the sha 09-18-1 read off the 0.1.0 bundle |
| Fixture written before deletion | `tests/fixtures/python_reference.json` added in `9cace7b`, the same commit that deletes `backend/`; commit message: "Behaviour of the Python pipeline was frozen into tests/fixtures/python_reference.json before removal" | ✓ |
| Pillow resampling, rounding, JPEG reduction | `preprocess.rs:135–137` ("Pillow-compatible bilinear convolution … round-half-to-even"), `loader.rs:115` ("choosing the factor exactly as Pillow's draft() did") | ✓ |

## The draft rule (B03) — algebra

Read from `desktop/src-tauri/src/detection/loader.rs::draft_factor`, not the changelog:

```rust
let ratio = (width / target).min(height / target);      // integer division
[8, 4, 2, 1].into_iter().find(|&s| ratio >= s).unwrap_or(1)
```

- Row 1, `r = min(⌊w/640⌋, ⌊h/640⌋)` — integer division on `u32` is floor. **Exact** ✓
- Row 2, `f = max{d ∈ {1,2,4,8} : d ≤ r}` — `find` over the descending list returns
  the largest `s ≤ ratio`; for `ratio = 0` the set is empty and the code returns 1.
  The conditions line states w, h ≥ 640 implicitly by using a real photo; the
  empty-set case never arises on screen. **Equivalent for r ≥ 1** ✓
- Row 3, 5568 × 3712: 5568/640 = 8.7 and 3712/640 = 5.8 exactly, so
  `r = min(8, 5) = 5`, `f = 4`, kept at 1392 × 928 — both sides ≥ 640 ✓.
  Asserted in `build_beats.py::check_algebra`, together with the six unit-test
  cases shipped in `loader.rs::draft_factor_matches_pillow`.
- "keeps both sides at least 640" (narration): f ≤ ⌊w/640⌋ ⇒ w/f ≥ 640, same for h ✓.

**Reproducible numerical case** — `evidence/draft_factor.out`: Pillow 12.3.0's
own `draft('RGB', (640, 640))` on every validation JPEG, against the Rust
formula. **26 of 26 agree.** The three `nikon_*` validation photos are
5568 × 3712 and draft to 1392 × 928 (f = 4).

**The "picks eight" claim** — `evidence/scale_probe.out`: jpeg-decoder 0.3.2's
own `Decoder::scale(640, 640)` on the same 26 files. On the Nikon frames it
returns 696 × 464 (f = 8). **It differs from Pillow on 15 of 26 photos.** The
probe is a scratch example compiled against Gavia's crate at `78b383e`; it is
not part of Gavia.

Typography: three outlined-SVG rows from `runtime/scripts/typeset_math.py`
(matplotlib mathtext, STIX, `svg.fonttype=path`). Real fraction bars on w/640
and h/640 (`\dfrac`), sized floor brackets (`\left\lfloor…\right\rfloor`), a
set-builder max with braces, ∈ and ≤ as glyphs. `min`, `max` upright; r, f, d,
w, h italic. **No raw TeX in any text card.**

### Rendered-frame review (MATH-TYPESETTING.md)

<!-- filled after render -->

## The parity run (B04)

| Row on screen | Value | Source |
|---|---|---|
| boxes Python found | 32 | `python_reference.json` `val[*].detections`, summed; = boxes ≥ 0.25 in `evaluate_python.out` (P = 29/32) |
| found again by Rust | 32 | `parity_rust.out`: "32 boxes compared" — the test asserts `compared == total` and panics on any box Rust adds |
| worst confidence gap | 0.0151 | `parity_rust.out`: "worst confidence delta 0.0151" (commit message rounds to 0.015) |
| change in AP@0.5 | −0.0011 | 0.8910 (`evaluate_rust.out`) − 0.8921 (`evaluate_python.out`) |

Also in the note / narration:

| Claim | Python | Rust | Match |
|---|---|---|---|
| Precision @ 0.25 | 0.9062 | 0.9062 | ✓ = 29/32 |
| Recall @ 0.25 | 0.8788 | 0.8788 | ✓ = 29/33 |
| AP@0.5 over conf ≥ 0.001 | 0.8921 | 0.8910 | moved in the third decimal |
| predictions ≥ 0.001 | 89 | 90 | "ninety to Python's eighty-nine" ✓ |
| worst box delta | — | 0.153 points | not on screen |

"confidences at most a point and a half apart": 0.0151 on a 0–1 scale = 1.51
percentage points ✓.

## The ruler (B05)

| Claim | Source | Result |
|---|---|---|
| last week: "one loon in five" | `09-18-1` B05 narration, from the card's recall 0.80012 | ✓ |
| card recall 0.800 | `loon_v1.json` `metrics.recall` = 0.80012; `metrics.note`: "Ultralytics validation split, recorded in the best.pt checkpoint." | ✓ still in 0.2.0 |
| app recall 0.879, 29 of 33, four missed | `evaluate_rust.out` and `evaluate_python.out`: R 0.8788 at the shipped 0.25 threshold = 29/33 | ✓ |
| "shipped threshold of 0.25" | `loon_v1.json` `defaults.confidence_threshold`; `evaluate.rs` `SHIPPED_THRESHOLD` | ✓ |

Not claimed: *why* the two recalls differ in detail (operating point,
letterboxing, NMS settings all differ between the two evaluators). The reel says
only that they are different rulers on the same weights.

## Roadmap and credit (B06, B07)

| Claim | Source |
|---|---|
| six required features, 1 shipped / 2 partly / 3–6 not started | `ROADMAP.md` table @ `78b383e` ✓ |
| next: survey counting, CSV | `ROADMAP.md` "Now" and feature 2 "Still to do" ✓ |
| per-photo count by Swara Joshi, this week, survived the rewrite | `663feeb` (Swara-Joshi, 2026-09-21) adds "Loons detected"; `9cace7b` "Brings in origin/swara's loon count"; `DetectionResult.tsx:175` at HEAD ✓ |
| Settings, Help, loon icon | `448b77c`, `1a3551b`, `f9d4964` ✓ |

## Claims deliberately softened

| Tempting claim | Why it is not made |
|---|---|
| "43 MB" | The released DMG measures 45.0 MiB. |
| "recall improved to 88%" | Same weights; a different evaluator. |
| "the extra box cost the AP" | Not isolated from the confidence shifts. |
| "identical output" | Confidences differ by up to 0.0151 and boxes by 0.153 points; the reel says "the same places" and gives the gap. |
| "first public release" | ROADMAP lists it under "Now"; the GitHub release is marked pre-release. Not claimed. |
| "faster" / "lighter on memory" | Nothing was timed. |
