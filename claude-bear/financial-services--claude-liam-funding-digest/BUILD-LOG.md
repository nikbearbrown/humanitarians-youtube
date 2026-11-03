# BUILD-LOG — financial-services--claude-liam-funding-digest

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-funding-digest/beat_sheet.json`
(Teardown register, 7 beats, all `filled`/`VIDEO`, dated 2026-08-03).

**Source-file check (logged, not asked — full detail in QUESTION.md):** the
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/spglobal/skills/funding-digest/SKILL.md`,
which does not exist on this machine (checked directly and via `find` across
`anthropics/financial-services` and the rest of `anthropics/`). Same situation
as the `claude-tag-plugins--claude-liam-datadog-api` precedent: not a
template-placeholder defect — the source sheet's B00 narration already quotes
the skill's full frontmatter description verbatim (trigger phrases, output
format, output fields), and B01/B02 carry specific, non-generic facts (file
sizes, folder anatomy, pipeline shape). This build reuses those stated facts
as the record rather than reconstructing generically, per the redo contract.

**What changed vs. source:**

- **Register:** Teardown → Plain. The source's B03 (`SkillTeardownMechanism`,
  narration: "What it gets right: repeatable results. What it bites: anything
  outside the spec.") and `BVDT` (`ClaudeVerdictArtifact`, a card literally
  titled "Verdict") are a design-quality judgment on the skill. Both dropped.
  `B01` (`SkillTeardownAnatomy`) and `B02` (`SkillTeardownPipeline`) *were*
  reused verbatim — their narration and their fully prop-driven components
  (eyebrow/title/files/phases all props, no fixed judgment text in the JSX —
  verified by reading both component source files) were already descriptive,
  not evaluative, in the source. The B03/BVDT pair is replaced by one new
  **both-directions** beat (**B03**, `MedhavyTwoColumnCard`, found via GATE L:
  `./art scenes --check MedhavyTwoColumnCard`, prop-driven, no baked-in verdict
  framing) stating the identical underlying facts — named triggers get the
  same fixed one-page slide; anything the file never names has nothing backing
  it — as two directions ("what the file names" / "what it doesn't say")
  rather than a grade.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW). Writer types "Claude already KNOWS what a good funding digest
  should say, right?", hesitates on KNOWS, corrects to "has to be told" →
  lands "Claude already has to be told what a good funding digest should say,
  right?" — the naive assumption (Claude exercises its own editorial judgment
  about what's newsworthy) corrected to the real mechanism (a file Claude
  reads before acting, which fixes the exact scope). Picked up directly by
  B01's "file it reads before acting" framing.
- **Beat count:** source's 7-beat shape (B00 → B01 anatomy → B02 pipeline →
  B03 design tell → BVDT verdict → BHTF handoff → BOUT outro) restructured to
  8: B00 (writer) → B01 (anatomy, reused) → B02 (pipeline, reused) → B03 (both
  directions, new component, replaces source B03+BVDT) → BCRY (carry-out, new)
  → BHTF (handoff, rewritten/generalized) → BOUT + BCTA (the fixed hai-simple
  `OutroSeries` + `OutroCTA` split) — same 7→8 restructuring precedent as
  `claude-tag-plugins--claude-liam-datadog-api` and the `claude-for-legal--*`
  family.
- **Facts/argument:** unchanged — the skill's quoted frontmatter description
  (trigger phrases: "deal flow digest," "weekly funding recap," "deal
  roundup," "transaction summary this week," "what happened in [sector] this
  week," "capital markets update"; output: one-page PPTX with key takeaways,
  valuation data, Capital IQ deal links), the 3-file anatomy (LICENSE 11k,
  SKILL.md 29k, references/), and the linear read→execute→return pipeline all
  carry over from the source's own stated facts (see QUESTION.md).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — generalized from the source's
  Datadog-specific... (n/a here) — generalized from a funding-digest-specific
  ask to a prompt runnable on *any* recurring report or slide the viewer
  already asks for, testing the same named-recipe-vs-judgment distinction the
  reel opened with.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`) — no beat in either version was ever AI-VIDEO,
pantry, or a human-drop slot. B03 is also REMOTION (`MedhavyTwoColumnCard`,
pre-existing, prop-driven, found via GATE L rather than authored new).
`compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the ~40%
pantry cap) is expected and accepted for the same reason every prior
all-REMOTION sibling in this loop has logged it: the NO-GENAI/NO-PANTRY LAW
forces every beat to GRAPHIC or REMOTION, and this reel's body is a
documentation/skill-scope explainer, not a worked-example narrative with room
for illustrative Manim figures.

## Gates

- **GATE L:** `./art scenes --check` run for all 8 patterns before slating —
  all RENDERABLE (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
  `SkillTeardownPipeline`, `MedhavyTwoColumnCard`, `WantQuote`,
  `ClaudeComposerAsk`, `OutroSeries`, `OutroCTA`).
- **GATE T (type_check.py):** one flag, confirmed false positive: `§8.9
  [BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` —
  the middle-dot `·` triggers the same truncation heuristic already logged and
  shipped unfixed on the identical string in the `claude-tag-plugins--*`
  and `claude-for-legal--*` siblings. Frame QC (below) confirms the BOUT
  eyebrow renders fully legible, no actual truncation. 0 pixel-beat FAILs
  beyond that one flag, 0 shape FAILs.
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.5s**, clears the ≥8s/≥9s TIMING LAW floor. A t=9.5s
  frame pull confirms the correction fully landed on screen: "Claude already /
  has to be told what a good / funding digest / shou|" (mid-type on the final
  word, correction already typed and visible).
- **Render:** `remotion_scenes.py` ran past the tool's 120s foreground timeout
  and was auto-backgrounded — blocked on it explicitly via `TaskOutput` per
  the ONE-SHOT/COMPLETION LAW rather than ending the turn. Completed clean,
  8/8 beats rendered, exit code 0, no retries needed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -2.9 dB — well above the
  -40 dB floor.
- **Gate V (frame QC):** pulled frames every 5s across the full 81.0s runtime,
  plus targeted frame pulls of B00 (t=9.5s, correction check), B03 (t=40s,
  two-column card), BCRY (t=52s, carry-out quote), and BOUT (t=76.5s, eyebrow
  truncation check). All 8 beats legible, correctly kerned, no text overlap,
  safe inset respected. BOUT eyebrow "CLAUDE BASICS · HUMANITARIANS AI"
  renders fully, confirming the GATE T flag as a false positive.
  `@HumanitariansAI` folderLabel explicit on B00 and BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (8/8 beats, no violations).
- **COMPLETION LAW:** review-cut mp4 mtime (1788305285) newer than
  beat_sheet.json mtime (1788305251); beat_sheet.json was never touched after
  the compile that produced this review cut, and will not be touched again —
  any further fix goes through a recompile.

## Output

`financial-services--claude-liam-funding-digest-slate.mp4` (review-cut naming
from `compile.py --review`; no beat is actually a slate — 8/8 beats real
VIDEO) — 81.0s, no slate content, review-resolution 1280×720 (compile.py's
`--review` default; the 4K master follows in Phase 4 under the 4K LAW),
audible narration throughout (mean_volume -23.9 dB, ffmpeg-verified). This is
the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "financial-services"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple`
skill-key fallback → "Claude Basics" — same resolution every other delivered
non-matching-family redo in this loop has used
(`claude-tag-plugins--claude-liam-datadog-api`, the `claude-for-legal--*`
siblings).

Metadata file written:
`financial-services--claude-liam-funding-digest.md` (channel @HumanitariansAI,
Playlist: **Claude Basics**, plus the direct code link per the DELIVERY
CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.
