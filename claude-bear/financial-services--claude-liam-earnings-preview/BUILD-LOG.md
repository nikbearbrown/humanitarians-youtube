# BUILD-LOG — financial-services--claude-liam-earnings-preview

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-earnings-preview/beat_sheet.json`
(a Teardown skill-explainer for the `earnings-preview` Anthropic Agent
Skill, already fully built, no separate SCRIPT.md — the source
`beats[*].narration_text` served as the locked script). Question, facts,
and full argument carried over unchanged: a skill is a folder Claude reads
before it acts (SKILL.md, plain-language instructions, no hidden code);
the instructions live in a Steps section executed in order, linear, no
branching unless a step calls for it; this specific skill's fixed scope
(build pre-earnings analysis with estimate models, scenario frameworks,
and key metrics to watch); and the practical your-turn prompt to ask
Claude to plan before running a skill.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "predict" -> "preview" — the
newcomer's wrong guess that an earnings-preview skill forecasts the actual
reported number, corrected to the reel's real subject: a skill that builds
scenarios and a watchlist, not a prediction). This wrong guess is specific
to this skill's name/content, distinct from the "trained" -> "briefed"
wrong guess used on the `earnings-analysis` sibling, since each redo's
naive framing is drawn from its own source content rather than copied
across siblings.

Register re-registered Teardown -> Plain: the source's B01/B02 (anatomy,
pipeline) were already close to descriptive/mechanical and ported with
only the skill name changed. The main register work was on the source's
B03 ("design tell") and BVDT ("verdict") — both carried explicit Teardown
trade-off/judgment language ("what it gets right... what it bites", "know
the limit") that Plain restates as a fact about scope (NB03: estimate
models, bull/bear scenarios, metrics to watch — "that's the whole brief")
and a single carry-out sentence (BCRY, `WantQuote`) instead of a bulleted
verdict recap. NB03 also directly falsifies B00's "predict" wrong guess by
stating the skill's actual scope brackets an outcome (scenarios) rather
than forecasting one.

Source is a compact 7-beat skill-explainer with no planted anchor scenario
and no claim requiring both failure directions (same shape as the
`earnings-analysis` sibling). Per the redo contract — question, facts,
argument, and beat count locked to the source — no anchor or
both-directions beat was invented; SCRIPT.md's six-move audit logs both as
N/A rather than fabricating structure the source never had. Beat count:
source 7 (B00, B01, B02, B03, BVDT, BHTF, BOUT) -> this redo 7 (B00, NB01,
NB02, NB03, BCRY, BHTF, BOUT). No beat dropped, merged, or added. No
source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's B00 was already `ClaudeComposerAsk` (Remotion) and every other
beat was already Remotion (`SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`,
`ClaudeTitleOutro`) — NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00, which WRITER LAW replaces regardless.

The 3 GRAPHIC beats (NB01-NB03) reused the same generic "chip row" Manim
template as the `financial-services--claude-liam-earnings-analysis`
sibling (`scenes.py` / `render_scenes.py`: one title + labeled chips +
optional arrows/accent + caption, parametrized per beat from
`BEAT_CONTENT`), same humanitarians palette (ground `#F3EBDD` / ink
`#2F2A26` / accent `#E4572E`), same accent/struck/no-stroke conventions
documented inline against GATE T's known false-positive classes for this
template — no new defect classes encountered.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, first pass, no retries): B00 9.30s, NB01 11.26s, NB02 8.28s,
NB03 12.61s, BCRY 8.70s, BHTF 17.54s, BOUT 5.29s. B00's 9.30s clears the
>=9s TIMING LAW window (30-word narration + `lead_silence_s: 0.8`); frame
pulls at t=2s/4s (f01/f02 of the Gate V sweep) confirmed the "predict" ->
"preview" correction lands and settles well before the beat ends.

`render_scenes.py` (3 GRAPHIC beats, Manim, foreground) completed clean,
first pass, no retries, well under the shell's timeout.
`remotion_scenes.py` (4 REMOTION beats: B00, BCRY, BHTF, BOUT) exceeded the
Bash tool's 120s default and was auto-moved to a background task by the
harness; per COMPLETION LAW's one-shot-invocation rule, blocked on it
synchronously via `TaskOutput(block=true)` rather than ending the turn, so
nothing was left orphaned — confirmed exit 0 and all 4 media files present
before compiling.

`type_check.py` (GATE T): PASS, 0 FAILs, first pass (all 7 beats §8.10
SKIP, no wordy-card/min-size/overflow/contrast/kerning violations).
Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-earnings-preview.mp4`, 7/7 beats
filled real (no slate), 74.0s, 3840x2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio (aac) present, duration
  73.981s/74.0s; mp4 mtime (1788293349) newer than beat_sheet.json mtime
  (1788293281)
- Gate V (visual): pulled 16 frames at ~4.5s spacing across the full
  73.98s runtime and read each directly — legible everywhere, safe inset
  respected, no text overlap, @HumanitariansAI handle correct on
  B00/BHTF/BOUT, one terracotta accent per GRAPHIC beat, WantQuote
  carry-out fully legible, BOUT subscribe CTA and title restate correct.
  Two frames (one on NB03's title fade-in, one on BHTF's composer
  type-on animation) landed mid-transition — normal in-between frames
  during a fade/type effect, not defects (confirmed by adjacent frames
  showing the settled state cleanly).
- B00 TIMING LAW: `actual_duration_s` 9.30s (>=9s window met via 30-word
  narration + `lead_silence_s: 0.8`); the "predict" -> "preview"
  correction lands fully on screen well before the beat ends (settled by
  f02, ~t=4s of 9.3s).

**Motion histogram:** graphic:3 remotion:4 — no non-blocking warning this
build (compile.py logged none); ratio follows this source's small 7-beat
count, same as the `earnings-analysis` sibling.

Metadata file written: `financial-services--claude-liam-earnings-
preview.md` (channel @HumanitariansAI, **Playlist: Claude Basics**). Per
playlists.json, SUBJECT.json's family ("financial-services") matches no
map prefix, so it falls through to the `hai-simple` skill-key fallback —
the same resolution every other `financial-services--*` sibling in
HAILOOP-LOG.md has logged (dd-checklist, dd-meeting-prep, deal-screening,
deal-sourcing, deal-tracker, deck-refresh, earnings-analysis, …),
including several that are also skill-teardown explainers of an Anthropic
Skill's generic mechanism, exactly like this one. Applied that convention
directly this time rather than re-deriving it, since the
`earnings-analysis` sibling's BUILD-LOG already documents the correction
from an earlier, wrong analogy attempt. Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-earnings-preview-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-earnings-preview/` (4K
master + description) for the Drive sync. Committed text artifacts (no
mp3/mp4) to the `humanitarians-youtube` clone under
`claude-bear/financial-services--claude-liam-earnings-preview/`, committed
(`16cab5cc`) and pushed clean — no repo `git pull --rebase` quirk this
time (unlike a couple of earlier siblings' logs).

**Status: DELIVERED.**
