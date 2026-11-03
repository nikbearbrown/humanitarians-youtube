# BUILD-LOG — claude-tag-plugins--claude-liam-asana-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-asana-api/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the Asana API Claude Tag Plugin
skill). 7 beats: B00 cold open (ClaudeComposerAsk, read the skill's own
summary aloud), B01 anatomy (AsanaApiAnatomy Remotion), B02 ten operations
(AsanaApiOps Remotion), B05 teardown tell (AsanaApiTell Remotion), BVDT
verdict (ClaudeVerdictArtifact), BHTF handoff, BOUT outro — all already
REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution beyond the
WRITER LAW swap at B00; no beat in the source planned as `ai-video-prompt`,
pantry, or a human-drop slot.

Facts carried over unchanged: Asana API covers the REST API at
`app.asana.com/api/1.0` plus the bundled `asana_tasks.sh` script; resource
hierarchy workspace → project → section → task → story, gid all the way
down; three universal rules — gid not name, the data envelope (reads
return `{"data": …}`, writes send `{"data": {…}}`, errors replace `data`
with `errors`), and `opt_fields` for expansion; ten core operations
(list/get/create/update-complete/comment/search/projects-sections/move/
gid-lookup/subtasks-tags-attachments); the one documented gotcha carried
forward as the both-directions exception: workspace search is
premium-only, capped at 100 unstable results, no real pagination.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw capability list aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "app" → "API" — the naive assumption
that Claude operates the Asana app's UI, corrected to the fact that it
calls Asana's REST API directly). Register re-registered Teardown → Plain:
the source's B05 framed the same facts as "what it gets right" / "where it
bites" — Teardown trade-off language — restated here as mechanism +
documented-boundary facts with no verdict on the skill's design quality.
Source's BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW (same disposition as the `action-creator` redo precedent in
this loop). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Anchor: B02 → B03, the "list my incomplete tasks in Launch"
request traced through gid resolution and the data envelope, then paid off
against pagination (complete when both habits hold, silently wrong when
either is skipped) — a WRONG-GUESS LAW candidate the source's own BHTF
already gestured at ("does it project `.data` from every response — not
assume a bare array?") but never dramatized as its own beat.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   12.01s, B01 15.27s, B02 17.73s, B03 26.41s, BCRY 10.15s, BHTF 20.16s,
   BOUT 3.46s.
2. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `AAB01Scene`/`AAB02Scene`/`AAB03Scene` per the naming-collision lesson
   documented in the `action-creator`/`screenshot-prompt-caching` sibling
   BUILD-LOGs) and `render_scenes.py`; rendered all three in the
   foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The first
   invocation exceeded the tool's 120s window and was moved to a
   background task by the harness; blocked on it directly with
   `TaskOutput` rather than ending the turn, per the one-shot-invocation
   law — all 4 beats completed, exit 0.

**Two real defects found and fixed by direct frame inspection, not by
trusting a default prop set:**

- **B00 TIMING LAW violation.** First render (mistakeRate 6, hesitateWithin
  3, hesitateBetween 22, charMs 55 — the same values used successfully in
  the shorter `action-creator` precedent) never finished typing "Is that
  it?" within the beat's 12.0s audio window — the last frame froze at "my
  tasks. Is t|", mid-word. WRITER LAW requires the beat to "End ON the
  question"; a cut-off ending fails that even though the correction
  ("app"→"API") itself was already visible and legible by t≈5s. Root
  cause: this reel's B00 text is longer (77 chars vs. the precedent's ~66)
  and the same hesitation/mistake rates pushed total typing time past the
  measured narration length. Fixed by lowering mistakeRate to 3,
  hesitateWithin to 2, hesitateBetween to 10, charMs to 40, and jitter to
  22 — re-rendered, and the last frame now reads "my tasks. Is that it?|",
  the full corrected question, cursor resting at the end.
- **B02 kerning/spacing defect, not caught by GATE T.** The anchor's
  quoted request text, `"list my incomplete tasks in Launch"`, rendered
  with `slant=ITALIC` on the SERIF (EB Garamond) font, collapsed the space
  between "my" and "incomplete" into "myincomplete" — visible on direct
  frame inspection at both the 16s and 24s sample points, though GATE T's
  pixel checks did not flag it (below its kerning-gap threshold; a missing
  space isn't a glyph-touching defect the same way an overlapping glyph
  is). Same defect class as the `action-creator` sibling's synthetic-
  italic Montserrat bug — this system's EB Garamond italic path also
  mishandles at least one word-boundary advance. Fixed by dropping
  `slant=ITALIC` from that one `Text()` call (the other two italic uses in
  this reel's `scenes.py`, "Never a name — always a gid." and "\"looks
  done\"", render correctly and were left alone — the defect is specific to
  this word pair, not italic serif in general). Re-rendered B02; the quote
  now reads "list my incomplete tasks in Launch" with correct spacing.

Recompiled after both fixes (`compile.py --force`):
`claude-tag-plugins--claude-liam-asana-api.mp4`, 7/7 real (no slate),
106.2s, 3840×2160 (THE 4K LAW — clean master forced to 4K automatically).

**Gate V (visual):** pulled frames at 6–8s intervals across the full
106.2s runtime plus targeted re-checks at the B00/B02 fix points, and read
them directly. B00's correction and finished question read cleanly. B01's
struck-through bare-array guess and the opened `data` envelope (with `gid`
tags, never a name) read cleanly. B02's THE ANCHOR (workspace→project→
section→task nesting, then the traced request) reads cleanly after the
italic fix. B03's THE ANCHOR RETURNS (complete pagination vs. "looks done"
truncation, plus the search-cap exception card) reads cleanly. BCRY's
carry-out card, BHTF's Your Turn composer card (the real multi-workspace
task-listing prompt, with the three watch-fors), and BOUT's outro/subscribe
card render legibly with safe inset respected. **Noted, not a defect
introduced here:** `OutroCTA` renders on a flat-white ground (`VOX.CREAM =
#FFFFFF` in `tokens/vox.ts`) rather than the humanitarians cream
(`#F3EBDD`) — same shared-component behavior already logged unremarked in
sibling hai-simple reels; out of this reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.4 dB
- ffprobe: video 3840x2160 h264, audio aac 48kHz present, duration 106.2s;
  mp4 mtime (1788192772) newer than beat_sheet.json mtime (1788192647)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written: `claude-tag-plugins--claude-liam-asana-api.md`
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
