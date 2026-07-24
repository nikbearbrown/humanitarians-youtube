# FACTCHECK -- independent-verification-protocol
Source chapter: `claude-agentic-ai/chapters/08-verification-is-the-control-system.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| Agents can self-certify by matching citations against training data rather than actual documents | SUPPORTED | Chapter 08 on self-verification limitations and the training-data matching problem |
| Verification should be designed before the agent starts, not after | SUPPORTED | Chapter 08 on pre-task verification protocol design |
| Evidence artifact must be independent of the agent's self-report | SUPPORTED | Chapter 08 distinguishes independent evidence from agent-generated confirmation |
| Different output types require different evidence artifacts | SUPPORTED | Chapter 08 eight-output-type evidence matrix |
| Research tasks: source map as artifact; code tasks: test run + diff as artifact | SUPPORTED | Chapter 08 evidence matrix examples for research and code output types |

## Exclusions confirmed
- Automated verification tooling: not mentioned, manual protocol design only
- Semantic entropy measurement: not mentioned, no entropy references
- Second-model review systems: not mentioned, single-agent verification scope

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Verification protocol | B01 | B01 establishes 'verified' is not evidence without a protocol |
| Evidence artifact | B02 | B02 ASK names it as the required output of the protocol |
| Source map | B04 | B03 CODE defines it as the artifact for research output type |
| Output type | B02 | B02 ASK frames the protocol as dependent on output type |
| Independent evidence | B03 | B01 shows the problem of agent self-report |
