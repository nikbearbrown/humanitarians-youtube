# PROMPTS — pattern-analysis-subagent

## B02 — Write subagent definition
```
claude "Write subagent definition:
  .claude/agents/pattern-analyzer.md
  inputs: submissions dir, rubric file
  tools: Read, Grep, Glob ONLY
  output: common_misconceptions (list)
           severity_by_section (dict)
           recommended_focus (3-sentence max)
  YAML frontmatter: name, description, tools"
```

## B05 — Add WriterReviewer second subagent
```
claude "Add WriterReviewer pattern:
  second subagent reviews pattern-analyzer output
  from a fresh context window.
  Catches errors the first subagent missed."
```
