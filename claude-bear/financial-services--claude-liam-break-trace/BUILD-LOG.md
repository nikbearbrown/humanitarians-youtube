# BUILD-LOG — financial-services--claude-liam-break-trace

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-break-trace/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `break-trace` Claude
Code Skill, from the `financial-services` book's `gl-reconciler` plugin —
already fully built, no SCRIPT.md; source `beats[*].narration_text` served
as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, containing one file (SKILL.md)
written in plain language; the instructions are steps, executed in order,
no branching unless a step says so; `break-trace`'s specific job is
root-causing a reconciliation break to its source transaction or posting by
following the audit trail back on each side and stating what differs and
why, used only after another skill (`gl-recon`) has already classified the
break; same input produces the same output every run; the skill only
handles what its file describes. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "fix" → "trace" — the newcomer's wrong guess that Claude
*resolves* a reconciliation discrepancy, corrected toward the actual
mechanism: the skill only traces the break to its cause and hands back a
diagnosis, never a fix). Register re-registered Teardown → Plain: the
source's B03 "gets it right: repeatable results / where it bites: anything
outside the spec" framing was restated in NB03 as a plain mechanism-and-
boundary fact (what the skill traces to, and what it declines to decide),
per the NO JUDGMENT register check. BVDT's verdict facts (same input → same
output every run; limited to what the file specifies) were merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. BHTF's prompt was adapted, not copied
verbatim: the source asked the viewer to "read the break-trace skill,"
which requires a plugin install a general viewer won't have, so this redo
substitutes an equivalent, actually-paste-ready prompt exercising the same
trace-before-fix habit without depending on any specific Skill file. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01→NB01, B02→NB02 kept as one beat each; B03's Teardown framing compressed
into NB03 (a plain mechanism-and-boundary fact); BVDT folded into BCRY;
BHTF kept (prompt adapted, see above); BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with break-trace-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 4-line text) reused directly from the `claude-plugins-official--
claude-liam-agent-development` sibling's proven working configuration
rather than re-discovering that sibling's own first-attempt overrun.
`actual_duration_s` (narration) 8.38s + `lead_silence_s` 1.0 gave the
writer a 9.38s window; rendered clip extended to 8.4s, meeting the ≥8s
TIMING LAW floor. Verified by frame pulls at t=2.0s ("fix" doomed in
terracotta), t=4.0s (mid-correction, "trace a brea[k]" typing), and
t=7.5s (full corrected question "Does Claude trace a break in the books?"
settled and legible) — correction lands well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (the
initial invocation exceeded the tool's 120s timeout and was moved to
background by the harness automatically — blocked on it via `TaskOutput`
before proceeding, per the COMPLETION LAW's foreground-render rule, never
treating a backgrounded render as "handled" without waiting on it);
NB01–NB03 rendered via `render_scenes.py`. First `type_check.py` pass was
**FAIL, 1 defect**, root-caused and fixed iteratively:

- **min-size §8.1, NB03** — smallest text-run height sat 1-2px under the
  20px floor across several rounds of guessing (shortening chip labels,
  shortening the title, bumping caption font_size) that each moved the
  number by 0-1px without clearing it. Root cause found by extracting the
  exact mid-clip frame `type_check.py` samples and running the same
  connected-component blob measurement locally (numpy/scipy) rather than
  guessing further: the failing 19px blob was the isolated word "say" in
  the chip label "say why" — "say" has no ascender and no descender
  (s-a-y's only extender is the 'y' descender, insufficient alone), so as
  its own disconnected blob (space-separated from "why") it measured
  shorter than any other label in the scene. Fixed by replacing the label
  with a single connected word carrying real ascender/descender extent
  ("explains" — p/l/h-shaped extenders) rather than continuing to guess at
  font sizes or synonyms; also renamed the NB03 title from "WHAT
  BREAK-TRACE DOES" (22 chars, needed heavy scale-to-fit at that bold
  weight) to "TRACE, NOT FIX" (14 chars, no scaling) and the middle
  accented chip from "trace to source" → "traces back" → "pinpoints" along
  the way — those intermediate edits were directionally reasonable (same
  defect class as a documented sibling fix) but were not, in fact, the
  binding constraint; kept the shorter title and "pinpoints" as
  improvements, reverted an interim caption font_size bump (30→36, tested
  and confirmed not the cause) back to the sibling's original 30 rather
  than leaving an unexplained deviation in place.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `financial-services--claude-liam-break-trace.mp4`, 7/7 beats filled
real (no slate), 76.6s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.1 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 76.6s; mp4
  mtime (1788266585) newer than beat_sheet.json mtime (1788266508)
- Gate V (visual): pulled frames at t=4/12/20/30/40/50/58/66/70/74s across
  the full runtime plus the targeted B00 correction-timing checks above.
  B00 (writer, correction visible and settled), NB01/NB02/NB03 (all chips
  legible, arrows and captions clean, no overlap), BCRY (carry-out quote +
  sparkline "Trace it. Don't fix it." read clean), BHTF (correct topic
  "BREAK-TRACE · RECONCILIATION SKILL", correct title "Trace It, Don't Fix
  It.", @HumanitariansAI folder label, paste-ready prompt legible), BOUT
  (OutroSeries: "BREAK-TRACE · @HumanitariansAI" eyebrow, correct title
  restate, crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 8.38s narration + 1.0s lead silence,
  rendered clip 8.4s (≥8s requirement met); correction ("fix"→"trace")
  lands and settles well inside the clip (verified by frame pulls above).

Metadata file written: `financial-services--claude-liam-break-trace.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`financial-services`) matches no
specific vertical prefix in the map (no `finance-`/`financial-` entry
exists), so resolution falls through in map order to the `hai-simple` key
itself (present in the map precisely as this general fallback), which
resolves to "Claude Basics" — this is the intended fallback path per the
skill's redo-worker rule ("match family, or the hai-simple prefix... use
_default only when nothing matches"), and "Claude Basics" is reached before
`_default` ("Claude Across the Curriculum") is ever considered. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
