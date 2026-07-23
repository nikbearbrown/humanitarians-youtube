# PROMPTS — nanomedicine-translation-gap

## B02 Claude Research Prompt
```
claude "Research the clinical translation gap in cancer nanomedicine. Compile the honest success ledger (Doxil, Abraxane, approved ADCs, radioligand therapies) and for each explain what specifically drove clinical success and whether EPR was the primary mechanism or not. Then identify the three most common reasons nanoparticle formulations fail in human clinical trials despite promising preclinical data. Contrast the 'radioligand loop model' (image-confirm-treat-image) with the 'passive accumulation line model' (formulate-inject-hope) as different clinical strategies for nanomedicine."
```

## B05 Claude Revision Prompt
```
claude "Evaluate: is the radioligand theranostic model (image to confirm target expression, treat, image to confirm response) generalizable to nanoparticle drug delivery? Or does it require properties unique to radiolabeled ligands — quantifiable imaging, known organ-specific biodistribution, known clearance path? What would a nanoparticle equivalent of the loop model look like?"
```

## B03 Python Script
```python
# translation_ledger.py
LEDGER = [
  {"drug": "Doxil (1995)",
   "actual_mechanism": "reduced cardiotoxicity (LVEF)",
   "epr_driven": "NO — efficacy not superior to free dox"},
  {"drug": "Abraxane (2005)",
   "actual_mechanism": "albumin-SPARC/gp60 pathway",
   "epr_driven": "NO — albumin mechanism, not passive EPR"},
  {"drug": "ADCs (2013-)",
   "actual_mechanism": "antibody active targeting",
   "epr_driven": "NO — receptor-mediated delivery"},
  {"drug": "Pluvicto (2022)",
   "actual_mechanism": "PSMA loop: image->treat->image",
   "epr_driven": "NO — confirmed-target radioligand"},
]
print("HONEST NANOMEDICINE LEDGER")
for r in LEDGER:
    print(f"  {r['drug']:<18} EPR: {r['epr_driven'][:3]}")
```
