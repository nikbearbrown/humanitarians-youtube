# PROMPTS — two-threads-one-week (v2 revision)
# Beat-prefixed generation prompts. No open pantry slots — nothing to
# generate; this file is kept for GATE F completeness (composer/code
# beats carry their own real prompts inline in beat_sheet.json).

No archival/pantry assets are needed for this reel. Every non-composer beat
is a from-scratch Manim scene in scenes.py; every composer/code beat's
"prompt" IS the on-screen content (see beat_sheet.json `shot.remotion.props.command`
for B02/B05/B09) and is not a separate generation task.

For reference, the two build prompts this reel's story is built around
(the ones a viewer would actually paste into Claude Code):

## B02 — write the log script

```
claude "write weekly_log_v1.py — log this week's real work
  across two threads, writing and the Loon Project"
```

## B05 — revise it into an actual log

```
claude "update weekly_log_v1.py -> weekly_log_v2.py:
  -> turn the dump into an actual log — ordered,
     readable, one line per entry
  -> call out this week's standout from each thread"
```

Both prompts were actually run against Claude conversationally while
authoring this reel; the resulting scripts (`weekly_log_v1.py`,
`weekly_log_v2.py`) are checked into this folder and were executed for
real to capture the OUTPUT-beat transcripts — not invented.

(v2 revision note: this replaces the earlier `weekly_recap_v1.py` /
`weekly_recap_v2.py` pair, which built toward a done/pending audit tally.
Per user request, that "no overclaiming" framing is dropped in favor of a
straightforward work log — same 8 real items, same real statuses, just
without the audit()/tally emphasis.)
