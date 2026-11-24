# FRICTIONAL — Brutalist, Shared

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-10-24
- **Tried:** build this week's video from the newest brutalist.art content. **Expected:** one topic.
  **Found:** three pull requests merged on Oct 23 (the first in the repo's history) plus three Blender
  skills; chose "the toolkit became shared" as the through-line.
- **Resisted:** the draft said "first three pull requests from fellows". Not every author could be
  confirmed as a fellow, so it now says "the first three pull requests in its history", which git proves.
- **Resisted:** the draft said thumbnails change "only number and command"; the 4K outputs shown carry
  no number, so the line now matches what is on screen (command + mascot).
- **Resisted:** beat IDs B05/B06 are reserved for Professor Bear's notes in fellows reels and triggered
  the notes-approval gate. Renumbered beats in tens (B00…B90); no notes beats exist in this film.
- **Resisted:** the toolkit finds Manim scenes by the literal `class Bxx_Name(Scene)` pattern; a shared
  base class hid them. Rewrote as plain Scene classes with a small Clock helper.
- **Resisted:** first layout previews overflowed the frame (text sized for a larger canvas); the portrait
  Short needed its frame pinned to 4.5 × 8 units. Every scene was re-checked by looking at frames.
- **Resisted:** the hesitant-writer beat first ended on the *uncorrected* line; shortened to one line
  so the correction lands with time to read it.
- **AI contribution:** Claude researched the commits, drafted script, sheets and scenes, and rendered.
  Kokoro `am_onyx` speaks the narration. Voice approval is Boopesh's to confirm.
- **Still open:** Whisper-based pronunciation check could not run (model host blocked in the build
  container); names were checked by phonemes instead and need a human listen.

---

## 2026-11-24 — Submission note for the week of Oct 18–24 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Oct 18–24. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
