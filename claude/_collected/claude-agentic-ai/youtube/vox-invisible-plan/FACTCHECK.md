# FACTCHECK — vox-invisible-plan

Source chapter: `claude-agentic-ai/chapters/07-planning-before-acting.md`

---

## Claims audit

| Claim | Verdict | Source / note |
|---|---|---|
| Agent cleaned up folder without plan: files moved, active items archived, one doc renamed | ✓ | Chapter 07 opening scene, verbatim |
| Agents plan whether you ask them to or not (ReAct architecture always builds internal sequence) | ✓ | Chapter 07: "they plan whether you ask them to or not... The question is not whether planning happens. The question is whether it happens in language the human can read before execution begins." |
| Invisible plan and visible plan produce identical output in the best case; in worst case, very different outcomes | ✓ | Chapter 07: "An agent working from an invisible plan and an agent working from a visible plan produce identical output in the best case. In the worst case, they produce very different outcomes." |
| Requiring explicit plan surfaces a step that was always there, does not add a step | ✓ | Chapter 07: "Requiring an explicit plan before execution does not add a step. It surfaces a step that was always there." |
| Plan elements: task decomposition, dependency order, missing info identification, stop conditions, verification evidence | ✓ | Chapter 07: Liang et al. 2024 cited for these elements |
| Asking before forming plan ("Ask-before-Plan") produces better outcomes than filling gaps silently | ✓ | Chapter 07: "Ask-before-Plan, 2024" cited |
| Aisha example: 90-day rule applied silently, January client file archived, recovery takes 40 minutes | ILLUSTRATIVE | Adapted from chapter 07 Aisha scenario. Numbers illustrative. |
| Folder cleanup done correctly: agent asks first, produces plan with 60-day threshold, manager adjusts, bounded execution | ✓ | Chapter 07 "Folder Cleanup Done Correctly" section, verbatim |

---

## Exclusions confirmed

- No ReAct paper formalism (Yao et al. 2023 not cited, only described in plain language). Pass.
- No planning-survey taxonomy from Liang et al. (no enumeration of planning framework types). Pass.
- No comparison of planning architectures across agent systems. Pass.

---

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| invisible plan | B04 (mechanism) | B01-B02 show the invisible plan in action |
| visible plan | B04 (mechanism) | B03 question beat asks why surfacing matters |
| checkpoint | B05 (card) | B04 establishes the two-timeline contrast |
| plan elements | B06 | B05 asserts the checkpoint is the key; B06 names what goes in it |
| stop condition | B06 | B06 plan elements accumulation |
| scope boundary | B08 (practice) | B07 Aisha example shows missing scope boundary |
