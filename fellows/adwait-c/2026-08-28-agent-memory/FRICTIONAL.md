# Frictional Log — Agent Memory

**Week of 2026-08-28** · Adwait Changan · Agentic AI playlist (Episode 4)
Topic: an agent has no memory — it re-pays a context budget every single turn.

**What I built this week**
- Counted what an agent actually re-sends: two tools plus one system prompt is 903 characters of instructions *before it does anything*, and every observation adds ~88 more.
- Laid out the framework: three things compete for one fixed budget.

**The one idea it teaches**
- Agents don't forget, they overflow. Context is a budget you spend each turn, not a place you store things.

**Where it pushed back (and what I did)**
- Led with the real character counts rather than an abstraction, so the "budget" idea is concrete.

**What I learned**
- Managing an agent's context is an economics problem — what's worth re-paying for every turn, and what isn't.

_Hours this week: ~20 (across the two videos built this week)._
