# FACTCHECK — problem-formulation-validator

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | If you can't describe what the build does in one sentence, you haven't decided yet — and Codex will decide for you | ✓ | Ch08: "If you can't describe what the build does in one sentence, you haven't decided. And Codex will decide for you." Verbatim. | — |
| B01 | Three-question formulation test: what does it do, what does it touch, what does it never touch | ✓ | Ch08: The three-question test is named and defined. Verbatim. | — |
| B01 | If any answer requires more than one sentence, the formulation isn't done | ✓ | Ch08: "If any answer requires more than one sentence, the formulation isn't done." Verbatim. | — |
| B04 | Q1 fails: 'build a feedback notifier' needs more than one sentence | Illustrative | Synthetic example illustrating a vague formulation. Consistent with Ch08's examples. | Marked synthetic. |
| B04 | Q2 passes: 'reads JSON from playtests/ folder, writes one .md to playtests/' | Illustrative | Synthetic example of a specific formulation. Consistent with Ch08's guidance. | Marked synthetic. |
| B04 | Q3 passes: 'never writes to src/ or modifies game code' | Illustrative | Synthetic example of a scope exclusion. | Marked synthetic. |
| B06 | Q1 corrected to full one-sentence description with input/filter/grouping/output | Illustrative | Synthetic illustration of the correction. Mechanism is verbatim from Ch08. | Marked synthetic. |
| B07 | 'Build a feedback notifier' is a category; the specific sentence is a decision | ✓ | Ch08: "A category is not a decision. A decision names the input, the filter, the grouping, and the output." Verbatim in spirit. | — |

## Manim Scenes
- B04_FormulationTrafficLight: Three-question traffic light — ILLUSTRATIVE. Q1 fail/Q2,Q3 pass is synthetic example of an underspecified build description.
- B06_FormulationAllGreen: All three questions pass after Q1 correction — ILLUSTRATIVE. The correction pattern is verbatim from Ch08 guidance.

## Illustrative Scenarios
All specific build descriptions (feedback notifier, playtests/ path) are SYNTHETIC examples constructed to illustrate Ch08's formulation test. They are not drawn from any real project.
