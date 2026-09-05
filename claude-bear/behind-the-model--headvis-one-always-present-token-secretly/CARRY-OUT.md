# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **One always-present, meaning-empty token quietly wins nearly every
> attention statistic you compute — exclude it before you trust what the
> rest of the pattern is actually showing you.**

(Compressed from the source's mechanism beat — "When no key is strongly
preferred, softmax must still spend its probability somewhere; the
ever-present, semantically-neutral BOS token becomes the low-resistance sink
where heads park leftover attention — so any max-reduction that includes it
reports the sink, not the structure" — restated in Plain register. The source
line already states mechanism, not a design judgment, so nothing needed
removing.)

## The wrong guess it defeats

That if one position wins the attention-max statistic almost every time,
across thousands of unrelated sentences, it must be carrying the sentence's
real meaning — attention is supposed to point at what matters. That's
backwards: softmax has to spend all of its probability on every row whether
or not any position deserves it, and the one position that's present in
every sequence and carries no sentence-specific meaning is the cheapest place
to park the leftover mass. In the measured case (layer 4, head 3, 50,000
sequences) token 0 wins the max in 91% of cases with over half the weight —
and the verb-to-subject dependency everyone expects only shows up once token
0 is excluded from the count.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (winning the max by
default vs. carrying real signal) without claiming every head is broken or
that excluding one token always reveals the truth.

## What it deliberately does not say

- Not a claim that a head dominated by the sink learned nothing — the real
  signal can still be sitting in the non-max mass of that same row, simply
  outweighed the moment you only look at the max (direction A, B05).
- Not a claim that a head with no BOS-dominance is automatically trustworthy
  — it may be parking its leftover weight on a different low-information
  filler token instead, and the same exclusion logic still applies
  (direction B, B06).
- Not a claim about why models learn to do this (training dynamics) — only
  the observed mechanism (softmax must spend its mass, BOS is the
  low-resistance seat) and its measured consequence for aggregate statistics.

---
**GATE C — signed:** ______________________  (human)
