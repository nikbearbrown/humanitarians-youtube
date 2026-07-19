# FACTCHECK — three-file-system
**Build the Three-File System with Claude: AGENTS + DESIGN + PROJECT**
Source: `codex-for-teachers/chapters/12-three-file-system.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | The simulation Codex builds without three files is generic; the one built with them is yours | ✓ | Chapter thesis: the three-file system narrows the solution space from Codex's training distribution to the teacher's specific project. |
| 2 | B01 | DESIGN.md: exactly 6 CSS color variables, 2 typefaces, 4 allowed interactions, 5 forbidden interactions | ✓ | Chapter specifies these exact quantities as the DESIGN.md template for simulation projects. |
| 3 | B01 | PROJECT.md Layer 1: intent, pedagogical goal, scope boundary | ✓ | Chapter names Layer 1 of PROJECT.md as containing these three elements. |
| 4 | B04 | 74 lines — under 80 | SYNTHETIC | Illustrative line count consistent with the chapter's under-80-lines target for DESIGN.md. The specific count is synthetic. |
| 5 | B04 | Three-file system complete under 45 minutes from first prompt | ✓ | Chapter includes a 45-minute scope test as a benchmark for generating all three files. Consistent with chapter guidance. |
| 6 | B06 | Claude generates a 7th color variable (--color-error) and correctly identifies it as a violation | SYNTHETIC | Illustrative scenario demonstrating the chapter's constraint-enforcement principle. The specific variable name is synthetic but the behavior (violation detection and substitution) is consistent with chapter guidance. |
| 7 | B07 | The DESIGN.md that specifies everything gets ignored; the one specifying the small set gets followed | ✓ | Chapter: over-specification creates noise; constraint effectiveness comes from specificity and limitation, not comprehensiveness. |

---

## Exclusions confirmed
- No discussion of PROJECT.md Layers 2 and 3
- No discussion of AGENTS.md integration with the three-file system
- No discussion of the three-file system for non-simulation projects

## Synthetic scenarios
DESIGN.md content (specific hex values, specific variable names), line counts, and constraint-violation scenarios are illustrative examples consistent with the source chapter's template and guidance. Not transcripts of actual Claude sessions.
