# BUILD-LOG — k12-teacher-skills--preserve-cognitive-demand-differentiation

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/k12-teacher-skills/youtube/preserve-cognitive-demand-differentiation/beat_sheet.json`
("The Hard Case", `nikbearbrown` brand, 8 filled beats, source chapter
"Agent Skills for K-12 Teachers (Anthropic) — k12-lesson-differentiation").
Read the source sheet and its SCRIPT.md in full before writing anything.

**Facts preserved, unchanged:** the trap (making a task easier for a
struggling student removes the thinking the lesson builds); the worked
case (17 ÷ 5 across three tiers — Below: concrete array, 17 dots grouped
by 5, 2 circled; At: 3 R2, basket analogy; Above: proof that R < divisor
— all three keep the remainder); the general rule (differentiation varies
scaffold/representation/entry point, never intellectual demand); the
ceiling check (UDL test: does every tier arrive at the same destination?
If not, that's tracking); the cognitive-load-theory partition (extraneous
load — the scaffold absorbs it; germane load — the learner keeps it, and
stripping it out deletes the lesson, not simplifies it).

**The call:** kept the source's 8-beat count (B00/B01/B02/B02a/B02b/B03/
B04/B05 → this reel's B00/B01/B02/B03/B04/BCRY/BHTF/BOUT). B00 replaced
`ClaudeComposerAsk` with `BrutalistHesitantWriter` per WRITER LAW: "easier"
→ "different" — the actual wrong guess a newcomer makes, corrected to the
reel's real claim. Source's B03 `ClaudeVerdictArtifact` verdict compressed
into BCRY's single carry-out sentence per CARRY-OUT LAW (judgment removed,
fact kept: "Differentiation changes the door in — never the hard case
waiting behind it."). Source's B04 handoff kept as BHTF with the same
prompt, reworded to be read aloud. Close re-skinned to `OutroCTA` /
@HumanitariansAI. Anchor B01 → B04: the 17 ÷ 5 remainder card, planted as
the hard case surviving all three tiers, returns identically and drops
into the GERMANE LOAD pile as the payoff. No source beat was AI-VIDEO,
pantry, or a human-drop slot — source was entirely REMOTION
(`ClaudeComposerAsk` / `K12Fig01Division` / `ClaudeWindow` /
`K12Fig05DiffVsTrack` / `K12Fig06LoadPartition` / `ClaudeVerdictArtifact` /
`ClaudeTitleOutro`), but every one of those components is hardcoded to the
Claude token palette with a baked-in `@NikBearBrown` watermark and carries
no palette props (`./art scenes --check` confirmed all RENDERABLE, but
inspecting the `.tsx` source showed the hardcoding). Rather than reuse them
and ship the wrong channel watermark, B01–B04 were rebuilt as reel-own
Manim scenes (`PCDB01Scene`–`PCDB04Scene`) in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`), matching this factory's own
`claude-code`/`financial-services` sibling reels' pattern of GRAPHIC body
beats around REMOTION bookends.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`, first pass.
   Durations: B00 10.18s, B01 24.0s, B02 22.04s, B03 21.12s, B04 21.16s,
   BCRY 4.93s, BHTF 19.75s, BOUT 2.60s.
2. Wrote `scenes.py` (4 Manim scenes) and `render_scenes.py`; all 4
   rendered clean on the first pass (`manim -qh`, foreground).
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground,
   backgrounded past the shell's 120s inline timeout and blocked on with
   `TaskOutput` rather than ending the turn — no unsupervised render left
   running, per the ONE-SHOT/COMPLETION LAW). All 4 rendered clean.
4. First `compile.py` pass → 8/8 real (no slate), 3840×2160 native (THE 4K
   LAW), mean_volume -24.0 dB, slow-mo factors 2.59x–2.87x (all under the
   3.0x flag threshold).
5. GATE T (`type_check.py`) → **PASS, 0 FAILs, first pass** — all 8 beats
   §8.10 SKIP.
6. **Gate V caught a real defect on first frame pull**: pulled a frame at
   t=9.3s inside B00 and found the writer's correction never lands —
   "easier" sits highlighted in terracotta with the cursor frozen mid-pause
   at the clip's own end (10.18s = the narration length exactly, with no
   `lead_silence_s` actually applied — grepping the runtime confirmed
   `lead_silence_s` is read by `repair_b00_audio.py` and documented in the
   schema, but `generate_audio_kokoro.py` never references it, so the prop
   was a no-op for this build path). Root cause: the writer's own
   type→pause→backspace→retype timeline for "easier"→"different"
   (estimated ~10.4s at the default `charMs`/`hesitate*` settings, given
   two apostrophes and an em-dash each triggering an unconditional
   punctuation pause) ran longer than the 10.18s audio clock, so the video
   got frozen on its last frame mid-correction. Fixed by (a) rewriting the
   naive writer text to drop both apostrophes and the em-dash
   ("can't"→"cannot", "I'll"→"I will", "—"→".", cutting three unconditional
   punctuation pauses to one) and (b) lengthening B00's narration from 33
   to 36 words (still inside the WRITER LAW's 20–35 target, one word over)
   to buy audio margin. Re-generated B00 audio only (11.43s), re-rendered
   B00 only (`--only B00 --force`), recompiled. Reverified: correction
   ("their task different?") fully settled by t≈10.0s inside the new
   11.4s clip — confirmed on frame pulls at 8/9/9.5/10/10.5/11/11.3s.
7. Recompiled clean; re-ran GATE T (PASS, 0 FAILs) since the sheet changed
   after the first compile.
8. Gate V (full pass): pulled 18 frames across the full 128.0s runtime and
   read every one directly. B00's correction confirmed landed; B01's
   three-tier anchor (converging arrows into REMAINDER = 2) legible; B02's
   growing/closing gap bars read cleanly; B03's one-room-vs-three-ceilings
   columns (including the "even from a good scaffold: tracking" caption)
   legible; B04's anchor return (REMAINDER = 2 card dropping into GERMANE
   LOAD, "strip it out -> not simplified. deleted.") legible; BCRY's
   carry-out quote, BHTF's Your Turn composer card (full prompt legible,
   @HumanitariansAI folder label), and BOUT's title outro all read with no
   overlap, no clipping, safe inset respected. No further defects found.
9. Audio presence + provenance, independently reverified: `ffprobe` shows
   3840×2160, duration 128.038s; master mtime (1788358310) newer than
   beat_sheet.json mtime (1788358210); `ffmpeg -af volumedetect` mean_volume
   **-24.0 dB**, max -2.7 dB.

**Noted, not a new defect:** `OutroCTA` renders on flat white rather than
the humanitarians cream ground — same shared-component behavior already
logged unremarked in sibling `financial-services--*` reels in this
family's log.

**Gates (final state):**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass after the B00 audio/text fix
- Gate V: PASS, second pass — 1 real defect caught and fixed (B00 timing;
  see step 6), 0 defects on reverification
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.7 dB
- ffprobe: duration 128.038s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking observation (compile.py):** motion histogram remotion:4
graphic:4 (50%) — over the ~40% pantry cap. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 4 GRAPHIC body beats
for this 8-beat reel — same disposition as every other hai-simple reel in
this family's log.

**Playlist resolution:** family `k12-teacher-skills` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback, fell through to the skill name itself: `hai-simple`
is a literal key in the map, resolving to **Claude Basics** — same
resolution as the `financial-services--*` siblings in this log.

Metadata file written:
`k12-teacher-skills--preserve-cognitive-demand-differentiation.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840×2160 natively (THE 4K LAW in compile.py forces any
clean, non-`--review` master to 4K), so the Fellows-facing 4K file is the
same render, copied to the `-4k` filename `deliver.py` expects.

```
cp k12-teacher-skills--preserve-cognitive-demand-differentiation.mp4 \
   k12-teacher-skills--preserve-cognitive-demand-differentiation-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
