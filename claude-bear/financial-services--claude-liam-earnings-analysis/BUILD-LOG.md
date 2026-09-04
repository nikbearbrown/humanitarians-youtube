# BUILD-LOG — financial-services--claude-liam-earnings-analysis

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-earnings-analysis/beat_sheet.json`
(a Teardown skill-explainer for the `earnings-analysis` Anthropic Agent
Skill, already fully built, no separate SCRIPT.md — the source
`beats[*].narration_text` served as the locked script). Question, facts,
and full argument carried over unchanged: a skill is a folder Claude reads
before it acts (SKILL.md, plain-language instructions, no hidden code);
the instructions live in a Steps section executed in order, linear, no
branching unless a step calls for it; this specific skill's fixed scope
(turn a company's quarterly numbers into an 8-12 page, 3,000-5,000 word
earnings update with 1-3 summary tables and 8-12 charts); and the
practical your-turn prompt to ask Claude to plan before running a skill.
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "trained" -> "briefed" — the
newcomer's wrong guess that specialized output means Claude was trained or
fine-tuned, corrected to the reel's real subject: a file Claude reads).
Register re-registered Teardown -> Plain: the source's B01/B02 (anatomy,
pipeline) were already close to descriptive/mechanical, so the main
register work was on the source's B03 ("design tell") and BVDT
("verdict") — both carried explicit Teardown trade-off/judgment language
("what it gets right... what it bites", "know the limit") that Plain
restates as a fact about scope (NB03) and a single carry-out sentence
(BCRY, `WantQuote`) instead of a bulleted verdict recap.

Source is a compact 7-beat skill-explainer with no planted anchor scenario
and no claim requiring both failure directions (unlike the deeper
`books--claude-liam-what-plugins-are` redo, which inherited those moves
from its deep-explainer source). Per the redo contract — question, facts,
argument, and beat count locked to the source — no anchor or
both-directions beat was invented; SCRIPT.md's six-move audit logs both as
N/A rather than fabricating structure the source never had, the same
honesty pattern the `what-plugins-are` redo used for its one-flag audit.
Beat count: source 7 (B00, B01, B02, B03, BVDT, BHTF, BOUT) -> this redo 7
(B00, NB01, NB02, NB03, BCRY, BHTF, BOUT). No beat dropped, merged, or
added. No source beat was `ai-video-prompt`, pantry, or a human-drop slot —
the source's B00 was already `ClaudeComposerAsk` (Remotion) and every
other beat was already Remotion (`SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeComposerAsk`, `ClaudeTitleOutro`) — NO-GENAI/NO-PANTRY LAW required
no substitution beyond B00, which WRITER LAW replaces regardless.

The 3 GRAPHIC beats (NB01-NB03) reused the same generic "chip row" Manim
template as the `books--claude-liam-*` hai-simple siblings (`scenes.py` /
`render_scenes.py`: one title + labeled chips + optional arrows/accent +
caption, parametrized per beat from `BEAT_CONTENT`), same humanitarians
palette (ground `#F3EBDD` / ink `#2F2A26` / accent `#E4572E`), same
accent/struck/no-stroke conventions documented inline against GATE T's
known false-positive classes for this template. B00 hesitant-writer
correction ("trained" -> "briefed") verified on screen: full corrected
question "Does Claude need to be briefed for earnings analysis?" legible
at t≈6s in the pulled frames, clip duration 10.45s (>=8s TIMING LAW window
met with `lead_silence_s: 0.8`).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; the Remotion render and a media-presence poll each exceeded
the shell's 120s default and were moved to the harness's background-task
tracking — per COMPLETION LAW's one-shot-invocation rule, blocked on both
synchronously with an explicit long-timeout foreground command rather than
ending the turn, so nothing was left orphaned); all 3 GRAPHIC beats
rendered via `render_scenes.py` (foreground, completed well under the
timeout). `type_check.py` (GATE T): PASS, 0 FAILs, first pass (§8.10 SKIP
on all 7 beats, no wordy-card/min-size/overflow/contrast/kerning
violations). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-earnings-analysis.mp4`, 7/7 beats
filled real (no slate), 77.0s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 77.0s/77.06s;
  mp4 mtime newer than beat_sheet.json mtime
- Gate V (visual): pulled 13 frames at 6s spacing across the full runtime
  and read each directly — legible everywhere, safe inset respected, no
  text overlap, @HumanitariansAI handle correct on B00/BHTF/BOUT, one
  terracotta accent per GRAPHIC beat, WantQuote carry-out fully legible.
  One frame (t≈48s) landed mid-typing on BHTF's composer animation ("I
  wan") — a normal in-between frame during the type-on effect, not a
  defect (confirmed by the next frame showing the full prompt cleanly
  typed).
- B00 TIMING LAW: `actual_duration_s` 10.45s (>=8s requirement met); the
  "trained" -> "briefed" correction lands fully on screen well before the
  beat ends.

**Motion histogram:** graphic:3 remotion:4 — no non-blocking warning this
build (compile.py logged none); the ratio follows this source's small
7-beat count the same way the deeper `what-plugins-are` redo's ratio
followed its 18-beat count.

Metadata file written: `financial-services--claude-liam-earnings-
analysis.md` (channel @HumanitariansAI, **Playlist: Claude Basics**). Per
playlists.json, SUBJECT.json's family ("financial-services") matches no
map prefix, so it falls through to the `hai-simple` skill-key fallback —
the same resolution every other `financial-services--*` sibling in
HAILOOP-LOG.md has logged (dd-checklist, dd-meeting-prep, deal-screening,
deal-sourcing, deal-tracker, deck-refresh, …), including several that are
also skill-teardown explainers of an Anthropic Skill's generic mechanism,
exactly like this one. An earlier draft of this build reasoned toward
"Extending Claude — Skills, Plugins & Connectors" by analogy to the
`books--claude-liam-what-plugins-are` redo's content-matching precedent —
but that precedent was logged for the `books` family specifically, and
every actual `financial-services` sibling consistently uses the mechanical
fallback instead. Corrected to match family convention before delivery.
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-earnings-analysis-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-earnings-analysis/` (4K
master + description) for the Drive sync. Committed text artifacts (no
mp3/mp4) to the `humanitarians-youtube` clone under
`claude-bear/financial-services--claude-liam-earnings-analysis/`,
committed (`cc0771c5`) and pushed clean.

**Playlist correction:** the initial delivery used "Extending Claude —
Skills, Plugins & Connectors" by analogy to the `books--claude-liam-what-
plugins-are` redo's content-matching precedent. Checking HAILOOP-LOG.md
against every actual `financial-services--*` sibling delivered so far
(dd-checklist, dd-meeting-prep, deal-screening, deal-sourcing,
deal-tracker, deck-refresh) showed all of them — including several that
are themselves skill-teardown explainers of an Anthropic Skill's generic
mechanism, same as this reel — consistently resolve to **Claude Basics**
via the `hai-simple` skill-key fallback, since the `financial-services`
family matches no playlists.json map prefix. The `books`-family precedent
does not extend to `financial-services`. Corrected `metadata.playlist` to
"Claude Basics" in `beat_sheet.json` and the `.md` description,
recompiled (`compile.py --force` — identical 77.0s/3840x2160/7-beat
output, GATE AUDIO -24.2 dB unchanged, GATE T re-confirmed PASS 0 FAILs),
regenerated the `-4k.mp4` copy (the stale one was auto-purged by
compile.py's QC stale-purge since it predated the recompile), and pushed a
second commit (`e901bb9f`) with the corrected files — never `--amend`, per
the same never-amend pattern already logged on the `deal-screening` and
`deck-refresh` siblings' post-push BUILD-LOG syncs.

**Status: DELIVERED.**
