# CARRY-OUT — knowledge-work-plugins--claude-liam-guideline-generation

**The line (written first, GATE C):**

> A Claude brand voice guideline isn't its own taste in good writing —
> it's a fixed extraction run on your source material that returns the
> same patterns every time, and it stops the moment you ask it to judge
> rather than extract.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
written extraction procedure vs. Claude's own literary taste), not the
topic (brand voice guidelines generally).

**The wrong guess it defeats:** that asking Claude to write a brand voice
guideline means it forms its own opinion about what your writing should
sound like — the way an editor with good taste would. It doesn't. The
`guideline-generation` skill reads the source material you hand it and
pulls out the same kind of patterns every time, the same way regardless of
whose writing it is. Ask it to judge whether a voice is any good, and it
has no step written for that; it will not invent taste it wasn't given a
procedure for.

**GATE C — signed:** derived directly from the source sheet's own intact
facts (see QUESTION.md) — the source beat_sheet.json's non-broken fields
already state the skill's scope ("Generates brand voice guidelines from
source materials," read-then-execute-then-return, same input → same
output, limited to what SKILL.md specifies); this line compresses that
into the reel's carry-out.
