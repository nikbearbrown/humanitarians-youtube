# BUILD-LOG — claude-plugins-official--claude-liam-project-artifact

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-project-artifact/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `project-artifact`
Claude Code plugin Skill — tabbed HTML status pages published via Claude's
Artifact tool — already fully built, no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: two tabs
(Overview, Workstreams) are always present; five (Attention, Background,
Plan, Risks and open questions, Decisions/FAQ) are conditional on config
content; the config file has four sections (Project, Artifact, Sources,
People); every publish embeds a JSON state block for delta computation on
refresh; and a refresh only computes a delta if the previous render's state
block is still on disk — otherwise it rebuilds from template with no change
summary. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open
with `BrutalistHesitantWriter` (WRITER LAW: "watches"/"itself" → "waits
for"/"when I ask" — two positionally-matched corrections in one beat,
landing the newcomer's actual wrong guess that a project status page keeps
itself current by watching your data, corrected toward the actual
mechanism: it waits, and updates only on request). Register re-registered
Teardown→Plain: the source's B05 "gets it right / where it bites" list (five
strengths, five gaps including claude.ai-login requirement, machine-local
config, and pattern-based injection flagging) was compressed to the single
most teachable, general-audience fact (the delta-requires-prior-render-on-
disk mechanism) rather than kept as a full strengths/gaps inventory — the
Claude-harness/security-internals gaps in the source were dropped as
assuming a technical or security-reviewer audience simple/hai-simple doesn't
target, not as a verdict on the skill's quality. BVDT's verdict facts were
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; source
B01's two halves (tab catalog, config structure) split across NB01/NB02;
source B02's four patterns compressed — "gather sources first" folded into
NB02, "delta vs. re-narrative on refresh" folded into NB03, and the two
patterns aimed at a technical builder audience dropped; B05's long list
compressed into NB03 (the one fact a general viewer needs and can act on);
BVDT folded into BCRY; BHTF kept, with the source's prompt trimmed to a
single concrete worked example; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ProjectArtifactAnatomy` / `ProjectArtifactDesign` / `ProjectArtifactTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with project-artifact-specific labels.

**B00 TIMING LAW** — text "My project page / watches my data / and updates /
itself?" with two positionally-matched trigger/replacement pairs
(`triggerWords: "watches, itself"` / `replacementWords: "waits for, when I
ask"`), narration 33 words + `lead_silence_s: 0.8`. Audio measured 10.50s —
first render, no retry needed. Verified by frame pulls at t=2.2s ("watches"
doomed in terracotta, mid-correction), t=4.5s (both corrections settled:
"My project page / waits for my data / and updates / when I ask?" fully
legible), and t=9.8s (question still held, unchanged) — well past the ≥8s
TIMING LAW floor.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (the tool
auto-backgrounded past its 120s default timeout; blocked on it via
`TaskOutput` with a 590s budget before proceeding, per the COMPLETION LAW's
foreground-render rule — never treated the backgrounded render as "handled"
without waiting on its exit code); NB01–NB03 rendered via `render_scenes.py`
(completed inside the foreground timeout, no backgrounding).

First `type_check.py` pass was **FAIL, 1 defect** (NB01), which took five
iterations to root-cause and fix — not a QC-sampling rubber stamp:

1. **min-size + bbox-overlap, chip0 "Overview + Workstreams" (22 chars) and
   title "TWO ALWAYS, FIVE THAT EARN IT" (29 chars):** smallest text run
   18px < 20px floor, plus a 21% bbox overlap in the title region. Shortened
   the title to "TWO TABS, ALWAYS ON" (19 chars) and chip0 to "2 tabs,
   always" — bbox-overlap cleared, min-size dropped to 19px (still FAIL).
2. **min-size persisted at 19px** after also shortening chip1 ("5
   conditional tabs" → "5 conditional"). Diagnosed via direct pixel crop of
   the accented chip2 ("content decides") at 3x zoom: the bold serif render
   showed "eamsit" instead of "earns it" when tried as a replacement label —
   'r' and 'n' had visually merged into what reads as 'm', a real bold-serif
   kerning collision (the classic "rn"→"m" illusion), not a GATE T false
   positive. Avoided entirely by using single-word chip labels going
   forward (no risk of inter-word space collapse or cross-word letter
   collision at BOLD weight).
3. **min-size still 19px** with chip2 = "if present" (space visibly
   collapsed between "if" and "present" at BOLD weight — legible but tight)
   and again with chip2 = "included" (clean single word, no collapse) —
   confirming chip2 was never the actual bottleneck; two different chip2
   texts produced the identical 19px reading.
4. **Root-caused via direct diagnostic**: imported `type_check.py`'s own
   `text_run_bboxes`/`labeled_blobs` functions against a saved frame and
   printed every candidate text-run bbox sorted by height. The smallest
   (h=19px) mapped to a bbox inside chip0, at the exact pixel region of the
   isolated "a" in "always" — a plain x-height letter, disconnected from its
   neighbors by EB Garamond's letterform spacing at this size, forming its
   own tiny connected-component blob independent of the rest of the word.
   Shortening chip0 further ("2 tabs, always" → "2, always") did not help:
   re-running the same diagnostic on the new render found the identical
   "al" blob at the same 19px height in the same screen region — the "a" is
   inherently ~19px tall at the sibling's original 26/22/18 font-size tiers
   for NORMAL (non-bold) weight text at this resolution, 1px under the
   20px floor, regardless of which word contains it.
5. **Fix**: bumped the shared `_chip()` function's font-size tiers in this
   reel's `scenes.py` from 26/22/18 to 30/26/22 (+4 across all three
   buckets) — comfortable headroom for any lone x-height glyph without
   changing which length bucket a label falls into. Re-rendered NB01;
   `type_check.py` went **FAIL → PASS, 0 FAILs** on the next run. Final
   NB01 chips: `["2, always", "5 conditional", "included"]`.

`beat_sheet.json`'s `graphic.production_viz.label`/`chips` for NB01 were
synced to the final wording directly at each step (not via a full
`build_beat_sheet.py` re-run, which would have discarded the already-measured
audio durations and render stamps), per COMPLETION LAW. `build_beat_sheet.py`
and `scenes.py` were both kept in sync with the shipped content for future
regen.

Recompiled after the fix:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-project-artifact.mp4`, 7/7
beats filled real (no slate), 121.8s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see the 5-iteration NB01 defect chain above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 121.75s; mp4
  mtime (1788173035) newer than beat_sheet.json mtime (1788172757)
- Gate V (visual): pulled frames across the full runtime (t=15/40/65/95/
  105/118/120s) plus targeted B00 checks (t=2.2/4.5/9.8s). B00: both
  corrections land and the full corrected question holds to the end of the
  10.5s clip. NB01 (post-fix): "2, always" / "5 conditional" / "included"
  all legible, well-spaced, no overlap. NB02: "config.md" / "4 sections" /
  "stored state block" clean. NB03: "you ask" / "stored block found" /
  "delta, not rebuild" clean. BCRY: carry-out sentence + sparkline read
  clean. BHTF: correct topic/title/@HumanitariansAI handle, paste-ready
  prompt text legible. BOUT (OutroSeries): correct eyebrow "PROJECT
  ARTIFACT · @HumanitariansAI", correct title restate "Snapshot, Not
  Sensor.", crimson underline, no truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.5s (≥8s requirement met); both
  corrections ("watches"→"waits for", "itself"→"when I ask") land on screen
  well before mid-clip and the full corrected question stays legible for
  the remainder.

Metadata file written: `claude-plugins-official--claude-liam-project-artifact.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors" — a more specific match than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with the
`claude-plugins-official--claude-liam-agent-development` sibling built in
this same family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
