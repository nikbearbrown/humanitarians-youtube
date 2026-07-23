# PROMPTS — warburg-therapeutic-history

## B02 Claude Research Prompt
```
claude "Research clinical attempts to target the Warburg effect in cancer therapy. Cover: 2-deoxyglucose, dichloroacetate, HIF-1alpha inhibitors. For each, find the most advanced clinical trial, the reported response rates, and the stated reason for failure. Then contrast with IDH inhibitors (ivosidenib, enasidenib) — what made those succeed when broader Warburg targeting did not?"
```

## B05 Claude Revision Prompt
```
claude "Which current clinical trials targeting aerobic glycolysis show the highest response rates? Does any look like it might replicate the IDH inhibitor pattern of narrow success?"
```

## B03 Python Script
```python
# warburg_timeline.py
DRUGS = [
  {"drug": "2-Deoxyglucose", "mech": "GLUT/HK block",
   "trial": "Phase I/II", "orr": "<5%",
   "outcome": "Toxicity; universal target"},
  {"drug": "Dichloroacetate", "mech": "PDK inhibitor",
   "trial": "Phase II (GBM)", "orr": "<10%",
   "outcome": "No survival benefit"},
  {"drug": "HIF-1a inhibitor", "mech": "HIF block",
   "trial": "Phase II", "orr": "<10%",
   "outcome": "Off-target toxicity"},
  {"drug": "Ivosidenib", "mech": "IDH1 inhibitor",
   "trial": "Phase III", "orr": "41%",
   "outcome": "FDA APPROVED (AML)"},
]
print(f"{'Drug':<20} {'ORR':<8} Outcome")
for d in sorted(DRUGS, key=lambda x: x['orr'], reverse=True):
  print(f"{d['drug']:<20} {d['orr']:<8} {d['outcome']}")
```
