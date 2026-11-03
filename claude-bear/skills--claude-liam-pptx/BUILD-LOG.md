# BUILD-LOG — skills--claude-liam-pptx

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-pptx/beat_sheet.json` (Teardown
source examining Anthropic's `pptx` skill). Picked up mid-flight: on
arrival SCRIPT.md, beat_sheet.json (all 15 beats authored), 15 narration
mp3s (Kokoro `am_onyx`, measured `actual_duration_s` already written back),
11 Manim body renders (`manim/NB01-11.mp4`), and 2 of 4 Remotion renders
(`media/B00.mp4`, `media/BCRY.mp4`) already existed — audio and GRAPHIC
phases were complete; `media/BHTF.mp4` and `media/BOUT.mp4` were still
missing, and no compiled cut, TYPECHECK.md, or metadata file existed yet.
Continued from that point rather than rebuilding anything already filled.

Question, facts, and body argument carried over unchanged from the source:
the three-path routing (markitdown / edit-template-via-XML /
pptxgenjs-create); the mandatory design rules (color specificity and the
60-70% dominant-color rule, one motif + dark-light sandwich structure,
never Arial, never an accent line under a title); the two-stage QA mandate
(content QA + visual QA via subagent); and the three documented failure
modes (npm dependency, error-prone hand-edited XML, brand-guideline
clashes). B00 replaced the source's cold open with
`BrutalistHesitantWriter` per WRITER LAW: correction "learn" → "skip"
python-pptx — the newcomer's wrong guess that building slides requires
learning the python-pptx library, corrected toward the real question of
whether it can be skipped entirely. One concrete ANCHOR (a 5-slide
investor pitch deck for a carbon-capture startup, lifted from the source's
own handoff line) planted at NB02, paid off at NB09. Landing at 15 beats:
B00 + 11 GRAPHIC (Manim chip-row) body beats + BCRY + BHTF + BOUT — see
SCRIPT.md's "Beat-count note" for the full expansion rationale and the
confirmed Claude-fidelity-skin seam on the source's three `Pptx*.tsx`
components (not reused, same reorganization already logged on the
`claude-liam-docx`/`claude-liam-claude-api`/`claude-liam-brand-guidelines`
siblings).

**This invocation's work:**

1. `remotion_scenes.py` (foreground) — rendered the two missing REMOTION
   slots: `BHTF` (`ClaudeComposerAsk`, extended to 31.9s to match measured
   narration) and `BOUT` (`OutroCTA`). B00/BCRY skipped as already filled.
   Clean, first pass, exit 0.
2. `type_check.py` (Gate T) — had not yet been run on this reel. **PASS,
   0 FAILs** across all 15 beats on the first run (min-size, overflow,
   contrast, contrast-local, bbox-overlap, card-clip, kerning all clean).
   `TYPECHECK.md` written.
3. `compile.py` (foreground, 4K LAW forces the clean master to 2160p) —
   **15/15 beats real** (no slate). Gates inside compile.py: content-check
   PASS, frame-check PASS (3840×2160), lane-check PASS, GATE AUDIO PASS
   (mean_volume -23.8 dB). Wrote `skills--claude-liam-pptx.mp4`
   (188.017s).

**Independent verification (not compile.py's self-report):**
- ffprobe: video 3840×2160 h264, audio aac present, duration 188.017s.
- mp4 mtime (1788550291) newer than beat_sheet.json mtime (1788550130).
- `ffmpeg -af volumedetect`: mean_volume **-23.8 dB**, max -3.0 dB — well
  above the -40 dB floor.
- Gate V (visual): pulled frames every 6s across the full 188s runtime (31
  frames) plus two targeted grabs — B00 at t=9.5s confirms the WRITER LAW
  correction fully landed on screen ("Do you need to skip python-pptx to
  build slides?", "skip" in ink, cursor at end) and BOUT at t=186.5s
  confirms the close ("PPTX. Liam, in for Bear." + Subscribe +
  @HumanitariansAI). Sampled body beats (NB01, NB02, NB05, NB07, NB09,
  NB11) and both Your Turn frames (empty prompt box, then the fully typed
  paste-ready command) all legible, safe inset respected, no text overlap,
  single accent per beat, humanitarians palette consistent throughout.

**Non-blocking warning (compile.py):** motion histogram graphic:11
remotion:4 — graphic at 73%, over the ~40% pantry cap in MOTION.md. This
is structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against an 11-beat GRAPHIC body — the ratio follows beat count,
not a choice made in this build. Same disposition as every sibling in
HAILOOP-LOG.md. Logged per the honesty rule rather than reworking beat
count to dodge the warning.

Playlist resolution: SUBJECT.json's family (`skills`) has no literal
prefix match in `playlists.json`; the reel's actual subject (an Anthropic
Agent Skill's routing and mechanism) is a direct content match for the
map's `claude-skills`/`claude-agent-skills`/`claude-plugins` prefixes →
**"Extending Claude — Skills, Plugins & Connectors"** (already stamped in
beat_sheet.json metadata on pickup — confirmed correct, not changed). Same
reasoning as the `skills--claude-liam-docx`/`skills--claude-liam-claude-api`
siblings. Metadata file written: `skills--claude-liam-pptx.md` (channel
@HumanitariansAI, direct code link per DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate: content-check,
frame-check, lane-check, GATE T (0 FAILs), GATE AUDIO (-23.8 dB),
independent ffprobe + volumedetect verification, and Gate V frame review.
