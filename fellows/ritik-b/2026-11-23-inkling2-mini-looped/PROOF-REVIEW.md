# Feedback: "Inkling 2 Mini, Looped Is Better?" — Ritik B., film 13

PROOF-1 (before audio). Each beat's narration + on-screen props is treated as the frame; reveal timings are read
from the pattern code (`ReelFramework` rows land at p 0.14 + 0.11·i → 0.32 + 0.11·i, `BlipLadder` bars at
p 0.11 + 0.095·i, exception at p 0.80–0.94; `ClaudeComposerAsk` types 0.6–2.1 s, output lines from ≈3.0 s).
Facts re-verified 2026-11-25 against config.json, the Inkling-2-Mini and TML-d24-varloop-research model cards and the
lab post (Nov 20, 2026). Re-cut v1 = `agentE_sheets.py` first draft (11 beats, 353 words, est 124.5 s).

## v1 — first pass

**Verdict:** unlisted-until-fixed. 10/12. Production gate FAIL.
This film attempts a config-first audit of a looped model but delivers it with three claims spoken before their
evidence is on screen, because the reveal order of the ask, worked-example and edge beats lags the narration.

### Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown before examples | **2** — B01's three roadmap cards (Read the config · Compute the cost · Check the claim) land at ≈13–16 s, before the first example (B02). |
| Reusable rubric | Viewer can apply the axes to a new case | **1** — card 2 says "compute follows passes", which only fits a looped model; a viewer auditing an ordinary MoE would have to guess what step 2 means. Card 3 hides its second question ("what would break it") inside the first. |
| Worked example | One case walked through live | **2** — B02 computes 6 + 12 × 3 + 6 = 48 from `loop_config`; B03 builds +1.0B per pass from config dims and lands on the lab's 5.4B. |
| Falsifiability / edge | Stress-tested against a counterexample | **2** — B06 puts LAB SAYS / EVIDENCE / NOT SHOWN together; B07 is the counterexample (closed-book trivia barely moves with passes). |
| Active task | Structured CTA, not "ask Claude" | **2** — B09 is a copyable prompt with GOOD / FLAG outcomes and tells the viewer to match per-token compute. |
| Friction | Viewer must resolve a tension | **1** — B04 raises 3.4B vs 5.4B and answers it in the same sentence ("compare speed on five point four"); nothing is left for the viewer to weigh. |

### Production gate — FAIL
- **Legibility at the moment of assertion — FAIL (3 frames).**
  - B00: "twenty-four … forty-eight" is spoken at ≈1–3 s; the only on-screen carrier ("48 runs from 24 stored") is output line 1, which fades in at ≈3.0 s. The typed command has no numbers.
  - B03: "attention plus eight experts: about eighty-three million" is spoken at ≈40–55 % of the beat; the decomposition (18.9M + 8 × 8.0M) exists only in the exception, which fades in at p 0.80.
  - B07: "forty-two points" is spoken at ≈50 %; "+42.1" exists only in the late exception (the bars show 21.1 and 63.2, so the viewer must subtract).
- **Sources on screen — FAIL (1 frame).** B08 line 4 ("passes lift reasoning (+42.1) but not recall") states the variable-loop model's numbers as if they were Inkling 2 Mini's; the model card itself warns against comparing the two directly.
- **Side-by-side at comparisons — PASS.** B04 (text "3.4B active" vs table "5.4 activated"), B05 (middle vs last bars, both ranges), B06 (LAB SAYS + EVIDENCE + NOT SHOWN, all three rows co-visible from p 0.54 to the end, ≈5.5 s), B07 (1 pass vs 3 passes, both tasks).

### The problem
Evidence trails the voice. The film's own rule is "no source, no verdict", yet in B00, B03 and B07 the viewer hears the
number before the frame can show it — the exact sin the series names.

### Do X next
1. [EDIT] B00 — open the typed command with "stores 24 layers but runs 48 per token" so the numbers are on screen by ≈1 s, as they are spoken.
2. [EDIT] B03 — move the decomposition into bar 2's sub ("per looped layer: attention 18.9M + 8 experts × 8.0M ≈ 83M; × 12 ≈ +1.0B", visible from p 0.2); the exception becomes the conclusion and says which input is lab-reported (3.4B) and which is computed (+1.0B).
3. [EDIT] B07 — put "+42.1" / "+1.0" in the 3-pass bars' subs so the difference is on screen when spoken.
4. [EDIT] B08 — label line 4 "variable-loop model" so the verdict doesn't transfer its numbers to Inkling 2 Mini.
5. [EDIT] B01 — make the rubric general: card 2 "Memory follows what's stored; compute follows what runs per token"; card 3 "Put each claim beside its evidence. Then ask what would break it." Voice the second question.
6. [EDIT] B04 — make it a question the viewer has to hold: the LABELS row first (text 3.4B vs table 5.4B), narration asks "Which is it?", the rule row answers only for memory vs speed, and B09's prompt makes the viewer apply it (pick a ~5B-active comparison, not 3.4B).
7. [EDIT] B07 — add the tension the lab's own caveat creates: the variable-loop model rarely trained at 1 pass, so its 1-pass scores may understate — but trivia had the same handicap and still barely moved. Viewer has to weigh both.
8. [EDIT] B05 — drop "one early checkpoint": the post gives "training step 2,000" but never calls it early. Say "one checkpoint, at step 2,000".
9. [EDIT] B06 — "extrapolated" → "a scaling-law prediction"; NOT SHOWN receipt "unpublished" → "not in post" (absence elsewhere can't be proven).
10. [EDIT] B02 — drop the GATE row (unvoiced mechanism, and its "starts fully closed" needs the lab's word, contradicting the keepNote); replace with an EXPERTS row (8 of 128, no shared expert) that B03's arithmetic depends on, and mark the LOOP row "(zero-indexed)" so "core_start 6 → layer 7" is on screen.

### What works
The three-step audit is real and each body beat's spark names its step; the 6 + 36 + 6 count and the +1.0B-per-pass
build are genuine worked steps from `config.json`; B05's "the middle's worst beats the end's best" is a reasoning move
the viewer can check against the bars; B07 uses the lab's own per-pass table to find where its claim stops.

### Found while re-scoring (applied with the fixes above)
11. [EDIT] B01 — the roadmap cards land at p 0.54 / 0.62 / 0.71, but v1 voiced "Read the config" at p ≈ 0.35, ahead of its card. v2 opens with a 17-word framing line so each step is voiced as its card lands.
12. [EDIT] B02 — v1 voiced "twenty-four layers" and the expert count before rows 1–2 could arrive. v2: heading "24 layers stored, 48 run per token" (on screen by p 0.12), experts folded into row 1, rows reordered STORED · LOOP · READ AS (zero-indexed → 7–18) · COUNT so each row is half-visible before it is voiced.
13. [EDIT] B05 — "one checkpoint, at step two thousand" is voiced at p ≈ 0.65, before the exception; v2 puts "at step 2,000" in every bar's sub (on screen from p 0.11).
14. [EDIT] B07 — v2 ends on "And the one-pass handicap hit both", voiced at p ≈ 0.9 when the exception carrying that caveat is up.

## v2 — after fixes (this is the cut that goes to audio)

**Verdict:** clear-for-public. **11/12.** Production gate **PASS**.
This film attempts a config-first audit of a looped model and delivers it: a reusable three-step rubric lands at
≈15–19 s, every body beat names the step it applies, and every number is on screen, with its source, when voiced.

### Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown before examples | **2** — B01 roadmap (Read the config · Compute the cost · Check the claim) is on screen by ≈19 s, before the first example; each step is voiced as its card lands. |
| Reusable rubric | Viewer can apply the axes to a new case | **2** — the cards are model-agnostic ("what is stored, and what repeats"; "memory follows what's stored, compute follows what runs per token"; "claim beside evidence, then what would break it"). Run on a plain MoE, step 2 is simply its active count. Every body beat's spark line names its step. |
| Worked example | One case walked through live | **2** — B02: `core_start 6 · core_end 18 · num_passes 3` → zero-indexed → 7–18 → 6 + 12 × 3 + 6 = 48. B03: attention 18.9M + 8 × 8.0M ≈ 83M per looped layer → × 12 ≈ +1.0B per pass → 3.4 + 2 × 1.0 = 5.4B, with which input is lab-reported (3.4B) and which is computed (+1.0B) said on screen. |
| Falsifiability / edge | Stress-tested against a counterexample | **2** — B06 holds LAB SAYS / EVIDENCE / NOT SHOWN / VERIFIED together; B05 shows the lab's 27-of-28 claim beside its own chart and the chart's limits; B07 is the counterexample (closed-book trivia +1.0 vs graph search +42.1 on the lab's own per-pass table). |
| Active task | Structured CTA, not "ask Claude" | **2** — B09: copyable prompt (local run, ~5B-active non-looped rival, 30 reasoning + 30 closed-book questions, accuracy + tokens/s) with GOOD / FLAG outcomes on screen. |
| Friction | Viewer must resolve a tension | **1** — two real tensions are on screen side by side (B04: the lab's text "3.4B active" vs its table "5.4 activated"; B07: the lab's own caveat that 1-pass scores may understate, against trivia barely moving under the same handicap), and B09 makes the viewer apply the resolution when picking a rival. But the narrator resolves both on the viewer's behalf within the beat, so it is received more than worked. Kept at 1 rather than spend ≈5 s of a 2:00 budget on a predict-then-reveal pause. |

### Production gate — PASS
- **Legibility at the moment of assertion — PASS.** B00: "stores 24 layers but runs 48" leads the typed command (on screen by ≈0.9 s; voiced ≈1.2–2.5 s). B02/B04/B06: the beat's key number is in the heading (on screen by p 0.12) and each row is half-visible before it is voiced. B03: the 83M decomposition sits in bar 2's sub (p ≥ 0.2), voiced at p ≈ 0.35–0.6. B05: "27 of 28" in the heading, "step 2,000" in every sub, "the 28 aren't listed" voiced at p ≥ 0.85 as the exception lands. B07: "+42.1" / "+1.0" in the 3-pass subs; the handicap caveat voiced at p ≈ 0.9. B08 lines are all up within ≈1.5 s. Type: one-decimal bar values, ≥ 23 px subs at 1080-short-axis (≥ 46 px at 4K); no fade below 100 % once revealed.
- **Sources on screen — PASS.** Every beat carries `source` / `sourceNote` / the ask's running line; every ReelFramework row that states a number has a receipt; computed rows say "computed"; the variable-loop numbers are labelled as that model's (B07 footer, B08 line 4).
- **Side-by-side at comparisons — PASS.** B04 text vs table (rows 1–4 co-visible from p 0.65, ≈5 s); B05 middle vs last, all four estimates plus the reference line at the end's best; B06 claim + evidence + not-shown co-visible from p 0.54 (≈5 s); B07 1 pass vs 3 passes for both tasks from p 0.52 (≈7 s).

### The problem (residual)
Friction is the weakest criterion: the tensions are shown, not left open. Acceptable for a 2:00 cut; noted for the series.

### Do X next
- [EDIT] (optional, not applied) A predict-then-reveal line in B04 ("before the rule: which number do you match?") would lift friction to 2 at ≈5 s of runtime.
- After audio: confirm the measured runtime lands in 1:55–2:10; trim B01's framing line first if it runs long.

### What works
The audit is reusable and visibly applied; both worked steps come from `config.json`, not from the lab's prose; the film
scores the lab's claims by evidence type (verified / computed / lab-only / the lab's own counter-data) and hands the
viewer a test that uses the film's own rule (match per-token compute, not the 3.4B headline).

**PROOF-1 result: 10/12 → 11/12; production gate FAIL → PASS. Cleared for audio.**

### After audio (measured)
First generation measured 129.99 s — inside 1:55–2:10 but on its edge. Trimmed B06's closing line ("Verified loop,
lab-reported advantage.") — its keepNote and B08's verdict line carry the same point on screen — and regenerated B06
only: **127.75 s (2:07.8), 11 beats**. B06 sync re-checked: "no outside replication cited" now closes the beat at
p ≈ 0.75–1.0 with the NOT SHOWN row up since p 0.45. B01's framing line was kept: it is what lands each step on its card.

## PROOF-2 (lead — rendered frames, both cuts)

**Verdict:** ship at 11/12. GATE V 0 BLOCKER / 0 MAJOR in both cuts (22 frames each), before and after the fix.
- [FIXED] B02 row 3 read "Zero-indexed: layers 7–18" — 7–18 is the count from 1 (zero-indexed it is 6–17). Now "Config counts
  from 0; from 1, layers 7–18 run three times, same weights." Re-rendered B02 in both cuts, recompiled, GATE V re-run clean.
- Labels all fit their columns in 16:9 (longest NOT SHOWN); bars read by their values; 9:16 has no clipping.
