# FACTCHECK — vox-action-surface

Source chapter: `claude-agentic-ai/chapters/03-tools-permissions-and-the-action-surface.md`

---

## Claims audit

| Claim | Verdict | Source / note |
|---|---|---|
| Agent given folder cleanup task: tax documents remain, client contracts deleted | ✓ | Chapter 03 opening scene, verbatim |
| "No malice. No error in the ordinary sense." | ✓ | Chapter 03: "No malice. No error in the ordinary sense." |
| Action surface = complete set of things the agent could affect; determined by access granted not task description | ✓ | Chapter 03: "the action surface: the complete set of things the agent could affect if its reasoning, plan, or context led it there... determined by the access you grant." |
| "The more the agent can touch, the larger the blast radius of any error." | ✓ | Chapter 03, verbatim |
| Blast radius scales with action surface, not intended task | ✓ | Chapter 03: "agent errors... expand harm in proportion to the surface, not in proportion to the intended task" |
| Tom example: folder access for report, secrets subfolder, agent reads for context, secrets in session log pasted to Slack | ILLUSTRATIVE | Adapted from chapter 03 Tom example. Numbers illustrative. |
| Fix: dedicated working folder, copy only what agent needs, keep source files in original location | ✓ | Chapter 03: "The correct version... create a dedicated working folder, copy a specific subset of documents into it" |
| Least privilege principle (Saltzer and Schroeder 1975): grant minimum tools task requires | ✓ | Chapter 03 cites Saltzer and Schroeder 1975 — principle stated in plain language only, no citation shown on screen |

---

## Exclusions confirmed

- No access-ladder enumeration in full (seven rungs). Only broad/narrow surface contrast shown. Pass.
- No OWASP LLM Top 10 history or list. Pass.
- No prompt injection attack mechanics. Pass.

---

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| action surface | B04 (mechanism) | B01-B02 show the damage; B03 question creates the need |
| blast radius | B05 (card) | B04 establishes that surface != task |
| working folder / narrow surface | B07 | B06 Tom example shows the overreach |
