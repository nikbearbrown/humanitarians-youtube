# PROMPTS — epr-delivery-funnel

## B02 Claude Research Prompt
```
claude "Research the EPR (enhanced permeability and retention) effect controversy in cancer nanomedicine. Explain the original EPR concept (Maeda, 1986), then summarize the Wilhelm 2016 meta-analysis finding (0.7% median tumor delivery). What are the five reasons for the EPR gap between mouse models and human tumors (IFP, EPR heterogeneity, mouse tumor vascularity, lack of EPR in desmoplastic tumors, protein corona)? Despite this, Doxil and Abraxane succeeded — explain why EPR was or was not the reason for their success."
```

## B05 Claude Revision Prompt
```
claude "Evaluate: is EPR-based passive targeting still a viable design principle in 2025? Or has the field moved to receptor-mediated active targeting, physical enhancement (focused ultrasound), or abandoning nanoparticles for ADCs and LNPs? What does the Doxil/Abraxane success actually tell us about EPR?"
```

## B03 Python Script
```python
# epr_attrition.py
STAGES = [
  ("Injected dose",      "100%"),
  ("Blood circulation",  "~60% remain"),
  ("Tumor vasculature", "~10% reach"),
  ("Interstitial space","~3% via EPR"),
  ("Cellular uptake",   "0.7% MEDIAN"),  # Wilhelm 2016
]
for stage, pct in STAGES:
    print(f"  {stage:<22} {pct}")
print("\nSource: Wilhelm et al., ACS Nano, 2016")
print("117 nanoparticle studies | IQR: 0.3-1.4%")
```
