# FACTCHECK — agent-memory

Every claim the narration makes, and what backs it. Written before rendering.

This is a **mechanism explainer**. Every claim is about how agent memory is built,
not about any product, benchmark or result. Plain register permits **exactly one**
flagged inference; it is at B07 and is spoken aloud: *"One flag: which pieces count
as relevant is a guess your retrieval makes, not a fact."*

| Beat | Claim | Status | Basis |
|---|---|---|---|
| B00 | Whether an assistant recalls something depends on what was built around the model, not on model intelligence | VERIFIED | Follows from statelessness plus the retrieve-into-context pattern; established below |
| B01 | An agent does not remember; memory is engineered | VERIFIED | Definitional — a text-generation model has no persistence between calls |
| B02 | The coffee-order scenario | CONSTRUCTED EXAMPLE | A hypothetical posed as a prediction prompt; not attributed to any product |
| B03 | Each model call is stateless; the whole conversation is re-sent every turn | VERIFIED | The published chat-completion contract: the caller supplies the full `messages` list on every request |
| B03 | The model keeps nothing between calls; the client keeps the list | VERIFIED | Same contract — persistence lives in the caller, not the model |
| B04 | "Agent memory" means short-term (in-request conversation) or long-term (an external store) layered on a model with none | VERIFIED | The standard framing across agent frameworks; stated as a taxonomy, not a product claim |
| B05 | Turns are appended and re-sent, so the request grows, and the context window is a hard ceiling | VERIFIED | Direct consequence of the same contract plus the documented existence of a finite context limit |
| B05 | When the window fills, the oldest turns are usually dropped | VERIFIED as the common strategy | Truncation/sliding-window is the ordinary handling; narration says "usually", which is accurate rather than hedging |
| B07 | Long-term memory is a store outside the model — notes, a database, a vector store — written to and searched | VERIFIED | The retrieval-augmented pattern as ordinarily implemented |
| B07 | Retrieved text is pasted into the conversation before the model call | VERIFIED | This is what "retrieve into context" means; nothing is written into the model |
| B07 | What counts as "relevant" is a guess the retrieval makes | **INFERENCE — FLAGGED ALOUD** | The one permitted flag. Relevance is a scoring decision, not ground truth |
| B08 | Save and retrieve are two ordinary calls around the model call | VERIFIED | Shown as illustrative code in the pattern's normal shape; no library or vendor named |
| B09 | Same model, same weights either way; only the save/retrieve code differs | VERIFIED | Follows from statelessness — the weights are identical per call |
| B10 | A remembered fact proves retrieval worked, not that the model understands | VERIFIED | Follows from the mechanism |
| B10 | A forgotten fact does not prove the store broke — the search may have missed, or nothing was saved | VERIFIED | The two documented failure directions of retrieval systems |
| BVDT | Short-term = what is in context now; long-term = what you saved and can retrieve | VERIFIED | Recapitulation. Verdict beats recapitulate; they assert nothing new |

## Deliberately excluded (would date the video or overclaim)

No model names or versions. No context-window sizes in tokens — those change and
would date the reel immediately; B05 makes the point structurally ("there is a
ceiling") instead. No vendor or framework named. No retrieval-accuracy figure. No
claim that any particular memory design works well.

## Numbers on screen

The only numerals are the turn labels in B05 (`turn 1`, `turn 2`, `turn 3`, `turn
60`) and the rubric numbering. `turn 60` is illustrative of "a long chat", not a
measured window limit, and no token count appears anywhere.

## Register check

Plain explains and stops; it does not judge the design. Reviewed every line for
Teardown drift: no beat rates statelessness or RAG as a good or bad design choice,
and no beat says what any approach "optimizes for". B10 states failure modes as
mechanism, not as criticism.

## A note on the handoff's third rubric item

BHTF asks the viewer whether they would consent to everything on their save list
being written down. That is a design consideration, not a claim: a memory system
decides what gets recorded about a person, and the honest version of this lesson
names that rather than leaving it implicit.
