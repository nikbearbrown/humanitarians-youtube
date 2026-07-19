# SOURCES — claude-liam-doc-coauthoring

Source skill: `anthropics/skills/skills/doc-coauthoring/SKILL.md`

## Key quotes and content used

### B01 — TRIGGER (DocCoauthoringAnatomy.tsx)
Source: SKILL.md § When to Offer This Workflow / Trigger conditions:
> User mentions writing documentation: "write a doc", "draft a proposal", "create a spec", "write up"
> User mentions specific doc types: "PRD", "design doc", "decision doc", "RFC"

### B02 — Stage 1 exit condition (DocCoauthoringStage1.tsx)
Source: SKILL.md § Stage 1: Context Gathering / Exit condition:
> "Sufficient context has been gathered when questions show understanding - when edge cases and trade-offs can be asked about without needing basics explained."

### B03 — Quality gate (DocCoauthoringStage2.tsx)
Source: SKILL.md § Stage 2: Refinement / Quality Checking:
> "After 3 consecutive iterations with no substantial changes, ask if anything can be removed without losing important information."

Near completion (SKILL.md § Stage 2 / Near Completion):
> "announce intention to re-read the entire document and check for: Flow and consistency across sections · Redundancy or contradictions · Anything that feels like 'slop' or generic filler · Whether every sentence carries weight"

### B04 — Stage 3 exit condition (DocCoauthoringStage3.tsx)
Source: SKILL.md § Stage 3: Reader Testing / Exit Condition:
> "When Reader Claude consistently answers questions correctly and doesn't surface new gaps or ambiguities, the doc is ready."

## SELF-DEMO declaration
- B03 (DocCoauthoringStage2): shows the 6-step section workflow verbatim from SKILL.md § Stage 2: Refinement — Step 1 Clarifying Questions, Step 2 Brainstorming, Step 3 Curation, Step 4 Gap Check, Step 5 Drafting, Step 6 Iterative Refinement
