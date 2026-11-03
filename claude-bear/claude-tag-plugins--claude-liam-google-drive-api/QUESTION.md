# QUESTION

**The question:** "Claude, Google Drive API." — when Claude finds a file in
your Drive, is it walking a folder path the way a normal filesystem would,
or is something else going on? Answered using the Google Drive API skill's
own worked facts as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/google-drive/skills/google-drive-api/../../youtube/claude-liam-google-drive-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold
open, B01 anatomy, B02 design, B05 teardown tell, BVDT verdict, BHTF
handoff, BOUT outro — all already REMOTION, no puppet/AI-video/pantry beat
to replace beyond the WRITER LAW swap). This reel keeps the question and
the source's body facts, re-registers the narration to Plain, replaces the
cold open with the Brutalist Hesitant Writer, folds the source's BVDT
verdict recap into a proper carry-out beat, and closes with the
Humanitarians AI skin.

**Why it earns a reel:** the Google Drive API skill covers the Drive REST
API v3 across two base hosts (metadata/search vs. upload). Everything in
Drive — including a folder — is a file; a folder is just a file whose
mimeType says so, and hierarchy is expressed entirely through each file's
`parents` array. There is no path API and no "list folder contents"
endpoint — you filter files by which folder ID appears in `parents`.
Google Workspace files (Docs, Sheets, Slides) have no downloadable bytes:
pulling them with `alt=media` returns a 403 `fileNotDownloadable`; they
have to go through the export endpoint instead. Responses only return the
fields you ask for, and the default subset omits `nextPageToken` — a
listing that looks complete can be silently truncated at one page. Files
on a shared drive are invisible by default; seeing them requires
`supportsAllDrives=true` on every call, plus two more parameters
(`corpora=allDrives`, `includeItemsFromAllDrives=true`) on list/search
calls — miss it and the file returns 404, indistinguishable from "doesn't
exist." Two bundled scripts, `drive_search.sh` and `drive_read.sh`, handle
the q-expression building, pagination, all-drives access, and the
mimeType branch between export and download.

**Naive framing (B00, corrected on screen):** "Claude finds my file by its
folder path in Drive. Right?" → corrects "path" to "ID" (there is no path
API; Drive resolves everything by file ID through the `parents` array).

**Body facts carried from source (unchanged):**
- everything is a file, including folders (`mimeType` says "folder");
  hierarchy is the `parents` array; no path API, no "get folder contents"
  call — you filter by parent ID
- Workspace files (Docs/Sheets/Slides) have no bytes — `alt=media` returns
  403 `fileNotDownloadable`; use the export endpoint instead. Binary files
  download directly via `alt=media`
- `fields=` must explicitly include `nextPageToken` or pagination silently
  stops after the first page (default subset omits it)
- shared drive files are invisible unless `supportsAllDrives=true` is set
  on every request; list/search calls need two more parameters
  (`corpora=allDrives`, `includeItemsFromAllDrives=true`); missing it
  returns 404, not a parameter error
- two bundled scripts: `drive_search.sh` (q-expression, pagination,
  all-drives) and `drive_read.sh` (branches on mimeType: export vs.
  download, guards large binaries)
- Your Turn: paste a real "find spreadsheets modified in the last 30 days
  on a shared drive, export the first as CSV" request and watch whether
  Claude passes all three shared-drive parameters, asks for
  `nextPageToken`, and branches to export instead of `alt=media` once it
  sees the file is a Sheet
