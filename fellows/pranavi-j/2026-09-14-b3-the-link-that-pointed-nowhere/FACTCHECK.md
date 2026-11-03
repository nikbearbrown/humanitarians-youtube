# FACTCHECK — The Link That Pointed Nowhere

Status: **RESOLVED — fellow reviewed 2026-09-17. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | Every Google News item's stored link was a dead-end redirect; the `url=` regex never matches modern links | PASS | `B3-VERIFICATION.md` "The bug" — confirmed live 2026-07-24 (`FINDINGS.md`) and re-confirmed this session | — |
| 2 | B04 | The real-URL resolution mechanism (signed id/timestamp/signature POSTed to an internal Google endpoint) | PASS, **with a framing note** | `B3-VERIFICATION.md` "Why it's not a simple regex/302 fix" — explicitly an undocumented, reverse-engineered internal API, "the same technique documented by third-party Google-News-link decoders; verified independently here" | Narration must not imply this is a stable, documented public API — it's reverse-engineered and could change or be blocked without notice. Beat sheet draft already frames it as internal/undocumented; keep that framing. |
| 3 | B05 | The classification-ordering near-miss (would have silently broken Google News labeling once unwrapping started working) | PASS | `B3-VERIFICATION.md` "Critical ordering fix, caught before deploying" — explicit in source | — |
| 4 | B06 | The three escalating verification rounds (20/20, 16/16, 6/6) | PASS | `B3-VERIFICATION.md` "Live verification" — all three rounds documented with exact counts | — |
| 5 | B06 | "All six still correctly labeled" | PASS | `B3-VERIFICATION.md`: "All 6 still correctly classified as FINRA Enforcement News" | — |
| 6 | B07 | "I haven't verified this on the fellow's actual n8n instance" | PASS — this is the source doc's own stated limitation | `B3-VERIFICATION.md` "What's NOT verified — flagged, not assumed": "not verified here — I have no live n8n to test against, only the workflow JSON" | — |
| 7 | B07 | "~400 extra requests per run, spread out on purpose" | PASS | `B3-VERIFICATION.md`: "roughly 400 extra requests per run... Sequential, not parallelized, by deliberate choice" | — |
| 8 | *(implicit, not in script)* | That this fix has already run successfully in the fellow's live production n8n workflow | **NOT CLAIMED — do not add** | Source doc is explicit this is unverified against live n8n | Keep the script scoped to "verified against the workflow file and a full local re-implementation," not "verified in production" |

## Dramatization check

No beat overstates the fix as production-proven, or presents the reverse-engineered API as a
stable, documented one. The main risk in this reel is implying more certainty than the source
material supports — B04's mechanism explanation and B07's honest limits are the two places this
matters most, and both are drafted with the qualifying language intact.

## Resolved 2026-09-17

1. **B04 framing** (row #2): strengthened — a small on-screen caveat label ("reverse-engineered —
   not a documented/official API") added directly to the flow diagram.
2. **B07 limitations**: kept exactly as drafted, no softening, no change.

Both open items are closed. Gate P (narration review) can proceed.
