# SOURCES — From The Model To The Bill

Primary source: **the author's own blog post** on the LLM lifecycle, supplied in
full at build time (2026-08-13). The post credits **Andrej Karpathy's deep dive
into LLMs** as the material it is compressed from; the reel credits Karpathy
aloud at B09.

**Part 2 of 2.** Part 1 (`weekly_updates/08-14(2)/`) adapted the build half —
pre-training, tokenization, attention, post-training, RL and the failure modes.
This reel adapts everything the post says *after* that. Between them the post is
fully covered.

---

## Figures on screen (all from the post)

| Figure | Beat | Note |
|---|---|---|
| 7B model = **28 GB** at 32-bit | B02, B07 | axis item FP32 |
| **14 GB** at half precision | B02, B07 | "half precision halves it" |
| **7 GB** at INT8 | B02, B07 | integer + scale factor |
| **3.5 GB** at INT4 | B02, B07 | the `hot` item, inside the band |
| error per value **~1e-7 → ~1e-1** | B02 `slideMeta`, B07 | growth across the ladder |
| `(x_max − x_min) / (q_max − q_min)` | B03 | the asymmetric scale |
| `W′ = W + BA`, B is d×r, A is r×k | B04 | drawn, not just stated |
| **6** trainable instead of **9** (3×3, rank 1) | B04, B07 | *derived* by the component |
| QLoRA = adapters on a frozen **4-bit** base | B04, B07 | one consumer GPU |
| output tokens cost several × input | B06 narration | and dominate latency |
| naive N-step loop ≈ **quadratic** | B06 caption | agentic/retrieval systems |

---

## Named in the post, deliberately absent from this reel

**Simon Willison's year-in-review posts (2023, 2024, 2025)**, the **arena
leaderboard**, and **smol news** — the post's "where I check what changed this
week" pointers. They are omitted on purpose: they date fast, and a dated link on
screen ages the reel badly. **1-bit models** ("claim a Pareto improvement rather
than a trade") are also omitted — the claim is live enough that stating it flatly
in a 12-second beat would overstate it.

No URL is shown on screen or read aloud anywhere in this reel.

---

## Honesty log

**The one derived-not-asserted number.** `LlmLoraFactorization` computes both
parameter counts from the `d`, `k`, `r` it draws with (`full = d*k`,
`lora = d*r + r*k`). So the "9 trainable / 6 trainable" rows are guaranteed to
match the matrices above them. The component header forbids adding an override
prop. This is the same discipline part 1 used for its schematic attention bars,
applied the other way round: there, the fix was to render no numbers; here, the
fix is to render numbers that cannot be wrong.

**A claim deliberately kept narrow.** B02's shaded band reads "4-bit — one
consumer GPU" and spans 1–4 GB. The blog's consumer-GPU claim is specifically
about QLoRA on a frozen 4-bit base; it says nothing about INT8 fitting a
consumer card. The band therefore excludes the 7 GB INT8 item, even though a
wider band would look tidier.

**An example labelled as an example.** B04 shows the blog's 3×3 rank-1 case,
where LoRA trains 6 numbers instead of 9 — a saving of a third, which badly
understates the real effect. The beat's caption says so outright: "At real scale
the ratio is orders of magnitude, not nine to six."

**Where the reel paraphrases rather than quotes.** The post says reasoning effort
"is usually misread as a model switch when it is really a budget"; the reel says
"misread as a model switch. It is really a budget — the same model, given more
room." The post's list of what the budget buys ("decompose the problem, try
approaches, check itself and verify") is on screen at B01 as four chips, in the
post's own order.

**No spend.** Free and local at every step: Kokoro `am_onyx`, no API keys, no
paid service. Same as part 1.
