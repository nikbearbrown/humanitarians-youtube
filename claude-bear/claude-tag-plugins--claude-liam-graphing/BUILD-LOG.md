# BUILD-LOG — claude-tag-plugins--claude-liam-graphing

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-graphing/beat_sheet.json`
(Teardown register, 7 beats, all `filled`/`VIDEO`, dated 2026-07-18).

**Source-file check (logged, not asked — full detail in QUESTION.md):** the
`source_skill` field points at
`../anthropics/claude-tag-plugins/claude-tag-data-viz/skills/graphing/SKILL.md`,
which does not exist on this machine (checked directly and via `find` across
the whole `claude-tag-plugins` tree — same situation as the `grafana-api` and
`datadog-api` siblings). Not a missing-content problem: the source sheet's
narration is fully written, specific, and non-generic at every beat (five
chartkit primitives, three data helpers each with an explicit skip
condition, the four-step workflow, five judgement defaults, and the source's
own five-things-right / five-gaps list). `PEDAGOGY.md` in the source folder
independently confirms the same five gaps. This build reuses the source
sheet's own stated facts as the record rather than reconstructing
generically, per the redo contract ("keep its facts").

**What changed vs. source:**

- **Register:** Teardown → Plain. The source's `B05` beat and its bespoke
  component `GraphingTell` are built around an explicit "what it gets right /
  where it bites" verdict frame — `GETS_RIGHT`/`BITES` are hardcoded constant
  arrays inside the component's JSX, not props — and `BVDT` is a
  `ClaudeVerdictArtifact` card literally labelled "Verdict." Both are a
  design-quality judgment on the skill's documentation, the identical defect
  shape already logged and worked around on the `grafana-api`/`datadog-api`
  siblings' `*Tell`/`BVDT` pairs. Because the verdict framing is baked into
  `GraphingTell`'s JSX (not prop-driven), reusing it verbatim would have put
  a Teardown-register visual under Plain-register narration — so this build
  did **not** reuse `GraphingTell`/`ClaudeVerdictArtifact` and instead
  authored one new beat (**B03**) on the existing, fully prop-driven
  `MedhavyTwoColumnCard` (confirmed via GATE L: found already in
  `runtime/remotion/src/scenes/` and already used by the `grafana-api`
  sibling), stating the identical underlying facts (the first-step judgment
  call, luminance-derived colors, offline `write_html`, per-helper skip
  conditions, the absolute-path gotcha, the GRID/ACCENT literal-string trap,
  the four-criteria render-and-look sentence, `rolling_mean`'s one-phrase
  edge behavior) as a **both-directions** split ("documented plainly" /
  "easy to miss") rather than a grade. `B01` (`GraphingAnatomy`) and `B02`
  (`GraphingDesign`) *were* reused verbatim — their fixed row content
  (primitives, data helpers, four steps, judgement defaults) was already
  descriptive, not evaluative, and narration was carried over near-verbatim
  from the source (trimmed one repeated clause in B02) without changing any
  fact.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW). Writer types "Claude already KNOWS how to make a good chart,
  right?", hesitates on KNOWS, corrects to "has to be told" → lands "Claude
  already has to be told how to make a good chart, right?" — the naive
  assumption (good chart design is innate Claude taste) corrected to the
  real mechanism (a kit of judgement defaults Claude reads before drawing).
  Picked up directly by B01's opening line.
- **Beat count:** source's 7-beat shape (B00 → B01 anatomy → B02 design →
  B05 teardown → BVDT verdict → BHTF handoff → BOUT outro) restructured to 8:
  B00 (writer) → B01 (anatomy, reused) → B02 (design, reused) → B03 (both
  directions, new component, replaces B05+BVDT) → BCRY (carry-out, new) →
  BHTF (handoff, rewritten) → BOUT + BCTA (the fixed hai-simple `OutroSeries`
  + `OutroCTA` split) — same restructuring precedent as the `grafana-api`/
  `datadog-api` siblings (7 → 8 via the outro split).
- **Facts/argument:** unchanged — five chartkit primitives (`theme`,
  `palette`, `finish`, `save`, `write_html`, including luminance-derived
  color resolution and offline HTML inlining), three data helpers each with
  an explicit skip condition (`zero_fill_days`, `rolling_mean`, `log_floor`),
  the absolute-`sys.path` requirement, the four-step workflow (look → infer
  colors → write → render and look), five judgement defaults with permission
  to deviate, and the source's own five documented gaps (absolute-path
  example written literally, GRID/ACCENT placeholder strings, the
  four-criteria render-and-look sentence with no rubric, `rolling_mean`'s
  one-phrase edge behavior, the PNG-only smoke test) all carry over from the
  source's own stated facts (see QUESTION.md).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — generalized from the
  source's graphing-specific five-point watch-list to a prompt runnable on
  any dataset the viewer picks, testing the same defaults-vs-taste
  distinction the reel opened with (same generalization as the
  `grafana-api`/`datadog-api` siblings' BHTF).

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`GraphingAnatomy`, `GraphingDesign`, `GraphingTell`, `ClaudeVerdictArtifact`)
— no beat in either version was ever AI-VIDEO, pantry, or a human-drop slot.
B03 is also REMOTION (`MedhavyTwoColumnCard`, pre-existing, prop-driven,
confirmed renderable via GATE L rather than authored new). `compile.py`'s
motion-histogram WARNING (`remotion` 8/8 = 100%, over the ~40% pantry cap) is
expected and accepted for the same reason every prior all-REMOTION sibling
in this family has logged it: the NO-GENAI/NO-PANTRY LAW forces every beat
to GRAPHIC or REMOTION, and this reel's body is a documentation/API-quirk
explainer, not a worked-example narrative with room for illustrative Manim
figures.

## Gates

- **GATE T (type_check.py):** one flag, confirmed false positive: `§8.9
  [BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` —
  the middle-dot `·` triggers the same truncation heuristic already logged
  and shipped unfixed on the identical string in the `grafana-api`/
  `datadog-api` siblings. Frame QC (below) confirms the BOUT eyebrow renders
  fully legible, no actual truncation. 0 pixel-beat FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.6s**, clears the ≥8s/≥9s TIMING LAW floor. Frame
  pulls at 5s and 9.5s confirm the writer's correction (KNOWS → "has to be
  told") lands well before 5s and the fully-typed, corrected question —
  "Claude already has to be told how to make a good chart, right?" — is on
  screen and legible before the beat ends.
- **Render note:** `remotion_scenes.py` exceeded the tool's 120s foreground
  timeout and was auto-backgrounded; blocked on it explicitly via
  `TaskOutput` (block=true) per the ONE-SHOT/COMPLETION LAW rather than
  ending the turn. It completed exit 0, 7/8 beats rendered clean; `B03`
  (`MedhavyTwoColumnCard`) failed on the first pass with a transient Remotion
  package-version-mismatch warning cutting off the actual error — re-ran
  `--only B03 --force` in the foreground and it rendered clean on retry
  (21.6s, matches its measured audio).
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect,
  verified independently of `compile.py`'s own report), max -2.9 dB — well
  above the -40 dB floor.
- **Gate V (frame QC):** pulled targeted frames for all 8 beats (B00 at
  5s/9.5s, B01 at 40s, B02 at 100s, B03 at 145s, BCRY at 160s, BHTF at 175s,
  BOUT at 186.2s, BCTA at 187.5s/189s) and read every one. All 8 beats
  legible, correctly kerned, no text overlap, safe inset respected. `BOUT`/
  `OutroSeries` renders on flat white rather than the humanitarians cream
  ground — same shared-component behavior already logged unremarked in the
  `grafana-api` sibling (there it was `BCTA`/`OutroCTA`). `@HumanitariansAI`
  folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (8/8 beats, no violations, canvas 3840×2160 for the native Remotion
  renders; review master compiled at review resolution per `--review`
  default).
- **COMPLETION LAW:** master mp4 mtime (1788210365) newer than beat_sheet.json
  mtime (1788210315); beat_sheet.json will not be touched again — any further
  fix goes through a recompile.

## Output

`claude-tag-plugins--claude-liam-graphing-slate.mp4` (review-cut naming from
`compile.py --review`; no beat is actually a slate — 8/8 beats real VIDEO) —
190.0s, no slate content, audible narration throughout (mean_volume -23.9 dB,
ffmpeg-verified independently). This is the review cut (COMPLETION LAW
satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-tag-plugins"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple`
skill-key fallback → "Claude Basics" — same resolution as the `grafana-api`/
`datadog-api` siblings and every other delivered non-matching-family redo in
this loop.

Metadata file written: `claude-tag-plugins--claude-liam-graphing.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.

## 2026-08-31 — Phase 4 delivery

- **4K master:** `compile.py` without `--review` enforces its 4K LAW
  automatically — wrote `claude-tag-plugins--claude-liam-graphing.mp4`
  natively at 3840×2160 (Remotion beats were already rendered at native 4K),
  190.0s, 8/8 beats real, mean_volume -23.9 dB (independently re-verified via
  ffmpeg volumedetect after the 4K compile, not just the compile step's own
  report). Copied to `-4k.mp4` so `deliver.py`'s `newest_master()` picks it as
  the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/claude-tag-plugins--claude-liam-graphing/` (4K master +
  description, syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop
  mount); repo
  `humanitarians-youtube/claude-bear/claude-tag-plugins--claude-liam-graphing/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `cc65c0e9`, pushed clean
  (verified `git log origin/main..HEAD` is empty against `origin/main`).

**Status: DELIVERED.**
