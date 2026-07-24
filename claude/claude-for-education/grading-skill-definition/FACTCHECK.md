# FACTCHECK — grading-skill-definition

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| Claude Code Skills YAML frontmatter: name, description, parameters | B03 | ✓ | Chapter 07: skill definition format documented |
| Skill invocation by /skill-name syntax with typed parameters | B04 | ✓ | Chapter 07: skill invocation syntax |
| Skills stored in .claude/skills/ directory | B02 | ✓ | Chapter 07: skill storage location |
| Skill constrains the workflow the same way every invocation | B07 | ✓ | Chapter 07: skill definitions are deterministic per invocation |
| Chain: pattern-analyzer → feedback-drafter | B05-B06 | ✓ illustrative | Chapter 07: skill chaining documented; synthetic chain scenario |
| Skill definitions shareable as files | B07 | ✓ | Chapter 07: skills are files in .claude/skills/ |

## Illustrative scenarios
- Three-submission run: synthetic scenario
- Feedback-drafter chained to pattern-analyzer: synthetic scenario consistent with chapter 07
- All scenarios consistent with chapter 07 documented skill behavior

## Exclusions verified
- No API key discussion: PASS
- No npm install walkthrough: PASS
