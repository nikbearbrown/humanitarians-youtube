# PROMPTS — lnp-endosomal-escape

## B02 Claude Research Prompt
```
claude "Research the endosomal escape problem in lipid nanoparticle (LNP) mRNA delivery. Explain: (1) why bare mRNA cannot be administered (charge, nuclease degradation, renal clearance, immune activation); (2) LNP structure — the roles of ionizable lipid, phospholipid, cholesterol, PEG-lipid; (3) the pH-responsive ionizable lipid mechanism for endosomal escape; (4) why only 1-2% of cargo escapes (the quantitative bottleneck); and (5) the three main strategies being explored to improve escape efficiency (endosomal disruptive polymers, pH-responsive peptides, targeted endosome disruption)."
```

## B05 Claude Revision Prompt
```
claude "Identify the three leading chemistry approaches to improving LNP endosomal escape: (1) ionizable lipid library screening (Moderna/BioNTech approaches), (2) fusogenic peptides, (3) endosome-disruptive polymers. What is the best published improvement in delivery efficiency vs. standard LNPs? Has any improved-escape formulation entered clinical trials?"
```

## B03 Python Script
```python
# lnp_escape.py
COMPONENTS = [
  ("Ionizable lipid", "ALC-0315 / SM-102",
   "neutral at pH7.4, cationic at pH5.5 -> escape"),
  ("Phospholipid",   "DSPC",      "structural bilayer"),
  ("Cholesterol",    "cholesterol","membrane stability"),
  ("PEG-lipid",      "ALC-0159",  "stealth / corona shield"),
]
ESCAPE_PCT = 0.015  # ~1-2% median (Sahay et al.)
DEGRADE_PCT = 1 - ESCAPE_PCT
print(f"Endosomal escape: {ESCAPE_PCT*100:.1f}%")
print(f"Lysosomal degradation: {DEGRADE_PCT*100:.1f}%")
print("\nFirst LNP drug: Onpattro (patisiran) 2018")
```
