# FACTCHECK -- least-privilege-file-agent
Source chapter: `claude-agentic-ai/chapters/03-tools-permissions-and-the-action-surface.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| Least privilege means the agent only accesses files required for the task | SUPPORTED | Chapter 03 on principle of least privilege for file agents |
| The working folder is the permission boundary for a file agent | SUPPORTED | Chapter 03 on scoping the agent's file access to a working directory |
| Pointing an agent at a full Documents directory creates unnecessary blast radius | SUPPORTED | Chapter 03 on blast radius scaling with directory scope |
| .env files should be classified as FORBIDDEN regardless of task description | SUPPORTED | Chapter 03 on hardcoded exclusions for credential files |
| cowork_prep.py scenario | ILLUSTRATIVE | Adapted from ch.03 working directory pattern. Synthetic script name and implementation. |

## Exclusions confirmed
- Cowork UI setup: not mentioned, script-based classification only
- Connector configuration: not mentioned, file pattern matching only
- Computer-use session management: not mentioned, no GUI interaction

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Least privilege | B01 | B01 establishes blast radius of over-scoped directory access |
| Working folder | B01 | B01 names working folder as the permission boundary |
| Forbidden pattern | B03 | B02 ASK names forbidden classification as a category |
| Before-after manifest | B04 | B02 ASK requires manifest output to show what was copied |
| FORBIDDEN CREDENTIALS | B06 | B05 CHANGE explicitly adds .env to the hardcoded forbidden list |
