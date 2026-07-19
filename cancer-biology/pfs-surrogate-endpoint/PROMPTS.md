# PROMPTS — pfs-surrogate-endpoint

## B02 Research Prompt
```
claude "Research the PFS-to-overall-survival surrogate endpoint problem in oncology: what is the Spearman correlation between PFS benefit and OS benefit across cancer types (citing Prasad and Mailankody 2017, Kim and Prasad 2015), list five high-profile cases where PFS benefit did not translate to OS benefit, explain when PFS is a valid surrogate (colorectal first-line) vs invalid (second-line lung), and what the FDA's current policy is on PFS as primary endpoint."
```

## B05 Revision Prompt
```
claude "Add a column: for each case, was the PFS benefit detected in a phase 3 trial with OS as a co-primary or secondary endpoint, and did that OS endpoint eventually read out positively or negatively?"
```

## B03 Script: pfs_audit.py
```python
# pfs_audit.py — Claude Code output
CASES = [
    {"drug": "Bevacizumab (breast)", "PFS_mo": 5.9, "OS_benefit": False,
     "FDA_approved": True,  "approval_withdrawn": True},
    {"drug": "Avastin (glioblastoma)", "PFS_mo": 4.0, "OS_benefit": False,
     "FDA_approved": True,  "approval_withdrawn": False},
    {"drug": "FOLFOX (colon, 1L)",   "PFS_mo": 2.1, "OS_benefit": True,
     "FDA_approved": True,  "approval_withdrawn": False},
    {"drug": "Sunitinib (GIST)",      "PFS_mo": 24.1,"OS_benefit": True,
     "FDA_approved": True,  "approval_withdrawn": False},
    {"drug": "Palbociclib (breast)",  "PFS_mo": 10.0,"OS_benefit": None,
     "FDA_approved": True,  "approval_withdrawn": False},
]
print(f"{'Drug':<28} {'PFS benefit':>11}  {'OS confirmed':>13}  {'Status'}")
print("-" * 70)
for c in CASES:
    os = "YES" if c["OS_benefit"] else ("PENDING" if c["OS_benefit"] is None else "NO <- FLAG")
    status = "WITHDRAWN" if c["approval_withdrawn"] else "APPROVED"
    print(f"{c['drug']:<28} {c['PFS_mo']:>10.1f}mo  {os:>13}  {status}")
```
