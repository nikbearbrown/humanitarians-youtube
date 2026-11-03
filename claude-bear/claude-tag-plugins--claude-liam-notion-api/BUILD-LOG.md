# BUILD-LOG — claude-tag-plugins--claude-liam-notion-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-notion-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-shaped skill-teardown reel, 7 beats:
B00 `ClaudeComposerAsk` typed ask; B01 `NotionApiAnatomy` — content model
(page=block, DB→data source→schema) + two bundled scripts; B02
`NotionApiDesign` — sanity-check endpoint, data-source-ID extraction,
schema-before-filter, sharing-before-404; B05 `NotionApiTell` — a "gets it
right / where it bites" teardown of the skill's own documentation; `BVDT`
`ClaudeVerdictArtifact` recap; `BHTF` your-turn; `BOUT` `ClaudeTitleOutro`).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup.

Question, facts, and full body argument carried over unchanged: a page is
a block sharing one ID space; a database is a container whose real table
(schema + rows) lives in a separate data source object; a row is a page
whose parent is that data source; schema reads, queries, and row creation
all take the data source ID (from the database object's `data_sources`
list), not the database ID — sending the database ID returns "object not
found"; two bundled scripts (`notion_search.sh`, `notion_read_page.sh`,
the latter not recursing into `child_page`/`child_database` blocks);
`Notion-Version` required on every request (`400 missing_version`
otherwise); a 404 almost always means a sharing problem, not a bad ID —
check Connections first; and the smaller documented gaps (file URLs in
block payloads expire ~1h, a pagination loop must guard against an error
envelope, filter conditions are keyed by property type so a schema read
before filtering is mandatory).

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "database" → "data source" — the
newcomer's actual wrong guess that the database's own ID is enough to
query it, corrected toward the real data-source-ID routing). Register
re-registered Teardown-shaped→Plain: the source's B05 "gets it right /
where it bites" list is a documentation-quality verdict — Teardown
judgment on the skill's own writing, not on Claude's behavior. Plain
register keeps every fact in that list (folded into NB03) but drops the
verdict framing entirely. `BVDT`'s verdict facts were merged into the
single `BCRY` carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. Close re-skinned to `@HumanitariansAI`
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each (B02's sanity-check-endpoint point folded
into NB02's version-header point; the schema-before-filter point moved to
NB03 alongside the source's other documented gaps, to avoid repeating
"data source ID" content across three beats); B05's "gets right/bites"
list reframed (not compressed away) into NB03's neutral "worth knowing"
facts, dropping only the verdict framing; BVDT folded into BCRY; BHTF
kept, with the source's five-point Claude-Code-session watch-list
replaced by one paste-ready prompt any viewer can run without special
workspace setup; BOUT kept.

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk`
for B00/BHTF, `NotionApiAnatomy`/`NotionApiDesign`/`NotionApiTell` for the
body, `ClaudeVerdictArtifact` for BVDT, `ClaudeTitleOutro` for BOUT), so
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap. None of the source's custom body components were reused
for NB01–NB03 even though they are REMOTION: `NotionApiTell`'s on-screen
text bakes in a "✓/✗ gets right / bites" rubric, the same defect class the
`confluence-api` sibling documented. NB01–NB03 instead reuse the generic
"chip row" Manim template (copied verbatim, mechanism and GATE T exemption
notes included, from the `claude-tag-plugins--claude-liam-confluence-api`
sibling), parametrized entirely from neutral title/chip/caption strings.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (exceeded
the tool's 120s foreground timeout and was moved to background by the
harness automatically — blocked on it via `TaskOutput` before proceeding,
per the COMPLETION LAW's foreground-render rule; all 4 beats came back
`ok`, B00 extended to 11.8s); NB01–NB03 rendered via `render_scenes.py`
(manim, foreground).

**Two real legibility defects found and fixed by frame-reading, neither
caught by GATE T's pixel-level checks:**

1. Word-space collapse in the shared `_chip()` Manim renderer: any chip
   label built from two or more plain-space-separated words rendered with
   the space at effectively zero width — "DB owns source" read as
   "DBownssource" on screen, "2 scripts" read as "2scripts". This affected
   both bold (accented) and non-bold chips, so it is not a bold-only
   artifact. GATE T's §8.1 min-size check does not evaluate word-spacing
   legibility, only pixel-run height, so it passed both times regardless.
   Root-caused by reading rendered frames directly (Gate V), not by any
   automated gate. Fixed at the content level, matching the established
   remedy from the `claude-for-legal--claude-liam-investigation-query`-
   class fix documented on siblings: switched every plain multi-word chip
   label in NB01/NB02/NB03 to a single hyphenated token
   (`DB-owns-source`, `2-scripts`, `version-header`, `not-bad-ID`,
   `no-recursion`, `links-expire`, `guard-loop`, `filter-by-type`).
   Labels built around a distinct symbol glyph (`page = block`) were left
   as-is — confirmed by direct pixel crop that the `=` glyph itself
   preserves visual word separation even when the surrounding whitespace
   collapses.
2. A second, distinct defect surfaced only after the hyphenation fix: the
   bold accented chip `404 = sharing` rendered with what reads as a
   spurious strike-through crossing the digits ("404"), a glyph-crossing
   artifact specific to bold-weight EB Garamond digits kerned tightly
   against an adjacent `=` glyph. Confirmed by cropping and zooming the
   frame. Fixed by dropping the digits from that chip entirely (renamed
   to `check-sharing`, keeping the same bold/accented/underlined
   treatment) rather than trying to re-kern digits GATE T has no check
   for — the "404" fact is already carried in the beat's spoken narration
   and its NB02 caption context.

`type_check.py` (GATE T) ran clean (0 FAILs) on the *first* pass over
content that had NOT yet been frame-read — the min-size §8.1 FAIL that
did surface (NB01, a too-long caption at 37 chars) was fixed by shortening
the caption, which is unrelated to the two space-collapse/glyph-crossing
defects above; those were caught only by pulling and reading actual
frames, not by GATE T. This is a genuine coverage gap in the type-spec's
automated checks worth flagging: legible pixel *height* is not the same
as legible *content*, and neither is checked by any current gate.
Synced `beat_sheet.json`'s `graphic.production_viz.chips` fields to
`scenes.py` before every re-render (COMPLETION LAW — no post-compile
sheet edits; all fixes were applied and re-rendered before the first
compile attempt completed as a real pass, then recompiled fresh after
each subsequent content fix). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-tag-plugins--claude-liam-notion-api.mp4`, 7/7 beats filled
real (no slate), 144.7s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the caption-length fix; the two
  word-spacing/glyph-crossing defects above were caught by Gate V, not
  GATE T, and fixed independently before the final GATE T pass)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe (self-verified, not just trusted from compile.py's log): video
  3840×2160 h264, audio (aac) present, duration 144.7s; mp4 mtime
  (1788220074) newer than beat_sheet.json mtime (1788219921)
- Gate V (visual): pulled 18 frames every 8s across the full 144.7s
  runtime, plus targeted crops of every GRAPHIC beat's chip row (this is
  where the two defects above were actually found) and B00 (t≈4s
  mid-correction terracotta "database" doomed, t≈8.5s corrected to "the
  data source ID", t≈11s full corrected question "How does that work?"
  settled with time to spare), BCRY (carry-out sentence and sparkLine
  footer read clean), BHTF (correct topic/title/`@HumanitariansAI` handle,
  paste-ready prompt text legible, no clipping), and BOUT (`OutroSeries`:
  correct eyebrow "NOTION API · @HUMANITARIANSAI", correct title restate
  "The Data Source, Not the Database.", crimson underline, no
  truncation). No blockers remaining after the two chip-content fixes.
- B00 TIMING LAW: `actual_duration_s` 11.75s (≥8s requirement met, ≥9s
  window from `lead_silence_s: 0.8` + 33-word narration); frame pulls
  confirm the correction ("database" → "data source") fully typed and
  settled well before the clip's end, with the full corrected question
  legible with time to spare.

Metadata file written: `claude-tag-plugins--claude-liam-notion-api.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-tag-plugins`) does not
match any map prefix by `str.startswith` (same as the `confluence-api`
sibling), so resolution fell through to the `hai-simple` skill-key entry,
which resolves to "Claude Basics". Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-tag-plugins--claude-liam-notion-api-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-tag-plugins--claude-liam-notion-api/` (4K master +
description) for the Drive sync. Committed and pushed to
`claude-bear/claude-tag-plugins--claude-liam-notion-api/` in
humanitarians-youtube (commit `64f3b8b8`: README.md = description,
beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md, QUESTION.md,
BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
