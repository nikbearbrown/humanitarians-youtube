# PROMPTS — psma-theranostic-loop

## B02 Claude Research Prompt
```
claude "Research the PSMA radioligand theranostic pair in prostate cancer. Explain: (1) why PSMA is an ideal target (overexpression on prostate cancer cells, functional role as folate transporter, membrane-facing domain); (2) Ga-68-PSMA-617 PET imaging mechanism; (3) Lu-177-PSMA-617 (Pluvicto) therapy — the VISION trial design and overall survival result; (4) alpha vs. beta emitters — why Ac-225 (alpha) has shorter range, higher LET, and less crossfire dependency vs. Lu-177 (beta); and (5) the off-target uptake organs (salivary glands, kidneys) as dose-limiting toxicity."
```

## B05 Claude Revision Prompt
```
claude "Compare the PSMA pair (Ga-68/Lu-177-PSMA-617) with the DOTATATE pair in neuroendocrine tumors. What structural similarities exist? What clinical evidence parallels the VISION trial? What does having two validated theranostic pairs teach us about which tumor types are candidates for this approach?"
```

## B03 Python Script
```python
# psma_theranostics.py
PAIR = [
  {"isotope": "Ga-68",  "use": "PET IMAGING",
   "range": "~1 mm",   "let": "low",
   "trial": "diagnostic only"},
  {"isotope": "Lu-177", "use": "THERAPY (Pluvicto)",
   "range": "1-2 mm",  "let": "beta",
   "trial": "VISION (NEJM 2021): OS 15.3 vs 11.3 mo"},
  {"isotope": "Ac-225", "use": "THERAPY (next-gen)",
   "range": "~50 µm", "let": "alpha (high)",
   "trial": "Phase I/II ongoing"},
]
for p in PAIR:
    print(f"{p['isotope']}: {p['use']} | range={p['range']} | {p['trial']}")
```
