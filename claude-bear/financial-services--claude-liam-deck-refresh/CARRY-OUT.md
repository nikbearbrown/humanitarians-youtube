# CARRY-OUT — financial-services--claude-liam-deck-refresh

**The line (written first, GATE C):**

> A deck refresh isn't Claude rewriting the story — it's one figure,
> swapped everywhere the step says to swap it, and left alone everywhere
> else.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(a targeted figure swap vs. reconsidering the narrative built on that
figure), not the topic (deck refreshes generally).

**The wrong guess it defeats:** that "refresh the deck with the new
numbers" means Claude reconsiders the deck the way an analyst would —
updating the commentary, the trend language, maybe the framing of a slide
along with the figure it names. It doesn't. The `deck-refresh` skill reads
a written SKILL.md and executes a linear pipeline: find every instance of
the target figure across the deck, replace it with the new figure, touch
nothing else. Ask it to also rewrite a sentence built around that number
and it will not improvise the edit — that sentence is outside what the
step says to change.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope and its own worked example ($485M → $512M); this
line compresses it into the reel's carry-out.
