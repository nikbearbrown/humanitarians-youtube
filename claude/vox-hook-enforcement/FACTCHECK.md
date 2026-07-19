# FACTCHECK — vox-hook-enforcement

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| Maria types the rule in CLAUDE.md under a NEVER heading | B01, B02 | ✓ illustrative | Chapter 08-hooks.md opening scenario |
| Claude reads CLAUDE.md, weights it, and the immediate prompt can outweigh it | B03 | ✓ | Chapter 08: "Claude had read CLAUDE.md, weighted it in its decision, and produced output where the immediate prompt's pull toward summary completeness outweighed the standing instruction's prohibition." |
| Claude follows context probabilistically — high but not absolute | B03, B06 | ✓ | Chapter 08: "Claude follows context probabilistically. The probability is high but not absolute." |
| student-07.md receives "Overall performance: B+" | B04 | ✓ illustrative | Based on chapter opening: "Claude returned a summary that included the sentence: 'Overall performance: B+'" |
| A Hook is a script that runs at specific lifecycle points | B07 | ✓ | Chapter 08: "A Hook is a script that runs automatically at specific lifecycle points in a Claude Code session." |
| PreToolUse hooks run before Claude uses a tool and can block it | B07 | ✓ | Chapter 08: "PreToolUse hooks run before Claude uses a tool (Write, Edit, Bash, etc.); the hook can inspect the proposed action and block it." |
| The hook receives proposed tool input on stdin | B09 | ✓ | Chapter 08 hook script shows `input=$(cat)` reading from stdin |
| Hook exits non-zero to block; Claude receives the error; Write does not happen | B07, B08 | ✓ | Chapter 08: "the script exits non-zero with an error message. Claude receives the error; the Write does not happen" |
| Three hooks for grading tool: block grades, verify after edit, session-end log | B12 | ✓ | Chapter 08: "Three hooks for the grading tool" section |
| Heuristic: if violating the rule would be a real problem, it is a Hook | B13 | ✓ | Chapter 08: "if violating this rule would be a real problem, it is a Hook. If violating this rule would be annoying, it is a CLAUDE.md entry." |
| FERPA referenced as a real-consequence example | B10 | ✓ | Chapter 08: "The grading tool is exactly the project where hooks matter. The stakes are real — student work, FERPA, the school's grading process." |
| Ask-Claude-to-write-the-hook pattern exists | B11 | ✓ | Chapter 08: "The 'ask Claude to write the hook' pattern" section |

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| CLAUDE.md | B02 | B01 (the rule she wrote) |
| advisory | B02 | B02 (the label on the document) |
| probabilistic | B03 | B03 (the probability dial) |
| Hook | B07 | B04-B05 (the failure that requires enforcement) |
| PreToolUse | B07 | B07 (introduced alongside Hook) |
| deterministic | B07 | B07 (contrasted with probabilistic) |
| stdin | B09 | B09 (only in the still; not in narration — compliant) |

## Illustrative numbers / scenarios labeled
- Maria and student-07.md: illustrative scenario from chapter
- "3 violations in 100 sessions" in B10 graphic: illustrative, not a measured rate
- All student names (Maria) are illustrative

## Exclusions verified
- No shell scripting tutorial: PASS — hook mechanics shown conceptually only
- No regex deep-dive: PASS — pattern matching not discussed
- No full settings.json walkthrough: PASS — file referenced as a location, not taught
- No history of enforcement systems: PASS — Shannon AI Wayback not included
