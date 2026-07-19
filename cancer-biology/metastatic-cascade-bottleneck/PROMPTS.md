# PROMPTS — metastatic-cascade-bottleneck

## B02 Research Prompt
```
claude "Research the metastatic cascade step by step: intravasation, survival in circulation, extravasation, micrometastasis formation, dormancy, and outgrowth. For each step, give the quantitative attrition (what fraction of cells survive to the next step), the key molecular bottleneck, and the strongest therapeutic strategy targeting that step."
```

## B05 Revision Prompt
```
claude "For each bottleneck step, what is the most advanced clinical-stage drug or intervention targeting it, its phase, and the primary endpoint being measured?"
```

## B03 Script: cascade_funnel.py
```python
# cascade_funnel.py — Claude Code output
import math
STEPS = [
    ("Shed from primary",      1_000_000, "Tumor vasculature remodeling"),
    ("Survive intravasation",      5_000, "Anoikis resistance"),
    ("Survive circulation",          500, "NK cell evasion, shear stress"),
    ("Extravasate",                   50, "CXCR4-CXCL12 homing"),
    ("Form micromet",                  5, "ECM attachment, dormancy exit"),
    ("Form macrometastasis",           1, "Angiogenic switch"),
]
for i, (step, n, bottleneck) in enumerate(STEPS):
    if i > 0:
        survival = n / STEPS[i-1][1] * 100
        print(f"  -> {survival:.3f}% survive")
    print(f"{step}: ~{n:,}  [{bottleneck}]")
```
