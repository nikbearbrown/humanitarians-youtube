# Why Jev Is Fast
### (And What "Faster Than an LLM" Actually Means Here)

*claude-hai · Simba · target ~4:20 · 16:9 · no sprint report — general topic, vendor-claim caveats throughout*

---

**[B00 — INTRO]** *(pattern: `ClaudeComposerAsk`)*
> Hi, I am Simba. A company called TypeSafe AI just shipped a model that answers in seventy to five hundred milliseconds — where a frontier language model doing the same decision takes three to over three hundred seconds. That's not a faster version of an LLM. It's a different kind of model, built to skip the part that makes LLMs slow in the first place.

**[B01 — SUMMARY]** *(pattern: `ClaudeStatement`)*
> Jev isn't competing with ChatGPT on writing essays. It's built for one job: turning messy input into a typed, structured decision — a choice, a score, a yes-or-no — with a confidence number attached. That narrower job is exactly what makes the speed possible.

**[B02 — STRUCTURE]** *(pattern: `AutoregressiveLoop` — reused as-is, no new component)*
> Every general-purpose LLM you've used decodes one token at a time. The last token and its cached context go in, one forward pass runs, the next token comes out — then that gets appended to the cache and the whole thing repeats. That's autoregressive decoding: inherently sequential, one step per token, however many tokens the answer needs.
>
> **props:** `kicker: "HOW A GENERAL LLM DECODES"`, `stepIn: "last token + KV cache in"`, `stepPass: "one forward pass"`, `stepOut: "next token out"`, `repeatLabel: "append to cache → repeat, one token at a time"`, `cacheLabel: "KV cache"`, `cacheBlocks: 5`, `sparkLine: "One step per token. However many tokens the answer needs."`

**[B03 — STRUCTURE]** *(pattern: `ParallelPass` — reused as-is, no new component)*
> Jev doesn't do that. It's non-autoregressive: the whole input goes in, one forward pass runs, and the entire typed answer comes out at once — because the answer isn't open-ended prose, it's one of a small, predefined set of shapes.
>
> **props:** `kicker: "HOW JEV DECODES"`, `tokens: ["input", "context", "goes", "in", "at", "once"]`, `passLabel: "one forward pass"`, `outputs: [{label:"Choice", detail:"approve / deny"}, {label:"Score", detail:"0.0–1.0, confidence-scored"}, {label:"Noul", detail:"yes / no"}]`, `sparkLine: "One pass. The whole typed answer, at once."`

**[B04 — REASONING]** *(pattern: `GuardCards` — reused as-is, no new component)*
> Three things make that possible. The output schema is fixed ahead of time — so there's no token-by-token uncertainty about what comes next. The training method is different too: Reinforcement Learning for Calibrated Decisions, tuned to produce a confidence-scored typed value, not fluent prose. And because the answer space is closed, the company claims the model can't produce a type error — by construction, not by a validator catching it after the fact. That third one is a company claim, not an independently verified one — worth flagging now, because it's about to matter.
>
> **props:** `kicker: "THREE THINGS ENABLING THAT"`, `cards: [{label:"Fixed output schema", detail:"Choice, Score, or Noul — decided before generation, not discovered token by token", ok:true}, {label:"RLCD training", detail:"Reinforcement Learning for Calibrated Decisions — tuned for a confidence-scored typed value, not prose", ok:true}, {label:"Closed answer space", detail:"company claims: can't produce a type error, by construction — not independently verified", ok:false}]`

**[B05 — RESULTS]** *(pattern: `DataTable`)*
> Here are TypeSafe's own published numbers, from their homepage, on their own example task: zero-point-one-one-four seconds versus eight-point-five-six-six seconds. Zero-point-zero-zero-zero-zero-eight-one dollars versus zero-point-zero-one-three-eight-eight dollars. That's where the headline figures come from — a hundred ninety-three times faster, four hundred forty-five times cheaper.

**[B06 — REASONING]** *(pattern: `FactStack`)*
> Here's the caveat, and it's TypeSafe's own words, not mine: their technical notes were written by their own model-capabilities team, and the company says the reported gains likely represent "the high end of real-world results." No published architecture. No released weights. No independent technical paper. Outside observers have guessed it might build on an existing open-weight model underneath — unverified, but worth knowing that's the state of the evidence.

**[B07 — FINDINGS]** *(pattern: `FindingPair`)*
> And even a sympathetic tech reporter covering the launch — Tom's Hardware — stopped short of endorsing the numbers. Their own line: "only practical use will tell." That's not dismissal. It's the normal amount of caution you'd want for any single-vendor benchmark on the vendor's own example task.

**[B08 — FINDINGS]** *(pattern: `FindingPair`)*
> The same coverage made the more important point: this is a category comparison, not an apples-to-apples one. Jev does structured decisions. Open-ended tasks — write me an email, summarize this document, have a conversation — are still an LLM's job. Comparing Jev's speed to a general model's speed on Jev's task type isn't quite the same as asking which one is "faster" in general.

**[B09 — SUMMARY / VERDICT]** *(pattern: `ClaudeVerdictArtifact`)*
> So: the mechanism is real and well understood — skip the autoregressive loop entirely by closing the answer space, and you remove the thing that makes LLM decoding slow. That part isn't a vendor claim, it's just how non-autoregressive generation works. The magnitude — a hundred ninety-three times, four hundred forty-five times — is TypeSafe's own number, on TypeSafe's own task, without independent verification yet.

**[B10 — NEXT STEPS]** *(pattern: `ClaudeComposerAsk`)*
> Your turn. If the thing you're building is closer to "pick one of these three options" than "write me something new," that's the category where a model like this is built to win — worth testing against your own workload before trusting anyone's benchmark, including TypeSafe's.

**[B11 — OUTRO]** *(pattern: `ClaudeTitleOutro`)*
> Why Jev is fast. Simba, for Humanitarians AI.

---
## Sources
- [TypeSafe AI — Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) (company blog; published numbers, architecture description)
- [TypeSafe AI homepage](https://typesafe.ai/) (headline performance claims: 193.6× faster, 444.6× cheaper, on the company's own example task)
- [Tom's Hardware — TypeSafe AI's Jev offers an alternative to LLMs that claims to be 193x faster and 445x cheaper](https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making) (independent coverage; author's skepticism and category-comparison caveat)
- Wikipedia — Jev (AI model) (company background, funding, and the company's own acknowledgment that its published gains represent "the high end of real-world results," with no published architecture, weights, or technical paper)

## Build notes
- **GATE L — resolved this pass**: searched `/home/claude/tk/runtime/remotion/src/scenes/` before deciding B02–B04. All three diagram beats reuse existing components as-is — nothing new authored:
  - **B02** — `AutoregressiveLoop`, the same component used in `hai-prefill-decode` for decode-step framing. Fits directly: step-in → one pass → step-out → repeat is exactly autoregressive decoding.
  - **B03** — `ParallelPass`, same component used in `hai-prefill-decode` for prefill framing, repurposed here for Jev's single-pass typed output instead of prefill's token batch. Legitimate reuse: both are "one forward pass, multiple outputs at once" shapes — the component doesn't assume prefill specifically.
  - **B04** — `GuardCards` (label/detail/ok per card), reused for the three enabling factors. The third card is deliberately set `ok:false` — a visual foreshadow that the "can't produce a type error" claim is company-stated, not independently verified, which B06–B08 then unpack. This is the one editorial choice in the diagram set: using the component's pass/fail visual language to flag a *sourcing* caveat, not a technical failure. Documented here so it isn't mistaken for a claim that the mechanism itself fails.
  - No component needed authoring. `AutoregressiveLoop` and `ParallelPass` were already built for `hai-prefill-decode`; `GuardCards` pre-existed independently.
- **Vendor-claim handling**: unchanged from prior draft — B05 states the company's own figures as company figures, B06–B08 are dedicated entirely to independent scrutiny (or the lack of it). Do not cut B06–B08 for time; they're load-bearing for accuracy, not padding.
- **Thematic note**: B02/B03 sit in the same visual language as `hai-prefill-decode`'s decode/prefill pair, but the argument is inverted — there, both diagrams describe one model's two phases; here, they contrast two different models' entire generation strategy. Worth a one-line callback if this and `hai-prefill-decode` ever get cross-referenced in an outro.
- No sprint report backs this one — general topic, same track as `hai-prefill-decode` and `hai-how-kv-cache-works`.
