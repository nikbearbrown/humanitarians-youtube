# Frictional Log — How Do You Test a Finance Agent

**Week of 2026-08-07** · Adwait Changan · Mycroft track
Topic: a successful sample run isn't enough — the controls also have to fail safely.

**What I built this week**
- `evaluation.py` — a harness that runs each case in an isolated temporary copy of the synthetic data and *plants defects*.
- Four reconciliation breaks (actuals↔ledger, unmapped account, customer↔revenue, headcount↔payroll) and two behavioral overreaches (step-limit exceeded, agent self-approval).
- Each defect is checked against an explicit expectation and contrasted with the valid baseline (−$120,000 EBITDA variance, 7 steps).

**The one idea it teaches**
- Proving a system works means proving its controls *fail safely*, not just that a clean run succeeds.

**Where it pushed back (and what I did)**
- Ran every case in an isolated copy so a planted defect could never contaminate the real data.

**What I learned**
- The valuable test isn't the passing case — it's the defect you plant to confirm the guardrail actually catches it.

_Hours this week: ~20 (across the two videos built this week)._
