# PROMPTS — prompt-anatomy-auditor

## B01 — Slate: Anatomy audit table
Render a terminal-style two-column table. Header: PROMPT ANATOMY AUDIT. Columns: COMPONENT | STATUS. Rows: Task (present, green), Context (missing, crimson X), Constraints (missing, crimson X), Output Format (missing, crimson X), Examples (missing, crimson X), Eval Criteria (missing, crimson X). Cream background, INK text, CRIMSON for missing rows.

## B04 — Slate: Component verdict map
Three-column table: COMPONENT | VERDICT | SCORE. Task: Present (4/5, green). Context: Implied (2/5, gold). Constraints: Missing (0/5, crimson). Format: Missing (0/5, crimson). Examples: Missing (0/5, crimson). Eval Criteria: Missing (0/5, crimson). Color-code each row by verdict.

## B06 — Slate: Before/after score delta
Side-by-side layout. BEFORE (original prompt): 2 present, avg 1.3, total 8/30. AFTER (improved prompt): 6 present, avg 4.1, total 24/30. Show delta arrows on each row. Green checkmarks on AFTER column.

## B07 — Slate: Teardown angle
Large centered text: "The anatomy is a diagnostic, not a template." Below, smaller: "Missing Evaluation Criteria = Claude decides when done. You don't." Cream background, CRIMSON accent rule at bottom.

## B08 — Slate: Teaser
Clean: "NEXT: Criteria-First Generator →" Minimal layout, INK on CREAM.
