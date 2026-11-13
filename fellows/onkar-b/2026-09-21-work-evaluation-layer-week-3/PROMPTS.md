# PROMPTS.md — hai-liam-evaluation-layer

Beat-prefixed. On-screen strings must match the render exactly.

## On-screen prompts

**B00 — the cold-open ask (the gap the episode closes)**

```
RETRIEVAL MATCH: "doc_01" — does that prove the claim is true?
```

Output lines, on screen:

```
MATCH: doc_01 · ledger row retrieved.
That is a search result, not a verdict.
Nothing in this step compared the claim against the ledger.
```

**B03 — the ask half of the ask→result pair**

```
Show the claim payload n8n posts in, beside the strict JSON verdict the Gatekeeper returns.
```

**B07 — the handoff (HANDOFF LAW: read aloud verbatim, then discussed)**

```
curl -X POST "http://localhost:8000/verify" -d '{"claim_id": "test_01", "generated_claim": "Q3 Revenue decreased 15%"}'
```

Expected response shown as output:

```
{"axis": "DIRECTIONAL_ERROR", "claim": -15, "truth": +12}
— inspect the JSON verdict: the axis, and the two figures it was graded on.
```

Why this earns the handoff slot: it is the author's own audit command, it runs
against the viewer's local server in one request, and it is falsifiable — the
narration tells the viewer exactly which axis should come back and what a wrong
answer would mean about their grader.

## Component props — no generation prompts this build

Every body visual is an existing Provenance Gatekeeper component driven by
props. Nothing was generated, so there are no image or video prompts to log.

| Beat | Component | Content supplied as props |
|---|---|---|
| B02 | `GatekeeperTaxonomy` | three `classes` rows: index, name, rule, claim, truth |
| B04 | `GatekeeperVerifyLoop` | four `nodes` (n8n → FastAPI → ChromaDB → VERDICT), the claim `payload`, and the retrieved `contextLine` |
| B05 | `GatekeeperDirectionalBlindspot` | claim/ledger text with the two hot words, similarity bar (no figure), verdict + sub |
| B06 | `GatekeeperScoreboard` | four `rows` + `finalKey`/`finalValue` |
| B08 | `HaiTitleOutro` | title, handle, credit line |

## Prompts NOT used

No image generation, no AI video, no pantry shopping list, no Higgsfield. The
whole reel is deterministic code plus local Kokoro narration.
