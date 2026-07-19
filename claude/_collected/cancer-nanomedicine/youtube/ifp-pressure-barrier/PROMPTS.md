# PROMPTS — ifp-pressure-barrier

## B02 Claude Research Prompt
```
claude "Research the interstitial fluid pressure (IFP) problem in solid tumor drug delivery. Explain: (1) how elevated IFP develops (leaky blood vessels + absent functional lymphatics); (2) why elevated IFP reverses the pressure-driven convection of drugs and nanoparticles — only diffusion drives inward transport at the tumor center; (3) the rim-dominant drug distribution this creates; (4) Jain's vascular normalization hypothesis — how anti-VEGF therapy temporarily reduces IFP by normalizing vessel structure; and (5) what losartan and other anti-fibrotic strategies do to the collagen barrier that maintains elevated IFP."
```

## B05 Claude Revision Prompt
```
claude "Evaluate the vascular normalization window: the brief period after anti-VEGF treatment when vessels are normalized and IFP temporarily drops before pruning. What timing data exists for combining anti-angiogenics with chemotherapy or nanoparticles to hit this window? What clinical trials have tested this? What does losartan do to the collagen barrier that maintains elevated IFP?"
```

## B03 Python Script
```python
# ifp_gradient.py
TISSUES = [
  {"type": "Normal tissue",
   "ifp_mmhg": "0-3",
   "lymphatics": "functional",
   "transport": "convection INWARD + diffusion",
   "drug_dist": "uniform"},
  {"type": "Solid tumor",
   "ifp_mmhg": "20-60 (pancreatic: up to 80)",
   "lymphatics": "absent/dysfunctional",
   "transport": "convection OUTWARD at rim; diffusion only",
   "drug_dist": "RIM-DOMINANT"},
]
print("IFP COMPARISON (Jain lab data):")
for t in TISSUES:
    print(f"  {t['type']}: IFP={t['ifp_mmhg']} mmHg | {t['drug_dist']}")
```
