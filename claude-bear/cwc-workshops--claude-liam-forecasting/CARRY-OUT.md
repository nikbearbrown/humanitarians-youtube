# CARRY-OUT

> Claude picks compute-it-yourself or hand-it-to-a-subagent by the flags —
> horizon, seasonality, promo, trend — not by guesswork, and whichever path
> runs, the number it returns is a computed estimate, never a fact about
> next month.

Test: if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses both halves of the skill (how the path gets
chosen; what the resulting number actually is) without overstating either.

**Wrong guess this defeats:** "Claude always spawns a subagent to forecast"
(or its mirror, "Claude just runs one formula every time"). Both miss that
the SKILL.md makes this a flag-gated decision: horizon ≤ 14 days, not
seasonal, no promo next month, and no mentioned trend break routes to a
one-line rolling mean (Path A); any one of those flipping routes to a
forecaster subagent that gets its own context window for the full 90-day
history (Path B) — because loading that history into the main conversation
would crowd out the rest of the task.
