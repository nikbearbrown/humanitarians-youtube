# FACTCHECK — agentic-design-patterns-part-1

DOUBLE-CHECK LAW: every claim spoken or shown, checked against the source and
rewritten in the Plain register. Source: `agentic-patterns-part1.md`
(Master Class Part 1), in `Agentic Design Video/`.

| # | Claim (beat) | Verdict | Source / derivation |
|---|---|---|---|
| 1 | Chaining degrades past 3–5 steps (B03) | ✓ | Source §Pattern 1, "The Magic Number (3 to 5)… beyond 3 to 5 steps, LLMs suffer from cognitive fatigue" |
| 2 | Errors cascade through a chain (B03) | ✓ | §Pattern 1, "that error will cascade and propagate through every subsequent node" |
| 3 | Chaining needs typed data contracts (B03, shown as the Validate gate) | ✓ | §Pattern 1, "Hard contracts (often JSON schemas) must be established between steps" |
| 4 | Routers are overconfident; use a threshold (B04) | ✓ | §Pattern 2, "models tend to be overconfident"; "If confidence is below a certain threshold (e.g., 8/10), the system must request clarification" |
| 5 | Router is a single point of failure (B04) | ✓ | §Pattern 2 Cons, "Single point of failure (if the router fails, the entire application fails)" |
| 6 | Parallelization needs queue + token bucket + backoff (B05) | ✓ | §Pattern 3, "token buckets, rate limiters, and exponential backoff"; Q&A names a message queue and 429 retries |
| 7 | Parallel outputs must be normalized before merge (B05) | ✓ | §Pattern 3, "The merger component must normalize the data" |
| 8 | Reflection costs two calls per cycle (B06) | ✓ (derived) | §Pattern 4 says "each revision cycle consumes input and output tokens" and the loop is generator + critic — two agent calls per pass. Arithmetic, not a source figure. |
| 9 | Cap the reflection loop at 2–3 (B06) | ✓ | §Pattern 4, "maximum 3 attempts"; Q&A, "a maximum loop counter (usually set to 2 or 3)" |
| 10 | Models hallucinate tool parameters (B07) | ✓ | §Pattern 5, "LLMs frequently hallucinate tool parameters" |
| 11 | Read-only credentials + human approval for destructive ops (B07, B09) | ✓ | §Pattern 5 Q&A, "restricted to a read-only replica"; "require manual approval in the UI" |
| 12 | Planning builds a DAG and checks constraints before executing (B08) | ✓ | §Pattern 6, "logical tree or DAG"; "evaluate hard constraints—such as API token budgets, execution deadlines, and authorization permissions—before generating the… plan" |
| 13 | Planning re-plans on failure rather than crashing (B08) | ✓ | §Pattern 6, "the planner shouldn't just crash… adjust the remaining steps" |
| 14 | Planning is hard to debug (B08) | ✓ | §Pattern 6 Cons, "debugging a dynamic dependency graph can be incredibly difficult" |
| 15 | "Twenty patterns, six in part one" (B02) | ✓ | Source intro, "We will break down all 20 patterns"; §Part 1 Overview lists exactly 6 |
| 16 | Single-prompt engineering is "over" (B00) | ✓ *de-sensationalized* | Source opens with "the era of 'single-prompt engineering' is officially over." Narration reframes this as a conditional — prompts fail *in production, at multi-step tasks* — rather than repeating the absolute. |

## Corrections applied

- **De-sensationalized the opening.** The source's "officially over" is a
  rhetorical claim about interviews. B00 narrates the mechanism instead (a
  notebook prompt failing in production) and B10 explicitly defends the case
  where a single call is still correct — which the source never does.
- **"Three change what runs / three change how it thinks" (B02) is our
  framing**, not the source's. The source groups all six as "core structural
  and operational patterns." Ours is a teaching aid; it makes no factual claim
  and is flagged here as an editorial device.
- **Dropped the bracketed citation markers** (`[1]`, `[3, 6]` …). The source's
  reference numbers point to a bibliography not included in the file, so they
  could not be verified and are not reproduced on screen.
- **No numbers invented.** The only figures on screen are 3–5 (chain ceiling),
  ≥8 confidence, 2–3 (loop cap), 20 and 6 (pattern counts) — all sourced above.

## Dating risk

No model names, version numbers, vendor pricing, or benchmark figures appear in
narration or on screen. The reel should not date.
