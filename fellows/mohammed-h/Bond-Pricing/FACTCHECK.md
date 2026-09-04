# FACTCHECK — hussain-bond-pricing-duration

Bond: face = $1,000, annual coupon = 5% ($50/yr), maturity = 10 years.
All figures below are independently recomputed from the closed-form formulas
(no external dataset — this is a hypothetical teaching bond), and cross-checked
against the standard fixed-income references in SOURCES.md.

price(y)     = Σ C/(1+y)^t + F/(1+y)^T
MacDur(y)    = [Σ t·C/(1+y)^t + T·F/(1+y)^T] / price
ModDur(y)    = MacDur / (1+y)
Convexity(y) = [Σ t(t+1)·C/(1+y)^(t+2) + T(T+1)·F/(1+y)^(T+2)] / price

## Claims verified (this build)
- Price at par: YTM = 5% → price = $1,000.00 exactly ✓ (coupon rate = yield ⇒ par, textbook identity)
- Price(2%) = $1,269.48 ✓ (recomputed; see correction below)
- Price(3%) = $1,170.60 ✓
- Price(7%) = $859.53 ✓
- Price(10%) = $692.77 ✓
- Macaulay duration at par (YTM=5%) = 8.11 years ✓
- Modified duration at par = MacDur/(1.05) = 7.72 years ✓
- Convexity at par = 75.00 ✓
- Duration-only estimate, +2% shock (→7%): $845.57 vs actual $859.53 (off by $13.96, ≈1.4% of par) ✓
- Duration+convexity estimate, +2% shock: $860.56 vs actual $859.53 (off by $1.04) ✓
- Duration-only estimate, −2% shock (→3%): $1,154.43 vs actual $1,170.60 (off by $16.17, ≈1.6% of par) ✓
- Duration+convexity estimate, −2% shock: $1,169.43 vs actual $1,170.60 (off by $1.17) ✓
- Convexity is always positive for an option-free (non-callable) bond ✓ (standard result)
- Callable bonds exhibit negative convexity above par — NOT used as a hard number in
  this build; mentioned only as a "next steps" direction in the handoff, no figure claimed.

## Correction applied — the prior project's numbers do not check out
The earlier `claude-for-finance/bond-pricing-duration` build (this repo's sibling
project, same topic) claimed:
  - Price(2%) ≈ **$1,404** — recomputed value is **$1,269.48**. $1,404 does not
    solve the standard price formula for this bond at 2% (it corresponds to a
    yield near 1.1–1.2%, not 2%). Its own FACTCHECK.md shows the correct
    per-term math (`50/1.02^t ... + 1000/1.02^10 ≈ 1404`) but the arithmetic
    sums wrong — the true annuity+face sum at 2% is $1,269.48, not $1,404.
  - "Macaulay duration of 7.7 years" — **7.72 is the MODIFIED duration**, not
    Macaulay. The true Macaulay duration for this bond at par is **8.11 years**.
    The old build's code comment then divided 7.72 by 1.05 again to get 7.35 —
    a double-discounting error compounding the mislabel.
This build uses the corrected values throughout (beat_sheet.json, scenes.py).

## What must still be verified (before treating this as authoritative beyond
## the classroom example above)
- [VERIFY: primary-source citation] The Macaulay-duration concept originates
  with Frederick Macaulay (1938); this build does not quote or cite that paper
  directly — narration and visuals rely on the standard closed-form formulas
  as given in Hull and Fabozzi (see SOURCES.md), not on a fetched primary text.
- [VERIFY] The "duration hedge with Treasury futures" and "callable bond
  negative convexity" lines in B09's handoff prompt are standard textbook
  extensions, not computed or verified figures in this build — no numbers are
  asserted for them on screen or in narration.
