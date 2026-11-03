# FACTCHECK — agentic-design-patterns-part-3

DOUBLE-CHECK LAW: every claim spoken or shown, checked against the source and
rewritten in the HAI Plain register. Source: `agentic-patterns-part3.md`
(Master Class Part 3), in `Agentic Design Video/`.

| # | Claim (beat) | Verdict | Source |
|---|---|---|---|
| 1 | Boss-worker isolates failure but bottlenecks (B03) | ✓ | §P14, "boss-worker topology isolates failure vectors but risks a central bottleneck" |
| 2 | Pure peer-to-peer produces useless loops (B03) | ✓ | §P14, "pure democracy topology is prone to extreme hallucination and infinite loops of useless discussion" |
| 3 | Cap the message budget or agents loop forever (B03) | ✓ | §P14 Q&A, "strict maximum message budget (e.g., N = 10)"; "automatic loop-breakers, strictly bounded message counts" |
| 4 | Complexity classifier routes to cheap/standard/reasoning (B04) | ✓ | §P15 diagram, simple → cheap/fast; medium → standard; complex → reasoning model |
| 5 | "Can halve the bill" in high-volume systems (B04) | ✓ *softened* | §P15 Pros says "often over 50%". Narration says "can halve the bill" — a conditional, weaker than the source's claim. Deliberate. |
| 6 | Misjudged complexity breaks hard tasks or wastes tokens (B04) | ✓ | §P15, "complex tasks get broken by weak models, and cheap tasks waste expensive reasoning tokens" |
| 7 | Tree of Thoughts = branch, score, prune (B05) | ✓ | §P16, "generating multiple parallel branches of thought, scoring their viability, pruning low-scoring branches" |
| 8 | Chess-player analogy (B05) | ✓ | §P16, "A grandmaster evaluating multiple future chess variations, mentally pruning weak lines" |
| 9 | Unusable for interactive applications (B05) | ✓ | §P16 Cons, "Extreme token consumption; unviable for real-time interactive user applications" |
| 10 | Evaluation = pre-deploy / in-flight / production (B06) | ✓ | §P17 diagram, golden test suite → SLA & cost monitoring → drift & anomaly detection |
| 11 | Static golden sets go stale; feed graded runs back (B06) | ✓ | §P17, "Static test sets get stale. Continuous ingestion of validated, human-graded production runs… is required" |
| 12 | Guardrails = PII redaction → injection check → model → output moderation (B07) | ✓ | §P18 diagram, verbatim chain |
| 13 | Canned journeys remove most of the attack surface (B07) | ✓ | §P18, "replacing open-text input fields with canned response workflows limits malicious input vectors entirely" |
| 14 | Guardrails cost latency and false positives (B07) | ✓ | §P18 Cons, "Introduces latency; false positives can frustrate users" |
| 15 | Priority scores on value, time sensitivity, effort, risk (B08) | ✓ | §P19, the composite formula `Score = (Value · TimeSensitivity) / (Effort · Risk)` |
| 16 | Completing a task forces a re-rank (B08) | ✓ | §P19, "Completing one task shifts the environment state, requiring the system to recalculate dependencies and rerank" |
| 17 | Agents thrash; non-deterministic order is hard to debug (B08) | ✓ | §P19, "agents to thrash between unrelated tasks"; Cons, "Non-deterministic execution order makes debugging highly complex" |
| 18 | Exploration = goal → map → cluster → investigate → report (B09) | ✓ | §P20 diagram, verbatim chain |
| 19 | Most token-hungry; must filter aggressively (B09) | ✓ | §P20, "Massively intensive; requires agent structures to summarize and filter non-essential information rapidly" |
| 20 | The five-step interview blueprint (B10) | ✓ | §Conclusion, all five steps verbatim in order: scope the goal (linear vs dynamic) · define workers · address trade-offs (cost/latency/accuracy) · guardrails + exception recovery · design the state machine |
| 21 | "Do not jump into writing code" (B10) | ✓ | §Conclusion, "do not jump into writing code" |
| 22 | "Patterns 14–20 of 20" (B02) | ✓ | Source header; Parts 1–2 established the 20-pattern scope |

## Corrections and editorial notes

- **"The constraints are the design" is OUR thesis.** Closer to the source than
  Part 2's was — the source's own opening says the expert/intermediate
  difference is "production constraints, safety guardrails, cost-resource
  trade-offs" — but the framing that all seven *subtract* capability on purpose
  is ours. Flagged as interpretation.
- **Both formulas cut**, consistent with Part 2's precedent: the priority score
  `(Value · TimeSensitivity) / (Effort · Risk)` is taught as its four inputs
  rather than shown as an equation. At ~21s a beat the formula consumes the beat.
- **Named model families cut.** The source names "o1/o3-class" models as the
  expensive tier. On screen this is "Reasoning · expensive". Model names date a
  video faster than anything, and the tier is the lesson, not the vendor.
- **The source's typo not reproduced:** §P16 writes "BFS (Breaded-First Search)"
  for Breadth-First Search. Search algorithms were cut from the reel entirely
  (extraneous at this length), so the error does not propagate.
- **"Over 50% cost reduction" softened to "can halve the bill"** — the source
  asserts it flatly with no citation that can be checked; the reel states it
  conditionally.
- **B11 ("when not to") has no counterpart in the source**, which advocates each
  pattern. Written independently, consistent with Parts 1 and 2.
- **Bracketed citation markers** (`[46]`, `[57, 58]`…) index a bibliography not
  reproduced in the notes; not followed, and no claim rests on one alone.

## Dating risk

No model names, versions, vendor pricing or benchmark numbers appear on screen.
The one figure spoken ("halve the bill") is presented conditionally. The reel
should not date.
