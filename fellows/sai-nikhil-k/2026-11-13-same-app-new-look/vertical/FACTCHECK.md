# FACTCHECK — Same App, New Look

| # | Claim | On screen | How verified | Result |
|---|---|---|---|---|
| 1 | 11 findings, 5 proposed changes | B00 output, B04 line 1 | `runs/R-20261116-01/findings.json` (11), `decisions/` (5) | ✔ |
| 2 | None approved; on a branch | B04 narration + line 4 | ledger: 5× `decision.built_before_approval`, status `proposed`; `approvals/` empty; `git status` on `design/hai-brand` | ✔ |
| 3 | Faint text 2.83:1 before | B00, B02 row 2, B04 | `contrast.py`: #88979D on #F6F8F9 | ✔ 2.8325 |
| 4 | Faint text 6.16:1 after | B00, B02 row 3, B04 | `contrast.py`: #5E6265 on #FFFFFF | ✔ 6.158 |
| 5 | Text needs 4.5:1 | B02 row 1, note | WCAG 2.2 SC 1.4.3 (normal text) | ✔ |
| 6 | axe: 6 failures before, 0 after | B00, B03, B04 | `recapture.out`: label 1+1, color-contrast 2+2 (light only) | ✔ |
| 7 | 106 undecided before, 0 after | B03, B04 | `recapture.json` `contrast_undecided.bgGradient` 14+17+22 ×2 themes | ✔ |
| 8 | A decorative glow hid the background | B03 narration | axe messageKey `bgGradient`; old CSS line 81 `radial-gradient(… var(--glow) …)` on body; D-0002 removes it | ✔ |
| 9 | Old fonts never loaded | B01 narration | `recapture.json` `h1.loaded` = [] on all six before screens under the app CSP; [Inter Variable] after | ✔ |
| 10 | Inter bundled in the app | B01 narration + caption | D-0001; `main.tsx` imports `@fontsource-variable/inter`; Google Fonts @import removed | ✔ |
| 11 | One main button style | B01 narration | D-0003; visible in both plate panels (black vs red uppercase) | ✔ |
| 12 | Small text up to 12 px | B01 narration | D-0004 + R-02 "sentence text ≥ 12px" (ledger, not re-measured) | ledger only |
| 13 | Five changes named | B04 line 1 | D-0001…D-0005 titles | ✔ |

## Algebra

CR = (L_light + 0.05) / (L_dark + 0.05), L = 0.2126 R + 0.7152 G + 0.0722 B on
linearised sRGB (c ≤ 0.04045 → c/12.92, else ((c+0.055)/1.055)^2.4).

- Before: (0.9357 + 0.05) / (0.2980 + 0.05) = 0.9857 / 0.3480 = 2.8325 → 2.83
- After:  (1.0000 + 0.05) / (0.1205 + 0.05) = 1.0500 / 0.1705 = 6.1584 → 6.16

`build_beats.py --check` asserts the rounded luminances reproduce the rounded
ratios, and that 2.83 < 4.5 ≤ 6.16.

## Rendered-frame math review

<!-- filled after the render -->
