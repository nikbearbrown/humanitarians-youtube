# BUILD-LOG — claude-tag-plugins--claude-liam-snowflake-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-snowflake-api/beat_sheet.json`
— a Teardown-register "skill-teardown" sheet (metadata `register:
"Teardown"`, `brand: "claude-liam"`, `audience: "Claude"`, `source_skill`
pointing at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/snowflake/skills/snowflake-api/SKILL.md`,
which does not exist on this machine). Unlike the `redshift-api` sibling
redo (a richly detailed source), this source is a **thin batch build**: its
7 beats (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro) each restate the same generic SKILL.md
frontmatter description — "Run SQL against Snowflake — submit statements,
poll async handles, fetch result partitions, cancel, and browse
warehouses/databases/schemas/tables" — rather than adding distinct
technical detail per beat; B03's `SkillTeardownMechanism.body` is even
visibly truncated mid-sentence ("fetch result partitions, cancel, ."). Same
defect class as the `clearance` sibling logged earlier in HAILOOP-LOG:
rather than inventing specifics (endpoint paths, header names, exact
terminal-state strings) the source never confirms, this build reconstructed
a generic, defensible account using only the one concrete fact the
source's description **does** establish — submitting SQL is asynchronous;
the response is a handle to poll later, not the answer — and stated
nothing beyond it. QUESTION.md and CARRY-OUT.md both log this disposition.

All 7 source beats were already REMOTION, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00; no beat in
either version was ever AI-VIDEO, pantry, or a human-drop slot. Kept the
source's 7-beat shape → 7 beats here too (B00 writer → B01 stakes/wrong-
guess falsified → B02 mechanism/anchor planted → B03 anchor payoff/both
directions → BCRY carry-out → BHTF handoff → BOUT outro), matching the
`redshift-api` sibling's compression pattern: the source's B01
anatomy/B02 pipeline/B03 design-tell beats collapsed into three fresh
GRAPHIC (Manim) beats built around the Plain-register spine instead of
reusing the source's bespoke `SkillTeardownAnatomy`/`SkillTeardownPipeline`/
`SkillTeardownMechanism` Remotion components (which, unlike redshift-api's
already-filled equivalents, carried only the generic template text here,
so reuse would have carried the defect forward).

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "answer" → "handle" — the naive
assumption that submitting SQL to Snowflake returns rows directly,
corrected to the fact that the first response is a statement handle to
check later). Register re-registered Teardown → Plain: the source's BVDT
framed the same facts as "what it gets right" / "what it bites" — Teardown
trade-off language — restated here as mechanism + documented-boundary facts
with no verdict on the skill's design quality. Source's BVDT verdict recap
folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Anchor:
B02 → B03, the "what tables are in this schema" query (lifted directly
from the source's own description) — submitted for its handle, then paid
off against terminal-state-isn't-proof and the "fetch every partition"
rule.

Built end to end this invocation:

1. Gate L (`./art scenes --check`) — confirmed `BrutalistHesitantWriter`,
   `WantQuote`, `ClaudeComposerAsk`, `OutroCTA` all RENDERABLE before
   authoring any beat.
2. GATE T (`type_check.py`) — PASS before any audio/render spend.
3. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Measured
   durations: B00 10.33s, B01 20.78s, B02 18.50s, B03 30.31s, BCRY 15.66s,
   BHTF 17.71s, BOUT 3.65s.
4. Wrote `scenes.py` (3 Manim scenes, reel-unique names `SFB01Scene`/
   `SFB02Scene`/`SFB03Scene` to avoid the naming-collision lesson logged in
   sibling hai-simple BUILD-LOGs) and `render_scenes.py`; rendered all
   three in the foreground — no failures on first pass.
5. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`, in the foreground,
   blocked on to completion (no background/orphan risk per the one-shot-
   invocation law) — all 4 beats completed, exit 0.

Verified directly, not assumed, before compiling:

- Pulled a frame at t=9.5s in the raw `media/B00.mp4` (measured 10.33s):
  the correction ("answer" → "handle") is fully visible and the writer
  finishes the complete corrected question with the cursor resting at the
  end — WRITER LAW ("end ON the question") and TIMING LAW (≥8s floor)
  both satisfied.

Compiled directly (`compile.py`, no `--force` needed — first compile):
`claude-tag-plugins--claude-liam-snowflake-api.mp4`, 7/7 real (no slate),
117.96s, 3840×2160 (THE 4K LAW forces a clean master to 4K automatically).
B01 stretched 1.66x, B02 1.79x, B03 2.27x to fill their narration windows.

**Gate V (visual):** pulled 15 frames at 8s intervals across the full
117.96s runtime and read every one directly. B00's naive question and its
"answer"→"handle" correction read cleanly. B01's "submit returns a handle,
not rows" split (identical handle for clean SQL and typo'd SQL, only the
typo'd one later flipping to FAILED on poll) reads cleanly. B02's THE
ANCHOR (warehouse chosen from the browsable WAREHOUSES/DATABASES/SCHEMAS/
TABLES list, the "what tables are in this schema" query submitted,
returning a single handle) reads cleanly. B03's THE ANCHOR RETURNS (same
handle polled to FINISHED/partitioned vs. FAILED, RUNNING-mid-poll flagged
as not stuck with a CANCEL option, then the "fetch every partition" card)
reads cleanly. BCRY's carry-out card, BHTF's Your Turn composer card (the
real "list the tables in a schema" prompt, with the three watch-fors), and
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
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.7 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 117.96s;
  mp4 mtime (1788227454) newer than beat_sheet.json mtime (1788227351)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-snowflake-api.md`
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
cp claude-tag-plugins--claude-liam-snowflake-api.mp4 \
   claude-tag-plugins--claude-liam-snowflake-api-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/claude-tag-plugins--claude-liam-snowflake-api/` (4K
master + description) and committed + pushed the text artifacts
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/claude-tag-plugins--claude-liam-snowflake-api/` in the
humanitarians-youtube clone: commit `bbfafa41`, pushed clean (`git status
--short` empty after).

**Status: DELIVERED.**
