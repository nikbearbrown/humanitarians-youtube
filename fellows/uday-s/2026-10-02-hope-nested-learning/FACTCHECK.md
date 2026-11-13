# FACTCHECK — Levels, Not Layers

Status: **GATE F SIGNED — 2026-10-02. 14 rows PASS, 1 row CORRECTED-AT-SOURCE.**

Subject: Behrouz, Razaviyayn, Zhong, Mirrokni, *"Nested Learning: The Illusion
of Deep Learning Architectures"*, **NeurIPS 2025** (arXiv 2512.24695), plus
Google Research's announcement post.

## The brief, checked

The reel was commissioned as **"Hope training by Google"**. One correction, made
on screen in B01 rather than silently:

| Brief implies | Verdict | What the reel says |
|---|---|---|
| HOPE is a *training* method | ❌ **NOT WHAT IT IS** | HOPE is an **architecture** — a self-modifying variant of Titans with a continuum memory system. It is trained by ordinary pre-training. The genuinely new thing is the Nested Learning *view* — that architecture and optimiser are the same kind of object at different update rates — and the design axis that follows from it. B01 states this as the first substantive beat. |

Everything else in the topic survives and is built on.

## How the figures were obtained

The Google Research blog shows the headline results **as charts with no numbers
in the text**, so the blog cannot source a figure. The paper PDF was fetched and
its text extracted with `pdftotext` (no layout mangling in reading order), and
every figure below was read from the table rows directly.

**One web summary was discarded.** A search result stated HOPE scored *15.11*
WikiText / *11.63* LAMBADA at 1.3B against Titans at *15.60 / 11.41*. The paper's
Table 2 says HOPE is **14.39 / 10.08** and Titans is 15.60 / 11.41 — the summary
had misread Titans' row as HOPE's and invented the rest. 15.11 does not appear in
the table. The reel uses the paper.

## Verified figures used on screen

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B01 | HOPE is a self-modifying architecture, a variant of Titans | ✓ PASS | paper, §8; Google Research post |
| 2 | B01 | the paper's thesis is that stacking depth hides the real axis | ✓ PASS | the title itself, and §1 |
| 3 | B03 | a transformer has two memory regimes: weights (fixed after training) and the attention window | ✓ PASS | paper §1, the "two extreme frequencies" framing |
| 4 | B03 | CMS is a spectrum of memory blocks, each updating at its own frequency | ✓ PASS | paper §7, Continuum Memory System |
| 5 | B03 | the paper's worked CMS example uses 4 levels of MLP blocks | ✓ PASS | paper §7, cost analysis of Hope-Attention |
| 6 | B04 | WikiText ppl at 1.3B/100B: Hope 14.39, Titans 15.60, Transformer++ 17.92 | ✓ PASS | Table 2, read in reading order |
| 7 | B04 | LAMBADA acc at 1.3B/100B: Hope 51.0, Titans 49.1, Transformer++ 42.6 | ✓ PASS | Table 2 |
| 8 | B05 | ablation — Hope 12.24 avg ppl / 58.1 acc; without CMS 13.04 / 57.3 | ✓ PASS | Table 6 |
| 9 | B06 | S-NIAH-3 at 16K: Hope 24.8, Titans 21.2, RWKV-7 5.8, DLA 4.0 | ✓ PASS | Table 1 |
| 10 | B06 | a plain Transformer scores 40.8 on the same test | ✓ PASS | Table 1, same row block |
| 11 | B06 | the paper scopes its win to attention-free models | ✓ PASS | §9.2, quoted on screen |
| 12 | B07 | CTNL: two languages learned in sequence; ICL drops dramatically | ✓ PASS | §9.1 — "ICL faces dramatic performance drop" |
| 13 | B07 | adding memory levels improves it; Hope-3 almost recovers the no-forgetting score | ✓ PASS | §9.1, verbatim claim |
| 14 | B08 | the authors write that catastrophic forgetting is **not** solved in general, and call NL a roadmap rather than a destination | ✓ PASS | conclusion, p.40 |

## The one visual that is schematic, and is labelled as such

**B07's bars carry no numbers.** The paper reports CTNL as a two-axis ChRF
scatter (Manchu→English against Kalamang→English), not one score per model, so
there is no single figure to put on a bar. The beat shows the **ordering** the
paper states in prose — ICL collapses, Hope-1 < Hope-2 < Hope-3, Hope-3 nearly
at the no-forgetting baseline — and says so on screen: *"ordering as reported —
axis not to scale."* No number is asserted.

## Precision notes

- **B04 and B05 perplexities are not the same quantity.** Table 2 reports
  WikiText perplexity; Table 6's 12.24 is an *average* over the language-modeling
  tasks. The citation strip in B05 states this, so the two beats cannot be read
  as one declining series.
- **Only the 1.3B row is used.** At 760M, HOPE also leads on perplexity but
  Samba edges it on LAMBADA accuracy (39.2 vs 38.8). The reel does not use the
  760M row at all rather than cherry-pick within it.
- **The `Avg.` column of Table 2 was not used.** Its cells did not survive text
  extraction in a row-attributable way, so no average accuracy is claimed. Only
  columns that were unambiguously row-aligned (Wiki ppl, LMB ppl, LMB acc) appear.
- **No qubit-style cross-vendor comparison of model sizes.** All B04 figures come
  from the same row block — same parameter count, same token budget.
- **"Hope-Attention beats the Transformer" is true but not shown.** At S-NIAH-3
  16K the CMS-augmented attention model scores 42.4 against the Transformer's
  40.8. It is left out because B06 is already carrying the reel's hardest turn
  and the extra bar would soften it; it is recorded here so the omission is
  visible.

## Claims deliberately NOT made

- **No claim that HOPE solves catastrophic forgetting.** The verdict beat says
  the opposite, in the authors' words.
- **No claim that HOPE is state of the art generally.** Its demonstrated win is
  within the attention-free family, which is what B06 is about.
- **No claim about products, deployment, or any Google model.** HOPE is research;
  nothing here says it ships in anything.
- **No training-cost, speed or efficiency claim.** The paper's optimiser results
  (M3, ViT on ImageNet-21K) are real but out of scope, and the reel does not
  gesture at them.
- **No claim that in-context learning is broken.** B07's ICL collapse is scoped
  to one sequential-learning task.
