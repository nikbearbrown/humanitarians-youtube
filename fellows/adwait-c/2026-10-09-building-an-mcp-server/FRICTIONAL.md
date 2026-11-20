# Frictional Log — Building an MCP Server

**Week of 2026-10-09** · Adwait Changan · Agentic AI playlist (Episode 10)
Topic: three calls are the whole shape — list what exists, describe one in full, run it.

**What I built this week**
- A working tool server end to end, plus a client that was told nothing in advance.
- The client asks what exists, gets two tools it had never heard of, asks for one contract in full, and calls it.

**The one idea it teaches**
- Nobody wrote the tool list by hand: the names come from the registry and the descriptions come from the functions' own docstrings (via `inspect.getdoc`). The comment you write for the next developer is the thing the machine reads.

**Where it pushed back (and what I did)**
- Showed the refusal too, because discovery only means something if the published list is exhaustive.

**What I learned**
- Good docstrings aren't just documentation here — they're the live interface the agent discovers.

_Hours this week: ~20 (across the two videos built this week)._
