# PROMPTS — pre-metastatic-niche

## B02 Research Prompt
```
claude "Research the pre-metastatic niche: the Kaplan 2005 VEGFR1 paper defining the concept, how tumor-derived exosomes with organ-specific integrins (avb5->liver, a6b4->lung) educate stromal and immune cells before CTCs arrive, the role of MDSCs and fibronectin in niche preparation, and what experimental strategies block niche formation — citing published in vivo evidence."
```

## B05 Revision Prompt
```
claude "For each organ-specific integrin pair, what is the most advanced experimental or clinical intervention blocking the exosome-integrin interaction, and what was the effect on metastatic colonization in vivo?"
```

## B03 Script: exosome_map.py
```python
# exosome_map.py — Claude Code output
INTEGRIN_MAP = [
    {"integrin": "a6b4 + a6b1", "organ": "lung",   "exosome_source": "breast",
     "MDSC_recruited": True, "blocker": "anti-a6 Ab (preclinical)"},
    {"integrin": "avb5",        "organ": "liver",  "exosome_source": "breast/pancreatic",
     "MDSC_recruited": True, "blocker": "anti-avb5 Ab (preclinical)"},
    {"integrin": "a6b1 + avb5", "organ": "brain",  "exosome_source": "breast",
     "MDSC_recruited": False, "blocker": "None identified"},
    {"integrin": "avb5",        "organ": "bone",   "exosome_source": "prostate",
     "MDSC_recruited": True, "blocker": "Denosumab (approved; different mech)"},
]
print(f"{'Integrin':<18}  {'Organ':<7}  {'Source':<20}  {'Blocker'}")
print("-" * 65)
for m in INTEGRIN_MAP:
    flag = "  <- NO BLOCKER" if m["blocker"] == "None identified" else ""
    print(f"{m['integrin']:<18}  {m['organ']:<7}  {m['exosome_source']:<20}  {m['blocker']}{flag}")
```
