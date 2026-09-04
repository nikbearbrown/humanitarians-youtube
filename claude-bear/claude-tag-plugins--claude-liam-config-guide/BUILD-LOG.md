# BUILD-LOG — claude-tag-plugins--claude-liam-config-guide

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-config-guide/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the `config-guide` Skill, already
fully built — no SCRIPT.md; source `beats[*].narration_text` plus
PEDAGOGY.md served as the locked script). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: Claude's
configuration model has four layered objects (agents, agent scopes,
identity profiles, presets/connections/repos/instructions); the
config-guide skill is an index that routes a question to one of five
reference files (agents-and-scopes, identity-profiles,
connections-and-presets, github-and-instructions, best-practices); the
guide is currently scoped to the Slack surface only; after explaining, it
always suggests debug-plugins in a brand-new Slack thread, because a new
thread gets a fresh container reflecting current config, not cached
state; and the concrete risk the source's teardown surfaced — the index
fails silently (no error, no fallback) if a reference file is missing.
B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "file" → "layer" — the newcomer's
wrong guess that Claude's settings live in one file, corrected toward the
actual four-layer model). Register re-registered Teardown→Plain: the
source's B05 "gets it right / where it bites" list was compressed to the
single most teachable, general-audience fact (the silent-failure risk)
rather than kept as a full strengths/gaps inventory — the source's other
gaps (no admin-permissions guidance, the topic table not being
self-describing) were dropped as assuming an admin/technical audience
simple/hai-simple doesn't target, not as a verdict on the skill's quality;
the source's "new thread reason unexplained" gap is in fact answered
in-reel at NB02 (container isolation), so it was not re-listed as a gap.
BVDT's verdict facts were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT
folded into BCRY; BHTF kept, with the source's admin-only, Slack-workspace-
specific instructions ("ask how agents and agent scopes work in @Claude")
replaced by a concrete, paste-ready prompt that needs no @Claude admin
access, so it's actually runnable by any viewer today; BOUT kept. Full
audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ConfigGuideAnatomy` / `ConfigGuideDesign` / `ConfigGuideTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 4
labeled chips + optional arrows/accent/strike + caption) copied verbatim
from the `claude-plugins-official--claude-liam-access` sibling. B00
hesitant-writer correction ("file" → "layer") verified on screen by
direct frame pulls: "file" typed and fully visible in terracotta (about
to be deleted) at t≈1.5–2.5s, erased and mid-replacement ("Where's the
layer\nwith|") by t≈4.5s, settled correct text "Where's the layer with
Claude's settings?" — full clip 11.0s (≥8s TIMING LAW window met).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; the invocation exceeded the tool's 120s timeout and was
moved to background by the harness automatically — blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule); NB01–NB03 rendered via `render_scenes.py`. First `type_check.py`
pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB02** — smallest text run 19px < floor 20px. Frame
  pull showed the cause: the accented chip's BOLD weight ("Slack only")
  rendered wider than its plain-weight neighbors of the same nominal
  length bucket, forcing extra scale-down under the min-size floor.
  Diagnosed by direct visual inspection (pulled a frame from
  `manim/NB02.mp4`), not just the log message. Fixed two ways: shortened
  the first chip label from "5 short files" to "index of 5" (removing an
  unrelated width contributor) and moved the accent from chip index 1
  ("Slack only") to chip index 2 ("new thread") — the bold-weight
  width-inflation problem only bites the accented chip, so moving it onto
  a shorter label ("new thread", same 10 chars as its now-plain neighbor)
  cleared the floor. Also better matches the narration/caption's actual
  emphasis (the new-thread requirement). Re-rendered NB02 only
  (NB01/NB03 untouched); `beat_sheet.json`'s
  `graphic.production_viz.chips`/`accent` for NB02 synced to match before
  recompile, per COMPLETION LAW (no post-compile sheet edits — this fix
  was applied and NB02 re-rendered before the first compile attempt).

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-tag-plugins--claude-liam-config-guide.mp4`, 7/7 beats
filled real (no slate), 109.2s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe (self-verified, not just trusted from compile.py's log): video
  3840×2160 h264, audio (aac) present, duration 109.2s; mp4 mtime
  (1788195531) newer than beat_sheet.json mtime (1788195389)
- Gate V (visual): pulled frames every 8s across the full runtime plus
  targeted checks of B00 (t≈1.5–2.5s "file" doomed in terracotta, t≈4.5s
  mid-correction "Where's the layer / with|", settled correct by end),
  NB01 (four chips + arrows + caption legible), NB02 (post-fix: all three
  chips legible and parallel-sized, "new thread" accent underline clean),
  NB03 (three chips legible, "no answer" accent), BCRY (carry-out sentence
  and sparkLine footer read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, paste-ready prompt text legible), and BOUT
  (OutroSeries: correct eyebrow "CLAUDE CONFIG GUIDE · @HumanitariansAI",
  correct title restate, crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.0s (≥8s requirement met); the
  "file" → "layer" correction lands on screen by t≈4.5s, well inside the
  clip.

Metadata file written: `claude-tag-plugins--claude-liam-config-guide.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-tag-plugins`) does NOT
match any map prefix by `str.startswith` (it is not a prefix of
`"claude-plugins"`, `"claude-code"`, or any other key — verified
programmatically, not by inspection alone), so resolution fell through to
the `hai-simple` skill-key entry, which resolves to "Claude Basics" —
same fallback used on siblings whose family string matches no map prefix
(e.g. `claude-for-legal`). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
