# PROOF — plain-language self-review (12-point rubric)

_Drafted by Claude for Boopesh to confirm after watching._

| # | Rubric point | How this film does it | Honest grade |
|---|---|---|---|
| 1 | One clear question | "When an AI credit model says no, why did it say no?" (B00, B10) | strong |
| 2 | Framework | the rule → the experiment → Applicant A → scorecard reasons → black-box reasons → what would change it (B20–B70) | strong |
| 3 | Reusable rubric | a reason must be specific and principal; for a linear scorecard read weight × (A − average); for a black box you need an attribution method and should check it is stable | good |
| 4 | Worked example | one made-up applicant, two real trained models, every bar from `results.json` | strong |
| 5 | Math shown properly | one formula (push = weight × (A − average)), checked exactly (intercept + pushes = A's log-odds; equals exact Shapley values for the scorecard) | good |
| 6 | Falsifiability / sanity | the two models are equally accurate (AUC 0.84) yet give different reasons; Shapley additivity error 0; the black-box list shifts with comparison group and retraining | strong |
| 7 | Edge / limits | synthetic applicants, a cutoff I chose, Shapley is one method of several, fairness out of scope, not legal advice (B20, B30, B70) | good |
| 8 | Active task | B80: retrain with other seeds and count how often A's top 3 changes | good |
| 9 | Friction recorded | FRICTIONAL.md: blocked sources, circular withdrawn, cutoff tuned, models disagree, length trim | good |
| 10 | Sources | Regulation B read verbatim (mirror of the official eCFR); circular and its withdrawal only from search summaries (⚠️) | partial |
| 11 | Disclosure | AI voice disclosed in the first sentence and on the outro; "synthetic applicants" on screen and spoken | strong |
| 12 | Length / pacing | landscape 2:27, Short 0:46, both < 3 min | ok |

Weakest point: the CFPB circular (and its 2025 withdrawal) could not be opened from the build container, so both rest
on search summaries; the film's numbers and the Regulation B quote do not depend on them.
