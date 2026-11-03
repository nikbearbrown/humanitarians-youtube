# BUILD-LOG — healthcare--claude-liam-contracts

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-contracts/beat_sheet.json` (7-beat
Teardown skill-teardown of Anthropic's `contracts` skill, already fully
built and delivered — its own `AUDIT.md` shows GATE T PASS, GATE AUDIO
PASS, no open defects). Unlike some `redo` siblings in other families
(e.g. `claude-for-legal--claude-liam-clearance`), this source carries
**real, filled-in facts**, not unfilled `>` placeholders: skill name
`contracts`, job statement ("Answer a question across a corpus of contract
documents with verified citations"), scope ("use when the user asks what a
contract says, which contracts have a clause, what changed between
amendments, or any question that needs reading and citing across a set of
contract files"), the corpus-must-be-local constraint, and a real 3-file
anatomy (README.md 12k, SKILL.md 40k, sweep.mjs 17k). Every fact in this
build's narration is carried over verbatim from the delivered source sheet.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the
  Teardown moment" and BVDT carried a "Verdict" artifact label with "what
  it gets right / what it bites" judgment framing. This build's B03 states
  the same constraint (a corpus, a question, a cited answer) without a
  design-tell frame, and BCRY carries the fact as a plain carry-out
  sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`.
  Writer types the newcomer's wrong-guess word "APPROVE" (implying Claude
  issues a legal sign/don't-sign verdict on the contract), hesitates,
  corrects to "search" → lands "Will Claude search my contract before I
  sign it?". Picked up directly by B03's stated scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01
  anatomy → B02 pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF
  handoff → BOUT outro), plus the fixed hai-simple outro split
  (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8 beats — same
  restructuring precedent as every sibling in this family
  (`claude-for-legal--claude-liam-clearance` and others).
- **Facts/argument:** unchanged — carried over verbatim from the real,
  already-filled source (see above).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is the source's own handoff line,
  lightly grounded into a concrete first-person scenario ("I have a folder
  of contract files and a question about them...") rather than the
  source's more abstract phrasing, keeping the same "explain your input
  requirements before you act" clause.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components
rather than converting to Manim/GRAPHIC — no beat in either version was
ever AI-VIDEO, pantry, or a human-drop slot. `compile.py`'s motion-histogram
WARNING (`remotion` 8/8 = 100%, over the ~40% pantry cap) is expected and
accepted for the same reason every prior all-REMOTION sibling logged it:
NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or REMOTION, and this
reel's body legitimately has no illustrative-figure beats to draw as
Manim — it is a file/pipeline/constraint explainer, not a worked-example
narrative.

## Gates

- **TYPECHECK / GATE T:** one flag, confirmed false positive: `§8.9
  [BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'`
  — the middle-dot `·` character trips the §8.9 truncation heuristic.
  Identical string, unfixed, already shipped in the DELIVERED
  `claude-for-legal--claude-liam-clearance` sibling; left as-is per that
  precedent rather than reworded away from house style. 0 pixel-beat
  FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 →
  measured `actual_duration_s` **11.09s**, clears the ≥8s floor. Late frame
  pull (t=9s) confirms the full corrected question "Will Claude search /
  my contract / before I sign it?" on screen with the correction landed
  (verified against an earlier frame at t=4s still mid-typing on the
  original "APPROVE" framing).
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect,
  verified independently of `compile.py`'s own report), max -2.9 dB — well
  above the -40 dB floor.
- **Gate V (frame QC):** pulled frames at 6s spacing across the full 68.6s
  runtime, plus a targeted sweep at 44-68s across the carry-out/handoff/
  outro boundary. All 8 beats legible, correctly kerned, no text overlap,
  safe inset respected. `OutroSeries`/`OutroCTA` render on flat white
  rather than the humanitarians cream ground — same shared-component
  behavior already logged unremarked in sibling reels (e.g.
  `claude-for-legal--claude-liam-clearance`). `@HumanitariansAI`
  folderLabel/handle correct on BHTF/BCTA.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (8/8 beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788338621) newer than
  beat_sheet.json mtime (1788338520); beat_sheet.json was never touched
  after the compile that produced the final master.

## Output

`healthcare--claude-liam-contracts.mp4` — 68.6s, 8/8 beats real (no
slate), native 3840×2160 (Remotion beats render at 4K already), audible
narration throughout (mean_volume -24.0 dB, ffmpeg-verified). This is the
review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "healthcare"`
matches no prefix in `playlists.json`'s map; falls to the `hai-simple`
skill-key fallback → "Claude Basics" — same resolution used by every other
`redo` sibling whose family has no direct playlist-map entry (e.g.
`claude-for-legal--*`).

Metadata file written: `healthcare--claude-liam-contracts.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

- **4K master:** `compile.py`'s 4K LAW already forced the master to native
  3840×2160 (Remotion beats render at native 4K), so copied directly to
  `healthcare--claude-liam-contracts-4k.mp4` rather than re-rendering at a
  higher resolution — verified via ffprobe (3840x2160).
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/healthcare--claude-liam-contracts/` (4K master + description,
  syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount);
  repo `humanitarians-youtube/claude-bear/healthcare--claude-liam-contracts/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `7b327134`, pushed clean
  (verified `git log` + `git status` against `origin/main`).

**Status: DELIVERED.**
