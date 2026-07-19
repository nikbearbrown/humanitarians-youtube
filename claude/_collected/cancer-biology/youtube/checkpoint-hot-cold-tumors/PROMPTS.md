# PROMPTS — checkpoint-hot-cold-tumors

## B02 Claude Research Prompt
```
claude "Compile single-agent anti-PD-1 or anti-PD-L1 response rates across six cancer types: Hodgkin lymphoma, melanoma, MSI-high colorectal, NSCLC PD-L1 high, triple-negative breast cancer, pancreatic adenocarcinoma. For each: ORR, median TMB, PD-L1 expression level, immune phenotype (hot/excluded/cold), and leading reason for non-response. Cite the pivotal trial."
```

## B05 Claude Revision Prompt
```
claude "Has any cold-to-hot conversion strategy (STING agonists, oncolytic viruses, radiation before checkpoint blockade) produced a meaningful improvement in pancreatic cancer checkpoint response rates in a phase 2 trial?"
```

## B03 Python Script
```python
# checkpoint_table.py
CANCERS = [
  {"name": "Hodgkin lymphoma", "orr": 0.72,
   "tmb": "low", "phenotype": "hot",
   "resistance": "PD-L1 amplification"},
  {"name": "Melanoma", "orr": 0.40,
   "tmb": "high", "phenotype": "hot",
   "resistance": "T cell exhaustion"},
  {"name": "MSI-high CRC", "orr": 0.36,
   "tmb": "high", "phenotype": "hot",
   "resistance": "beta-2-microglobulin loss"},
  {"name": "NSCLC PD-L1 hi", "orr": 0.30,
   "tmb": "moderate", "phenotype": "excluded",
   "resistance": "KRAS co-mutation"},
  {"name": "TNBC", "orr": 0.18,
   "tmb": "low", "phenotype": "cold",
   "resistance": "immunosuppressive TME"},
  {"name": "Pancreatic", "orr": 0.04,
   "tmb": "low", "phenotype": "cold",
   "resistance": "desmoplastic stroma"},
]
for c in sorted(CANCERS, key=lambda x: -x['orr']):
  print(f"{c['name']:<22} ORR={int(c['orr']*100)}% {c['phenotype']:<10} {c['resistance']}")
```
