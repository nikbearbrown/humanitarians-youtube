# PROMPTS — hpv-vaccination-elimination

## B02 Claude Research Prompt
```
claude "Research the Australian HPV vaccination program. What is the current vaccination coverage? How has vaccine-type HPV prevalence changed in vaccinated cohorts? What does WHO define as cervical cancer elimination? What is the projected year Australia will reach that threshold? Compare with a country that has low HPV vaccination coverage."
```

## B05 Claude Revision Prompt
```
claude "What would happen to Australia's cervical cancer elimination projection if HPV vaccination rates drop below herd immunity threshold? What is that threshold estimated to be?"
```

## B03 Python Script
```python
# hpv_projection.py
COUNTRIES = [
  {"country": "Australia",
   "coverage_pct": 84,
   "hpv_prevalence_drop": "~80-90% in vaccinated cohorts",
   "incidence_2024": 6.5,
   "elimination_year": "~2028",
   "who_threshold": 4.0},
  {"country": "Romania",
   "coverage_pct": 10,
   "hpv_prevalence_drop": "minimal change",
   "incidence_2024": 26.0,
   "elimination_year": "N/A",
   "who_threshold": 4.0},
]
WHO = 4.0
print(f"{'Country':<12} {'Coverage':<10} {'Incidence':<12} {'Elimination'}")
print("-" * 55)
for c in COUNTRIES:
  status = "ON TRACK" if c['incidence_2024'] < 10 else "NOT ON TRACK"
  print(f"{c['country']:<12} {c['coverage_pct']}%{' ':<7} "
        f"{c['incidence_2024']}/100k{' ':<4} {c['elimination_year']} ({status})")
```
