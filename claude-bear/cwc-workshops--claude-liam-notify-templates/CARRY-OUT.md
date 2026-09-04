# CARRY-OUT

> Claude doesn't write these alerts — it fills three fixed templates from
> data it already has. A sweep becomes one summary and one append, never
> one call per SKU.

Test: if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses both halves of the skill (fixed template, not
composed prose; one batch append, not N per-item calls) without
overstating either.

**Wrong guess this defeats:** "Claude writes each notification" (composes
custom prose per alert). The skill's own opening line rules this out:
"Notifications are template fills, not creative writing. Do not spawn a
subagent for this." The mirror wrong guess — that a daily sweep across many
SKUs should send one alert per SKU — is also wrong: the skill's own
"Batch, don't spam" rule says send one summary notification for a sweep,
and even when a task explicitly asks for one message per SKU, every line
still goes into a single batch append, never one call per notification.
