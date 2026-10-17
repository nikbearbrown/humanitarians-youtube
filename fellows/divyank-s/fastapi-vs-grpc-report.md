# Report: Claude, Dispatched. — FastAPI vs gRPC, Two Cuts

**Topic:** FastAPI vs gRPC — architecture, why real systems run both, use cases (incl. IoT), honest tradeoffs
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/fellows/divyank-s/2026-10-04-fastapi-vs-grpc/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-fastapi-vs-grpc.mp4` | `short/claude-liam-fastapi-vs-grpc-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 394.75s (6:34.8) | 161.9s (2:41.9) |
| **Beats** | 32 | 12 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | derived from the signed-off parent; outro narration hand-rewritten and regenerated |
| **Signed** | "Liam, in for Divyank" / `@DivyankSingh` throughout, including the outro card | same |

Both are real, rendered, playable files. Neither is published or authorized for publication.

## 2. The requested points, and where each is covered

No single source document underlies this reel — the content is general,
stable, publicly-documented API-architecture practice, deliberately kept
free of version numbers, benchmark percentages, and named third-party
product claims (see `FACTCHECK.md`). The requested points are grouped into
4 acts:

| Act | Content | Beats |
|---|---|---|
| **I — Two Answers to One Question** | What RPC actually means; FastAPI (Starlette + Pydantic, HTTP/1.1 + JSON) vs. gRPC (HTTP/2 + protobuf); readable-vs-compact, one-request-per-connection-vs-multiplexed | `A1-1`–`A1-6` |
| **II — Why You'd Run Both** | The gateway/BFF pattern — the real answer to "why two API services"; one request living two lives (browser-facing JSON, internal protobuf); one-API-vs-split as division of labor, not duplication | `A2-1`–`A2-6` |
| **III — What Each One Is Actually For** | FastAPI's documentation/readability/universal-compatibility strengths; gRPC's compact-payload/persistent-connection strengths; explicit IoT rationale (battery/bandwidth cost of repeated JSON field names); the four gRPC interaction patterns and streaming as REST's structural gap | `A3-1`–`A3-6` |
| **IV — The Tradeoffs Nobody Mentions** | The browser-can't-speak-gRPC-natively gap (gRPC-Web + proxy requirement); the symmetric debuggability-vs-performance tradeoff, stated in both directions; "pick one, everywhere" and its honest cost either way | `A4-1`–`A4-6` |

On screen, specifically:

- **Application / architecture** (`A1-2`, `A1-3`, `A1-5`): Starlette +
  Pydantic vs. HTTP/2 + protobuf, laid out as the same RPC problem solved
  with opposite commitments — readable/loosely-typed vs.
  compact/strictly-typed.
- **Need for two API services** (`A2-1`, `A2-2`, `A2-5`): the gateway
  standing between a JSON-only browser and a protobuf-only internal fleet,
  and the explicit "one API pays the tax either way" framing for why
  splitting is division of labor, not redundancy.
- **Purpose / IoT** (`A3-1`): a constrained, battery-powered device paying
  a real per-byte cost for repeated JSON field names — stated as a
  property of the architecture, not a specific product claim.
- **Volunteered beyond the ask** (per the open invitation to go
  research-centric): the four gRPC interaction patterns and bidirectional
  streaming as a gap REST never had natively (`A3-3`, `A3-5`); the
  gRPC-Web + proxy requirement as a named limitation most surface-level
  comparisons omit (`A4-2`); the debuggability tradeoff stated
  symmetrically in both directions rather than favoring either framework
  (`A4-3`, `A4-5`).

## 3. Sourcing and fact-check method

Per `FACTCHECK.md`, every claim is kept at the level of **stable, publicly
documented mechanism** — protocol, payload format, connection model,
interaction pattern — and explicitly excludes version numbers, benchmark
percentages, pricing, and unverified third-party product claims, since
none of those were sourced or verified for this build and would date the
video.

## 4. The archival imagery — used as metaphor, not evidence

The topic has no historical photographic referent, so all 5 real
Wikimedia Commons stills (public domain or CC-licensed) illustrate a
CONCEPT, never the technologies themselves:

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | Vintage telephone switchboard | the remote-procedure-call problem, generically |
| A1-4 | 1908 postcard | the readability of a plain-text format |
| A2-1 | Translators at work | a gateway translating between two protocols |
| A3-1 | Raspberry Pi Pico 2 / RP2350 microcontroller, macro photo | a constrained IoT device |
| A4-1 | 1917 Russian wax seal | a sealed, strictly-formatted binary protocol |

## 5. Building the two aspect ratios

Signed for Divyank from the first draft (`@DivyankSingh`, "in for Divyank"
throughout) — no retrofit needed, unlike the earliest builds this session.

Portrait coverage was planned into the beat sheet up front: one
`BinaryBranch`/`DivergentFates` hero beat per act (`A1-5`, `A2-3`, `A2-5`,
`A4-3`, `A4-4`). As with every prior Short this session, `shorts.py`'s
auto cap-check needed manual correction. The first manual plan (keeping
all 5 VOX stills, all 5 hero beats, and the 50.5s verdict artifact) still
landed at 182.3s — over the 3:00 cap — so the verdict beat (`BVDT`) and
the act-4 VOX still (`A4-1`) were dropped in favor of keeping all 5
mechanism hero beats intact. Final plan: 12 beats, 161.9s, zero `ONDA
CHECK` blocks. The recurring auto-rewritten-outro bug (raw narration
fragments stitched into a broken sentence) appeared again and was
hand-fixed before its audio was generated.

## 6. A toolkit bug found and fixed during this build

The outro title card's handle (`ClaudeTitleOutro` / `ClaudeTitleOutro916`)
was **hardcoded** to `@NikBearBrown` by `OUTRO-LOCK.md`, with no `handle`
field in the component's prop schema at all — meaning every beat sheet's
`"handle": "@DivyankSingh"` was silently ignored, and the rendered outro
card actually showed `@NikBearBrown` despite the JSON being correct. This
affected every build this session, confirmed visually via this build's
QC contact sheet before the fix.

Fixed by adding an optional `handle` prop to both components (default
unchanged — every other reel in the toolkit still renders
`@NikBearBrown` unless it explicitly opts in), then re-rendering and
recompiling just the `BOUT` beat for both the 16:9 master and the 9:16
Short. Confirmed visually afterward: the outro card now reads
`@DivyankSingh`. The five earlier builds this session
(llm-as-a-judge, chapter-4, vector-databases, chapter-5,
gcp-cicd-deployment) still carry the old, incorrect outro and were not
revisited as part of this build.

## 7. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement).
- **`shorts.py`'s auto-planner still has no concept of portrait-composition
  support or of the verdict beat's outsized duration** — manual `--drop`
  overrides were required twice in this build alone before the Short fit
  the cap.
- **Neither video is published or authorized for publication.**
