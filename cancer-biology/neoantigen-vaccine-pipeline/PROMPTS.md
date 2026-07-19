# PROMPTS — neoantigen-vaccine-pipeline

## B02 Research Prompt
```
claude "Research personalized neoantigen cancer vaccines: the mRNA-4157/V940 Moderna-Merck trial results (recurrence-free survival in stage III/IV melanoma), the pipeline steps (tumor sequencing -> neoantigen prediction -> mRNA manufacturing -> dosing), manufacturing timeline and cost, extension to other tumor types (NSCLC, colorectal), and the main barriers to broad adoption."
```

## B05 Revision Prompt
```
claude "Add the main failure point at each pipeline stage — what percentage of patients fail to reach dosing due to tumor biopsy quality, sequencing turnaround, neoantigen prediction accuracy, or manufacturing failure?"
```

## B03 Script: neoantigen_pipeline.py
```python
# neoantigen_pipeline.py — Claude Code output
STAGES = [
    {"stage": "Tumor biopsy + QC",        "days": 3,   "cost_usd": 500,   "attrition_pct": 10},
    {"stage": "Whole-genome sequencing",   "days": 14,  "cost_usd": 1500,  "attrition_pct": 5},
    {"stage": "Neoantigen prediction",     "days": 7,   "cost_usd": 3000,  "attrition_pct": 15},
    {"stage": "mRNA manufacturing",        "days": 28,  "cost_usd": 50000, "attrition_pct": 8},
    {"stage": "QC release + dosing",       "days": 7,   "cost_usd": 2000,  "attrition_pct": 2},
]
cumulative_loss = 0
print(f"{'Stage':<30} {'Days':>5}  {'Cost':>8}  {'Loss':>6}  {'Cumulative loss'}")
print("-" * 70)
for s in STAGES:
    cumulative_loss = 100 - (100 - cumulative_loss) * (1 - s["attrition_pct"]/100)
    print(f"{s['stage']:<30} {s['days']:>5}d  ${s['cost_usd']:>7,}  {s['attrition_pct']:>5}%  {cumulative_loss:>8.1f}%")
```
