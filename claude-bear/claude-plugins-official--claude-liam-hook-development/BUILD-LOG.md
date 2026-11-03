# BUILD-LOG — claude-plugins-official--claude-liam-hook-development

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-hook-development/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `hook-development`
Claude Code plugin-dev Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` and `PEDAGOGY.md` served as the locked script and
facts). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup.

Question, facts, and full body argument carried over unchanged: two hook
types (Prompt-Based — recommended, LLM-driven, matcher + prompt field, 30s
default timeout; Command — bash, deterministic, exit 0/2/other, 60s
default timeout, CLAUDE_PLUGIN_ROOT for portability); two config formats
(plugin hooks.json wrapper vs. flat settings direct format); nine
lifecycle events, of which only four (PreToolUse, Stop, SubagentStop,
UserPromptSubmit) support Prompt-Based hooks, the other five (PostToolUse,
SessionStart, SessionEnd, PreCompact, Notification) are Command-only; four
execution rules (parallel with no ordering/shared output, session-start-
only load with no hot-swap, case-sensitive matchers, and the named
security defaults). B00 replaced the source's `ClaudeComposerAsk` typed-ask
cold open with `BrutalistHesitantWriter` (WRITER LAW: "any" → "only four"
— the newcomer's wrong guess that the recommended hook type fires on every
event, corrected toward the actual four-of-nine restriction). This
restriction is also `PEDAGOGY.md`'s own stated verdict note for the source
reel ("The key gap to surface: prompt hooks are recommended without
stating the 4-event restriction upfront"), which is why it was chosen as
the single most teachable fact carried through B00, NB03, and BCRY.
Register re-registered Teardown→Plain: the source's B05 "gets it right /
where it bites" list (5 rights, 5 gaps) was compressed to the single most
teachable, general-audience fact (the four-event restriction and its
silent-failure mode) rather than kept as a full strengths/gaps inventory —
the other four gaps (hot-swap timing, hook-collaboration limits, format
confusion, matcher case-sensitivity) were dropped as secondary to the one
restriction that most directly contradicts the "recommended type" framing,
not as a verdict on the skill's quality. BVDT's verdict facts were merged
into the single BCRY carry-out sentence rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT
folded into BCRY; BHTF kept, with the source's already-generic,
already-runnable prompt ("Give Claude a plugin that logs every Write tool
call to a JSON file and blocks any Write to a dot-env file") carried over
unchanged and its five watch-points compressed to four by folding the
source's standalone "restart reminder" point into the PostToolUse/
Command-hook point it actually explains; BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`HookDevelopmentAnatomy` / `HookDevelopmentDesign` / `HookDevelopmentTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with hook-development-specific labels.

**B00 TIMING LAW — cleared on the first render, no fix needed.** Text
"Does a Prompt-Based hook / fire on any of / the nine events / I use?"
(4 lines, trigger word "any" → "only four"), charMs=42, mistakeRate=4%,
hesitateBetween=8% (the established fix-pattern rates from the
agent-development/access siblings' second attempts, used here from the
start), audio 10.24s. Verified by frame pull: "any" sits doomed in
terracotta at t≈5.3–5.9s, the full corrected question "Does a Prompt-Based
hook fire on only four of the nine events I use?" is settled and legible
by t≈10.1s, comfortably inside the 10.27s clip — well past the ≥8s TIMING
LAW floor.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground); NB01–NB03 rendered via `render_scenes.py` (foreground).
First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB02** — smallest text run measured 17px, 3px under the
  20px floor. Root cause: chip label `"4 take prompt hooks"` (19 chars)
  fell into the 18px font-size tier (`_chip`'s length-based tiering), which
  scaled under the floor after fit-to-box. Fixed by shortening the chip
  labels to `["9 events", "4 of 9", "no ordering"]` (all ≤10 chars, into
  the 26px tier) — re-rendered NB02 only, and `beat_sheet.json`'s
  `graphic.production_viz.chips` for NB02 was synced directly (not via a
  full `build_beat_sheet.py` re-run, which would have discarded the
  already-measured audio durations and render stamps) before the
  recompile, per COMPLETION LAW.

`type_check.py` went 1→**PASS**, but Gate V (frame-pull visual review, run
next) caught a defect GATE T's automated check does not measure — text
*content* correctness, not size or contrast:

- **Space-collapse in BOLD chip text, NB02 + NB03 — a real rendering
  defect, not a QC-sampling false alarm.** Frame pulls of NB02 (`"4 of 9"`
  chip, the beat's one BOLD/accented chip) and NB03 (`"never runs"` chip,
  same BOLD/accented pattern) showed the multi-word label rendered with
  **no space at all** — `"4of9"` and `"neverruns"` — while every
  NORMAL-weight multi-word chip and caption in the same scenes (`"no
  ordering"`, `"nine events"`, `"no hot-swap · case-sensitive matchers"`,
  `"recommended ≠ everywhere"`) rendered with correct spacing. Confirmed
  not a mid-animation transient by pulling frames at 3s and 20s into
  NB02's 40.2s clip — both showed the same collapsed `"fourofnine"` in the
  settled, fully-held state. Isolated the trigger by testing intermediate
  labels: `"9 events"` → `"9events"` (fails, 2 words), `"nine events"` →
  renders correctly (2 words, NORMAL weight, not accented in that slot),
  `"four of nine"` → `"fourofnine"` (fails, 3 words, BOLD/accented). The
  common factor across every failure was BOLD weight applied to a
  multi-word `Text` string in this Manim/font environment — not word
  count, not digits alone (`"nine events"` at NORMAL weight was never
  affected; the earlier `"9 events"` failure was consistent with the same
  BOLD-weight rule since NB02's first chip was never actually the accented
  one in that draft — the fix below removes the ambiguity by testing
  hyphenated forms instead of re-diagnosing further). Fixed by hyphenating
  both accented labels into single tokens — NB02's accent chip to
  `"four-of-nine"`, NB03's accent chip to `"never-runs"` — consistent with
  the reel's existing hyphen/underscore convention (`"Prompt-Based"`,
  `"CLAUDE_PLUGIN_ROOT"`). Re-rendered NB02 and NB03 only; `beat_sheet.json`
  synced directly for both beats before the recompile. Reverified by frame
  pull: `"four-of-nine"` and `"never-runs"` both render with correct,
  fully-connected hyphenated text, held legible for the remainder of each
  clip.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-hook-development.mp4`, 7/7
beats filled real (no slate), 163.5s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the NB02 min-size fix above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 163.5s; mp4
  mtime (1788157775) newer than beat_sheet.json mtime (1788157620)
- Gate V (visual): pulled frames every ~12s across the full runtime plus
  targeted checks of B00 (t≈5.3-5.9s "any" doomed in terracotta, t≈10.1s
  settled+correct question, held to the end of the 10.27s clip), NB01-NB03
  (all chips legible post-fixes, including the recompiled NB02/NB03 with
  the hyphenated accent labels), BCRY (carry-out sentence + sparkline read
  clean), BHTF (correct topic/title/@HumanitariansAI handle, paste-ready
  prompt text legible), and BOUT (OutroSeries: correct eyebrow "HOOK
  DEVELOPMENT · @HumanitariansAI", correct title restate "Only Four of the
  Nine.", crimson underline, no truncation). No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 10.24s (≥8s requirement met); the
  "any" → "only four" correction lands on screen by t≈10.1s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written:
`claude-plugins-official--claude-liam-hook-development.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors"; this is a more specific match than falling through
to the `hai-simple` skill-key default ("Claude Basics"), consistent with
the `claude-plugins-official--claude-liam-agent-development` and
`claude-plugins-official--claude-liam-access` siblings built in this same
family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
