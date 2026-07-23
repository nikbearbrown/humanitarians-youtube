# PROMPTS — nanoparticle-characterization

## B02 Claude Research Prompt
```
claude "Research the nanoparticle characterization cascade required for regulatory submission. For each of the seven key measurements — size (DLS), polydispersity index (PDI), zeta potential, encapsulation efficiency, drug release rate, colloidal stability, and sterility/endotoxin — explain: what it measures, its primary artifact or limitation, the acceptable range or regulatory expectation, and why that parameter matters for clinical safety or efficacy. Explain why triangulation across multiple methods is required (no single measurement is sufficient) and what cryo-TEM adds vs. DLS."
```

## B05 Claude Revision Prompt
```
claude "Explain why a nanoparticle formulation that passes all seven lab characterization tests can still fail in vivo. Identify the three most common reasons for in vitro/in vivo discordance: (1) protein corona changes everything after injection; (2) in vitro release assays don't replicate endosomal conditions; (3) DLS in buffer ≠ DLS in plasma. For each, what does the discordance look like experimentally?"
```

## B03 Python Script
```python
# np_characterization.py
CASCADE = [
  ("Size (DLS)",         "1-1000 nm",   "overestimates large particles (intensity-weighted)"),
  ("PDI",               "<0.2",        "not absolute — preparation-dependent"),
  ("Zeta potential",    ">±30 mV",     "ionic strength masks true surface charge"),
  ("Encapsulation eff.","70%+",        "dialysis artifact: equilibrium not equilibrated"),
  ("Drug release",      ">80% in 24h", "in vitro release ≠ in vivo release (pH, enzymes)"),
  ("Colloidal stability","<10% change", "buffer ≠ serum conditions"),
  ("Sterility/endotoxin","<0.5 EU/mL",  "LAL assay — NP surface can interfere"),
]
for m, spec, artifact in CASCADE:
    print(f"  {m:<22} spec={spec:<12} artifact: {artifact}")
```
