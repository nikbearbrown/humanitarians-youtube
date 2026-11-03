# PEDAGOGY — What Vector Databases Do That SQL Cannot (ai-explainer, narrated by Anjana)

Fresh build from the pre-authored `narration/*.txt` + `visuals/*.md` briefs in
this folder. One insight: "similar" is not a weaker version of "equals". It is a
different shape of question, and answering it needs meaning stored as position,
queries expressed as points, and an index that deliberately gives up exactness
to stay fast.

**Sibling to `embeddings-explainer`.** That video is about what a vector *is*;
this one is about what you do with a few million of them. They share the
palette and the way vector space is drawn, on purpose — B02's scatter is meant
to be recognised by anyone who watched the other one.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B06 (verdict) / B07 (handoff) /
  B08 (outro). B01–B05 illustrate the mechanism — the SQL query that cannot be
  written, the space records are stored in, the ranked query, the brute-force vs
  graph comparison, the four use cases ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence (the
  `???` where an operator should be, the two clusters and the distance between
  them, the rings arriving at dots in rank order, 1,000,000 against 47) lives on
  screen ✓
- your-turn closing standard: B06 VERDICT → B07 YOUR TURN → B08 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source `beats.json` says `am_onyx` —
  overridden to `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B05 on the dark ground, same PEDAGOGY-approved
  deviation as the ECIS episodes and the other standalones.
- **NARRATION BUDGET:** body beats run 47–86 words. B04 (86) is over the 45–70
  range — logged as a deviation below.

## Three authoring decisions

**1. Palette — channel dark-stage values, per the established precedent.** The
briefs list their own hexes (`#1A1A2E` navy ground, `#4A90D9`, `#E74C3C`,
`#F1C40F`, `#27AE60`). Every one of those *roles* is preserved and rendered in
the channel's values, the same resolution the author confirmed for
`embeddings-explainer` and for ECIS Episodes 7–8. Ground `#0a0a0f`, vectors and
SQL-side blue `#3E7CB1`, query gold `#D4A853`, success green `#4A9C6D`, failure
red `#C0392B`, muted grey `#7F8C8D`.

**2. The B02 cluster colors were remapped — and this one is not cosmetic.** The
briefs assign **blue** to the positive-sentiment cluster and red to the negative
one. That collides twice: blue is the sibling video's color for *a vector*, and
the sibling already established green-positive / red-negative for exactly this
kind of scatter. Rendering a positive cluster in blue here would mean blue
signified "embedding" in one video and "good news" in the next.

Resolved: **green for the positive cluster, red for the negative one**, with
blue kept for vectors and SQL-side material. The briefs' actual requirement —
two clusters that are visibly, immediately different — is fully met, and the two
standalone videos now agree with each other. Logged because it is a deliberate
departure from a brief's stated color, not an oversight.

**3. B05 was labelled "Your Turn" but is not one.** Same mismatch as the
sibling's B05 and ECIS Episodes 7 and 8: the narration is a close ("…vectors are
the right storage. Anjana here, thanks for watching") and the brief is a use-case
montage plus a title card. Built as the close. A real your-turn handoff with a
pasteable prompt was added at B07 per HANDOFF LAW, and the sign-off moved to B08
where this series always puts it.

## Narration budget deviation

**B04 (Making It Fast) runs 86 words.** It is the only beat that has to do a
full before-and-after *and* explain a mechanism: why brute force fails (a
million vectors, a million comparisons), what the fix is called, and then the
actual walk — enter anywhere, hop to the closest neighbour, repeat. Cutting the
walk would leave "approximate nearest-neighbor index" as a name with nothing
behind it, which is the opposite of what this toolkit is for. The visual is
correspondingly the episode's longest build: a split screen where the right-hand
side animates four hops.

## Evidence discipline (DOUBLE-CHECK LAW)

This video makes no claims about a proprietary system. Every statement is about
how vector databases work in general, checkable against published documentation
rather than against something only the author can confirm.

### Claims about how the technology works

| Claim (as scripted) | Where | Status |
|---|---|---|
| SQL has no operator for "similar to this" | B01 | ☑ true of standard SQL; see the honesty note below |
| Records are stored as embeddings — position encodes meaning | B02 | ☑ standard |
| Anything embeddable (text, image, audio) becomes a point in the same kind of space | B02 | ☑ standard |
| A query is a vector; results are ranked by distance rather than filtered by a condition | B03 | ☑ standard |
| Cosine similarity measures the angle between two vectors; smaller angle, higher similarity | B03 | ☑ standard — and it is the angle, not the magnitude, which is why the inset draws the angle |
| Exhaustive search is O(n) per query — a million vectors, a million distance calculations | B04 | ☑ standard |
| ANN indexes trade exactness for speed | B04 | ☑ standard |
| One common approach is a neighbour graph, searched by entering somewhere and hopping to closer neighbours | B04 | ☑ standard — this is the HNSW family, described without naming it in narration; the visual labels it |

### Illustrative placeholders

| Figure | Where | Status |
|---|---|---|
| The `products` table and its three result rows | B01 | ☑ illustrative |
| The six sentence snippets in the two clusters | B02, B03 | ☑ illustrative — generic financial phrasing, no company named |
| "768 numbers" | B02 | ☑ illustrative — a real and common width, used as a concrete number rather than a claim about a specific model. Deliberately the same figure the sibling video uses. |
| Similarity scores 0.94 / 0.89 / 0.83 | B03 | ☑ illustrative — plausible cosine scores in rank order, not computed |
| "1,000,000 comparisons" vs the graph's count | B04 | ☑ the million is exact by construction (one comparison per vector). The graph-side number is **not** the briefs' hand-typed 47 — it is computed from the walk actually drawn on screen (neighbours examined at each hop), so the number and the picture cannot disagree. It lands at 40, which is what "a few dozen" looks like. |
| The 2D scatter itself | B02, B03, B04 | ☑ illustrative — a real embedding space has hundreds of dimensions and any 2D picture is a lossy projection, same simplification logged in the sibling video |

**One honesty note on B01.** "SQL has no operator for similar" is true of
standard SQL and is the right thing to say in a 17-second beat, but Postgres
with `pgvector` does give you a distance operator, and several engines now ship
vector types. The claim the video is actually making is about the *relational
model* — rows matching a predicate — not about which product you can install an
extension into. Kept as scripted because the distinction would cost more than it
teaches here, and because the extension case proves the point rather than
undermining it: what it adds is precisely a vector index.

## Friction protected

- Kept: the second query in B01 stopping dead at the operator. It would be
  faster to narrate "SQL can't do similarity" over a static frame; watching a
  query fail to be writable is the whole hook.
- Kept: the red cluster staying visible and dim inside the outer ring in B03. Leaving it there is what shows that nothing was
  *excluded* — it just ranked low, which is the difference between ranking and
  filtering.
- Kept: the angle inset in B03. "Cosine similarity" is otherwise a name for a
  number the viewer has no picture of.
- Kept: the hops in B04 animating one at a time. The count (dozens vs a
  million) is the headline, but the hops are the explanation.
- Kept: the walk being a *real* greedy search over the generated graph rather
  than a drawn polyline. The first version used a 3-nearest-neighbour graph and
  the search stalled in a local minimum, walking away from the target — caught
  in frame QC. Fixed by raising the graph to 5 neighbours and letting the walk
  run until no neighbour improves, which is what the narration describes. It
  now takes 6 hops, and the beat says 6 rather than rounding to the briefs'
  four, because the drawn walk is the source of truth.

## Sign-off notes

1. No proprietary claims; the evidence table splits general-technology facts
   from illustrative placeholders, and the one over-claim risk (B01) is argued
   above rather than quietly kept.
2. Palette follows the precedent the author set for the sibling video; the B02
   cluster remap is logged with its reasoning.
3. The B05 relabel and the moved sign-off line are the only edits to source
   narration.
4. B04's narration-budget deviation is argued above rather than waived.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
