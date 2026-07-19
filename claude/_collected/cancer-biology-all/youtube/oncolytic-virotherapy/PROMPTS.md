# PROMPTS — oncolytic-virotherapy

## B02 Research Prompt
```
claude "Research oncolytic virotherapy: T-VEC mechanism (modified HSV-1, deleted ICP34.5, added GM-CSF), the OPTiM trial results (durable response rate vs GM-CSF), why systemic delivery fails (neutralizing antibodies, liver sequestration, innate immune clearance), what engineering modifications are being tested to overcome systemic barriers, and the current clinical pipeline beyond melanoma."
```

## B05 Revision Prompt
```
claude "List the five most advanced systemic oncolytic virotherapy programs in clinical trials as of 2024, their virus type, modification strategy, cancer target, and current phase."
```

## B03 Script: tvec_compare.py
```python
# tvec_compare.py — Claude Code output
STRATEGIES = [
    {"delivery": "Intratumoral (T-VEC)", "virus": "HSV-1 modified",
     "DRR_pct": 16.3, "barrier": "Requires accessible lesion", "status": "FDA APPROVED"},
    {"delivery": "Systemic IV (Pexa-Vec)", "virus": "Vaccinia",
     "DRR_pct": 0.0,  "barrier": "Neutralizing Ab + liver sequestration", "status": "Phase 3 FAILED"},
    {"delivery": "Systemic (ONCOS-102)",  "virus": "Adenovirus",
     "DRR_pct": None, "barrier": "Innate immune clearance", "status": "Phase 1/2"},
    {"delivery": "Cell carrier (OV-CAR-3)","virus": "Measles",
     "DRR_pct": None, "barrier": "Cell survival after infusion", "status": "Preclinical"},
]
for s in STRATEGIES:
    drr = f"{s['DRR_pct']:.1f}%" if s["DRR_pct"] is not None else "not reported"
    print(f"[{s['status']:<18}] {s['delivery']:<30}  DRR: {drr}")
    print(f"   Barrier: {s['barrier']}")
```
