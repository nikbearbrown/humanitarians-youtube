# BUILD-PROMPT — claude-liam-theme-factory ("Claude, Restrained.")

Standalone rebuild prompt for this reel. State when written: beat_sheet.json
authored (12 beats, skill-teardown modifier), Kokoro am_onyx audio GENERATED
and MEASURED (mp3/ + timings.json; actual_duration_s in the beat sheet is
ground truth), PEDAGOGY.md ends VERDICT: PASS, SOURCES.md logs every quote,
hex, and computed ratio. What remains: visuals → conform → render → QC.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build the visuals and final cut for the EXISTING reel
youtube/claude-liam-theme-factory ("Claude, Restrained." — an ai-explainer
skill-teardown of Anthropic's theme-factory skill, claude-liam channel).
Free pipeline only: no ElevenLabs, no higgsfield, no publishing, no git
commit or push. Run without approval pauses.

HARD CONSTRAINT — THE CLOCK IS LOCKED. The narration audio already exists
(mp3/beat-*.mp3) and actual_duration_s in beat_sheet.json is measured
ground truth. Do NOT regenerate audio, do NOT edit narration_text, do NOT
touch mp3/. Every beat's visuals conform to its existing audio duration.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md   (the skill-teardown modifier section
  governs this reel)
- skills/make/explainer/SKILL.md (and its MOTION.md / REMOTION.md)
- skills/make/your-turn/SKILL.md (closing block contract)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts and tokens/layout.ts (SAFE)
- youtube/claude-liam-theme-factory/beat_sheet.json (the edit — 12 beats)
- youtube/claude-liam-theme-factory/PEDAGOGY.md and SOURCES.md
- youtube/claude-liam-algorithmic-art/ — the exemplar: copy its
  remotion-src composition pattern and per-beat media/ flow
- ../anthropics/skills/skills/theme-factory/SKILL.md and themes/*.md —
  the SOURCE. All ten themes' hexes and fonts come from these files
  verbatim; SOURCES.md lists the verified values.

FORMAT

- 1920x1080 (16:9), 30 fps. Per-beat mp4s in media/, named by beat id,
  conformed to each beat's actual_duration_s (+0.4 s tail, matching the
  house conform rule). Assemble with runtime/scripts/compile.py; render
  Remotion only via runtime/scripts/remotion_scenes.py, foreground,
  --concurrency=1.

THE BEATS (visual contract — narration and durations are in the sheet)

- B00 ClaudeComposerAsk cold open — props are in the beat sheet. Composer
  shows its RESULT lines (ask lands answered).
- B01 ThemeFactoryAnatomy — the skill folder as an ink-line tree with real
  byte counts (SOURCES.md): SKILL.md 3,124 B · themes/ 10 files 513–544 B
  · theme-showcase.pdf · LICENSE.txt. Terracotta ring on themes/.
- B02 ThemeFactoryThemeCard — Golden Hour as a museum spec sheet: four
  TRUE-hex swatches materializing with names + codes (#f4a900 #c1666b
  #d4b896 #4a403a), FreeSans Bold / FreeSans line, "best used for" plaque.
- B03 ThemeFactoryConsentGate — four nodes SHOW → ASK → WAIT → APPLY.
  Nodes 1/4 in Claude palette (machine work); 2/3 carry the terracotta
  accent + a human silhouette. WAIT pulses as the narration lands on it.
  Verbatim caption: "Get explicit confirmation about the chosen theme."
- B04 ThemeFactoryTenSkins — THE CENTERPIECE. One slide card (title, two
  bullets, small chart) re-skinned through all ten themes in narration
  order (Ocean Depths → … → Midnight Galaxy), gallery name plaques,
  transform-don't-cut: colors/fonts morph, layout never moves. TRUE hexes
  from each themes/*.md. Time the theme switches to the narration's
  name-drops using the beat's audio (word-level timing if needed).
  Caption once, small: "Redrawn from theme-showcase.pdf".
- B05 ThemeFactoryMirror — the same card re-skins into THIS video's cream
  #FAF9F5 / ink #3D3929 / terracotta #D97757, and the frame highlights:
  the reel's own skin revealed as an eleventh theme. Spark line:
  "You're watching one."
- B06 ClaudeComposerAsk (escape-hatch ask) — props in the beat sheet.
- B07 ThemeFactoryCustomTheme — a NEW theme card ("Brutalist Cream")
  assembles in the skill's own spec format from the B06 ask; a review
  chip visibly blocks APPLY until sign-off. Spark line: "The gate
  survives."
- B08 ThemeFactoryContrastMeter — live WCAG meter over true-hex swatch
  pairs, ratios counting up to the REAL values in SOURCES.md: Silver on
  Deep Purple 12.57:1 AAA · Chocolate on Beige 5.32:1 AA · Mustard on
  Beige 1.05:1 FAIL (the mustard text visibly vanishes into the beige as
  the narration says "invisibility"). Spark line: "One load-bearing
  sentence."
- BVDT ClaudeVerdictArtifact — artifactLines in the beat sheet; enlarged
  card per the your-turn spec.
- BHTF ClaudeComposerAsk handoff — greeting "Your turn.", typing on (one
  of the exactly-two typing beats), command per the beat sheet.
- BOUT ClaudeTitleOutro — title · @NikBearBrown · "Liam, in for Bear."

LAWS THAT BITE HERE

- TRUE-HEX EXCEPTION (logged in SOURCES.md): theme swatches and themed
  demo cards render the source hexes exactly — the colors are the data.
  Frame chrome, labels, plaques stay in the fidelity palette; terracotta
  remains the ONE accent per beat and never appears as a fifth swatch.
- ILLUSTRATE LAW: the Claude UI appears only in B00, B06, BVDT, BHTF,
  BOUT. Every other beat is a concept illustration.
- SHOW-DON'T-TELL: reveals land on the spoken word (theme names in B04,
  the ratio verdicts in B08, WAIT in B03).
- FILL-THE-CANVAS / TYPESIZE, SPARK-LINE (≤4 words, no lonely asterisk),
  LOGO LAW (NBB bug lower-right every beat, full-size on BOUT), SAFE
  inset from tokens/layout.ts — all standing.
- No screenshots, no screen recordings, no lifted images anywhere.

ASSEMBLE, QC, REPORT

1. Implement the seven ThemeFactory* scenes in the reel's remotion-src/
   (adapt the algorithmic-art composition pattern; props match each
   component's zod schema). Render per-beat media/*.mp4 conformed to the
   locked audio durations.
2. python3 runtime/scripts/compile.py youtube/claude-liam-theme-factory
   → conform, mux, captions.
3. VISUAL QC LAW (full pass, not just the probe): ffmpeg frames at 2 fps
   plus each beat at ~15/50/85%, READ the PNGs, audit the 9-point rubric,
   log _qc/REPORT.md, fix root causes and re-render until zero BLOCKER
   and zero MAJOR.
4. ffprobe the final mp4 (audio present; duration ≈ sum of conformed
   beats). Report per-beat durations, total runtime, QC findings, file
   path, and the beat → timestamp table.

If any scene fails after two attempts, replace THAT beat with a labeled
PIPELINE slate and log it in BUILD-LOG.md — never silently drop a beat.
Never publish; the human flips anything public.
```
