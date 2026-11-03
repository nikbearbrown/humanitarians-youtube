# BUILD-LOG — knowledge-work-plugins--claude-liam-choose-zoom-approach

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-choose-zoom-approach/beat_sheet.json`
(examining the Anthropic `choose-zoom-approach` skill: chooses the right
Zoom architecture for a use case, deciding between REST API, Webhooks,
WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone,
Contact Center, or a hybrid approach; anatomy = one-file SKILL.md
instruction set; pipeline = read→execute→return, linear, no branching
unless a step says so).

**Source-gap finding (logged, not asked — see QUESTION.md for full
detail):** the source's `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/.../zoom-plugin/skills/choose-zoom-approach/SKILL.md`)
does not exist on this machine (different machine's home directory), but
no reconstruction was needed — the source beat_sheet.json's own narration
already names the full set of surfaces and the hybrid option in enough
detail to redo faithfully.

**The call:** register re-registered Teardown → Plain. Source's B03 framed
"what it gets right / what it bites" as a design-tell verdict — Plain
instead states the mechanism (matching a use case's shape to a fixed list
of surfaces) and its two failure directions (a matched surface isn't a
finished build; an unclear/compound need isn't a failed match — hybrid is
one of the listed answers) as properties of the practice, never a verdict
on the skill's design. Source's BVDT verdict recap folded into a dedicated
BCRY carry-out beat per CARRY-OUT LAW. B00 replaced the source's
`ClaudeComposerAsk` cold open (itself already Remotion, not AI-video/
puppet — no NO-GENAI violation in the source) with
`BrutalistHesitantWriter` per WRITER LAW: "API" → "approach" — the naive
assumption that there's one Zoom API to call, corrected to: it's a choice
of approach among several. Added a wrong-guess beat (B01: "one API for
everything" vs. matched surfaces, falsified by a poll-vs-webhook case: a
REST API asked to report the instant a meeting ends can only be polled,
arriving late every time, where a webhook fires instantly) and an anchor
(B02 → B03: "notify us the instant a meeting ends" scanned against the
nine named surfaces, landing on Webhooks, then paid off with the two
both-directions cautions) per this factory's PHASE 1 structure, since the
source's Teardown shape (anatomy / pipeline / design-tell / verdict)
carried neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY,
BHTF, BOUT) per the redo contract.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries. B00 landed at 11.99s (clear of the ≥9s TIMING LAW floor) on
   the first narration draft (35 words + `lead_silence_s: 0.8`). Durations:
   B00 11.99s, B01 19.63s, B02 20.50s, B03 20.65s, BCRY 9.37s, BHTF
   15.04s, BOUT 3.88s (+1.0s tail).
2. Verified B00's correction on frame pulls at t=5/8/11s: "Which Zoom"
   still mid-typing at 5s, "Which Zoom approach / should I use?" fully
   corrected and settled well before the 12.0s cutoff at both 8s and 11s.
   TIMING LAW satisfied on the first pass.
3. Wrote `scenes.py` (3 Manim scenes, reel-unique names `ZAB01Scene` /
   `ZAB02Scene` / `ZAB03Scene`) and `render_scenes.py`; all three rendered
   clean in the foreground on the first pass.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the shell moved
   it to a background task past the 120s inline timeout — blocked on it
   with `TaskOutput` rather than ending the turn, per the one-shot
   COMPLETION LAW. Exit 0, all four beats rendered clean on the first pass.
5. First `compile.py` pass → 7/7 real (no slate), native 3840×2160 (THE 4K
   LAW), GATE AUDIO mean_volume -24.1 dB inline.
6. GATE T (`type_check.py`) FAILED on the first pass: 2 pixel beats — B02
   kerning (max inter-glyph gap 39px, 13.0× expected, on the Menlo-set
   quote text with embedded quotation marks) and B03 min-size (a 14px
   label under the 20px/1080p-logical floor). Fixed by switching the B02
   and B03 anchor-quote text from mono to `font=SERIF` (kerning cleared),
   and bumping B03's undersized labels — re-rendered, GATE T FAILED again
   (still 1 pixel beat: the B03 top quote+tag group, scaled to 0.65× after
   its intro beat, landed at 14px). Bumped that group's pre-scale font
   sizes (20→22) and the scale factor (0.65→0.8), plus widened/enlarged
   the two bottom-card labels that were also under floor (15–16px → 20px,
   with generous `_fit_text` max-width so they would not silently shrink
   back below it). Re-rendered B03 only, recompiled: GATE T → PASS, 0
   FAILs, third pass.
7. Gate V (visual, manual): pulled 20 frames at 5s spacing across the full
   102.0s runtime and read every one directly. All legible, correct
   content, no clipping or overlap, correct anchor payoff (B02→B03 the
   anchor quote scanning to Webhooks, then splitting into the two
   both-directions cards), correct carry-out/handoff/outro with
   `@HumanitariansAI` branding.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.1 dB**, max -2.6 dB. Master mtime
   (1788403422) is newer than beat_sheet.json mtime (1788402465).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), third pass (B02 font fix + two rounds of B03
  font-size fixes above)
- Gate V: PASS, first pass — no defects requiring a fix
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.6 dB
- ffprobe: duration 102.04s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking note (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your
Turn) + BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC
body beats for this 7-beat reel.

**Playlist resolution:** family `knowledge-work-plugins` matches the
`knowledge-work-plugins` prefix key in
`skills/make/hai-simple/loop/playlists.json` directly → **Extending
Claude — Skills, Plugins & Connectors**.

Metadata file written:
`knowledge-work-plugins--claude-liam-choose-zoom-approach.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors**, plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the fix
passes above). Proceeding to Phase 4 (4K render + deliver.py) in this same
invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
