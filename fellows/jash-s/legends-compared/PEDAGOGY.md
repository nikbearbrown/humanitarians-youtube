# PEDAGOGY.md — Legends, Compared

## The insight (not just a topic)

"Four athletes get called 'the greatest' — but greatness isn't one mechanism.
It's at least four: a **streak** that can break (Ferguson), a **cumulative total**
still climbing (Ronaldo), a **multi-format career** where some doors are already
closed (Rohit Sharma), and a **fixed peak** frozen at the moment of retirement
(Federer)." The reel's job is to make a viewer able to name which mechanism
they're actually praising, next time they call someone "the greatest."

Measurable outcome: after watching, a viewer should be able to **classify any
"greatest ever" claim into one of the four dominance-shapes**, and name the one
number that would prove or break it.

## Act structure

| Beat | Act | Shape illustrated |
|---|---|---|
| B00 | ASK | cold open — the four-mechanism thesis, as a Claude ask |
| B01 | THESIS | all four named side by side, no numbers yet |
| B02 | FERGUSON | the streak — 12 wins, a hard stretch, a second title |
| B03 | RONALDO | the total — 976 goals, three sources, still climbing |
| B04 | ROHIT SHARMA | the multi-format run — 2 closed doors, 2 open |
| B05 | FEDERER | the frozen peak — 20, now second to 24 |
| B06 | VERDICT | all four shapes named again, with the numbers |
| B07 | HANDOFF | Your Turn — apply the framework to the viewer's own pick |
| B08 | OUTRO | title restate |

ILLUSTRATE LAW check: UI (ClaudeComposerAsk / ClaudeVerdictArtifact /
ClaudeTitleOutro) only at B00, B06, B07, B08 — the beats where the interface
itself is the subject (the ask, the recap artifact, the handoff, the sign-off).
B01–B05 illustrate the *content* (a new component, `DominanceStatBeat`, four
different chart "kinds": thesis / streak / bars / timeline / peak) — no two
consecutive beats reuse the same chart kind.

## Sourcing

Every stat in this beat sheet is logged with its source in `FACTCHECK.md`,
verified 2026-07-30. Per house convention: **a fact-check that doesn't cite
sources is just a second opinion** — same rule this channel used to grade the
ecosystem-wheel debunker.

## Branding note

`brand_labels.json` doesn't have an entry for a sports-comparison series — the
existing `claude` / `claude-liam` kicker ("Computational Skepticism") doesn't
fit this content. This beat sheet uses a new brand key, `claude-liam-legends`.
**Add this line to `runtime/qc/brand_labels.json` before running `./art run`:**

```json
"claude-liam-legends": { "kicker": "Legends, Compared", "chip": "@NikBearBrown" }
```

Without it, GATE L's branding check simply skips (unknown channels aren't
checked) — but adding it keeps the on-screen kicker consistent and correct
rather than leaving it unchecked.

## Build note — one new component required

`DominanceStatBeat` does not exist yet in `runtime/remotion/src/scenes/`. It
needs to render four modes from one flexible schema (`kind`: `thesis` |
`streak` | `bars` | `timeline` | `peak`), matching the `EcosystemWheelBeat`
precedent — cream stage, one Claude accent on the spark line only, the chart
body in its own neutral exhibit palette. Not yet built; do not run `./art run`
until it exists and is registered in `Root.tsx`.

---

VERDICT: PASS
