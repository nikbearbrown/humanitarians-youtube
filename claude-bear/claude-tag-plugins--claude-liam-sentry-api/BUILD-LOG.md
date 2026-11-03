# BUILD-LOG — claude-tag-plugins--claude-liam-sentry-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-sentry-api/beat_sheet.json`
(Teardown register, 7 beats, all `filled`/`VIDEO`, dated 2026-07-25).

**Source-file check (logged, not asked — full detail in QUESTION.md):** the
`source_skill` field points at
`../anthropics/claude-tag-plugins/sentry/skills/sentry-api/SKILL.md`, which does
not exist on this machine (checked directly; no `sentry/` skill tree at all under
`claude-tag-plugins/`). **Same situation as the `datadog-api` sibling redo** in
this loop: not a template-placeholder defect — the source sheet's narration is
fully written, specific, and non-generic at every beat (data model, all eight
operations, four workflow patterns, five things it documents well, five gaps).
This build reuses the source sheet's own stated facts as the record rather than
reconstructing generically, per the redo contract ("keep its facts").

**What changed vs. source:**

- **Register:** Teardown → Plain. The source's `B05` beat and its bespoke
  component `SentryApiTell` are built around an explicit "what it gets right /
  where it bites" verdict frame (baked into the component's fixed title and
  column headers, GETS_RIGHT/WHERE_BITES arrays, not just the narration), and
  `BVDT` is a `ClaudeVerdictArtifact` card literally labelled "Verdict." Because
  the verdict framing is baked into `SentryApiTell`'s JSX, reusing it verbatim
  would have put a Teardown-register visual under Plain-register narration — so
  this build did **not** reuse `SentryApiTell`/`ClaudeVerdictArtifact` and instead
  authored one new beat (**B03**) on the existing, fully prop-driven
  `MedhavyTwoColumnCard` (found via GATE L, same component the `datadog-api`
  sibling used), stating the identical underlying facts (security note position,
  `sentry_issues.sh`'s script coverage, the shortId/numeric-ID recipe, frame
  order, rate-limit header meaning vs. the trailing-slash mention, detail-on-PUT
  ambiguity, tag-distribution guard, `stats_v2` encoding, shortId's search-only
  resolution) as a **both-directions** split ("documented plainly" / "easy to
  miss") rather than a grade. `B01` (`SentryApiAnatomy`) and `B02`
  (`SentryApiDesign`) *were* reused — their fixed-component visual content
  (data model, core operations, workflow, gotchas) was already descriptive, not
  evaluative — but the narration was compressed from the source's ~250-word,
  85-second single beat down to fit the hai-simple ≤150-word/beat guidance,
  tracking the same facts the components' baked bullet lists already display.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW). Writer types "That PROJ-123 in the URL IS the ID Claude sends
  to the API, right?", hesitates on IS, corrects to "isn't" → lands "That
  PROJ-123 in the URL isn't the ID Claude sends to the API, right?" — the
  newcomer's most natural wrong guess (the visible shortId is the ID) corrected
  to the real mechanism (a search is required to resolve it). Picked up
  directly by B01's data-model framing (shortId ≠ numeric ID).
- **Beat count:** source's 7-beat shape (B00 → B01 anatomy → B02 design →
  B05 teardown → BVDT verdict → BHTF handoff → BOUT outro) compressed to 8:
  B00 (writer) → B01 (anatomy, reused/compressed) → B02 (design,
  reused/compressed) → B03 (both directions, new component, replaces
  B05+BVDT) → BCRY (carry-out, new) → BHTF (handoff, rewritten) → BOUT + BCTA
  (the fixed hai-simple `OutroSeries` + `OutroCTA` split) — same
  restructuring precedent as the `datadog-api` and `claude-for-legal--*`
  siblings in this family (7 → 8 via the outro split).
- **Facts/argument:** unchanged — the org→project→issue→event hierarchy,
  frames[-1] as the crashing frame, the eight core operations, the four
  workflow patterns (resolve shortId first, Link-header cursors, check
  `detail` on PUT 200, `-L` for redirects), the security note on untrusted
  retrieved content, `X-Sentry-Rate-Limit-Reset` as epoch seconds, and the
  `stats_v2` `-G`/`data-urlencode` requirement all carry over from the
  source's own stated facts (see QUESTION.md).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — generalized from the source's
  Sentry-specific five-point watch-list to a prompt runnable on *any* API the
  viewer picks, testing the same shown-vs-sent distinction the reel opened
  with.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SentryApiAnatomy`, `SentryApiDesign`, `SentryApiTell`, `ClaudeVerdictArtifact`)
— no beat in either version was ever AI-VIDEO, pantry, or a human-drop slot. B03
is also REMOTION (`MedhavyTwoColumnCard`, pre-existing, prop-driven, found via
GATE L rather than authored new). `compile.py`'s motion-histogram WARNING
(`remotion` 8/8 = 100%, over the ~40% pantry cap) is expected and accepted for
the same reason every prior all-REMOTION sibling has logged it: the
NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or REMOTION, and this
reel's body is a documentation/API-quirk explainer, not a worked-example
narrative with room for illustrative Manim figures.

## Gates

- **GATE T (type_check.py):** one flag, confirmed false positive: `§8.9
  [BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` —
  the middle-dot `·` triggers the same truncation heuristic already logged and
  shipped unfixed on the identical string in the `datadog-api` and
  `fto-triage` siblings. Frame QC (below) confirms the BOUT eyebrow renders
  fully legible, no actual truncation. 0 pixel-beat FAILs beyond this, 0 shape
  FAILs.
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.9s**, clears the ≥8s/≥9s TIMING LAW floor. A t=10.5s
  frame pull confirms the full corrected question on screen with the
  correction landed: "That PROJ-123 / in the URL isn't / the ID Claude sends /
  to."
- **Render:** `remotion_scenes.py` ran past the tool's 120s foreground
  timeout and auto-backgrounded; blocked on it explicitly via `TaskOutput`
  (block=true) per the ONE-SHOT/COMPLETION LAW rather than ending the turn.
  Completed clean, exit 0, all 8/8 beats rendered on the first pass — no
  retry needed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect,
  verified independently of `compile.py`'s own report), max -2.5 dB — well
  above the -40 dB floor.
- **Gate V (frame QC):** pulled frames every 8s across the full 164.0s
  runtime, plus targeted full-resolution pulls of B00 (t=10.5s, correction
  check), B01, B02, B03, BCRY, BHTF, BOUT, and BCTA. All 8 beats legible,
  correctly kerned, no text overlap, safe inset respected. `BOUT`/`OutroSeries`
  and `BCTA`/`OutroCTA` both render on flat white rather than the
  humanitarians cream ground — same shared-component behavior already logged
  unremarked in the `datadog-api` and `fto-triage` siblings. `@HumanitariansAI`
  folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (8/8 beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788226210) newer than beat_sheet.json
  mtime (1788226168); beat_sheet.json was never touched after the compile
  that produced this review cut, and will not be touched again — any further
  fix goes through a recompile.

## Output

`claude-tag-plugins--claude-liam-sentry-api-slate.mp4` (review-cut naming from
`compile.py --review`; no beat is actually a slate — 8/8 beats real VIDEO) —
164.0s, no slate content, native 3840×2160 (Remotion beats render at 4K
already), audible narration throughout (mean_volume -23.9 dB, ffmpeg-verified).
This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-tag-plugins"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key
fallback → "Claude Basics" — same resolution every other delivered
non-matching-family redo in this loop has used (`datadog-api`,
`claude-for-legal--*` siblings).

Metadata file written: `claude-tag-plugins--claude-liam-sentry-api.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.
