# PROMPTS — agentic-handoff-auditor

## B01 — Slate: Handoff failure diagram
Flow diagram: three boxes — "Step 1" -> "HANDOFF" -> "Step 2". HANDOFF box: CRIMSON border, label "format mismatch: numbered list vs JSON array." Step 2 box: CRIMSON X and label "fails here." Arrows in INK. Teardown palette.

## B04 — Slate: Compatibility matrix
Four columns: HANDOFF | OUTPUT FORMAT | INPUT EXPECTED | STATUS. Row 1: "1->2" | "markdown paragraphs" | "text block" | COMPATIBLE (green check). Row 2: "2->3" | "numbered list" | "JSON array" | INCOMPATIBLE (crimson X). Row 3: "3->4" | "unstructured text" | "structured fields" | AMBIGUOUS (gold ~). CREAM background, INK text.

## B06 — Slate: Before/after handoff 2->3
Two rows side by side. BEFORE: "2->3 INCOMPATIBLE" — crimson border, "numbered list vs JSON array." AFTER: "2->3 COMPATIBLE" — green border, "JSON array output matches expectation." Arrow between. Caption: "One format spec closes the gap."

## B07 — Slate: Teardown
Large centered text: "Weakest handoff = format left to interpretation." Below: "Spec the output contract at every step." CRIMSON on "left to interpretation." CRIMSON rule at bottom. Cream background.

## B08 — Slate: Teaser
Clean: "NEXT: Data GIGO Detector →" Minimal teardown style.
