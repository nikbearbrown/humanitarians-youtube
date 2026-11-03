# FACTCHECK — Claude, Reviewed. (LLM Evaluation Through Human-in-the-Loop)

No book chapter underlies this build — a general research-centric topic
per the human's request. Because the task names Claude/Anthropic and is
explicitly LLM-judge-shaped, the `claude-api` skill's `build-eval` guide
(`shared/evals/build-eval.md`) was loaded first and is the primary
grounding source for the Claude-specific/current claims below.

| # | Claim | Tag | Source |
|---|---|---|---|
| 1 | The grading-method ladder: programmatic check → pairwise blind comparison → model-graded pointwise rubric → human spot-check, roughly cheapest-to-most-judgment | Cited, current | `claude-api` skill, `shared/evals/build-eval.md` §Step 2, read directly this session |
| 2 | "Never use the model under test as its own judge" | Cited, current | Same source, same section — stated as an explicit rule, not inferred |
| 3 | LLM judges "can be gamed... they can fixate on surface features" | Cited, current | Same source, §Failure modes to avoid |
| 4 | Human spot-check is appropriate "when even a rubric is hard to write," and a handful of human-graded examples can outweigh a hundred model-graded ones | Cited, current | Same source, §Step 2, grading method #4 |
| 5 | The eval-building process requires two explicit human sign-off gates: the input set, and the grading method itself (tested by "would you have scored any of these differently?") | Cited, current | Same source, framing text + §Step 1/§Step 2 |
| 6 | Human-only grading is accurate but "limits how often the eval can run" | Cited, current | Same source, grading method #4 |
| 7 | Reinforcement learning from human feedback (RLHF): human reviewers rank pairs of model outputs, producing preference labels that train a reward model | General/stable | Long-established, widely documented ML practice; stated here only in general mechanism terms, no specific paper's numbers or dates cited |
| 8 | Inter-annotator disagreement is a measurable, trackable signal rather than noise to average away | General/stable | Standard practice in annotation/evaluation methodology; stated qualitatively |
| 9 | Triage-based sampling (disagreement-driven, boundary-driven, stratified) as a practical alternative to grading every case by hand | General/stable, synthesized | A standard active-learning/human-review pattern; not tied to a specific named system or paper |

## Explicitly excluded

- No claim that this video reflects a specific company's internal eval
  pipeline — the content is general methodology, grounded in the
  current, sourced `build-eval.md` guide plus well-established industry
  practice (RLHF, annotator agreement), not a specific product's
  documented process.
- No benchmark numbers, inter-annotator agreement percentages, or named
  study citations for RLHF/triage — these are stated at the level of
  stable, qualitative mechanism, consistent with this session's standing
  discipline against unverified quantitative claims.
