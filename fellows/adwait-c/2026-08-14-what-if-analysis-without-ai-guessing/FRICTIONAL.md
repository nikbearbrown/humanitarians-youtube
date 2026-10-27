# Frictional Log — What-If Analysis Without AI Guessing

**Week of 2026-08-14** · Adwait Changan · Mycroft track
Topic: finance teams need scenarios, but an agent must not quietly turn assumptions into forecasts.

**What I built this week**
- `scenario.py` — binds every scenario to the exact verified baseline run and its CSV hashes.
- Accepts only explicit `AMOUNT` or `PERCENT_OF_ACTUAL` assumptions; preserves source and assumption lineage; rejects duplicates, non-finite, and negative results.
- Deterministic arithmetic, **no external LLM**. From a verified EBITDA baseline of $230,000: +5% revenue → $275,500; −$20,000 COGS → $250,000.

**The one idea it teaches**
- Scenario math has to be deterministic and traceable, or an "illustration" silently becomes a "forecast."

**Where it pushed back (and what I did)**
- Refused anything that wasn't an explicit, bounded assumption tied to the hashed baseline.

**What I learned**
- The guardrail isn't the arithmetic — it's forbidding the agent to invent the inputs.

_Hours this week: ~20 (across the two videos built this week)._
