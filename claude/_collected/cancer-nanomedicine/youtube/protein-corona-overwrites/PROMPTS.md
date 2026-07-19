# PROMPTS — protein-corona-overwrites

## B02 Claude Research Prompt
```
claude "Research protein corona formation on nanoparticles in biological environments. Explain: (1) the kinetics — how fast hard and soft corona form; (2) which proteins adsorb first (albumin, apolipoproteins, fibrinogen, complement C3); (3) the consequences for active targeting (buried ligands), immune clearance (opsonization → MPS uptake), and pharmacokinetics; (4) the strategies to minimize corona formation (PEG coating, zwitterionic surfaces, stealth design) and their limitations; and (5) whether exploiting the corona (designing particles to adsorb specific proteins) is a viable alternative strategy."
```

## B05 Claude Revision Prompt
```
claude "Compare two protein corona strategies: (a) designing a pre-coated particle that adsorbs a specific corona you choose (albumin-coated for stealth, apolipoprotein A-I corona for liver targeting), vs. (b) eliminating the corona entirely with zwitterionic surfaces. What evidence exists for each in vivo? Has either entered clinical trials?"
```

## B03 Python Script
```python
# protein_corona.py
CORONA_TIMELINE = [
  {"time": "<30 s",  "layer": "soft",
   "proteins": ["albumin", "fibrinogen"],
   "consequence": "Vroman effect — albumin arrives first"},
  {"time": "<1 min", "layer": "hard",
   "proteins": ["apolipoprotein", "complement C3"],
   "consequence": "opsonization -> MPS clearance"},
  {"time": ">1 min", "layer": "stable hard",
   "proteins": ["immunoglobulins", "vitronectin"],
   "consequence": "targeting ligands buried — new identity"},
]
print("PROTEIN CORONA TIMELINE (Vroman effect):")
for t in CORONA_TIMELINE:
    print(f"  {t['time']:8} {t['layer']:10} {t['consequence']}")
```
