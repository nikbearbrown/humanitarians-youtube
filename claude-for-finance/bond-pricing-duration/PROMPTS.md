# PROMPTS — bond-pricing-duration

## B01 — PROBLEM slate
Visual: price-yield curve, convex shape
Caption: "Bond price and yield move inversely. Duration measures how much."

## B06 — SUMMARY slate
Table: YTM | Duration approx dP | Actual dP | Error (convexity gap)
For 2% shock: error ~1.5%

## B07 — NEXT STEPS slate
Duration hedge: short Treasury future
Hedge ratio = Portfolio Duration / Future DV01

## B08 — NEXT STEPS 2 slate
Callable bond: negative convexity above par
price = min(call_price, option-free_price)
