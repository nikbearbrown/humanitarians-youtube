# FACTCHECK -- agentic-pre-mortem
Source chapter: `claude-agentic-ai/chapters/09-failure-modes-of-agentic-work.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| Eight failure modes taxonomy: tool overreach, stale context, plausible summary, silent omission, prompt injection, fabricated completion, irreversible action, automation bias | SUPPORTED | Chapter 09 defines these eight failure mode categories |
| Prompt injection is live when agent reads external content (email bodies) | SUPPORTED | Chapter 09 on injection vectors through external data sources |
| Irreversible action risk escalates when save becomes send | SUPPORTED | Chapter 09 on irreversibility and action consequence severity |
| Naming failure modes before the task determines what you supervise | SUPPORTED | Chapter 09 on pre-task risk identification and supervision design |
| Fabricated completion is live in email-drafting tasks | SUPPORTED | Chapter 09 on fabrication risk in generative output tasks |

## Exclusions confirmed
- Formal agent red-teaming: not mentioned, pre-mortem table only
- AgentDojo benchmark walkthrough: not mentioned, no benchmark references
- Full OWASP LLM Top 10: not mentioned, focused on the 8-mode chapter taxonomy

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Pre-mortem | B01 | B01 establishes the need to identify risks before the task runs |
| Failure mode taxonomy | B01 | B01 names eight modes as the framework |
| Irreversible action | B04 | B03 CODE shows the mode in the table; B04 shows it LIVE |
| Prompt injection | B04 | B03 CODE shows the mode; B04 shows it LIVE for email task |
| Prevention step | B02 | B02 ASK requires concrete prevention, not general caution |
