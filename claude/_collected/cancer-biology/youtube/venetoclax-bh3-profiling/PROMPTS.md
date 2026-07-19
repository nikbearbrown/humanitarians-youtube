# PROMPTS — venetoclax-bh3-profiling

## B02 Claude Research Prompt
```
claude "Research BH3 profiling as a predictive biomarker for venetoclax response. What is the assay methodology? What published studies correlate BH3 profiling with clinical outcomes in CLL and AML? What are the barriers to routine clinical implementation, and are any trials incorporating it as a companion diagnostic?"
```

## B05 Claude Revision Prompt
```
claude "Does any analogous functional assay to BH3 profiling exist for MCL-1 inhibitors? What is the clinical development status of MCL-1 inhibitors versus venetoclax?"
```

## B03 Python Script
```python
# bh3_profile_audit.py
ASSAY = {
  "method": "BH3 peptide + flow cytometry (MOMP)",
  "cell_requirement": "fresh (cannot fix/freeze)",
  "turnaround": "same-day",
  "predictive_studies": [
    "Vo 2012 Science (AML, n=34)",
    "Bhatt 2020 NEJM Evid (CLL, n=48)",
  ],
  "barriers": [
    "Fresh cells required",
    "Specialized flow cytometry lab",
    "Same-day processing",
  ],
  "companion_dx_status": "No FDA companion dx yet",
}
print(f"Method: {ASSAY['method']}")
print(f"Predictive studies: {len(ASSAY['predictive_studies'])}")
for b in ASSAY['barriers']:
  print(f"  BARRIER: {b}")
print(f"Status: {ASSAY['companion_dx_status']}")
```
