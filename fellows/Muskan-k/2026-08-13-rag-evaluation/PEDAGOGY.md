# PEDAGOGY — Where RAG Breaks. (claude-hai · teaching explainer, ~90s)

**The ONE insight:** RAG fails in two stages, so measure both. Recall/Precision
grade *what you fetched*; Answer Relevance/Faithfulness grade *what you wrote*.
The metric that drops tells you which stage to fix.

**Audience (HAI):** practitioners/learners building RAG; skeptical spine —
"measure before you guess."

## Act structure (framework-first)
- B00 cold-open ask (composer), answered ✓
- B01 the framework GRAPHIC (two-stage pipeline) — shown BEFORE the metrics ✓
- B02 retrieval metrics (recall + precision, Venn) · B03 generation metrics
  (relevance + faithfulness) — the two axes each ✓
- B04 failure-localization 2×2 (the reusable diagnostic / payoff) ✓
- B05 handoff (scaffolded task) · B06 title outro ✓
- Body B01–B04 = 4K cards; UI only at B00/B05/B06 (ILLUSTRATE LAW).

## Correctness discipline (DOUBLE-CHECK LAW — standard definitions, no invented numbers)
| On screen | Standard definition |
|---|---|
| Recall | relevant-and-retrieved ÷ all-relevant (Venn: overlap ÷ Relevant circle) |
| Precision | relevant-and-retrieved ÷ all-retrieved (Venn: overlap ÷ Retrieved circle) |
| Answer Relevance | does the answer address the question |
| Faithfulness | is every claim grounded in the retrieved context (no hallucination) |
| How measured | retrieval → labeled ground-truth; generation → LLM-as-judge |
| Failure localization | retrieval metrics low → fix context (chunking/embeddings/top-k); generation low → fix prompt/model |

No product/version claims; only the generic, widely-accepted metric definitions.

## PROOF intent (baked in up front)
- Framework shown before examples (B01). Reusable rubric = the 2×2 (B04).
- "How measured" footers act as the method/source. Active task = B05.

## Narration review (GATE P)
Listen for: does each metric's visual enact its definition (the Venn ratios, the
answer↔question / answer↔context arrows)? Is the diagnostic earned?

VERDICT: PASS — sign "VERDICT: PASS" after review.
