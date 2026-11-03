# CARRY-OUT — skills--claude-liam-xlsx

**Sentence (BCRY, written first per CARRY-OUT LAW):**

> Write the formula, never the number it computes — that's what keeps a
> sheet alive when inputs change. And a clean error scan proves the
> formulas didn't break; it doesn't prove they point at the right cells.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the distinction that matters (formula vs.
hardcoded number) without overclaiming what `scripts/recalc.py` actually
verifies (NB11 grounds the "doesn't prove" clause in the row-offset trap —
a formula can point at the wrong cell and never throw an Excel error at
all).

**Wrong guess it defeats:** that once a value is computed, typing the
number straight into the cell is just as good as writing the formula that
produced it. NB03/NB04 break this with the skill's own absolute rule: never
calculate a value in Python and hardcode it — write the actual Excel
formula, because a typed-in number goes stale the instant an input changes
and a live formula does not.
