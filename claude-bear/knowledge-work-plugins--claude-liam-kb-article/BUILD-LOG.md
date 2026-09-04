# BUILD-LOG — knowledge-work-plugins--claude-liam-kb-article

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-kb-article/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `kb-article` Claude
skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: kb-article
is a folder Claude reads before it acts; its SKILL.md is the instruction
set; the pipeline reads SKILL.md, executes each step in order, and returns
the finished article; run twice on the same resolved ticket it produces the
same article both times (same input, same output); and the concrete edge of
that design — it only drafts an article when one of the file's named
triggers is met (a ticket resolution worth documenting for self-service,
the same question keeps coming up, a workaround needs publishing, or a
known issue should be communicated to customers), nothing the file doesn't
name. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "instinct" → "a skill file" — the
newcomer's wrong guess that Claude senses on its own when a ticket is
"worth" an article, corrected toward the actual mechanism: a written file it
checks against). Register re-registered Teardown→Plain: the source's B03
"gets it right / where it bites" design-tell language and BVDT's separate
verdict artifact were merged into a single plain mechanism-and-consequence
beat (NB03) plus the BCRY carry-out, dropping the Teardown framing per the
NO JUDGMENT register check. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03 + BVDT compressed into NB03 (the one fact a general
viewer needs and can act on: same input/same output reliability paired with
the named-trigger-list scope limit); BHTF kept, with the source's
your-turn prompt cleaned up from a truncated metadata-concatenation string
into a complete, paste-ready sentence (the underlying ask — draft a
knowledge base article from a resolved issue or common question, narrate
the plan first — is unchanged); BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-journal-entry-prep` sibling, adapted
with kb-article-specific labels.

**B00 TIMING LAW — calibrated from the start, no failed first render.**
Applied the timing rates already proven on the `agent-development`,
`close-month`, and `journal-entry-prep` siblings (charMs=42, mistakeRate=4%,
hesitateWithin=2%, hesitateBetween=8%, jitter=26) rather than the slower
defaults that caused the earliest sibling's first-attempt timeout. Text:
"Can Claude draft / a knowledge base / article using / instinct?" (single
trigger word "instinct" → replacement "a skill file"). Rendered clean on
the first attempt: `actual_duration_s` 10.33s (audio) + `lead_silence_s` 0.8
= 11.13s window, well past the ≥9s TIMING LAW floor. Verified by frame pull
at t≈9.5s: the full corrected question "Can Claude draft a knowledge base
article using a skill file?" is settled and legible, cursor still blinking
at end of text — correction landed well before the clip's end.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, single pass — no redo needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, all 3 succeeded on first attempt); B00/BCRY/
BHTF/BOUT rendered via `remotion_scenes.py` (foreground, all 4 succeeded on
first attempt — no timeout, no background handoff needed this time).

`type_check.py` (GATE T) ran clean on **both** the pre-render dry pass (all
7 beats §8.10 SKIP, as expected before media exists) and the post-compile
pass: **PASS, 0 FAILs** across min-size, overflow, contrast,
contrast-local, bbox-overlap, card-clip, and kerning checks — no fix
iteration needed.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-kb-article.mp4`, 7/7 beats
filled real (no slate), 85.1s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (clean on the first pass)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect)
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 85.081s; mp4
  mtime (1788503361) newer than beat_sheet.json mtime (1788503276)
- Gate V (visual): pulled 14 frames every 6s across the full 85.1s runtime
  plus a targeted B00 frame at t≈9.5s. B00: naive typing mid-frame, then the
  full corrected question "Can Claude draft a knowledge base article using
  a skill file?" settled and legible with cursor blinking. NB01 (chip row:
  kb-article/ → SKILL.md → the program, SKILL.md accented, caption "the
  file is the program" — legible, no overlap). NB02 (read SKILL.md →
  execute steps → return article, return article accented, caption "steps
  run in order, not by feel" — all three labels legible). NB03 (same ticket
  → same article → only what's named, caption "reliable, and no wider than
  the file names" — legible). BCRY (carry-out sentence + "Not a feeling. A
  file." sparkline read clean). BHTF (correct topic "KB-ARTICLE · ANTHROPIC
  SKILL", title "Claude, Kb Article.", @HumanitariansAI handle, paste-ready
  prompt text legible). BOUT (OutroSeries: correct eyebrow "KB ARTICLE ·
  @HumanitariansAI", correct title restate, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.33s (≥8s requirement met); the
  "instinct" → "a skill file" correction lands on screen and the full
  corrected question stays legible through the clip's final frame.

Metadata file written:
`knowledge-work-plugins--claude-liam-kb-article.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"` key
directly, which resolves to "Extending Claude — Skills, Plugins &
Connectors". Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
