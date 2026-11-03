# SOURCES — The Link That Pointed Nowhere

Primary source for every measured claim in this beat sheet:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/B3-VERIFICATION.md` (dated 2026-08-31) — the
  bug, the reverse-engineered resolution mechanism, the classification-ordering near-miss, all
  three verification rounds, and the honestly-flagged unverified items.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md` — referenced by
  B3-VERIFICATION.md for the original 2026-07-24 confirmation that the bug existed.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the hardened n8n
  workflow copy containing the `unwrapGoogleNewsUrl()` fix and the reordered classification call.

## Claim → source mapping

| Beat | Claim | Source | Notes |
|---|---|---|---|
| B03 | The failing `url=([^&]+)` regex; modern Google News links carry no `url=` param | `B3-VERIFICATION.md` "The bug" | — |
| B04 | The id/timestamp/signature → internal endpoint resolution mechanism | `B3-VERIFICATION.md` "Why it's not a simple regex/302 fix" | Explicitly reverse-engineered/undocumented — keep that framing on screen |
| B05 | The classification-ordering near-miss | `B3-VERIFICATION.md` "Critical ordering fix, caught before deploying" | — |
| B06 | 20/20, 16/16, 6/6 verification rounds; all 6 correctly re-classified | `B3-VERIFICATION.md` "Live verification" | — |
| B07 | Unverified on live n8n; ~400 extra requests/run | `B3-VERIFICATION.md` "What's NOT verified" | Both are the source doc's own stated caveats, not inferred |

## Citation status (open)

- No claim in this beat sheet is sourced from anything outside the three files above.
- The resolution mechanism (B04) references "the same technique documented by third-party
  Google-News-link decoders" per the source doc, but does not name or link any specific
  third-party tool — kept general per the source material's own phrasing.
