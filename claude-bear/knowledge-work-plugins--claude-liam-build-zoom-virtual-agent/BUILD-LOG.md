# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-virtual-agent

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-virtual-agent/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-virtual-agent` Anthropic skill — a reference skill for Zoom
Virtual Agent). This invocation started from a bare `SUBJECT.json` (no prior-
pass artifacts) and built the reel end to end.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill ("what it gets right… what it bites")
and framed a "Verdict" card; this redo states the same five-item scope
boundary as fact (no grading language) and folds the verdict into a
`WantQuote` carry-out beat. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "be" -> "build" — the
newcomer assumption that Claude itself personally becomes the conversational
agent that chats with customers, corrected to Claude building the
integration code around Zoom's own Virtual Agent product). Close re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt was
rewritten clean — the source's handoff string was truncated/garbled ("...use
after routing to a virtual-agent wor. Read the build-zoom-virtual-agent
skill...") and referenced a skill file the general viewer won't have
installed; this version asks Claude directly to walk through the web embed /
mobile wrapper / knowledge-base sync pieces, no plugin dependency. Built
from the nearest structural precedent in this exact family
(`knowledge-work-plugins--claude-liam-build-zoom-contact-center-app` —
identical 8-item anatomy file list and a five-item scope constraint),
matching its conventions exactly; the anatomy/pipeline facts (a skill is a
folder Claude reads; execution is linear: read, execute steps in order,
return result) are generic across both Zoom skills, so B01/B02's narration
and Manim scenes were reused verbatim, only B03's five scope items rewritten
for this skill (web embeds, Android/iOS wrapper, knowledge-base sync,
lifecycle handling, troubleshooting vs. the sibling's app/web/native
integrations, engagement/state, campaigns, callbacks, version-drift).

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so no substitution was required beyond the WRITER LAW
and channel-skin row hai-simple already mandates.

## Built end to end this invocation

1. Read the source sheet + narration in full (locked facts:
   build-zoom-virtual-agent is a *reference* skill for Zoom Virtual Agent;
   used after routing to a virtual-agent workflow for web embeds, Android or
   iOS wrapper integrations, knowledge-base sync, lifecycle handling, or
   troubleshooting; a skill = a folder Claude reads before acting, 8 items —
   RUNBOOK.md, SKILL.md, android/, concepts/, ios/, references/, scenarios/,
   troubleshooting/; execution is linear — read SKILL.md, execute steps in
   order, return result). Read the structure template
   (`claude-liam-simple-delve`) and the nearest built precedent in this
   exact family (`knowledge-work-plugins--claude-liam-build-zoom-contact-center-app`,
   identical anatomy and scope-constraint shape) to match conventions
   exactly.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Step 0):
   carry-out line is "Build Zoom Virtual Agent doesn't hand you an AI that
   talks to your customers — it makes Claude build the integration…fitted
   around Zoom's own Virtual Agent product," defeating the wrong guess that
   "virtual agent" means a conversational AI Claude itself becomes.
3. Authored `SCRIPT.md` (Plain register, 7 beats matching the source's beat
   count) and `beat_sheet.json` — B00 `BrutalistHesitantWriter`
   (humanitarians palette, trigger "be" -> replacement "build", 29-word
   narration + `lead_silence_s` 0.8 per TIMING LAW), B01/B02/B03 as
   GRAPHIC/Manim (anatomy, pipeline, five-item scope constraint), BCRY
   `WantQuote` carry-out, BHTF `ClaudeComposerAsk` your-turn with a freshly
   written runnable prompt, BOUT `OutroCTA`. Confirmed via
   `./art scenes --check` that `BrutalistHesitantWriter`, `ClaudeComposerAsk`,
   `WantQuote`, and `OutroCTA` are all RENDERABLE before slating (GATE L).
4. Wrote `scenes.py`: B01Scene and B02Scene copied verbatim from the
   `build-zoom-contact-center-app` precedent (facts are identical between
   both Zoom skills — an 8-item anatomy and a 3-phase linear pipeline, and
   neither scene's on-screen text references the specific skill name).
   B03Scene rewritten fresh for this skill's five scope items (web embeds,
   Android/iOS wrapper integrations, knowledge-base sync, lifecycle
   handling, troubleshooting). `render_scenes.py` copied unchanged.
5. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`.
   Measured durations became the clock: B00 13.25s, B01 15.02s, B02 9.34s,
   B03 18.09s, BCRY 15.06s, BHTF 16.41s, BOUT 6.27s.
6. Rendered the three Manim beats via `render_scenes.py` in the foreground —
   all 3 ok on first attempt.
7. Rendered the four Remotion beats via `remotion_scenes.py` — exceeded the
   tool's 120s timeout and was moved to background by the harness
   automatically; blocked on it via `TaskOutput` (block=true) before
   proceeding, per the one-shot COMPLETION LAW's foreground-render rule,
   confirmed exit code 0 with all four beats reporting `ok` (B00 extended to
   13.2s, BCRY to 15.1s, BHTF to 16.4s, BOUT to 6.3s).
8. Verified B00 directly before compiling: pulled frames at t=0.8/1.2/1.6/
   2.0/2.4/2.8/3.0/12.5s — "be" types in terracotta by t=1.2s, resolves to
   "build" in ink by t=2.8s, full corrected question "Does Claude build my
   Zoom virtual agent?" legible at t=12.5s, well inside the 13.27s clip.
   `ffprobe` confirms `media/B00.mp4` = 13.27s with video + audio streams,
   clearing the >=8s TIMING LAW floor.
9. `compile.py` pass -> 7/7 real (no slate), 94.4s, native 4K (3840x2160)
   via the 4K LAW. content-check/frame-check/lane-check all PASS. B03's
   19.7s Manim clip was center-cropped 0.8s head/tail to match its 18.09s
   narration track (normal `compile.py` behavior, not a defect). GATE AUDIO
   PASS mean_volume -24.0 dB.
10. **GATE T (`type_check.py`): PASS on first run, 0 FAILs** — no fixes
    needed (the reused anatomy/pipeline scenes and the fresh B03Scene all
    cleared min-size/kerning/bbox checks cleanly).
11. **Gate V (frame QC): full beat sweep, all 7 beats read directly** — B01
    (anatomy), B02 (pipeline), B03 (five-item scope), BCRY (carry-out),
    BHTF (your-turn prompt), BOUT (outro) all legible, safe inset, no text
    overlap, correct topic/title/`@HumanitariansAI` throughout. Two
    already-logged shared-component quirks present (not new defects, not
    fixed here, consistent with every sibling in this factory):
    BOUT/`OutroCTA` renders on flat white rather than the humanitarians
    cream ground; BHTF/`ClaudeComposerAsk` shows the component's default
    "Fable 5 / High" model label since it wasn't overridden. First sweep
    clean — no re-render needed.
12. Final master verified directly, independent of `compile.py`'s
    self-report: `ffprobe` confirms one video stream (3840x2160, matches
    4K LAW) + one audio stream, 94.46s; `ffmpeg -af volumedetect` confirms
    mean_volume -24.0 dB / max -2.7 dB; `[ -nt ]` confirms the `.mp4` is
    newer than `beat_sheet.json` — all COMPLETION LAW conditions met.

## Gates

- **TIMING LAW (B00):** narration 29 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **13.25s** (compiled 13.2s), clears the
  >=9s floor comfortably. Correction ("be" -> "build") visible on-screen by
  t=2.8s, full corrected question legible by t=12.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS on first run, 0 FAILs.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly, zero
  new defects (two already-logged shared-component quirks, unfixed on
  every sibling in this factory — see above).
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffmpeg`/`ffprobe`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was needed
— copied directly to
`knowledge-work-plugins--claude-liam-build-zoom-virtual-agent-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-build-zoom-virtual-agent/`
(4K master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-build-zoom-virtual-agent/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
