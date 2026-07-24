# FACTCHECK — routing-matrix

Source chapter: `claude-cowork/chapters/01-what-cowork-is-for.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Four routing tiers: Chat, CoWork, Claude Code, Human-only | B01 | ✓ | Chapter defines the task routing hierarchy: quick/chat tasks, delegated/CoWork tasks, autonomous/Claude Code tasks, and human-only regulated tasks. |
| 2 | Routing decision is about accountability, not capability | B01 | ✓ | Chapter: "The question isn't whether Claude can do the task — it's whether the accountability for the outcome can be delegated." |
| 3 | 20-task classification produces 8 Chat, 7 CoWork, 3 Claude Code, 2 Human-only | B04 | ✓ illustrative | Synthetic scenario consistent with chapter's routing framework. Proportions illustrative. |
| 4 | Production-systems signal reclassifies 3 of 5 boundary tasks from Claude Code to CoWork | B06 | ✓ illustrative | Synthetic scenario. Consistent with chapter's principle that side effects on production systems require human checkpoints. |
| 5 | Production signal changes accountability requirement, not capability | B06, B07 | ✓ | Chapter: adding context about irreversibility changes which tier is appropriate, not what Claude is capable of doing. |

---

## Illustrative elements

- 20-task classification with tier counts — synthetic, consistent with chapter routing framework.
- 5-task boundary reclassification after production signal — synthetic, illustrates the signal-routing principle.
- Specific boundary examples (schedule a meeting, run the monthly report) — synthetic, illustrative of ambiguous cases chapter discusses.

---

## Exclusions confirmed

- NO capability comparison between Claude tiers ✓
- NO discussion of specific API or tool configuration ✓
