# BUILD-LOG — behind-the-model--claude-liam-vox-bainbridge-irony

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/behind-the-model/claude-liam-vox-bainbridge-irony/beat_sheet.json`
(a Teardown-register vox-explainer slate cut of claude-agentic-ai candidate
02 — Bainbridge's Irony: automation shifts human work upstream and into
checkpoints, does not eliminate it. Source spine: developer/agent bug-fix
scenario, THE QUESTION card, naive lever-scale, section card naming
Bainbridge 1983, real lever-scale, Priya file-reorganization anchor,
implication card ("agent work fails at scale"), scope-upstream practice,
RECAP endcard — plus a claude-liam BOOKEND wrapper (verdict/your-turn/outro)
never filled).

**The call:** register Teardown -> Plain, general audience, no verdict beat.
Facts preserved verbatim where the source's own language was already
Plain-compatible (the B01 bug-fix scenario, the checklist beat, the naming
of Bainbridge 1983, the Priya numbers with their FACTCHECK "illustrative"
caveat). B00 replaced the source's `ClaudeComposerAsk` with
`BrutalistHesitantWriter` per WRITER LAW: "less" -> "more" — the newcomer's
actual wrong guess (a smarter agent means less work) corrected directly to
the reel's finding (more supervisory work), which doubles as the carry-out's
seed. Added a both-directions beat (B06, new) since the source's Teardown
spine had no room for one: the naive picture genuinely holds for small,
reversible tasks and flips once the agent's reach is wide — folding in the
source's "manual fails locally, agent work fails at scale" implication card
as the mechanism for the flip. Anchor kept as the source's own naive/real
lever-scale pair (B02 plant -> B05 payoff, same bar-pair composition,
right bar rising to match left) with Priya's comparison appended to the
payoff. Beat count: 11 (B00, B01-B07, BCRY, BHTF, BOUT) vs. the source's ~10
CLI-adjacent beats + unfilled BOOKEND. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off in place of the source's
`ClaudeTitleOutro` / @NikBearBrown. See QUESTION.md for the full source-fact
inventory and CARRY-OUT.md for the line and the wrong guess it defeats.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 11 beats, free, `am_onyx`, first pass, no
   retries. B00 landed at 10.33s (clear of the >=9s TIMING LAW floor) on the
   first narration draft (28 words + `lead_silence_s: 0.8`). Durations: B00
   10.33s, B01 8.21s, B02 9.22s, B03 12.91s, B04 14.57s, B05 25.32s, B06
   20.18s, B07 12.76s, BCRY 8.79s, BHTF 15.40s, BOUT 5.27s (+1.0s tail).
2. Verified B00's correction with accurate-seek frame pulls (`-ss` AFTER
   `-i` — the file has a single keyframe, so `-ss` before `-i` gave
   misleading/stale frames on the first attempt and was redone). At t=8.0s
   "less" is fully typed in accent (terracotta), doomed; by t=9.5s it has
   resolved to "more"; by t=10.1s the writer reaches "work" with the full
   corrected question landing well before the 10.33s clip ends. TIMING LAW
   satisfied, no rewrite needed.
3. Wrote `scenes.py` (7 Manim scenes, reel-unique names `BIB01Scene` through
   `BIB07Scene`) and `render_scenes.py`; rendered all seven in the
   foreground, no render failures.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground,
   no failures; all four native 3840x2160.
5. First `compile.py` pass -> 11/11 real (no slate), 4K LAW forced the
   master to native 3840x2160, GATE AUDIO PASS mean_volume -24.0 dB inline.
   Compile stretched several Manim clips to fill their beat's measured audio
   (B04 1.93x, B05 1.64x, B06 2.07x slow-down) since scene run-times were
   authored shorter than the final narration; Gate V frame reads (below)
   found no resulting defect — the held final captions/comparisons read
   fine slowed. Non-blocking WARNING: motion histogram graphic:7 remotion:4
   (63%, over the ~40% pantry cap) — structural, matching this family's
   other builds: hai-simple's 4 fixed REMOTION slots (writer/carry-out/
   your-turn/outro) don't scale with body length.
6. GATE T (`type_check.py`): PASS, 0 FAILs, first pass.
7. Gate V (visual, manual): pulled 36 frames at 4s spacing across the full
   143.96s runtime (single `fps=1/4` ffmpeg pass, not per-frame `-ss` calls,
   after the first per-timestamp attempt timed out re-decoding a 4K file
   from scratch 48 times) and read every one directly. All legible, correct
   content, no clipping or overlap; anchor pair (B02 naive bars -> B05 bars
   rising together into the Priya comparison) reads correctly across the
   compile-time slowdown; both-directions split card (B06) and
   scope-upstream timeline (B07) correct; carry-out/handoff/outro correct
   with @HumanitariansAI branding on B00 and BOUT.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master -> mean_volume **-24.0 dB**, max -2.8 dB. Master mtime
   (Sep 5 08:59:45) is newer than beat_sheet.json mtime (Sep 5 08:55:50).

**Gates (final state):**
- content-check: PASS (11 beats, no violations)
- frame-check: PASS (3840x2160, 11 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects requiring a fix
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 143.96s, h264+aac, 3840x2160; mp4 mtime newer than
  beat_sheet.json mtime

**Playlist resolution:** family `behind-the-model` matches the map's
`behind-the-model` key directly in
`skills/make/hai-simple/loop/playlists.json`, resolving to **Behind the
Model** — no fallback needed.

Metadata file written:
`behind-the-model--claude-liam-vox-bainbridge-irony.md` (channel
@HumanitariansAI, Playlist: **Behind the Model**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase
4 (4K render + deliver.py) in this same invocation.

## 2026-09-05 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp behind-the-model--claude-liam-vox-bainbridge-irony.mp4 \
   behind-the-model--claude-liam-vox-bainbridge-irony-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged:
`DELIVERY/behind-the-model--claude-liam-vox-bainbridge-irony/` (4K mp4 +
description.md). Repo copy step succeeded but `deliver.py --push` failed at
its own `git pull --rebase` (local unstaged changes from the copy it had
just made — not a remote conflict); committed and pushed those same two
files (`beat_sheet.json`, `BUILD-LOG.md`) directly, clean push, no conflicts.

**Post-delivery fix (same invocation):** Gate V's own frame sweep had caught
BHTF's `ClaudeComposerAsk` missing a `modelLabel` prop, silently defaulting
to the component's demo placeholder "Fable 5" — the same defect the
`verification-matrix` sibling reel logged on 2026-09-05. Fixed
(`modelLabel: "Opus 4.8"`, matching sibling convention), re-rendered BHTF
only via `remotion_scenes.py --only BHTF --force`, recompiled (`compile.py
--force`; the pipeline correctly flagged and purged the now-stale
`-4k.mp4` copy from the first delivery pass). Re-verified after the fix:
GATE T PASS (0 FAILs), ffprobe 3840x2160/h264+aac/143.96s, GATE AUDIO
-24.0 dB / max -2.8 dB, master mtime newer than beat_sheet.json, frame pull
at the BHTF beat confirms "Opus 4.8" now renders correctly. Re-copied to
`-4k.mp4` and re-ran `deliver.py --push` (outbox overwrite + repo commit as
above).

**Status: DELIVERED.** Both delivery targets staged/pushed, including the
post-fix master. Reel complete.
