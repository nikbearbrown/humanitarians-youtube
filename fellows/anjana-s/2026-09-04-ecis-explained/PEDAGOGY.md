# PEDAGOGY — ECIS Episode 5: The System That Learned From Its Own Mistakes (ai-explainer, narrated by Anjana)

Fresh build from the pre-authored `narration/*.txt` + `visuals/*.md` briefs in
this folder (`script.md` and `README.md` were skeletons). One insight: the
system did not get bigger this week — it got more honest about where it was
wrong. Every upgrade in this episode is a correction derived from ECIS's own
reviewed errors, not a new capability bolted on.

Sequel to Episodes 1–4. Episode 3 gave it three models, gates, and provenance;
Episode 4 gave it speaker authority, chunk quality, and trend context. Episode 5
closes the loop: the system reviews its own output and retrains on the boundary
it kept missing.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the mechanism itself — the four-reader
  pipeline, the decision boundary, the two vote panels, the three detectors, the
  decay timelines, the five-dimension close ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence
  (the two boundary quotes, the vote spreads, the density meters, the hash
  match, the three horizon checkmarks) lives on screen, not in the voice ✓
- your-turn closing standard: B07 VERDICT (`ClaudeVerdictArtifact`, handoff line
  "Let's recap with Claude.") → B08 YOUR TURN (`ClaudeComposerAsk`, prompt read
  aloud verbatim and discussed per HANDOFF LAW) → B09 TITLE outro ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip. Source
  files say `am_onyx` — overridden to `af_bella` per the series convention set
  in Episode 1 ✓
- Dark-stage deviation: B01–B06 render on the dark ground (`#0a0a0f`) rather
  than the default cream fidelity stage — the same PEDAGOGY-approved deviation
  carried by Episodes 1–4, kept for series continuity.
- **NARRATION BUDGET — logged deviation.** Four body beats (B01 ~105 words, B02
  ~95, B03 ~110, B04 ~105) run over the 45–70-word body-beat range. Kept
  verbatim from the pre-authored `narration/*.txt` per the series convention
  (Episodes 3 and 4 did the same). Mitigation: each of those beats carries a
  dense multi-stage `show` block, so the voice is reacting to visible evidence
  rather than reciting an unseen list — the PPT TEST passes. Flagged here rather
  than silently accepted; if a future episode trims, this is the beat set to cut.
- **No real company names or tickers anywhere in this reel** — B05 uses Company
  A and Company B, matching the Episode 4 convention; the B02 boundary quotes
  and the B04 negation chunk are generic, illustrative constructions, not real
  transcript excerpts.

## Series coherence check

Two places where Episode 5 could look like it contradicts an earlier episode.
Neither does, and both are deliberate:

| Apparent tension | Resolution |
|---|---|
| B01 says "four independent readers"; Episode 3 was about *three models* (Llama, Mistral, Qwen) | Different axes. The four READERS are keyword matching, FinBERT, NER, and an LLM. The LLM reader is the one that runs three models. Consistent, not a retcon. |
| B06 says "five weight dimensions"; earlier episodes named fewer | The series arc: Reader (Ep 1) → Model (Ep 2–3) → Speaker + Quality (Ep 4) → Section (Ep 5). Section weighting is the fifth, and it is introduced in this episode's B03. The count is the running total, and it checks out. |

## Evidence discipline (DOUBLE-CHECK LAW)

Every figure below comes from the pre-authored `narration/*.txt` and
`visuals/*.md` briefs in this folder — the author's own description of their own
system. **Nothing was invented for the video.** Rows are listed so a human can
confirm each one still matches the real pipeline before audio is generated.

| Claim (as scripted) | Where it appears | Source in this folder | Confirmed? |
|---|---|---|---|
| Four independent readers: keyword matching, FinBERT, NER, LLM | B01 | `narration/01_recap.txt` | ☑ |
| Signals pre-registered before outcome, graded at 30 / 90 / 180 days | B01, B05 | `narration/01_recap.txt`, `05_decay.txt` | ☑ |
| The maintained-vs-none boundary was the pipeline's hardest call | B02 | `narration/02_finetune.txt` | ☑ |
| QLoRA adapter on an 8B base model — rank 16, 4-bit quantization, 5 epochs | B02 | `narration/02_finetune.txt` | ☑ |
| "200+ reviewed extractions" as the training-data counter | B02 | `visuals/02_finetune.md` | ☑ |
| Self-consistency = same prompt 3×, majority vote | B03 | `narration/03_penalties.txt` | ☑ |
| Penalty now scales with majority/minority spread (was flat) | B03 | `narration/03_penalties.txt` | ☑ |
| Worked spreads: 0.80 vs 0.75 → 0.77; 0.80 vs 0.20 → 0.62 | B03 | `visuals/03_penalties.md` | ☑ |
| Section weights: prepared remarks 1.0, Q&A 0.8; 0.75 × 0.8 = 0.60 | B03 | `narration/03_penalties.txt`, `visuals/03_penalties.md` | ☑ |
| Negation forces full extraction; FinBERT handles negation inconsistently | B04 | `narration/04_detectors.txt` | ☑ |
| Keyword density separates explicit lexical signals from sentiment-only ones (0.85 vs 0.05 meters) | B04 | `narration/04_detectors.txt`, `visuals/04_detectors.md` | ☑ |
| Duplicate transcripts caught by matching and skipped | B04 | `narration/04_detectors.txt` | ☑ |
| Decay profile: right at 30 but wrong at 180 = decaying; right at all three = persistent | B05 | `narration/05_decay.txt` | ☑ |
| Five weight dimensions: Reader, Model, Speaker, Quality, Section | B06 | `visuals/06_close.md` | ☑ |
| The two boundary quotes and the negation chunk | B02, B04 | `visuals/02_finetune.md`, `04_detectors.md` | ☑ illustrative — generic constructions, not real transcript excerpts |
| Company A "raised, 0.84" / Company B "lowered, 0.79" | B05 | `visuals/05_decay.md` | ☑ illustrative — generic placeholders, no real tickers |

**Standing rule for this table:** if any row stops describing the real pipeline
— a hyperparameter changes, a detector is dropped, the section weights move —
fix the beat's narration and on-screen text before re-rendering. Episode 3
shipped a first draft claiming a twenty-five-company run that had not happened;
that correction is why this table is per-figure and why every row names its
source file.

## Friction protected

- Kept: all three detectors in B04 rather than trimming to the most visual one
  — the rhythm of three fast upgrades is what sells "the system audited itself,"
  and cutting to one would make it look like a single patch.
- Kept: both vote panels in B03 side by side. The insight is that the *same*
  2/3 vote earns a different penalty; one panel alone cannot carry that.
- Kept: the deliberately small QLoRA adapter block in B02. The temptation is to
  scale it up for legibility, but its smallness relative to the base model IS
  the argument — a targeted fix, not a retrain.
- Kept: B01's full recap, even though it repeats Episode 1. A viewer arriving at
  Episode 5 cold needs the four-reader pipeline before any of the upgrades mean
  anything.

## Sign-off notes

1. Evidence table above is per-figure and every row names the source file in
   this folder that it came from. No figure was invented for the video.
   **Human confirmation obtained before audio spend (2026-09-04)** on the four
   falsifiable rows most likely to drift: the QLoRA hyperparameters (rank 16,
   4-bit, 5 epochs, 8B base), the "200+ reviewed extractions" counter, that all
   three detectors actually shipped, and the 1.0 / 0.8 section weights. All four
   confirmed as describing the real pipeline.
2. Narration-budget deviation on B01–B04 logged above and accepted, on the
   condition that each carries a dense `show` block (they do).
3. Dark-stage deviation for B01–B06 approved, continuing Episodes 1–4.
4. Series coherence checked against Episodes 3 and 4 (readers vs models; the
   running five-dimension count).
5. Animated-slate review happens after `remotion_scenes.py` renders — frame-grab
   QC per VISUAL QC LAW, both orientations.

VERDICT: PASS
