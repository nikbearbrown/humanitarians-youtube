# CHECKS-REPORT — Suno, Part One.

PROOF GATE exit condition for the beat sheet. Written before the render pass.
Classification per `skills/make/nopunt/SKILL.md` (SHOW / HOLD / CARD).

## Per-beat classification

| Beat | Act | Class | Artifact the beat SHOWS |
|---|---|---|---|
| B00 | cold open | SHOW | Claude composer; ask types, three result lines reveal |
| B01 | BLUF | SHOW | description → model → finished track pipeline, animated waveform + stem strips |
| B02 | how it works | SHOW | genre corpus converging; word→sound waveform pairs; segment-by-segment generation strip; two waveforms from one prompt |
| B03 | signing in | SHOW | four step cards highlighting in narration order, completing with checks |
| B04 | the workspace | SHOW | Suno window; sidebar walked Home→Create→Library→Explore, content pane repopulating per section |
| B05 | Simple mode | SHOW | Create page; tabs, description box typing, Instrumental toggle actuating, Create arming |
| B06 | description formula | SHOW | three ingredient cards resolving into one assembled sentence, fragments tinted to source |
| B07 | generating + cost | SHOW | Create pressed, two slots filling with progressive waveforms, timer, credit ledger deducting |
| B08 | reading the results | SHOW | two song cards playing in turn with live waveforms + playheads; three-dot menu opening |
| BVDT | verdict | CARD | artifact page — the whole procedure, six lines revealing in turn (bookend; CARD is legal here) |
| BHTF | recap + Part 2 tease | SHOW | composer returns; Part 2 question types; three preview lines reveal |
| BOUT | outro | CARD | title restate, handle, subline (bookend; OUTRO LAW) |

**Totals: 10 SHOW / 0 justified-HOLD / 0 PUNT-flagged.** The two CARDs are the
verdict and outro bookends, which the law exempts.

## Teaching-arc checklist

| Item | Status | Where |
|---|---|---|
| FRAMEWORK beat before examples | ✓ | B02 explains the mechanism before any UI is shown |
| WORKED EXAMPLE | ✓ | B06 builds one real description; B05/B07/B08 carry that same example through generation and results |
| FALSIFIABILITY | ✓ | B02 ends on "the same prompt never returns quite the same song twice" — a claim the viewer can test immediately, and B08 makes them test it by comparing the two versions |
| SCAFFOLDED TASK | ✓ | The viewer is told to work along from B00; B08 asks them to play both versions and compare |
| BOOKENDS | ✓ | Cold open (B00) → BLUF (B01) → body → verdict (BVDT) → recap/tease (BHTF) → title outro (BOUT) |
| NO-SOURCE-NO-VERDICT | ✓ | All claims logged in `FACTCHECK.md`; nothing asserted that isn't verified there |

## Deviations from default doctrine (deliberate, author-approved)

1. **HANDOFF LAW — "Your Turn" replaced with a recap + Part 2 tease.** Requested by
   the author. Rationale: this is part 1 of a 3-part internal training series, so the
   second-to-last beat's job is to close the loop and hand to Part 2, not to send the
   viewer off to Claude. The composer beat and typing convention are preserved.
2. **Kicker.** `claude-hai`'s fixed kicker is "Irreducibly Human", which is not this
   series. Registered `claude-hai-lyrical` (kicker "Lyrical Literacy", chip
   "@HumanitariansAI") in `runtime/qc/brand_labels.json` rather than mislabelling the
   reel. GATE L passes.
3. **BOUT underfill.** `ClaudeTitleOutro` is a shared house component used by dozens of
   reels; its sparse poster card is the intended OUTRO LAW look. Not modified. Gate V
   reports it as a MAJOR underfill under `--lenient`; accepted rather than forking a
   shared component for one reel.

## Register check

Audience is HAI Lyrical Literacy volunteers with no music or AI background. Register is
internal training, not promotion. Specifically enforced this pass:

- Pro access is mentioned once (B03), mechanically, as a consequence of signing in with
  Discord. All "free forever / no credit card / free Pro access" framing removed.
- Credit arithmetic (B07) is stated flatly, with no editorialising about generosity.
- The host's name is spoken exactly once, in BOUT.
