# BUILD LOG — hai-simple/knowledge-work-plugins--claude-liam-interview-prep

Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-interview-prep` (Teardown
register, 7-beat skill-teardown of an Anthropic skill named `interview-prep`) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.

## Source defect found on read

The source's B03 narration truncates its own quoted trigger-phrase list mid-sentence:
"Claude's job: Create structured interview plans with competency-based questions and
scorecards. Trigger with \"inte." — cut off right after opening the quote. This is the
same batch template-truncation bug already logged on this family's `call-prep` and
`claude-for-legal/customize` siblings. Milder here too: the source's own B00 carries the
complete, untruncated sentence — "Create structured interview plans with competency-based
questions and scorecards. Trigger with 'interview plan for', 'interview questions for',
'how should we interview', 'scorecard for', or when the user is preparing to interview
candidates." Nothing had to be invented; the complete phrase list was recovered from B00
and used wherever B03's truncated copy would otherwise appear. Full detail in
`QUESTION.md`.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's B03 opened with "Here is the Teardown moment"
  and B03/BVDT carried "what it gets right / what it bites" and "Verdict" framing; this
  build's B03 states the same scope without ruling on the skill's design, and BCRY
  carries the fact as a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "CONDUCT" (implying Claude runs the interview
  itself), hesitates, corrects to "prep" → lands "Does Claude prep interviews for me?".
  The correction is picked up directly by B03's stated scope (Claude builds the plan,
  never conducts the interview) and by BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  source's single `BOUT` (`ClaudeTitleOutro`) split into hai-simple's fixed two-part
  Humanitarians AI outro (`OutroSeries` + `OutroCTA`) — 7 → 8 beats total, same
  restructuring precedent as every other hai-simple redo in this family (e.g.
  `knowledge-work-plugins--claude-liam-call-prep`).
- **Facts/argument:** unchanged and generalized — the skill's anatomy (SKILL.md, 1k, the
  only file), its pipeline (Steps section, linear execution), and its scope (creates a
  structured interview plan with competency-based questions and a scorecard, triggered on
  specific phrases, nothing outside that) are reworded only for register. The source's
  truncated trigger-phrase quote is completed from its own B00, never guessed at.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is a new, complete first-person Claude prompt
  ("Read the interview-prep skill in this folder, tell me exactly what sections the plan
  will include, then build me an interview plan for a role I name") — the source's own
  handoff quoted the skill's job description but never asked Claude to state its own
  scope before acting.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the
~40% pantry cap) is expected and accepted for the same reason every prior all-REMOTION
sibling logged it: this reel is a file/pipeline/scope explainer, not a worked-example
narrative, and has no illustrative-figure beats to draw as Manim.

## Gates

- **TYPECHECK / GATE T:** first pass FAILed on B03 (§8.5 no-wordy-card: the `body` prop
  counted as 13 words, over the 12-word pull-quote limit — the hyphenated
  "competency-based" token counts as two words). Fixed by shortening `body` to "One
  interview plan, questions and scorecard — nothing more." (8 words). Second pass: PASS,
  0 FAILs (all 8 beats §8.10 SKIP — no truncation issues in this build's own strings).
- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.0s**, clears the ≥8s/≥9s-window floor. Frame pull at t=9.5s (of
  11.0s) confirms the full corrected question "Does Claude prep interviews for me?" on
  screen with the correction already landed and the cursor still blinking.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor), max
  -2.9 dB. Verified independently via `ffprobe`/`ffmpeg volumedetect` on the compiled
  master, not just the compile-step log.
- **Gate V (frame QC):** sampled one frame per beat (B00 late, B01, B02, B03, BCRY, BHTF,
  BOUT, BCTA) at full 3840×2160 resolution and read each: all legible, correctly kerned,
  no text overlap, safe inset respected, `@HumanitariansAI` handle correct throughout.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations).

## Output

`knowledge-work-plugins--claude-liam-interview-prep.mp4` — 76.7s, 8/8 beats real (no
slates), native 3840×2160 (compile.py's 4K LAW forces this even without `--review`, since
all beats are Remotion rendered natively at 4K), audible narration throughout
(mean_volume -23.9 dB, independently verified). This is the review cut AND satisfies the
4K master requirement in the same file (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, audible audio verified via ffprobe independently of compile.py's own
GATE AUDIO report).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches the `knowledge-work-plugins` prefix in
`playlists.json`'s map directly (no fallback needed).

## Phase 4 (4K + delivery)

- **4K master:** the Phase-3 compile already wrote the master natively at 3840×2160 (see
  Output above). Copied it to
  `knowledge-work-plugins--claude-liam-interview-prep-4k.mp4` so `deliver.py`'s
  `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/knowledge-work-plugins--claude-liam-interview-prep/` (4K master + description,
  syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-interview-prep/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md +
  QUESTION.md — no media).

**Status: DELIVERED.**
