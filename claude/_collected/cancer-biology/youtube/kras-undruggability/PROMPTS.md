# PROMPTS — kras-undruggability

## B02 Claude Research Prompt
```
claude "Research the history and current status of KRAS-targeted therapy. Specifically: what structural features of wild-type KRAS made it undruggable for 40 years, what chemical insight enabled the G12C covalent inhibitors (sotorasib, adagrasib), what are their clinical response rates in NSCLC from the CodeBreaK 100 and KRYSTAL-1 trials, and what is the current clinical development status of KRAS G12D inhibitors?"
```

## B05 Claude Revision Prompt
```
claude "What is the key difference in chemical strategy required to target G12D versus G12C? The reactive cysteine approach won't work for G12D -- what approaches are in trials, and have any phase 2 data been reported?"
```

## B03 Python Script
```python
# kras_status.py
VARIANTS = [
  {"variant": "G12C",
   "nsclc_freq": "13%", "pdac_freq": "1%",
   "drug": "sotorasib / adagrasib",
   "orr": "37% / 43%",
   "mech": "covalent to reactive cysteine",
   "status": "FDA APPROVED"},
  {"variant": "G12D",
   "nsclc_freq": "4%", "pdac_freq": "41%",
   "drug": "MRTX1133 (trial)",
   "orr": "pending Phase 2",
   "mech": "non-covalent; no reactive handle",
   "status": "Phase 2"},
  {"variant": "G12V",
   "nsclc_freq": "8%", "pdac_freq": "34%",
   "drug": "none approved",
   "orr": "N/A",
   "mech": "no selective approach yet",
   "status": "Preclinical"},
]
for v in VARIANTS:
  print(f"{v['variant']}: {v['status']} | {v['drug']} | ORR {v['orr']}")
  print(f"  Chem: {v['mech']}")
```
