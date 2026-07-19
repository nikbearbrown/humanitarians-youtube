# PROMPTS — adaptive-therapy-revolution

## B02 Research Prompt
```
claude "Research adaptive therapy in cancer: the evolutionary rationale (Gatenby framework), the Moffitt abiraterone prostate cancer trial (Zhang et al. 2017), clinical evidence in other cancers, practical barriers to adoption, and settings where it outperforms continuous dosing. Cite published sources."
```

## B05 Revision Prompt
```
claude "Add a column for each cancer type: what is the minimum drug holiday that preserves competitive suppression? Cite any dose-scheduling trials."
```

## B03 Script: adaptive_audit.py
```python
# adaptive_audit.py — Claude Code output
TRIALS = [
    {"setting": "Prostate (abiraterone)", "strategy": "adaptive", "PFS_mo": 27.0,
     "control_PFS_mo": 16.8, "status": "Phase 2 complete"},
    {"setting": "Breast (endocrine)", "strategy": "adaptive", "PFS_mo": None,
     "control_PFS_mo": None, "status": "Preclinical only"},
    {"setting": "GBM (TMZ)", "strategy": "adaptive", "PFS_mo": None,
     "control_PFS_mo": None, "status": "Phase 1 recruiting"},
]
for t in TRIALS:
    pfsr = f"{t['PFS_mo']:.1f} vs {t['control_PFS_mo']:.1f} mo" if t['PFS_mo'] else "no RCT data"
    print(f"{t['setting']}: {pfsr} — [{t['status']}]")
```
