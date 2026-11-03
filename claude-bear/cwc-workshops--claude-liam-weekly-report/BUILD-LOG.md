# BUILD-LOG — cwc-workshops--claude-liam-weekly-report

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-weekly-report/beat_sheet.json`
— a Teardown-register skill-teardown of the Anthropic `weekly-report` Skill
(the weekly inventory report: four sections — stockouts, low stock, open
purchase orders, forecast risk — each backed by a named data file; the
skill's own hard rule that it must be built with one script over the whole
file, never a tool call per SKU). Source is 6 beats (B00 composer-ask cold
open + B01 anatomy + B02 generic pipeline diagram + B03 design tell + BHTF
your-turn + BOUT outro), already entirely REMOTION, so NO-GENAI/NO-PANTRY
LAW required no substitution beyond the mandatory B00 swap.

**Picked up mid-build, not started fresh.** On opening the reel dir,
QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (6 beats), all 6
mp3s + `mp3/timings.json`, `manim/NB01.mp4` + `manim/NB02.mp4`, and
`media/B00.mp4` / `media/BCRY.mp4` / `media/BOUT.mp4` already existed from
an earlier invocation today. Verified rather than trusted: read
SCRIPT.md's six-move audit and beat-count note (confirms the redo keeps
the source's exact 6-beat shape — B02's generic pipeline diagram dropped
outright since it carries no weekly-report-specific fact, its freed slot
becoming the mandatory BCRY carry-out this chassis requires and the source
never had), and cross-checked `beat_sheet.json` narration/timing fields
against the rendered mp3 durations in `timings.json` — consistent. Only
`media/BHTF.mp4` was missing (the `ClaudeComposerAsk` Your Turn beat).

B00 (`BrutalistHesitantWriter`) carries the WRITER LAW correction
"per-SKU" → "once": the naive assumption that building this report means
one tool call per SKU, corrected to the skill's actual rule of one tool
call total. 33-word narration + 0.8s lead silence measured 9.88s audio
(clears the ≥9s TIMING LAW floor); frame-verified at t≈4s (naive text
mid-type) and t≈7–9s (correction complete, full final question "Does
Claude call a tool once for the report?" settled on screen, no leftover
"per-SKU").

Built this invocation:

1. Rendered the one missing beat: `remotion_scenes.py <REEL_DIR> --only
   BHTF`. The call exceeded the tool's 120s foreground window and was
   moved to a background task by the harness; blocked on it directly via
   `TaskOutput` rather than ending the turn, per the one-shot-invocation
   COMPLETION LAW. Exit 0 — `BHTF: ok: ClaudeComposerAsk -> media/BHTF.mp4
   (extended to 21.6s)`.
2. Compiled (`compile.py`, review cut then master, no `--force` needed —
   first compile of this master): `cwc-workshops--claude-liam-weekly-report.mp4`,
   6/6 real (no slate declared), 103.4s, native 3840×2160 (THE 4K LAW
   forced the clean non-review master to 4K automatically — no separate
   4K re-render needed).
3. Gates at compile time: content-check PASS (6 beats, no violations),
   frame-check PASS (3840×2160, 6 beats, no violations), lane-check PASS
   (cut=master, no violations), GATE AUDIO PASS mean_volume **-23.9 dB**
   max -2.8 dB.

**Gate V (visual):** pulled frames at 0.5s intervals (`ffmpeg -vf fps=2`,
207 frames) across the full 103.4s runtime and read a spread of ~14
directly, including targeted pulls at both sides of every beat boundary.
B00's naive framing and its "per-SKU"→"once" correction read cleanly, the
writer settling on the complete corrected question. NB01 ("A SKILL IS A
FOLDER" — 4 sections / SKILL.md / 4 data files, caption "SKILL.md names
the files and the sections") and NB02 ("ONE SCRIPT, NOT ONE CALL EACH" —
67k rows / one script / zero per-SKU calls, caption "daily drops sections;
weekly adds the aging check") both legible, one terracotta accent each,
safe inset respected. BCRY's quote card carries the exact carry-out
sentence with sparkline "One script. Not one call each." BHTF's composer
card shows the correct topic line ("WEEKLY-REPORT · ANTHROPIC SKILL"),
segment title, the full self-contained Your Turn prompt, and the correct
`@HumanitariansAI` folder label (no stray handle defect). BOUT's outro
card reads "WEEKLY-REPORT · @HumanitariansAI" / "One Script, Not One Call
Each." with no Claude mascot. **No defects found** — nothing required a
re-render.

**Gates:**
- content-check: PASS (6 beats, no violations)
- frame-check: PASS (3840x2160, 6 beats, no violations)
- lane-check: PASS (cut=master, no violations)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 103.416667s;
  mp4 mtime (1788245489) newer than beat_sheet.json mtime (1788245376)

Metadata file written: `cwc-workshops--claude-liam-weekly-report.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: this reel's family
`cwc-workshops` matches no prefix in the map, so resolution fell through
to the `hai-simple` skill-key entry, which maps to "Claude Basics" — same
disposition as every other `cwc-workshops--*` sibling in this loop — plus
the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K package + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp cwc-workshops--claude-liam-weekly-report.mp4 \
   cwc-workshops--claude-liam-weekly-report-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/cwc-workshops--claude-liam-weekly-report/` (4K master +
description) and committed + pushed the text artifacts (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/cwc-workshops--claude-liam-weekly-report/` in the
humanitarians-youtube clone: commit `94c327ce`, pushed clean (`git status
--short` empty after).

**Status: DELIVERED.**
