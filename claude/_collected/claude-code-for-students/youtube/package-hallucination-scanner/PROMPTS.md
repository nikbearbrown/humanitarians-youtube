# PROMPTS — package-hallucination-scanner

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Write package_auditor.py:
  read Python file -> extract imports
  query PyPI JSON API per package
  report EXISTS / HALLUCINATED
  flag 404 as slopsquatting risk"
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Add --npm flag:
  check npm registry API
  registry.npmjs.org/-/v1/search?text=<pkg>
  same EXISTS/HALLUCINATED output"
```
