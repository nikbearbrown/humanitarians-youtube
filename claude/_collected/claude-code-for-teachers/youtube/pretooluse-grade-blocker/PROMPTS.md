# PROMPTS — pretooluse-grade-blocker

## B02 — Write block-grades.sh + settings.json
```
claude "Write PreToolUse hook block-grades.sh:
  read Write tool input from stdin as JSON
  extract 'content' field
  grep -qE for grade patterns:
    [0-9]{1,3}%, [A-F][+-]?,
    [0-9]+/[0-9]+
  exit 1 + 'BLOCKED: contains final grade'
  Also write settings.json config."
```

## B05 — Extend with percentile distinction
```
claude "Extend hook to also detect
  grade patterns in percentile ranges:
  'in the top 15%' vs '85%'
  distinguish quantity from grade.
Update grep pattern."
```
