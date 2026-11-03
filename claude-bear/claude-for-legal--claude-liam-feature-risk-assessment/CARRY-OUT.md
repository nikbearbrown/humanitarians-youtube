# CARRY-OUT — claude-for-legal--claude-liam-feature-risk-assessment

**The sentence:**

> A feature-risk-assessment doesn't tell you a feature is safe — it tells you what to look at before someone decides.

**Test:** if someone repeats only this in a meeting next week, is it still true? Yes —
it names the actual output (a documented checklist, not a verdict) without naming any
specific skill's steps, so it survives being repeated out of context.

**The wrong guess it's built to defeat:** that "run a risk assessment" means "get a
safe / not-safe answer" — that the output is a judgment call Claude renders for you. The
reel falsifies this with a concrete case (B01): a feature that looks harmless on a quick
look (an optional photo-ID upload) still gets the same four questions asked of it that
any feature gets — the checklist doesn't skip an item because the feature looks fine.

**Why this compresses the distinction that matters, not the topic:** the topic is
"feature risk assessment"; the distinction is *documented vs. judged*. Every body beat
exists to make that distinction land — the four boxes (B02, planted; B03, paid off) are
what make "someone has what they need to decide" a checkable, specific outcome rather
than a vague gesture at "risk was considered."
