# BUILD-LOG — claude-tag-plugins--claude-liam-grafana-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-grafana-api/beat_sheet.json`
(Teardown register, 7 beats, all `filled`/`VIDEO`, dated 2026-07-18).

**Source-file check (logged, not asked — full detail in QUESTION.md):** the
`source_skill` field points at
`../anthropics/claude-tag-plugins/grafana/skills/grafana-api/SKILL.md`, which
does not exist on this machine (checked directly and via `find` across the
whole `claude-tag-plugins` tree — same situation as the `datadog-api` sibling
redo). Not a missing-content problem: the source sheet's narration is fully
written, specific, and non-generic at every beat (time-format-by-endpoint
mapping, role model, alert-surface endpoints, error field paths, dashboard
version-conflict behavior). This build reuses the source sheet's own stated
facts as the record rather than reconstructing generically, per the redo
contract ("keep its facts").

**What changed vs. source:**

- **Register:** Teardown → Plain. The source's B05 beat and its bespoke
  component `GrafanaApiTell` are built around an explicit "what it gets right
  / where it bites" verdict frame — `GETS_RIGHT`/`BITES` are hardcoded
  constant arrays inside the component's JSX, not props — and `BVDT` is a
  `ClaudeVerdictArtifact` card literally labelled "Verdict." Both are a
  design-quality judgment on the skill's documentation, the identical defect
  shape already logged and worked around on the `datadog-api` sibling's
  `DatadogApiTell`/`BVDT` pair. Because the verdict framing is baked into
  `GrafanaApiTell`'s JSX (not prop-driven), reusing it verbatim would have put
  a Teardown-register visual under Plain-register narration — so this build
  did **not** reuse `GrafanaApiTell`/`ClaudeVerdictArtifact` and instead
  authored one new beat (**B03**) on the existing, fully prop-driven
  `MedhavyTwoColumnCard` (confirmed via GATE L: `./art scenes --check
  MedhavyTwoColumnCard` — already found and used by the `datadog-api`
  sibling), stating the identical underlying facts (time-format warning
  placement, the named error field, the session-only `grafana()` helper, the
  GNU/BSD `date` gap, the buried provisioning-lock header, the literal
  "grafana" path segment) as a **both-directions** split ("documented
  plainly" / "easy to miss") rather than a grade. `B01` (`GrafanaApiAnatomy`)
  and `B02` (`GrafanaApiDesign`) *were* reused verbatim — their fixed row
  content (time formats, role model, data-frame response, alert surfaces,
  design gotchas) was already descriptive, not evaluative, and narration was
  rewritten to match what's on screen without changing any fact.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW). Writer types "Claude already KNOWS how APIs like Grafana
  work, right?", hesitates on KNOWS, corrects to "has to be shown" → lands
  "Claude already has to be shown how APIs like Grafana work, right?" — the
  naive assumption (training already covers this) corrected to the real
  mechanism (a file Claude reads before acting). Picked up directly by B01's
  opening line.
- **Beat count:** source's 7-beat shape (B00 → B01 anatomy → B02 design →
  B05 teardown → BVDT verdict → BHTF handoff → BOUT outro) restructured to 8:
  B00 (writer) → B01 (anatomy, reused) → B02 (design, reused) → B03 (both
  directions, new component, replaces B05+BVDT) → BCRY (carry-out, new) →
  BHTF (handoff, rewritten) → BOUT + BCTA (the fixed hai-simple `OutroSeries`
  + `OutroCTA` split) — same restructuring precedent as the `datadog-api`
  sibling (7 → 8 via the outro split).
- **Facts/argument:** unchanged — three time formats by endpoint (ms for
  ds/query + annotations, seconds for state-history, RFC-3339 for silences,
  GNU vs. BSD `date`), the three-tier role model, the data-frame response
  shape and its in-band error field, the two alert-rule surfaces
  (Prometheus API live state vs. provisioning API definitions, UI-locked
  without the disable-provenance header), the GET-then-full-replace dashboard
  update with its 412 conflict, ds/query batching, and the annotations
  no-page-param constraint all carry over from the source's own stated facts
  (see QUESTION.md).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — generalized from the source's
  Grafana-specific five-point watch-list to a prompt runnable on *any* API the
  viewer picks, testing the same read-vs-know distinction the reel opened
  with (same generalization as the `datadog-api` sibling's BHTF).

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`GrafanaApiAnatomy`, `GrafanaApiDesign`, `GrafanaApiTell`,
`ClaudeVerdictArtifact`) — no beat in either version was ever AI-VIDEO,
pantry, or a human-drop slot. B03 is also REMOTION (`MedhavyTwoColumnCard`,
pre-existing, prop-driven, confirmed renderable via GATE L rather than
authored new). `compile.py`'s motion-histogram WARNING (`remotion` 8/8 =
100%, over the ~40% pantry cap) is expected and accepted for the same reason
every prior all-REMOTION sibling in this family has logged it: the
NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or REMOTION, and this
reel's body is a documentation/API-quirk explainer, not a worked-example
narrative with room for illustrative Manim figures.

## Gates

- **GATE T (type_check.py):** one flag, confirmed false positive: `§8.9
  [BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` —
  the middle-dot `·` triggers the same truncation heuristic already logged
  and shipped unfixed on the identical string in the `datadog-api` sibling.
  Frame QC (below) confirms the BOUT eyebrow renders fully legible, no actual
  truncation. 0 pixel-beat FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 36 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.78s**, clears the ≥8s/≥9s TIMING LAW floor. Frame
  pulls at 5s, 10.5s, and 11.5s confirm the writer's correction (KNOWS →
  "has to be shown") lands well before 5s and the fully-typed, corrected
  question — "Claude already has to be shown how APIs like Grafana work,
  right?" — is on screen and legible before the beat ends.
- **Render note:** `remotion_scenes.py` exceeded the tool's 120s foreground
  timeout and was auto-backgrounded; blocked on it explicitly via
  `TaskOutput` (block=true) per the ONE-SHOT/COMPLETION LAW rather than
  ending the turn — it completed clean, exit 0, all 8/8 beats rendered on the
  first pass.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect,
  verified independently of `compile.py`'s own report), max -2.9 dB — well
  above the -40 dB floor.
- **Gate V (frame QC):** pulled targeted frames for all 8 beats (B00 at 5s/
  10.5s/11.5s, B01 at 30s, B02 at 80s, B03 at 125s, BCRY at 138s, BHTF at
  150s, BOUT at 165s, BCTA at 167s) and read every one. All 8 beats legible,
  correctly kerned, no text overlap, safe inset respected. `BCTA`/`OutroCTA`
  renders on flat white rather than the humanitarians cream ground — same
  shared-component behavior already logged unremarked in the `datadog-api`
  sibling. `@HumanitariansAI` folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (8/8 beats, no violations, canvas 3840×2160 for the native Remotion
  renders; review master compiled at 1280×720 per `--review` default).
- **COMPLETION LAW:** master mp4 mtime (1788208581) newer than beat_sheet.json
  mtime (1788208537); beat_sheet.json will not be touched again — any further
  fix goes through a recompile.

## Output

`claude-tag-plugins--claude-liam-grafana-api-slate.mp4` (review-cut naming
from `compile.py --review`; no beat is actually a slate — 8/8 beats real
VIDEO) — 169.0s, no slate content, audible narration throughout (mean_volume
-24.0 dB, ffmpeg-verified independently). This is the review cut (COMPLETION
LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-tag-plugins"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple`
skill-key fallback → "Claude Basics" — same resolution as the `datadog-api`
sibling and every other delivered non-matching-family redo in this loop.

Metadata file written: `claude-tag-plugins--claude-liam-grafana-api.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.

## 2026-08-31 — Phase 4 delivery

- **4K master:** `compile.py` without `--review` enforces its 4K LAW
  automatically — wrote `claude-tag-plugins--claude-liam-grafana-api.mp4`
  natively at 3840×2160 (Remotion beats were already rendered at native 4K),
  169.0s, 8/8 beats real, mean_volume -24.0 dB (independently re-verified via
  ffmpeg volumedetect after the 4K compile, not just the compile step's own
  report). Copied to `-4k.mp4` so `deliver.py`'s `newest_master()` picks it as
  the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/claude-tag-plugins--claude-liam-grafana-api/` (4K master +
  description, syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop
  mount); repo
  `humanitarians-youtube/claude-bear/claude-tag-plugins--claude-liam-grafana-api/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `bc6e6c0b`, pushed clean
  (verified `git log origin/main..HEAD` is empty against `origin/main`).

**Status: DELIVERED.**
