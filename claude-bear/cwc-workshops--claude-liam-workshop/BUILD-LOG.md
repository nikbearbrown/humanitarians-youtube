# BUILD-LOG — cwc-workshops--claude-liam-workshop

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-workshop/beat_sheet.json` — a
Teardown-register skill-teardown of the Anthropic `workshop` Skill (a coach
for the Research Desk SEC-agents workshop, seven acts numbered zero through
six). Started fresh: only `SUBJECT.json` existed on open (confirmed via
`ls` and the empty `.filmloop/cwc-workshops--claude-liam-workshop.w44071.out`
log from an earlier queued run that never produced artifacts).

Facts re-grounded directly against the skill's own SKILL.md rather than
trusted from the source narration: the source reel's `source_skill`
metadata field points at a Bear-machine path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/cwc-workshops/research-desk/.claude/skills/workshop/SKILL.md`)
that does not exist here — same defect class as the `-weekly-report`,
`-forecasting`, and `-eval-audit-and-sweep` siblings, resolved the identical
way: the skill content itself is present, unchanged, at the Cowork-mirrored
path `/Users/nik/Documents/Cowork/anthropics/cwc-workshops/research-desk/.claude/skills/workshop/SKILL.md`,
read in full before scripting.

Reading the real SKILL.md changed the plan from what the source Teardown
narration alone would have supported: the source's B03 "design tell" was a
generic "specification-driven, what it bites is anything outside the spec"
verdict with no `workshop`-specific detail, and the source's B04 "lens"
closed with a mild exhortation ("that gap is the practitioner's to close").
Both are replaced with facts pulled directly from the file's own rules: the
explicit two coaching modes ("coach me" vs. "do it and teach me", chosen
once, remembered in `.workshop-progress.json`); the fixed five-part
explanation shape required after every step (what changed / why it works /
the platform concept / see it / try this); and the specific, genuinely
interesting constraint in rule 3 — even when a step fails, Claude is barred
from reading `solutions/` or the project's git history for the fix, and
must instead check the real documentation and the error message and fix
forward. That last rule became NB02, replacing the source's generic B02
pipeline diagram entirely (dropped outright — "Read SKILL.md → Execute →
Return output" carries zero `workshop`-specific facts and would be true of
any skill in the source's batch).

**B00 WRITER LAW:** wrong guess — a newcomer assumes a skill named after a
hands-on workshop must build the SEC agents automatically. Typed text:
"Does Claude's skill / do the SEC-agent / workshop for me?", trigger "do" →
replacement "coach", landing on "Does Claude's skill coach the SEC-agent
workshop for me?" Grounded directly in the SKILL.md's own self-description:
"You are the participant's coach for this workshop." Audio measured 9.64s
(clears the ≥9s TIMING LAW floor) + 0.8s lead silence = 9.67s rendered clip.
Frame-verified at t≈4s (mid-correction, "coach" mid-type) and t≈9s (full
corrected question settled, no leftover "do"): confirmed clean.

**Beat count: 7**, matching the source exactly (B00 + B01 + B02 + B03 + B04
+ BHTF + BOUT = 7). Kept the same shape as the `-weekly-report` sibling's
approach: B00 → BrutalistHesitantWriter (wrong-guess pedagogy folded into
WRITER LAW); B01 → NB01 (anatomy, unchanged in scope, two-mode fact added
from the real file); B02 (generic pipeline) dropped outright, freeing a
slot; B03 (design tell, Teardown verdict) → NB02 (the no-solutions-folder
rule, re-grounded, stripped of verdict, carrying BOTH-DIRECTIONS: step
works → Claude explains why; step breaks → Claude still can't shortcut to
the answer key); B04 (lens/Plato move) → NB03 (re-registered Plain, the
source's closing exhortation dropped); freed B02 slot → BCRY, the
mandatory carry-out beat the source (pre-dating the `simple`/`hai-simple`
spine) never had; BHTF rewritten as a fully self-contained prompt (the
source's version named "the workshop skill" by file, which only works with
that exact SKILL.md installed; this redo has the viewer ask Claude to write
and use its own small five-part coaching file live, runnable in any Claude
conversation today); BOUT re-skinned to the Humanitarians AI outro
(`OutroSeries`). Full audit in SCRIPT.md.

One-flag: zero flags. Every claim restates the `workshop` SKILL.md's own
text directly (see SCRIPT.md One-flag audit for the full list). Anchor:
N/A as a separate planted/paid-off case — the `workshop` skill's own
coaching cycle is the single worked example throughout, named at B00 and
carried through NB01–NB03 without dropping it (same disposition as the
`-weekly-report` sibling).

**Built this invocation, start to finish:**

1. `generate_audio_kokoro.py` — 7/7 beats, am_onyx, $0.00. B00 measured
   9.64s (clears the ≥9s floor).
2. `render_scenes.py` (manim -qh) — NB01/NB02/NB03 chip-row GRAPHIC beats,
   reusing the calibrated generic chip-row renderer copied verbatim from
   the `-weekly-report` sibling (humanitarians palette #F3EBDD/#2F2A26/#E4572E,
   one terracotta accent per beat).
3. `remotion_scenes.py` — B00 (BrutalistHesitantWriter), BCRY (WantQuote),
   BHTF (ClaudeComposerAsk), BOUT (OutroSeries). Exceeded the tool's 120s
   foreground window and was moved to a background task by the harness;
   blocked on it directly via `TaskOutput` rather than ending the turn, per
   the one-shot-invocation COMPLETION LAW. Exit 0, all 4 beats ok.
4. `compile.py` — first pass: content-check/frame-check/lane-check PASS,
   GATE AUDIO PASS (-24.0 dB), master forced to native 3840×2160 (THE 4K
   LAW), 101.9s, 7/7 real (no slate declared).
5. `type_check.py` (GATE T) — **first pass FAILED**: NB02's chip label
   "docs, not solutions/" fell under the §8.1 min-size floor (17px < 20px)
   after auto-scaling to fit the chip width. Fixed the root cause — the
   label itself, not the renderer — by shortening NB02's three chips to
   "step breaks" / "check the docs" / "explain anyway" in both `scenes.py`
   and `beat_sheet.json`'s `graphic` block, re-rendered only NB02, and
   recompiled (`--force`). Second pass: **GATE T PASS**, 0 FAILs.

**Gate V (visual):** pulled frames at 0.5s intervals (`ffmpeg -vf fps=2`,
204 frames) across the full 101.9s runtime and read a spread of 7 directly
(mid-beat for every beat) plus 2 targeted pulls inside B00 at t≈4s/9s.
B00's naive framing and its "do"→"coach" correction read cleanly, full
corrected question settled before cutoff, `@HumanitariansAI` folder label
visible. NB01 ("A SKILL IS A FOLDER" — 7 acts / 2 modes / 1 file, caption
"One file. Two modes. Same coach."), NB02 ("NO PEEKING AT THE ANSWER KEY" —
step breaks / check the docs / explain anyway, caption "Stuck or not:
reason it, don't copy it."), and NB03 ("THE SCRIPT, AND THE LEARNING" —
SKILL.md / Claude's explanation / participant's grasp, the third chip
correctly struck to show the file's reach ends at the middle step) all
legible, one terracotta accent each, safe inset respected, no
overlap. BCRY's quote card carries the exact carry-out sentence with
sparkline "Fixes the script. Not the grasp." BHTF's composer card shows the
correct topic line ("WORKSHOP · ANTHROPIC SKILL"), segment title, the full
self-contained Your Turn prompt, and the correct `@HumanitariansAI` folder
label. BOUT's outro card reads "WORKSHOP · @HumanitariansAI" / "The Script,
Not The Understanding." with no Claude mascot. **No defects found** after
the NB02 label fix — nothing else required a re-render.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (cut=master, no violations)
- GATE T (type_check.py): PASS, 0 FAILs (after the NB02 chip-label fix)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160, audio present; duration 101.916667s; mp4 mtime
  newer than beat_sheet.json mtime

Metadata file written: `cwc-workshops--claude-liam-workshop.md` (channel
@HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: this reel's family
`cwc-workshops` matches no prefix in the map, so resolution fell through to
the `hai-simple` skill-key entry, which maps to "Claude Basics" — same
disposition as every other `cwc-workshops--*` sibling in this loop — plus
the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K package + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp cwc-workshops--claude-liam-workshop.mp4 \
   cwc-workshops--claude-liam-workshop-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
