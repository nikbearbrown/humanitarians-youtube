# BUILD-LOG — claude-quickstarts--feature-list-checkpoint-persistence

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-quickstarts/youtube/feature-list-checkpoint-persistence/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel examining the checkpoint-and-resume
pattern in `autonomous-coding/autonomous_agent_demo.py`). Question ("Persisting
Progress Across Context Windows."), facts (a context window empties completely
between sessions; `feature_list.json` is the external source of truth — 200 entries,
each with an id and a status of incomplete/passing; git is the immutable per-feature
ledger; each session reads the file, finds the first incomplete entry, implements it,
tests it, commits, marks it passing; scope excludes how the list is generated and what
the test framework does), and the 8-beat count (B00–B07 in the source) carried over
unchanged. B00 replaced `ClaudeComposerAsk` with `BrutalistHesitantWriter` (WRITER
LAW). Register re-registered Teardown→Plain: the source's B05 (`ClaudeVerdictArtifact`)
framed its four-line recap as "what the body demonstrated" — that verdict-card framing
was removed; the rebuilt BCRY states the same mechanism as a single carry-out sentence.
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt
kept functionally identical to the source's (already a genuine, generic, runnable ask).
No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the source was
already all-Remotion (`ClaudeComposerAsk` × 2, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`, plus B01–B04 as `ClaudeComposerAsk` command cards) — so
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW itself. Body
beats B01–B04 rebuilt as GRAPHIC (Manim) in the humanitarians palette instead of the
source's fixed Claude-palette command cards, matching established channel-skin
practice (`claude-quickstarts--claude-liam-first-run`). The source's three
empty-narration `BOOKEND`-lane beats (`BVDT`, `BHTF`, `BOUT`) were leftover template
scaffold never part of the rendered 8-beat sequence (source `build.filled`/`of` counts
only B00–B07) and were not carried into this redo — this reel's own `BCRY`/`BHTF`/
`BOUT` are authored fresh per the hai-simple spine.

Built from scratch this invocation (SUBJECT.json only, no prior artifacts): wrote
QUESTION.md, CARRY-OUT.md (GATE C), SCRIPT.md (GATE P draft), beat_sheet.json,
scenes.py + render_scenes.py (Manim, humanitarians palette). Ran:

```
python3 runtime/scripts/generate_audio_kokoro.py <REEL_DIR>
python3 render_scenes.py                          # B01-B04 Manim
python3 runtime/scripts/remotion_scenes.py <REEL_DIR>   # B00, BCRY, BHTF, BOUT
python3 runtime/scripts/compile.py <REEL_DIR>
```

**Iteration during the build (logged per the honesty rule):**
- B00 WRITER LAW: "remembers" → "rereads" (naive assumption that resuming mid-project
  means the agent remembers where it stopped, corrected to: it rereads a file). First
  render measured 10.52s narration (≥8s TIMING LAW floor cleared with margin); frame
  pull at the end of the beat confirmed the full corrected question ("How does it
  resume?") lands on screen with the correction visible.
- GATE T failed on first B03 render for two linked reasons: (1) §8.1 min-size —
  the rotated `"session boundary"` label (rendered sideways next to the dashed
  boundary line) measured 8px on the horizontal-scanline checker, well under the
  20px floor — rotated text reads as near-zero height to a checker that scans
  horizontal rows; (2) §8.4 kerning — the title `"THE FILE, ACROSS THE BOUNDARY."`
  tripped the pixel-level inter-glyph gap check: narrow letters in "FILE" (I, L)
  dragged the frame's mean glyph-run width down, so the ordinary word-gap before
  "ACROSS" (64px) read as 12× the (artificially small) expected advance — traced by
  reproducing the checker's own row_ink/column-run analysis directly against the
  rendered frame (peak_row 71, the title's cap-height band) rather than guessing.
  Fixed both by content: un-rotated the boundary label (also more legible for
  viewers — nobody should have to tilt their head) and reworded the title to
  "TRACKING PROGRESS ACROSS SESSIONS." (no isolated narrow-letter word directly
  before a normal word-gap), which dropped the over-threshold gap fraction from
  39% to 9% — well under the checker's 30% fail line. Re-rendered B03, GATE T
  cleared.
- Gate V frame pull caught two real defects no automated check flagged: (1) B01's
  `"session boundary"` label (`next_to(boundary, DOWN, buff=1.7)`) was pushed
  almost off the bottom of the frame — clipped, only the tops of letters visible;
  fixed by cutting `buff` to 0.3, keeping the label fully inside frame with clear
  separation from the footer line below it. (2) B04's dashed session-boundary line
  (`DashedLine(UP*3.6, DOWN*3.6)`) ran the full frame height and visibly crossed
  straight through the footer text ("Nothing outside the mechanism itself."),
  cutting through the word "mechanism"; fixed by shortening the line's vertical
  extent (`UP*2.3, DOWN*2.3`, recentered) so it clears the footer with room to
  spare. Re-rendered both beats, recompiled, re-pulled frames at the same
  timestamps to confirm both fixes — clean, no remaining overlap or clipping
  anywhere in the 18-frame full-runtime pass.

Result: `claude-quickstarts--feature-list-checkpoint-persistence.mp4`, 8/8 beats
filled real (no slate), 107.5s, 3840×2160.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS (0 FAILs after the B03/B01/B04 fixes above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio aac present, duration 107.56s; mp4 mtime
  (1788185483) newer than beat_sheet.json mtime (1788184536)
- Gate V (visual): pulled 18 frames at 6s spacing across the full runtime (two
  passes, before and after the B01/B04 fixes) and read them directly — B00's
  correction ("remembers" → "rereads") is legible and the full landed question is
  on screen before the beat ends; B01's session-timeline wipe, B02's two-file
  mechanism + read/implement/test/commit/mark-passing cycle, B03's anchor (file
  rows flipping across the session boundary, read-head landing on the first
  incomplete row), and B04's scoped checkpoint-mechanism box are all legible with
  no text overlap, no clipping, and safe inset respected; BCRY/BHTF/BOUT compose
  and outro cards are centered and fit their content with no truncation. No
  blockers remaining after the fixes above.
- B00 TIMING LAW: `actual_duration_s` 10.52s (≥8s requirement met, first
  iteration); correction and full landed question both visible before the beat
  ends.

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:4 (50%
remotion) — over the ~40% pantry cap per MOTION.md, but structural for
hai-simple's fixed shape (B00 writer + BCRY + BHTF + BOUT are REMOTION by skill
contract) at this 8-beat count, not a choice made in this build — same
structural note as the `claude-liam-first-run` sibling at 7 beats.

Metadata file written: `claude-quickstarts--feature-list-checkpoint-persistence.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: `claude-quickstarts` has no direct
entry in the map, so per the PHASE 3 fallback rule the `hai-simple` prefix was
matched instead — and the direct code link per DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate.
