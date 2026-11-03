# PEDAGOGY — Reading the Claims (hai cli-explainer, patent agent progress video 4)

A progress-recap video documenting the real classifier build for claim protection scope, a genuine model refusal and its graceful handling, and the full ClaimsAgent class built and tested end-to-end.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real spread of word counts across 9 known independent claims, with no clean line ✓
- B01 — the real evidence that word count / limitation markers don't predict scope, which is why an LLM call was used instead of a heuristic ✓
- B02 — the first real classification result, with its actual breadth/posture/caveat ✓
- B03 — the real refusal encountered (verbatim stop_reason and category) ✓
- B04 — the honest fix: catch it, mark unclear, name the reason — not routed around ✓
- B05 — the real class structure (ClaimReading, PatentClaimsReading, ClaimsAgent) ✓
- B06 — the real end-to-end test result, matching the independently verified claim counts ✓
- B07 — HANDOFF, a runnable prompt that explicitly tells the viewer to read the caveat, not just the label ✓
- B08 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "word counts from forty-seven to three hundred and three" | Real output of inspect_independent_claims.py, this session | OK — exact real figures |
| The first classification's breadth/posture/reasoning/caveat | Real Claude API response, this session | OK — the actual returned JSON fields |
| The real refusal (stop_reason, category "bio") | Real debug output from this session's actual API call | OK — literal field values |
| "seventeen claims, one independent, sixteen dependent" | Real end-to-end test output, matching the independently verified count from earlier in the session | OK — cross-checked against prior verification, not just trusted on its own |

## Friction protected

- Kept: B03 presents the refusal as a real, structural limitation rather than glossing over it as a fixed edge case — the video is honest that some real patents, especially biotech/pharma, won't get an automated reading at all.
- Kept: B07's handoff explicitly directs the viewer to the confidence caveat, not just the classification label — reinforcing the same discipline the video itself demonstrated.

VERDICT: PASS
