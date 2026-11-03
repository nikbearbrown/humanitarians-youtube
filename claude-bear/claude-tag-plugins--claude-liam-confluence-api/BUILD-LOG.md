# BUILD-LOG — claude-tag-plugins--claude-liam-confluence-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-confluence-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown skill-teardown reel, 7 beats:
B00 `ClaudeComposerAsk` typed ask; B01 `ConfluenceApiAnatomy` — two REST
generations, three bundled scripts, four body formats; B02
`ConfluenceApiDesign` — the prompt-injection security note, the pagination
URL relativity trap, six error codes; B05 `ConfluenceApiTell` — a "gets it
right / where it bites" teardown of the skill's own documentation; `BVDT`
`ClaudeVerdictArtifact` recap; `BHTF` your-turn; `BOUT` `ClaudeTitleOutro`).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup.

Question, facts, and full body argument carried over unchanged: Confluence
Cloud runs two REST API generations at once (v2 `/wiki/api/v2/` default —
pages, spaces, blog posts, comments, attachments, labels; v1
`/wiki/rest/api/` only for CQL search, attachment upload/download, and
label add); three bundled scripts (`cql_search.sh`, `read_page.sh`,
`write_page.sh`); the `/wiki` prefix is mandatory on every path (missing
it = 404, not an auth error); the pagination URL relativity trap (v2's
`_links.next` is site-root-relative, strip `/wiki` off the base before
prepending; v1's is `/wiki`-root-relative, prepend the base as-is; getting
it backwards silently truncates results); the security note the source
calls the most important thing in the skill (retrieved content is quoted
as inert evidence, never followed as instructions); and the smaller
documented gaps (`atlas_doc_format`'s double-parsed value field, the
default list size sitting well under the real max, extra
permission/header requirements for delete and upload).

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "one"/"API" → "two"/"APIs" — the
newcomer's actual wrong guess that Claude calls a single Confluence API,
corrected toward the real two-version routing model). Register
re-registered Teardown→Plain: the source's B05 "gets it right / where it
bites" list is a documentation-quality verdict — Teardown judgment on the
skill's own writing, not on Claude's behavior. Plain register keeps every
fact in that list (folded into NB03: `atlas_doc_format` double-parse,
silent list truncation) but drops the verdict framing entirely — this reel
never rates the skill's documentation, it only states what's true and what
a general viewer would find easy to miss. `BVDT`'s verdict facts were
merged into the single `BCRY` carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
`@HumanitariansAI` (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's "gets right/bites" list reframed
(not compressed away) into NB03's neutral "worth knowing" facts, dropping
only the verdict framing itself; BVDT folded into BCRY; BHTF kept, with the
source's Claude-Code-session/ENG-space-specific task replaced by one
paste-ready prompt any viewer can run without special space/label setup
(it exercises the same three behaviors: search, read, and quote-vs-obey);
BOUT kept.

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION
(`ClaudeComposerAsk`/`ConfluenceApiAnatomy`/`ConfluenceApiDesign`/
`ConfluenceApiTell`/`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's mandated cold-open swap. The
source's `ConfluenceApiTell` component was deliberately NOT reused for
NB03 even though it is REMOTION and technically available: its on-screen
text is hardcoded as "CONFLUENCE API · TEARDOWN" with "✓ WHAT IT GETS
RIGHT" / "✗ WHERE IT BITES" column headers — a verdict rubric baked into
the component itself, not just the narration. Reusing it would put
Teardown judgment on screen under Plain narration, which is exactly the
defect CARRY-OUT LAW's "no design judgment" check exists to catch. NB01–
NB03 instead reuse the generic "chip row" Manim template (title + up to
five labeled chips + optional accent/caption) copied verbatim, mechanism
and GATE T exemption notes included, from the
`claude-plugins-official--claude-liam-access` sibling — fully neutral,
parametrized entirely from plain title/chip/caption strings.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(exceeded the tool's 120s timeout and was moved to background by the
harness automatically — blocked on it via `TaskOutput` before proceeding,
per the COMPLETION LAW's foreground-render rule; all 4 beats came back
`ok`); NB01–NB03 rendered via `render_scenes.py` (manim, foreground).

First `type_check.py` pass was **FAIL, 3 defects** (NB01/NB02/NB03 all
min-size §8.1: smallest text runs 18px/8px/17px < the 20px floor). Root
cause: chip labels and captions too long for the shared `_chip()`
renderer's width/char-length buckets — NB01's 5-chip row (`cql_search.sh`,
`read_page.sh`, `write_page.sh` alongside the two version chips) squeezed
every chip under its `0.82×chip_w` scale cap, and NB02/NB03's long
single-line captions (59/53 chars) got `set_width`-clamped hard enough to
shrink glyph height below the floor. Fixed at the content level (not the
validator): NB01 cut to 3 short chips (`v2 = default`, `v1 = fallback`,
`3 scripts` — the three script names moved to narration only, where they
were already spoken in full); NB02/NB03 captions shortened to ≤40 chars
(`get it backwards, pages stop quietly`; `words are evidence, never
instructions`) and NB03's longest chip renamed `silent limits`. Synced
`beat_sheet.json`'s `graphic.production_viz` fields to match scenes.py
before re-rendering (COMPLETION LAW — no post-compile sheet edits; this
fix was applied and NB01–NB03 re-rendered before the first compile
attempt completed as a real pass). `type_check.py` went 3→**PASS, 0
FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-tag-plugins--claude-liam-confluence-api.mp4`, 7/7 beats
filled real (no slate), 146.4s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 3 defects + fix above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe (self-verified, not just trusted from compile.py's log): video
  3840×2160 h264, audio (aac) present, duration 146.4s; mp4 mtime
  (1788197241) newer than beat_sheet.json mtime (1788197092)
- Gate V (visual): pulled 18 frames every 8s across the full 146.4s
  runtime plus targeted checks of B00 (t≈4s "one"/mid-correction doomed
  terracotta, t≈9s fully settled "Claude just calls / two Confluence
  APIs. / How does that work?"), NB01 (three chips + caption legible, v1
  accented), NB02 (three chips legible, `/wiki required` accented), NB03
  (four chips legible, `not commands` accented), BCRY (carry-out sentence
  and sparkLine footer read clean), BHTF (correct topic/title/
  `@HumanitariansAI` handle, paste-ready prompt text legible, no
  clipping), and BOUT (`OutroSeries`: correct eyebrow "CONFLUENCE API ·
  @HumanitariansAI", correct title restate "Two APIs, Not One.", crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.6s (≥8s requirement met, ≥9s
  window from `lead_silence_s: 0.8` + 29-word narration); frame pulls at
  4fps confirm both corrections ("one"→"two", "API"→"APIs") fully typed
  and settled by t≈9.0s of the 9.6s clip — the full corrected question
  "Claude just calls / two Confluence APIs. / How does that work?" is
  legible with time to spare before the beat ends.

Metadata file written: `claude-tag-plugins--claude-liam-confluence-api.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-tag-plugins`) does NOT
match any map prefix by `str.startswith` (verified programmatically: no
map key is a prefix of `claude-tag-plugins`, and `claude-tag-plugins` is
not a prefix of any map key), so resolution fell through to the
`hai-simple` skill-key entry, which resolves to "Claude Basics" — same
fallback used on the `claude-tag-plugins--claude-liam-config-guide`
sibling. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-tag-plugins--claude-liam-confluence-api-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-tag-plugins--claude-liam-confluence-api/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/claude-tag-plugins--claude-liam-confluence-api/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md, TYPECHECK.md — no mp3/mp4).

**Status: DELIVERED.**
