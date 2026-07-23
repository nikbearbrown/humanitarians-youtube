# PROMPTS — tumor-heterogeneity-tracerx

## B02 Research Prompt
```
claude "Research the TRACERx trial: what fraction of driver mutations were subclonal vs. clonal in early-stage NSCLC, what was the relationship between clonal neoantigen burden and immunotherapy response, and what strategies — multi-region sampling, ctDNA, single-cell sequencing — best capture intratumoral heterogeneity for clinical decision-making? Cite TRACERx-specific findings."
```

## B05 Revision Prompt
```
claude "Quantify: what fraction of TRACERx patients would have been mis-stratified for immunotherapy if only a single biopsy was used to estimate clonal neoantigen burden?"
```

## B03 Script: heterogeneity_audit.py
```python
# heterogeneity_audit.py — Claude Code output
# TRACERx-inspired mutation classification
MUTATIONS = [
    {"gene": "TP53",   "type": "clonal",    "ccf": 1.00, "target_for_IO": True},
    {"gene": "KRAS",   "type": "clonal",    "ccf": 0.95, "target_for_IO": True},
    {"gene": "CDKN2A", "type": "subclonal", "ccf": 0.42, "target_for_IO": False},
    {"gene": "PIK3CA", "type": "subclonal", "ccf": 0.31, "target_for_IO": False},
    {"gene": "MYC",    "type": "subclonal", "ccf": 0.19, "target_for_IO": False},
]
clonal = [m for m in MUTATIONS if m["type"] == "clonal"]
subcl  = [m for m in MUTATIONS if m["type"] == "subclonal"]
print(f"Clonal (trunk) mutations: {len(clonal)} -- present in ALL cells -- IO targets")
for m in clonal:
    print(f"  {m['gene']} CCF={m['ccf']:.2f}")
print(f"Subclonal (branch) mutations: {len(subcl)} -- partial coverage")
for m in subcl:
    flag = "  <- missed by single biopsy" if m["ccf"] < 0.40 else ""
    print(f"  {m['gene']} CCF={m['ccf']:.2f}{flag}")
```
