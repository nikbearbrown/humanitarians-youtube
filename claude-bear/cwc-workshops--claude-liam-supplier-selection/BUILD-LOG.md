# BUILD-LOG — cwc-workshops--claude-liam-supplier-selection

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-supplier-selection/beat_sheet.json`
(a Teardown skill-teardown-format reel built from the `agent-decomposition`
workshop's "supplier-selection" Claude Skill). Question, facts, and body
argument carried over unchanged from the source SKILL.md: a Claude "skill"
is a folder Claude reads before it acts; "supplier-selection" is a folder
with one file, `SKILL.md`, whose method is `score = 0.5 × (1 − norm_price)
+ 0.3 × (1 − norm_lead_time) + 0.2 × reliability` — price normalized and
weighted at 50%, lead time at 30%, reliability at 20%; the highest score
wins, with tie-breaks on lowest price, then lowest lead time, then
alphabetical supplier id; the file also lists supplier-specific override
notes (e.g. an unlisted price break, a strict MOQ enforcement, an
import-lead-time caveat) explicitly marked as "not in the catalog data,"
to be applied after the score is computed and capable of changing the
pick. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("cheapest" → "highest-scoring" —
the newcomer's actual misconception, that Claude just sorts by price,
picked back up at B02's wrong-guess beat).

Register re-registered Teardown → Plain: the source's B03 design-tell beat
ran a Popper move ("what it bites: anything outside the spec") and BVDT
ran a Plato move (artifact vs. world) as design judgment on whether
"supplier-selection" is a *good* skill; both were dropped and their facts
folded into B05 as plain consistency/limit statements, no verdict
language. Close re-skinned to `WantQuote` / `ClaudeComposerAsk` /
`OutroCTA` with @HumanitariansAI and Liam's sign-off. No source beat was
ai-video-prompt, pantry, or a human-drop slot — NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00. Source ran 7 beats
(B00/B01/B02/B03/BVDT/BHTF/BOUT); this redo runs 9 (B00–B05 body,
BCRY/BHTF/BOUT) — the split adds the wrong-guess beat (B02) and a
dedicated both-directions beat (B05) that Plain register requires and the
Teardown source folded into fewer beats. Full six-move + beat-count audit
in SCRIPT.md.

Built following the identical shape of the sibling redo
`cwc-workshops--claude-liam-reorder-policy` (same source series, sibling
skill referenced inside supplier-selection's own SKILL.md via the
"expedite override" clause, already delivered) — its `scenes.py` chip-row
template (itself a known-passing baseline verified against GATE T) was
copied and re-parametrized for this reel's content, including extending
the mono-font chip detection to `"supplier"`-prefixed labels.

Built from scratch this session: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (9 beats), scenes.py + render_scenes.py (Manim "chip row"
template, adapted from the verified sibling reel
`cwc-workshops--claude-liam-reorder-policy/scenes.py`).

Pipeline run in full:
1. `generate_audio_kokoro.py` — 9/9 beats, `am_onyx`, actual_duration_s
   written back. B00 measured 10.2s (TIMING LAW floor is 8s — met).
2. `render_scenes.py` — 5/5 GRAPHIC beats (B01–B05) rendered via Manim, no
   failures.
3. `remotion_scenes.py` — 4/4 REMOTION beats (B00, BCRY, BHTF, BOUT)
   rendered, foreground (auto-backgrounded past the tool's 120s timeout;
   blocked on it explicitly via TaskOutput per the ONE-SHOT/COMPLETION
   LAW rather than ending the turn) — exit 0.
4. `compile.py` — `cwc-workshops--claude-liam-supplier-selection.mp4`,
   9/9 beats real (no slate), 87.5s, 3840×2160.

**Gates:**
- content-check: PASS (9 beats, no violations)
- frame-check: PASS (3840×2160, 9 beats, no violations)
- lane-check: PASS (cut=master, no lane violations)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio present, duration 87.52s; mp4 mtime
  (1788244096) newer than beat_sheet.json mtime (1788244016) —
  COMPLETION LAW satisfied
- Gate V (visual): pulled 15 frames at 6s spacing across the full runtime
  and read them directly — B00's correction ("cheapest" → "highest-
  scoring") is legible, landed and settled by 6s, full corrected question
  readable by 9s; every chip beat reads cleanly (no overlap, safe inset
  respected, @HumanitariansAI handle on B00); the B03→B05 anchor pair
  (PRICE 50% / LEAD TIME 30% third-chip payoff) reuses the identical
  three-chip composition so the payoff reads as the same object
  returning; BCRY carries the carry-out sentence alone, serif, large;
  BHTF shows the corrected handoff command and @HumanitariansAI folder
  label; BOUT shows the title, SUBSCRIBE, and handle. No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.2s (≥8s requirement met); the
  "cheapest" → "highest-scoring" correction lands on screen, confirmed by
  direct frame pull at 6.0s and 9.0s into the clip.

**Non-blocking warning (compile.py):** motion histogram graphic:5
remotion:4 — graphic at 55%, over the ~40% pantry cap in MOTION.md.
Structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against a compact 5-beat GRAPHIC body that mirrors the source's
own thin 3-body-beat argument (source: one file, one formula, tie-break
rule) plus the wrong-guess and both-directions beats Plain register
adds — the ratio follows beat count on a short, source-thin reel, not a
choice made in this build. Identical to the sibling
`claude-liam-reorder-policy` build's logged warning. Logged per the
honesty rule rather than padding beat count to dodge the warning.

Metadata file written: `cwc-workshops--claude-liam-supplier-selection.md`
(channel @HumanitariansAI). Per playlists.json, `SUBJECT.json`'s `skill`
field (`hai-simple`) has a direct map entry → **Playlist: Claude Basics**,
and the content (what decides a Claude Skill's output) matches that
playlist exactly — no override needed. Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
