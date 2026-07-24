# FACTCHECK — package-hallucination-scanner

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B00 | requests_oauth_helper does not exist on PyPI | ✓ | Verified as of 2025; no such package on pypi.org |
| B03 | PyPI JSON API: pypi.org/pypi/{package}/json returns 404 for non-existent packages | ✓ | PyPI API documentation |
| B03 | ast module handles 'import X' and 'from X import Y' patterns | ✓ | Python stdlib ast docs |
| B05 | npm registry search endpoint: registry.npmjs.org/-/v1/search | ✓ | npm registry API documentation |
| B07 | Hallucination rate low but recurrence rate high (same names across outputs) | ✓ | Spracklen et al. 2024-25: 58% of fabricated names recur across queries |

## Illustrative / Synthetic

- react-query-optimizer-v3 as npm hallucination example — synthetic
- Specific scan output examples — illustrative

## Sources

- Spracklen et al. 2024-25 USENIX Security: slopsquatting analysis
- PyPI JSON API: pypi.org/pypi/{package}/json
- npm registry API: registry.npmjs.org/-/v1/search

## Exclusions Confirmed

- No full supply-chain security methodology ✓
- No PyPI moderation policy ✓
- No cross-ecosystem deep comparison ✓
