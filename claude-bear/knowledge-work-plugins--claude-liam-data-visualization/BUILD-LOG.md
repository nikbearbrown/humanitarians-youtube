# BUILD-LOG — knowledge-work-plugins--claude-liam-data-visualization

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-data-visualization/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`data-visualization` Anthropic skill — the `data` plugin's chart-design
tool). Only `SUBJECT.json` existed on pickup.

**Source-material defect found and worked around:** unlike the sibling
redo `knowledge-work-plugins--claude-liam-create-viz` (truncated
narration), this source's own body narration was never skill-specific to
begin with — it is content-free batch-build scaffolding: B01 = "SKILL.md
is the instruction set. 1 file total."; B02 = a generic 3-step "Read
SKILL.md -> Execute -> Return output" pipeline with no data-visualization
content at all; B03 quotes the skill's own `description` field and cuts it
off mid-word ("Use when building ch."). Its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/data/skills/data-visualization/SKILL.md`)
does not exist anywhere in this local tree (confirmed: `ls` fails). Per the
REDO LAW, the missing facts could not be invented, so they were re-sourced
directly from the real, public file: `github.com/anthropics/knowledge-work-plugins`,
`data/skills/data-visualization/SKILL.md` (fetched via
`raw.githubusercontent.com`/curl, read in full this invocation). All facts
in this reel — the chart-selection-by-relationship table, the explicit
avoid-list (pie/3D/dual-axis charts), the color/design-principles section
(one accent carries the story, sequential/diverging/categorical rules,
red/green-only failing colorblind viewers), and the accessibility
checklist (patterns/line-styles as a color-independent backup, screen
reader alt text) — are sourced from that real file, not from the source
sheet's content-free template text.

**Distinct angle from the same-family sibling:** `create-viz` (redone
earlier the same day) already covers chart-type-selection-vs-styling with
an "honest axis" framing. To avoid retreading that ground, this reel's
wrong guess and body argument are built around **color and accessibility**
instead — a part of the real `data-visualization` SKILL.md the `create-viz`
reel did not use.

**Register re-registered Teardown -> Plain**: the source graded the skill
("What it gets right: repeatable results. What it bites: anything outside
the spec.") and framed a "Verdict" card; this redo states the chart-type
and accessibility rules as fact (no grading language) and folds the close
into a `WantQuote` carry-out beat. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"colorful" -> "accessible" — the newcomer assumption that data
visualization means picking bright colors, corrected to: color has to
encode meaning, and the chart type comes first). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt was
rewritten clean — the source's handoff string was a broken, truncated
template referencing the skill file directly; this version asks the
viewer to paste five made-up survey scores and ask Claude to name the
chart type and pick colorblind-safe colors, which doubles as a live test
of the reel's own claim.

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
   `knowledge-work-plugins--claude-liam-create-viz` (same family, already
   DONE, built earlier the same day) as a concrete precedent for the
   defect class and the file layout (`scenes.py`, `render_scenes.py`,
   `<slug>.md` format). Confirmed the source's `source_skill` path does
   not exist locally; re-sourced real facts from the public
   `anthropics/knowledge-work-plugins` GitHub repo via `curl`/
   raw.githubusercontent.com this invocation.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Plain
   register: carry-out written first, then the reel reverse-engineered to
   land it). Wrong guess: "data visualization" means picking bright
   colors. Correction: color is a constraint that has to earn its place
   (meaning-bearing, colorblind-safe), applied only after the chart type
   is chosen from the data's relationship.
3. Wrote `SCRIPT.md` (7-beat table, redo audit, register audit, deliberately
   -not-claimed section) and `beat_sheet.json`, matching the source's exact
   7-beat count (B00, B01, B02, B03, BVDT->BCRY, BHTF, BOUT). GATE L checked
   all four reused Remotion components before slating — `BrutalistHesitantWriter`,
   `WantQuote`, `ClaudeComposerAsk`, `OutroCTA` all RENDERABLE with matching
   props (`./art scenes --check`).
4. Generated audio: `generate_audio_kokoro.py`, free, `am_onyx`, cost $0.00.
   Measured durations: B00 10.86s, B01 15.70s, B02 18.79s, B03 16.96s, BCRY
   9.71s, BHTF 13.40s, BOUT 4.86s.
5. Wrote `scenes.py` / `render_scenes.py` for the three GRAPHIC beats (B01
   anatomy — folder + SKILL.md contents; B02 mechanism — a
   relationship-to-chart-type list filling in, then a "ruled out" list
   struck through; B03 constraint — bars draining to grey except one
   accent bar, a red/green pair marked unreadable, the same chart redrawn
   with hatch patterns instead of color), Manim, humanitarians palette,
   durations matched to measured audio. Rendered all three in the
   foreground — clean on first pass.
6. Rendered the four REMOTION beats via `remotion_scenes.py` (foreground).
   The render exceeded the tool's inline timeout and the harness moved it
   to a tracked background task; per the COMPLETION LAW, blocked on it
   directly via `TaskOutput(block=true)` until the task-completion
   notification confirmed exit code 0 — all 4/4 beats rendered clean on
   the first pass (B00, BCRY, BHTF, BOUT). Verified `media/B00.mp4`
   directly: `ffprobe` confirms 10.87s with audio+video tracks, clearing
   the >=8s TIMING LAW floor; a frame pull at t=9.5s shows the correction
   complete and legible — "Claude, make my chart accessible."
7. First `compile.py` pass -> 7/7 real (no slate), native 4K master, 91.3s,
   mean_volume -24.0 dB.
8. GATE T (`type_check.py`): **FAIL** on first run — B02's "RULED OUT:"
   list min-size flagged at 12px < 20px floor. Root cause was NOT font
   size: it was the TERRA strikethrough `Line()` bisecting each struck
   word ("Pie charts", "3D charts", "Dual axes"), splitting letter bodies
   into small isolated ink fragments below the floor — verified by a
   zoomed direct-frame crop of the exact struck region at 4K, same
   rendering-geometry artifact class already documented for
   `ESB06Scene`/simple-watermark `S02`/`S05`/`S15`/`S16` in
   `type_check.py`'s `HAND_DRAWN_PATTERNS` §8.1 exemption set (all struck
   text is fully legible at design size; only the blob detector splits it).
   **Fix:** renamed the three scene classes from the generic
   `B01Scene`/`B02Scene`/`B03Scene` to reel-unique `DVB01Scene`/
   `DVB02Scene`/`DVB03Scene` (per the file's own documented
   collision-avoidance convention — bare boilerplate names are shared
   across hundreds of reels' exemption lookups), then added a new,
   evidence-documented `DVB02Scene` entry to `HAND_DRAWN_PATTERNS` in
   `runtime/scripts/type_check.py`, matching the `ESB06Scene` precedent's
   justification format exactly. Re-ran: §8.1 cleared, but surfaced a
   **second, real** finding — contrast §8.3 FAIL: the "RULED OUT:" label
   was set in TERRA-on-cream (~2.74:1, below the 4.5:1 WCAG floor for
   typographic text, a known palette constraint documented elsewhere in
   the same file for structural marks but not exempt for actual prose).
   **Fix:** switched that label to INK (the strikethrough lines themselves,
   which are structural marks rather than typography, stayed TERRA). Also
   independently caught and fixed a content bug while reviewing frames:
   B03's "story bar" that was meant to demonstrate "one accent color
   carries the finding, everything else fades to grey" was colored brown
   (`#8C6D46`), not the actual TERRA accent — the visual didn't match its
   own narration's claim. Switched it to TERRA. Re-rendered B03,
   recompiled, re-ran `type_check.py`: **GATE T PASS**, 0 FAILs.
9. Gate V: pulled a frame sweep across the full 91.2s master (18 frames
   spanning all 7 beats, both before and after the B02/B03 fixes) and read
   each directly. All clean — B00's hesitation/correction arc reads
   clearly, B01's folder anatomy is legible, B02's relationship list and
   ruled-out list both read with clean struck text at 4K, B03's accent bar
   now visibly matches "one accent color carries the finding" with the
   red/green pair crossed out and the pattern-fill row legible,
   BCRY/BHTF/BOUT all legible. One pre-existing, non-blocking cosmetic
   note: `OutroCTA` renders on flat white rather than the humanitarians
   cream ground — a known shared-component quirk already logged unfixed on
   multiple siblings in this factory (e.g.
   `knowledge-work-plugins--claude-liam-create-viz`); not a new defect.
10. Final master verified directly: 3840x2160 (born natively via
    compile.py's 4K LAW), 91.2s, mean_volume -24.0 dB (max -3.0 dB), mtime
    (1788450990) newer than `beat_sheet.json` (1788450286) — the COMPLETION
    LAW conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.86s**, clears the >=8s floor. The
  correction ("colorful"->"accessible") is visible and settled on-screen
  by t=9.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** FAIL (min-size false-positive on struck
  text; then a real contrast violation once the false positive cleared) ->
  fixed (reel-unique scene names + documented §8.1 exemption; TERRA label
  -> INK) -> PASS, 0 FAILs on re-run.
- **Gate V (frame QC):** full sweep across all 7 beats, all read directly;
  also caught and fixed a content bug (B03's accent bar was brown, not
  TERRA) that GATE T's automated checks would not have flagged.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was
needed — copied directly to
`knowledge-work-plugins--claude-liam-data-visualization-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-data-visualization/` (4K
master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-data-visualization/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
