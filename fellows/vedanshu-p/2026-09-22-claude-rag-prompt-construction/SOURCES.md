# SOURCES — claude-rag-prompt-construction

*"Labels Are Not Decoration." · RAG Foundations, Chapter 8 — Prompt Construction
and Context Injection*
*DOUBLE-CHECK LAW record.*

---

## Primary source

| Field | Value |
|---|---|
| Book | *RAG Foundations* — Vedanshu Daxesh Patel |
| Repo | `D:\ai1-cli-main` |
| Chapter | `chapters/08-prompt-construction.md` |
| Fact-check record | `chapters/08-prompt-construction.md.verified.json` — `verified: true`, `verified_by: Vedanshu Daxesh Patel`, `verified_at: 2026-08-13`, GATE 4, 0 discrepancies |

Folder dated **2026-09-22** per explicit instruction — independent of the
chapter's own fact-check date and of the session's calendar date.

## Claims, and how the reel treats each

| Claim | Basis | Verdict |
|---|---|---|
| A RAG prompt has three distinguishable parts: instructions, retrieved context, the question | Ch. 8 §"The augmented prompt's anatomy" | Framed as the chapter's anatomy; drawn in B02 |
| Structuring a prompt explicitly — labelled sections — reduces the chance the model misreads which part is which | Anthropic, Claude Platform Docs, "Prompting Best Practices" | Cited on B02; attributed to the vendor docs, not to research |
| Each retrieved chunk benefits from its own wrapper tagged with its source, so claims can be attributed | Anthropic, Claude Platform Docs | Cited on B02 and enacted in B07 |
| Models use information at the beginning or end of a long context more reliably than information in the middle; holds even for long-context models | Liu et al. (2023; published 2024), TACL 12:157–173 | **Drawn as shape only** — see the honesty note below |
| Place long retrieved documents near the top, before instructions and the question | Anthropic's own internal testing | **Explicitly marked unsettled** — B04 exists for this |
| A grounding instruction helps the model stay on the retrieved material | Anthropic, Claude Platform Docs | Cited on B05 |
| Grounding instructions reduce the risk of an unsupported answer; they do not eliminate it | Ch. 8 §"Grounding instructions" | Carried in B05's warning line and the BVDT verdict |
| An answer can open grounded and then drift into ungrounded elaboration — a particularly deceptive failure | Ch. 8 | **Enacted** in B05: two sentences, one anchor |

## The honesty decisions

### 1. B03 draws no numbers, on purpose

REBUILD LAW permits exact data when the source publishes it, and
"orderings/anchors only" when it does not. Chapter 8 reports the *direction* of
the Lost-in-the-Middle effect — best at the beginning or end, "noticeably worse"
in the middle — and publishes no per-position figures.

So `LostMiddleCurve` draws the ordering and the U-shape with the accuracy axis
**deliberately unlabelled**. Plausible-looking percentages would have been the
single easiest way to turn a real, well-documented finding into a fabricated
one, and they would have been invisible to a viewer. The component's docstring
records this so a later editor does not "improve" it by adding numbers.

### 2. B04 exists because the chapter refused to simplify

Chapter 8 does something most write-ups of this material do not: it states the
position effect as established, then explicitly declines to promote the ordering
rule that follows from it, because that recommendation "comes from one vendor's
internal tests, not an independently reproduced research result," and "the field
has not fully converged on one universal ordering rule."

Flattening both into a single "best practices" list would have been the easiest
edit available and the most misleading. `EvidenceTiers` draws them as two
visibly unequal tiers instead — a **solid** bar for the peer-reviewed finding, a
**hollow dashed** track for the vendor guidance.

The tentative tier is drawn hollow rather than terracotta. Being unsettled is
not an error, and colouring it like a warning would overstate the chapter's own
position — the chapter calls it "a reasonable default."

### 3. B05 keeps both sentences equally confident

The ungrounded sentence is **not** greyed out, struck through, or marked in the
prose itself. Same serif, same size, same weight as the grounded one. The only
visible difference is that one draws an anchor to a source chunk and the other
has nothing to draw.

This is the chapter's actual point: the failure is deceptive *because* the
accurate opening lends the rest an appearance of reliability. A figure that
visually flagged the drift would have shown a problem that does not look like
that in practice.

### 4. The worked example is the chapter's own

The resignation question, the resignation-policy chunk, and the HR-contacts
chunk that "happened to also mention notice" are all the chapter's. Nothing was
substituted for a more dramatic example. The answer shown in B07 —
"Two weeks' written notice." — is a plausible completion of the chapter's
scenario and is presented as the *worked example's* answer, not as a measured
system output; this reel runs no code.

### 5. Nothing version-dated

No model version numbers, no drifting counts, no benchmark figures.

## Sources cited on screen

| # | Source | Used in |
|---|---|---|
| 1 | Anthropic. *Prompting Best Practices* (Claude Platform Docs) — "Structure prompts with XML tags", "Long context prompting" | B02, B05, B07 citations |
| 2 | Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023; 2024). *Lost in the Middle: How Language Models Use Long Contexts.* TACL 12, 157–173 | B03, B04 citations |

Es et al. (*RAGAS*, 2023/2024) is in the chapter's reference list but is not
drawn on by any claim this reel makes, so it is not cited on screen.

## Figures

| Source figure | Treatment |
|---|---|
| `images/prompt-construction-fig-01.png` — an unstructured wall of text beside the same content in labelled INSTRUCTIONS / CONTEXT / QUESTION sections, each chunk tagged | **Rebuilt natively** as B02 (`PromptTwoLayouts`). REBUILD LAW — never embedded |
| `images/prompt-construction-fig-02.png` — the annotated well-assembled prompt, with callouts to the instruction block, the tagged chunks and the question | **Rebuilt natively** as B07 (`AnnotatedPrompt`), with one addition the still cannot make: the *resolution*. Both chunks stay equally plausible until late, then the relevant one lights and the near-miss recedes |

The source figures are drawn in the book's red; both rebuilds are in the Claude
fidelity palette (cream `#F0EFE6`, warm ink `#3D3929`, terracotta `#D97757`) per
CLAUDE-BRAND.md. Logged as the required retint decision.

## Components

New this reel (GATE L: six searches, every one a genuine miss):

| Composition | Beat | 9:16 twin |
|---|---|---|
| `PromptTwoLayouts` | B02 | `PromptTwoLayouts916` |
| `LostMiddleCurve` | B03 | `LostMiddleCurve916` |
| `EvidenceTiers` | B04 | `EvidenceTiers916` |
| `GroundingDrift` | B05 | `GroundingDrift916` |
| `AnnotatedPrompt` | B07 | `AnnotatedPrompt916` |

Closest leads, all **rejected on inspection** (a hit is a lead, not a verdict):
`ChunkSizeTradeoff` (13.0) and `ChunkOverlapGuard` — Chapter 4's components,
whose props are hardcoded to chunking arguments (`axisLeft`/`leftFailTitle`,
`factText`/`severedNote`); `BrandB01AlignmentDrift` (5.5) and
`AlgArtQualityDial` (4.0) — both expose only `sparkLine`, with their content
fixed to their own reels. Opening the files settled each one.

All five sit on the existing `EmbedChrome` `FigureFrame` and reuse
`ChunkChrome`'s `useBeatClock`, so Chapters 3–8 share one chrome and one clock.

Reused unmodified (props only): `ClaudeComposerAsk` (B00, BHTF),
`BrutalistHesitantWriter` (B01), `ProblemPredictCard` (B06),
`ClaudeVerdictArtifact` (BVDT), `TitleOutroChannel` (BOUT).

## Two deliberate deviations from ai-explainer doctrine

Both are consistent with the fourteen sibling reels in this series and are
recorded here rather than passed silently.

1. **OUTRO LAW → `TitleOutroChannel`, not `ClaudeTitleOutro`.** `OUTRO-LOCK.md`
   §Scope restricts the locked card to `claude-liam-*` slugs. It hardcodes
   `@NikBearBrown` and renders no subline, so using it would stamp the wrong
   channel on the card and **drop the author signature**, which is an explicit
   requirement of this build. `compile.py` emits a skin lint for this; the lint
   is the thing that is wrong here.
2. **LOGO LAW — no corner brand bug on the figure beats.** The shared
   `EmbedChrome` `FigureFrame` carries no logo slot, and it is the chrome every
   reel from Chapter 3 onward renders through. Adding a bug would retroactively
   alter already-shipped siblings. Channel identity is carried instead by the
   `@VedanshuDaxeshPatel` footer chip on the composer beats and full-size on the
   outro card. Flagged as a real deviation, not a silent one.

## VOX LAW — zero pantry stills, and that is the correct number

This reel uses **no photographic stills**, and none were fetched. VOX LAW holds
that a still is evidence, never texture. Chapter 8's evidence is entirely
prompts, layouts, and one research finding about position — there is no beat
whose evidence is an image, so a pantry still could only be decoration.

Both source figures were rebuilt natively rather than embedded (REBUILD LAW), so
no image file enters the render at all. Consistent with the Ch. 4 ai-explainer,
which reached the same conclusion for the same reason.

## Determinism

Every beat is a pure function of its frame — no `Math.random` at render.
`BrutalistHesitantWriter` is seeded (`claude-rag-prompt-construction-b01`), so
the typing performance is identical on every render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API, no network call.
