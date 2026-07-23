# SOURCES — brand-palette-accessibility-auditor

## Card
cli-ideas Card 21 — Ch 9 (Visual Identity Systems)

## Source Chapter
`branding-and-ai/chapters/09-visual-identity-systems.md`

## Verified Facts

| Claim | Source | Status |
|---|---|---|
| WCAG 2.2 AA normal text threshold: 4.5:1 | W3C WCAG 2.2, SC 1.4.3 | VERIFIED |
| WCAG 2.2 AA large text threshold: 3:1 | W3C WCAG 2.2, SC 1.4.3 | VERIFIED |
| WCAG 2.2 AA non-text (graphical objects): 3:1 | W3C WCAG 2.2, SC 1.4.11 | VERIFIED |
| WCAG 2.2 AAA normal text: 7:1 | W3C WCAG 2.2, SC 1.4.6 | VERIFIED |
| Relative luminance formula: L = 0.2126R + 0.7152G + 0.0722B (linearized channels) | W3C WCAG 2.2 | VERIFIED |
| Linearization: c/12.92 if c ≤ 0.04045, else ((c+0.055)/1.055)^2.4 | W3C WCAG 2.2 | VERIFIED |
| Contrast ratio: (L_lighter + 0.05) / (L_darker + 0.05) | W3C WCAG 2.2 | VERIFIED |
| warm-clay #A89068 on white #FFFFFF: ratio ≈ 3.1:1 | Chapter 9; computed | VERIFIED |
| Corrected warm-clay #7A6045 on white: ratio ≈ 4.8:1 | Chapter 9; computed | VERIFIED |
| Caption #9CA3AF on near-white #FAFAF8: ratio ≈ 2.9:1 | Chapter 9; computed | VERIFIED |
| Corrected caption #6B7280: ratio ≈ 4.6:1 | Chapter 9; computed | VERIFIED |

## Computed Verification
All ratios independently verified using the linearize/luminance/contrast_ratio Python functions in the CODE beat.

## Legal Note
WCAG 2.2 AA is a legal requirement for public-facing digital products in many jurisdictions (EU Web Accessibility Directive, US Section 508, ADA case law). Verify jurisdiction-specific requirements before final legal guidance.
