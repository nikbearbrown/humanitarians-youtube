# Feedback: "Inkling 2 Small, What Changed?" — Ritik B., film 12 (explainer)

PROOF-1 — before audio. The "frame" for each beat is its narration plus the on-screen props in
`beat_sheet.json`, read against the pattern source (`ReelFramework.tsx`, `BlipLadder.tsx`, `ReelExecSummary.tsx`,
`ClaudeComposerAsk.tsx` in brutalist.art, read-only) for *when* each element becomes visible. Two passes are kept:
the first assembled cut (v1) and the cut after the [EDIT]s (v2, the one sent to audio).

---

## Pass 1 — first assembled cut (v1)

**Verdict:** unlisted-until-fixed. **9/12.** Production gate **FAIL**.
"This film attempts a config-first audit of a generation change but delivers three steps of a four-step rubric,
with two numbers voiced before they are readable, because the cut was written before checking what each pattern
actually renders and when."

### Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown before the examples | **1** — B01 voiced a 4-step rubric, but `ReelExecSummary` renders `roadmap.slice(0, 3)`: step 4 ("find what would break it") was spoken and never shown. The numbered steps were also voiced in the first 3 s of B01, before the cards fade in at 44–81 % of the beat. |
| Reusable rubric | Viewer can apply the axes to a new case | **1** — step 3 offered only "stated reason / OPEN". The attention-residual change (B06) fits neither: there *is* a published reason, just not the lab's. A viewer applying the rubric to a new model would have to guess. |
| Worked example | One case walked through live, reasoning visible | **2** — B03 recomputes 17B active from config.json bar by bar, each bar a named product. |
| Falsifiability / edge | Rubric stress-tested on a counterexample | **1** — B05 put claim and config side by side, but B06's hard case ended in narration ("a paper says…") with no score: the rubric was extended by voice-over, not tested on screen. B03's untied-embedding assumption was hidden, so the worked example could not fail visibly. |
| Active task | Structured CTA, not "ask Claude" | **2** — copyable prompt with GOOD / FLAG lines. |
| Friction | Viewer must resolve a tension | **2** — B04's two bars disagree about what "Small" means (−59 % compute vs −39 % stored). (Note: v1 answered its own question in the same breath — fixed below anyway.) |
| **Total** | | **9/12** |

### Production gate — FAIL
- **Legibility at the moment of assertion — FAIL.**
  - B01: step 4 voiced, never rendered (3-card limit). Steps 1–3 voiced ~3 s before their cards appear.
  - B03: "about thirty-two million parameters" voiced at ~20 % of the beat, but 31.9M lived only in `exception`, which fades in at 80–94 %.
  - B04: the model card's "≥ 500 GB of GPU memory" voiced at ~70 %, carried only in `exception` (80 %+).
- **Sources on screen — FAIL.** B00's output lines had no dates and the running line named no posts; "on purpose"
  (Inkling's encoder-free choice) was voiced with nothing on screen to back it.
- **Side-by-side — PASS.** B02 (old → new per row), B05 (lab quote vs config), B04 (two bars) all hold ≥ 2 s.

### The problem
B01 — the framework beat — was the weakest frame in the film: a rubric the viewer cannot see in full is the
"empty center" this standard hunts. Everything downstream (step labels, the verdict's scores) depends on it.

### Do X next
1. [EDIT] B01: fold the rubric to **3 steps** that fit the 3 cards (diff the configs · recompute the headline ·
   match change to reason, or OPEN). "What would break it" moves to where it can be shown: B06's hard case.
2. [EDIT] B01: open with a 15-word intro so "One / Two / Three" land as cards 1–3 fade in (44 / 53 / 61 %).
3. [EDIT] B03: print each multiplication in the bar's `sub` ("each 3 × 4,608 × 2,304 = 31.9M"), so the number is
   on screen while voiced; name the assumptions in `source` (gated MLP, router omitted).
4. [EDIT] B03: make the worked example falsifiable on screen — `exception` cross-checks the total (≈ 594.1B vs the
   lab's 594B) and shows that tied embeddings would give 16.3B / 593.1B, so the untied assumption is tested, not assumed.
5. [EDIT] B04: move "≥ 500 GB" into the `heading` (visible from the first second); end the beat on the open
   question ("which number earns the name Small?") and let the verdict score it, so the viewer holds the tension.
6. [EDIT] B05: v1 said "≈ 292M ✓". The computed range is 291.7–292.9M depending on whether the patch embedding
   includes the temporal axis — show the range, not a tick.
7. [EDIT] B06: v1 voiced "the idea comes from a Kimi team paper". The lab never says so; the link is our inference
   from a config key name. Say "the nearest paper", put the lab's silence on screen (`LAB SAYS: Nothing`), and score
   the case **BORROWED** in the keep-note — the rubric's third outcome, which the handoff and verdict then use.
8. [EDIT] B00: date-tag the output lines (JUL 15 / NOV 5), say "encoder-free by design" on screen, and name
   thinkingmachines.ai's two posts and both config files in the running line.
9. [EDIT] B07: turn the verdict into a scorecard (CHECKED / VISIBLE / OPEN-BORROWED / FRICTION) so the close
   scores the claims with the rubric's own words.

### What works
The spine is right: hook on a real reversal (encoder-free → 292M encoder, audio dropped, no stated reason), a
worked recompute of the headline, claim-vs-config side by side. Keep B02's old → new rows with config-key receipts,
and B03's bar-per-product ladder with the lab's 17B as the dashed line.

---

## Pass 2 — after the [EDIT]s (v2, sent to audio)

**Verdict:** clear-for-public (pending PROOF-2 on frames). **12/12.** Production gate **PASS**.
"This film attempts a config-first audit of Inkling → Inkling 2 Small and delivers it: a 3-step rubric shown by
~23 s, each step applied on screen, a hard case that forces a third score, and a task that reuses all three."

### Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown before the examples | **2** — B01 shows the 3-step audit as numbered cards (thesis by ~14 s, cards 17–22 s), each card landing as it is voiced, before any Inkling number. |
| Reusable rubric | Viewer can apply the axes to a new case | **2** — diff → recompute → match change to reason, scored CHECKED / OPEN / BORROWED. The handoff restates all three for any model family. |
| Worked example | One case walked through live, reasoning visible | **2** — B03: 31.9M per expert × 8 × 48 = 12.2B, + 3.2B attention, + 1.9B embeddings = 17.3B vs the lab's 17B dashed line; each product printed under its bar. B05 repeats the move for the 292M encoder (23 × 12 × 1,024²). |
| Falsifiability / edge | Rubric stress-tested on a counterexample | **2** — B05 holds LAB SAYS / CONFIG / COMPUTED / WHY? together; B06 is an ambiguous case (a reason exists, from another model) that the 2-outcome rubric cannot score, forcing BORROWED; B03 shows how its own assumption could fail (tied → 16.3B / 593.1B). |
| Active task | Structured CTA, not "ask Claude" | **2** — B08 types a copyable 3-step prompt ending in a table, with GOOD (sums shown · each change quoted, OPEN or BORROWED) and FLAG (reason with no quote · totals with no math). |
| Friction | Viewer must resolve a tension | **2** — B04 leaves "which number earns the name Small?" open with −59 % and −39 % on screen and ≥ 500 GB in the heading; the viewer holds it until the verdict's FRICTION line. |
| **Total** | | **12/12** |

### Production gate — PASS
- **Legibility at assertion — PASS (by timing contract).** Every claim beat carries a `legibility` field naming the
  artifact and when it is up. Checked against the pattern ramps: ReelFramework rows fully visible at 32/43/54/65 %,
  keep-note 76–94 %; BlipLadder bars 11–65 %, ref line 62–76 %, exception 80–94 %; ReelExecSummary cards 44–81 %.
  No voiced number depends on an element that appears after it is spoken (B03 31.9M in bar 1's sub; B04 500 GB in
  the heading; B05/B06 rows in voiced order). To confirm on rendered frames in PROOF-2.
- **Sources on screen — PASS.** Every beat with a number has `source` / `receipt` / `sourceNote`; computed figures
  say "computed" and name assumptions; B00's lines are dated and the running line names both posts and configs.
- **Side-by-side — PASS.** B02 (66 × 6,144 → 48 × 4,608 etc., per row), B04 (−59 % vs −39 %, with Inkling's 100 %),
  B05 (lab quote with config and computed range), B06 (config key vs lab silence vs paper) — all on screen together
  for ≥ 5 s.

### Facts (re-verified 2026-11-25, primary sources fetched fresh)
| Claim on screen | Source checked |
|---|---|
| 66 × 6,144 → 48 × 4,608; window 512 → 1,024; 256+2 shared, 6 active → 384, 8, 0 shared; expert width 2,304 | both `config.json` (`text_config`) |
| 4-layer hMLP, 40px patches; dMel `audio_config` → 23-layer ViT, hidden 1,024, mlp_ratio 4, 20px patches, merge 2; no `audio_config` | both `config.json` |
| `n_layers_per_attn_res_block: 6` (new) | Inkling-2-Small `config.json`; absent from Inkling's |
| 594B / 17B; 292M encoder "based on Perception Encoder", 20×20 patches, 2×2 pooling; "does not support audio"; Nov 5 (weights Nov 12) | thinkingmachines.ai/news/inkling-2-small |
| 975B / 41B; "encoder-free architecture for audio and vision"; Jul 15 2026 | thinkingmachines.ai/news/introducing-inkling |
| NVFP4 checkpoint needs ≥ 500 GB aggregated VRAM; no mention of attention residuals | HF model card (Inkling-2-Small README) |
| Block AttnRes; fixed unit-weight sum replaced by attention; evidence on Kimi Linear 48B / 3B | arXiv:2603.15031 abstract |
| 17.3B active, ≈ 594.1B total, 291.7–292.9M encoder, −59 % / −39 %, 2.9 % / 4.2 % | computed (`agentD_sheets.py` docstring has the arithmetic) |

Dropped from the draft (not needed, or not verifiable as worded): the KV-cache ladder, the Artificial Analysis
index score, the alignment caveats, and "training data: not released" (the card describes the data; it doesn't say
"not released" in those words).
