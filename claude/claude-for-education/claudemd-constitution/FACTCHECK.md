# FACTCHECK — claudemd-constitution

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| CLAUDE.md is read at every session start | B01 | ✓ | Chapter 03: CLAUDE.md is active context Claude loads at the beginning of each session |
| CLAUDE.md has five sections: Bash commands, style deviations, test runners, architectural decisions, environment quirks | B07 | ✓ | Chapter 03: five-section constitution documented |
| mod_rewrite requires paths to end in .html | B03 | ✓ | Standard Apache mod_rewrite behavior for static sites |
| mailto: links as contact-form alternative for static sites | B03 | ✓ | Standard practice for no-backend deployments |
| Removing a CLAUDE.md constraint changes Claude's proposals | B05-B06 | ✓ illustrative | Synthetic scenario demonstrating CLAUDE.md as constraint document |
| CLAUDE.md is not advice but constraint | B06 | ✓ | Chapter 03: CLAUDE.md constrains Claude's proposals mechanically |

## Illustrative scenarios
- Form endpoint / Node.js handler proposal after removing no-backend line: illustrative synthetic
- mailto: link proposal with no-backend constraint: illustrative synthetic
- All scenarios consistent with chapter 03 documented behavior

## Exclusions verified
- No API key discussion: PASS
- No npm install walkthrough: PASS
- No Claude installation tutorial: PASS
