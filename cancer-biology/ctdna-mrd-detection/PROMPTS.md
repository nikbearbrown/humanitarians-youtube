# PROMPTS — ctdna-mrd-detection

## B02 Research Prompt
```
claude "Research ctDNA minimal residual disease testing in solid tumors: which cancer types have the strongest clinical validation (colorectal, breast, lung, bladder), what is the sensitivity and specificity of the leading platforms (Foundation Medicine, Guardant, Grail), what is the lead time to imaging detection, and which clinical trials have shown ctDNA-MRD-guided escalation/de-escalation of adjuvant therapy changes outcomes?"
```

## B05 Revision Prompt
```
claude "Add a column: for each cancer type, what is the cost per test, and is it covered by Medicare or major private insurers as of 2024?"
```

## B03 Script: ctdna_matrix.py
```python
# ctdna_matrix.py — Claude Code output
DATA = [
    {"cancer": "Colorectal (stage II)", "sensitivity": 0.88, "lead_mo": 8, "rct": "DYNAMIC (NEJM 2022)"},
    {"cancer": "Breast (early)",        "sensitivity": 0.70, "lead_mo": 11, "rct": "C-TRAK (ongoing)"},
    {"cancer": "NSCLC (stage I-III)",   "sensitivity": 0.75, "lead_mo": 5,  "rct": "TRACERx (Nature 2022)"},
    {"cancer": "Bladder",               "sensitivity": 0.82, "lead_mo": 3,  "rct": "Pilot only"},
    {"cancer": "Ovarian",               "sensitivity": 0.60, "lead_mo": 2,  "rct": "No RCT"},
]
print(f"{'Cancer':<28} {'Sens':>5}  {'Lead (mo)':>10}  {'Trial evidence'}")
print("-" * 65)
for d in DATA:
    flag = "  <- VALIDATED" if "NEJM" in d["rct"] or "Nature" in d["rct"] else ""
    print(f"{d['cancer']:<28} {d['sensitivity']*100:>4.0f}%  {d['lead_mo']:>9}mo  {d['rct']}{flag}")
```
