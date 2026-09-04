# BUILD-LOG — knowledge-work-plugins--claude-liam-guideline-generation

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-guideline-generation/beat_sheet.json`
(7-beat Teardown "skill-teardown" sheet for the Anthropic `guideline-generation`
skill, brand `claude-liam`, @NikBearBrown).

**Source defect found and worked around:** the source sheet's narration
contains an unfilled template gap — a literal `>` character in place of the
skill's one-line description in several narration strings (B00, B03/BVDT)
and in one Remotion prop (`B03.shot.remotion.props.body`). Confirmed this
is a batch build defect, not a design choice, by diffing against sibling
sheets from the same batch (`claude-liam-accessibility-review`,
`claude-liam-analyze`), where the equivalent slot interpolated correctly.
The description sentence itself is intact elsewhere in this exact source
sheet — `B00.shot.remotion.props.output[1]` and
`BVDT.shot.remotion.props.artifactLines[1]` both read verbatim "Generates
brand voice guidelines from source materials." Used that source-confirmed
sentence to fill every gap; no external file was read or invented. Full
account in QUESTION.md. The `source_skill` path the source names
(`/Users/bear/Documents/CoWork/bear-textbooks/.../guideline-generation/SKILL.md`)
does not exist on this machine (different machine's home directory) and
was not needed for this reason — the source sheet's own intact fields
carried enough to redo faithfully.

**The call:** register re-registered Teardown -> Plain. Source's B03/BVDT
framed "what it gets right / what it bites" as a design-tell verdict —
Teardown language — removed; Plain states only the mechanism (read source
material, extract the patterns the file defines, structure them, return
the guideline) and its two failure directions as properties of the
practice, never a verdict on the skill's design. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: "taste" -> "your samples" — the naive assumption that a brand voice
guideline comes from Claude's own literary taste, corrected to: it's built
from the material you hand it. Added a wrong-guess beat (B01: an editor's
private taste vs. a written spec that pulls the same kind of patterns from
source material every time, falsified by "ask it to judge whether your
voice is any good, and there's no step written for that") and an anchor
(B02 -> B03: ten blog posts, traveling read -> extract -> structure ->
return, landing on "one guideline document," then paid off into "run
twice, same guideline" / "asking whether the voice is good has no step")
per this factory's PHASE 1 structure requirement — the source's Teardown
shape (anatomy / pipeline / design-tell / verdict) carried neither. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the
source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No source
beat was AI-VIDEO, pantry, or a human-drop slot — every source beat was
already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat
replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 9.73s (clear of the >=9s TIMING LAW
   floor) on the first narration draft (33 words + `lead_silence_s: 0.8`).
   Durations: B00 9.73s, B01 22.29s, B02 20.42s, B03 19.56s, BCRY 12.69s,
   BHTF 18.18s, BOUT 3.73s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `GLGB01Scene` /
   `GLGB02Scene` / `GLGB03Scene`, ported from the `analyze` sibling's
   already-fixed TEAL-border card convention) and `render_scenes.py`;
   rendered B01/B02/B03 clean on the first pass, foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`, foreground. The
   shell tool's default 120s timeout moved the render to background
   automatically; per the one-shot COMPLETION LAW this was NOT treated as
   a hand-off — blocked on `TaskOutput` (590s budget) in the same turn
   until it exited (code 0) before proceeding. All four beats rendered
   clean on the first pass; confirmed BHTF's explicit
   `folderLabel: "@HumanitariansAI"` override rendered correctly.
4. `compile.py` — same background-timeout situation, same TaskOutput
   block-until-exit handling. First pass -> 7/7 real (no slate),
   3840x2160 (THE 4K LAW), GATE AUDIO pass on the first compile — but
   GATE T (below) caught one defect that required a targeted re-render.
5. GATE T (`type_check.py`) FAILED on first pass: B03's mini-row label
   "STRUCTURE" (font_size 14, scaled 0.6x post-layout) rendered at ~10px,
   under the 20px §8.1 floor. Root-caused via the B02/B01 sibling beats'
   passing sizes (font_size 15-17 unscaled maps to ~20-22px, confirming
   ~1.29px per font_size unit) — the B03 mini-row's post-scale font sizes
   were the only ones in the reel small enough to cross the floor. Fixed
   in `scenes.py` by switching those three labels to `_fit_text` at
   font_size 28 (from 14-15) with a 2.7-unit width cap, giving headroom
   after the 0.6x shrink. Re-rendered B03 only (`render_scenes.py` skips
   existing beats), recompiled (only B03's slot re-encoded), re-ran GATE
   T -> PASS (smallest run 21px >= floor 20px, tight but clean).
6. Gate V (visual, manual): pulled 12 evenly-spaced frames across the full
   107.6s runtime plus two targeted frames (B00 at t=9.0s to confirm the
   writer's correction; BOUT at t=105s to catch the very end past the
   coarse ~9s sampling interval) and read every one directly. B00's
   correction ("taste" -> "your samples") is fully typed and settled by
   t=9.0s of a 9.7s beat; B01's struck "Claude's taste" figure and lit
   "THE SPEC" card (read SKILL.md / execute steps / return the guideline)
   read cleanly, including the "judge the voice? -- no step" caption
   outside the card border; B02's four-stop anchor (READ/EXTRACT/
   STRUCTURE/RETURN, with the traveling "TEN BLOG POSTS" token beside each
   TEAL-bordered card) is legible at every step, landing on "one guideline
   document"; B03's condensed anchor-return and both-directions split
   (struck-through "JUDGE?", the fixed STRUCTURE label at its new size)
   read cleanly; BCRY's carry-out quote, BHTF's Your Turn composer card
   (confirmed `@HumanitariansAI`, not the hardcoded default), and BOUT's
   `OutroCTA` (confirmed `@HumanitariansAI`, no Claude mascot) all render
   legibly with no overlap, no clipping, no contrast issues. No defects
   found.
7. Audio presence: independently verified with `ffprobe` (aac stream,
   48000 Hz present) and `ffmpeg -af volumedetect` on the final master ->
   mean_volume **-24.1 dB**, max -2.9 dB. Master mtime (1788490592) is
   newer than beat_sheet.json mtime (1788490247).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after one targeted fix (B03 mini-row font sizes)
- Gate V: PASS, second look after the GATE T fix — no defects found
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 107.6s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `knowledge-work-plugins` matches the
`knowledge-work-plugins` key in
`skills/make/hai-simple/loop/playlists.json` directly, resolving to
**Extending Claude — Skills, Plugins & Connectors**.

Metadata file written:
`knowledge-work-plugins--claude-liam-guideline-generation.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors**, plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
