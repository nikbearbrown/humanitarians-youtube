# BUILD-LOG — knowledge-work-plugins--claude-liam-close-management

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-close-management/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `close-management`
finance Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script, and the finance `SKILL.md` this source once
pointed to no longer exists on disk, so the source reel's own narration was
treated as the sole record of the Skill's facts). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: close-
management is a folder Claude reads before it acts — task sequencing,
dependencies, and status tracking for the month-end close; the SKILL.md
inside is plain language with no hidden code; a Steps section is executed
linearly, in order, with no branching unless a step explicitly says so;
and the whole thing is a bounded specification — repeatable for exactly
what it names, silent on everything outside that. B00 replaced the
source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "automate" → "structure" — the
newcomer's wrong guess that the skill automates the whole month-end close
by itself, corrected toward the actual mechanism: it only structures the
order Claude runs the close in). Register re-registered Teardown→Plain:
the source's B03 "gets it right / where it bites" framing (repeatable
results vs. anything outside the spec) was restated as plain mechanism-
and-scope description rather than a design verdict, per the NO JUDGMENT
register check. BVDT's verdict facts (same input, same output, every run;
limit: only what the file says) were merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. The source prompt's truncation bug ("statu" — "status
tracking" cut off mid-word) was repaired to the full phrase in BHTF. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B03 compressed into NB03 (the two facts —
repeatable within scope, silent outside it — restated as plain mechanism
and consequence); BVDT folded into BCRY; BHTF kept, with the source's
prompt carried over and its "statu" truncation repaired; BOUT kept. Full
audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with close-management-specific labels.

**B00 TIMING LAW** — reused the sibling's proven-safe parameters verbatim
(charMs 42, mistakeRate 4%, hesitateWithin 2%, hesitateBetween 8%, jitter
26) rather than re-deriving them, since that sibling had already found the
failure boundary (a longer/riskier config ran out of its window) and the
fix. Text is 63 chars (vs. the sibling's fixed 60-char text) — no defect
this time: audio measured 11.78s (lead_silence_s 1.0 included), well past
the ≥8s floor. Verified by frame pull: "automate" sits doomed in terracotta
at t≈3.0–3.4s, the correction to "structure" is settled by t≈4.5s, and the
full corrected question "Does close-management structure the way I run my
month-end close?" is fully typed and legible by t≈9.5s, holding to the end
of the 11.8s clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, no `--voice` flag needed — voice is read per-beat from the
sheet); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground;
exceeded the tool's 120s timeout and was moved to background by the
harness automatically — blocked on it via `TaskOutput` before proceeding,
per the COMPLETION LAW's foreground-render rule); NB01–NB03 rendered via
`render_scenes.py`.

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB03** — smallest text run 19px, 1px under the 20px
  floor. First hypothesis (matching the agent-development sibling's
  documented failure class) was the struck chip label "outside the spec"
  (17 chars, non-bold, dimmed MUTE) — shortened it to "outside spec" (12
  chars) to move it into the larger font-size bucket and re-rendered NB03
  only. Re-check still reported the identical 19px, proving the real
  culprit was untouched by that edit. Diagnosed directly by measuring
  isolated Manim `Text` mobjects for every chip word at the actual
  declared font sizes: the accented chip label "same sequence" splits
  into two independent connected-component blobs at render time (the
  word-gap breaks 4-connectivity), and the word "same" alone — s/a/m/e,
  no ascender or descender — has a raw ink bounding box of only
  ≈22.5px at font_size 26, which the mask's anti-aliasing-edge erosion
  brings under the 20px floor; the same risk existed for "names" in
  the unaccented "what it names" chip (≈21.7px raw, similarly thin
  margin). This is a structural risk for any all-x-height word at this
  font-size tier, not specific to one label's char count. Fixed by
  raising the chip font-size tiers in `scenes.py` (26/22/18 → 32/27/22)
  rather than hunting for ascender/descender-safe words per chip —
  confirmed by direct measurement that "same" and "names" at fs=32 raise
  to ≈27.7px/≈26.7px raw (comfortable margin over the floor after
  erosion) while the widest affected labels ("what it names", "same
  sequence") still fit the fixed chip width without triggering the
  scale-down path. Re-rendered all 3 GRAPHIC beats (the font-size change
  is global to the shared chip-row renderer, even though only NB03 had
  failed) — `beat_sheet.json`'s NB03 `graphic.production_viz.chips` was
  synced directly to the fixed wording (not via a full
  `build_beat_sheet.py` re-run, which would have discarded the already-
  measured audio durations and render stamps) before the recompile, per
  COMPLETION LAW.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-close-management.mp4`, 7/7
beats filled real (no slate), 101.6s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 101.6s; mp4
  mtime (1788405234) newer than beat_sheet.json mtime (1788404720)
- Gate V (visual): pulled frames across the full runtime (B00 at t≈8s
  fully settled and legible with the @HumanitariansAI handle; NB01 "A
  SKILL IS A FOLDER" chip row legible, arrows and accent underline clean;
  NB02 "THE PIPELINE IS LINEAR" three-step row clean; NB03 "A BOUNDED
  SPEC" post-fix chips all parallel-sized and legible; BCRY carry-out
  quote + sparkline read clean; BHTF correct topic/title/@HumanitariansAI
  handle, paste-ready prompt text legible; BOUT OutroSeries: correct
  eyebrow "CLOSE-MANAGEMENT · @HumanitariansAI", correct title restate,
  crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.78s (≥8s requirement met); the
  "automate" → "structure" correction lands on screen by t≈4.5s and the
  full corrected question stays legible for the remainder of the clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-close-management.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is a direct key match in the map, resolving to
"Extending Claude — Skills, Plugins & Connectors" — no prefix-matching
needed. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
