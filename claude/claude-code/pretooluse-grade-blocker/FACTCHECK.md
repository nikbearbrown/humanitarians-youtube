# FACTCHECK — pretooluse-grade-blocker

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| PreToolUse hook executes before Write tool | B00 | ✓ | Chapter 08: hooks fire before the named tool executes |
| Hook receives JSON on stdin | B03 | ✓ | Chapter 08: hook input is the tool call JSON piped to stdin |
| exit 1 blocks the Write operation | B03 | ✓ | Chapter 08: non-zero exit from PreToolUse hook blocks the tool call |
| settings.json configures hooks | B02 | ✓ | Chapter 08: hook wiring is in .claude/settings.json |
| grep -qE for regex pattern match: correct bash | B03 | ✓ | Standard bash: -q suppresses output, -E enables extended regex |
| Grade pattern regex covers percentages, letter grades, fractions | B03 | ✓ | Regex covers common grade formats |
| CLAUDE.md instruction is probabilistic; hook is deterministic | B01 | ✓ | Chapter 08: hooks are mechanically enforced, instructions are weighted |
| Percentile distinction: "in the top 15%" vs "earned 85%" | B05-B06 | ✓ illustrative | Context-sensitive pattern matching synthetic scenario |

## Illustrative scenarios
- B+ detection and regeneration: synthetic demonstration
- Percentile vs grade distinction: synthetic scenario consistent with chapter 08

## Exclusions verified
- No API key discussion: PASS
- No npm install walkthrough: PASS
