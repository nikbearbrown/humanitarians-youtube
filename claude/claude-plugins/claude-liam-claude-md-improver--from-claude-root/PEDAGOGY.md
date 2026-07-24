# PEDAGOGY — claude-liam-claude-md-improver

## Skill reviewed
`anthropics/claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`

## What learners will be able to do
- Identify all five CLAUDE.md file locations and what belongs in each (project root, local, global, package, subdirectory)
- Apply the six-criterion quality rubric (Commands, Architecture, Patterns, Conciseness, Currency, Actionability) to score a CLAUDE.md
- Use the diff-with-why format to propose reviewable targeted additions rather than wholesale rewrites
- Recognize the phase gate: quality report must come before any updates
- Know the `#` shortcut for live session learnings and the `.claude.local.md` pattern for personal preferences

## What makes this teachable
The five-location taxonomy covers the full CLAUDE.md surface cleanly.
The quality rubric is concrete — six named criteria with A-F grades.
The "report before update" gate is explicitly stated as a hard requirement.
The diff-with-why format is a usable template learners can replicate.

## Gaps the teardown surfaces
- Phase 3 requires user confirmation before Phase 4, but the skill gives no guidance for unattended sessions
- Quality criterion weights (High/Medium) are qualitative; numeric scores don't add up to a stated total
- Template reference (`references/templates.md`) is external — no fallback if the file is missing
- Discovery `head -50` cap silently truncates results in large monorepos
- "Preserve existing content structure" in Phase 5 has no guidance when the structure itself is the problem

## VERDICT: PASS

Five-location taxonomy, weighted quality rubric, report-before-update gate, and diff-with-why format are all solid.
Teardown adds value by surfacing the unattended-session gap and the silent `head -50` truncation risk.
