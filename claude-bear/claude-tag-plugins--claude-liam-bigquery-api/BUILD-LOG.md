# BUILD-LOG — claude-tag-plugins--claude-liam-bigquery-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-bigquery-api/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the BigQuery API Claude Tag Plugin
skill). 7 beats: B00 cold open (ClaudeComposerAsk, reading the skill's own
capability summary aloud), B01 job model/two execution modes
(BigQueryApiAnatomy Remotion), B02 eight operations (BigQueryApiOps
Remotion), B05 teardown tell (BigQueryApiTell Remotion), BVDT verdict
(ClaudeVerdictArtifact), BHTF handoff, BOUT outro — all already REMOTION,
so NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW
swap at B00; no beat in the source planned as `ai-video-prompt`, pantry, or
a human-drop slot.

Facts carried over unchanged: every BigQuery query runs as a job in a
billing project (the project charged for bytes scanned is not necessarily
where the data lives); every job gets an ID and is pinned to a location;
two execution modes — synchronous (`jobs.query`, blocks to a timeout, rows
inline) vs asynchronous (`jobs.insert` → poll `jobs.get` → page with
`getQueryResults`); the critical invariant that a `DONE` job can still have
failed (`status.errorResult` must be checked before trusting rows);
location must be passed on every subsequent call or it 404s; eight core
operations with the bundled `bq_query.sh` script driving both modes,
polling, pagination, and f/v decoding; the documented pagination
field-name split (`nextPageToken` on list endpoints vs `pageToken` on
query results) carried forward as the one exception fact.

Given this reel's beat count (7, matching the source exactly per the
redo-mode "keep beat count" rule), the body beats compress the source's
three Teardown beats (B01 anatomy, B02 eight operations, B05 teardown
tell) into three GRAPHIC beats (B01, B02, B03) built fresh in Manim rather
than reusing the source's bespoke Remotion components — one idea per beat,
following hai-simple's Plain-register spine (stakes → wrong guess,
falsified → mechanism / anchor planted → anchor payoff / both directions)
instead of the source's anatomy/ops/tell structure. The eight-operations
enumeration and the write-heavy-ops/auth-placeholder/nested-f-v gaps from
the source's B02/B05 were deliberately compressed rather than carried in
full — QUESTION.md and CARRY-OUT.md both log this as "not a claim that
location and the error check are the only rules," matching the same
disposition as the `asana-api` sibling redo in this loop.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw capability list aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "call" → "job" — the naive
assumption that a BigQuery query is one instant API call, corrected to the
fact that it's a tracked job). Register re-registered Teardown → Plain:
the source's B05 framed the same facts as "what it gets right" / "where it
bites" — Teardown trade-off language — restated here as mechanism +
documented-boundary facts with no verdict on the skill's design quality.
Source's BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW. Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Anchor: B02 → B03, the "top 10 names, California" job
traced through billing-project-pays + location-pinning, then paid off
against DONE-but-failed and the pagination field-name split.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.75s, B01 16.73s, B02 18.71s, B03 26.20s, BCRY 12.84s, BHTF 22.21s,
   BOUT 3.67s.
2. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `BQB01Scene`/`BQB02Scene`/`BQB03Scene` per the naming-collision lesson
   documented in sibling hai-simple BUILD-LOGs) and `render_scenes.py`;
   rendered all three in the foreground — no failures on first pass.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the tool's 120s window and was moved to a background task by
   the harness; blocked on it directly with `TaskOutput` rather than
   ending the turn, per the one-shot-invocation law — all 4 beats
   completed, exit 0. B00 (BrutalistHesitantWriter) extended to 11.8s by
   the compile step to fill the narration window.

No defects found on first-pass frame inspection — verified directly, not
assumed:

- B00's typed text ("Claude must just make one API call and hand back my
  rows. Is that it?") was checked at t=10.5s in the rendered clip before
  compiling into the master: the correction ("call" → "job") is fully
  visible and the writer finishes the complete corrected question with
  the cursor resting at the end, satisfying WRITER LAW ("end ON the
  question") and TIMING LAW (media/B00.mp4 measured 11.77s, well above
  the 8s floor).
- B03's Manim clip (12.0s native) was slowed 2.18x by the compile step to
  fill its 26.2s narration window — the largest stretch factor of the
  three GRAPHIC beats. Checked directly on frame pulls at 6s intervals
  through the beat: the held cards (DONE/no-error, DONE/errorResult, the
  pagination-split exception card) read as deliberate, legible pauses,
  not sluggish drift — the scene's own `self.wait()` calls already
  carried most of the beat's runtime, so the stretch elongates holds
  rather than visibly slowing motion.

Compiled directly (`compile.py`, no `--force` needed — first compile):
`claude-tag-plugins--claude-liam-bigquery-api.mp4`, 7/7 real (no slate),
113.1s, 3840×2160 (THE 4K LAW — clean master forced to 4K automatically).

**Gate V (visual):** pulled frames at 6s intervals across the full 113.1s
runtime plus a targeted late-frame check on B00, and read them directly.
B00's naive question and its "call"→"job" correction read cleanly, ending
on the complete corrected question. B01's sync-vs-async split (one
blocking request vs. a job card with an ID) reads cleanly. B02's THE
ANCHOR (billing-project/location-pinning on the "top 10 names · California"
job) reads cleanly, including the "every follow-up call carries it" note.
B03's THE ANCHOR RETURNS (DONE/no-error vs. DONE/errorResult "looks
finished", plus the `nextPageToken`/`pageToken` exception card) reads
cleanly. BCRY's carry-out card, BHTF's Your Turn composer card (the real
Texas top-5-names prompt, with the three watch-fors), and BOUT's
outro/subscribe card render legibly with safe inset respected. **Noted,
not a defect introduced here:** `OutroCTA` renders on a flat-white ground
(`VOX.CREAM = #FFFFFF` in `tokens/vox.ts`) rather than the humanitarians
cream (`#F3EBDD`) — same shared-component behavior already logged
unremarked in sibling hai-simple reels (e.g. `asana-api`); out of this
reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 113.1s;
  mp4 mtime (1788194110) newer than beat_sheet.json mtime (1788194005)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-bigquery-api.md`
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
render, copied to the `-4k` filename `deliver.py` expects.
