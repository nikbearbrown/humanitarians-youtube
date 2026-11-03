# Sources — In-Context Learning: What the Prompt Can (and Can't) Teach

General AI/STEM topic explainer. In-context learning (ICL) — a model conditioning on examples or
instructions placed directly in its prompt at inference time, and producing task-appropriate
output on new inputs without any update to its weights — is a well-known, widely-discussed,
generically-named capability studied broadly across large language models (not unique to any one
vendor or product). This video describes the general, settled shape of the idea qualitatively:
what ICL is, why it can look like "learning" even though no weights change, and the boundaries
researchers have broadly documented on what it can and can't reliably do. It does not cite a
specific paper's numeric result, name a specific benchmark, or claim any one real model's current
in-context behavior — ICL capability varies by model, task, and how examples are chosen or
ordered, and remains an active area of ongoing research.

Three broad, well-documented qualitative findings anchor this video's rubric and are described
generically, with no specific paper, author, or vendor named and no specific accuracy number
claimed:

- **Pattern-location, not parameter learning:** a substantial line of research frames in-context
  learning as the model locating and completing a pattern already reachable from its pretraining
  and architecture, using only what's present in the current context — rather than acquiring a
  genuinely new capability it lacked going in. Mechanistic work on attention-based "copying" or
  pattern-completion behavior in transformer models is sometimes offered as one proposed
  explanation for how this happens; this video presents it as a proposed, broadly-discussed
  account, not a settled fact about every model's internals.
- **Sensitivity to example order and selection:** it is a broadly-documented, replicated finding
  across the ICL literature that few-shot prompting performance can be noticeably sensitive to
  the order in which examples are presented, how many are given, and which examples are chosen —
  the same underlying task, differently arranged, can produce a meaningfully different result.
  This video states this qualitatively (performance "can be sensitive," results "can become less
  reliable") and does not attach a specific percentage or named benchmark to it.
- **Demonstrations can conflict with a model's pretrained prior:** research on in-context learning
  has found that a model does not always fully adopt a demonstrated input-output mapping as a
  literal new rule — particularly when that mapping conflicts with patterns the model's
  pretraining would otherwise favor, the model may partially fall back toward its prior rather
  than the demonstrated rule. This video states this qualitatively, as a documented tendency, not
  a universal law or a measured number for any named system.
- **Bounded by context length:** in-context learning can only use information actually present in
  the model's context window at inference time; this is a structural/definitional bound, not a
  benchmarked claim.

No specific real model or vendor is named or benchmarked anywhere in this video. The worked
example (B04, a toy invented substitution rule taught purely through example pairs in a prompt)
and its falsifiability case (B05, the same task reordered with one mapping flipped against the
likely pretrained prior) are both fully generic and illustrative, matching the pattern used in
this fellow's prior STEM videos (e.g. the "strawberry" tokenization example, the
fabricated-citation hallucination example, the agronomy-hint chain-of-thought example, the
90%-confidence calibration example).

## Distinct from adjacent, already-covered topics in this series

- `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` covers whether a claim is
  fabricated at all. This video assumes the model is trying to follow a demonstrated pattern and
  asks a different question: what can prompt-only conditioning teach it, and where does that stop.
- `2026-10-06-lost-in-the-middle-why-more-context-isnt-better` covers where in a long context a
  fact sits and whether position affects retrieval. This video is about whether examples can teach
  a pattern at all and how robustly, independent of where in the context they sit.
- `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason` covers whether a stated
  reasoning trace actually caused the answer. This video does not examine reasoning traces at all.
- `2026-10-21-calibration-why-confidence-isnt-accuracy` covers whether a stated confidence number
  tracks real accuracy. This video does not involve confidence scores at all.
