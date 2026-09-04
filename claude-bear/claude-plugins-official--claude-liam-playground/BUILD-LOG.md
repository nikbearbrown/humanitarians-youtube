# BUILD-LOG — claude-plugins-official--claude-liam-playground

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-playground/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `playground` Claude
Code plugin Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill
organizes around six templates across four zones (design-playground,
data-explorer, concept-map, and three review templates); every playground
must meet five core requirements (single self-contained HTML file, live
preview with no Apply button, natural-language prompt with non-default
values only, copy button, three-to-five presets); the whole thing runs on a
single-state-object invariant (controls write, renders read, `updateAll()`
on every change) that is what makes the live preview reliable; the prompt
output has its own natural-language-not-value-dump rule; and nothing in the
skill's own design enforces that rule automatically, which is why the
required "open the file in a browser" verification step exists. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "values" → "a prompt" — the
newcomer's wrong guess that a Claude-built playground just hands back the
raw values you picked, corrected toward the actual deliverable: a
natural-language prompt you copy into Claude).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's "gets it right / where it bites" list
compressed into NB03 (the one fact a general viewer needs and can act on —
nothing enforces the natural-language rule, so checking by hand is
required); BVDT folded into BCRY; BHTF kept, with the source's already
generic, already-runnable prompt (an interactive card-design playground
with border radius, shadow, padding, and color) carried over unchanged;
BOUT kept, re-skinned to the Humanitarians AI outro. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`PlaygroundAnatomy` / `PlaygroundDesign` / `PlaygroundTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap. NB01–NB03 were, however,
built fresh as GRAPHIC (Manim) rather than reused from the source's
`PlaygroundAnatomy` / `PlaygroundDesign` / `PlaygroundTell` REMOTION
components: those three components bake Teardown framing directly into
on-screen text ("PLAYGROUND · TEARDOWN", "What it gets right / where it
bites", a two-column GETS_RIGHT/BITES split) — a register violation on
screen, not just in narration. Plain requires the visual framing to drop
the verdict too, so this redo built new GRAPHIC beats on the shared generic
"chip row" Manim template (copied from the `claude-plugins-official--
claude-liam-agent-development` sibling) instead of retrofitting
judgment-shaped card components.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with playground-specific labels.

**GATE T — two real defects caught and fixed, not QC-sampling traps.**

1. First render: NB02's chip labels ("controls write" / "state" / "renders
   read") and NB03's chip labels ("natural language" / "or a value dump" /
   "up to the builder") measured 19px and 18px respectively against the
   20px floor. Fix: shortened all three NB02 chips to single words
   ("writes" / "state" / "reads") and NB03's captions/chips to shorter
   forms, and widened the `_chip()` fit thresholds (0.82→0.88 width,
   0.68→0.76 height) for headroom. Re-rendered NB01–NB03; NB03 passed at
   exactly 20px, but NB02 still failed at 19px unchanged — the width/height
   threshold widening had no effect because the failing chip text was never
   entering the shrink branch (`scale` stayed at 1.0); the 19px was the
   *natural* size of the base font tier, not a shrink artifact. Root cause:
   the base chip font-size tiers (26/22/18) were simply too small at this
   box geometry. Fixed by raising the tiers to 30/26/22 and re-rendering
   all three chip-row beats — confirmed by the next GATE T pass: **PASS,
   0 FAILs**.
2. Gate V frame pull on NB03 (t≈95s) surfaced a second, GATE-T-invisible
   defect: the chip label "builder decides" rendered as "builderdecides"
   with no visible space between the words — a Manim `Text` rendering
   quirk this toolkit's type-checker does not test for (it checks size/
   contrast/overlap, not intra-label spacing). Fixed by replacing the
   two-word label with a single word, "guesswork", sidestepping the defect
   rather than root-causing the Pango/Text space-collapse itself (out of
   scope for a one-shot build; NB01's "review (x3)" and NB03's
   "value dump" both correctly rendered spaces, so the defect was not
   universal across all multi-word chips — narrower single-word chips were
   the safe, verified fix). Re-rendered NB03 only, recompiled, reverified
   by frame pull: "instruction · value dump · guesswork" all legible with
   correct spacing.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, no manual `--only` reruns needed — B00's narration/timing worked
on the first pass). B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground call; exceeded the tool's 120s timeout and was moved to
background by the harness automatically — blocked on it via `TaskOutput`
before proceeding, per the COMPLETION LAW's foreground-render rule, never
treating a backgrounded render as "handled" without waiting on it);
NB01–NB03 rendered via `render_scenes.py` (ran fast enough to stay
foreground each time). `compile.py --force` also exceeded the 120s timeout
on two of its three runs (auto-backgrounded, blocked on via `TaskOutput`
both times) — same rule, same handling.

`type_check.py` went FAIL (2 defects) → FAIL (1 defect) → **PASS, 0
FAILs** across the three fix iterations above. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-playground.mp4`, 7/7 beats
filled real (no slate), 147.3s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac, mono) present, duration
  147.317s; mp4 mtime (1788165725) newer than beat_sheet.json mtime
  (1788165600)
- Gate V (visual): pulled frames at t=2.2/4.0/5.0/5.5/6.0/6.5/7.0/8.5s
  across B00 specifically (the "values" trigger word confirmed doomed in
  terracotta at t≈5.0-5.5s, corrected to "a prompt?" and fully settled and
  legible by t≈6.5s, held through the end of the 8.9s clip — well past the
  ≥8s TIMING LAW floor) plus t=25/65/95/110/130/145s spanning NB01, NB02,
  NB03 (post-fix), BCRY, BHTF, and BOUT. All legible, correct topic/title/
  @HumanitariansAI branding, correct humanitarians accent color on B00/
  NB01-03, no truncation, no overlap. No blockers remaining after the two
  GATE T fixes above.
- B00 TIMING LAW: `actual_duration_s` 8.87s (≥8s requirement met, though
  closer to the floor than the agent-development sibling's 10.1s — the
  correction still lands with sufficient margin per the frame-pull
  sequence above: doomed at t≈5.0s, settled by t≈6.5s, held for the
  remaining ~2.4s of the clip).

Metadata file written: `claude-plugins-official--claude-liam-playground.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match — `"claude-plugins-official".startswith("claude-
plugins")`), which resolves to "Extending Claude — Skills, Plugins &
Connectors"; this is a more specific match than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with the
`claude-plugins-official--claude-liam-agent-development` sibling built in
this same family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
