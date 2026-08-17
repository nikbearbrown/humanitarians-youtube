# FACTCHECK — How Facial Recognition Actually Works (And When It Shouldn't)

Status: **Resolved 2026-08-03 — verified against NISTIR 8280 directly, before narration was locked (not after, as a correction).**

| # | Beat | Claim (as spoken) | Verdict | Source / derivation |
|---|---|---|---|---|
| 1 | B01 | Pipeline is detect -> embedding -> compare to database -> similarity score, not a binary match | PASS | Standard, well-documented face-recognition architecture; consistent with NIST's own FRVT methodology description |
| 2 | B01 | "A 98% match is a probability, not a certainty" | PASS | Consistent with how similarity scores/thresholds work in every FRVT-tested system; illustrative percentage, not attributed to a specific vendor |
| 3 | B02 | Legitimate uses: accessibility, phone unlock, missing-persons reunification, medical diagnosis support | PASS | Widely documented, uncontroversial use cases; no specific vendor/product named |
| 4 | B03 | Harmful uses: mass surveillance, unconsented retail tracking, biometric data can't be reset like a password | PASS | Widely documented concern categories in the public policy debate; "can't be reset" is a factual property of biometric identifiers vs. passwords |
| 5 | B04 | NIST tested 189 algorithms on 18+ million images | PASS | NISTIR 8280 (2019): 189 algorithms from 99 developers, 18.27 million images of 8.49 million people — see SOURCES.md |
| 6 | B04 | Most algorithms show real accuracy differences across demographic groups, generally worse for women and darker skin | PASS | NISTIR 8280 finding, corroborated by NIST's own Dec 2019 news release |
| 7 | B04 | Best-performing algorithms show those gaps shrink to nearly nothing | PASS | NISTIR 8280 — some of the most accurate one-to-many algorithms showed similar false-positive rates across demographic groups |
| 8 | B04 | "Some industry voices argue the disparity is overstated" | PASS | Security Industry Association's Feb 2020 response piece takes this position — cited directly, not left vague |
| 9 | B05 | "Fluency trap" analogy (a precise-looking number can feel like a settled fact) | PASS (framing, not an empirical claim) | Editorial framing device connecting to the fellow's own prior work; not presented as a scientific finding |
| 10 | B06 | Closing thesis: scrutiny should scale with stakes, not a fixed policy verdict | PASS (editorial stance, not an empirical claim) | Consistent with the balanced-tone brief; does not assert a specific regulatory position |

## Balance check

The script states the NIST finding of real demographic gaps AND the fact that
gaps shrink for top-tier algorithms AND that an industry-aligned source
disputes the framing — all three in the same beat (B04), not split across
beats in a way that would bury one side. No claim in this script asserts a
policy conclusion (ban/regulate/expand) — B06 states only that scrutiny
should scale with stakes, which is compatible with multiple policy views.

No corrections were required — the original draft (verified before lock) is
the same as what's in `beat_sheet.json`.
