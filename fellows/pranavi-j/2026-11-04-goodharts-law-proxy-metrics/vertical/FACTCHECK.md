# FACTCHECK — Goodhart's Law: When the Proxy Stops Being the Target

Status: **RESOLVED — fellow reviewed 2026-11-04. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | A proxy metric is a measurable stand-in, chosen because it correlates with a real target under the conditions where it was first adopted; nothing guarantees that correlation holds once conditions change | PASS — this is the standard, generic framing of Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure") and the related Campbell's Law in the social-science/economics/ML literature; not specific to any one vendor, company, or system | — | — |
| 2 | B03/B04/B05 | A proxy can diverge from its real target specifically when something changes incentives, selection pressure, or how the system is operated/scored on that number — and the proxy can remain internally consistent (still "look fine" by its own standard) even as it stops tracking the real target | PASS — this is the well-established, broadly-discussed general mechanism behind Goodhart's Law / Campbell's Law and behind documented "reward hacking" / metric-gaming findings in reinforcement learning and ML evaluation, stated here generically and qualitatively, with no claim about any one named system's specific metrics | Narration kept to general, hedged framing ("can diverge," "can still look fine"), not a universal law that every proxy always fails | Keep conditional language ("can," "when something changes") rather than asserting divergence as inevitable for every proxy |
| 3 | B04/B05 | A call center's average handle time (AHT), tracked as a stand-in for efficient service, can be reduced by agents rushing or ending calls early, improving the tracked number while the real target (problems actually resolved) gets worse; the specific numbers shown (6.5 MIN → 4.0 MIN; 82% → 61%) | PASS (mechanism) / ILLUSTRATIVE (numbers) — average handle time is a widely-used, textbook-level example of a gameable call-center proxy metric discussed broadly in customer-service and operations-management literature; the specific before/after numbers in this video are invented for teaching clarity, not a disclosed measurement from any real call center, company, or vendor | Narration and on-screen text must not imply these numbers were measured from a real system | Keep phrasing generic ("a call center," not a named company); label numbers as illustrative in SOURCES.md |
| 4 | B05 | Pairing a gameable proxy (average handle time) with a counterbalancing check that is also tracked (first-call resolution / repeat-call rate) can catch a gaming attempt that would otherwise go unnoticed, keeping the overall tracked picture aligned with the real target | PASS — pairing a narrow, gameable efficiency metric with a quality/outcome counter-metric (e.g. resolution rate, callback rate, customer satisfaction) specifically to resist gaming is a standard, widely-recommended practice in operations-management and metrics-design literature; stated here generically, with no specific named system or statistic claimed as measured | Avoid implying this pairing makes gaming impossible in all cases — frame as "can catch," not "always catches" | Keep qualitative: "can catch," "stays visible," never an absolute guarantee |
| 5 | B03/B06 | Whether a proxy has gone stale is testable by asking three questions: what the number actually stands in for, whether anything is being scored/rewarded on the number itself, and whether anything about its production or incentives has changed since it was first trusted | PASS — editorial framework distilled from the generic Goodhart's-Law/Campbell's-Law literature and standard metrics-design practice, not a factual claim requiring external citation | — | — |
| 6 | B06, B07 | The scaffolded audit task and the takeaway statement | PASS — a generic, runnable procedure and an editorial summary, not a factual claim requiring external citation | — | — |

## Dramatization check

No beat names or benchmarks a specific real company, product, vendor, or dataset. The worked
example (B04's call-center average-handle-time scenario) and its falsifiability/counterbalance
case (B05, the identical scenario with a tracked counterbalancing check added) are both framed as
generic, textbook-level illustrations of how proxy metrics behave, consistent with this fellow's
established house style for STEM topic explainers (hallucination, tokenization,
lost-in-the-middle, chain-of-thought faithfulness, calibration, in-context learning). No specific
numeric result is presented as a real measurement anywhere — the call-center numbers are invented
for teaching clarity and are internally consistent (the same pressure produces the same underlying
drop in both B04 and B05; only whether a counterbalancing check is tracked differs).

## Distinct from this fellow's prior videos

This video is explicitly not a re-run of six adjacent, already-covered topics in this series:

- **Not hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`): that video
  is about whether a stated claim is fabricated at all. This video assumes every number shown is
  accurately computed and asks a different question: does the number still track what it was
  chosen to track?
- **Not tokenization**: that topic is about how text is chunked into tokens before any reasoning
  happens. This video has nothing to do with text segmentation.
- **Not lost-in-the-middle** (`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`): that
  video is about where in a long context a fact sits. This video is about numeric/behavioral
  metrics tracked over time, not retrieval position.
- **Not chain-of-thought faithfulness** (`2026-10-15-chain-of-thought-why-the-reasoning-isnt-
  always-the-reason`): that video is about whether a stated reasoning trace actually produced an
  answer. This video doesn't involve reasoning traces at all.
- **Not calibration** (`2026-10-21-calibration-why-confidence-isnt-accuracy`): that video is about
  whether a stated confidence number tracks real accuracy for a single prediction. This video is
  about whether an operational metric, tracked over time and under incentive pressure, still
  tracks the real-world target it was chosen to represent — a distinct, system-level question.
- **Not in-context learning** (`2026-10-28-in-context-learning-limits`): that video is about what
  a prompt alone can teach a model with no weight updates. This video has nothing to do with model
  prompting or weight updates — it's about metrics and incentives in any system, human or
  automated.

## Real-world tie-in (kept generic, per the house rule)

This week's companion project-update video separately covers a real engineering bug involving a
dashboard severity proxy and the operational severity label used elsewhere drifting apart once one
of the two started being corrected independently of the other. That specific incident is NOT named,
described in technical detail, or otherwise identified anywhere in this STEM video — per the house
rule, this video stays fully generic. B06's narration carries one brief, general sentence ("this
isn't unique to any one system; it happens anywhere a number gets tracked instead of the thing it
was meant to represent") that is true of the general phenomenon on its own terms, without
referencing any specific project, company, or bug.

## Resolved 2026-11-04

1. Confirmed the B04 worked example (a call center's average handle time, gamed, with the real
   target silently worsening unwatched) and the B05 falsifiability/counterbalance case (the
   identical scenario and numbers, but with the real target now tracked as a counterbalancing
   check, catching the same gaming attempt) are fine as described: fully generic, illustrative, no
   real company/vendor named or benchmarked, and the qualitative claims about incentive-driven
   divergence and counterbalancing checks are conservative, hedged, and consistent with
   well-documented general findings in the Goodhart's-Law/metrics-design literature. No specific
   numeric result, paper, author, or vendor is cited or implied anywhere in the beat sheet,
   narration, or on-screen text.

Gate P (narration review) can proceed.
