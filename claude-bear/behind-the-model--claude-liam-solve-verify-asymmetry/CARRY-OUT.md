# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **For hard problems, checking an answer costs far more than producing
> one — and a faster model doesn't close that gap, it just produces more
> answers that still need checking.**

(Compressed from the source's B07 summary beat — "The gap is not about AI
speed. It is about problem structure... Faster models widen the gap — they
produce more candidates per unit time, each of which still requires full
verification" — restated in Plain register. It states mechanism, not a design
judgment, so nothing needed removing.)

## The wrong guess it defeats

That because an AI answers fast, confirming the answer should be about as
fast — you're just glancing at work already done. That's backwards for hard
problems: the measured ratio of check-time to solve-time runs from about 3x
on simple arithmetic to about 300x on a full proof sketch, and it holds even
after the one suspicious number (that low 3x) was traced to a measurement
artifact and corrected. Producing one plausible answer is comparatively
cheap; confirming it's actually correct means doing the real computation —
the expensive part.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (speed at generating an
answer vs. cost of confirming it) without claiming faster models are useless
or that every task has this gap to the same degree.

## What it deliberately does not say

- Not a claim that every AI answer needs a hundred-times-longer check — the
  ratio is measured per problem type and grows with difficulty; simple
  arithmetic ties out close to 1:1 once the measurement artifact is removed.
- Not a claim that a big ratio means the AI's answer was wrong — a checked
  ratio only measures confirmation cost, independent of whether the answer
  happens to be right (direction A, B05).
- Not a claim that faster models are bad — a faster model doesn't widen the
  per-problem ratio; it can widen the total volume of unchecked answers
  produced per unit time (direction B, B06).

---
**GATE C — signed:** ______________________  (human)
