# BUILD-LOG — financial-services--claude-liam-financial-plan

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-financial-plan/beat_sheet.json`,
following the sibling `financial-services--claude-liam-dcf-model` redo (built
the same day) as the structural template.

**Source-gap finding:** the source sheet is NOT a placeholder shell — its B00
narration states the `financial-plan` skill's real facts in full: build or
update a comprehensive financial plan covering retirement projections,
education funding, estate planning, and cash flow analysis; used for new
client onboarding, annual plan reviews, or scenario modeling; triggers on
"financial plan", "retirement plan", "can I retire", "education funding",
"estate plan", "cash flow analysis", or "plan update". (B03/BVDT/BHTF carry a
truncated repeat of the same sentence, cut off mid-word — a template
character-limit artifact, not a second fact; B00's is the complete version.)
No reconstruction needed. `source_skill` path does not exist on this machine
(different machine's home directory) — irrelevant, since the source sheet's
own narration already carries the facts.

**The call:** register re-registered Teardown -> Plain. Source's
B03/BVDT "what it gets right / what it bites" design-tell verdict removed;
Plain keeps only the mechanism (fixed steps run over given inputs) and its
two failure directions. B00 replaced the source's `ClaudeComposerAsk` cold
open with `BrutalistHesitantWriter` per WRITER LAW: "judgment" -> "a skill"
— the naive assumption that a financial plan reflects Claude's own judgment
about the client, corrected to: it is Claude running a skill's fixed steps
over the inputs it was given. Added a wrong-guess beat (B01: advisor
judgment vs. SKILL.md-named steps, falsified by "ask for something outside
that list, and there's no independent expertise underneath to fall back
on") and an anchor (B02 -> B03: the retirement-age dial driving a single
monthly-savings-target readout, planted then paid off across a small
scenario grid) per this factory's PHASE 1 structure requirement — the
source's Teardown shape (anatomy/pipeline/design-tell/verdict) carried
neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF,
BOUT) per the redo contract.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.71s (clear of the >=9s/>=8s TIMING LAW
   floor) on the first narration draft (33 words + `lead_silence_s: 0.8`).
   Durations: B00 10.71s, B01 27.31s, B02 19.37s, B03 24.94s, BCRY 10.62s,
   BHTF 22.02s, BOUT 4.46s (+1.0s tail).
2. Verified B00's correction on frame pulls at t=6.5s/9.5s: "judgment" still
   mid-typing (accent color) at 6.5s, fully backspaced and replaced with
   "a skill?" by 9.5s, legible with margin before the 10.7s cutoff. TIMING
   LAW satisfied on the first pass.
3. Wrote `scenes.py` (3 Manim scenes, reel-unique names `FPB01Scene` /
   `FPB02Scene` / `FPB03Scene`) and `render_scenes.py`.
4. First Manim render pass sized `self.wait()` calls to my own duration
   *estimates* (22/17/23s), not the real Kokoro output (27.31/19.37/24.94s).
   `compile.py` silently covered the gap by time-stretching the clips
   2.2-2.8x ("B01: clip 11.9s slowed 2.29x to fill 27.3s beat"), which would
   have played every animation in visible slow motion. Root-caused rather
   than accepted: retimed the `self.wait()` calls in all three scenes to
   match the actual narration durations (new natural clip lengths 27.3s /
   19.4s / 24.9s, within 0.1s of the audio), re-rendered, recompiled —
   0 slowdown messages, clean 1:1 timing.
5. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground —
   all four rendered clean on the first pass.
6. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (4K LAW),
   mean_volume -24.0 dB.
7. GATE T (`type_check.py`) FAILED on the first pass: 1 min-size (§8.1) in
   B03 — "smallest text run 11px < floor 20px". Root-caused: the B03
   scenario grid is scaled 0.72x after its reveal (`grid.animate.scale(0.72)`
   ), and the grid unit labels were sized (font_size 15/18) for their
   pre-scale appearance, landing at ~11px effective height post-scale — well
   under the 20px/1080-logical floor. Fixed the actual content: enlarged the
   grid unit labels (font_size 15->30, 18->34) so they clear the floor after
   the 0.72x scale-down, with a wider card to match (2.4x1.7 -> 2.7x2.0).
   Re-rendered, re-checked: floor violation dropped from 11px to 14px, same
   FAIL — so the grid labels were not the (only) culprit. Traced it to the
   "$1,200 → $1,850" / "$1,200 ≈ $1,240" comparison lines below the grid: the
   arrow/approx-equals glyphs (→, ≈) render with a much shorter ink-height
   than the surrounding digits regardless of font_size, so bumping their
   font_size (19->30) only partially closed the gap (11px->14px). Removed
   the glyphs outright rather than keep inflating font size around them
   ("$1,200 to $1,850" / "$1,200 vs $1,240" — plain words, no symbol whose
   glyph metrics fight the floor), and while touching that block also
   enlarged the two remaining caption lines (font_size 15/16 -> 22) and
   dropped trailing commas/periods for margin. Re-rendered, recompiled,
   re-checked GATE T: PASS, 0 FAILs.
8. Gate V (visual, manual): pulled frames every 4s across the full 120.4s
   runtime (30 frames) and read every one directly. Found ONE real defect
   GATE T's automated checks did not catch: in B01, the "SKILL.md STEPS"
   card label and the first trigger-tag line ("onboarding") occupied
   near-identical vertical positions (`right_label` at
   `box.get_top() + DOWN*0.4`, `trigger_lines` centered at
   `box.get_center() + UP*0.75`) and rendered fused into one illegible run
   ("SKILLoumnJudSTEPS") for the duration both were on screen. Fixed by
   separating them: `right_label` pulled up to `DOWN*0.3` from the box top,
   `trigger_lines` recentered lower at `UP*0.15`, `output_tags` pushed down
   to `DOWN*0.95` to keep clear of both. Re-rendered B01, recompiled,
   re-checked GATE T (still PASS) and re-pulled the full 30-frame sweep: the
   card now reads "SKILL.md STEPS" / "onboarding / annual review / scenario"
   / "RETIREMENT EDUCATION ESTATE CASH FLOW" cleanly, with legible margin
   between each line. No other defects found across B00/B02/B03/BCRY/BHTF/
   BOUT on the full sweep.
9. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final master
   -> mean_volume **-24.0 dB**, max -2.9 dB. Master mtime (1788299673) is
   newer than beat_sheet.json mtime (1788298472). Master already 3840x2160
   (4K LAW).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), third pass (B03 glyph/caption fix above)
- Gate V: PASS, second pass (B01 label/trigger-line overlap fix above) — no
  defects remain
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 120.44s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — same structural disposition as every other hai-simple reel in
this family (B00 writer + BCRY + BHTF + BOUT mandated REMOTION against 3
GRAPHIC body beats).

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback, fell through to matching the skill name itself:
`hai-simple` is a literal key in the map, resolving to **Claude Basics** —
same resolution as the `dcf-model` and `3-statement-model` sibling reels.

Metadata file written: `financial-services--claude-liam-financial-plan.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the three fix
passes above: Manim pacing, GATE T min-size, Gate V label overlap).
Proceeding to Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-financial-plan.mp4 \
   financial-services--claude-liam-financial-plan-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-financial-plan/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-financial-plan/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4).

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
