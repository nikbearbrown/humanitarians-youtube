# BUILD-LOG — knowledge-work-plugins--claude-liam-cowork-plugin-customizer

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of `anthropics/knowledge-work-plugins/youtube/claude-liam-cowork-plugin-customizer/beat_sheet.json`
(a Teardown-register batch build, 7 beats, brand `claude-liam`, `@NikBearBrown`,
`source_skill` pointing at `/Users/bear/Documents/CoWork/bear-textbooks/.../cowork-plugin-customizer/SKILL.md`
— a path on Bear's separate machine, not present here). Unlike a prior redo
in this family (`claude-code--claude-liam-plugin-structure`), no local
equivalent of the real `SKILL.md` exists anywhere in this workspace —
confirmed by grep across the whole `books/` tree and against
`BUILD-SKILL-EXPLAINERS-LOG.md`/`SKILL-EXPLAINERS-BATCH-LOG.md`, which
record this reel as a 2026-07-25 batch build.

**Source defect found and handled (see QUESTION.md for full detail):** the
source's B00, B03, BVDT, and BHTF narration each contain a literal unfilled
`>` placeholder where a skill-specific detail (Claude's exact customization
job, the "gets right/bites" specifics, the handoff task) was meant to be
substituted by the batch builder and never was. Per NO-INVENTED-FACTS, this
redo does not guess what those placeholders were meant to say. It keeps the
one substantive fact the source states outright — "customize a Claude Code
plugin for a specific organization's tools" (present in the source's B00
`output` array and BVDT artifact lines, not behind a placeholder) — as the
anchor, and states the rest of the mechanism generically and accurately
(a Skill is a folder containing `SKILL.md`; Claude reads it, then works
through its Steps section in order; the same request produces the same
steps; going past the written scope switches Claude to general judgment
rather than erroring). The source's own Your Turn task named the private
skill directly, unrunnable by any viewer — generalized to "open this
skill's SKILL.md and walk me through the steps" pointed at any Skill the
viewer actually has, keeping the lesson runnable.

Kept beat count (7): B00 hesitant-writer cold open (naive guess "installs"
→ corrected to "reads" — the newcomer's default read of a folder named
*cowork-plugin-customizer* is that the word "plugin" makes it installed
software), B01 anatomy + anchor planted (folder → SKILL.md → the one
job-line), B02 mechanism (Steps run top to bottom, same order every time),
B03 anchor payoff + both directions (the job-line now governs a drawn
sequence; a request that steps outside it switches Claude to general
judgment, not an error), BCRY carry-out, BHTF generalized Your Turn, BOUT
outro. Anchor B01→B03: the skill's one stated job-line, planted inside the
folder/file reveal, paid off by the same line governing a visible Steps
sequence and showing where a request can step off it.

B00 WRITER LAW: naive guess "installs" → corrected to "reads"; 33-word
narration + `lead_silence_s: 0.8`, measured 11.24s (clears the TIMING LAW
≥9s window); confirmed on a frame pull at 18s into the rendered B00.mp4
(20.2s total) that the writer's final text reads "Is cowork-plugin-
customizer / a plugin that Claude / reads?" — correction visible well
before the beat ends.

Built from scratch this invocation (QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json, scenes.py + render_scenes.py for the 3 Manim body beats):

1. Gate L (`./art scenes --check`) confirmed `BrutalistHesitantWriter`,
   `ClaudeComposerAsk`, `OutroCTA`, `WantQuote` all RENDERABLE before
   slating any beat.
2. `generate_audio_kokoro.py` — 7/7 beats, cost $0.00, measured durations
   11.24/20.37/17.77/19.35/10.20/15.68/4.12s written back as ground truth.
3. Rendered 3 Manim body beats (`CPCB01Scene`/`CPCB02Scene`/`CPCB03Scene`)
   via `render_scenes.py` in the foreground — all 3 ok on first pass.
4. Rendered 4 Remotion beats via `remotion_scenes.py` in the foreground
   (first invocation hit the 2-minute tool timeout after B00 alone
   finished; re-ran in the foreground with a longer timeout and it
   completed BCRY/BHTF/BOUT cleanly — no beat was ever left to render
   unsupervised).
5. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, GATE AUDIO PASS mean_volume -23.9 dB. THE 4K LAW forced the clean
   master natively to 3840×2160.
6. Gate V (first pass): pulled 12 frames at 8s spacing plus a dedicated
   B00-correction frame and read all of them. **Found a real defect**: in
   B01, the italic job-line quote ("Customize a Claude Code plugin for one
   organization's tools.") was sized and positioned to overflow the
   folder-card border — text crossed the card's bottom edge, a containment
   violation. Root-caused to `scenes.py` placing a wide single-purpose
   quote too close to a card sized for the file-name reveal alone.
7. Fixed `scenes.py` B01: enlarged the folder card, moved "THE ANCHOR"
   label and job-line fully below the card with clear spacing, and split
   the typed quote onto two pre-wrapped lines so the Transform animation
   never produces an overflowing line. Re-rendered B01 only (9.25s clip)
   and recompiled — `compile.py` re-ran clean, GATE AUDIO PASS -23.9 dB
   again, 4K forced again.
8. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788431527) newer than
   beat_sheet.json mtime (1788431169); h264 3840×2160 + aac streams
   present, duration 99.739s; `ffmpeg -af volumedetect` mean_volume
   **-23.9 dB**, max -3.0 dB — independently confirms GATE AUDIO.
9. GATE T (`type_check.py`): **PASS, 0 FAILs**, re-run after the B01 fix.
10. Gate V (second pass, post-fix): re-pulled the B01 frame at the same
    timestamp — job-line now fully contained below the card, no overflow,
    safe inset respected. Spot-checked the typing transition at several
    points through the (2.2×-stretched) B01 clip: the settled end-state is
    clean at every check; one single transient frame mid-Transform showed
    letter-ghosting from the stretch interacting with the fast (0.08s)
    per-keystroke animation — the same category of artifact the sibling
    reel `claude-code--claude-liam-plugin-structure` logged as
    non-blocking for time-stretched static-camera Manim, and here it
    resolves to fully legible text well before the beat ends. Re-checked
    B02/B03/BCRY/BHTF and a dedicated BOUT frame (94.7-99.8s window, missed
    by the regular 8s-spaced sampling) — all read legibly, safe inset
    respected, no text overlap.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 99.739s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — same structural disposition as every other hai-simple reel in
this family (B00 writer + BCRY + BHTF + BOUT are REMOTION by skill
contract). Manim clips were time-stretched to fill measured audio (B01
9.25s→20.4s at 2.20x, B02 9.1s→17.8s at 1.95x, B03 11.6s→19.4s at 1.67x);
spot-checked in Gate V, no blocking artifacts.

Metadata file written:
`knowledge-work-plugins--claude-liam-cowork-plugin-customizer.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `knowledge-work-plugins` matches the map's
`knowledge-work-plugins` prefix directly — plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
