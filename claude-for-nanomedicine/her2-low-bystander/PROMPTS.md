# PROMPTS — her2-low-bystander

## B02 Claude Research Prompt
```
claude "Research the mechanistic difference between T-DM1 and T-DXd that enabled HER2-low breast cancer treatment. Explain: (1) the DAR trade-off (why too low = insufficient kill, too high = aggregation/clearance); (2) cleavable vs. non-cleavable linkers and the bystander effect; (3) what the DESTINY-Breast04 trial showed (HER2-low as a new targetable entity, PFS and OS benefit); and (4) why lipophilicity of the DXd payload matters for bystander killing but limits systemic toxicity concerns."
```

## B05 Claude Revision Prompt
```
claude "Survey the ADC field beyond HER2. Name two other ADCs: (1) trastuzumab deruxtecan for HER2-low lung cancer and (2) sacituzumab govitecan for TROP2-positive TNBC. For each, explain what linker/payload design enabled the new indication. What does the cleavable linker + bystander mechanism generalize to?"
```

## B03 Python Script
```python
# adc_comparison.py
ADCS = [
  {"name": "T-DM1",
   "linker": "non-cleavable (SMCC)",
   "bystander": "NO",
   "her2_min": "HER2-high (3+ or ISH+)",
   "trial": "EMILIA: OS 29.9 vs 25.9 mo"},
  {"name": "T-DXd",
   "linker": "cleavable (tetrapeptide)",
   "bystander": "YES — DXd diffuses to neighbors",
   "her2_min": "HER2-low (1+ or 2+/ISH-)",
   "trial": "DESTINY-B04 (NEJM 2022): PFS 9.9 vs 5.1 mo"},
]
for a in ADCS:
    print(f"{a['name']}: {a['linker']} | bystander={a['bystander']}")
```
