# BUILD-LOG — claude-plugins-official--claude-liam-build-mcpb

## 2026-08-30 — review cut, DONE

**Redo-mode build** (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-build-mcpb/beat_sheet.json`
— an 8-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about
the `build-mcpb` plugin-dev skill. Register re-registered Teardown -> Plain;
B00 is `BrutalistHesitantWriter` (WRITER LAW) in place of the source's
`ClaudeComposerAsk`; close carries the Humanitarians AI skin (`OutroCTA`).
The source's own narration (B00-B02) is fully self-contained and true —
manifest anatomy, the no-auto-prefix env var trap, the no-sandbox security
model, the build pipeline, and the test-without-toolchain rule all carry
over verbatim as plain mechanism facts (see QUESTION.md for the full
fidelity note). The source's Teardown VERDICT (B05/BVDT: "gets five things
right / here's where it bites," ranking the skill file's documentation
quality) was dropped entirely per the register rewrite — no design
judgment survives into Plain.

Built from scratch this invocation (no prior partial state found): wrote
`QUESTION.md`, `CARRY-OUT.md`, `SCRIPT.md`, `beat_sheet.json` (11 beats:
B00 writer, B01-B07 GRAPHIC body, BCRY carry-out, BHTF your-turn, BOUT
outro), `scenes.py` + `render_scenes.py` (the generic chip-row/chip-stack
Manim renderer, reused verbatim from the `claude-for-legal--claude-liam-
matter-intake` / `hiring-review` sibling redos, including their GATE-T
fixes baked in from the start: long-label font tier raised 17->21pt,
chip-width cap raised 3.4->5.0, MUTE-dim instead of literal strike-through,
upright serif captions, vertical stack for independent claim->conclusion
pairs).

**The anchor:** one illustrative environment variable, `ROOT_DIR`, carries
two of the source's real traps through a single running example — planted
at B03 (one setting, one job), extended at B05 (the no-auto-prefix
name-mismatch trap), and paid off at B06 (the anchor's exact 3-chip
composition returns, accented, with the no-sandbox/unvalidated-path trap
in the caption). B06 was deliberately kept to the SAME 3 chips as B03
(not a 4th chip appended) after estimating that a 4-chip row at this
reel's font-tier/width-cap combination risked reproducing the exact
GATE-T min-size failure the matter-intake sibling hit on its own 2-chip
B01 (long label + narrow chip_w -> set_width() clamp -> glyph shrinks
under the 20px floor) — moved the payoff into the caption instead.

**Pipeline, in order, all foreground (no backgrounded render steps
crossed a turn boundary):**

1. `generate_audio_kokoro.py` — 11/11 beats, am_onyx, $0.00. B00 measured
   10.86s.
2. `render_scenes.py` (Manim) — 7/7 GRAPHIC beats (B01-B07), 0 failures
   first pass.
3. `remotion_scenes.py` — 4/4 REMOTION beats (B00, BCRY, BHTF, BOUT), 0
   failures first pass. (This step and the next both exceeded the tool's
   2-minute default and were auto-backgrounded by the harness; blocked on
   each synchronously via a foreground `until`-loop against the task's own
   output file rather than ending the turn, per the one-shot invocation
   rule — there is no next turn to catch a background notification.)
4. `compile.py` — clean master first pass: 11/11 real (no slate),
   3840x2160 (4K LAW forces any non-`--review` master to 4K), 147.8s,
   GATE AUDIO PASS mean_volume -24.1 dB.
5. `type_check.py` (GATE T) — **PASS, 0 FAILs, first pass.** No fixes
   needed — the chip-renderer's pre-baked font-tier/width-cap fixes from
   the sibling redos held for this reel's content without further
   adjustment.
6. Gate V (manual frame reads, `ffmpeg -ss ... -frames:v 1`, read
   directly, not just checked numerically):
   - B00: pulled frames at t=3/4.5/5.0/5.5/6/8.5/10.5s. Confirmed the
     ACCENT LAW moment — "safe" typed in full, held in terracotta at
     t=4.5s, backspaced (t=5.0s mid-delete), replaced by "easy" in ink
     (t=5.5s) — and confirmed the beat lands the complete corrected
     question ("Does bundling it as an MCPB make it easy to run?") with
     the cursor after the closing "?" by t=8.5s, held to the end of the
     10.86s window (~2.4s margin, comfortably clear of the 9s TIMING LAW
     floor and the sibling's tighter ~1-2s margins).
   - B02, B06, B07, BHTF, BOUT, BCRY: spot-checked one frame each — all
     legible at native size, safe inset, no text-on-text overlap, correct
     humanitarians palette (one terracotta accent per beat), correct HAI
     outro skin (`OutroCTA`, @HumanitariansAI subscribe pill).
   - Gate V: **PASS**, no fixes required.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master directly (not just trusting compile.py's own report):
   mean_volume **-24.1 dB**, max -2.9 dB, both channels present (h264 +
   aac), 3840x2160, duration 147.760333s. Master mtime (1788141544) newer
   than `beat_sheet.json` mtime (1788141418).

**Non-blocking warning (compile.py):** motion histogram graphic:7
remotion:4 — graphic at 63%, over the ~40% pantry-cap guidance.
Structural: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) all REMOTION by skill contract, against 7
GRAPHIC body beats for this 11-beat reel (the source sheet's own beat
count, preserved per the redo-mode LOCKED SCRIPT contract) — same
disposition as the `claude-for-legal` family's longer hai-simple redos.

**Playlist resolution:** family `claude-plugins-official` matches the
`claude-plugins` prefix key in `skills/make/hai-simple/loop/playlists.json`
(prefix-match, `.startswith`) -> **Extending Claude — Skills, Plugins &
Connectors**. Confirmed against the map file directly, not assumed.

Metadata file written:
`claude-plugins-official--claude-liam-build-mcpb.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors**, plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate on the first pass
(no iteration needed on GATE T or Gate V). Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in `compile.py` forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-plugins-official--claude-liam-build-mcpb.mp4 \
   claude-plugins-official--claude-liam-build-mcpb-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/claude-plugins-official--claude-liam-build-mcpb/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/claude-plugins-official--claude-liam-build-mcpb/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `1bfcdab9`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
