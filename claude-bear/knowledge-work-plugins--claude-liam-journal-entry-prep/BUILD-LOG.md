# BUILD-LOG — knowledge-work-plugins--claude-liam-journal-entry-prep

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-journal-entry-prep/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `journal-entry-prep`
Claude skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged:
journal-entry-prep is a folder Claude reads before it acts; its SKILL.md is
the instruction set; the pipeline reads the request, works out the debit
and credit, and attaches supporting documentation; run twice on the same
numbers it produces the same entry both times (same input, same output);
and the concrete edge of that design — it only covers the named transaction
types (accruals, prepaid amortization, fixed asset depreciation, payroll
entries, revenue recognition), nothing the file doesn't name. B00 replaced
the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "training" → "a skill file" — the
newcomer's wrong guess that Claude was specially trained for accounting,
corrected toward the actual mechanism: a written file it follows step by
step). Register re-registered Teardown→Plain: the source's B03 "gets it
right / where it bites" design-tell language and BVDT's separate verdict
artifact were merged into a single plain mechanism-and-consequence beat
(NB03) plus the BCRY carry-out, dropping the Teardown framing per the NO
JUDGMENT register check. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03 + BVDT compressed into NB03 (the one fact a general
viewer needs and can act on: same input/same output reliability paired with
the named-transaction-list scope limit); BHTF kept, with the source's
your-turn prompt cleaned up from a truncated metadata-concatenation string
into a complete, paste-ready sentence (the underlying ask — prepare journal
entries with proper debits, credits, and supporting documentation, narrate
the plan first — is unchanged); BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-close-month` sibling, adapted with
journal-entry-prep-specific labels.

**B00 TIMING LAW — calibrated from the start, no failed first render.**
Applied the timing rates already proven on the `agent-development` and
`close-month` siblings (charMs=42, mistakeRate=4%, hesitateWithin=2%,
hesitateBetween=8%, jitter=26) rather than the slower defaults that caused
the earliest sibling's first-attempt timeout. Text: "Can Claude prep /
journal entries / using / training?" (single trigger word "training" →
replacement "a skill file"). Rendered clean on the first attempt:
`actual_duration_s` 10.52s (audio) + `lead_silence_s` 0.8 = 11.32s window,
well past the ≥9s TIMING LAW floor. Verified by frame pull at t≈9.5s: the
full corrected question "Can Claude prep journal entries using a skill
file?" is settled and legible, cursor still blinking at end of text —
correction landed well before the clip's end.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, single pass — no redo needed); NB01–NB03 rendered via
`render_scenes.py` (all 3 succeeded on first attempt); B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (foreground; the run exceeded the tool's
120s timeout and was moved to background by the harness automatically —
blocked on it via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule, never treating a backgrounded render as "handled"
without waiting on its exit code — exit 0, all 4 beats ok).

`type_check.py` ran **FAIL on the first pass** (1 pixel beat): NB02's
initial chip labels ("read the request", "post debit & credit", "attach
documentation") were long enough (16–21 chars) to trigger the chip
renderer's font-scale-down path, pushing the smallest text run to 18px,
under the 20px (1.9% frame-height) floor. Fixed by shortening the three
labels to the close-month sibling's proven-safe pattern (≤14 chars: "read
request", "debit & credit", "attach support") in both `scenes.py` and
`build_beat_sheet.py`, syncing the same three strings into
`beat_sheet.json`'s `graphic.production_viz.chips` field directly (no
`build_beat_sheet.py` re-run, so `actual_duration_s`/build stamps were left
untouched), re-rendering only `manim/NB02.mp4`, and recompiling with
`--force`. Second `type_check.py` pass: **PASS, 0 FAILs**.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-journal-entry-prep.mp4`, 7/7
beats filled real (no slate), 83.9s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the NB02 chip-label fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 83.9s; mp4
  mtime (1788502270) newer than beat_sheet.json mtime (1788502187)
- Gate V (visual): pulled frames every 6s across the full runtime (14
  frames) plus a targeted B00 frame at t≈9.5s. B00: naive typing mid-frame,
  then the full corrected question "Can Claude prep journal entries using a
  skill file?" settled and legible with cursor blinking. NB01 (chip row:
  journal-entry-prep/ → SKILL.md → the program, SKILL.md accented, caption
  "the file is the program" — legible, no overlap). NB02 (read request →
  debit & credit → attach support, attach support accented, caption "steps
  run in order, not by feel" — all three labels now clearly legible at
  correct size after the fix). NB03 (same numbers → same entry → only
  what's named, caption "reliable, and no wider than the file names" —
  legible). BCRY (carry-out sentence + "Not guesswork. A file." sparkline
  read clean). BHTF (correct topic "JOURNAL-ENTRY-PREP · ANTHROPIC SKILL",
  title "Claude, Journal Entry Prep.", @HumanitariansAI handle, paste-ready
  prompt text legible). BOUT (OutroSeries: correct eyebrow "JOURNAL ENTRY
  PREP · @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.52s (≥8s requirement met); the
  "training" → "a skill file" correction lands on screen and the full
  corrected question stays legible through the clip's final frame.

Metadata file written:
`knowledge-work-plugins--claude-liam-journal-entry-prep.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"` key
directly, which resolves to "Extending Claude — Skills, Plugins &
Connectors". Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
