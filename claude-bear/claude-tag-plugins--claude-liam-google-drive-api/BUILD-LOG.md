# BUILD-LOG — claude-tag-plugins--claude-liam-google-drive-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-google-drive-api/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the Google Drive API Claude Tag
Plugin skill). 7 beats: B00 cold open (ClaudeComposerAsk, reading the
skill's own summary aloud), B01 anatomy (GoogleDriveApiAnatomy Remotion),
B02 design (GoogleDriveApiDesign Remotion), B05 teardown tell
(GoogleDriveApiTell Remotion), BVDT verdict (ClaudeVerdictArtifact), BHTF
handoff, BOUT outro — all already REMOTION, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00; no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot. Also
read `PEDAGOGY.md` in the source dir (VERDICT: PASS) for the skill's own
teachable-points summary, which confirmed the four-fact ordering (two
hosts, everything-is-a-file, fields=/nextPageToken, shared drive) as the
right entry point.

Facts carried over unchanged: Drive REST API v3 across two base hosts
(metadata/search vs. upload); everything is a file — a folder is a file
whose mimeType says so, hierarchy via `parents[]`, no path API, no
"get folder contents" endpoint; Workspace files (Docs/Sheets/Slides) have
no downloadable bytes — `alt=media` returns 403 `fileNotDownloadable`,
must use export instead; binary files download directly via `alt=media`;
`fields=` omits `nextPageToken` by default — pagination silently
truncates at one page unless it's explicitly requested; shared drive files
are invisible unless `supportsAllDrives=true` is set on every request,
plus `corpora=allDrives` and `includeItemsFromAllDrives=true` on
list/search calls — missing it returns 404, not a parameter error; two
bundled scripts, `drive_search.sh` (q-expression, pagination, all-drives)
and `drive_read.sh` (branches on mimeType: export vs. download, guards
large binaries).

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw capability list aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "path" → "ID" — the naive
assumption that Claude finds a Drive file by walking a folder path like a
normal filesystem, corrected to the fact that Drive has no path API and
resolves everything by file ID through the `parents` array). Register
re-registered Teardown → Plain: the source's B05 framed the same facts as
"what it gets right" / "where it bites" — Teardown trade-off language —
restated here as mechanism + documented-boundary facts with no verdict on
the skill's design quality. Source's BVDT verdict recap folded into a
dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition as the
`asana-api` redo precedent in this loop, which used the identical 7-beat
shape). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Anchor: B02 → B03, the "spreadsheets modified this month on our
shared drive, exported as CSV" request, traced through the three
shared-drive parameters and `fields=nextPageToken`, then paid off against
export-vs-`alt=media` — a WRONG-GUESS LAW candidate the source's own BHTF
already gestured at (an equivalent handoff prompt) but never dramatized as
its own anchor beat with a payoff.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   12.14s, B01 15.23s, B02 18.13s, B03 25.96s, BCRY 10.92s, BHTF 19.05s,
   BOUT 3.88s.
2. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `GDB01Scene`/`GDB02Scene`/`GDB03Scene` per the naming-collision lesson
   documented in sibling hai-simple BUILD-LOGs) and `render_scenes.py`;
   rendered all three in the foreground.
3. Rendered BCRY/BHTF/BOUT via `remotion_scenes.py` in one foreground
   invocation that exceeded the tool's 120s window and was moved to a
   background task by the harness — blocked on it directly with
   `TaskOutput` rather than ending the turn, per the ONE-SHOT/COMPLETION
   LAW. That same invocation reported `B00: FAIL: BrutalistHesitantWriter`
   with only a generic Remotion-package-version-mismatch warning in the
   captured stderr tail (the actual error was truncated by the script's
   800-char stderr cap). Reproduced the exact same render standalone via
   `npx remotion render` outside the batch and it succeeded cleanly
   (3840x2160, 20s) — the failure was transient (likely a resource/Chrome
   contention artifact of rendering four compositions back to back), not
   a defect in the props or component. Re-ran
   `remotion_scenes.py --only B00 --force` as its own foreground/backgrounded-
   and-blocked-on invocation; it succeeded (extended to 12.1s). All 7
   beats had media before compiling.

**One real defect found and fixed by direct frame inspection, not by
trusting a default prop set:**

- **B02 (`GDB02Scene`) chip text overflow/collision.** First render's
  `includeItemsFromAllDrives=true` parameter chip used a fixed 4.0-unit
  box width shared across all three shared-drive parameter chips; that
  string (31 characters) rendered wider than its box at font_size 16,
  overflowing both edges — on the left, into the neighboring "shared
  drive" box's border (visible on direct frame inspection at t=6s and
  t=8s into the beat, text and box outline visibly overlapping). The
  `fields= ... nextPageToken` chip had the same defect at both edges. GATE
  T's pixel checks did not flag it (same defect class as the `asana-api`
  sibling's italic-kerning bug and the `action-creator` sibling's
  synthetic-italic bug — a missing/colliding word boundary isn't a
  glyph-overlap the pixel check's threshold catches). Root cause: fixed
  chip width sized for the shortest string in the group, not the longest.
  Fixed by measuring each `Text()` mobject's rendered width first and
  sizing its chip to `text.width + 0.5`, with all three chips left-aligned
  at a fixed x=0.4 (clear of the shared-drive box's right edge at
  x≈-1.9) instead of center-aligned at a shared x. Re-rendered B02;
  frames at t=8s and t=10s now show all three parameter chips and the
  fields= chip fully containing their text with no overlap into the
  shared-drive box or each other.

Recompiled after the fix (`compile.py --force`):
`claude-tag-plugins--claude-liam-google-drive-api.mp4`, 7/7 real (no
slate), 106.3s, 3840×2160 (THE 4K LAW — clean master forced to 4K
automatically).

**Gate V (visual):** pulled frames at 7s intervals across the full 106.3s
runtime plus targeted re-checks at the B00 correction point and the B02
fix points, and read them directly. B00's correction ("path" struck in
terracotta, replaced by "ID") lands by t≈6s and the finished question
holds cleanly to the end of its 12.1s window. B01's "GET
/folders/{id}/contents" guess struck through and the real
parents-containment query read cleanly. B02's THE ANCHOR (the shared-drive
export request, all three parameters, and the fields=/nextPageToken flag)
reads cleanly after the chip-width fix. B03's THE ANCHOR RETURNS (complete
pagination vs. the two silent failures — 403 on alt=media, 404 on missing
supportsAllDrives) reads cleanly. BCRY's carry-out card, BHTF's Your Turn
composer card (the real shared-drive spreadsheet-export prompt, with the
three watch-fors), and BOUT's outro/subscribe card render legibly with
safe inset respected. **Noted, not a defect introduced here:** `OutroCTA`
renders on a flat-white ground (`VOX.CREAM = #FFFFFF` in `tokens/vox.ts`)
rather than the humanitarians cream (`#F3EBDD`) — same shared-component
behavior already logged unremarked in sibling hai-simple reels (e.g.
`asana-api`); out of this reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect,
  independently re-verified), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 106.317s;
  mp4 mtime (1788206973) newer than beat_sheet.json mtime (1788206617)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-google-drive-api.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-tag-plugins` matches no prefix in the map, so resolution fell
through to the `hai-simple` skill prefix, which maps to "Claude Basics" —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-31 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-tag-plugins--claude-liam-google-drive-api.mp4 \
   claude-tag-plugins--claude-liam-google-drive-api-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
