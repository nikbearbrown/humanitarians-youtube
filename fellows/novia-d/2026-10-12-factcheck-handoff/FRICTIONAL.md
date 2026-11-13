# Frictional Log — The Handoff

## 2026-10-11

**What I was working on:** A handoff reel from `FACTCHECK_HANDOFF.md` — what was added on top of the original prompt — so the next person can run the pipeline. Not a recut of Chapter 14 video 1 or 2. Bella / Hello Novia. Local only until I signed off.

**What I tried, and what I expected:** Sixteen-beat cream explainer: eight additions, sentence flow, status, Your Turn. Expected the status slide to match the handoff doc.

**Where it resisted, and what I did next:** First status beat still showed the old 19 / 1 bar split ("current format" vs "older format"). That was stale. I corrected Part E to 36 packages, all current format, as of 2026-10-12, and the B12 slide was rebuilt (terracotta 36, not the bars).

**What Claude contributed, what I accepted/changed/rejected:** Claude drafted the reel from the handoff doc and first compiled the landscape 4K. I accepted the spine and the cream look. I rejected the stale 19 / 1 status and the spoken "next is 8" leftover. I also held the GitHub push until I had watched it.

**What I understand now, and what I still don't:** The video is the extra system on top of the prompt, not a new fact-check of a chapter. Still open that night: the 9:16 4K cut.

Evidence in this folder: `SOURCE.md` Part E, `BUILD-LOG.md`, `scenes.py` (`B12_WhatIsDone`).

## 2026-10-12

**What I was working on:** Portrait 4K of the same cut, then source-only upload under `fellows/novia-d`.

**What I tried, and what I expected:** Same 16 beats, 2160×3840, Bella track unchanged. Source to GitHub; masters stay local.

**Where it resisted, and what I did next:** `ClaudeScienceChipGrid` and `ClaudeScienceSourceFlow` have no 916 compositions — Onda blocked B05 and B11. Those two short beats were rewritten to `ClaudeWindow916` with the same copy. Short compile then failed GATE F (no `SHOTLIST.md` in `short/`); paperwork was copied in and the 4K portrait compiled (238.1s). Full-repo clone of the YouTube tree hung; the source commit was made only on `fellows/novia-d` paths.

**What Claude contributed, what I accepted/changed/rejected:** Claude patched B05/B11, compiled both 4K masters, and opened the GitHub commit. I accepted the ClaudeWindow916 fallback and the source-only upload. I rejected uploading mp4/mp3, rejected any path outside `fellows/novia-d`, and rejected touching a professors' README.

**What I understand now, and what I still don't:** Both formats exist locally (3840×2160 and 2160×3840). Status on screen is 36 current-format packages as of 2026-10-12. This folder had no `FRICTIONAL.md` until this file — the house rule is one log per work folder, not one at the top of `novia-d`. Still open: Drive link for these two new masters, if we add one later.

Evidence in this folder: `beat_sheet.json`, `short/beat_sheet.json`, `BUILD-LOG.md`.
