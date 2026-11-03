# FACTCHECK — Lost in the Middle

Status: **GATE F CLOSED — 2026-10-02.** The central finding is quoted verbatim
from a peer-reviewed paper. No per-model figure is claimed anywhere.

| # | Beat | Claim (as spoken / shown) | Verdict | Source |
|---|---|---|---|---|
| 1 | B00 | A model can miss something that was inside the context window | ✅ PASS | Follows from S1 — the paper's whole subject |
| 2 | B01 | Where information sits in the window changes how reliably it is used | ✅ PASS | S1, verbatim |
| 3 | B02 | Experimental design: one answering document, buried in irrelevant ones, slid through positions | ✅ PASS | S1/S3 — this is the paper's multi-document QA setup, described in words |
| 4 | B02 | On-screen line names "multi-document QA and key-value retrieval" | ✅ PASS | S3 — the two tasks evaluated |
| 5 | B03 | The shape is strong at both ends, sagging in the middle | ✅ PASS | S2 — the U-shaped curve |
| 6 | B03 | On-screen caption states the curve is an **illustration, not measured values** | ✅ PASS | Deliberate. The shape is from the paper; the specific numbers plotted are invented for legibility and labelled as such. |
| 7 | B03 | "the same curve you get from people asked to memorise a list" | ✅ PASS | Stated as a resemblance (primacy/recency), not as a claim that the mechanisms are the same. No cognitive-science source is asserted. |
| 8 | B04 | The on-screen quotation | ✅ PASS | S1, **verbatim**, with full attribution on the card |
| 9 | B04 | "even for explicitly long-context models" | ✅ PASS | S1, verbatim — part of the same sentence |
| 10 | B05 | "A bigger context window is not a bigger attention span" | ✅ PASS | Editorial restatement of S1; no new claim |
| 11 | B06 | The four remedies | ✅ PASS | **Engineering advice**, framed as such. Each follows directly from the position-dependence in S1; none is presented as a measured result. |

## Claims deliberately CUT

- **Every per-model accuracy number in the paper.** They are specific to the
  models and context lengths tested and quoting them as current would
  misrepresent them.
- The common paraphrase that models "ignore" the middle. The paper says
  performance *degrades*, and the reel says degrades.
- Any claim that a named current model does or does not still show the effect.
  Not tested here, so not claimed.

## Scope check

The reel describes a finding about retrieval-style tasks and says so on screen.
It does not generalise to all long-context behaviour.
