# BUILD-LOG — claude-for-legal--claude-liam-legal-hold

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-legal-hold/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about
the litigation-ops skill `legal-hold`.

**Source-fidelity: no gap this time.** Unlike the `case-brief` and
`build-guide` sibling redos (whose source SKILL.md files were unreachable
from this machine), the actual `legal-hold` SKILL.md **was found and read
in full**: `/Users/nik/Documents/Cowork/anthropics/claude-for-legal/litigation-legal/skills/legal-hold/SKILL.md`.
Every specific claim in this reel (the confirmation gate before issuing or
releasing a hold — *"Do not send the notice without an explicit yes"* —
the four flags `--issue/--refresh/--release/--status`, and the "What this
skill does not do" edge list) is a direct read of that file, logged in
QUESTION.md/SCRIPT.md. This let the reel's wrong-guess/mechanism spine be
grounded in the skill's actual documented behavior (a real confirmation
gate) rather than a generic "delete the folder" case.

**Facts kept unchanged from source:** the skill's stated purpose (issue,
refresh, release, or report on legal holds; drafts the hold notice as
.docx; updates `legal_hold` fields in `_log.yaml`; calendars the next
refresh); a skill is a folder Claude reads before it acts; SKILL.md is one
file read top to bottom, executed step by step.

**New content, grounded in the real SKILL.md (not invented):** the
confirmation gate before the two consequential steps (`--issue`,
`--release`) and the four explicit "what this skill does not do" bullets
(does not enforce preservation, does not set scope alone, does not
auto-refresh without review, does not send the notice) became this redo's
wrong-guess/break and payoff/limit beats.

**Beat-count note (redo):** source is 7 beats (B00, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF your-turn, BOUT outro) — no
explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats, so this redo expands modestly,
identically in shape to the `case-brief`/`build-guide` sibling redos: B01
(stakes) + B02 (wrong guess, broken) new; B03/B04/B05 carry the source's
anatomy/pipeline/design-tell facts to the anchor; B06 new anchor-payoff;
B07 (both directions) new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT = 11
beats.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude issues legal
holds" means Claude decides, on its own, when a lawsuit calls for freezing
documents. Typed text: "Claude decides who's on hold / from the legal-hold
skill. / What is a skill?", trigger "decides" → replacement "was told",
ending on the real question. Audio 11.41s, clearing the ≥8s WRITER LAW
floor with margin — verified on a late frame (t=9.5s) that the correction
resolves to "was told" before the beat ends.

**Body beats (B01–B07):** all Manim GRAPHIC scenes, reusing the
chip-row/chip-stack renderer pattern from the `case-brief` sibling redo
verbatim, adapted in this reel's own `scenes.py` with legal-hold-specific
chip labels and narration grounded in the real SKILL.md. Anchor pair: B03
plants `legal-hold/` + `SKILL.md` as two plain chips; B06 returns the
identical composition with `SKILL.md` accented. Close: BCRY `WantQuote`
(carry-out), BHTF `ClaudeComposerAsk` (`folderLabel: "@HumanitariansAI"`),
BOUT `OutroCTA` (`@HumanitariansAI`). All Remotion + WantQuote component
prop schemas verified renderable via `./art scenes --check` before
authoring the sheet (GATE L).

**GATE T (type_check.py) — two real bbox-overlap FAILs, root-caused and
fixed, not worked around:**

1. B02 and B07 both failed `bbox-overlap §8.6b` on first render: a chip's
   hollow box-outline (drawn via `RoundedRectangle(stroke_width=3)`) was
   itself being counted as a valid oversized "text-run" blob by
   `type_check.py`'s color-based `ink_mask`/`visible_text_mask` detector
   (it does not distinguish vector strokes from glyphs), because its
   border pixel density crossed the checker's own 4%-of-bbox-area "nearly
   empty, not text" floor. Since the label text sits inside that same box,
   it registered as 100%-contained overlap. Root-caused by writing a small
   standalone script against `type_check.py`'s own `blob_bboxes` /
   `text_run_bboxes` functions and inspecting the exact flagged pixel
   regions (not by guessing from rendered frames alone) — confirmed the
   flagged blob's bbox matched the chip box's pixel dimensions exactly.
   Fix: reduced `_chip()`'s `stroke_width` (3 → 1.5 → 1.0 for
   chip_stack's wider/shorter boxes, which have a higher perimeter/area
   ratio than chip_row's boxes and needed the lower value to clear the
   same 4% floor). Verified with the same diagnostic script before
   re-rendering, not just by re-running the full gate blind.
2. A red herring along the way: B07's title text ("NEITHER ONE IS PROOF")
   was initially suspected as the overlap source (a nested sub-blob inside
   the title's bbox) and rewritten twice before the diagnostic script
   proved the flagged bbox coordinates were IDENTICAL across three
   different title strings — meaning the title was never the cause; the
   B07 chip-stack box (same root cause as B02) was. The title was kept at
   the improved, more natural wording ("NOT PROOF, EITHER WAY") since it
   reads better than the original, but the actual fix was the stroke-width
   change. Logged here so a future pass on this scenes.py doesn't
   re-diagnose the same false lead.

GATE T: PASS on the next run (0 FAILs across all 11 beats) after both
fixes, with all 7 GRAPHIC beats re-rendered for visual consistency (the
`_chip()` helper is shared).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-legal-hold.mp4`, 119.8s. One non-blocking
WARNING carried through compile: GRAPHIC beats are 7/11 (63%), over the
toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md) — noted,
not treated as a gate; this reel is legitimately diagram-heavy (a skill's
anatomy/mechanism/spec argument reads naturally as labeled-chip diagrams)
and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled ~2fps frames across the full runtime and
read one representative frame per beat by hand — all legible, correct chip
content, safe insets, no overlapping text, the B03→B06 anchor pair visually
identical as intended, B07's vertical-stack layout reads cleanly, B00's
correction frame confirmed, outro carries the @HumanitariansAI /
SUBSCRIBE HAI skin correctly.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (13:41) is newer than
beat_sheet.json's last content edit (13:32) — beat_sheet.json was NOT
touched after this point, per the "never touch beat_sheet.json after
compile" law; any further fix from here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-legal-hold-4k.mp4` created — a
copy of the compiled master, which was already genuine 3840×2160 (the
Remotion beats are natively 4K; the Manim beats are 1080p source upscaled
into the 4K canvas by the compile step itself, same as every other GRAPHIC
beat in this pipeline). Wrote `claude-for-legal--claude-liam-legal-hold.md`
(YouTube description, @HumanitariansAI, playlist "Claude Basics", direct
code link, AI disclosure). Ran `deliver.py --push` to stage
`DELIVERY/claude-for-legal--claude-liam-legal-hold/` and commit text
artifacts to the humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-legal-hold/` — committed and
pushed successfully.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). 4K delivered to both
targets.
