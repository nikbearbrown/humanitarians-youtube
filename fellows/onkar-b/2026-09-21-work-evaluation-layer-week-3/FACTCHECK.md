# FACTCHECK.md — hai-liam-evaluation-layer ("Finding Is Not Grading.")

DOUBLE-CHECK LAW: every claim checked before scripting. Source: the author's own
Week 3 script for the Provenance Gatekeeper development log.

| # | Claim (as narrated) | Verdict | Basis | Fix applied |
|---|---|---|---|---|
| 1 | A retrieval match proves a document was found, not that a claim is true | TRUE | Similarity retrieval returns the nearest record; it performs no comparison between the claim's assertion and the record's content. This is the episode's thesis. | Kept, and stated on screen in B00's output lines rather than only in the voice. |
| 2 | Three variance axes: Supported / Magnitude Error / Directional Error | TRUE as a design claim | This is the author's own taxonomy for the Gatekeeper's grader, restated from the script. It is a design decision, not an external standard, and the reel presents it that way ("we grade… against the Variance Matrix"). | Kept. Each axis is shown with a worked claim/truth pair so it is defined by example. |
| 3 | Magnitude Error = right direction, wrong size | TRUE | Matches the script's definition. | Kept. On-screen pair: claim "revenue up 15%" vs truth "revenue up 12%". |
| 4 | Directional Error = right metric, inverted polarity | TRUE | Matches the script's definition. | Kept. On-screen pair: claim "revenue down 12%" vs truth "revenue up 12%". |
| 5 | n8n → FastAPI `/verify` → ChromaDB → strict JSON verdict → n8n | TRUE per the source | The script states each element: an n8n orchestrator, a FastAPI webhook receiving a claim payload, ChromaDB for the real data, and a strict JSON Verification Verdict returned. | Kept, and confined to exactly those elements. No invented middleware, queue, model, or deployment detail. |
| 6 | Near-identical strings: "decreased 12%" vs "growth … 12%" score as highly similar | TRUE directionally | Two sentences differing by one polarity word share almost all tokens, so an embedding-similarity score is high. This is the documented weakness the episode is about. | Kept — **but no numeric score is shown or spoken** (see the metrics note below). |
| 7 | Similarity search "will pass it because the tokens are nearly identical" | TRUE as scoped | Scoped to a naive similarity-threshold check, which is what the script contrasts against. | Kept. The verdict card says similarity *cannot see a sign flip* rather than claiming any specific tool always fails. |
| 8 | Q3 figures (±12%, 15%, doc_01) | ILLUSTRATIVE | Demonstration data from the author's own test fixtures; not a real company's results. | No company is named anywhere; "doc_01" and "test_01" read as fixtures on screen, which is what they are. |
| 9 | "Strict JSON, not prose — the next node branches on a field" | TRUE | Follows from the script's own stated requirement of a structured verdict returned to an orchestrator; branching on a structured field is the reason a workflow tool needs one. | Kept as the reel's design judgment. |

## The metric that is deliberately NOT on screen

The script's Scene 4 does not quote a similarity score, and neither does this
reel. `GatekeeperDirectionalBlindspot`'s own component header states the rule:
a cosine score shown without a source is an invented metric under DOUBLE-CHECK
LAW. So `simValue` is left empty — the bar fills to show "near-identical"
qualitatively, with no number printed and none spoken. An earlier draft of this
beat sheet carried "cosine similarity 0.97" and "similarity 0.94"; both were
removed before any render.

## Stripped to keep the video from dating

- No model names or versions, no embedding-model benchmark claims.
- No throughput, latency, or accuracy statistics.
- No claim that ChromaDB, FastAPI or n8n are the best tools for the job — they
  appear because they are what this project uses.

## Register check

The source is the author's own script, rewritten rather than parroted: B00 was
re-pointed so the narrator does not claim to be the author (BUILD-LOG deviation
1), the body beats were rewritten to react to what is on screen, and the
judgment lines ("you cannot branch on a sentence"; "it is being graded, not
consulted") are additions in register.
