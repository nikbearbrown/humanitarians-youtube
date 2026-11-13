# B02 — Statistical Rigor

## Composition type
Remotion

## Layout
Dark stage. Three panels stacked vertically: bootstrap CIs, permutation test, power analysis.

## Elements

### Top panel: Bootstrap Confidence Intervals
- Two horizontal bars, one for "Model A" and one for "Model B."
- Each bar has a central dot (point estimate) and whisker lines extending left and right (95% CI).
- Model A whiskers: 0.18 to 0.24, point at 0.21.
- Model B whiskers: 0.20 to 0.27, point at 0.23.
- The intervals partially overlap, showing the uncertainty.
- Label: "bootstrap 95% CI (1,000 resamples)."

### Middle panel: Permutation Test
- A bell-shaped histogram of 10,000 permuted metric differences.
- The distribution is centered near zero (null hypothesis).
- A vertical red line marks the observed difference, sitting in the right tail.
- Shaded area beyond the red line shows the p-value region.
- Label: "permutation test, p = 0.03."

### Bottom panel: Power Analysis
- A smooth curve plotting statistical power (y-axis, 0.0 to 1.0) vs sample size (x-axis, 0 to 600).
- A horizontal dashed line at power = 0.80 (threshold).
- A vertical dashed line drops from the curve's intersection with 0.80 down to the x-axis.
- The x-axis intersection labeled: "need 340 more signals."
- Label: "power analysis."

## Animation sequence
1. Top panel: two bars animate with whiskers extending outward (2.5s).
2. "bootstrap 95% CI" label fades in (0.5s).
3. Middle panel: histogram bars grow upward, observed-difference line draws in red (2.5s).
4. "p = 0.03" label fades in (0.5s).
5. Bottom panel: power curve draws left to right, dashed lines appear at intersection (2.5s).
6. "need 340 more signals" label fades in (0.5s).

## Palette
- Model A bar: #4A90D9 (blue)
- Model B bar: #9B59B6 (purple)
- CI whiskers: same color as bar, lighter
- Histogram bars: #95A5A6 (grey)
- Observed difference line: #E74C3C (red)
- P-value shading: #E74C3C at 30% opacity
- Power curve: #27AE60 (green)
- Threshold lines: #F1C40F (gold, dashed)
- Background: #1A1A2E
