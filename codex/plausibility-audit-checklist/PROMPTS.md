# PROMPTS — plausibility-audit-checklist

All Remotion beats. No Manim scenes. No AI image generation needed.

| Beat | Pattern | Key Props |
|------|---------|-----------|
| B02 | NikBearBrownTerminalAsk | command: Python script reads build log, capacity report with [PA]/[PF]/[TO]/[IJ]/[EI] labels, markdown table, unlabeled steps, stdlib only, runningText: "building audit script…" |
| B03 | NikBearBrownCodeBlock | filename: `capacity_audit.py`, shows argparse, re.findall, context extraction, markdown table, unlabeled detection |
| B05 | NikBearBrownTerminalAsk | command: add --missing flag printing only unlabeled steps with suggested absent capacity, runningText: "adding --missing flag…" |
| B09 | NikBearBrownOutro | brand/tagline/handle/url standard props |

All other beats (B00, B01, B04, B06, B07, B08) render as labeled slates via vox_compile.
