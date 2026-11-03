# BUILD-LOG — knowledge-work-plugins--claude-liam-create-viz

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-create-viz/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`create-viz` Anthropic skill — the `data` plugin's chart-generation tool).
Only `SUBJECT.json` existed on pickup.

**Source-material defect found and worked around:** the source sheet's own
narration was truncated mid-thought in B03 and mid-word in BHTF — the same
class of batch-build defect the sibling reel
`knowledge-work-plugins--claude-liam-content-strategy` found and worked
around (2026-09-03, earlier this session):
- B03: `"Claude's job: Create publication-quality visualizations with
  Python. Use when turning query results or a DataFrame. What it gets
  right..."` — cuts the skill's own description short instead of finishing
  the sentence ("...into a chart, selecting the right chart type for a trend
  or comparison, generating a plot for a report or presentation, or needing
  an interactive chart with hover and zoom.").
- BHTF: `"I want to create publication-quality visualizations with python.
  use when turning query re. Read the create-viz skill..."` — breaks off
  mid-word ("re[sults]").

Its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/data/skills/create-viz/SKILL.md`)
does not exist anywhere in this local tree. Per the REDO LAW ("keep its
question, its facts, its body argument"), the missing/truncated facts could
not simply be invented. Resolved by fetching the real, public source
directly: `github.com/anthropics/knowledge-work-plugins`,
`data/skills/create-viz/SKILL.md` (confirmed via `WebSearch` to be a genuine
public Anthropic repo, then read in full via `curl`/raw.githubusercontent.com
this invocation). All facts in this reel — the chart-type-by-relationship
table, the matplotlib/seaborn-default-plotly-on-request split, the accuracy
constraints (zero-baseline bars, no hidden axis breaks, colorblind-safe
meaningful color, insight-stating titles) — are sourced from that real file,
not from the source sheet's truncated template text.

**Register re-registered Teardown -> Plain**: the source graded the skill
("What it gets right: repeatable results. What it bites: anything outside
the spec.") and framed a "Verdict" card; this redo states the accuracy
constraints as fact (no grading language) and folds the verdict into a
`WantQuote` carry-out beat. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "pretty" -> "honest" —
the newcomer assumption that this skill is about making a chart look nice,
corrected to: it's a decision procedure that keeps the chart honest before
anything gets styled). Close re-skinned to `OutroCTA` / @HumanitariansAI
with Liam's sign-off. BHTF's prompt was rewritten clean — the source's
handoff string was a broken template referencing a skill file and a
connected data warehouse the general viewer won't have; this version asks
the viewer to paste six made-up monthly numbers and ask Claude to name the
chart type and reasoning before styling, which doubles as a live test of the
reel's own claim.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so the law required no substitution beyond the WRITER
LAW and channel-skin row it already mandates.

## Built end to end this invocation

1. Read `SKILL.md` (hai-simple), `SKILL.md` (simple, parent), the source
   `beat_sheet.json` + `PEDAGOGY.md`/`LENS-AUDIT.md`, and the structure-
   template sheet (`claude-liam-simple-delve`). Also read the sibling redo
   `knowledge-work-plugins--claude-liam-content-strategy` (same family,
   already DONE) as a concrete precedent for exactly this defect class and
   the file layout (`scenes.py`, `render_scenes.py`, `<slug>.md` format).
   Discovered the source's truncated narration and missing local
   `source_skill` path; re-sourced real facts from the public
   `anthropics/knowledge-work-plugins` GitHub repo (WebSearch to confirm
   genuine, then fetched the raw SKILL.md via curl).
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Plain
   register: carry-out written first, then the reel reverse-engineered to
   land it). Wrong guess: "create a visualization" means making an existing
   chart idea look nicer. Correction: it picks the chart type from the
   data's relationship first, then enforces accuracy rules that can't be
   styled away.
3. Wrote `SCRIPT.md` (7-beat table, redo audit, register audit, deliberately
   -not-claimed section) and `beat_sheet.json`, matching the source's exact
   7-beat count (B00, B01, B02, B03, BVDT->BCRY, BHTF, BOUT). GATE L checked
   all four reused Remotion components before slating — `BrutalistHesitantWriter`,
   `ClaudeComposerAsk`, `WantQuote`, `OutroCTA` all RENDERABLE with matching
   props (`./art scenes --check`).
4. Generated audio: `generate_audio_kokoro.py`, free, `am_onyx`, cost $0.00.
   Measured durations: B00 11.43s, B01 16.45s, B02 17.39s, B03 17.30s, BCRY
   9.79s, BHTF 12.05s, BOUT 4.12s.
5. Wrote `scenes.py` / `render_scenes.py` for the three GRAPHIC beats (B01
   anatomy — folder + SKILL.md/reference contents; B02 mechanism — a
   relationship-to-chart-type table filling in row by row; B03 constraint —
   a bar chart snapping to a zero baseline, a colorblind-safe swatch row,
   and a title swap from a metric name to a stated finding), Manim,
   humanitarians palette, durations matched to measured audio. Rendered all
   three in the foreground — clean on first pass.
6. Rendered the four REMOTION beats via `remotion_scenes.py` (foreground).
   The render exceeded the tool's inline timeout and the harness moved it to
   a tracked background task; per the COMPLETION LAW (never end a turn on an
   unsupervised render), blocked on it directly via `TaskOutput(block=true)`
   until the task-completion notification confirmed exit code 0 — 3/4 beats
   rendered clean (B00, BCRY, BOUT); BHTF (`ClaudeComposerAsk`) failed with a
   transient Remotion package-version-mismatch warning during that run.
   Retried BHTF alone (`--only BHTF --force`), again blocked on the
   background task directly — succeeded clean on retry, 12.1s. Verified
   `media/B00.mp4` directly: `ffprobe` confirms 11.43s with audio+video
   tracks, clearing the >=8s TIMING LAW floor; a frame pull at t=10.5s shows
   the correction complete and legible — "Claude, make my chart honest."
7. First `compile.py` pass -> 7/7 real (no slate), native 4K master, 89.5s,
   mean_volume -23.9 dB.
8. GATE T (`type_check.py`): **FAIL** on first run — B02's smallest text run
   measured 18px, below the 20px floor (1.9% of 1080px logical). Root cause:
   Unicode arrow glyphs ("→") rendered as `Text(...)` mobjects in B02Scene
   and B03Scene produce thin blobs whose bounding-box height falls under the
   floor even at a readable font size, because the glyph itself is
   structurally short (a horizontal line + small arrowhead), not because the
   font size was too small. **Fix:** replaced both Unicode-arrow `Text`
   mobjects with proper geometric `Arrow` mobjects (vector shapes, not
   typography — exempt from §8.1 by construction) in `scenes.py`, re-rendered
   B02 and B03, recompiled. Re-ran `type_check.py`: **GATE T PASS**, 0 FAILs.
9. Gate V: pulled a 6-second frame sweep across the full 89.5s master (15
   frames spanning all 7 beats) and read each directly. All clean — B00's
   hesitation/correction arc reads clearly, B01's folder anatomy is legible,
   B02's relationship table and B03's accuracy table both show clean
   geometric arrows with no clipping, BCRY/BHTF/BOUT all legible. One
   pre-existing, non-blocking cosmetic note: `OutroCTA` renders on flat
   white rather than the humanitarians cream ground — a known shared-
   component quirk already logged unfixed on multiple siblings in this
   factory (e.g. `knowledge-work-plugins--claude-liam-content-strategy`);
   not a new defect.
10. Final master verified directly: 3840x2160 (born natively via
    compile.py's 4K LAW), 89.5s, mean_volume -23.9 dB (max -3.4 dB), mtime
    (1788436642) newer than `beat_sheet.json` (1788436360) — the COMPLETION
    LAW conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 35 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.43s**, clears the >=8s floor. The
  correction ("pretty"->"honest") is visible and settled on-screen by
  t=10.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** FAIL -> fixed (B02 min-size, arrow glyphs ->
  geometric Arrow mobjects) -> PASS, 0 FAILs on re-run.
- **Gate V (frame QC):** full 15-frame sweep across all 7 beats, all read
  directly. One defect found and fixed pre-sweep (via GATE T); clean on the
  sweep that followed the fix.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was
needed — copied directly to
`knowledge-work-plugins--claude-liam-create-viz-4k.mp4`. `deliver.py --push`
staged `DELIVERY/knowledge-work-plugins--claude-liam-create-viz/` (4K master
+ description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-create-viz/` (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md — no media) to `humanitarians-youtube`, clean, no conflicts.
`HAILOOP-LOG.md` updated with the matching entry.
