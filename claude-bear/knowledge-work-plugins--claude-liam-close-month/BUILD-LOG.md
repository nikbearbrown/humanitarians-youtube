# BUILD-LOG — knowledge-work-plugins--claude-liam-close-month

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-close-month/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `close-month` Claude
skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: close-month
is a folder Claude reads before it acts; its SKILL.md is the instruction
set; the pipeline is four fixed steps in order — reconcile QuickBooks
against payment processors, flag anything that doesn't match, write a
plain-language P&L narrative, export the close packet; run twice on the
same numbers it does the same four steps both times (same input, same
output); and the concrete edge of that design — it only does what those
steps say, nothing the file doesn't cover. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "judgment" → "a skill file" — the newcomer's wrong guess that
Claude closes the books using its own accounting judgment, corrected toward
the actual mechanism: a written file it follows step by step). Register
re-registered Teardown→Plain: the source's B03 "gets it right / where it
bites" design-tell language and BVDT's separate verdict artifact were merged
into a single plain mechanism-and-consequence beat (NB03) plus the BCRY
carry-out, dropping the Teardown framing per the NO JUDGMENT register check.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03 + BVDT compressed into NB03 (the one fact a general
viewer needs and can act on: same input/same output reliability paired with
its scope limit); BHTF kept, with the source's your-turn prompt cleaned up
from a truncated metadata-concatenation string into a complete, paste-ready
sentence (the underlying ask — reconcile, flag, write, export, narrate the
plan first — is unchanged); BOUT kept. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with close-month-specific labels.

**B00 TIMING LAW — calibrated from the start, no failed first render.**
Applied the timing rates already proven on the `agent-development` sibling
(charMs=42, mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26)
rather than the slower defaults that caused that sibling's first-attempt
timeout. Text: "Can Claude / close my books / using / judgment?" (3
newlines, single trigger word "judgment" → replacement "a skill file").
Rendered clean on the first attempt: `actual_duration_s` 10.24s (audio) +
`lead_silence_s` 0.8 = 11.04s window, well past the ≥9s TIMING LAW floor.
Verified by frame pull: "judgment" sits doomed in terracotta at t≈4.0s, and
the full corrected question "Can Claude close my books using a skill file?"
is settled and legible by the clip's final frame (media/B00.mp4, 10.2s
after render's tail-fit).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, single pass — no redo needed); NB01–NB03 rendered via
`render_scenes.py` (all 3 succeeded on first attempt); B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (foreground; the run exceeded the tool's
120s timeout and was moved to background by the harness automatically —
blocked on it via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule, never treating a backgrounded render as "handled"
without waiting on its exit code — exit 0, all 4 beats ok). `type_check.py`
ran **PASS, 0 FAILs** on the first pass — no defects to fix.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-close-month.mp4`, 7/7 beats
filled real (no slate), 82.3s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 82.3s; mp4
  mtime (1788406503) newer than beat_sheet.json mtime (1788406327)
- Gate V (visual): pulled frames every 6s across the full runtime (14
  frames) plus targeted checks of B00 (t≈2.2s naive question mid-type, t≈4.0s
  "judgment" doomed in terracotta, final frame settled+correct on "a skill
  file?"), NB01 (chip row: close-month/ → SKILL.md → the program, SKILL.md
  accented, caption "the file is the program" — legible, no overlap), NB02
  (reconcile → flag gaps → export packet, export packet accented, caption
  "steps run in order, not by judgment" — legible; chip-internal word
  spacing renders tight for "flag gaps"/"export packet" at this font/weight,
  a known EB Garamond kerning-rendering characteristic already tolerated by
  GATE T's calibration on the `agent-development` sibling, not a new
  defect — both remain readable as two words), NB03 (same input → same
  output → only the spec, caption "reliable, and only as wide as the file"
  — legible), BCRY (carry-out sentence + "Not judgment. A file." sparkline
  read clean), BHTF (correct topic "CLOSE-MONTH · ANTHROPIC SKILL", title
  "Claude, Close Month.", @HumanitariansAI handle, paste-ready prompt text
  legible), and BOUT (OutroSeries: correct eyebrow "CLOSE MONTH ·
  @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.24s (≥8s requirement met); the
  "judgment" → "a skill file" correction lands on screen by t≈4.0s and the
  full corrected question stays legible through the clip's final frame.

Metadata file written: `knowledge-work-plugins--claude-liam-close-month.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"` key
directly, which resolves to "Extending Claude — Skills, Plugins &
Connectors". Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
