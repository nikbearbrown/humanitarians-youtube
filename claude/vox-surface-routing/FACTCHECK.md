# FACTCHECK — vox-surface-routing

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B05 | Claude generates fluent text from whatever is in context window; quality indistinguishable regardless of whether context is full data or pasted notes | ✓ | Chapter 01: "She cannot tell from the text alone." Context window determines output; fluency is constant. | — |
| B06 | Three surfaces: Chat (typed/pasted context), Code (repo context), Cowork (files/apps/calendar context) | ✓ | Chapter 01: "If the context is in your head, your clipboard, or a few pasted documents, Claude AI chat is the right surface. If the context lives inside a software repository — Claude Code. If the context lives in a folder of files, a connected calendar, a linked spreadsheet, or a local application, Claude Cowork is the right surface." | — |
| B06 | A task with context in wrong place for chosen surface will fail because surface cannot see what it needs | ✓ | Chapter 01: "A task with context in the wrong place for the surface you chose will fail not because Claude is incompetent, but because it cannot see what it needs." — near-verbatim | — |
| B08 | Alex uses chat (one note pasted), Sam uses Cowork (folder pointed); both outputs look equally professional; only Sam's is based on actual data | Illustrative | Constructed illustrative example from chapter 01 framing. | None needed |
| B09 | Five routing dimensions: output type, context source, risk, reversibility, verification path | ✓ | Chapter 01: "five routing dimensions — output type, context source, risk, reversibility, and verification path" — verbatim | — |
| B12 | Claude will not tell you the surface cannot see what it needs; routing decision is user's | ✓ | Chapter 01: "Claude will accept whatever task you give it on whatever surface you give it on. It will not tell you that the task belongs somewhere else." | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| context window | B05 | B04 established naive model is wrong; viewer wants mechanism |
| routing dimensions | B09 | B08 established the real case; viewer wants operational form |

## Exclusion Confirmation
- NO deep feature comparison of Claude products: PASS (surface differences shown by context access only)
- NO technical internals of how each surface works: PASS (absent)
- NO extended automation research citations: PASS (Amershi et al. not included)

## Illustrative Examples
- B08: Alex (chat, 1 note) vs Sam (Cowork, folder) — ILLUSTRATIVE (from card spec)
