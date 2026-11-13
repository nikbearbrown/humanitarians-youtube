# Figure Audit — Phase 6 (Check Images)

*Run date: 2026-07-15. The repo's `svg-visual-audit.mjs` needs Node (unavailable here), so this is the manual equivalent across the same defect classes: SUB (subscript), SUP (superscript), MATH (Greek/→/≠/×), OVER (overflow). Plus an accuracy cross-check against chapter text.*

## Defect-class scan

| Class | Method | Result |
|---|---|---|
| SUB / SUP | grep SVGs for `₀-₉ ⁰-⁹` | **0 found** |
| MATH (Greek, arrows, ×, ≠, √, ∞) | grep SVGs for the glyph set | **0 remaining** (arrows/×/✗/←/· were caught in Phase 5 and replaced with ASCII-safe text, then re-rendered) |
| OVER (text overflow / clipping) | visual review of all 11 rendered PNGs | **0 found** — all text sits within its box/canvas |

## Per-figure accuracy cross-check (figure vs. chapter text)

| Figure | Verified against | OK |
|---|---|---|
| 01-fig-01 stages+durations | Ch 1 process list | ✓ |
| 01-fig-02 Maya plan | Ch 1 worked example | ✓ |
| 02-fig-01 present/past/why | Ch 2 worked example | ✓ |
| 03-fig-01 INNER/LEFT/RIGHT | Ch 3 join table (Wikipedia-sourced) | ✓ |
| 04-fig-01 pattern→function | Ch 4 pattern list | ✓ |
| 05-fig-01 4.0% vs 4.3%, CI overlap | Ch 5 worked example | ✓ |
| 06-fig-01 messy→pivot | Ch 6 worked example | ✓ |
| 07-fig-01 correct vs AI pipeline | Ch 7 worked example | ✓ |
| 08-fig-01 PACE (Google) | Ch 8 (fact-checked attribution) | ✓ |
| 09-fig-01 STAR segments | Ch 9 worked example | ✓ |
| 10-fig-01 scores S3/SQL2/Stat1/Case2/Beh2 | Ch 10 worked example | ✓ |

## Accepted notes (not defects)

- **06-fig-01 (messy sheet):** monospace column alignment is approximate because the render uses a fallback monospace font; still clearly columnar and legible. Accepted.
- All figures render with fallback fonts (EB Garamond→serif, Inter→sans, JetBrains→mono) since brand fonts aren't installed here; DESIGN.md sanctions these fallbacks.

## Verdict

**0 unresolved flags.** Layout and notation clean; every figure matches its chapter text. Re-run `DRY_RUN=1 node scripts/svg-visual-audit.mjs` when Node is available for the deterministic confirmation.
