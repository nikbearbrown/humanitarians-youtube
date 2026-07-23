# PROMPTS — hallmarks-2022-debate

## B02 Claude Research Prompt
```
claude "Research the 2022 Hallmarks of Cancer additions: phenotypic plasticity, polymorphic microbiomes, senescent cells. For each, find the strongest supporting evidence and the strongest rebuttal. Produce a table: hallmark | key supporting studies | key challenges | consensus status"
```

## B05 Claude Revision Prompt
```
claude "Add a column: what experiment would definitively settle whether each 2022 addition is a true mechanistic hallmark vs. a descriptive category?"
```

## B03 Python Script
```python
# hallmarks_audit.py
HALLMARKS = [
  {"name": "Phenotypic plasticity",
   "support": "EMT studies, cancer stem cell lit",
   "rebuttal": "No RCT; plasticity is descriptive",
   "tier": "PROPOSED"},
  {"name": "Polymorphic microbiomes",
   "support": "Fusobacterium in CRC, FMT studies",
   "rebuttal": "Causal chain unproven; correlation only",
   "tier": "CONTESTED"},
  {"name": "Senescent cells",
   "support": "SASP in tumor microenvironment",
   "rebuttal": "Context-dependent; some anti-tumor roles",
   "tier": "PROPOSED"},
]
for h in HALLMARKS:
  print(f"{h['name']}: [{h['tier']}]")
  print(f"  Support: {h['support']}")
  print(f"  Rebuttal: {h['rebuttal']}")
```
