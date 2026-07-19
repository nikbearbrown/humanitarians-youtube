# PEDAGOGY — vox-subagent-context
## Why One Subagent Query Saved 48% of the Context Window

## One-mechanism rule
This film teaches exactly one mechanism: inline research reads all source documents into the main session's context window, displacing build work; a subagent runs in its own isolated context and returns only a summary, leaving the main session's build context untouched.

## Audience
Teachers who use Claude Code to build classroom tools. They have experienced a session becoming less capable over time (context pressure) but may not have identified research tasks as the cause. They do not need to know how subagents are configured — only why the isolation produces a measurable benefit.

## Learning outcome
After watching, the viewer should be able to identify a research-heavy task in their own builds and know that moving it to a subagent keeps the main session's build context intact.

## Beat-by-beat check

| Beat | Pedagogical function | Passes? |
|---|---|---|
| B01 | Cold open: hook in the numbers (30% → 78% → 22% remains) before the title | PASS |
| B02 | Show the mechanism: context bar fills; viewer sees 22% remaining visually | PASS |
| B03 | Question card: frames "why" to create need-to-know | PASS |
| B04 | Mechanism detail: files arrive one at a time — viewer sees the compound cost | PASS |
| B05 | Resolution: two-box diagram shows isolation and summary return | PASS |
| B06 | Comparison: side-by-side numbers make the benefit concrete (22% vs 68% remaining) | PASS |
| B07 | Classroom example: 25 submissions vs summary page — makes the abstract concrete | PASS |
| B08 | Heuristic: the decision rule the viewer can carry away and apply | PASS |
| B09 | Endcard: three-line summary crystallizes the mechanism | PASS |

## Exclusion compliance
- NO subagent configuration YAML walkthrough
- NO multi-agent orchestration patterns
- NO Writer/Reviewer pattern
- NO auto memory discussion
- One mechanism only: inline research bloats main context; subagent isolates, returns summary

## Accuracy
- All numbers (30%, 48%, 78%, 22%) sourced verbatim from chapter 10; see FACTCHECK.md
- Heuristic quoted verbatim: "if the task reads more than the main session needs to see, it is a subagent task"
- "a few hundred words" / "300 words" for summary size — supported by chapter text

VERDICT: PASS
