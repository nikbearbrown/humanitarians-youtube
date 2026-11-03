# BUILD-LOG — skills--claude-liam-mcp-builder

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-mcp-builder/beat_sheet.json` — a
fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at `anthropics/skills/skills/mcp-builder/SKILL.md` — that path no
longer exists on this machine; the skills tree has been reorganized since
the source's 2026-07-18 build. Nothing depended on it: the source
`beats[*].narration_text` already carried every fact verbatim, and
PEDAGOGY.md/SOURCES.md corroborated them). 7 source beats: B00 cold open
(`ClaudeComposerAsk`, REMOTION — not AI-video/pantry, so NO-GENAI/NO-PANTRY
LAW required no substitution beyond the WRITER LAW swap), B01 anatomy
(4 phases), B02 tool anatomy, B05 teardown ("gets right/bites"), BVDT
verdict, BHTF handoff, BOUT outro.

Facts carried over unchanged: four phases in fixed order — research
(protocol spec, language choice, tool list, all before code), implement
(project structure, API client, then each tool), review/test with the MCP
Inspector, evaluate (ten questions); TypeScript + Zod recommended stack,
streamable HTTP for remote / stdio for local; every tool needs an input
schema (Zod/Pydantic, typed + constrained + per-field descriptions), an
output schema, four annotations (`readOnlyHint`, `destructiveHint`,
`idempotentHint`, `openWorldHint`), and an actionable error message; naming
is prefix + action (`github_create_issue`, `github_list_repos`); research
depends on the target API's own live docs — unavailable/stale docs stall
the phase; the ten evaluation questions must be read-only, complex,
realistic, verifiable, in XML format, which rules out naturally complex
tasks built around a tool that writes state; TypeScript is recommended even
when a team's expertise is in Python.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "write" → "research and build" — the
newcomer's assumption that the skill starts by writing code, corrected to
the fact that it starts with research and planning). Register re-registered
Teardown → Plain: the source's B05 framed the live-docs dependency, the
read-only eval constraint, and the TypeScript recommendation as "what it
gets right" / "where it bites" — Teardown language — restated here as a
mechanism/asymmetry fact (B03) with no verdict on the skill's design.
Source's BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW (same disposition as this family's other skill-teardown
redos). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Anchor: B02 → B03, `github_create_issue` (a write tool) vs
`github_list_repos` (a read-only tool) — same prefix+action naming pattern,
built segment by segment, and only the read-only one fits the ten-question,
read-only evaluation proof directly. Both-directions in B03: a read-only
tool gets checked directly against the real answer; a tool that writes
state can't be verified the same way, even though it's a normal call an
agent makes. Compressed the source's project-structure/API-client
implementation detail and the MCP Inspector review step out of the 7-beat
Plain cut — logged in SCRIPT.md's "Deliberately not claimed" and QUESTION.md.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, $0.00. Durations:
   B00 10.86s, B01 19.95s, B02 26.37s, B03 28.74s, BCRY 12.89s, BHTF 24.02s,
   BOUT 2.97s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `MCBB01Scene` /
   `MCBB02Scene` / `MCBB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The command
   exceeded the harness's 120s default foreground timeout and was moved to
   background automatically — per the COMPLETION LAW's foreground-render
   rule, blocked on it with `TaskOutput(block=true)` rather than ending the
   turn; confirmed exit 0, all 4 beats `ok` before proceeding.
4. B00 verified directly: `media/B00.mp4` = 10.87s (clears the ≥8s TIMING
   LAW floor). Pulled a frame at t≈9.5s: the full corrected question "How do
   I research and build an MCP server for GitHub?" is settled and legible.
5. `compile.py` → first pass 7/7 real (no slate), 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — real defects found and fixed across two
iterations, plus one verified false positive added to the checker's
established exemption set:**

- B03: terracotta-on-cream contrast FAIL — "writes real state" and "outside
  the ten" labels measured 2.74–3.12:1 against cream, below the 4.5:1 WCAG
  floor (the same documented accent-on-cream constraint as the toolkit's
  `#D97757`/`#E4572E` terracotta family). Fixed by switching those labels to
  INK, keeping terracotta only on the structural card border/arrow (never
  on readable text) — same fix applied to B02's "WRITE" chip label
  pre-emptively.
- B01 (surfaced after the contrast fix, same coordinates persisting across
  recompiles): min-size FAIL, an 8px blob below the 20px floor. Traced with
  the checker's own blob-detection functions (not guessed) to the corner
  where two stacked TEAL card borders' anti-aliased curves nearly touched,
  producing a false ink fragment at the seam — not a caption. Fixed at the
  root by widening the sub-card vertical step (0.75 → 0.95 units) so the
  borders no longer nearly touch, removing the artifact instead of
  exempting it.
- B03: kerning FAIL, max inter-glyph gap 37px > threshold 11px (12.0×
  expected) on the MONO string `github_create_issue`. Verified by direct
  frame crop at the checker's own mid-clip sample point (t=dur×0.5 of the
  raw manim/B03.mp4): the string renders as one cleanly kerned, fully
  legible mono run — the same underscore-glyphs-sit-low-and-thin false
  positive class already documented for `MIVB03Scene`
  (`claude-code--claude-liam-mcp-integration`). Registered `MCBB03Scene` in
  `type_check.py`'s `KERNING_EXEMPT_PATTERNS` with the same verification
  convention.
- GATE T: **PASS (0 FAILs)** after the fixes and the one exemption addition
  (edit committed directly to `runtime/scripts/type_check.py`, the shared
  toolkit script — not a reel-local file).

**Gate V (visual) — three real defects found by the mandatory full-runtime
frame read, none caught by GATE T's single mid-clip sample:**

1. **B01** — the "docs: live" / "docs: offline/stale" labels and their
   arrows were positioned almost directly beneath the stacked
   protocol-spec/language/tool-list card column (not beside it as
   intended), producing heavy text-on-text overlap. Compounding it, the
   "tool list" card's label was inflated far larger than its siblings by an
   errant `.scale_to_fit_width(2.3)` call that force-*enlarged* a short
   string to fill the target width instead of only shrinking overlong
   ones. Fixed by giving all three sub-card labels one consistent
   `font_size` (scaling down only when too wide, never up), and replacing
   the two simultaneous side-by-side branches with sequential fades in the
   same slot directly below the card — confirmed clean by frame pulls
   before and after.
2. **B02** — all four tool-anatomy card labels rendered as vertical stacked
   letters instead of horizontal words. Root cause: `.arrange(DOWN,
   buff=0.1)` had been chained onto a plain multi-line `Text(...)` object,
   which already handles `\n` natively — `.arrange()` instead re-grouped
   the mobject's internal characters/lines into a column. Fixed by removing
   the `.arrange()` call and using `line_spacing` for the one genuinely
   multi-line label.
3. **B02** — the anchor build (`github_create_issue`) showed two
   overlapping copies of the string simultaneously. Root cause:
   `TransformFromCopy(create_segs, create_full)` animates a *copy* of the
   source into the target while leaving the original untouched and
   visible — and the per-segment build loop immediately before it had
   already assembled `create_segs` into the complete, correctly-positioned
   final string, making the subsequent transform both redundant and
   visually colliding with itself. Fixed by deleting `create_full` and the
   `TransformFromCopy` entirely, anchoring the WRITE chip to the
   already-complete `create_segs` group instead.

All three fixes were re-rendered, recompiled, re-verified by GATE T (still
PASS) and a fresh full-runtime frame pull (42 frames at 3s spacing across
126.8s) before calling Gate V clean: B00's title correction, B01's
research/implement/review/evaluate chain with the docs-live/docs-stale
branches now reading sequentially with no overlap, B02's four tool-anatomy
cards reading horizontally plus the clean `github_create_issue` /
`github_list_repos` anchor build, B03's anchor payoff (checked-against-real-
list vs. writes-real-state/outside-the-ten) and the TypeScript/Python
asymmetry note, BCRY's carry-out card, BHTF's Your Turn composer card, and
BOUT's outro/subscribe card all read legibly with safe inset respected and
no text overlap anywhere in the final master.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect,
  independently re-verified), max -3.0 dB
- ffprobe: duration 126.803s; mp4 mtime (1788546724) newer than
  beat_sheet.json mtime (1788545375)

**Non-blocking notes:** motion histogram remotion:4 graphic:3 — structural,
not a defect (hai-simple's mandated B00/BCRY/BHTF/BOUT-REMOTION shape
against 3 GRAPHIC body beats for a 7-beat reel, same as every other short
reel in this family). `OutroCTA` renders on flat white rather than the
humanitarians cream ground — same shared-component behavior already logged
unremarked in sibling reels in this family.

Metadata file written: `skills--claude-liam-mcp-builder.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's family `skills` has no literal prefix match in the map, so
content-matched to the Anthropic Agent Skill subject, the same override
already established by the `claude-api`/`frontend-design`/`brand-guidelines`
`skills--*` siblings built earlier this loop) — plus the direct code link
per the DELIVERY CONTRACT format.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-04 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp skills--claude-liam-mcp-builder.mp4 skills--claude-liam-mcp-builder-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/skills--claude-liam-mcp-builder/` (4K master +
description) and committed to `humanitarians-youtube/claude-bear/
skills--claude-liam-mcp-builder/` (README.md, beat_sheet.json, SCRIPT.md,
SUBJECT.json, CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
