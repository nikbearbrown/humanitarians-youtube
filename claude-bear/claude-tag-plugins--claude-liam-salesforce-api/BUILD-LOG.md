# BUILD-LOG — claude-tag-plugins--claude-liam-salesforce-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-salesforce-api/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the salesforce-api Claude Tag Plugin
skill). 7 beats: B00 cold open (ClaudeComposerAsk, reading the skill's
four governing rules aloud), B01 anatomy (request setup + seven
operations), B02 design (workflow/key patterns), B05 teardown tell, BVDT
verdict (ClaudeVerdictArtifact), BHTF handoff, BOUT outro — all already
REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution beyond the
WRITER LAW swap at B00; no beat in the source planned as `ai-video-prompt`,
pantry, or a human-drop slot.

Facts carried over unchanged: every call needs the org's own instance URL
(My Domain) plus the versioned data path; success and error responses have
different shapes — success is a JSON object (or, for PATCH/DELETE, 204 No
Content with an empty body), errors are always a JSON array with an
errorCode; SOQL has no `SELECT *` (`FIELDS(ALL)`/`FIELDS(CUSTOM)` need
`LIMIT 200`); Describe is the schema (field names, picklist values,
createable/updateable flags, `__c`/`__r` naming); seven operations
(SOQL via `sf_query.sh` paging `nextRecordsUrl`, SOSL needing `-G`, CRUD,
upsert by external ID with 201/200/300, Describe, Composite with `@{}`
cross-refs and `allOrNone`, Limits); the critical invariant that Composite's
outer 200 does not mean every subrequest succeeded (check each
`httpStatusCode`); and the documented gap that composite subrequest URLs
must repeat the outer request's API version.

Given this reel's beat count (7, matching the source exactly per the
redo-mode "keep beat count" rule), the body beats compress the source's
three Teardown beats (B01 anatomy, B02 design, B05 teardown tell) into
three GRAPHIC beats (B01, B02, B03) built fresh in Manim rather than reusing
the source's bespoke Remotion components — one idea per beat, following
hai-simple's Plain-register spine (stakes → wrong guess, falsified →
mechanism / anchor planted → anchor payoff / both directions) instead of
the source's anatomy/design/tell structure, same disposition as the
`redshift-api`/`bigquery-api` siblings in this loop. The full seven-operation
enumeration, SOQL's `FIELDS()`/`LIMIT 200` rule, SOSL's `-G` requirement,
and the external-ID upsert codes were deliberately compressed rather than
carried in full — QUESTION.md and CARRY-OUT.md both log this as "not a
claim that status codes are the only rule."

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's four governing rules aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "failed" → "worked" — the naive
assumption that an empty PATCH response means the write failed, corrected
to the fact that 204 No Content with no body is the success state).
Register re-registered Teardown → Plain: the source's B05 framed the same
facts as "what it gets right" / "where it bites" — Teardown trade-off
language — restated here as mechanism + documented-boundary facts with no
verdict on the skill's design quality. Source's BVDT verdict recap folded
into a dedicated BCRY carry-out beat per CARRY-OUT LAW. Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Anchor: B02 → B03, the
"open Opportunities closing this quarter, with Account name and owner"
query (the same worked example from the source's own B00/BHTF), pulling
an Id, then PATCHed to Closed Won and paid off against the 204 success
state plus the Composite both-directions caveat.

Built end to end this invocation:

1. GATE T (`type_check.py`) — PASS before any audio/render spend (all 7
   beats SKIP on §8.10 pixel-check pre-render, as expected with no media
   yet).
2. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.86s, B01 18.56s, B02 20.22s, B03 28.44s, BCRY 13.74s, BHTF 27.46s,
   BOUT 3.73s.
3. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `SFB01Scene`/`SFB02Scene`/`SFB03Scene` per the naming-collision lesson
   documented in sibling hai-simple BUILD-LOGs) and `render_scenes.py`;
   rendered all three in the foreground — no failures on first pass.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the tool's 120s foreground window and was moved to a
   background task by the harness; blocked on it directly with
   `TaskOutput` rather than ending the turn, per the one-shot-invocation
   law — all 4 beats completed, exit 0. B00 (BrutalistHesitantWriter)
   extended to 11.9s by the compile step to fill the narration window.

No defects found on first-pass frame inspection — verified directly, not
assumed:

- B00's typed text ("An empty response from Salesforce means my update
  failed.") was checked at t≈9.5s in the rendered clip before compiling
  into the master: the correction ("failed" → "worked") is fully visible
  and the writer finishes the complete corrected question with the cursor
  resting at the end, satisfying WRITER LAW ("end ON the question") and
  TIMING LAW (media/B00.mp4 measured 11.87s, well above the 8s floor).
- B03's Manim clip (11.8s native) was slowed 2.42x by the compile step to
  fill its 28.4s narration window — the largest stretch factor of the
  three GRAPHIC beats. Checked directly on frame pulls at 8s intervals
  through the beat: the held cards (the anchor's 204/empty resolution,
  the outer:200/sub1:204/sub2:200/sub3:400 Composite grid, the
  `allOrNone: false` note) read as deliberate, legible pauses, not
  sluggish drift.

Compiled directly (`compile.py`, no `--force` needed — first compile):
`claude-tag-plugins--claude-liam-salesforce-api.mp4`, 7/7 real (no slate),
125.0s, 3840×2160 (THE 4K LAW — clean master forced to 4K automatically).

**Gate V (visual):** pulled frames at 8s intervals across the full 125.0s
runtime plus a targeted late-frame check on B00, and read them directly.
B00's naive question and its "failed"→"worked" correction read cleanly,
ending on the complete corrected question. B01's "silent success, loud
failure" split (a clean PATCH resolving 204/empty beside a bad-field PATCH
resolving a JSON array with an errorCode, flagged terracotta) reads
cleanly. B02's THE ANCHOR (instance URL + Describe confirming StageName
updateable/Closed Won valid, then the SOQL query returning a single Id)
reads cleanly. B03's THE ANCHOR RETURNS (the same Id's PATCH resolving
204, then the Composite batch — outer 200, three subrequests each with
their own status, one flagged terracotta, `allOrNone: false` note) reads
cleanly. BCRY's carry-out card, BHTF's Your Turn composer card (the real
Opportunities-to-Closed-Won prompt, with the three watch-fors), and
BOUT's outro/subscribe card render legibly with safe inset respected.
**Noted, not a defect introduced here:** `OutroCTA` renders on a flat-white
ground (`VOX.CREAM = #FFFFFF` in `tokens/vox.ts`) rather than the
humanitarians cream (`#F3EBDD`) — same shared-component behavior already
logged unremarked in sibling hai-simple reels (e.g. `redshift-api`,
`bigquery-api`); out of this reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (independently re-verified
  via `ffmpeg volumedetect`, not just compile.py's own report), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 125.0s;
  mp4 mtime (1788224542) newer than beat_sheet.json mtime (1788224427)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-salesforce-api.md`
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
cp claude-tag-plugins--claude-liam-salesforce-api.mp4 \
   claude-tag-plugins--claude-liam-salesforce-api-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
