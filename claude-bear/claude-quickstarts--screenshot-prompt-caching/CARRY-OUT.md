# CARRY-OUT.md (GATE C — written before narration)

**Carry-out line:**

> Claude doesn't know a screenshot repeats until you tell it to remember one —
> and that memory only lasts until the picture, or the session, changes.

**Secondhand test:** if someone repeats only this in a meeting next week, is
it still true? Yes — it compresses the actual distinction (caching is
requested, not automatic; and it's bounded, not permanent) without needing
the 50-turn / 5-state arithmetic to back it up.

**The wrong guess it defeats:** "Claude already looked at this screenshot
once, so sending it again must be free" — plausible because nothing about
the *content* changed, and wrong because the API has no built-in notion of
"I've seen this exact image before" without an explicit `cache_control` flag
on the block.

**sparkLine (short form, for the on-screen quote card):** "Remembered, not
free."
