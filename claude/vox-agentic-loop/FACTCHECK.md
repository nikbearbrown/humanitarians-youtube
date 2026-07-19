# FACTCHECK — vox-agentic-loop

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| Claude Code runs an agentic loop: gather context, take action, verify result, loop | B03 | ✓ | Chapter 02: "Claude Code is an *agentic loop*. The model gathers context... It takes action... It verifies results... then it loops" |
| The loop can execute multiple file changes before returning control | B04 | ✓ | Chapter 02: "An agentic system that runs the loop can produce wrong actions — modified files, executed commands, changed state — before you have a chance to read the explanation." |
| Teacher example: contact page request triggers writing contact.html, modifying nav, installing form library | B04 | ✓ illustrative | Based on chapter: teacher scenario with class-website; form library not explicitly from chapter but consistent with described risks (CDN, JS, dependencies) |
| Plan mode: Shift+Tab twice enters read-only mode | B07 | ✓ | Chapter 02: "Plan mode (Shift+Tab twice) puts Claude in read-only mode." |
| Plan mode: Claude can read and propose but cannot edit, run, or change anything | B07 | ✓ | Chapter 02: "It can read files, propose plans, explain what it would do — but it cannot edit, run, or change anything until you switch out of plan mode." |
| Ctrl+G opens plan in editor | B08 | ✓ | Chapter 02: "Press Ctrl+G. The plan opens in your text editor." |
| Plan mode is for first sessions and costly-to-undo operations | B10 | ✓ | Chapter 02: "use plan mode when you want to see the plan before approval; use it especially for any operation whose failure would be expensive." Heuristic ("30 seconds") is illustrative. |
| Claude.ai is turn-based; Claude Code is agentic | B02 | ✓ | Chapter 02: "Claude.ai is a turn-based conversation. You type. The model produces text. You read. You decide what to do. Claude Code is an *agentic loop*." |

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| agentic loop | B02-B03 | B02 (chatbot comparison creates the need for a name) |
| Gather / Act / Verify | B03 | B03 (the loop is shown before the terms are named) |
| plan mode | B07 | B05-B06 (the problem of uncontrolled execution creates need) |

## Illustrative numbers / scenarios labeled
- "30 seconds to undo" in B10: illustrative heuristic — not from chapter
- Contact page / class-website scenario: illustrative from chapter

## Exclusions verified
- No npm install walkthrough: PASS
- No full Claude Code installation tutorial: PASS
- No comparison with GitHub Copilot: PASS
- No discussion of API keys: PASS
