# BUILD-LOG — knowledge-work-plugins--claude-liam-capacity-plan

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-capacity-plan/beat_sheet.json`
(7-beat Teardown "skill-teardown" sheet for the Anthropic `capacity-plan`
skill, brand `claude-liam`, @NikBearBrown).

**Source note:** the source sheet's narration already carries real,
specific facts about the skill — plan resource capacity, workload analysis
and utilization forecasting; used when heading into quarterly planning,
the team feels overallocated and you need the numbers, deciding whether to
hire or deprioritize, or stress-testing whether upcoming projects fit the
people you have — see QUESTION.md. The `source_skill` path it names (a
different machine's home directory) does not exist locally, but no
reconstruction was needed. Used the `knowledge-work-plugins--claude-liam-analyze`
sibling (identical source shape: cold open / anatomy / pipeline / design
tell / verdict / handoff / outro, skill-teardown) as the structural
template — its scaffold conventions (humanitarians-palette Manim cards
with TEAL borders, `render_scenes.py`, `scenes.py` docstring guidance,
ASKED/MATCHED/STEPPED/RETURNED anchor pattern) were reused directly.

**The call:** register re-registered Teardown -> Plain. Source's B03/BVDT
framed "what it gets right / what it bites" as a design-tell verdict —
Teardown language — removed; Plain states only the mechanism (run the
workload analysis, then forecast utilization from it) and its two failure
directions as properties of the practice, never a verdict on the skill's
design. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW: "instinct" -> "the file" — the
naive assumption that Claude senses an overloaded team by feel, corrected
to: it runs a written procedure against numbers. Added a wrong-guess beat
(B01: a manager's private feel for who's stretched thin vs. a two-step
workload-analysis/utilization-forecast procedure, falsified by "hand it a
request with no workload or capacity numbers attached, and there's
nothing for either step to run on") and an anchor (B02 -> B03: team at 118%
utilization heading into quarterly planning, traveling asked -> matched ->
stepped -> returned "hire one or cut one project", then paid off into "run
twice, same numbers" / "team morale has nothing tailored to reach for")
per this factory's PHASE 1 structure requirement — the source's Teardown
shape (anatomy / pipeline / design-tell / verdict) carried neither. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the
source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No source
beat was AI-VIDEO, pantry, or a human-drop slot — every source beat was
already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 11.20s (clear of the >=9s TIMING LAW
   floor) on the first narration draft (33 words + `lead_silence_s: 0.8`).
   Durations: B00 11.20s, B01 25.47s, B02 21.91s, B03 20.82s, BCRY 12.95s,
   BHTF 21.59s, BOUT 4.03s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CPLB01Scene` /
   `CPLB02Scene` / `CPLB03Scene`, ported from the `analyze` sibling's
   already-fixed TEAL-border card convention) and `render_scenes.py`;
   rendered B01/B02/B03, foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The shell tool's
   default 120s timeout moved the render to background automatically; per
   the one-shot COMPLETION LAW this was NOT treated as a hand-off —
   blocked on `TaskOutput` (590s budget) in the same turn until it exited
   (code 0) before proceeding. All four beats rendered clean on the first
   pass.
4. `compile.py` — same background-timeout situation, same TaskOutput
   block-until-exit handling. First pass -> 7/7 real (no slate),
   3840x2160 (THE 4K LAW), mean_volume -24.2 dB (GATE AUDIO pass on the
   first compile).
5. **GATE T (`type_check.py`) FAILED on the first pass** — B03 min-size
   §8.1: smallest text run measured 10px, below the 20px floor. Root
   cause: the condensed MATCHED/STEPPED/RETURNED row is drawn at
   font_size 15/15/14 and then scaled by 0.6x (`row.animate.scale(0.6)`)
   for the anchor-return composition — the post-scale pixel height fell
   under the floor. This defect exists unfixed in the `analyze` sibling's
   identical pattern too (its own type-check ran before B03.mp4 existed,
   so pixel checks silently SKIPped there and never caught it — confirmed
   by reading that sibling's TYPECHECK.md, which shows "no video / SKIP"
   for all GRAPHIC beats). Fixed here by bumping the three labels'
   pre-scale `font_size` to 30/30/28 and wrapping them in the existing
   `_fit_text` helper (caps width at 2.6 so the larger size can't overflow
   the 3.0-wide card); re-rendered B03 alone, recompiled with `--force`,
   re-ran GATE T: PASS, 0 FAILs.
6. Gate V (visual, manual): pulled 11 frames across the full 118.9s
   runtime (t=9.5, 20, 33, 45, 55, 65, 75, 85, 100, 108, 116) and read
   every one directly. B00's correction ("instinct" -> "the file") is
   fully typed and settled by t=9.5s of an 11.2s beat; B01's struck
   manager's-instinct figure and lit two-step procedure card read cleanly
   at both t=20 (mid-build) and t=33 (post-strike, "no numbers, no
   procedure" caption visible); B02's four-stop anchor (ASKED / MATCHED /
   STEPPED / RETURNED, the traveling "118% UTILIZATION" token) is legible
   at t=45 and lands on "hire one or cut one project" by t=55; B03's
   condensed anchor-return (t=65, mid-transition, confirms no overlap
   during the scale-down) and both-directions split (t=75, struck-through
   "TAILORED?" fully rendered and legible after the GATE T fix) read
   cleanly; BCRY's carry-out quote (t=85), BHTF's Your Turn composer card
   (t=100/108, confirmed `@HumanitariansAI`, command text not clipped),
   and BOUT's `OutroCTA` (t=116, confirmed `@HumanitariansAI`, no Claude
   mascot, correct title) all render legibly with no overlap, no
   clipping, no contrast issues. No defects found this pass. (OutroCTA
   renders on flat white rather than the humanitarians cream ground — a
   known shared-component quirk logged unfixed on every sibling reel in
   this factory, not a new defect.)
7. Audio presence: independently verified with `ffprobe` (h264 3840x2160
   video + aac audio stream present) and `ffmpeg -af volumedetect` on the
   final master -> mean_volume **-24.2 dB**, max -2.5 dB. Master mtime
   (1788398545) is newer than beat_sheet.json mtime (1788398166).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: FAIL -> fixed -> PASS (0 FAILs), second pass (B03 min-size fix)
- Gate V: PASS, first pass after the GATE T fix — no defects found
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max
  -2.5 dB
- ffprobe: duration 118.9s; mp4 mtime newer than beat_sheet.json mtime

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
`knowledge-work-plugins--claude-liam-capacity-plan.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors**, plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp knowledge-work-plugins--claude-liam-capacity-plan.mp4 \
   knowledge-work-plugins--claude-liam-capacity-plan-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/knowledge-work-plugins--claude-liam-capacity-plan/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-capacity-plan/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `1960d254`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
