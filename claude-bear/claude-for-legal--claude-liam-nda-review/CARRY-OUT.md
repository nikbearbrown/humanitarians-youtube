# CARRY-OUT — claude-for-legal--claude-liam-nda-review

**The sentence:**

> A clean NDA review isn't a green light — it's only checked once someone reads the flagged clauses against the law that actually applies.

**Test:** if someone repeats only this in a meeting next week, is it still true? Yes —
it names the actual boundary (flag vs. legal check) without naming any tool's specific
steps, so it survives being repeated out of context.

**The wrong guess it's built to defeat:** that asking Claude to review an NDA means
getting it cleared — a final legal sign-off that it's safe to sign. The reel falsifies
this with a concrete case (B01): a confidentiality clause that never carves out
information which later becomes public through no fault of anyone. That clause reads
exactly like a complete, ordinary definitions section sitting next to every other
clause that does include the standard carve-outs — the gap is invisible unless it's
checked against a baseline, and "nothing flagged" doesn't mean nothing is missing.

**Why this compresses the distinction that matters, not the topic:** the topic is
"NDA review"; the distinction is *a flag against a baseline vs. a legal clearance*.
Every body beat exists to make that distinction land — the missing-carve-out case
(B01) is what a baseline check can quietly miss, and the verification boundary
(B02–B03) is what turns a flag into either "fine after all" or "needs to change."
