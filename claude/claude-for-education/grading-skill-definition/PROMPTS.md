# PROMPTS — grading-skill-definition

## B02 — Define grade-pattern-analyzer skill
```
claude "Write Claude Code Skill definition:
  .claude/skills/grade-pattern-analyzer.md
  inputs: submissions_dir, rubric.md
  scan each submission for rubric criteria
  output per-student report:
    strength flags, gap flags,
    recommended_focus sentence
    NO numeric or letter grade
  YAML frontmatter: name, description, params"
```

## B05 — Add feedback-drafter and chain skills
```
claude "Add second skill: feedback-drafter.
  Takes pattern-analyzer output.
  Drafts per-student feedback sentences.
  Chain the two skills — verify workflow runs
  without re-specifying either."
```
