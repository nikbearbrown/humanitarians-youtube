# BUILD-LOG — claude-quickstarts--screenshot-prompt-caching

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-quickstarts/youtube/screenshot-prompt-caching/beat_sheet.json`
(a Teardown-register scaffold: B01–B04 fully narrated as Manim/GRAPHIC beats;
B00 cold open, B05 verdict card, B06 your-turn, and B07 outro all drafted but
never rendered (SLATE); plus three abandoned BOOKEND placeholder slates
BVDT/BHTF/BOUT carrying only generic template text, never reconciled with the
earlier beats — same unfinished-scaffold shape as several other
`claude-quickstarts` sources in this queue). Question, facts, and the worked
example carried over unchanged: a 50-turn computer-use task, 35 of those
turns resending an identical screenshot, ~2,000 tokens/screenshot; the
concrete case of 5 unique desktop states A–E across the 50 turns (100,000
tokens uncached vs. 10,000 cached, 90% saved); the fix is one field,
`cache_control: {"type": "ephemeral"}`, on the image block. B00 replaced the
source's `ClaudeComposerAsk` cold open (drafted, never rendered) with
`BrutalistHesitantWriter` (WRITER LAW: "nothing" → "the same", framed as a
question rather than the source's/sibling's statement form). Register
re-registered Teardown → Plain — the source narration itself carried no
separate design verdict to remove, so this was a metadata/skin change, not a
content cut. Close/outro re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Source's B05 verdict/recap beat dropped as a restatement of
B01–B04 (Plain register carries no separate verdict beat); source's B04
exclusions clause folded into this reel's B04 both-directions clause. No
source beat was `ai-video-prompt`, pantry, or a human-drop slot (every
drafted beat was already `ClaudeComposerAsk`/`ClaudeVerdictArtifact`/
`ClaudeTitleOutro` Remotion shapes, most simply unbuilt), so NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (already covered by
WRITER LAW).

**Duplicate-source note (logged for transparency, not treated as a
blocker):** the identical underlying facts were already built and delivered
once before as `hai-simple/claude-basics--screenshot-prompt-caching`
(2026-08-28), from a *different* source-sheet path
(`anthropics/youtube/claude-basics/screenshot-prompt-caching/`).
`queue_scan.py --from-sheets` queues every `beat_sheet.json` under
`anthropics/` independently by design (no cross-path dedup), so this is a
second, separately sourced redo target, not a re-run of the same job — same
situation as the `claude-quickstarts--browser-coordinate-scaling` /
`claude-basics--browser-coordinate-scaling` sibling pair. To avoid a
byte-identical duplicate, this build uses fresh narration throughout, a
different wrong-guess framing (question form: "does sending it again cost
nothing?" vs. the sibling's statement form: "...is free, right?"), and pulls
in the "dialog still open / progress bar still crawling" imagery from the
*original* Teardown source's B01 narration that the `claude-basics` sibling
did not use — while keeping every number exactly as sourced, since they are
measured facts (from the source's own `SOURCES.md` seed), not illustrative
choices invented for this reel.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   10.62s, B01 23.25s, B02 20.69s, B03 21.18s, B04 26.97s, BCRY 8.00s,
   BHTF 20.52s, BOUT 3.80s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground, full
   run in one invocation — no timeout issue this time).
4. **B00 TIMING LAW verified clean on the first render:** this reel used the
   already-corrected timing knobs from the sibling's pilot-lesson fix
   (charMs=38, hesitateBetween=12, mistakeRate=4, hesitateWithin=2, 4
   punctuation marks in the writer text) rather than the original
   over-aggressive defaults, so no re-render was needed. Frame pulls at 9.0s
   and 10.0s of the 10.63s clip both show "again cost the same?" fully typed
   and resting legibly, well before the beat ends.
5. `compile.py` → `claude-quickstarts--screenshot-prompt-caching.mp4`, 8/8
   real (no slate), 136.0s, 3840×2160 (THE 4K LAW).
6. **GATE T caught one real bbox-overlap finding, root-caused as a known
   false-positive class, then exempted per the file's own established
   precedent format (content checked first, validator touched only after):**
   B04Scene's scope-limit card ("not the full protocol · not permanent",
   RoundedRectangle border + centered label) tripped §8.6b — the card
   border's closed-stroke bbox was detected as a text-run blob
   (499,761)-(1420,899), reported as enclosing a second small blob
   (901,819)-(938,841) corresponding to the "·" middot glyph between the two
   clauses. This is the same box-border-encloses-interior-label pattern
   already documented for ~10 other scenes in `type_check.py`'s
   `BBOX_OVERLAP_EXEMPT_PATTERNS` (e.g. `MIVB01Scene`, `EFB03Scene`–
   `EFB06Scene`). Verified by frame pull at t=15s of the raw manim/B04.mp4
   (well after the card's FadeIn settles) plus additional pulls at t=3/5/7/9s
   spanning the card's full on-screen life: the label sits cleanly centered
   inside its border with visible margin in every frame, no real
   text-on-text overlap. Added `B04Scene` to `BBOX_OVERLAP_EXEMPT_PATTERNS`
   with a precedent-matching comment. GATE T then passed 0 FAILs.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the B04Scene bbox-overlap exemption above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -0.9 dB
- ffprobe: video 3840×2160 h264, audio aac present, duration 136.04s; mp4
  mtime newer than beat_sheet.json mtime

**Gate V (visual):** pulled 17 frames at 8s spacing across the full 136.0s
runtime (fps=1/8), plus 4 targeted pulls across B04's full on-screen life
(t=3/5/7/9s) and 2 targeted pulls on B00's correction (t=9/10s). All clean:
B00's correction ("nothing" → "the same") lands and rests legibly well
before the beat ends. B01's dialog/progress-bar icons and 50-turn strip are
legible with clear margin. B02→B04's anchor (the 50-frame A–E filmstrip,
100,000 tokens uncached → 10,000 tokens cached, 90% saved) is visually
recognizable as the same filmstrip across both appearances, per ANCHOR LAW.
B04's scope-limit card and two-line footer sit clear of the frame's bottom
edge with no overlap (confirming the GATE T exemption above was correct).
BCRY/BHTF/BOUT text is centered, legible, no overlap, safe inset respected,
HAI skin correct (@HumanitariansAI, Subscribe pill, no Claude branding). No
blockers remaining.

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count,
same as every other 8-beat hai-simple sibling's identical, already-accepted
warning.

**Zero inference flags:** every on-screen claim (50-turn task, 35 identical
repeats, ~2,000 tokens/screenshot, `cache_control: {"type":"ephemeral"}`,
5 unique states A–E, 100,000 vs. 10,000 tokens, 90% savings, session-only
persistence) is a direct carry-over of the source scaffold's own sourced
numbers — see SOURCES.md. Per ONE-FLAG LAW, a fully-sourced explanation
carries no flag.

Metadata file written: `claude-quickstarts--screenshot-prompt-caching.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `hai-simple` prefix,
since `claude-quickstarts` has no direct entry in the map — plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
