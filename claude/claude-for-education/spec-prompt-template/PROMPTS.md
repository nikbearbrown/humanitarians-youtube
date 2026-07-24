# PROMPTS — spec-prompt-template

## B02 — Build spec_template.py
```
claude "Write spec_template.py:
  takes assignment description from stdin
  generates five-element specification template:
  (1) specific_task: function signature + types
  (2) invariants: constraints that must not change
  (3) context: file paths / SDD sections
  (4) output_format: what Claude produces then runs
  (5) negative_constraints: must NOT do or touch
  Output as markdown with fill-in placeholders."
```

## B05 — Add validation step
```
claude "Add validation step:
  refuse template if description doesn't name
  a specific function or artifact.
  Test on: 'help me with the CSV stuff'"
```
