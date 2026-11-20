# SOURCES — "Who Approves the Threshold?"

## Primary source

**`materiality.py`** — `projects/Mycroft-Finance-Investigator/mycroft_finance_investigator/`
in `nikbearbrown/mycroft`, PR #17.

- **B04** shows the `approved_by` refusal from `validate_approval()`, extracted with
  `inspect.getsource()` and dedented only.
- **B05** shows four real `record-materiality` runs against
  `data/verified/mycroft-finance-investigator`. Captured stdout:

```
agent signs it    ->  approved_by must be a named human, not the agent
no real basis     ->  reasoning must state a basis, not a placeholder
named human       ->  APPROVED at 10000.00 by Dana Whitfield, Controller
signs again       ->  materiality approval already recorded
```

- **B07** reflects `test_threshold_refuses_after_the_data_changes`, one of 18 passing cases
  in `tests/test_materiality.py`.

## What is a fixture, and where it is said

"Dana Whitfield, Controller" is a **test value**, not a person who approved anything. The
repository ships `config/sample-materiality-approval.json` whose own `reasoning` field reads
"SAMPLE FIXTURE, NOT AN APPROVAL". **No approved threshold is committed**, and B09 says so on
screen rather than in a footnote — a video about named approval that displayed a fabricated
signature would refute its own argument.

Synthetic sample data · recipe `DRAFT` · human gate `OPEN`.

## Register

The argument — *an agent that can approve its own threshold has hidden the judgement rather
than removed it* — is the fellow's framing. The Teardown register earns its place at B03,
where the obvious engineering shortcut is named as the failure being designed against.

## Toolkit provenance

Built with `brutalist.art` (`ai-explainer`), Kokoro `am_onyx`, cost $0.00. Patterns:
`ClaudeComposerAsk`, `ClaudeScienceLayerStack`, `ClaudeScienceChipGrid`, `CwcConceptCard`,
`ClaudeCodeBeat`, `ClaudeWindow`, `ClaudeScienceSourceFlow`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`. No new component; no retint.
