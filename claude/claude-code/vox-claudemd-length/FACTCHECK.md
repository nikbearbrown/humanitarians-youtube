# FACTCHECK — vox-claudemd-length

Source chapter: `claude-code-for-teachers/chapters/03-claude-md.md`

## Claims verified

| Beat | Claim | Source | Status |
|---|---|---|---|
| B01 | Rule on line 12: Vanilla CSS only; Claude ignores it after third build | Card example seed: "Claude generates Tailwind classes on a new component despite 'Vanilla CSS only' being in the file." | VERIFIED |
| B02 | 47 lines after website build; 80 after grading tool; 220 after simulation | Card example seed: "Teacher starts with a 47-line CLAUDE.md...After the grading tool (80 lines)...After the simulation (220 lines)" | VERIFIED |
| B04 | Compliance is probabilistic — Claude "may sometimes generate code that violates a CLAUDE.md rule" | Chapter: "The compliance is probabilistic — Claude may sometimes generate code that violates a CLAUDE.md rule, especially under prompt pressure." | VERIFIED |
| B04-B07 | 200-line soft cap; beyond that instruction-following degrades | Chapter: "The 200-line guideline is the soft cap — beyond that, Claude starts to ignore the actual instructions because the file is too noisy." | VERIFIED |
| B05 | Teacher trims to 95 lines, moves to Skills/Hooks, compliance restores | Card example seed | VERIFIED (illustrative) |
| B06 | CLAUDE.md five categories: bash commands, code style, test runners, architectural decisions, environment quirks | Chapter "What goes in: the five elements" | VERIFIED |
| B06 | Skills: on-demand workflow files not loaded at session start | Chapter: "Skills — on-demand, invoked. A SKILL.md file in .claude/skills/. Not loaded at session start." | VERIFIED |
| B06 | Hooks: execute regardless of what Claude decides | Chapter: "Hooks — deterministic, enforced. A script that runs at specific lifecycle events... regardless of what Claude decides." | VERIFIED |

## Illustrative numbers
- 47 lines, 80 lines, 220 lines, 95 lines — from card example seed; illustrative.
- "200-line guideline" — from chapter text; chapter's recommendation.

## Terms table

| Term | Definition in film | Debut beat |
|---|---|---|
| CLAUDE.md | file Claude reads at session start; advisory | B01 (implicit), B04 (explained) |
| advisory | probabilistic instruction-following — not guaranteed | B04 |
| Skills | on-demand workflow files, not loaded at session start | B06 |
| Hooks | scripts that execute regardless of Claude's decision | B06 |

## Exclusions honored

- NO context-window math or token-count discussion
- NO comparison with other tools' context files
- NO full Skills/Hooks explanation (referenced as the fix only)
- One mechanism: CLAUDE.md length degrades compliance; stay under 200 lines.

## Status: VERIFIED
