# BUILD-LOG — knowledge-work-plugins--claude-liam-incident-response

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-incident-response/beat_sheet.json`
(the Anthropic `incident-response` skill, Teardown/skill-teardown source, no
SCRIPT.md — source `beats[*].narration_text` served as the locked script).
Built from a clean SUBJECT.json only; no prior-session artifacts were
present in the reel dir.

Question, facts carried over unchanged: the skill's job is triage,
communicate, write postmortem; its trigger phrases ("production is down,"
a severity-assessment alert, a mid-incident status update, writing the
postmortem after resolution); its mechanism (SKILL.md is the instruction
set, read before acting, a Steps section executed linearly, no branching
unless a step says so); its behavior (same input → same output every run;
limited to what the file states). Source's 7-beat skill-teardown chassis
(B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict,
BHTF your-turn, BOUT outro) was expanded to 11 beats (B00 + NB01–NB07 +
BCRY/BHTF/BOUT) so hai-simple's required stakes/wrong-guess/mechanism/
anchor/both-directions/carry-out spine each got its own beat and the anchor
(a 2 a.m. "production is down" alert) could be planted at the stakes and
paid off at the limit — full accounting in SCRIPT.md's "Beat-count note
(redo)". No new facts introduced; NB01–NB07 restate exactly what source
B00/B01/B02/B03/BVDT already said, reordered and stripped of verdict/
judgment language. B00 replaced the source's `ClaudeComposerAsk` cold open
with `BrutalistHesitantWriter` (text: "Claude's incident response is pure
instinct. Isn't it?", trigger `instinct` → `instructions`, single-word
trigger per the books--claude-liam-troubleshooting BUILD-LOG lesson that a
multi-word `triggerWords` phrase silently never matches).

**Build sequence, foreground throughout (per this skill's ONE-SHOT
completion law — no background render steps):**

1. `generate_audio_kokoro.py` — 11/11 beats, $0.00. First pass measured B00
   at only 7.64s (narration too short for the WRITER LAW's ≥9s window);
   lengthened the narration to 34 words ("...at two in the morning...So
   what do they actually say?") and regenerated B00 alone — 10.18s,
   comfortably clearing the floor.
2. `render_scenes.py` (Manim) — all 7 GRAPHIC beats (NB01–NB07) rendered
   clean on the first pass, reusing the exact chip-row renderer and GATE T
   mitigations (EB Garamond not Montserrat, underline accent not filled
   terracotta, wrap-not-shrink for long labels) proven in
   `books--claude-liam-troubleshooting/scenes.py` — only `BEAT_CONTENT`
   changed.
3. `remotion_scenes.py` — all 4 REMOTION beats (B00/BCRY/BHTF/BOUT)
   rendered clean on the first pass. (First invocation hit the harness's
   2-minute default command timeout with zero output written — not a
   render failure, just an undersized timeout for four `npx remotion
   render --scale=2` calls; re-ran the same command with a 10-minute
   timeout in the foreground and it completed normally. No background
   process was left running at any point.)
4. B00 WRITER LAW verification: pulled a 0.1s-spaced frame sequence across
   t=3.0–5.4s (`fps=10` extract + tile contact sheet) rather than
   whole-second samples, since whole-second sampling (t=4,5,6,9) happened
   to land entirely after the swap and looked like "no correction ever
   shown." The finer sequence confirms the correction plays exactly as
   designed: "instinct" fully typed in terracotta and held (~t=3.0–3.4s),
   backspaced letter by letter (~t=3.5–3.9s), retyped as "instructions."
   and held (~t=4.0s onward) — well inside the 10.18s beat.
5. `compile.py --height 2160` — 11/11 beats filled real (no slate) on the
   first attempt, 115.0s, 3840×2160.

**Gates:**
- content-check: PASS (11 beats, no violations)
- frame-check: PASS (3840×2160, 11 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs on the first run — no chip-render
  fixes needed this time (labels were short enough to stay clear of the
  min-size/wrap edge cases the troubleshooting build hit)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 115.0s; mp4
  mtime (23:51:38) newer than beat_sheet.json mtime (23:46:50)
- Gate V (visual): pulled frames at 6s spacing across the full runtime (19
  frames) via a contact sheet, plus targeted single-frame checks of BCRY,
  BHTF, and BOUT at their midpoints. No blockers: every chip-row beat
  legible with safe inset, no text overlap, @HumanitariansAI handle
  correct on B00 (first-beat overlay only), HAI outro skin (OutroCTA,
  SUBSCRIBE + @HumanitariansAI) correct on BOUT, carry-out quote + sparkline
  legible on BCRY, Your Turn prompt legible on BHTF.
- B00 TIMING LAW: `actual_duration_s` 10.18s (≥9s window met after the
  narration-length fix above); the "instinct"→"instructions" correction
  lands on screen and holds, verified at 0.1s resolution.

**Non-blocking warning (compile.py):** motion histogram graphic:7
remotion:4 — graphic at 63%, over the ~40% pantry cap in MOTION.md.
Structural, same disposition as every `books--claude-liam-*` /
`knowledge-work-plugins--claude-liam-*` sibling in HAILOOP-LOG.md:
hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION against a
GRAPHIC body carried over from the source's argument. Logged per the
honesty rule rather than reworking beat count to dodge the warning.

Metadata file written: `knowledge-work-plugins--claude-liam-incident-response.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per playlists.json, `knowledge-work-plugins` is a direct,
literal key in the map (no fallback reasoning needed). Direct code link per
DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
