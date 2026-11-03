# BUILD-LOG — behind-the-model--claude-liam-vox-team-fence-gap

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-written Teardown sheet
(`anthropics/youtube/behind-the-model/claude-liam-vox-team-fence-gap/beat_sheet.json`,
"Why Individual Caution Does Not Add Up to Team Safety," brand `claude-liam`,
`@NikBearBrown`, cold open `ClaudeComposerAsk`, GRAPHIC/CARD body beats
B01–B08 fully narrated with Manim scenes in `scenes_std.py`, `YOURTURN`,
`OUTRO`, plus three unused empty-narration BOOKEND placeholders — BVDT/BHTF/
BOUT — confirmed dead scaffold via empty `narration_text` and not carried
forward). Built entirely fresh this invocation (only SUBJECT.json present on
pickup).

Kept the question and every fact: five (source's own body alternates
"four"/"five" — standardized on five throughout this redo) teammates each use
Claude carefully and individually, with no shared rules across the team; one
adds an MCP connector to read the shared team Dropbox; it's added at the
*account* level, not scoped to that one person; every teammate's agent then
inherits read access to the whole shared folder, including a confidential
client contract; no one intended it and no one knew; the accountability gap
sits at the boundary between people, not inside anyone's individually careful
practice; the fix is naming the fence (data scope, connector approval,
accountability) before anyone connects anything. Compressed the source's
B01/B05 (setup + concrete case) into B01's anchor-planting beat, B03/B04 (the
rule + verdict) into B03/B04's break+mechanism beats, B06/B07 (fix + checklist)
into B06's anchor-payoff beat, and added a wrong-guess beat (B02: careful
individuals should sum to a careful team — falsified by the anchor's own
case) and a both-directions beat (B05: not every shared thing needs a rule —
a private, unshared read isn't a team-level risk) per this factory's PHASE 1
six-move spine, since the source's Teardown shape carried neither explicitly.

**Anchor B01→B06:** four teammates each inside their own fence, one unfenced
shared Dropbox folder in the center holding a confidential contract file.
Planted with no fence around the center; returns at B06 with a new fence
drawn around the shared center, labeled with the three rules (data scope,
connector approval, accountability).

B00 WRITER LAW: naive framing "does that make **us** safe?" corrected to
"does that make **the team** safe?" (personal-safety framing → team-safety
framing, the reel's actual distinction). Single-word trigger ("us") per the
constitution/IVP/MPC redo lesson on multi-word triggers; replacement ("the
team") may contain a space since it is only typed, never token-matched.
35-word narration + `lead_silence_s: 0.8`, measured 11.26s (clears the ≥9s
TIMING LAW window with margin); frame-verified at t=10.5s that the full
corrected question ("...the team safe?") is legible well before the beat ends.

Build sequence:
1. `generate_audio_kokoro.py` — 10/10 beats, first pass, no retries (B00
   11.26s, B01 17.11s, B02 5.95s, B03 14.51s, B04 9.39s, B05 10.90s, B06
   17.24s, BCRY 9.51s, BHTF 18.05s, BOUT 5.14s).
2. `render_scenes.py` — 6 Manim GRAPHIC beats (B01–B06), clean first pass.
3. `remotion_scenes.py` — 4 REMOTION beats (B00/BCRY/BHTF/BOUT); auto-
   backgrounded past the tool's 120s foreground timeout, blocked on
   explicitly via `TaskOutput(block=true)` per the ONE-SHOT/COMPLETION LAW
   rather than ending the turn — exit 0, all 4 confirmed rendered (B00
   extended to 11.3s).
4. `compile.py --height 2160` (no `--review`) — THE 4K LAW forced the clean
   master natively to 3840×2160. content-check/frame-check/lane-check all
   PASS, GATE AUDIO PASS mean_volume -23.9 dB.

**GATE T caught 2 real FAILs on the first pass** (B01/B04: small caption/
label text — folder label, connector/confidential-contract captions — set at
13–15px in the original scenes.py, well under the 41px floor at this master
resolution) — fixed by bumping every sub-22 label `font_size` to 22+ and
every sub-30 title to 32. GATE T: PASS, 0 FAILs after one fix pass.

**Gate V's frame-pull sweep caught 4 further real defects that GATE T's
automated min-size/bbox-overlap checks did not** (a genuine gap between the
automated floor check and actual legibility/overlap, not a false positive):
the font-size bump above made the "SHARED\nDROPBOX" folder label too big for
its original fixed-size box, clipping against the border in every beat that
reused `_shared_folder()` (B01/B03/B04/B05/B06) — fixed by sizing the box
from the label's own measured width/height instead of a fixed constant;
B02/B03's "TEAM SAFE" caption sat flush against its checkmark box with no
visible gap — fixed by widening the `next_to` buff 0.18–0.2 → 0.35; B05's
"own file" caption touched the bottom edge of its dashed fence — fixed by
switching from a manual offset to `next_to(..., buff=0.35)`; B05's title "NOT
EVERYTHING NEEDS A FENCE" rendered with "NOT" and "EVERYTHING" visually fused
at this weight/size (a real kerning-adjacent legibility defect, confirmed by
frame pull, not a checker gap) — reworded to "A PRIVATE READ ISN'T A TEAM
RISK," which also reads more precisely against the beat's actual claim. All
four re-rendered (B01/B03/B04/B05/B06 via Manim), recompiled, re-verified
GATE T still PASS (0 FAILs) and re-pulled frames confirm every fix clean:
folder labels sit inside their boxes with margin, "TEAM SAFE" and "own file"
captions clear of their boxes/fences, B05's title reads correctly, B06's
anchor-payoff fence + three rule labels legible, BCRY/BHTF/BOUT correctly
skinned (Humanitarians AI palette, @HumanitariansAI folder label, Fable 5
composer, SUBSCRIBE + @HumanitariansAI outro — not the source's
@NikBearBrown/claude-liam skin).

**Gates:**
- content-check: PASS (10 beats, no violations)
- frame-check: PASS (3840×2160, 10 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, after 1 fix pass for min-size)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe independently reverified: 3840×2160, h264 + aac, duration
  120.06s; mp4 mtime (1788626097) newer than beat_sheet.json mtime
  (1788625185)

**Non-blocking warning (compile.py):** motion histogram graphic:6 remotion:4
— GRAPHIC at 60%, over the ~40% pantry-cap guideline in MOTION.md.
Structural for this shape: hai-simple's mandated B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) are REMOTION by skill contract, against 6 GRAPHIC
body beats for this 10-beat reel (B01–B06) — same disposition as every other
`behind-the-model--*` sibling at this beat count.

Metadata file written: `behind-the-model--claude-liam-vox-team-fence-gap.md`
(channel @HumanitariansAI, Playlist: **Behind the Model** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`behind-the-model` matches the map's `behind-the-model` prefix directly —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-05 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
