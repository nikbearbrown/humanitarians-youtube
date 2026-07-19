# FACTCHECK -- self-check-vs-independent-verification
Source chapter: `claude-agentic-ai/chapters/08-verification-is-the-control-system.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| Self-check improves output at the margins but cannot catch systematic errors | SUPPORTED | Chapter 08 on self-verification limitations: agent checks against the same representations used to generate |
| Self-check cannot catch wrong citations because the agent treats its own output as ground truth | SUPPORTED | Chapter 08 on circular self-verification and the training-data matching problem |
| Independent verification (opening the cited papers) catches errors that self-check misses | SUPPORTED | Chapter 08 on independent evidence as the requirement for true verification |
| Self-check finds 2 of 6 errors / human check finds 5 | ILLUSTRATIVE | Adapted from ch.08 framing of self-check limitations. Synthetic ratio to illustrate the gap. |
| A wrong citation can pass self-check because the agent rates its own claim as verified | SUPPORTED | Chapter 08 on citation verification failure in self-check |

## Exclusions confirmed
- Second-model review architecture: not mentioned, single-model self-check only
- Automated fact-checking APIs: not mentioned, human source-check demonstration only
- Retrieval-augmented verification: not mentioned, no RAG references

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Self-check | B01 | B01 establishes the 2-of-6 vs 5-of-6 gap between methods |
| Independent verification | B01 | B01 names opening cited papers as the independent method |
| Wrong citation | B05 | B04 shows self-check passes all claims; B05 introduces the deliberate wrong citation |
| SELF-CAUGHT / HUMAN-CAUGHT | B03 | B02 ASK sets up the two-method comparison structure |
