# PROMPTS — beta-carotene-false-positive

## B02 Claude Research Prompt
```
claude "Research the beta-carotene and lung cancer epidemiology case study. What were the ATBC and CARET trial designs and findings? What increased lung cancer risk was observed in supplement users? What type of confounding explains why the observational signal was backwards? Identify two other examples where a plausible cancer epidemiology association failed to survive a randomized trial."
```

## B05 Claude Revision Prompt
```
claude "Does vitamin D supplementation and cancer risk follow the same epidemiological pattern as beta-carotene? What do observational studies suggest, and what have randomized trials (VITAL) actually found?"
```

## B03 Python Script
```python
# bradford_hill_check.py
CRITERIA = [
  {"criterion": "Strength",
   "observational": "pass", "trial": "pass"},
  {"criterion": "Consistency",
   "observational": "pass", "trial": "REVERSED"},
  {"criterion": "Specificity",
   "observational": "pass", "trial": "N/A"},
  {"criterion": "Temporality",
   "observational": "pass", "trial": "pass"},
  {"criterion": "Biological gradient",
   "observational": "pass", "trial": "pass"},
  {"criterion": "Experiment",
   "observational": "N/A",
   "trial": "REVERSED: +17-28% risk in smokers"},
]
print(f"{'Criterion':<22} {'Observational':<16} Trial")
print("-" * 60)
for c in CRITERIA:
  print(f"{c['criterion']:<22} {c['observational']:<16} {c['trial']}")
```
