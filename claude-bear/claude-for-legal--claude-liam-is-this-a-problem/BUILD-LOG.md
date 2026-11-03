# BUILD-LOG — claude-for-legal--claude-liam-is-this-a-problem

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-is-this-a-problem/beat_sheet.json`
— a "skill-teardown" sheet (metadata `register: "Teardown"`, `brand:
"claude-liam"`, `source_skill` pointing at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/product-legal/skills/is-this-a-problem/SKILL.md`,
a path that does not exist on this machine — same class of issue as the
`claude-code--claude-liam-plugin-settings` redo precedent, except there
the equivalent file existed locally under a mirrored path; here it does
not exist anywhere in this workspace). 7 beats in the source: B00 cold
open (`ClaudeComposerAsk`, REMOTION), B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF handoff, BOUT outro.

**Blocker encountered and how it was resolved (logged per the honesty
rule):** the source's own narration was never fully written. B01
("A skill is a folder Claude reads before it works…") and B02 ("The
pipeline is in the Steps section…") are complete, true, and generic to
any Claude skill — carried over into this reel essentially unchanged.
But B00, B03, BVDT, and BHTF carry a literal, unresolved `>` placeholder
exactly where the skill-*specific* claim belongs (e.g. BHTF: "I want to
`>`. Read the is-this-a-problem skill…"; B03: "Claude's job: `>`. What it
gets right…"). This is not a redaction — it's an unfinished batch build,
and the actual `SKILL.md` that would fill it in is unreachable (wrong
machine). Rather than treat an unreachable source file as a hard stop, or
invent specific legal criteria I have no basis for, I reconstructed only
the generic mechanism the skill's own name and its two *complete* beats
already establish: `is-this-a-problem` is a triage skill; its `SKILL.md`
defines, as explicit written conditions, what counts as "a problem" in
its domain; Claude's answer comes from matching a situation against that
list, not from independently judging severity. No specific legal
thresholds, statutes, or scenarios are invented anywhere in this reel —
see QUESTION.md for the full reasoning. This is the same generic-when-
unverifiable posture PHASE 1 requires for facts about Claude itself,
applied here to facts about a legal skill I can't read.

Facts carried over unchanged from the source (B01/B02, both complete in
the original): a skill is a folder; `SKILL.md` is the whole instruction
set in plain language; Claude reads the file, then follows it; the
pipeline lives in a Steps section and executes linearly, read → check →
answer.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "decide" → "check" — the naive
assumption that Claude weighs a situation and judges it, corrected to the
fact that a written skill defines what counts as a problem, and Claude is
checking a situation against that definition). Register re-registered
Teardown → Plain — the source had no judgment language to begin with in
B01/B02, so nothing needed cutting there; the reconstructed B03 states
the mechanism and its limit (reliable on covered cases, silent — not
wrong — on uncovered ones) with no verdict on whether the skill was well
designed. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Added an anchor (B02 → B03: the
checklist step, matching a situation against written conditions) and a
both-directions beat (B03) per this factory's PHASE 1 structure
requirement — the source didn't carry these as distinct beats, matching
the `plugin-settings` redo precedent's disposition.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   9.96s, B01 14.61s, B02 15.0s, B03 18.24s, BCRY 10.03s, BHTF 17.77s,
   BOUT 3.39s (total 89.0s).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `ITAPB01Scene` /
   `ITAPB02Scene` / `ITAPB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the
   foreground (the first invocation hit the tool's 2-minute default
   timeout after B00 finished; re-ran with a longer timeout and it
   picked up cleanly — B00 was skipped as already filled, BCRY/BHTF/BOUT
   completed).
4. B00 verified directly: `media/B00.mp4` = 9.97s (meets the ≥8s TIMING
   LAW floor). Pulled a frame at t≈9.5s: the correction ("decide" →
   "check") is complete and visible.
5. `compile.py` → `claude-for-legal--claude-liam-is-this-a-problem.mp4`,
   7/7 real (no slate), 3840×2160 (THE 4K LAW).

**GATE T (type_check.py):** FAILED twice before passing.
- First pass: B01 min-size FAIL — a `font_size=18` "Claude" figure label
  measured under the 20px floor. Bumped to 24 — FAIL persisted (measured
  min moved from 15px to 15px, meaning the true offender was a different,
  still-20px element).
- Second pass: bumped the two remaining `font_size=20` elements
  (`folder_txt`, the three `lines` labels) to 26 — measured min moved
  15px → 19px, confirming those were the actual offenders and revealing
  the scaling relationship (~0.73px measured per Manim font-size unit).
- Third pass: bumped both to 32 (with the folder card widened and the
  folder label split to two lines, and the pipeline label shortened from
  "check it against the conditions" to "check against conditions" to
  avoid frame-width overflow at the larger size) — **PASS, 0 FAILs.**

**Gate V (visual):** pulled 11 frames at 8s spacing across the full 90s
runtime plus a direct pull of the BOUT beat, and read all of them
directly. Caught two real defects not flagged by GATE T's pixel checks:
1. B01, t≈16s: the "Claude" figure circle traveled along a path that cut
   directly through the "check against conditions" text, and its
   "Claude" label was left behind at its start position instead of
   traveling with the circle (the label was never included in the
   `.animate.move_to` calls). Fixed by grouping figure + label into one
   `VGroup` and moving that group along a track below the text baseline
   instead of through it.
2. B03, t≈40–48s: the "unknown situation" hexagon glyph moved to
   `check_box.get_center()` — landing directly on top of the "check
   against conditions" label and remaining there through the following
   `no_card`/`distinct`-text beats. Fixed by landing the glyph beside the
   box (`check_box.get_left() + LEFT * 1.1`) instead of on top of its
   label.
Re-rendered both scenes, recompiled, re-ran GATE T (still PASS), and
re-pulled the full frame grid: B00's title-correction card, B01's
folder→file→pipeline sequence (figure now travels cleanly below the
text), B02's read/check/answer anchor-planting, B03's anchor return
(three "consistent" answers, then the uncovered glyph beside the check
box with "not named — no answer" and "not wrong — just outside the
checklist" legible and non-overlapping), BCRY's carry-out card, BHTF's
Your Turn composer card, and BOUT's outro/subscribe card all read
legibly with safe inset respected and no remaining text overlap.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, third pass — see above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 90.0s, video 3840x2160; mp4 mtime (1788106580) newer
  than beat_sheet.json mtime (1788105609)

**Non-blocking notes:** motion histogram remotion:4 graphic:3 — same
structural disposition as every other 7-beat hai-simple redo in this
factory (B00/BCRY/BHTF/BOUT mandated REMOTION, 3 body beats GRAPHIC).
Manim clips were time-stretched 1.22–1.72x by `compile.py` to fill
measured audio durations (B01 10.8s→14.6s, B02 9.5s→15.0s, B03
10.6s→18.2s) — checked by direct frame read at multiple timestamps per
beat; no visible artifacting (static-camera compositions, no fast
motion to stretch).

Metadata file written:
`claude-for-legal--claude-liam-is-this-a-problem.md` (channel
@HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's family
`claude-for-legal` has no entry in the map, so resolution fell through to
the `hai-simple` prefix, which maps to "Claude Basics" — not `_default`,
per the resolution order in PHASE 3 step 6) — plus the direct code link
per the DELIVERY CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-for-legal--claude-liam-is-this-a-problem.mp4 \
   claude-for-legal--claude-liam-is-this-a-problem-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Result: outbox staged at
`DELIVERY/claude-for-legal--claude-liam-is-this-a-problem/` (4K mp4 +
description); repo copy staged at
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-is-this-a-problem/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media); committed (`f6fc577a`) and pushed
to github.com/nikbearbrown/humanitarians-youtube.

**Status: DELIVERED.**
