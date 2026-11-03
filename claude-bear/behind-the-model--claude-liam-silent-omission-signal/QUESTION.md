# QUESTION

**The question:** "Silent Omission Signal" — an agent processes what it can
reach and reports the result as the whole picture, with no error, no
warning, no count of what was skipped. What makes that omission *silent*,
and what actually catches it?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-silent-omission-signal/beat_sheet.json`
(metadata `register: "Teardown"`, `brand: "claude-liam"`, build `cut:
"review"`, 4 of 9 array entries filled: B01-B04 rendered as Manim video,
B00/B05/B06/YOURTURN/B07 left as unfilled slates, plus 3 further unfilled
BOOKEND slates — BVDT/BHTF/BOUT — carrying only placeholder text, never
reconciled with the earlier beats). This reel keeps the question and the
source's body facts, re-registers the narration to Plain, replaces the cold
open with the Brutalist Hesitant Writer, folds the source's B05 (verdict)
and B06+YOURTURN (two overlapping handoff asks) into a single carry-out plus
a single Your Turn, and closes with the Humanitarians AI skin.

**Why it earns a reel:** an agent given a folder of files to summarize
processes whatever it can reach and presents the result as complete. No
error message, no warning, no count of files skipped — the brief reads as
fluent and confident either way. The gap stays invisible until something
downstream uses the wrong number. This happens because agents optimize
toward task completion: a tool-call failure (a folder not found, a file not
readable) is logged internally, not surfaced in the output, unless the task
was explicitly built to surface it — silence is the path of least
resistance, not a malfunction. The recognition sign is an absence: a
complete run should carry a count ("eight documents found, eight
processed"); when that count is missing, the omission may be silent. The
fix is one added instruction — require an inventory artifact before the
summary: items in scope, items processed, items skipped, items denied. A
matching count doesn't prove the rest of the summary is accurate, and a
mismatch doesn't always mean something important was lost — but without the
count, there's no way to tell which case you're in.

**Naive framing (B00, corrected on screen):** "If a file's missing, my
agent will flag it, right?" → corrects "flag" to "skip" (the agent does NOT
flag a missing or unreadable file — it silently skips it and reports the
rest as if that were the whole job).

**Body facts carried from source (unchanged):**
- an agent asked to summarize a folder processes only what it can reach and
  presents that as the complete picture
- no error message, no warning, no count of files skipped in a silent
  omission — the output is fluent and confident regardless
- agents optimize toward task completion; a tool-call failure is logged
  internally but not surfaced unless the task explicitly asks for it
- the recognition sign: absence of a processed-count in the output (a
  complete run would name one — "eight documents found, eight processed")
- the fix: an inventory artifact required before the summary — items in
  scope, items processed, items skipped or inaccessible (with reasons)
- neither direction is guaranteed by the count alone: a match doesn't prove
  the rest of the summary is right, and a mismatch doesn't always mean
  something important was lost — the count only tells you whether you can
  see the gap at all
