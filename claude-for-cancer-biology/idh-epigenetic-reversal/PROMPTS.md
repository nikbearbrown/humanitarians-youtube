# PROMPTS — idh-epigenetic-reversal

## B02 Claude Research Prompt
```
claude "Trace the causal chain from IDH1/IDH2 mutation to epigenetic phenotype in AML, citing primary literature at each step. Then research the clinical evidence for ivosidenib and enasidenib: overall response rates from the pivotal trials, and what cellular evidence confirms the epigenetic reversal mechanism (not cytotoxicity) is responsible."
```

## B05 Claude Revision Prompt
```
claude "Does the IDH inhibitor model generalize? Are there other oncometabolites that block epigenetic enzymes and could similarly be pharmacologically reversed? What is the clinical development status of succinate dehydrogenase or fumarate hydratase inhibitors?"
```

## B03 Python Script
```python
# idh_causal_chain.py
CHAIN = [
  {"node": "mutant IDH1/2",
   "mech": "neomorphic enzyme activity",
   "citation": "Ward 2010 Nature"},
  {"node": "2HG accumulates",
   "mech": "oncometabolite produced",
   "citation": "Dang 2010 Nature"},
  {"node": "TET2/KDM blocked",
   "mech": "competitive inhibition by 2HG",
   "citation": "Xu 2011 Science"},
  {"node": "hypermethylation",
   "mech": "demethylase failure -> marks persist",
   "citation": "Turcan 2012 Nature"},
  {"node": "differentiation locked",
   "mech": "blast arrest",
   "citation": "DiNardo 2018 NEJM"},
]
for i, step in enumerate(CHAIN):
  print(f"Step {i+1}: {step['node']}")
  print(f"  Mechanism: {step['mech']}")
  print(f"  Evidence: {step['citation']}")
```
