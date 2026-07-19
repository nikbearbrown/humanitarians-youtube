# FACTCHECK — workspace-access-audit

Source chapter: `claude-cowork/chapters/02-preparing-a-safe-workspace.md`
Date: 2026-07-13

---

## Claims audit

| # | Claim | Beat | Verdict | Source / Note |
|---|-------|------|---------|---------------|
| 1 | Least-privilege is a delegation discipline, not just a security policy | B01 | ✓ | Chapter: "The workspace permission model is not primarily a security tool — it's a delegation discipline. Over-permissioned workspaces make task attribution impossible." |
| 2 | Three permission classifications: always-needed, task-specific, never-used | B02, B07 | ✓ | Chapter defines a permission audit framework with these three categories. |
| 3 | 8 permissions granted with 3 never-used | B04 | ✓ illustrative | Synthetic scenario consistent with chapter's workspace configuration discussion. |
| 4 | Task-specific permissions should be time-boxed to when the task runs | B07 | ✓ | Chapter: "Grant access when the task needs it; revoke it when the task completes." |
| 5 | Post-removal blast radius is bounded to what active tasks need | B06 | ✓ | Chapter: "The goal is a workspace where any unexpected side effect is traceable to an active task and bounded by that task's permission set." |

---

## Illustrative elements

- 8-permission workspace with specific never-used examples (system temp, email folder, shell commands) — synthetic, consistent with chapter's over-permission examples.
- 3 always-needed permissions (project folder, output folder, CLAUDE.md) — synthetic, illustrative.

---

## Exclusions confirmed

- NO specific OS or platform permission APIs ✓
- NO discussion of encryption or data-at-rest security ✓
