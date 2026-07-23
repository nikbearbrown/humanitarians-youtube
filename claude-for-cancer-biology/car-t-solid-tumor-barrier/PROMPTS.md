# PROMPTS — car-t-solid-tumor-barrier

## B02 Research Prompt
```
claude "Research CAR-T therapy in solid tumors vs hematologic cancers: list FDA-approved indications with objective response rates, identify the five main barriers to solid tumor activity (antigen heterogeneity, T cell exhaustion, immunosuppressive TME, poor trafficking, on-target off-tumor toxicity), and for each barrier cite the strongest preclinical or clinical evidence it can be overcome."
```

## B05 Revision Prompt
```
claude "For each of the five barriers, what is the single most promising engineering solution currently in clinical trials? Cite the trial ID and phase."
```

## B03 Script: cart_compare.py
```python
# cart_compare.py — Claude Code output
DATA = [
    ("B-ALL (pediatric)", "hematologic", 85, "APPROVED"),
    ("DLBCL",             "hematologic", 40, "APPROVED"),
    ("Multiple Myeloma",  "hematologic", 73, "APPROVED"),
    ("GBM",               "solid",        8, "INVESTIGATIONAL"),
    ("Pancreatic",        "solid",        3, "INVESTIGATIONAL"),
    ("Ovarian",           "solid",        5, "INVESTIGATIONAL"),
]
print(f"{'Indication':<22} {'Type':<14} {'ORR':>5}  {'Status'}")
print("-" * 55)
for name, typ, orr, status in DATA:
    flag = "  <- FLAG" if orr < 15 else ""
    print(f"{name:<22} {typ:<14} {orr:>4}%  {status}{flag}")
```
