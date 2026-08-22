# PEDAGOGY — From The Model To The Bill

**Reel:** `weekly_updates/08-20/` · slug `claude-sai-model-to-the-bill`
**Part 2 of 2.** Companion to `weekly_updates/08-14(2)/` ("From The Crawl To The
Conversation"), which covered the build half. This reel is the deployment half
that was deliberately dropped there to hold ~120s. Together they cover the whole
blog post.
**Target length:** ~120s. Narration totals **356 words**, which at this
channel's **measured** Kokoro `am_onyx` rate (176.7 wpm, taken from the built
part-1 master rather than estimated) projects to **~121s**.

**GATE P is UNSIGNED.** A human signs the line at the very bottom of this file
before any audio is generated. Claude must never sign it.

---

## The ONE idea

**Everything after training is a cost decision — memory, latency, dollars — and
the discipline is to buy capability only where it changes the answer.**

Part 1 asked *how does one get built*. This one asks *what does it cost to run*,
and answers it four times at four scales: per request (inference budget), per
GPU (precision), per fine-tune (adapters), per task (model choice). The closing
move is the same in all four: the cheap option is only cheap if it works.

---

## Act structure

| Beat | Act | Pattern | Carries | Words |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open — training vs running. "this is Sai." | 35 |
| B01 | INFERENCE | `LlmInferenceKnobs` **(new)** | Temperature is a position; effort is a budget | 40 |
| B02 | PRECISION | `ScaleComparison` | 28 → 14 → 7 → 3.5 GB on a log axis | 31 |
| B03 | QUANTIZATION | `BinaryBranch` | Symmetric vs asymmetric; after vs during | 37 |
| B04 | ADAPTERS | `LlmLoraFactorization` **(new)** | W′ = W + BA; 6 trainable instead of 9 | 34 |
| B05 | CHOOSING | `DivergentFates` | Cheapest sticker vs cheapest cost per success | 37 |
| B06 | LEVERS | `ClaudeScienceChipGrid` | Caching, caps, routing, batch; the quadratic | 38 |
| B07 | VERDICT | `ClaudeVerdictArtifact` | The deployment half on one page | 43 |
| B08 | HANDOFF | `ClaudeComposerAsk` | Price one task, two ways | 35 |
| B09 | OUTRO | `ClaudeTitleOutro` | Title restate + sign-off | 26 |

---

## ILLUSTRATE-LAW check

Body beats B01–B06 use, in order:

`LlmInferenceKnobs` → `ScaleComparison` → `BinaryBranch` →
`LlmLoraFactorization` → `DivergentFates` → `ClaudeScienceChipGrid`

Six distinct patterns; **no two consecutive body beats share one.** ✅
The Claude UI appears only at B00, B07, B08 and B09. ✅
Every body beat carries an ordered `show` block. ✅
**No pattern is reused from part 1's body**, so the two reels do not feel like
the same six slides with new words. ✅

**Two new templates** were written for this reel, in
`runtime/remotion/src/LlmDeployIllu.tsx`: `LlmInferenceKnobs` (a value moving
along a range, then a budget opening to reveal the work it buys) and
`LlmLoraFactorization` (a matrix equation where the shapes carry the argument).
Neither motion existed in the library.

---

## Evidence and honesty

**Every figure is the author's own, from the blog post.** Specifically: a 7B
model at 28 GB in 32-bit, 14 at half precision, 7 at INT8, 3.5 at INT4; error
per value growing from roughly 1e-7 to 1e-1; the asymmetric scale
`(x_max − x_min) / (q_max − q_min)`; `W′ = W + BA` with B of shape d×r and A of
r×k; the 3×3 rank-1 example giving 6 trainable numbers instead of 9; QLoRA as
adapters on a frozen 4-bit base putting 7B fine-tuning on one consumer GPU;
output tokens costing several times input tokens; a naive N-step agentic loop
growing roughly quadratically. **Nothing is invented.**

Three deliberate safeguards:

1. **B04's counts are DERIVED, not asserted.** `LlmLoraFactorization` computes
   `full = d*k` and `lora = d*r + r*k` from the same `d`, `k`, `r` it uses to
   draw the matrices, so the "9 trainable" and "6 trainable" figures on screen
   cannot disagree with the picture beside them. There is deliberately no prop
   to override them — do not add one.
2. **B02 uses a numeric pattern, which is allowed here because the numbers are
   real.** `ScaleComparison` is the one pattern the guide warns to use only with
   genuine figures; all four memory values are the author's. The shaded band is
   labelled **only** for the 4-bit case, because that is the only size the blog
   actually claims fits one consumer GPU — no claim is extended to INT8.
3. **B04's caption states the limit of its own example**: "At real scale the
   ratio is orders of magnitude, not nine to six." The 3×3 grid is the blog's
   teaching example, and the reel says so rather than letting 9→6 read as the
   real-world saving.

**Unverified:** no outbound URL is shown or read aloud. The blog's links
(Simon Willison's year-in-review posts, the arena leaderboard, smol news) were
not re-fetched. See `SOURCES.md`.

---

## Deliberate deviations — please confirm

1. **Attribution: hosted by Sai, not Liam-in-for-Bear.** Same standing override
   as every reel in this series since 2026-07-31. B00 says "this is Sai";
   B09 signs off "Sai." Voice is Kokoro `am_onyx`; handle `@HumanitariansAI`
   (org handle throughout — `@NikBearBrown` removed from B00/B08/B09 on
   2026-08-21 at the author's request).
2. **Title is Claude's proposal, not yours.** "From The Model To The Bill" was
   chosen to rhyme with part 1's "From The Crawl To The Conversation" and to
   name the through-line (cost). If you want a different one it is three props:
   `metadata.title`, B00's `segment`, B07's `artifactTitle`, B09's `title`.
3. **Scope: this reel finishes the blog.** Nothing from the post is now
   unadapted. The closing pointers (Willison, arena, smol news) are mentioned in
   `SOURCES.md` but not on screen — they date fast and would age the reel.

---

## Human review checklist

Before signing, read the `narration_text` of all ten beats end to end and check:

- [ ] It stands alone. A viewer who missed part 1 can still follow this.
- [ ] It does not merely repeat part 1's shape with new nouns.
- [ ] Every number is one you recognise from your own post.
- [ ] B02's band claim is narrow enough — 4-bit only, not INT8.
- [ ] B04's caption keeps the 9→6 example honest about its scale.
- [ ] Attribution is right: "this is Sai" at B00, "Sai." at B09.
- [ ] You are happy with the title (deviation 2).
- [ ] The B08 handoff prompt is one a viewer can actually paste and run.

---

*Signing this line unlocks audio generation. Claude must not fill it in.*

VERDICT: PASS    — reviewer: Sai Nikhil Kunapareddy  date: 08/13/2026