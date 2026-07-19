# PROMPTS — mgmt-methylation-glioblastoma

## B02 Claude Research Prompt
```
claude "Research MGMT promoter methylation in glioblastoma. What fraction of GBM patients have MGMT methylation? What is the survival difference for methylated vs unmethylated patients on temozolomide (cite Hegi 2005 NEJM)? Is there evidence unmethylated patients should receive alternative therapy? Distinguish predictive from prognostic value."
```

## B05 Claude Revision Prompt
```
claude "What current clinical trials are testing alternative or intensified regimens specifically for MGMT-unmethylated GBM? What approach shows most promise?"
```

## B03 Python Script
```python
# mgmt_decision.py
BRANCHES = [
  {"status": "Methylated",
   "freq": "40-45% of GBM",
   "tmz_response": "YES -- MGMT silenced",
   "median_os_mo": 21.7,
   "recommendation": "Temozolomide standard"},
  {"status": "Unmethylated",
   "freq": "55-60% of GBM",
   "tmz_response": "MINIMAL -- MGMT active",
   "median_os_mo": 12.7,
   "recommendation": "Clinical trial preferred"},
]
print(f"{'Status':<14} {'TMZ Response':<22} {'OS (mo)':<10} Recommendation")
print("-" * 70)
for b in BRANCHES:
  print(f"{b['status']:<14} {b['tmz_response']:<22} "
        f"{b['median_os_mo']:<10} {b['recommendation']}")
```
