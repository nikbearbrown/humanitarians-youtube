# BUILD-LOG — knowledge-work-plugins--claude-liam-daily-briefing

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-daily-briefing/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `daily-briefing`
sales Skill, already fully built — no SCRIPT.md in the source; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and body argument carried over unchanged: daily-briefing
is a single-file (SKILL.md, ~7k) Skill; Claude reads the file before it
works, then runs a linear Steps section (read SKILL.md, execute, return
output); it works standalone once the user tells Claude their meetings and
priorities in chat, and is supercharged once calendar/CRM/email are
connected so it reads them directly; the same input produces the same
briefing every run, and anything outside what the file specifies gets no
handling. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "REMEMBER" → "read" — the
newcomer's wrong guess that Claude has persistent memory of the user's day,
corrected toward the actual mechanism: the SKILL.md and whatever
input/connection is given are read fresh every time, never recalled).
Register re-registered Teardown → Plain: the source's B03 "design tell"
("Here is the Teardown moment...") and BVDT "verdict" beats were merged
into a single Plain-register B03 mechanism beat (the source's own B01
anatomy and B02 pipeline narration needed no rewrite at all — already
Plain, no judgment language to strip). Close re-skinned to
@HumanitariansAI, split into BOUT (OutroSeries, title restate) + BCTA
(OutroCTA, "…Liam, in for Bear." + handle) per this family's current
8-beat close convention (matches sibling `knowledge-work-plugins--claude-
liam-crm-cleanup`, built earlier the same day).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn +
BOUT outro). This redo is 8 beats: B00 (writer, replacing composer-ask
1:1) + B01 (anatomy, kept) + B02 (pipeline, kept) + B03 (design tell +
verdict merged, one mechanism beat) + BCRY (carry-out, new per CARRY-OUT
LAW) + BHTF (your turn, kept, made concretely paste-ready) + BOUT
(OutroSeries) + BCTA (OutroCTA) — the 7→8 delta is entirely the close
split, not new body content. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap. All 8 beats in this
redo are REMOTION, reusing registered patterns verbatim
(`BrutalistHesitantWriter`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `WantQuote`, `ClaudeComposerAsk`, `OutroSeries`,
`OutroCTA`) — no new component authoring, no Manim scaffold needed (GATE L
checked all 8 patterns RENDERABLE before slating; see `./art scenes
--check` output in this session).

Audio generated fresh (`generate_audio_kokoro.py`, all 8 beats, free/local,
`am_onyx`; B00 measured 10.6s on the first pass, clearing the >=9s TIMING
LAW window with no retune needed). Remotion rendering ran into heavy
resource contention from numerous long-running orphaned chrome-headless-
shell processes left by other factory workers on this shared machine (ps
showed 30+ such processes, several hours to days old) — two full-sheet
`remotion_scenes.py` invocations timed out (2min, then 10min) after
rendering only 6/8 beats progressively in the foreground; verified via
`ls media/` between attempts that no beat was lost or corrupted, then
finished the remaining BOUT/BCTA individually via `--only <beat>`, each of
which completed in well under a minute once run in isolation. All renders
were run and waited on in the foreground per COMPLETION LAW; nothing was
backgrounded.

`type_check.py`: **PASS, 0 FAILs** on first run (all beats §8.10 SKIP —
no wordy-card/pull-quote content over the checked thresholds). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-daily-briefing.mp4`, 8/8 beats
filled real (no slate), 75.4s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW). Motion histogram: remotion 8/8 (100%) — flagged by compile.py's
~40% pantry-cap warning; accepted per this family's standing precedent
(file/pipeline/scope skill-explainer reels have no illustrative-figure
content to carry a second visual language, matching every
`knowledge-work-plugins--claude-liam-*` sibling built this session).

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (compile.py + independently
  re-verified via `ffmpeg volumedetect`), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 75.4s; mp4
  mtime (1788447314) newer than beat_sheet.json mtime (1788447141)
- B00 TIMING LAW: frame-verified — "REMEMBER" doomed in terracotta at
  t≈1.8s, full corrected question ("Does Claude read my meetings for a
  briefing?") settled and legible by t≈8.5s, well inside the 10.6s clip
- Gate V (visual): pulled frames across the full runtime (B00, B01, B02,
  B03, BCRY, BHTF, BOUT, BCTA) plus the B00 early/mid/late sequence — all
  8 beats legible, correctly labeled, no overlap, no truncation. No
  blockers.

Metadata file written: `knowledge-work-plugins--claude-liam-daily-briefing.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" — no fallback
needed. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
