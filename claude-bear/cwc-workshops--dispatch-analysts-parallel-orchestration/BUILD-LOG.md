# BUILD-LOG — cwc-workshops--dispatch-analysts-parallel-orchestration

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/dispatch-analysts-parallel-orchestration/beat_sheet.json`
(a Teardown-register reel built from the Code with Claude 2026 Workshop's
research-desk fan-out/fan-in example). Question, facts, and body argument
carried over unchanged: a custom tool (`dispatch_analysts`) is the
orchestration trigger the server intercepts; it spawns independent analyst
sessions, each with its own full context window, running in parallel; the
head agent waits without blocking while the server monitors the sessions
and resumes the head when all finish with the accumulated results; the
worked example (NVDA/AMD/MU, scores 9/6/4) and the serial-vs-parallel
timing collapse (fifty analysts: 25 minutes serial vs. ~30s parallel) carry
over exactly. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("conversations" → "sessions" —
the newcomer's actual misconception: that parallelizing means opening
several manual chat windows rather than one call that spawns sessions —
picked back up at B02's wrong-guess beat). Register re-registered
Teardown → Plain: the source's B07 orchestration-contract beat argued the
schema was "not clever engineering," "not overhead," and "the entire
reason fan-out works at scale" — design-judgment framing on why the
pattern was built that way. That framing was stripped in this redo's B08:
the same schema facts (fixed fields in, fixed fields out, off-schema
rejected cleanly) are stated as what happens, with the negative case made
explicit (skip the contract and a bad session can corrupt the merged
report silently) — a both-directions statement of fact, not a verdict on
whether the design is good engineering. The source's B08 verdict-recap
beat ("Let's recap with Claude...") was dropped entirely; its content is
compressed into the carry-out (BCRY) instead of restated as a separate
recap. Close re-skinned to `WantQuote` / `ClaudeComposerAsk` / `OutroCTA`
with @HumanitariansAI and Liam's sign-off.

NO-GENAI/NO-PANTRY LAW check: no source beat was ai-video-prompt, pantry,
or a human-drop slot beyond B00 (source B00 was already `ClaudeComposerAsk`
REMOTION, not a seedance puppet — hai-simple's WRITER LAW still requires
replacing it with `BrutalistHesitantWriter`). The source's body beats
(B02–B07) are bespoke Remotion components — `CwcOrchestrationQuestion`,
`CwcFanOutConcept`, `CwcFanOutFlow`, `CwcSpreadMechanism`,
`CwcFanOutSpeedGain`, `CwcResultAggregation`, `CwcOrchestrationContract` —
confirmed still registered and renderable (`./art scenes --check`) before
reuse; no substitution needed for those. One new component was required:
no library scene existed for "three separate chats, copied by hand" (the
wrong-guess beat Plain register requires and the Teardown source has no
equivalent for, going straight from the question to the mechanism) — built
as a single GRAPHIC/Manim beat (B02) reusing the verified chip-row
template verbatim from the sibling reel
`cwc-workshops--claude-liam-mining/scenes.py` (itself root-caused for
GATE T there).

Beat count: source ran 11 main-line beats (B00 host ask, B01 the-question,
B02–B07 mechanism/anchor/aggregation/contract, B08 verdict recap, B09
your-turn, B10 outro) plus 3 duplicate `lane: BOOKEND` beats used for the
source's own short-form cut (not carried into this redo — hai-simple has
no separate short-cut requirement here). This redo runs 12: B00 (writer)
+ B01 (question, kept) + B02 (new wrong-guess) + B03–B08 (source's
B02–B07, narration re-registered) + BCRY (new carry-out, absorbing the
source's dropped B08 verdict) + BHTF + BOUT (source's B09/B10, humanitarians
skin). No facts added or dropped. Full six-move + beat-count audit in
SCRIPT.md.

Built from scratch this session: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (12 beats), scenes.py + render_scenes.py (Manim "chip row"
template, copied from the verified sibling reel
`cwc-workshops--claude-liam-mining/scenes.py`).

Pipeline run in full, every step foreground, waited to exit before
proceeding (per this loop's ONE-SHOT rule):
1. `type_check.py --skip-pixels` — GATE T: PASS (before any render).
2. `generate_audio_kokoro.py` — 12/12 beats, `am_onyx`, actual_duration_s
   written back. B00 measured **11.26s** (TIMING LAW floor is 8s — met by
   a wide margin).
3. `render_scenes.py` — 1/1 GRAPHIC beat (B02) rendered via Manim, no
   failures.
4. `remotion_scenes.py` — 11/11 REMOTION beats rendered. Run in 7
   sequential foreground calls (`--only <beat>` for B06/B07/B08/BCRY/BHTF/
   BOUT after an initial batch call covering B00/B01/B03/B04/B05 was cut
   short by the tool's own 2m/10m command timeouts, not by the render
   process itself — no orphaned background renders; each call was waited
   on to its own exit code before the next was issued).
5. `compile.py` — `cwc-workshops--dispatch-analysts-parallel-orchestration.mp4`,
   12/12 beats real (no slate), 192.4s, 3840×2160.

**Gates:**
- content-check: PASS (12 beats, no violations)
- frame-check: PASS (3840×2160, 12 beats, no violations)
- lane-check: PASS (cut=master, no lane violations)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.6 dB
- ffprobe: video 3840×2160 h264, audio present, duration 192.3s; mp4 mtime
  newer than beat_sheet.json mtime (COMPLETION LAW satisfied)
- Gate V (visual): pulled frames at 8s spacing across the full 192s runtime
  plus a targeted pull late in B00 (9.5s in), and read them directly —
  B00's correction ("conversations" → "sessions") is legible and landed by
  9.5s, well inside its 11.3s window; B02's wrong-guess chip row ("THREE
  SEPARATE CHATS, COPIED BY HAND") reads cleanly; B04's NVDA/AMD/MU flow
  diagram (the anchor) is legible in full, matching the source's worked
  example exactly; B06 pays it off legibly ("50 analysts: 25 minutes
  serial vs. 30 seconds parallel"), directly answering B00's "fifty
  analysts" framing; B08's schema-contract diagram reads cleanly with the
  softened sparkLine ("Fixed schema in. Fixed schema out."); BHTF and BOUT
  carry the @HumanitariansAI handle and Liam's sign-off correctly, prompt
  card shows the exact your-turn command text. No overlap, no unsafe
  insets, no blockers found in any pulled frame.
- B00 TIMING LAW: `actual_duration_s` 11.26s (≥8s requirement met with
  margin); the "conversations" → "sessions" correction confirmed on screen
  by frame pull.

**Non-blocking warning (compile.py):** motion histogram remotion:11
graphic:1 — remotion at 91%, over the ~40% pantry cap in MOTION.md.
Structural, not a choice made in this build: the source's entire body
(B02–B07) is already bespoke Remotion components, not Manim, and reusing
them intact (rather than rebuilding six working, GATE-T-clean components
as Manim scenes purely to hit a motion-language ratio) is what the redo
contract's "keep the body argument" instruction asks for. Logged per the
honesty rule rather than padding the ratio by converting working
components for no pedagogical reason.

Metadata file written:
`cwc-workshops--dispatch-analysts-parallel-orchestration.md` (channel
@HumanitariansAI). Per playlists.json, `SUBJECT.json`'s `skill` field
(`hai-simple`) maps directly → **Playlist: Claude Basics**; content
(orchestrating parallel Claude agents) matches — no override needed.
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `cwc-workshops--dispatch-analysts-parallel-orchestration-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/cwc-workshops--dispatch-analysts-parallel-orchestration/`
(4K master + description) for the Drive sync. Pushed to
`humanitarians-youtube` as commit `a1d1205f`
(`claude-bear/cwc-workshops--dispatch-analysts-parallel-orchestration/`:
README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4), confirmed
`origin/main` up to date.

**Status: DELIVERED.**
