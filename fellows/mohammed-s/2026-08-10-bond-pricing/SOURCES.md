# SOURCES — hussain-bond-pricing-duration

## Formulas / textbook grounding
- Hull, J. C. — *Options, Futures, and Other Derivatives* — bond pricing,
  Macaulay/modified duration, convexity (standard chapter on interest-rate risk).
- Fabozzi, F. J. — *Fixed Income Mathematics* — duration and convexity
  formulas, the par-bond worked example this reel's numbers resemble.
- These are the same two references the sibling `claude-for-finance/
  bond-pricing-duration` project cited; this build independently recomputed
  every number from the closed-form formulas (see FACTCHECK.md) rather than
  reusing that project's figures, two of which did not check out.

## Numbers
All price/duration/convexity figures on screen are computed directly from
the formulas in FACTCHECK.md for a hypothetical 5%-coupon, 10-year, $1,000
face-value bond — not sourced from a live market dataset. No real-world
issuer, ticker, or market yield is claimed anywhere in this reel.

## Corrections logged (DOUBLE-CHECK LAW)
See FACTCHECK.md "Correction applied" — the prior sibling project's
Price(2%)=$1,404 and "Macaulay duration 7.7yr" claims were arithmetic/labeling
errors; corrected to $1,269.48 and Macaulay 8.11yr / Modified 7.72yr here.

## Provenance
- No pantry media (stills/footage) used in this build — every visual is
  Manim (native) or a Remotion scene (Claude UI fidelity components).
- Voice: Kokoro `am_onyx` ("Onyx"), free/local — no ElevenLabs, no API key.
