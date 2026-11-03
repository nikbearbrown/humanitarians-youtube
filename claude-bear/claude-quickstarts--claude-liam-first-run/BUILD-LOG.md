# BUILD-LOG — claude-quickstarts--claude-liam-first-run

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-quickstarts/youtube/claude-liam-first-run/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel examining the real Anthropic
skill `first-run`). Question ("Claude, First Run."), facts (a skill is a
folder Claude reads before acting; SKILL.md is the full instruction set; the
Steps section runs linearly; first-run's own job is env check → one safe
browser-only task → open the trajectory viewer), and the 7-beat count carried
over unchanged. B00 replaced `ClaudeComposerAsk` with `BrutalistHesitantWriter`
(WRITER LAW). Register re-registered Teardown→Plain: the source's B03 graded
the skill ("what it gets right… what it bites") — that judgment was removed
entirely; the rebuilt B03 states the same three steps and the same boundary
as a fact, not a verdict. BVDT (verdict recap) became BCRY (`WantQuote` carry-
out card) per simple's verdict→carry-out row. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was generalized from a
private-repo skill path few viewers have access to, into a genuinely runnable
ask (any detailed instructions the viewer already has). No source beat was
`ai-video-prompt`, pantry, or a human-drop slot — the source was already
all-Remotion — so NO-GENAI/NO-PANTRY LAW required no substitution beyond the
WRITER LAW itself. Body beats B01–B03 (`SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism`, fixed Claude-palette
Remotion with no palette-override props) were rebuilt as GRAPHIC (Manim) in
the humanitarians palette instead, matching this skill's established
channel-skin practice (`claude-basics--anthropic-retrieval-demo-…`) rather
than keeping the Claude-branded chrome.

Built from scratch this invocation (SUBJECT.json only, no prior artifacts):
wrote QUESTION.md, CARRY-OUT.md (GATE C), SCRIPT.md (GATE P draft),
beat_sheet.json, scenes.py + render_scenes.py (Manim, humanitarians palette).
Ran:

```
python3 runtime/scripts/generate_audio_kokoro.py <REEL_DIR>
python3 render_scenes.py                          # B01–B03 Manim
python3 runtime/scripts/remotion_scenes.py <REEL_DIR>   # B00, BCRY, BHTF, BOUT
python3 runtime/scripts/compile.py <REEL_DIR>
```

**Iteration during the build (logged per the honesty rule):**
- B00's first render (text "Claude just knows / what to do first — / it's
  built in, right? / So what's actually there?", charMs 55, hesitateBetween
  22) ran out of its 11.3s audio window before typing the landed question —
  the writer stalled on "it's written in, right?" and never reached line 4.
  Shortened the text ("Claude just runs / first-run — it's / built in,
  right? / What's really there?") and tightened timing knobs (charMs 46,
  hesitateBetween 8, hesitateWithin 2, jitter 20); re-rendered; verified by
  pulling a frame at 10.9s — full text lands, correction visible, caret
  idle before the beat ends.
- GATE T first failed on BHTF: `topic` prop "CLAUDE BASICS · WHAT A SKILL IS"
  truncated in the composer card. Shortened to "CLAUDE BASICS · SKILLS";
  re-rendered BHTF; GATE T cleared that finding.
- Gate V frame pull caught two real rendering defects the automated gates
  didn't: (1) B01's 📄 emoji rendered as a blank white box (glyph not in the
  render font) — replaced with a vector document icon drawn from Manim
  primitives; (2) B03's ✓ character rendered as garbled stacked digits
  ("27⁄13" — a fraction-glyph fallback) — replaced with a hand-drawn
  checkmark built from `VMobject.set_points_as_corners`. Re-rendered both.
  The first icon redraw (a Polygon file shape with a folded corner + three
  internal ruled lines) then tripped GATE T's kerning-sanity check
  (§8.4: "max inter-glyph gap 307px" on B01) — the internal ruled lines read
  as a false glyph run to the pixel scanner. Fixed by content, not by
  touching the validator: simplified the icon to a single `RoundedRectangle`
  with no internal strokes. GATE T cleared.

Result: `claude-quickstarts--claude-liam-first-run.mp4`, 7/7 beats filled
real (no slate), 77.2s, 3840×2160.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS (0 FAILs after the B01/B03 fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160, audio present, duration 77.18s; mp4 mtime
  (1788183555) newer than beat_sheet.json mtime (1788183081)
- Gate V (visual): pulled 13 frames at 6s spacing across the full runtime and
  read them directly — B00's correction ("built" → "written") is legible and
  the full landed question ("What's really there?") is on screen before the
  beat ends; B01's folder→file anatomy, B02's three-phase pipeline, and
  B03's three-step scope box with dashed boundary are all legible with no
  text overlap and safe inset respected; BCRY/BHTF/BOUT text is centered,
  BHTF's composer card fits its topic label without truncation. No
  blockers remaining after the two mid-build fixes above.
- B00 TIMING LAW: `actual_duration_s` 11.33s (≥8s requirement met, second
  iteration); correction and full landed question both visible before the
  beat ends.

**Non-blocking note (compile.py):** motion histogram remotion:4 graphic:3 —
structural for hai-simple's fixed shape (B00 writer + BCRY + BHTF + BOUT are
REMOTION by skill contract) at this 7-beat count, not a choice made in this
build.

Metadata file written: `claude-quickstarts--claude-liam-first-run.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: `claude-quickstarts` has no
direct entry in the map, so per the PHASE 3 fallback rule the `hai-simple`
prefix was matched instead — and the direct code link per DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) next in this same invocation.
