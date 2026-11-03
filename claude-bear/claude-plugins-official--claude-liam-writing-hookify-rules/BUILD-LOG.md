# BUILD-LOG — claude-plugins-official--claude-liam-writing-hookify-rules

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-writing-hookify-rules/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at
`claude-plugins-official/plugins/hookify/skills/writing-rules/SKILL.md`).
7 beats: B00 cold open (`ClaudeComposerAsk`, REMOTION — not AI-video/pantry,
so NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW
swap), B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF
handoff, BOUT outro.

**Distinct from the sibling reel:** a separate hai-simple redo already
exists under the `claude-code` family (`claude-code--claude-liam-writing-rules`),
built from a much richer source covering the hookify rule's own internals
(frontmatter fields, event types, pattern precision). That source is not
this reel's source. THIS source's own facts are about the *skill mechanism*
itself, not the rule format — so this reel's question and body are about
skill discovery/matching, not rule authoring, to avoid duplicating the
sibling's content. See QUESTION.md for the full disambiguation note.

Facts carried over unchanged: a skill is a folder Claude reads before it
works; the instruction set is one file, SKILL.md ("the file is the
program" — source B01); the description near the top of that file states
exactly when to use it, and this skill's description is quoted verbatim in
the source's B03 "design tell" — fires for "create a hookify rule," "write a
hook rule," "configure hookify," "add a hookify rule," or guidance on
hookify rule syntax and patterns; once fired, Claude reads SKILL.md and
executes each step in order, linear, no branching unless a step says so
(source B02 pipeline); verdict: same input produces the same output every
run, but only within what the SKILL.md specifies (source BVDT).

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "name" -> "describe" — the naive
assumption that a skill is switched on by typing its exact name, corrected
to the fact that Claude matches your own wording against the file's
description). Register re-registered Teardown -> Plain: the source's B03
framed the description text as "the interesting constraint" and BVDT named
a "limit" — descriptive language about what the file specifies, kept as
fact, judgment dropped. Source's BVDT verdict recap folded into a dedicated
BCRY carry-out beat per CARRY-OUT LAW. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Added an anchor (B02 -> B03: the
skill's four real trigger phrases; a request that lands inside them fires
reliably every time, a request that doesn't simply leaves the skill off) and
a both-directions beat (B03) per this factory's PHASE 1 structure
requirement — the source didn't carry these as distinct beats.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   9.39s, B01 16.75s, B02 19.61s, B03 17.34s, BCRY 8.26s, BHTF 17.77s,
   BOUT 3.78s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CPOB01Scene` /
   `CPOB02Scene` / `CPOB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
4. B00 verified directly: `media/B00.mp4` = 9.4s (meets the >=8s TIMING LAW
   floor). Pulled frames at t=3.0s/8.5s: the correction ("name"->"describe")
   is complete and fully legible by t=8.5s.
5. `compile.py` -> `claude-plugins-official--claude-liam-writing-hookify-rules.mp4`,
   7/7 real (no slate), 3840x2160 (THE 4K LAW).
6. **Gate V, pass 1:** pulled frames every 6s across the full runtime and
   read them directly. Found one real defect: in B02's transition, a
   simultaneous `FadeOut` of the request bubble/arrow/chips alongside the
   "SKILL FIRES" chip's `.animate.move_to(...)` caused the chip to pass
   directly through and overlap the bubble text mid-move (caught at the
   fps=1/6 sample near t=36s). Fixed by splitting the single simultaneous
   `self.play(...)` into two sequential plays (fade out fully, then move) in
   `scenes.py`; re-rendered B02, recompiled. Re-checked the same timestamp:
   overlap gone, "SKILL FIRES" now animates in cleanly isolated.

**GATE T (type_check.py) — one finding, confirmed false positive, not a
real defect:**

- First pass (after the Gate V fix): FAIL (1 pixel beat). B02's contrast
  check (§8.3) flagged "terracotta accent #D97757 on cream 2.74:1 < 4.5:1
  WCAG." Investigated: all body text in B01–B03 already used INK
  (`✓ MATCH`, `✓`, `SKILL FIRES`, `FIRES` were explicitly set to INK, not
  TERRA, during scene authoring). Pulled the exact frame the checker samples
  (t=dur*0.5 of `manim/B02.mp4`) and read it directly: the only terracotta
  pixels are structural card-border strokes — the "add a hookify rule"
  chip's recolored highlight outline and the "SKILL FIRES" chip's border —
  both thin rounded-rectangle outlines that the blob detector's text-run
  filter mistakes for typography (the same documented false-positive class
  as ~40 other exemptions already in `STRUCTURAL_TERRACOTTA_PATTERNS`, e.g.
  `S04Scene`/`S09Scene`/`S14Scene` for simple-delve's decorative border
  rings). Registered `CPOB01Scene`, `CPOB02Scene`, `CPOB03Scene` in
  `STRUCTURAL_TERRACOTTA_PATTERNS` with the same documentation style as the
  existing entries (content fix per the false-positive's own established
  pattern, not a loosened check — every other check on these beats still
  runs and still gates).
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual), final pass:** pulled frames across the full runtime again
after both fixes and read them directly — B00's cold-open correction, B01's
folder->file->description sequence and the "help me write a rule for
hookify" match, B02's four-phrase anchor and step-list closer, B03's anchor
return (three reliable fires) and the no-match split, BCRY's carry-out card,
BHTF's Your Turn composer card, and BOUT's outro/subscribe card all read
legibly with safe inset respected and no text overlap. **Noted, not a defect
introduced here:** `OutroCTA` renders on flat white rather than the
humanitarians cream ground — same shared-component behavior already logged
unremarked in sibling reels in this family.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after registering the confirmed contrast
  false-positive exemption above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 93.9s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

Metadata file written: `claude-plugins-official--claude-liam-writing-hookify-rules.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `claude-plugins-official` matches the map's
`claude-plugins` prefix — plus the direct code link per the DELIVERY
CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
