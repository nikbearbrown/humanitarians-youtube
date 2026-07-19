# PROMPTS — mutational-signatures-exposure

## B02 Claude Research Prompt
```
claude "Describe five major mutational signatures using the COSMIC catalog: SBS4 (tobacco), SBS7a/b (UV), SBS2/13 (APOBEC), SBS6 (MMR-deficiency), SBS22 (aflatoxin). For each: dominant mutation spectrum, which cancers carry it, what generates it, and does identifying it currently change clinical management?"
```

## B05 Claude Revision Prompt
```
claude "Find a documented case or published report where mutational signature analysis changed a patient's treatment plan — for example a never-smoker found to carry SBS4, or MSI-high identified via SBS6 leading to pembrolizumab eligibility."
```

## B03 Python Script
```python
# signature_table.py
SIGS = [
  {"id": "SBS4",  "exposure": "tobacco",
   "cancers": "lung", "actionable": "NO"},
  {"id": "SBS7",  "exposure": "UV light",
   "cancers": "melanoma", "actionable": "YES - sun protection"},
  {"id": "SBS2/13", "exposure": "APOBEC",
   "cancers": "breast, lung, bladder", "actionable": "EMERGING"},
  {"id": "SBS6",  "exposure": "MMR defect",
   "cancers": "CRC, endometrial", "actionable": "YES - pembrolizumab"},
  {"id": "SBS22", "exposure": "aflatoxin",
   "cancers": "HCC", "actionable": "NO - retrospective only"},
]
print(f"{'Sig':<8} {'Exposure':<12} {'Cancers':<22} Actionable")
print("-" * 60)
for s in SIGS:
  print(f"{s['id']:<8} {s['exposure']:<12} {s['cancers']:<22} {s['actionable']}")
```
