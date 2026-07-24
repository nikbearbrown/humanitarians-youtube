# FACTCHECK — three-check-deployment

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| Three-check deployment protocol: functional, environment, pedagogical | B01 | ✓ | Chapter 14: three-check protocol documented |
| Google Fonts CDN blocking on school networks | B04 | ✓ | Common real restriction — many school networks block external CDNs |
| aria-label for unlabeled buttons: WCAG 4.1.2 criterion | B06 | ✓ | WCAG 4.1.2: name, role, value — buttons must have accessible names |
| axe-core: real open-source accessibility testing tool | B05 | ✓ | axe-core is the real Deque Systems tool used in browser devtools |
| 375px as mobile breakpoint: standard (iPhone SE width) | B03 | ✓ | 375px is the standard iPhone SE viewport width |
| System-serif fallback when CDN font blocked | B04 | ✓ | CSS font-family fallback behavior: falls back to generic family |
| Environment check catches CDN issues that functional check misses | B01 | ✓ | Chapter 14: environment check specifically targets network dependencies |

## Illustrative scenarios
- Google Fonts CDN blocked: representative real failure mode, not a specific chapter example
- Pedagogical check questions: synthetic examples consistent with chapter 14
- All failure modes consistent with chapter 14 documented categories

## Exclusions verified
- No API key discussion: PASS
- No npm install walkthrough: PASS
