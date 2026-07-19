# PROMPTS — knudson-two-hit-math

## B02 Claude Research Prompt
```
claude "Reconstruct Knudson's 1971 two-hit hypothesis argument from his PNAS paper. What were his data inputs, what mathematical model did he apply, and what did he predict? Then list five hereditary cancer syndromes where the two-hit mechanism was subsequently confirmed at the molecular level — with year of confirmation and gene."
```

## B05 Claude Revision Prompt
```
claude "Explain the PTEN haploinsufficiency exception to the two-hit model. Does losing one copy of PTEN produce cancer risk in some contexts? Does this refine or undermine the two-hit model?"
```

## B03 Python Script
```python
# two_hit_audit.py
CONFIRMATIONS = [
  {"syndrome": "Retinoblastoma",
   "gene": "RB1", "year": 1987,
   "deviation": "None -- canonical"},
  {"syndrome": "Li-Fraumeni",
   "gene": "TP53", "year": 1990,
   "deviation": "Dominant negative also seen"},
  {"syndrome": "FAP",
   "gene": "APC", "year": 1991,
   "deviation": "None"},
  {"syndrome": "VHL disease",
   "gene": "VHL", "year": 1993,
   "deviation": "None"},
  {"syndrome": "HBOC",
   "gene": "BRCA1", "year": 1994,
   "deviation": "Haploinsufficiency partial"},
]
print(f"{'Syndrome':<20} {'Gene':<8} {'Year':<6} Deviation")
print("-" * 60)
for c in sorted(CONFIRMATIONS, key=lambda x: x['year']):
  print(f"{c['syndrome']:<20} {c['gene']:<8} {c['year']:<6} {c['deviation']}")
```
