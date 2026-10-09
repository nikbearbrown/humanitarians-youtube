# SOURCES.md — claude-liam-context-window

## Factual Claims

| Beat | Claim | Source |
|---|---|---|
| B00 / B01 / B02 | Everything in the request counts toward the context window: system prompt, every message (incl. tool results, images, documents), tool definitions — **and the output Claude generates for the turn.** | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) — "Everything in the request counts toward the context window: the system prompt, every message in `messages`... and your tool definitions. The output Claude generates for the turn... counts too." |
| B00 / B05 | As token count grows, accuracy and recall can degrade — Anthropic calls this "context rot." More context is not automatically better. | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) — "As token count grows, accuracy and recall degrade, a phenomenon known as *context rot*... more context isn't automatically better." |
| B04 / B06 | What happens when a request would exceed the context window depends on the app / API surface: (1) the raw API can reject the request outright (400 `invalid_request_error`, "prompt is too long"), or on newer models stop generation with `stop_reason: "model_context_window_exceeded"`; (2) server-side **compaction** can automatically summarize earlier turns so the conversation continues past the limit; (3) chat interfaces such as claude.ai can manage the window on a rolling "first in, first out" basis — i.e., drop the oldest turns. | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) — "Context window overflow behavior" section (error behavior); "Manage context with compaction" section (summarization); footnote 1 on the standard-behavior diagram ("Chat interfaces such as claude.ai can also manage the context window on a rolling 'first in, first out' basis"). |
| B04 / B05 | The context window ceiling itself is fixed per model and does not grow mid-conversation. | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) — "Context window capacity: The context window (up to 1M tokens, depending on the model) holds the conversation history plus the new output Claude generates." |
| B05 | Filling more of a larger context window costs more to process than filling less of it (standard token-based pricing scales with tokens processed). | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) — long-context requests are billed at standard per-token pricing; no free-tier exemption for size. General inference from Anthropic's token-based pricing model, not a single verbatim quote. |
| B03 | A token is often a sub-word fragment, not a whole word (BPE-style tokenization). | Anthropic, [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) — describes the token-counting endpoint and notes the tokenizer changes between model families; general BPE tokenization behavior. |
| B03 | Code, numbers, jargon, and non-English text often use more tokens per word than plain English prose. | **Not sourced to an Anthropic doc.** This is general, well-established BPE-tokenizer behavior (confirmed via third-party tokenizer analyses, not Anthropic's own published docs). Flagged here per the DOUBLE-CHECK LAW rather than attributed to Anthropic — if a firmer Anthropic-sourced citation is wanted before recording, this line should be re-verified or softened further. |

## Corrections Applied (DOUBLE-CHECK LAW)

- Original B00/B04/B06 drafts asserted, as fact, that "the oldest turns are always silently dropped" when a context window fills. Corrected to reflect that behavior at the limit is **application-defined** (error / compaction-summary / rolling-FIFO drop), per the source above — no single mechanism is universal.
- Original B01/B02 omitted Claude's own reply from the list of things sharing the token budget. Corrected: the reply is explicitly called out as counting toward the window (see first row above), and added as a fifth `layers` entry in B02.
- Original B04 (`AttritionChain`) and B05 (`ScaleComparison`) props used invented specific percentages/scale values with no real-world backing. Both are now explicitly labeled `ILLUSTRATIVE` in the on-screen `slideMeta`/meta label, and B05's axis units are abstract (`×`) rather than a token count, so nothing on screen reads as a real measurement.

## Persona / Channel Change (rebrand)

Switched from `claude-liam` (Teardown, @NikBearBrown, Liam in for Bear, `am_onyx`) to
`claude-hai` (Plain, @HumanitariansAI, Liam in for Gomathy, `af_bella`).
No factual claims changed — only register, persona line, voice, and folder chip.

- **Voice conflict found and flagged, not silently resolved:** three in-repo sources
  disagree on the HAI voice — `CLAUDE.md`'s top-level tier table says Kokoro `af_bella`;
  `skills/make/hai/SKILL.md` (the standalone `hai` command) says `af_kore` under the
  persona name "Kore"; `brands/hai.md` and `skills/make/ai-explainer/SKILL.md`'s channel
  table both say `am_onyx`. Used `af_bella` per the user's explicit instruction (which
  matches CLAUDE.md). Worth reconciling in the toolkit's own docs.
- **Scope choice:** this is the lighter `claude-hai` CHANNEL variant on the existing
  ai-explainer/Claude-UI chassis (same `ClaudeComposerAsk` / `BrutalistHesitantWriter` /
  `ClaudeVerdictArtifact` / `ClaudeTitleOutro` patterns, `claude` palette) — not the
  standalone `hai` skill (`skills/make/hai/SKILL.md`), which would additionally require a
  new `hai-` directory, a CLI worked-exercise beat, a full humanitarians-palette reskin,
  and the `OutroSeries`/`OutroCTA` outro. Flagging in case the fuller treatment is wanted.
- **B08 outro — fixed.** Re-read `OUTRO-LOCK.md` in full: it explicitly scopes itself to
  "claude-liam / @NikBearBrown reels ONLY" and states other channels "have their OWN
  outros and NEVER get this card, handle, or mascot." So `ClaudeTitleOutro` was never a
  legal option for this channel, lock or no lock — switched to `OutroCTA`
  (`runtime/remotion/src/scenes/OutroCTA.tsx`), the component `skills/make/hai/SKILL.md`
  Step 5 names as the HAI-lane outro. It takes free-text `line` + `handle` props (no
  hardcoding), so `@NikBearBrown` cannot appear.
  - **Options considered:**
    (a) `OutroCTA` — chosen. Existing, on-doctrine, simplest.
    (b) `OutroSeries` — same family, same trade-off below; shape (eyebrow + tagline) fits
    a series sign-off better than a title-restate, so a worse structural match here.
    (c) Build a new generic Claude-skin outro variant (e.g. `ClaudeTitleOutroGeneric` with
    a `handle` prop) — would preserve visual continuity with B00–B07 but is new code in
    shared `runtime/remotion/src/`, out of scope for a pre-audio beat revision.
  - **Trade-off accepted:** `OutroCTA` renders on `VOX` tokens
    (`runtime/remotion/src/tokens/vox.ts`) — flat white `#FFFFFF` ground, near-black ink,
    one crimson accent — not the cream `#FAF9F5` / terracotta `claude` palette used
    everywhere else in this reel. So B08 is a deliberate one-beat palette break. It also
    displays a hardcoded "Subscribe" pill (baked into the component, not a prop) —
    cosmetic only.
  - **Doc note:** `skills/make/hai/SKILL.md` and `brands/hai.md` describe this outro as
    rendering "in the humanitarians palette" (`tokens/humanitarians.ts` — cream `#F3EBDD`,
    teal `#1F4E5F`, etc.). The actual component imports `VOX` tokens instead, which are a
    different, plainer white/ink/crimson set. Another doc-vs-code mismatch found in this
    build, alongside the voice conflict above.
- Word-budget rule from `ai-explainer/SKILL.md` applied: the HAI persona's greeting cue
  is restricted to the shortest forms (Hi · Ola · Hej · Ciao). Changed B00's greeting
  from "Namaste, Liam" to "Hi, Liam" accordingly.
- **Narrator renamed Liam → Bella.** The voice actually speaking is Kokoro `af_bella`, so
  the on-screen/spoken self-identification now names the voice it matches: "this is
  Bella, in for Gomathy" (B00), "Bella, in for Gomathy" (B08 outro), greeting "Hi, Bella".
  `Liam` was Bear's documented substitute-narrator name for `am_onyx`
  (`ai-explainer/SKILL.md`'s IN-FOR-BEAR LAW) — using it over an `af_bella` reading never
  matched the voice. "Bella" as an on-screen persona name isn't itself a documented house
  persona (unlike Liam/Bear/HAI/Medhavy/Musinique); it's a personalization for this
  individual reel, chosen by the user.
