# PROMPTS — cancer-dormancy-recurrence

## B02 Research Prompt
```
claude "Research cancer dormancy: the molecular mechanisms that hold disseminated tumor cells in a dormant state (TGF-beta2, BMP signaling, urokinase receptor ratio), the known triggers of reactivation (aging bone marrow niche, inflammatory signals, surgery, anesthesia), and the clinical evidence for dormancy duration in breast, prostate, and melanoma. Which therapies have shown ability to maintain dormancy or prevent reactivation?"
```

## B05 Revision Prompt
```
claude "For each reactivation trigger, what is the evidence that it is clinically actionable — is there a trial blocking that trigger in humans, and what happened?"
```

## B03 Script: dormancy_triggers.py
```python
# dormancy_triggers.py — Claude Code output
MECHANISMS = [
    {"mechanism": "TGF-b2/p38 MAPK arrest",   "evidence": "STRONG", "druggable": True,
     "strategy": "TGF-b inhibitors (trials: galunisertib)"},
    {"mechanism": "BMP pathway suppression",   "evidence": "MODERATE", "druggable": True,
     "strategy": "BMP7 analogs (preclinical)"},
    {"mechanism": "uPAR:uPA ratio low",        "evidence": "MODERATE", "druggable": False,
     "strategy": "No approved drug"},
    {"mechanism": "Aging bone marrow niche",   "evidence": "STRONG", "druggable": False,
     "strategy": "Exercise + anti-inflammatory (observational)"},
    {"mechanism": "Post-surgical inflammation","evidence": "WEAK", "druggable": True,
     "strategy": "NSAIDs peri-op (pilot trials)"},
]
for m in MECHANISMS:
    drug = "DRUGGABLE" if m["druggable"] else "no drug target"
    print(f"[{m['evidence']:<8}] {m['mechanism']:<30}  {drug}")
    print(f"           Strategy: {m['strategy']}")
```
