# Claude, Google Drive API.

Claude doesn't find a file in your Drive by walking a folder path — there's
no path API. Everything in Drive, including a folder, is a file, and
hierarchy exists only through each file's `parents` array of IDs. Ask for
"the contents of this folder" and Claude filters files by which ID appears
in their `parents` list, because there's no "get folder contents" call.
Files on a shared drive are invisible by default: seeing them takes three
extra parameters on the search, and once the list comes back, `fields=`
has to explicitly ask for `nextPageToken` or the results quietly stop at
one page. Get all three shared-drive parameters right and the list comes
back complete, page after page — but if that file turns out to be a Google
Sheet, it has no downloadable bytes, and pulling it with `alt=media`
returns a flat 403, not a helpful error; the fix is the export endpoint
instead. Skip any one of these three habits and the failure never says
which parameter you missed — a missing `supportsAllDrives` just looks like
the file was never there.

**Topic:** GOOGLE DRIVE API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-google-drive-api

---

## Chapters

0:00 Claude finds my file by its folder path in Drive. Right?
0:12 Not a separate thing — a file with a mimeType
0:27 THE ANCHOR — shared drive, invisible by default
0:46 Complete — or silently wrong
1:12 Carry-out
1:23 Your turn
1:43 Outro

---

## YOUR TURN

"Find all spreadsheets modified in the last 30 days on our shared drive,
and export the first one as CSV."

Why it's worth running: it forces three checks in one shot — does Claude
pass all three shared-drive parameters on the search, does it request
`nextPageToken` in `fields=` instead of assuming one page is everything,
and does it reach for the export endpoint instead of `alt=media` once it
sees the result is a Google Sheet.

---

## Deliberately not claimed

Not a verdict on whether the Google Drive API skill is well designed —
that's Teardown territory; this reel states the mechanism and stops. Not a
claim that these three habits are the only rules that matter — `fields=`
scoping beyond `nextPageToken`, rate limits, the `gdrive` helper's
session-only lifetime, and the export size cap are real, but the
carry-out compresses the three habits that govern every single call, not
the full reference. Not a claim that every Drive request needs the
bundled scripts — only that a hand-rolled request still owes the same
three habits.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
