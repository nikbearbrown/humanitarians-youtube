# BUILD-LOG — knowledge-work-plugins--claude-liam-financial-statements

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-financial-statements/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the financial-statements finance
Claude Tag Plugin skill). 7 beats: B00 cold open (ClaudeComposerAsk), B01
anatomy (skill = folder + SKILL.md), B02 pipeline (Steps section, linear
execution), B03 design tell, BVDT verdict (ClaudeVerdictArtifact), BHTF
handoff, BOUT outro — all already REMOTION, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00; no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot.

**Unlike the `cash-flow-snapshot` sibling redo in the same batch, this
source's template slot filled correctly at every occurrence.** The
skill's own description survives intact in the source's B00/B03/BVDT
narration: "Generate financial statements (income statement, balance
sheet, cash flow) with period-over-period comparison and variance
analysis. Use when preparing a monthly or quarterly P&L, closing the
books and need to flag material variances, comparing actuals to budget,
building a financial summary for leadership review, or looking up GAAP
presentation requirements and period-end adjustments." No local copy of
`financial-statements`'s own `SKILL.md` exists on this machine (its path
in the source metadata, `/Users/bear/Documents/CoWork/…/finance/skills/
financial-statements/SKILL.md`, resolves on a different machine), so this
redo states the mechanism and documented job the source confirms and does
not invent the specific numeric variance threshold, GAAP line items, or
output layout — logged in QUESTION.md and CARRY-OUT.md.

Given this reel's beat count (7, matching the source exactly per the
redo-mode "keep beat count" rule), the body beats compress the source's
three Teardown beats (B01 anatomy, B02 pipeline, B03 design tell) into
three GRAPHIC beats (B01, B02, B03) built fresh in Manim, following
hai-simple's Plain-register spine (stakes → wrong guess, falsified →
mechanism / anchor planted → anchor payoff / both directions) instead of
the source's anatomy/pipeline/tell structure.

B00 replaced the source's `ClaudeComposerAsk` cold open (which stated the
skill name with no wrong-guess framing) with `BrutalistHesitantWriter`
(WRITER LAW: "decides" → "checks" — the naive assumption that Claude
applies its own accounting judgment to decide what counts as a material
variance, corrected to the fact that it checks the numbers against a
rule already written in the file). Register re-registered Teardown →
Plain: the source's B03/BVDT framed the same facts as "what it gets
right" / "what it bites" and a scored verdict — Teardown language —
restated here as mechanism and a determinism fact with no verdict on the
skill's design. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Anchor: B02 → B03, the "financial
statements · Q1" request submitted through four ordered steps (build
statements, compare periods, flag variances, return output), then run
again for an identical output, paid off against a Q2 request through the
same steps producing a different (but structurally identical-shaped)
output.

**Because every claim in this reel is the source's own confirmed
statement** — a folder/file Claude reads, not a judgment module; the
documented job (three statements, comparison, variance analysis, use
cases); linear step execution; same-input-same-output; the limit is only
what the file says — and none of it is this reel's inference, **no
ONE-FLAG beat was needed**, logged as a deliberate choice in both
QUESTION.md and SCRIPT.md's register audit, not an omission.

Built end to end this invocation:

1. GATE T (`type_check.py`) — PASS before any audio/render spend.
2. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.75s, B01 20.33s, B02 19.37s, B03 21.91s, BCRY 7.89s, BHTF 12.03s,
   BOUT 3.58s.
3. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `FSB01Scene`/`FSB02Scene`/`FSB03Scene` per the naming-collision lesson
   documented in sibling hai-simple BUILD-LOGs) and `render_scenes.py`;
   all three rendered clean on the first pass.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the tool's 120s window and was moved to a background task by
   the harness; blocked on it directly with `TaskOutput` rather than
   ending the turn, per the one-shot-invocation law — all 4 beats
   completed, exit 0.
5. Verified B00 directly before compiling: `media/B00.mp4` measured
   10.77s (TIMING LAW floor is 8s); pulled a frame at t=9.5s and read the
   correction ("decides" → "checks") fully visible, cursor resting at the
   end of the complete corrected question ("Claude checks what's a
   material variance. Right?") — WRITER LAW satisfied.
6. First `compile.py` pass: 7/7 real, no slate, 96.9s, 4K, GATE AUDIO
   PASS (-24.0 dB).

**Gate V (visual) — one defect found and fixed, not shipped around:**
pulled 12 frames at 8s intervals across the full 96.9s runtime and read
them directly. On the first pass, the B02 "THE ANCHOR" output card
(`Q1 — INCOME / BALANCE / CASH, 1 FLAGGED`) extended past the right edge
of the 3840×2160 frame — confirmed by cropping the frame's right edge,
which showed the card's rounded border and part of its text cut off by
the canvas boundary. Root cause: `scenes.py`'s B02 `out_card` was
positioned at `RIGHT * 5.9` with width 3.0, placing its right edge at
Manim x≈7.4 against a half-frame-width of ≈7.11 — a genuine overflow, not
a rendering artifact. Fixed by narrowing the card to width 2.6 and moving
it to `RIGHT * 5.5` (right edge ≈6.8, inside the safe frame), re-rendered
`FSB02Scene` only, and recompiled with `--force`. Re-pulled all 12 frames
plus the outro tail: THE ANCHOR now sits fully inside frame with margin,
and every other beat (B00's correction, B01's "no separate judgment
module" struck-through card, B03's THE ANCHOR RETURNS three-way
comparison, BCRY's carry-out, BHTF's Your Turn composer card, BOUT's
title/subscribe card) read cleanly — no overlapping text, safe inset
respected. **Noted, not a defect introduced here:** `OutroCTA` renders on
a flat-white ground rather than the humanitarians cream (`#F3EBDD`) —
same shared-component behavior already logged unremarked in sibling
hai-simple reels (e.g. `cash-flow-snapshot`, `redshift-api`); out of this
reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 96.86s;
  mp4 mtime (1788486419) newer than beat_sheet.json mtime (1788486090)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your
Turn) + BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC
body beats for this 7-beat reel — same disposition as every other short
hai-simple reel in this family.

Metadata file written:
`knowledge-work-plugins--claude-liam-financial-statements.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's own family `knowledge-work-plugins` matches that exact prefix
in the map — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
