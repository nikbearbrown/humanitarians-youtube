# PROMPTS — The Bottleneck Moved.

Every prompt this reel shows on screen or used to make a visual, verbatim. Part of the
GATE F paperwork set (`FACTCHECK.md` · `SHOTLIST.md` · `PROMPTS.md`).

Note on honesty: the three composer beats show prompts a viewer could genuinely paste into
Claude. None is a mock-up written to look good on screen — that would be a DOUBLE-CHECK LAW
violation dressed as design.

---

## B00 — cold open (ASK, shown on screen)

**Greeting:** `Merhaba, Liam` · **runningText:** `separating the two costs…`

> My team adopted AI across marketing this year. Output is up roughly 5x and reach is flat.
> Separate the costs for me: which parts of marketing did AI actually make cheaper, which
> parts did it leave exactly where they were, and which part are we now over-investing in
> because it got cheap?

**Result lines shown (the ask lands answered — COLD OPEN LAW):**

1. `cheaper: producing the asset — drafts, variants, images`
2. `unchanged: earning the attention, earning the trust`
3. `you scaled the step that was already free`

The "5x / flat" figures belong to this fictional asker and are the premise of the question,
not a claim the narrator makes about the market. Logged as claim #1 in `FACTCHECK.md`.

---

## B03 — the ask micro-beat of the one ASK→RESULT pair (shown on screen)

**runningText:** `drawing the funnel…` · **Result:** B04 (`BnkFunnel`)

> Draw the attention funnel a single marketing asset passes through after it is published —
> published, seen, read, remembered, acted on. Label the stages honestly as an ordinal shape,
> not measured data, and mark which stages a faster writing tool changes.

ASK→RESULT LAW: this is the actual prompt behind the next beat's graphic, not decoration.
The instruction to label the shape as ordinal is in the prompt itself — the honesty
constraint is visible to the viewer, not just applied behind their back.

---

## B08 — the handoff (shown on screen, READ ALOUD VERBATIM)

**Greeting:** `Your turn.` · **runningText:** `paste this into Claude…`

> Here are my last 20 marketing assets. For each one, tell me which cost it was buying down —
> production, distribution, or trust. Then show me where my hours actually went, and name the
> one asset that would have performed better if I'd spent double the time on half the output.

**The rubric shown beneath it (HANDOFF LAW — a scaffolded task, not "ask Claude about X"):**

1. `grade it: does it sort EVERY asset?`
2. `grade it: does it disagree with you anywhere?`
3. `grade it: does it name hours you can't account for?`

Plus the spoken failure signal: *"If it agrees with everything, you gave it too little to
work with."* The narration reads the prompt aloud word for word, then spends two lines
discussing how to judge the answer — a handoff where the prompt only appears on screen is a
defect.

---

## Generation prompts — the five illustration beats

These beats are **not** generated media. They are deterministic renders of committed scene
source, so there is no image/video prompt to log. What follows is the authoring intent each
composition was built to satisfy — recorded so a later rebuild can check itself against the
original brief rather than guessing from the rendered frame.

| Beat | Composition | Pattern | Authoring intent |
|---|---|---|---|
| B01 | `BnkSplit` | divergence | One node ("the cost of a marketing asset") splits at "AI arrives" into two tracks that visibly diverge — production diving to near zero in ink, worth-reading holding dead flat in terracotta. The BLUF *is* a split, so the pattern must enact the split, not label it. |
| B02 | `BnkCosts` | scale | Three ordinal bars — produce ≪ distribute ≪ be believed — growing to rank as each is named, with the band bracketing ONLY the cheap one. Axis must read "ORDINAL RANKING, not a measurement" on screen. |
| B04 | `BnkFunnel` | attrition | The post-publish chain, each stage narrower, lighting in narration order; then the top doubles while the tail visibly does not move. `slideMeta` must read "ORDINAL SHAPE ONLY · illustrative, not measured data". |
| B05 | `BnkCutoff` | threshold | A cutoff on a volume axis: below it "more output buys reach" resolves YES; above it "more output costs trust" resolves NO. The falsifier caption is the point of the beat, not a footnote. |
| B06 | `BnkBranch` | branch | Two branches off "20 hours a week freed", with B02's cost bars ghosted behind each so the example visibly USES the framework. Resolver: "buy down the cost that did NOT fall". |

All five carry the `@NikBearBrown` corner bug (LOGO LAW) via the shared `Stage` wrapper in
`runtime/remotion/src/scenes/BottleneckMoved.tsx`.

## Build prompt

The single paste-ready prompt that builds this reel end to end lives in `BUILD-PROMPT.md`.
