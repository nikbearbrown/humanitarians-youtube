# FACTCHECK — vox-subagent-context

Source chapter: `claude-code-for-teachers/chapters/10-subagents.md`

## Claims verified

| Beat | Claim | Source | Status |
|---|---|---|---|
| B01 | Session at 30% context; research task pushes to 78%; 22% remains | Chapter opening: "/context showed the conversation history at 78% of the window. The build itself had taken 30% of the window. The research had taken 48%. The remaining 22% was barely enough to draft feedback for one student." | VERIFIED |
| B01-B04 | Files read in session stay in context | Chapter: "Claude read the doc. Read the LMS export. Read the November meeting notes...Read a related school-board document." (all inline) | VERIFIED |
| B05 | Subagent: own isolated context window; returns only summary to main session | Chapter: "A subagent is a Claude session spawned by the main session. It has: Its own context window. Independent of the main session...A short summary as its output." | VERIFIED |
| B05 | Summary is "a few hundred words" | Chapter: "the subagent reads all 25 submissions in its own context; the subagent returns the three-section report. The main session's context grows by the size of the report (a few hundred words)" | VERIFIED |
| B07 | Pattern-analyzer subagent reads all 25 in its own window; main session gets pattern report | Chapter worked example: pattern-analyzer subagent definition and output example | VERIFIED |
| B08 | Heuristic: "if the task reads more than the main session needs to see, it is a subagent task" | Chapter: "The heuristic: if the task reads more than the main session needs to see, it is a subagent task." | VERIFIED (verbatim) |

## Illustrative numbers
- 30%, 48%, 78%, 22% — from chapter text; exact and source-supported (not illustrative).
- "25 submissions" — from chapter's worked example; illustrative.

## Terms table

| Term | Definition in film | Debut beat |
|---|---|---|
| context window | session's working memory — files read stay there | B02 (shown), B04 (explained) |
| subagent | Claude session in its own isolated context; returns only summary | B05 |

## Exclusions honored

- NO subagent configuration YAML walkthrough
- NO multi-agent orchestration patterns
- NO Writer/Reviewer pattern
- NO auto memory discussion
- One mechanism: inline research bloats main context; subagent isolates it, returns summary.

## Status: VERIFIED
