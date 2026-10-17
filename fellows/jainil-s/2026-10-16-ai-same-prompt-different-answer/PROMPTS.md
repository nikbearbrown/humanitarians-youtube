# PROMPTS — Same Prompt, Different Answer

## On-screen prompts

**B00 — the ask.**

> Same prompt, same model, two different answers. Is this a bug?

Output lines: `Almost certainly not.` · `And temperature 0 won't fix it either.`

**B07 — the handoff.** Read aloud verbatim, then discussed.

> I have tests that compare model output to an expected string, and they fail
> intermittently. Help me rewrite them to assert on the properties I actually
> care about instead of on exact text.

Why this prompt: the reel's practical consequence is that asserting on exact
output is the wrong test, and lowering the temperature is the wrong fix. The
prompt points at the thing the viewer can actually change. The narration says
so explicitly rather than leaving it implied.

## Build prompt

**`DigitDiff` / `DigitDiff916`**

> Two numbers that are supposed to be identical, set in mono and aligned
> character for character, with the shared prefix in ink and everything from
> the first disagreeing character onward in terracotta on BOTH rows. Alignment
> is the whole point: a reader has to see *where* the two computations parted
> company, not merely that they did. A `diffLabel` line underneath carries the
> size of the gap. Portrait sets the numbers smaller rather than cropping,
> because the digits that differ are at the end of the string.

## Evidence script

`sampling_evidence.py` was written and run before any narration existed. Its
temperature-zero section was then **rewritten** after checking SGLang's
documentation, because the original framing blamed floating-point
non-associativity directly and that is not correct. See `SOURCES.md` →
"A correction this source forced".
