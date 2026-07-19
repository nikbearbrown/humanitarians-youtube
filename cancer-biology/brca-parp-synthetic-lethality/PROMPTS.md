# PROMPTS — brca-parp-synthetic-lethality

## B02 Claude Research Prompt
```
claude "Research synthetic lethality: BRCA/PARP paradigm. Find clinical evidence for success (olaparib, rucaparib, niraparib approvals), the most common resistance mechanisms, and the three most promising extensions beyond BRCA. For each extension, cite clinical trial status and objective response rates."
```

## B05 Claude Revision Prompt
```
claude "Add the MTAP-PRMT5 synthetic lethal pair. Compare the evidence strength for MTAP-PRMT5 versus original BRCA/PARP — cite the most advanced clinical trial for each."
```

## B03 Python Script
```python
# synthetic_lethality_matrix.py
MATRIX = [
  {"context": "BRCA1/2-mutant ovarian",
   "works": "YES", "orr": "54-72%",
   "resistance": "BRCA reversion mutation"},
  {"context": "BRCA-mutant breast",
   "works": "YES", "orr": "59%",
   "resistance": "BRCA reversion mutation"},
  {"context": "Most solid tumors",
   "works": "NO", "orr": "<10%",
   "resistance": "Geometry mismatch"},
]
print(f"{'Context':<28} {'Works':<6} {'ORR':<8} Resistance")
print("-" * 65)
for r in MATRIX:
  print(f"{r['context']:<28} {r['works']:<6} {r['orr']:<8} {r['resistance']}")
```
