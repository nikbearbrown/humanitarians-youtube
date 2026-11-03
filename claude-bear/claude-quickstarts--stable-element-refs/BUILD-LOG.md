# BUILD-LOG — claude-quickstarts--stable-element-refs

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-quickstarts/youtube/stable-element-refs/beat_sheet.json` (a
Teardown-register scaffold, 4/8 beats filled with Manim, no SCRIPT.md, sourced
per its own SOURCES.md from `browser-use-demo/browser_tool_utils/` — an
illustrative worked example, not a file present in this checkout; see SOURCES.md
here). Question, anchor numbers, and worked example carried over unchanged: a
"Confirm Order" button at (960,540) on a 1920x1080 page, tagged `ref=confirm_order_1`,
reflows to roughly (720,405) after resizing to 1440x900 — the id stays attached,
the pixel doesn't. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "pixel" -> "ref"). Register re-registered
Teardown -> Plain (source narration carried no judgment to remove). Close/outro
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Source's B05
verdict/recap beat dropped as a restatement (matches the sibling
`claude-quickstarts--browser-coordinate-scaling` redo's precedent); source's B04
exclusions beat became this reel's BOTH-DIRECTIONS beat (B04: holds for anything
tagged before load, does not cover elements that appear after load without a
fresh tagging pass). No source beat was `ai-video-prompt`, pantry, or a
human-drop slot, so NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

**ONE FLAG, and why it differs from the sibling reel:** unlike
`claude-quickstarts--browser-coordinate-scaling`, whose sibling redo could read
`coordinate_scaling.py` directly and quote its exact formula, no
`browser-use-demo`/`browser_tool_utils` folder exists in this local checkout —
only the source scaffold's own citation of it. Per PHASE 1's "describe behavior
generically when in doubt," B02 states the tagging mechanism at the pattern
level (attach identity to the element, not its location) and carries the reel's
one explicit flag: the exact implementation varies tool to tool. See SOURCES.md.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00 10.84s,
   B01 21.87s, B02 20.12s, B03 22.83s, B04 16.66s, BCRY 8.38s, BHTF 15.06s,
   BOUT 4.84s.
2. Wrote `scenes.py` (4 Manim scenes, B01-B04) sized to the measured durations,
   and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The first invocation
   tripped the shell's 2-minute default timeout mid-run and was auto-moved to
   background by the tool; per the COMPLETION LAW ("never end your turn
   expecting to be woken by a background render"), this was NOT treated as a
   stopping point — blocked on the task's actual exit via `TaskOutput` in the
   same turn before proceeding. All four beats completed clean (exit 0).
4. **B00 TIMING LAW verified, not just asserted:** narration measured 10.84s
   (32-word script, within the 20-35 word band) + 0.8s lead silence, giving the
   writer clip 10.87s total — comfortably over the >=8s / >=9s-window floor.
   Frame pulls at 9.0s and 10.5s of the 10.87s clip confirm the "pixel" ->
   "ref" correction completes and rests legibly with buffer before the beat
   ends (matches the render tool's own report: "extended to 10.8s").
5. **Gate V (visual) caught three real layout bugs across two render passes,
   fixed at the root, not papered over:**
   - **B01, pass 1:** the "Confirm Order" label was centered on top of a
     drawn button rectangle sized smaller than the text, so the box border
     visually crossed the label (looked like strikethrough). Root cause:
     placing text via a guessed `move_to` offset assumes the text renders
     smaller than it does. Fixed by dropping the button rectangle entirely
     and using a plain dot (matching the sibling reel's proven convention) —
     the label sits above the dot via `.next_to()`, never straddling a shape.
   - **B01, pass 1:** the "remembered (960, 540)" ghost-coordinate label
     directly overlapped a second "Confirm Order" button+label drawn in the
     same small reflowed-page card — two independent label groups placed too
     close together in a cramped space. Fixed by removing the (unnecessary,
     since B01 doesn't need to show the button's real new position — that's
     B03's job) second button entirely, and moving the ghost label to sit
     below the whole card via `.next_to(page2, DOWN)` instead of tucked
     against the ghost dot.
   - **B03, pass 1:** the "ref=confirm_order_1" chip (20 characters, the
     widest string in the reel) was centered on a dot offset toward one side
     of its card, so the wide label's left edge extended past the card's
     left border. Fixed by re-centering the dot at the card's exact center
     (not an off-center offset) so the chip's margins are symmetric on both
     sides, and widening the cards (3.3/2.9 -> 4.0/3.5) for extra clearance.
   - **B04, two passes:** the "TAGGED BEFORE LOAD" / "APPEARS AFTER LOAD"
     card headers were placed via `move_to(card.get_top() + DOWN*0.4)`,
     which put them straddling the card's rounded top border. Fixed by
     moving them outside the card via `.next_to(card, UP)`. First fix
     attempt still left "YES" crossing the card's top border (button group
     positioned too high inside the card); root-caused via the same
     bounding-box arithmetic (card top edge vs. label top edge) and fixed by
     lowering the button group inside the card (`UP*0.35` -> `UP*0.1`).
   Re-verified every fix with fresh frame pulls after each re-render; zero
   remaining overlaps across a full sweep of the 121.6s runtime (14 frames
   total, roughly one every 8-10s plus targeted pulls on every fixed beat).
6. **GATE T (type_check.py): PASS, 0 FAILs, no exemptions needed** — clean on
   the first run after the Gate V fixes above (no kerning false positives to
   adjudicate this time, unlike the sibling reel).
7. `compile.py` -> `claude-quickstarts--stable-element-refs.mp4`, 8/8 real (no
   slate), 121.6s, 3840x2160 (THE 4K LAW).

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 121.6s; mp4 mtime
  (11:44:06) newer than beat_sheet.json mtime (11:33:49)

**Gate V (visual):** pulled frames across the full runtime (roughly every 8-10s)
plus targeted re-pulls on every beat touched by a fix, and read them directly.
B00's correction ("pixel"->"ref") lands and rests legibly before the beat ends.
B01's anchor (Confirm Order button, (960,540) on 1920x1080 -> remembered pixel
misses on the 1440x900 reflow) and B03's payoff (same button, `ref=confirm_order_1`
survives the identical resize while the pixel chip changes from (960,540) to
(720,405)) are visually recognizable as the same object across both appearances,
per ANCHOR LAW. B02's FLAG marker is legible and unambiguous. B04's two-panel
both-directions split reads cleanly with no border collisions. BCRY/BHTF/BOUT
text is centered, legible, no overlap, safe inset respected, HAI skin correct
(@HumanitariansAI, Fable 5 composer, no Claude branding). No blockers remaining.

**Non-blocking warning (compile.py):** motion histogram remotion:4 graphic:4 —
remotion at 50% of beats, over the ~40% pantry cap in MOTION.md. Structural, not
a defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn)
+ BOUT (outro) all REMOTION by skill contract, against 4 GRAPHIC body beats for
this 8-beat reel — the ratio is fixed by beat count, same accepted warning as
every other 8-beat hai-simple reel in this family.

**One inference flag (ONE-FLAG LAW):** B02 flags that the exact tagging
implementation (attribute name, injection timing, duplicate-id handling) varies
tool to tool — the reel teaches the pattern, not one fixed API, because no
locally-inspectable source file could confirm one specific implementation in
this checkout. See SOURCES.md for the full reasoning.

Metadata file written: `claude-quickstarts--stable-element-refs.md` (channel
@HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `hai-simple` skill-name key,
since `claude-quickstarts` has no direct entry in the map — plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.
