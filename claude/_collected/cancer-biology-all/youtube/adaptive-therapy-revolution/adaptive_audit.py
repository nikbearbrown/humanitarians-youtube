#!/usr/bin/env python3
# adaptive_audit.py — count the claim, don't trust it.
# Prints a progression-free-survival comparison across cancer types.
# Runs as-is: `python3 adaptive_audit.py`
TRIALS = [
    {"setting": "Prostate (abiraterone)", "PFS_mo": 27.0,
     "control_PFS_mo": 16.8, "status": "Phase 2 complete"},   # Zhang et al. 2017, Nat Commun 8:1816
    {"setting": "Breast (endocrine)",     "PFS_mo": None,
     "control_PFS_mo": None, "status": "Preclinical only"},
    {"setting": "GBM (TMZ)",              "PFS_mo": None,
     "control_PFS_mo": None, "status": "Phase 1 recruiting"},
]
for t in TRIALS:
    pfs = (f"{t['PFS_mo']:.1f} vs {t['control_PFS_mo']:.1f} mo"
           if t['PFS_mo'] else "no RCT data")
    print(f"{t['setting']:<26} {pfs:<18} [{t['status']}]")
