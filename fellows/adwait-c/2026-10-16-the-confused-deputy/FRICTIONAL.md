# Frictional Log — The Confused Deputy

**Week of 2026-10-16** · Adwait Changan · Agentic AI — explainer
Topic: an agent that acts, plus text nobody controls, is an old security bug with a new surface.

**What I built this week**
- Took two ordinary ingredients — an operator instruction and a fetched ticket — and showed they arrive in the same context as the same kind of thing.
- Nothing in that context marks which one was authorised, so the tool runs with the agent's permissions.

**The one idea it teaches**
- The text has no permissions. The agent has yours. That gap is the whole vulnerability.

**Where it pushed back (and what I did)**
- Ranked the defences honestly: none of them *detect* an injection, all of them *limit* it, and only a human before the irreversible step holds when detection fails.

**What I learned**
- You don't fix prompt injection by detecting it. You contain it — and you keep a human in front of the irreversible action.

_Hours this week: ~20 (across the two videos built this week)._
