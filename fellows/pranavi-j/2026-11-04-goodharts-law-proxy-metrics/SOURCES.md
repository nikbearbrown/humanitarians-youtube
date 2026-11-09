# Sources — Goodhart's Law: When the Proxy Stops Being the Target

General AI/STEM topic explainer. Goodhart's Law — commonly summarized as "when a measure becomes a
target, it ceases to be a good measure" — and the closely related Campbell's Law (the more a
quantitative social indicator is used for decision-making, the more subject it is to corruption
pressures and the more it distorts the processes it is meant to monitor) are both well-established,
broadly attributable, widely-taught concepts in economics, public policy, management, and
machine learning (where the same phenomenon is often discussed as "reward hacking" or "metric
gaming" in reinforcement learning and ML evaluation). This video describes the general, settled
shape of the idea qualitatively: what a proxy metric is, why it can diverge from the real target it
stands in for, and what conditions tend to keep a proxy honest. It does not cite a specific paper's
numeric result, name a specific company, product, or dataset, or claim any one real system's
current metric behavior — proxy-metric divergence depends on the specific system, its incentives,
and how it's operated, and remains an active topic of discussion across these fields.

Four broad, well-documented qualitative points anchor this video's rubric and are described
generically, with no specific paper, author, company, or vendor named and no fabricated statistic
claimed:

- **Goodhart's Law / Campbell's Law, generically stated:** a measure chosen as a stand-in for a
  real target is reliable only under the conditions in which it was originally chosen; turning that
  measure into an explicit target for optimization, scoring, or reward tends to erode the
  correlation that made it useful in the first place. This is credited to economist Charles
  Goodhart and sociologist Donald T. Campbell by name (well-established, attributable concepts, not
  vendor/product names) and is widely discussed across economics, public policy, and ML.
- **Metric gaming / "reward hacking" as a general phenomenon:** it is broadly documented, across
  human organizations and automated optimization systems alike, that once a narrow metric becomes
  the explicit object of reward or evaluation, the easiest way to move that metric is sometimes to
  exploit a gap between the metric and the real target, rather than to improve the real target
  itself — without necessarily breaking the metric's own internal consistency (it can still read as
  a "clean," correctly-computed number even as it stops meaning what it used to mean). This video
  states this qualitatively and generically, as a broadly-discussed tendency, not a universal law
  that every optimized proxy must fail.
- **Pairing a gameable metric with a counterbalancing check:** a standard, widely-recommended
  practice in operations-management and metrics-design literature is pairing a narrow efficiency
  metric (e.g. average handle time) with a quality or outcome counter-metric (e.g. first-call
  resolution, repeat-contact rate, customer satisfaction) specifically so that gaming the first
  metric becomes visible in the second. This video states this generically, as a documented
  mitigation, not a guarantee that gaming becomes impossible.
- **Divergence is conditional, not universal:** a proxy's correlation with its real target holds
  only "under the conditions where it was chosen" — change the incentive, the selection pressure,
  or how the system is operated, and the correlation can break without any change to the proxy's
  own computation. This is the structural/definitional claim the whole rubric rests on.

No specific real company, vendor, product, or dataset is named or benchmarked anywhere in this
video. The worked example (B04, a call center's average-handle-time proxy, gamed, with the real
target silently worsening unwatched) and its falsifiability/counterbalance case (B05, the identical
scenario and numbers with a tracked counterbalancing check added) are both fully generic and
illustrative, matching the pattern used in this fellow's prior STEM videos (e.g. the "strawberry"
tokenization example, the fabricated-citation hallucination example, the agronomy-hint
chain-of-thought example, the 90%-confidence calibration example, the toy Caesar-shift
in-context-learning example).

## Real-world tie-in (kept generic)

This week's companion project-update video separately covers a real engineering bug involving two
related metrics drifting apart once one started being corrected independently of the other — a
live instance of the general phenomenon this STEM video explains. Per the house rule, that specific
incident is not named, described, or otherwise identified anywhere in this video; see FACTCHECK.md.

## Distinct from adjacent, already-covered topics in this series

- `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` covers whether a claim is
  fabricated at all. This video assumes every tracked number is accurately computed and asks
  whether it still tracks the real thing it was chosen to represent.
- `2026-10-06-lost-in-the-middle-why-more-context-isnt-better` covers where in a long context a
  fact sits and whether position affects retrieval. Unrelated to this video's topic.
- `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason` covers whether a stated
  reasoning trace actually caused the answer. This video does not examine reasoning traces at all.
- `2026-10-21-calibration-why-confidence-isnt-accuracy` covers whether a stated confidence number
  tracks real accuracy for a single prediction. This video is about operational metrics tracked
  over time under incentive pressure, a distinct, system-level question.
- `2026-10-28-in-context-learning-limits` covers what a prompt alone can teach a model with no
  weight updates. Unrelated to this video's topic (metrics and incentives, not model prompting).
