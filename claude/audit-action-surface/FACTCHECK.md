# FACTCHECK -- audit-action-surface
Source chapter: `claude-agentic-ai/chapters/03-tools-permissions-and-the-action-surface.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| An agent's action surface is the set of tools and permissions available to it | SUPPORTED | Chapter 03 defines the action surface as the scope of agent capability |
| Blast radius of an error scales with the action surface, not task complexity | SUPPORTED | Chapter 03 on blast radius and permission minimization |
| Date extraction from contracts requires read + CSV write -- nothing else | ILLUSTRATIVE | Adapted from ch.03 worked example on minimal permission design. Synthetic scenario. |
| Browser access is NOT REQUIRED for a local file extraction task | SUPPORTED | Chapter 03 on identifying necessary vs. unnecessary tool grants |
| The permission matrix approach flags each access type against task requirements | SUPPORTED | Chapter 03 on pre-task permission auditing |

## Exclusions confirmed
- MCP server configuration: not mentioned, single-agent tool list only
- OWASP LLM Top 10 full walkthrough: not mentioned, no OWASP references
- Enterprise permission management: not mentioned, individual task scope only

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Action surface | B01 | B01 establishes blast radius scales with the surface |
| Permission matrix | B02 | B01 shows need to audit all access types before the task |
| Blast radius | B01 | B01 frames the stakes of an over-permissioned agent |
| NOT REQUIRED flag | B03 | B02 ASK names the flagging requirement |
