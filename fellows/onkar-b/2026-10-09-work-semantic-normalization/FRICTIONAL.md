# Frictional log — Semantic Normalization

## 2026-10-09 — the project update, in two aspect ratios

**What I was working on.** A project update explainer on replacing strict string equality with a semantic parser to handle the unpredictable formatting of LLM outputs.

**What I tried, and what I expected.** 
- I initially expected the LLM to output clean integers if I provided a strict system prompt.
- When that failed, I tried strict Python equality checks (`if claim == truth`), expecting stylistically identical outputs.

**Where it resisted, and what I did next.** 
- The strict equality check caused massive false positives. Mathematically accurate claims (e.g., "5 million") were failing against the ledger (e.g., "5000000") solely due to syntax.
- I engineered a regex parser (`parse_financial_number`) inside `main.py` that forcefully strips text, commas, and suffixes, converting both the claim and the truth into standard float values before evaluation.

**What Claude contributed, and what I did with it.** 
- Mine: The logic requirement to separate magnitude errors from data type errors.
- Claude's: Writing the core regex extraction script and handling the multiplier logic (k, m, b) to ensure strings like `4.5M` safely convert to `4500000.0`.

**What I understand now, and what I still do not.**
- Understood: Security layers must evaluate the underlying mathematical value of AI output, not the stylistic syntax.