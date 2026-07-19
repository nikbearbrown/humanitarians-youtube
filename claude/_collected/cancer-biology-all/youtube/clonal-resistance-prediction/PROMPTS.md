# PROMPTS — clonal-resistance-prediction

## B02 Research Prompt
```
claude "Research clonal evolution of EGFR-mutant NSCLC under targeted therapy: map the resistance mechanisms by frequency (T790M, C797S, MET amplification, HER2 amplification, histologic transformation), the approved second and third-generation therapy sequence, and the point at which no approved therapy exists. For each resistance mechanism, identify whether ctDNA can detect it before imaging."
```

## B05 Revision Prompt
```
claude "Add the ctDNA detection window for each resistance node: how many months before imaging does a ctDNA liquid biopsy typically detect the resistance clone?"
```

## B03 Script: resistance_tree.py
```python
# resistance_tree.py — Claude Code output
NODES = [
    {"mutation": "T790M",       "freq_pct": 55, "next_therapy": "Osimertinib", "ctdna_lead_mo": 4},
    {"mutation": "MET amp",     "freq_pct": 15, "next_therapy": "None approved", "ctdna_lead_mo": 3},
    {"mutation": "HER2 amp",    "freq_pct":  5, "next_therapy": "None approved", "ctdna_lead_mo": 2},
    {"mutation": "C797S (post-osi)", "freq_pct": 20, "next_therapy": "Trial only", "ctdna_lead_mo": 5},
    {"mutation": "SCLC transform",   "freq_pct":  5, "next_therapy": "Platinum-etoposide", "ctdna_lead_mo": None},
]
for n in NODES:
    lead = f"{n['ctdna_lead_mo']}mo early" if n['ctdna_lead_mo'] else "not detectable"
    print(f"{n['mutation']:<22} {n['freq_pct']:>3}%  next: {n['next_therapy']}  ctDNA: {lead}")
```
