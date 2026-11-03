# Frictional log — Vendor Intelligence update: Who Can Approve?

## 2026-10-23 — weekly project-update reel (changelog), 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`,
(8/12, gate PASS), `_qc/REPORT.md`, `vendor-intel-dashboards.mp4`,
`short/vendor-intel-dashboards-short.mp4`. Source: my change log (Ticket 3). (YouTube: TBD.)

**What I was working on.** A changelog reel on one ticket: splitting the reviewer and
viewer dashboards. The reviewer "approve" panel was bolted onto the public search page,
so anyone browsing briefs could also approve them; I moved it to its own
`frontend/review.html` (366 lines) and slimmed `frontend/index.html` from 1,131 to 983.

**What I tried, and what I expected.**
* By now the build is routine, and disk had recovered to ~7 GB, so I expected an
  uneventful render — and got one. The friction this week was in the *ticket*, not the reel.

**Where it resisted, and what I did next.**
* Two silent failures, found in the same corner of the code. First: there was no line
  between *viewing* a brief and *approving* one — same page, same buttons — so approval,
  a privilege, was one click away for any visitor. Split the pages.
* Second, found in passing: the reviewer box was labelled "notes / corrected brief" but
  the code only ever sent `notes`. So anyone who carefully rewrote a brief had their
  correction filed as a note, and the API's whole corrected-brief feature was
  unreachable. A field that looked like it worked, did nothing, with no error. Separated
  the fields; `brief` is now sent only when it actually changed.

**What Claude contributed, and what I did with it.**
* Mine: the change log (the files, the line counts, the bug), the neutral framing.
* Claude's: built the reel under DOUBLE-CHECK; ran PROOF (8/12), flagging B03 (the silent
  correction) as the strongest, most transferable beat.

**What I understand now, and what I still do not.**
* Understood: two shapes of the same silent-failure lesson — a privilege exposed on the
  wrong page, and a form field that's collected but never sent. Both look fine until they
  bite, and neither throws an error .