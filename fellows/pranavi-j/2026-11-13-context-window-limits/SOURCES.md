# Sources — Context Window Limits: The Budget That Doesn't Grow

General AI/STEM topic explainer. A transformer-based language model's context window — the fixed
number of token positions it can attend to at once, shared by everything in a single request
(system instructions, any retrieved or pasted-in documents, conversation history, and the room
reserved for the model's own output) — is a well-established, broadly-taught architectural fact
about how these models consume input, not a claim specific to any one vendor, company, product, or
benchmark. This video describes the general, settled shape of the idea qualitatively: what a
context window actually is (a token budget, not a character or word budget), why everything
sharing a single request competes for the same fixed pool, and what the two broad classes of
overflow behavior look like (an explicit error/rejection vs. an implicit truncation). It does not
cite a specific paper's numeric result, name a specific company, product, or dataset, or claim any
one real system's current context-window size — window sizes vary enormously across systems and
change over time, and remain an active area of engineering work across the field.

Four broad, well-documented qualitative points anchor this video's rubric and are described
generically, with no specific paper, author, company, or vendor named and no fabricated statistic
claimed as a real system's measurement:

- **Tokens, not characters or words:** text is converted into tokens — sub-word units produced by
  a tokenizer — before a transformer-based language model processes it, and the model's context
  window is a fixed number of token positions, not a fixed character or word count. Because the
  mapping from characters/words to tokens is not 1:1 and varies by language, punctuation, and
  content, estimating a budget by eye (counting words or characters) is a common, well-documented,
  fixable source of error. This is a structural/definitional fact about how these models are built
  and trained, not a benchmarked claim.
- **One shared pool, not separate budgets:** system instructions, retrieved or pasted-in documents,
  conversation history, and the output the model is asked to produce are all part of the same
  single sequence a transformer-based model processes at once; they are not drawn from separate,
  independently-sized budgets. Growing any one of them necessarily shrinks the room available to
  the others. This is a well-established architectural fact, stated here generically.
- **Two broad classes of overflow behavior:** when a request's total token count would exceed the
  available budget, systems that wrap or serve a language model broadly fall into two documented
  patterns — rejecting the request outright with an explicit error before generating a response, or
  implicitly truncating some portion of the input (commonly the oldest conversation turns, under a
  "sliding window" approach, though other truncation strategies are also documented) and proceeding
  without necessarily surfacing to the caller what was dropped. Both patterns are broadly discussed
  in software-engineering and applied-AI practice around building on top of language models; this
  video states this generically, as "a system can do either," not as a universal behavior of any
  one named system.
- **Filling the window has a real, non-zero cost even under the limit:** every token inside the
  context window — not just tokens that exceed it — consumes real compute, and in metered systems,
  real latency and/or monetary cost, whether or not the budget is ever exceeded. This is a general,
  well-documented operational fact about how these systems are typically priced and run, stated
  here qualitatively with no specific real pricing figure cited for any named system.

No specific real model, vendor, product, or dataset is named or benchmarked anywhere in this
video, and no specific context-window size is cited as if it were a current, universal fact about
any named system. The worked example (B04, an illustrative 1,000-token budget shared by fixed
instructions, a pasted-in document, and a growing conversation history, with the oldest turns
silently dropped) and its falsifiability case (B05, the identical scenario and overflow, but with
the system checking the total and refusing outright instead) are both fully generic and
illustrative, matching the pattern used in this fellow's prior STEM videos (e.g. the call-center
average-handle-time example in the Goodhart's Law video, the toy Caesar-shift example in the
in-context-learning-limits video, the "strawberry" tokenization example, the fabricated-citation
hallucination example).

## Real-world tie-in (kept generic)

This week's companion project-update video separately covers a real engineering bug where a UI had
no cap matching a backend's hard limit on how many items a single request could carry — a live
instance of the general phenomenon this STEM video explains (a hard capacity limit that bites you
if nothing on the sending side respects what the receiving side can actually hold). Per the house
rule, that specific incident is not named, described, or otherwise identified anywhere in this
video; see `FACTCHECK.md`.

## Distinct from adjacent, already-covered topics in this series

- `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` covers whether a claim is
  fabricated at all. Unrelated to this video's topic (capacity, not fabrication).
- `2026-09-29-tokenization-why-ai-cant-count-its-own-letters` covers how text is chunked into
  tokens. This video assumes tokenization has already happened and is about what happens once the
  resulting count exceeds a fixed ceiling.
- `2026-10-06-lost-in-the-middle-why-more-context-isnt-better` covers where in a long context
  (that DOES fit) a fact sits and whether position affects retrieval. This video covers what
  happens when content does NOT fit at all.
- `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason` covers whether a stated
  reasoning trace actually caused the answer. Unrelated to this video's topic.
- `2026-10-21-calibration-why-confidence-isnt-accuracy` covers whether a stated confidence number
  tracks real accuracy for a single prediction. Unrelated to this video's topic.
- `2026-10-28-in-context-learning-limits` covers what a prompt alone can teach a model with no
  weight updates — a mechanism question. This video covers the capacity ceiling of the context
  window itself and what happens at and past it — a distinct, capacity-and-overflow question. See
  `FACTCHECK.md` for the one-sentence distinction used in this video's own narration/premise.
- `2026-11-04-goodharts-law-proxy-metrics` covers a tracked number diverging from its real target
  under incentive pressure. Unrelated to this video's topic (a fixed resource constraint, not a
  metric-divergence question).
