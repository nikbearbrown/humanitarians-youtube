# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Every Google Drive call Claude makes turns on three habits — treat a
> folder as a file, add `supportsAllDrives` for anything shared, and export
> instead of download for anything Google made — skip one and the failure
> looks like something else entirely, never like a missing parameter.**

## The wrong guess it defeats

That Claude finds a file in your Drive by walking a folder path, the way a
normal filesystem would. There is no path API. Every object in Drive —
including a folder — is a file, and hierarchy exists only through each
file's `parents` array of IDs. Ask for "the contents of this folder" and
Claude isn't calling a folder-contents endpoint; it's filtering files by
which ID appears in their `parents` list.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (three specific habits
govern every call, and a violated habit fails silently under a misleading
error) without overstating what those three habits guarantee.

## What it deliberately does not say

- Not a verdict on whether the Google Drive API skill is well designed —
  that's Teardown territory; this reel states the mechanism and stops.
- Not a claim that these three habits are the *only* things that matter —
  `fields=` scoping beyond `nextPageToken`, rate limits, and export size
  caps are real, but the carry-out compresses the three habits that govern
  every single call, not the full reference.
- Not a claim that every Drive request needs the bundled scripts — only
  that a hand-rolled request still owes the same three habits.

---
**GATE C — signed:** ______________________  (human)
