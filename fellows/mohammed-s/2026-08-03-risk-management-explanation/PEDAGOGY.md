# PEDAGOGY AUDIT — mycroft-credit-rating
# "AAA to D: Rating Mycroft's Risk Score" | cli-explainer, nbb register (Onyx, no channel fiction)
# Auditor: Claude Sonnet 5 | 2026-07-26

## Source verified
- github.com/Humanitariansai/Mycroft — PR #16, "Add camelCase report format with credit rating (additive, non-breaking)"
- `n8n_Workflows/Risk_Management_Agent/format-report.js` (fetched verbatim via PR diff — new file, 76 lines)
- `n8n_Workflows/Risk_Management_Agent/test-format-report.js` (fetched verbatim via PR diff — new file, 159 lines)
- `Json_code` diff hunk (the actual n8n node's `jsCode` before/after)

## Criteria (required-spine cli-explainer rubric)

### 1. REQUIRED SPINE PRESENT
B00 cold open (ClaudeComposerAsk, ask answered) → B01 PROBLEM (before any prompt) →
B02 CLI → B03 CODE → B04 OUTPUT → B05 CLI (revision) → B06 CODE → B07 OUTPUT →
B08 SUMMARY → B09 NEXT STEPS (handoff) → B10 OUTRO. All eleven required slots
present, in order, none doubled up.
**SCORE: PASS**

### 2. THE ACTUAL-CODE LAW
B03 shows `scoreToRating()` **in full**, byte-identical to `format-report.js`
lines 7–16 — short enough it needed no trimming. B06 shows the `return` block
of `formatReport()` trimmed with a literal `// … 10 more …` elision marker on
both the original-fields half and the camelCase half — every line actually
kept is verbatim source, nothing paraphrased or invented. Ask→code plausibility:
B02's ask ("bond-style tiers, AAA down to D") plausibly generates B03's exact
threshold ladder; B05's ask ("nest it, additive only") plausibly generates
B06's `camelCaseReport` block.
**SCORE: PASS**

### 3. THE REVISION LAW
B05→B06→B07 is a genuine second cycle, not a cosmetic rerun: cycle 1 (B02–B04)
only produces the standalone rating function; cycle 2 adds the actual
integration (nesting, nothing renamed) and a materially different, more
complete OUTPUT (B07 proves the 14+15 key invariant, B04 only proved the
rating math). This is a real design tension pulled from the codebase itself —
`test-format-report.js`'s own comment ("These must never change... the
RiskLog Google Sheet auto-maps to them") is the reason the nested shape was
chosen over a flat added field — not an invented bug-then-fix.
**SCORE: PASS**

### 4. OUTPUT BEATS ARE MOTION, NEVER STILL
B04 and B07 are both Manim scenes (`scenes.py`, not yet authored — see Open
items below), never a static png. Both are specified with an explicit sweep/
assemble motion, not a hold on a finished frame.
**SCORE: PASS** (pending scene authorship, tracked below — does not block the gate)

### 5. NO FABRICATION / DOUBLE-CHECK LAW
Every on-screen number traces to real source: the 9-tier threshold ladder
(100/85/70/55/40/30/20/10) is `scoreToRating()` verbatim. The B04 sweep
values (9, 10, 20, 30, 40, 55, 70, 85, 100) are the literal `RATING_CASES`
boundary pairs in `test-format-report.js`. "14 original keys" / "15
camelCase keys" are the literal lengths of `ORIGINAL_KEYS` and `CAMEL_KEYS`
in the same file. The Google Sheet auto-map claim (B01, B05) is the literal
comment above `ORIGINAL_KEYS`, not an inference. No model-version numbers or
drifting counts appear anywhere.
**SCORE: PASS**

### 6. HANDOFF LAW
B09's prompt is read aloud and discussed (not just displayed): it generalizes
the specific lesson (nest instead of reshape; lock the invariant with a test)
to the viewer's own Code node, using bracketed placeholders for their own
derived field. It is a genuinely runnable prompt, not a summary restated as
a question.
**SCORE: PASS**

### 7. REGISTER / VOICE OVERRIDE APPLIED CORRECTLY
Teardown throughout: every CODE/OUTPUT beat states the mechanism, then the
design judgment (B03: "cuts finer, the way a bond rating cuts finer than
pass or fail"; B06: the additive framing; B08: "the hard part was never the
nine if-statements"). Per your explicit instruction this build, the
nbb persona's default IN-FOR-BEAR line and the `@NikBearBrown` channel
identity are dropped: B00 and B10 sign off as **Mohammed Hussain**, voice is
still Kokoro `am_onyx` ("Onyx"), and the visual palette stays the nbb
teardown palette (white / ink / crimson) since that's a register choice, not
a channel-fiction claim.
**SCORE: PASS**

### 8. DURATION
Sum of `estimated_duration_s` = 168s (2:48) — under your 3:00 cap with a 12s
margin before real Kokoro audio is measured. Word-per-second estimates per
beat range 2.0–3.1, consistent with a brisk but legible Teardown read; actual
runtime will be re-measured from the generated MP3s per the audio-first rule
(never hand-fixed).
**SCORE: PASS**

## Open items (do not block this gate — flagged for the build steps after sign-off)
- **`scenes.py`** for `B04_RatingSweep` / `B07_AdditiveMerge` doesn't exist
  yet — authored after you sign this gate, before `generate_audio_kokoro.py`.
- **Corner logo mark**: the LOGO LAW's low-opacity corner bug is normally the
  NBB mark for `@NikBearBrown` reels. Since this reel signs off as Mohammed
  Hussain, not that channel, I've left the corner mark unset rather than
  reuse a mark that isn't yours — tell me what (if anything) you want there,
  or I'll ship with no corner mark.

## Overall assessment
The episode reconstructs a real, verifiable build: a rating function grounded
in the actual PR diff, a revision motivated by a real invariant documented in
the shipped test file, and an OUTPUT beat pair that proves the additive claim
using the test suite's own assertions rather than a claim taken on faith.
Nothing on screen extends past what `format-report.js` and
`test-format-report.js` actually say.

**VERDICT: PASS** — recommended by this audit; awaiting your sign-off before
any audio is generated (GATE P is a quality gate, not a formality — if
anything above reads wrong, tell me and I'll redraft the beat sheet before
we spend a single render).
