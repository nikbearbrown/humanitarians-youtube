# BUILD-LOG — claude-tag-plugins--claude-liam-redshift-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-redshift-api/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the redshift-api Claude Tag Plugin
skill). 7 beats: B00 cold open (ClaudeComposerAsk, reading the skill's
three governing rules aloud), B01 anatomy (request setup + six
operations), B02 design (workflow/key patterns), B05 teardown tell, BVDT
verdict (ClaudeVerdictArtifact), BHTF handoff, BOUT outro — all already
REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution beyond the
WRITER LAW swap at B00; no beat in the source planned as `ai-video-prompt`,
pantry, or a human-drop slot.

Facts carried over unchanged: every call is a POST to
`redshift-data.<region>.amazonaws.com/`, header `X-Amz-Target:
RedshiftData.<Action>`, no REST paths; the API is fully asynchronous —
`ExecuteStatement` submits and returns an `Id`, `DescribeStatement` is
polled to a terminal state, `GetStatementResult` pages on `NextToken`; the
critical invariant that `ExecuteStatement` returning 200 does not mean the
SQL succeeded (a bad query is still accepted, and the failure only shows up
as `Status: FAILED` on a later `DescribeStatement` poll); request setup
needs a region plus one `RS_TARGET` shape (`WorkgroupName`,
`ClusterIdentifier`+`DbUser`, or `SecretArn`); six operations (run via
`rs_query.sh`, resume by `Id`, cancel, `BatchExecuteStatement` with
separately-fetched sub-statement IDs, `ListStatements`, catalog browsing
capped at 3 TPS); typed cell decoding via `to_entries[0].value` rather than
a naive `.value`; and the documented gap that `ExecuteStatement` is not
idempotent without `ClientToken`.

Given this reel's beat count (7, matching the source exactly per the
redo-mode "keep beat count" rule), the body beats compress the source's
three Teardown beats (B01 anatomy, B02 design, B05 teardown tell) into
three GRAPHIC beats (B01, B02, B03) built fresh in Manim rather than reusing
the source's bespoke Remotion components — one idea per beat, following
hai-simple's Plain-register spine (stakes → wrong guess, falsified →
mechanism / anchor planted → anchor payoff / both directions) instead of
the source's anatomy/design/tell structure. The full six-operation
enumeration, the three-connection-target detail beyond the chosen
workgroup, and the source's B05 gaps (idempotency, 24h result retention,
size limits) were deliberately compressed rather than carried in full —
QUESTION.md and CARRY-OUT.md both log this as "not a claim that polling and
cell decoding are the only rules," matching the same disposition as the
`bigquery-api` sibling redo in this loop.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's three governing rules aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "worked" → "began" — the naive
assumption that a 200 from `ExecuteStatement` means the query succeeded,
corrected to the fact that 200 only means the query began running).
Register re-registered Teardown → Plain: the source's B05 framed the same
facts as "what it gets right" / "where it bites" — Teardown trade-off
language — restated here as mechanism + documented-boundary facts with no
verdict on the skill's design quality. Source's BVDT verdict recap folded
into a dedicated BCRY carry-out beat per CARRY-OUT LAW. Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Anchor: B02 → B03, the
"top 20 events, past month, grouped by name" query (the same worked example
from the source's own B00/BHTF), submitted for its Id, then paid off
against FINISHED/FAILED and the cell-decode rule.

Built end to end this invocation:

1. GATE T (`type_check.py`) — PASS before any audio/render spend.
2. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.26s, B01 18.77s, B02 21.23s, B03 31.08s, BCRY 17.77s, BHTF 23.68s,
   BOUT 3.52s.
3. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `RSB01Scene`/`RSB02Scene`/`RSB03Scene` per the naming-collision lesson
   documented in sibling hai-simple BUILD-LOGs) and `render_scenes.py`;
   rendered all three in the foreground — no failures on first pass.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the tool's 120s window and was moved to a background task by
   the harness; blocked on it directly with `TaskOutput` rather than
   ending the turn, per the one-shot-invocation law — all 4 beats
   completed, exit 0. B00 (BrutalistHesitantWriter) extended to 10.3s by
   the compile step to fill the narration window.

No defects found on first-pass frame inspection — verified directly, not
assumed:

- B00's typed text ("A 200 from Redshift means my query worked. Right?")
  was checked at t=9.0s in the rendered clip before compiling into the
  master: the correction ("worked" → "began") is fully visible and the
  writer finishes the complete corrected question with the cursor resting
  at the end, satisfying WRITER LAW ("end ON the question") and TIMING LAW
  (media/B00.mp4 measured 10.27s, well above the 8s floor).
- B03's Manim clip (13.3s native) was slowed 2.33x by the compile step to
  fill its 31.1s narration window — the largest stretch factor of the
  three GRAPHIC beats. Checked directly on frame pulls at 8s intervals
  through the beat: the held cards (FINISHED/HasResultSet, FAILED,
  STARTED-mid-poll, the `to_entries[0].value` decode card) read as
  deliberate, legible pauses, not sluggish drift.

Compiled directly (`compile.py`, no `--force` needed — first compile):
`claude-tag-plugins--claude-liam-redshift-api.mp4`, 7/7 real (no slate),
127.3s, 3840×2160 (THE 4K LAW — clean master forced to 4K automatically).

**Gate V (visual):** pulled frames at 8s intervals across the full 127.3s
runtime plus a targeted late-frame check on B00, and read them directly.
B00's naive question and its "worked"→"began" correction read cleanly,
ending on the complete corrected question. B01's "200 means accepted, not
correct" split (identical 200+Id for a clean query and a typo'd one, only
the typo'd one later flipping to FAILED on poll) reads cleanly. B02's THE
ANCHOR (region + RS_TARGET set to WorkgroupName, the "top 20 events · past
month · grouped by name" query submitted, returning a single Id) reads
cleanly. B03's THE ANCHOR RETURNS (the same Id polled to FINISHED/
HasResultSet vs. FAILED, STARTED-mid-poll flagged as not stuck, then the
`to_entries[0].value` decode card) reads cleanly. BCRY's carry-out card,
BHTF's Your Turn composer card (the real Serverless workgroup prompt, with
the three watch-fors), and BOUT's outro/subscribe card render legibly with
safe inset respected. **Noted, not a defect introduced here:** `OutroCTA`
renders on a flat-white ground (`VOX.CREAM = #FFFFFF` in `tokens/vox.ts`)
rather than the humanitarians cream (`#F3EBDD`) — same shared-component
behavior already logged unremarked in sibling hai-simple reels (e.g.
`bigquery-api`); out of this reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 127.3s;
  mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-redshift-api.md`
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
cp claude-tag-plugins--claude-liam-redshift-api.mp4 \
   claude-tag-plugins--claude-liam-redshift-api-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/claude-tag-plugins--claude-liam-redshift-api/` (4K
master + description) and committed + pushed the text artifacts
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/claude-tag-plugins--claude-liam-redshift-api/` in the
humanitarians-youtube clone: commit `7f87ea4d`, pushed clean (`git status
--short` empty after).

**Status: DELIVERED.**
