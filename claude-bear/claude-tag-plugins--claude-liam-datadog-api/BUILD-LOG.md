# BUILD-LOG — claude-tag-plugins--claude-liam-datadog-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-datadog-api/beat_sheet.json`
(Teardown register, 7 beats, all `filled`/`VIDEO`, dated 2026-07-18).

**Source-file check (logged, not asked — full detail in QUESTION.md):** the
`source_skill` field points at
`../anthropics/claude-tag-plugins/datadog/skills/datadog-api/SKILL.md`, which does
not exist on this machine (checked directly and via `find` across the whole
`claude-tag-plugins` tree). **Unlike the `claude-for-legal--*` sibling redos**
(`fto-triage`, `marketing-claims-review`, `material-contract-schedule`, …), this
is not a template-placeholder defect: the source sheet's narration is fully
written, specific, and non-generic at every beat (header names, error strings,
pagination-scheme-to-endpoint mapping, JSON:API envelope depth). This build
reuses the source sheet's own stated facts as the record rather than
reconstructing generically, per the redo contract ("keep its facts").

**What changed vs. source:**

- **Register:** Teardown → Plain. The source's B05 beat and its bespoke
  component `DatadogApiTell` are built around an explicit "what it gets right /
  where it bites" verdict frame (baked into the component's fixed title and
  column headers, not just the narration), and `BVDT` is a `ClaudeVerdictArtifact`
  card literally labelled "Verdict." Both are a design-quality judgment on the
  skill's documentation. Because the verdict framing is baked into
  `DatadogApiTell`'s JSX (not prop-driven), reusing it verbatim would have put a
  Teardown-register visual under Plain-register narration — so this build did
  **not** reuse `DatadogApiTell`/`ClaudeVerdictArtifact` and instead authored one
  new beat (**B03**) on the existing, fully prop-driven `MedhavyTwoColumnCard`
  (found via GATE L: `./art scenes "generic two column comparison list card"`),
  stating the identical underlying facts (only one bundled script, the one-line
  dashboard warning, the two unflagged JSON:API traps vs. the security note, the
  site-check, the named error string, the per-endpoint pagination assignment) as
  a **both-directions** split ("documented plainly" / "easy to miss") rather than
  a grade. `B01` (`DatadogApiAnatomy`) and `B02` (`DatadogApiDesign`) *were*
  reused verbatim — their narration and their components' fixed headline text
  were already descriptive, not evaluative, in the source.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW). Writer types "Claude already KNOWS how APIs like Datadog work,
  right?", hesitates on KNOWS, corrects to "has to be shown" → lands "Claude
  already has to be shown how APIs like Datadog work, right?" — the naive
  assumption (training already covers this) corrected to the real mechanism
  (a file Claude reads before acting). Picked up directly by B01's "two headers
  ride on every request" opening.
- **Beat count:** source's 7-beat shape (B00 → B01 anatomy → B02 design →
  B05 teardown → BVDT verdict → BHTF handoff → BOUT outro) compressed to 8:
  B00 (writer) → B01 (anatomy, reused) → B02 (design, reused) → B03 (both
  directions, new component, replaces B05+BVDT) → BCRY (carry-out, new) → BHTF
  (handoff, rewritten) → BOUT + BCTA (the fixed hai-simple `OutroSeries` +
  `OutroCTA` split) — same restructuring precedent as every `claude-for-legal--*`
  sibling in this family (7 → 8 via the outro split).
- **Facts/argument:** unchanged — v1/v2 split by resource, the two header names,
  the regional-site 403 trap and its `validate`-first fix, the `curl -g`
  requirement, the three pagination schemes, the spans/logs envelope asymmetry,
  the events double-`.attributes` path, and the dashboard-PUT-replaces-everything
  behavior all carry over from the source's own stated facts (see QUESTION.md).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — generalized from the source's
  Datadog-specific five-point watch-list to a prompt runnable on *any* API the
  viewer picks, testing the same read-vs-know distinction the reel opened with.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`DatadogApiAnatomy`, `DatadogApiDesign`, `DatadogApiTell`, `ClaudeVerdictArtifact`)
— no beat in either version was ever AI-VIDEO, pantry, or a human-drop slot. B03
is also REMOTION (`MedhavyTwoColumnCard`, pre-existing, prop-driven, found via GATE
L rather than authored new). `compile.py`'s motion-histogram WARNING (`remotion`
8/8 = 100%, over the ~40% pantry cap) is expected and accepted for the same reason
every prior all-REMOTION sibling has logged it: the NO-GENAI/NO-PANTRY LAW forces
every beat to GRAPHIC or REMOTION, and this reel's body is a documentation/API-
quirk explainer, not a worked-example narrative with room for illustrative Manim
figures.

## Gates

- **GATE T (type_check.py):** one flag, confirmed false positive: `§8.9
  [BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` — the
  middle-dot `·` triggers the same truncation heuristic already logged and
  shipped unfixed on the identical string in the `fto-triage` sibling. Frame QC
  (below) confirms the BOUT eyebrow renders fully legible, no actual truncation.
  0 pixel-beat FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 36 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.63s**, clears the ≥8s/≥9s TIMING LAW floor. A t=10.5s
  frame pull confirms the full corrected question on screen with the correction
  landed: "Claude already / has to be shown how APIs / like Datadog / work,
  right?"
- **Render note:** `remotion_scenes.py`'s first pass FAILed B03
  (`MedhavyTwoColumnCard`) with a Remotion package-version-mismatch warning
  banner obscuring the real error; auto-backgrounded past the tool's 120s
  foreground timeout — blocked on it explicitly via `TaskOutput` per the
  ONE-SHOT/COMPLETION LAW rather than ending the turn. Re-ran `--only B03
  --force` in isolation and it rendered clean on retry (transient first-render
  hiccup, not a content or prop defect) — all 8/8 beats confirmed rendered
  before compiling.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -2.9 dB — well above the
  -40 dB floor.
- **Gate V (frame QC):** pulled frames every 5s across the full 134.5s runtime,
  plus targeted full-resolution pulls of B01, B02, B03, BHTF, and BCTA, and the
  QC contact sheet for BOUT. All 8 beats legible, correctly kerned, no text
  overlap, safe inset respected. `BCTA`/`OutroCTA` renders on flat white rather
  than the humanitarians cream ground — same shared-component behavior already
  logged unremarked in `fto-triage` and its siblings. `@HumanitariansAI`
  folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (8/8 beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788199265) newer than beat_sheet.json
  mtime (1788199211); beat_sheet.json was never touched after the compile that
  produced this review cut, and will not be touched again — any further fix
  goes through a recompile.

## Output

`claude-tag-plugins--claude-liam-datadog-api-slate.mp4` (review-cut naming from
`compile.py --review`; no beat is actually a slate — 8/8 beats real VIDEO) —
134.5s, no slate content, native 3840×2160 (Remotion beats render at 4K
already), audible narration throughout (mean_volume -23.9 dB, ffmpeg-verified).
This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-tag-plugins"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key
fallback → "Claude Basics" — same resolution every other delivered
non-matching-family redo in this loop has used (`claude-for-legal--*` siblings).

Metadata file written: `claude-tag-plugins--claude-liam-datadog-api.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.

## 2026-08-31 — Phase 4 delivery

- **4K master:** `compile.py` without `--review` enforces its 4K LAW
  automatically — wrote `claude-tag-plugins--claude-liam-datadog-api.mp4`
  natively at 3840×2160 (Remotion beats were already rendered at native 4K),
  134.5s, 8/8 beats real, mean_volume -23.9 dB. Copied to `-4k.mp4` so
  `deliver.py`'s `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/claude-tag-plugins--claude-liam-datadog-api/` (4K master +
  description, syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop
  mount); repo
  `humanitarians-youtube/claude-bear/claude-tag-plugins--claude-liam-datadog-api/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `66c24b1c`, pushed clean
  (verified `git log` + `git status` against `origin/main`).

**Status: DELIVERED.**
