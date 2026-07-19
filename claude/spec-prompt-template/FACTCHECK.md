# FACTCHECK — spec-prompt-template

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| Five-element specification: task, invariants, context, output_format, negative_constraints | B03 | ✓ | Chapter 04: five-element specification documented |
| stdlib-only as invariant: valid Python constraint | B03 | ✓ | Standard Python dependency constraint |
| then-run slot in output_format | B03 | ✓ | Chapter 04: output_format includes oracle command |
| Negative constraints separate from invariants | B04 | ✓ | Chapter 04: two distinct sections prevent collapse into one vague list |
| Validation refusing vague requests | B05-B06 | ✓ | Chapter 04: specificity requirement for delegation |
| Template generates from assignment description | B03 | ✓ | Chapter 04: template tool accepts assignment context |

## Illustrative scenarios
- Weak prompt producing three wrong functions: synthetic illustration
- help me with the CSV stuff rejected: synthetic scenario demonstrating validation
- parse_grades(path: str) -> list[Grade] as revised example: consistent with chapter 04 worked examples
- All scenarios consistent with chapter 04 documented behavior

## Exclusions verified
- No API key discussion: PASS
- No npm install walkthrough: PASS
