# FACTCHECK — vox-same-prescription

Source chapter: `claude-cowork/chapters/97-fundamental-themes.md`

## Terms table

| Term | Definition used in reel | Source verification |
|---|---|---|
| Weights | The learned parameters that determine a model's outputs — the same parameters are used whether producing or auditing | Chapter §"Tier 4 — Metacognitive & Supervisory Intelligence" |
| Self-check / verify | A model re-reading its own output to confirm correctness | Chapter: "A model cannot reliably flag its own errors because it cannot step outside its own patterns" |
| Blind spot | An error that is invisible from inside the model's own patterns but visible from outside | Chapter: "The plausibility-checking that catches AI errors must come from outside the model. It must come from the human." |
| Audit | The act of evaluating output for correctness | Chapter §"Tier 4" — "the same weights that produced the output are the weights doing the audit" |

## Narration claims check

| Beat | Claim | Status |
|---|---|---|
| B01 | You ask the model to verify its own citations; it confirms; one citation is wrong | Consistent with chapter example seed and chapter §"Tier 4" |
| B04 | First pass: model reads source, produces wrong citation | Consistent with example seed: "attributes a metric to 'the Q3 report'" |
| B05 | Verify pass: same model, same output, same reading, VERIFIED — error still present | Core mechanism from chapter: "same weights doing the audit" |
| B07 | Same weights produce output AND audit output | Direct from chapter: "the same weights that produced the output are the weights doing the audit" |
| B08 | "The same weights that produced the output are the weights doing the audit. A model cannot step outside its own patterns." | Near-verbatim from chapter §"Tier 4" |
| B09 | Error is visible from outside (human), invisible from inside (model) | Chapter: "The plausibility-checking that catches AI errors must come from outside the model" |
| B11 | Model attributes metric to Q3 report; verify step confirms Q3 report; actual source was projection slide | Illustrative; labeled "illustrative" in narration; consistent with video-ideas.md example seed |
| B13 | "The check that catches the mistake must come from outside the model." | Direct synthesis of chapter §"Tier 4" |

## Verdict

All claims directly sourced from the chapter or labeled illustrative. No factual errors found.
