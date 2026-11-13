# PROMPTS — It Was Still Learning

## On-screen prompts

**B00 — the ask.**

> Training accuracy is 100% and validation is flat. Safe to stop?

Output lines: `Flat is not the same as finished.` ·
`Sometimes it generalises much later.`

**B06 — the handoff.** Read aloud verbatim, then discussed.

> Here is my early stopping configuration. Help me work out whether it could
> have halted a run that was still improving on held-out data, and what signal
> other than validation accuracy I could watch instead.

Why this prompt: the reel's finding is only actionable against a specific
stopping rule, and patience settings are almost always inherited from whatever
template the script started life as. The narration says that out loud rather
than leaving it implied.

## Build prompts

**None.** No component was built for this reel — see `SHOTLIST.md`. The three
body beats reuse `CardSet`, `DoubleDescentCurve` and `ClaudeBarChart`, all
built in earlier weeks and all verified Claude-skinned before use.

## Evidence script

`grokking_evidence.py` was written and run before any narration existed, and
**three configurations were discarded** before one reproduced the phenomenon
cleanly — two of which produced delayed *partial* generalisation that would
have been easy to describe loosely as grokking. See `FACTCHECK.md` →
"Changed during the build".
