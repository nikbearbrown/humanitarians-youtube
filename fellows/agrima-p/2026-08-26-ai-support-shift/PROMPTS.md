# PROMPTS — ai-support-shift
# Beat-prefixed generation prompts. No open pantry slots — nothing to
# generate; this file is kept for GATE F completeness (composer/code
# beats carry their own real prompts inline in beat_sheet.json).

No archival/pantry assets are needed for this reel. Every non-composer beat
is a from-scratch Manim scene in scenes.py; every composer/code beat's
"prompt" IS the on-screen content (see beat_sheet.json `shot.remotion.props.command`
for B02/B05/B09) and is not a separate generation task.

For reference, the two build prompts this reel's story is built around
(the ones a viewer would actually paste into Claude Code):

## B02 — write the old bot
```
claude "write support_bot_v1.py — an old-style keyword-matching support bot,
like a phone tree. Test it on 3 real support messages."
```

## B05 — revise it
```
claude "update support_bot_v1.py:
  -> match on the MEANING/intent of a message, not one exact phrase
     (a family of related signals)
  -> detect when a message is urgent/emotional enough to hand off to
     a human agent
  -> re-test on the SAME 3 messages"
```

Both prompts were actually run against Claude conversationally while
authoring this reel; the resulting scripts (`support_bot_v1.py`,
`support_bot_v2.py`) are checked into this folder and were executed for
real to capture the OUTPUT-beat transcripts — not invented.
