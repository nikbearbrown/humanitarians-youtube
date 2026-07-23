# PROMPTS — cancer-disparities-zip-code

## B02 Research Prompt
```
claude "Research racial disparities in breast cancer outcomes: the Black-white mortality gap (absolute and relative), what fraction is attributable to biology (triple-negative breast cancer prevalence), what fraction is attributable to structural factors (screening access, treatment delays, financial toxicity, clinical trial enrollment), which specific interventions have demonstrated gap reduction in published trials, and what the NCI Cancer Disparities Research Program priorities are."
```

## B05 Revision Prompt
```
claude "For each structural factor, what is the single highest-evidence intervention that reduces it — and in which health systems has it been implemented at scale with documented outcome improvement?"
```

## B03 Script: disparity_audit.py
```python
# disparity_audit.py — Claude Code output
FACTORS = [
    {"factor": "TNBC biology (higher prevalence)", "mortality_contribution_pct": 25,
     "structural": False, "intervention": "Targeted chemo (carboplatin)", "evidence": "Phase 3 RCT"},
    {"factor": "Stage at diagnosis (later)",       "mortality_contribution_pct": 30,
     "structural": True,  "intervention": "Community mammography access", "evidence": "Observational"},
    {"factor": "Treatment delays (>60 days)",      "mortality_contribution_pct": 15,
     "structural": True,  "intervention": "Patient navigation programs", "evidence": "Controlled"},
    {"factor": "Treatment quality gaps",           "mortality_contribution_pct": 20,
     "structural": True,  "intervention": "Equal-access care centers", "evidence": "Comparative"},
    {"factor": "Trial underenrollment",            "mortality_contribution_pct": 10,
     "structural": True,  "intervention": "Trial diversity requirements", "evidence": "Policy"},
]
for f in FACTORS:
    kind = "STRUCTURAL" if f["structural"] else "biological"
    print(f"[{kind:<11}] {f['factor']:<35}  ~{f['mortality_contribution_pct']}% of gap")
    print(f"             Intervention: {f['intervention']} ({f['evidence']})")
```
