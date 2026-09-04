# BUILD-LOG — financial-services--claude-liam-3-statement-model

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-3-statement-model/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
unlike some sibling hai-simple redos (`claude-for-legal--claude-liam-handbook-updates`,
`ai-inventory`, `fto-triage`, `gap-surfacer`), this source sheet is NOT a
placeholder shell. Its narration already states the `3-statement-model`
skill's real facts: it completes, populates, and links 3-statement
financial model templates (Income Statement, Balance Sheet, Cash Flow
Statement); triggered when asked to fill out model templates, complete
existing model frameworks, populate financial models with data, complete a
partially filled IS/BS/CF framework, or link integrated statements within
an existing template structure; Claude reads SKILL.md and executes the
steps linearly. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/.../model-builder/skills/3-statement-model/SKILL.md`)
does not exist on this machine (different machine's home directory), but
no reconstruction was needed — the source beat_sheet.json's own narration
carried enough to redo faithfully.

**The call:** register re-registered Teardown -> Plain. Source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (a fixed
list of steps that link an existing template) and its two failure
directions (tied out is not right; blank is not broken) as properties of
the practice, never a verdict on the skill's design. Source's BVDT verdict
recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW. B00
replaced the source's `ClaudeComposerAsk` cold open (itself already
Remotion, not AI-video/puppet — no NO-GENAI violation in the source) with
`BrutalistHesitantWriter` per WRITER LAW: "judgment" -> "the steps" — the
naive assumption that filling in a model takes financial judgment,
corrected to: it takes following a written set of steps. Added a
wrong-guess beat (B01: analyst judgment vs. written steps, falsified by
"ask for something the steps don't cover and it won't improvise") and an
anchor (B02 -> B03: net income traveling income statement -> retained
earnings -> cash flow statement, planted then paid off) per this factory's
PHASE 1 structure requirement — the source's Teardown shape (anatomy /
pipeline / design-tell / verdict) carried neither. Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the source's
7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT) per the redo contract.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.6s (well clear of the >=9s TIMING LAW
   floor) on the first narration draft (34 words + `lead_silence_s: 0.8`).
   Durations: B00 10.6s, B01 18.5s, B02 14.6s, B03 18.7s, BCRY 9.8s, BHTF
   18.8s, BOUT 4.2s (+1.0s tail -> 5.2s).
2. Verified B00's correction on frame pulls at t=6.5/9.5/10.3s: "judgment"
   still mid-typing (accent color) at 6.5s, fully backspaced and replaced
   with "the steps?" by 9.5s, legible with margin before the 10.6s cutoff.
   TIMING LAW satisfied on the first pass — no rewrite needed.
3. Wrote `scenes.py` (3 Manim scenes, reel-unique names `TSMB01Scene` /
   `TSMB02Scene` / `TSMB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground, no render failures at any point.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the shell moved it to a background task past the 120s inline timeout;
   blocked on it with `TaskOutput` rather than ending the turn — no
   unsupervised background render was left running). All four rendered
   clean on the first pass.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (GATE AUDIO pass on the first compile).
6. GATE T (`type_check.py`) FAILED on the first pass: 2 pixel beats.
   - B02: min-size (an 18px label under the 20px floor) + 100% bbox-overlap
     — a "NET INCOME" token card was landing directly on top of the
     un-faded "retained earnings"/cash-flow row labels it was meant to
     replace. Root cause fixed, not patched: removed the floating token
     entirely and replaced the travel mechanic with the same
     recolor-plus-connector-arrow pattern the `handbook-updates` sibling
     used successfully (recolor the origin row TERRA, draw an Arrow to the
     next card, recolor that row TERRA, repeat) — no two labels ever
     occupy the same space at once. Also bumped row/label font sizes for
     margin (16px -> 18-19px).
   - B03: contrast fail (2.74:1 vs the 4.5:1 WCAG floor) on non-bold TERRA
     body text, plus a 100% bbox-overlap from a unicode "✓" checkmark glyph
     whose bounding box read as merged with adjacent text. Fixed by
     dropping the checkmark glyph entirely (replaced with plain "OK" text)
     and switching every readable label in the beat from TERRA to INK —
     TERRA is now reserved for non-text accents only (borders, connector
     lines, the strike-through), matching this reel's own B01/B02 usage and
     the ACCENT LAW. Re-rendered both beats, recompiled: GATE T -> PASS,
     0 FAILs, second pass.
7. Gate V (visual, manual): pulled frames every 4s across the full 96.2s
   runtime (24 frames) and read every one directly. Found ONE real defect
   not caught by GATE T: in B01, the "??? — not on the list" line sat
   *inside* the WRITTEN STEPS card and printed directly through its bottom
   border (visible at t=20s and t=24s) — the card was sized for 4 steps,
   not 5 lines of content. Fixed by moving that line entirely outside the
   card (`.next_to(right_box, DOWN, buff=0.4)` instead of stacking under
   the in-card step list) so it can never be clipped by the border it sits
   near. Re-rendered B01, recompiled, re-pulled frames at t=18-26s: line
   now sits cleanly below the card with visible margin, caption below it
   with margin to the bottom of frame. Re-ran GATE T after this fix ->
   still PASS (card-clip §8.13 did not previously catch this one, since it
   is a border-touch rather than an edge-of-frame clip — logged as a gap
   in the automated check, not something the script was asked to change).
   No other defects found across B00/B02/B03/BCRY/BHTF/BOUT.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master -> mean_volume **-24.0 dB**, max -3.1 dB. Master mtime
   (1788255718) is newer than beat_sheet.json mtime (1788254863).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-handbook-updates`,
`claude-code--claude-liam-writing-rules`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B02/B03 fixes above)
- Gate V: PASS, second pass (B01 card-clip fix above) — no defects remain
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -3.1 dB
- ffprobe: duration 96.208s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as the `ai-inventory` and `handbook-updates` sibling reels.

Metadata file written:
`financial-services--claude-liam-3-statement-model.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the two fix
passes above). Proceeding to Phase 4 (4K render + deliver.py) in this same
invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-3-statement-model.mp4 \
   financial-services--claude-liam-3-statement-model-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-3-statement-model/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-3-statement-model/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `e7214a0e`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
